# 🚶‍♂️ Gait Analysis System using Dynamic Time Warping (DTW)

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Completed-success)]()
[![Course](https://img.shields.io/badge/Course-SBEG%20207-green)](https://github.com/)

A biomedical engineering tool designed to objectively assess gait asymmetry and rehabilitation progress. This system compares a patient's walking signal to a healthy reference using **Dynamic Time Warping (DTW)**, allowing for accurate similarity scoring even when the patient walks slower or with irregular timing.

---

## 📋 Table of Contents
- [Project Overview](#-project-overview)
- [Biomedical Context](#-biomedical-context)
- [Key Features](#-key-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [Algorithm Details](#-algorithm-details)
- [Project Structure](#-project-structure)
- [Team Members](#-team-members)

---

## 🏥 Project Overview
In physical therapy (e.g., post-stroke rehabilitation), patients often regain movement patterns but lack the correct rhythm or speed. Standard "Euclidean Distance" metrics fail to accurately score these patients because their gait cycles are temporally misaligned with healthy references.

**This project solves that problem by:**
1.  **Simulating** various pathological gait patterns (Bradykinesia, Ataxia, Tremors).
2.  **Aligning** the signals non-linearly using the **Needleman-Wunsch / DTW algorithm**.
3.  **Visualizing** the specific areas of mismatch (time-warping) to help clinicians diagnose issues.

---

## 🧬 Biomedical Context
We simulate and analyze four distinct clinical scenarios:

| Case | Condition | Biological Signal Characteristics |
| :--- | :--- | :--- |
| **1. Healthy Control** | Normal | Smooth sine wave, matches reference speed ($Score \approx 3.5$). |
| **2. Bradykinesia** | Slow Walking | Lower amplitude, 40% longer duration. Represents stroke/muscle atrophy ($Score \approx 9.0$). |
| **3. Ataxia** | Severe Irregularity | Phase shifts, erratic steps, chaos. Represents cerebellar damage ($Score \approx 40$). |
| **4. Resting Tremor** | Parkinson's | Normal speed but superimposed high-frequency (4-6Hz) noise. |

---

## ✨ Key Features
* **Interactive GUI:** Built with `Tkinter` for universal compatibility.
* **Real-time Visualization:** * **Signal Alignment Plot:** Shows exactly how patient peaks map to healthy peaks.
    * **DTW Heatmap:** A color-coded cost matrix showing the "Energy Landscape" of the alignment.
* **Path Backtracking:** Visualizes the optimal warping path (Red Line).
* **Step-by-Step Animation:** Watch the algorithm find the optimal path in real-time.
* **Matrix Inspector:** A popup window that displays the raw numerical values of the DP table for debugging/education.
* **Stress Testing:** Verifies algorithm stability with $N=1000+$ data points.

---

## ⚙️ Installation

### Prerequisites
* Python 3.8 or higher.

### Install Dependencies
Run the following command to install the required libraries:

```bash
pip install numpy matplotlib
