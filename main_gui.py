import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt  # Needed for style reset

from dtw_logic import GaitAnalysisLogic

# --- CONFIGURATION ---
THEME_COLOR = "#2C3E50"  # Dark Blue-Grey Background
TEXT_COLOR = "#ECF0F1"  # White Text


class DPTablePopup:
    """ Popup window for numerical table """

    def __init__(self, parent, matrix, path):
        top = tk.Toplevel(parent)
        top.title("DP Table Construction (First 15x15)")
        top.geometry("900x600")

        frame = ttk.Frame(top)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        v_scroll = ttk.Scrollbar(frame, orient=tk.VERTICAL)
        h_scroll = ttk.Scrollbar(frame, orient=tk.HORIZONTAL)

        limit = 15
        columns = [str(i) for i in range(limit + 1)]
        tree = ttk.Treeview(frame, columns=columns, show="headings",
                            yscrollcommand=v_scroll.set, xscrollcommand=h_scroll.set, height=20)

        v_scroll.config(command=tree.yview)
        h_scroll.config(command=tree.xview)
        v_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        h_scroll.pack(side=tk.BOTTOM, fill=tk.X)
        tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        for col in columns:
            tree.heading(col, text=f"P{col}" if col != '0' else "Ref")
            tree.column(col, width=50, anchor=tk.CENTER)

        path_set = set(path)
        for i in range(min(limit + 1, matrix.shape[0])):
            row_values = []
            for j in range(min(limit + 1, matrix.shape[1])):
                val = matrix[i, j]
                str_val = "∞" if np.isinf(val) else f"{val:.1f}"
                if (i - 1, j - 1) in path_set:
                    str_val = f"[{str_val}]"
                row_values.append(str_val)
            tree.insert("", tk.END, values=row_values)


class GaitApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Biomedical Gait Analysis (Team Project)")
        self.root.geometry("1280x850")
        self.root.configure(bg=THEME_COLOR)

        self.logic = GaitAnalysisLogic()
        self.current_matrix = None
        self.current_path = None
        self.h_sig = None
        self.p_sig = None

        # Reset Matplotlib to default style (White background)
        plt.style.use('default')

        # --- LAYOUT ---
        main_container = ttk.Frame(root)
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Content Area
        content_area = tk.Frame(main_container, bg=THEME_COLOR)
        content_area.pack(fill=tk.BOTH, expand=True)

        # 1. CONTROLS (Left)
        controls = tk.LabelFrame(content_area, text=" Patient Cases ", bg=THEME_COLOR, fg=TEXT_COLOR,
                                 font=("Arial", 12, "bold"))
        controls.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 15), ipadx=10, ipady=10)

        # Buttons
        self.create_btn(controls, "Case 1: Healthy Control", "match")
        self.create_btn(controls, "Case 2: Bradykinesia (Slow)", "slow")
        self.create_btn(controls, "Case 3: Severe Ataxia", "severe")
        self.create_btn(controls, "Case 4: Tremor (Parkinson's)", "tremor")  # NEW BUTTON

        tk.Frame(controls, height=2, bg="white").pack(fill=tk.X, pady=15)

        tk.Button(controls, text="View DP Matrix (Numbers)", command=self.show_table, bg="#3498DB", fg="white",
                  font=("Arial", 10, "bold")).pack(fill=tk.X, pady=5)

        # ANIMATION BUTTON
        self.btn_anim = tk.Button(controls, text="▶ Animate Alignment", command=self.animate_path, bg="#2ECC71",
                                  fg="white", font=("Arial", 10, "bold"), state=tk.DISABLED)
        self.btn_anim.pack(fill=tk.X, pady=5)

        tk.Frame(controls, height=2, bg="white").pack(fill=tk.X, pady=15)
        tk.Button(controls, text="⚠️ Run Stress Test", command=self.stress, bg="#E74C3C", fg="white").pack(fill=tk.X,
                                                                                                           pady=5)

        # Status Label
        self.lbl_status = tk.Label(controls, text="System Ready", bg=THEME_COLOR, fg="#BDC3C7", wraplength=200,
                                   justify="left")
        self.lbl_status.pack(pady=20)

        self.lbl_score = tk.Label(controls, text="Score: --", bg=THEME_COLOR, fg="white", font=("Arial", 16, "bold"))
        self.lbl_score.pack()

        # 2. VISUALIZATION (Right)
        # Standard white figure
        self.fig = Figure(figsize=(8, 8), dpi=100, facecolor='white')
        self.canvas = FigureCanvasTkAgg(self.fig, master=content_area)
        self.canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Initialize subplots
        self.ax1 = self.fig.add_subplot(211)
        self.ax2 = self.fig.add_subplot(212)
        self.fig.tight_layout(pad=3.0)

    def create_btn(self, parent, text, case):
        btn = tk.Button(parent, text=text, command=lambda: self.run(case), bg="#ECF0F1", fg="#2C3E50",
                        font=("Arial", 10))
        btn.pack(fill=tk.X, pady=5)

    def run(self, case):
        try:
            self.h_sig, self.p_sig = self.logic.generate_data(case)
            self.current_matrix, self.current_path = self.logic.compute_dtw(self.h_sig, self.p_sig)
            score = self.current_matrix[-1, -1]

            self.lbl_status.config(text=f"Loaded: {case.upper()}")
            self.lbl_score.config(text=f"Score: {score:.2f}")
            self.btn_anim.config(state=tk.NORMAL)

            self.plot_static()  # Draw the normal static plots

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def plot_static(self):
        self.ax1.clear()
        self.ax2.clear()

        # Plot 1: Signal Alignment (Standard Colors: Green/Orange)
        offset = 3
        self.ax1.set_title("Biomedical Signal Alignment")
        self.ax1.plot(self.h_sig, color='green', label='Healthy')
        self.ax1.plot(self.p_sig + offset, color='orange', label='Patient')

        for idx in self.current_path[::5]:
            self.ax1.plot([idx[0], idx[1]], [self.h_sig[idx[0]], self.p_sig[idx[1]] + offset],
                          color='gray', alpha=0.3, linestyle='--')
        self.ax1.legend()

        # Plot 2: Heatmap
        self.ax2.set_title("DTW Cost Matrix & Optimal Path")
        self.cax = self.ax2.imshow(self.current_matrix[1:, 1:], origin='lower', cmap='viridis', aspect='auto')

        path_x = [p[1] for p in self.current_path]
        path_y = [p[0] for p in self.current_path]
        self.ax2.plot(path_x, path_y, color='red', linewidth=2)

        self.canvas.draw()

    def animate_path(self):
        """ Dynamically draws the red line to show the algorithm working """
        if self.current_path is None: return

        # Clear the red line only
        self.plot_static()
        # Remove the full red line so we can draw it piece by piece
        self.ax2.lines[-1].remove()
        self.canvas.draw()

        # Animation Loop
        path_x = [p[1] for p in self.current_path]
        path_y = [p[0] for p in self.current_path]

        # We draw chunks of 5 points to make it faster
        step_size = 5
        for i in range(0, len(path_x), step_size):
            # Draw segment
            self.ax2.plot(path_x[:i], path_y[:i], color='red', linewidth=2)
            self.canvas.draw()
            self.canvas.flush_events()  # Force update

        # Ensure full line is drawn at end
        self.ax2.plot(path_x, path_y, color='red', linewidth=2)
        self.canvas.draw()

    def show_table(self):
        if self.current_matrix is not None:
            DPTablePopup(self.root, self.current_matrix, self.current_path)

    def stress(self):
        if self.logic.stress_test():
            messagebox.showinfo("Success", "Stress test passed!")
        else:
            messagebox.showwarning("Fail", "Stress test failed")


if __name__ == "__main__":
    root = tk.Tk()
    app = GaitApp(root)
    root.mainloop()