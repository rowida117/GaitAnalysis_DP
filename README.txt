Gait Analysis System using Dynamic Time Warping

Course: SBEG 207

--- HOW TO RUN ---
1. Prerequisites:
   Ensure you have Python installed.
   Install the required libraries by running:
   pip install numpy matplotlib

2. Execution:
   Run the main application file:
   python main_gui.py

3. Usage:
   - The GUI will launch automatically.
   - Click "Case 1", "Case 2", "Case 3", or "Case 4" to visualize different patient scenarios.
   - The top graph shows the signal alignment (Gray lines show the warping).
   - The bottom graph shows the DP Cost Matrix and the optimal path (Red line).
   - The button "View DP Matrix" to show the first 15*15 sample of the dp matrix
   - Click "Run Stress Test" to verify the algorithm performance on large datasets.
   -Click "Animate Alignment" to show how the red line be done in the matrix 

--- FILES ---
1. main_gui.py: The frontend application (GUI).
2. dtw_logic.py: The backend containing the DP algorithm and data generation.