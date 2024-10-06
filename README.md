## Parking Lot Management System 
This project is a Parking Lot Management System developed in Python. It utilizes OpenCV, Pickle, NumPy, and CVZone libraries to monitor parking space occupancy in real-time.

# Table of Contents
-Introduction
-Features

# Introduction
The Parking Lot Management System captures a screenshot of the parking space and uses a tool called parkingSpacePicker to identify and store the locations of available parking spaces in a file. This file is then utilized to process video feeds, allowing the system to determine whether each space is occupied or available. The system employs adaptive thresholding and blurring techniques to enhance the accuracy of the detection results.

# Features
Real-time monitoring of parking spaces
Manual selection of parking space locations for increased accuracy
Color-coded representation:
-Green boxes for the nearest places to park
-Red boxes for occupied spaces
-Yellow boxes for available spaces
Adaptive thresholding and blurring methods for improved detection
