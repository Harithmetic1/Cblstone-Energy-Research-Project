import math
import time
import random
import matplotlib.pyplot as plt
from collections import deque
import statistics

class AnomalyDetector:
    '''
        This script is for the assessment program of the graduate software engineer role at cobblestone energy
        Author: Harith Oluwatosin Onigemo

        Find the description and objectives of the program below

        Project Title:
        Efficient Data Stream Anomaly Detection

        Project Description:
        Your task is to develop a Python script capable of detecting anomalies in a continuous data stream. This stream, simulating real-time sequences of floating-point numbers, could represent various metrics such as financial transactions or system metrics. Your focus will be on identifying unusual patterns, such as exceptionally high values or deviations from the norm.

        Objectives
        Algorithm Selection: Starting out with the Z-score Algorithm 
        Data Stream Simulation: A function to emulate data stream, incorporating regular patterns, seasonal elements and random noise for realism
        Anomaly Detection: The primary mechanism used for accurately flagging anomalies is the Z-score Method Algorithm. This method is simple to understand and can be adapted easily to different data streams
        Optimization: The algorithm utilises a moving window to allow incremental calculation of small data ranges
        Visualization: The continuous stream of data and anomalies are visualized using mathplotlib plot and scatter functions.

        Find out a more concise explanation of the anomaly detection method in the doc linked below
        https://docs.google.com/document/d/1QqFAGUfCa50SOAlNtDnRtBg3BDeG9I636a_a2sisc70/edit?usp=sharing
    '''

    def __init__(self) -> None:
        self.anomaly_rate = 0.95
        self.z_score_threshold = 3
        self.detected_anomalies = 0
        

    def main(self):
        try:
            self.visualise_stream()
        except Exception as e:
            print(f"An error as occured: {e}")
            plt.close()
            return


    def data_stream(self):
        while True:
            try: 
                current_time = time.time()
                base_pattern = math.sin(current_time) # Use the current time to simulate seasonality
                noise = random.uniform(-0.1, 0.1)  # Generate random noise to attach to the stream
                if random.random() > self.anomaly_rate:  # uses a 5% chance to generate an anomaly, can be adjusted as requested
                    yield base_pattern * 5 + noise 
                else: 
                    yield base_pattern + noise
                time.sleep(0.1) # generate a stream data every 100 ms
            except Exception as e: # Handle cases where stream value is missing
                print(f"Error getting stream data: {e} \nSkipping missing value")


    def detect_anomaly(self, data, window = 50):
        '''Uses a double ended queue to implement a sliding window, 
        the sliding window will allow this function to detect anomalies within a certain period
        thereby allowing the algorithm adapt to concept drift (changing trends)'''
        buffer = deque(maxlen=window) 
        anomalies = []

        for value in data:
            if len(buffer) >= window: # wait for one period before calculating anomalies
                mean = statistics.mean(buffer) # mean calculated incrementally
                std_dev = statistics.stdev(buffer) # standard deviation calculated incrementally
                z_score = (value - mean) / std_dev if std_dev > 0 else 0 # z score calculation with error handling for division by zero

                print(f"Z_score: {z_score}")
                if abs(z_score) > self.z_score_threshold: # the threshold is set at 3 standard deviations, about 0.3% of the window should be an anomaly
                    anomalies.append(value)
                
            buffer.append(value)
            yield value, anomalies

    def visualise_stream(self):
        plt.ion()
        fig, ax = plt.subplots()
        data_points = []
        anomalies = []
        received_values = 0
        anomaly_abscissa = []
        for value, anomaly in self.detect_anomaly(self.data_stream()):
            data_points.append(value)
            received_values += 1 if value else 0
            anomaly_length = len(anomaly)
            anomalies.append(anomaly[-1] if anomaly else None)
            print(f"Anomalies: {anomalies[-1]}, anomaly length: {anomaly_length}, detected anomalies: {self.detected_anomalies}")

            ax.clear()
            ax.plot(data_points, label = "Data Stream")
            if(self.detected_anomalies < len(anomaly)): # This will allow the plot to properly place the anomalies
                anomaly_abscissa.append(received_values)
            ax.scatter(anomaly_abscissa, anomaly, color = "red", label="Anomalies")
            ax.legend()
            plt.pause(0.05)
            self.detected_anomalies = anomaly_length # Update the number of anomalies detected


detect_anomaly = AnomalyDetector()
print(AnomalyDetector.__doc__)

detect_anomaly.main()

        