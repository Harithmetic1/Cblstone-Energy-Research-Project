# Efficient Data Stream Anomaly Detection

**Author**: Harith Oluwatosin Onigemo  
**Purpose**: Submission for Graduate Software Engineer assessment at Cobblestone Energy.

---

## Project Overview

This project involves the development of a Python script capable of detecting anomalies in a continuous, real-time data stream. The simulated data stream represents various real-world metrics, such as financial transactions or system performance metrics, where anomalies may indicate significant events or irregularities.

---

## Project Objectives

### 1. Algorithm Selection

The Z-score algorithm is used initially to identify anomalies, with plans to potentially migrate to an Exponential Weighted Moving Average (EWMA) method for improved performance in cases of concept drift and gradual trend changes.

### 2. Data Stream Simulation

A custom function simulates a real-time data stream with regular patterns, seasonal variations, and random noise, providing a realistic testbed for the anomaly detection algorithm.

### 3. Anomaly Detection

The Z-score method, known for its simplicity and adaptability, serves as the primary mechanism for flagging anomalies in the data stream. Anomalies are identified based on deviations from a moving window mean and standard deviation.

### 4. Optimization

The algorithm leverages a sliding window approach for efficient, incremental calculations, enabling anomaly detection without processing delays.

### 5. Visualization

Real-time data and detected anomalies are visualized using Matplotlib, with plots for the continuous data stream and scatter points marking anomalies for easy interpretation.

---

## Further Details

A comprehensive explanation of the Z-score anomaly detection method, along with potential adaptations, can be found in the [documentation here](https://docs.google.com/document/d/1QqFAGUfCa50SOAlNtDnRtBg3BDeG9I636a_a2sisc70/edit?usp=sharing).

---
