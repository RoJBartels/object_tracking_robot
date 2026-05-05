# Real-Time Object Following (OpenCV)

A minimal computer vision project that detects a colored object in a webcam feed and simulates robot-like movement decisions.

Built as a fast prototype to demonstrate perception-driven control.

---

## Overview

The system:

* Detects a red object using HSV color segmentation
* Tracks its position in real time
* Simulates movement decisions (left / right / forward)

---

## Tech Stack

* Python
* OpenCV
* NumPy

---

## Run

```bash
pip install -r requirements.txt
python main.py
```

Press `ESC` to exit.

---

## How It Works

Pipeline:

```text
Camera → Color Detection → Contour → Centroid → Decision
```

* Largest red object is detected
* Center position is computed using image moments
* Movement is determined based on horizontal offset

---

## Demo

![Tracking Demo](media/Object_Tracking_Demo.gif)

---

## Key Highlights

* Real-time object tracking using OpenCV
* Centroid-based position estimation
* Simple control logic (robot-inspired)
* Clean perception → decision pipeline

---

## Next Steps

* Distance estimation (object size)
* Smoother control (reduce jitter)
* Hardware integration (Raspberry Pi / motors)
* ROS2 integration
