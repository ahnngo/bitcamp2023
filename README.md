# BitCamp 2023 - IntelliDrive Drowsiness Detector

This repository contains files related to the BitCamp 2023 project for detecting drowsiness in drivers. The project utilizes facial detection techniques to monitor the driver's eyes and alert them when they become drowsy.

## Files Included

The repository includes the following important files:

- `dataset`: directory containing the dataset used for training the machine learning model.
- `face_detector`: directory containing code for the facial detection technique used in the project.
- `detect_drowsiness_video.py`: the main code for detecting drowsiness in drivers using video input.
- `eye_detector.model`: the trained machine learning model for detecting eye states.
- `requirements.txt`: file containing the required Python libraries for the project.
- `training.py`: the code for training the machine learning model.

## Prerequisites

All the dependencies and required libraries are included in the file `requirements.txt`. You need to have Python 3 installed on your system.

## Installation

1. Clone the repo
$ git clone https://github.com/ahnngo/bitcamp2023.git

2. Change your directory to the cloned repo 
$ cd bitcamp2023

3. Now, run the following command in your Terminal/Command Prompt to install the libraries required

$ pip3 install -r requirements.txt

## Working

1. Open a terminal. Go into the cloned project directory and type the following command to train the machine learning model:
$ python3 training.py --dataset dataset

3. To detect drowsiness in drivers using video input, type the following command:
$ python3 detect_drowsiness_video.py

## Contributors

The following people have contributed to the project:

- [Anh (Alec) Ngo](https://github.com/ahnngo)
- [Anh Le](https://github.com/anhle1008)
