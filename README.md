<h1 align="center">IntelliDrive Drowsiness Detector</h1>

<div align= "center"><img src="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.istockphoto.com%2Fphoto%2Fdrive-safely-written-on-the-road-gm467514262-60373292&psig=AOvVaw1U0jlR4lhXSCsG9zf1MrvC&ust=1681313425654000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCLCJld6Sov4CFQAAAAAdAAAAABAE"/>
  <h4>Inspired by the increasing number of accidents caused by drowsy driving, IntelliDrive Drowsiness Detector employs image processing and deep learning to identify driver fatigue and provides a 5-second alert to prevent incidents.
  </h4>
</div>


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

```
$ git clone https://github.com/ahnngo/intellidrive-drowsiness-detector.git
```

2. Change your directory to the cloned repo 

```
$ cd intellidrive-drowsiness-detector
```

3. Now, run the following command in your Terminal/Command Prompt to install the libraries required

```
$ pip3 install -r requirements.txt
```

## Working

1. Open a terminal. Go into the cloned project directory and type the following command to train the machine learning model:

```
$ python3 training.py --dataset dataset
```

2. To detect drowsiness in drivers using video input, type the following command:

```
$ python3 detect_drowsiness_video.py
```

## Contributors

The following people have contributed to the project:

- [Anh (Alec) Ngo](https://github.com/ahnngo)
- [Anh Le](https://github.com/anhle1008)
