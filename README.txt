Project: Gait Analysis System using Dynamic Time Warping (DTW)
Course: SBEG 207 - Biomedical Engineering
Team: 11

------------------------------------------------------------------
OVERVIEW
------------------------------------------------------------------
This software allows clinicians to objectively assess gait asymmetry by comparing 
a patient's walking signal to a healthy reference using Dynamic Time Warping (DTW).
It aligns non-linear signals, calculates a similarity score, and visualizes the 
optimal warping path.

------------------------------------------------------------------
FILE STRUCTURE
------------------------------------------------------------------
1. main_gui_tkinter.py  : The Graphical User Interface (Frontend). Run this file.
2. dtw_logic.py         : The mathematical backend (DP Algorithm & Data Generation).
3. README.txt           : This instruction file.

------------------------------------------------------------------
PREREQUISITES & INSTALLATION
------------------------------------------------------------------
You need Python installed (version 3.8+ recommended).
The project requires the following external libraries:

   pip install numpy matplotlib

(Note: 'tkinter' is included with standard Python installations. If you get an error, 
ensure your Python installation includes tcl/tk support).

------------------------------------------------------------------
HOW TO RUN
------------------------------------------------------------------
1. Unzip the project folder "Team_11_Gait_Project".
2. Open a terminal or command prompt inside this folder.
3. Run the following command:

   python main_gui_tkinter.py

------------------------------------------------------------------
FEATURES & USAGE
------------------------------------------------------------------
1. Select Patient Case:
   - Case 1 (Healthy): Baseline match (Score ~3.5).
   - Case 2 (Bradykinesia/Slow): Simulates a patient walking 40% slower.
   - Case 3 (Ataxia/Severe): Simulates chaotic/irregular gait.
   - Case 4 (Tremor - BONUS): Simulates Parkinsonian high-frequency noise.

2. Visualizations:
   - Top Plot: Shows the signal alignment. Gray dashed lines indicate the 
     warping (matching) points.
   - Bottom Plot: Heatmap of the DP Cost Matrix. The RED line is the 
     optimal backtracking path.

3. Advanced Tools:
   - "View DP Matrix (Numbers)": Opens a popup window showing the actual 
     numerical construction of the DP table (first 15x15 cells).
   - "Animate Alignment": Dynamically draws the red backtracking path to 
     demonstrate the algorithm's decision process step-by-step.

4. Stability Check:
   - "Run Stress Test": Generates 1,000+ data points to verify the O(NM) 
     complexity handles large datasets without crashing.

------------------------------------------------------------------
TROUBLESHOOTING
------------------------------------------------------------------
- If the graph text is too small, try resizing the window.
- If you encounter backend errors, this version uses Tkinter (instead of PyQt5)
  to ensure maximum compatibility with Windows/Mac/Linux environments.