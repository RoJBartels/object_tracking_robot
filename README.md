# 🟥 Object Following Robot (Simulation)

A minimal computer vision project that detects a colored object in a camera feed and simulates a robot following it. Built in < 1 day as a rapid robotics prototype.

## 🚀 Project Goal

Build a simple perception-to-action pipeline:

* Detect an object (based on color) using a camera
* Estimate its position in the image
* Simulate movement decisions (left/right/forward)

This project focuses on **fast prototyping in robotics without heavy frameworks like ROS**.

---

## 🧠 Tech Stack

* Python
* OpenCV
* NumPy

---

## 📸 Features

* Real-time webcam feed
* Color-based object detection (HSV space)
* Object highlighting via mask
* (Next steps)

  * Object position tracking
  * Movement logic simulation

---

## 🛠️ Installation

```bash
git clone <your-repo-url>
cd object-following-robot

pip install -r requirements.txt
```

---

## ▶️ Run

```bash
python main.py
```

Press `ESC` to exit the application.

---

## ⚙️ How It Works

1. Capture webcam frames using OpenCV
2. Convert image from BGR to HSV
3. Apply color threshold to detect red objects
4. Create a mask and overlay result

---

## 🧪 Example Use

Hold a red object (e.g. a cup or ball) in front of your webcam.

* The mask highlights detected regions
* The processed image shows only the detected object

---

## 🧩 Next Steps

* [ ] Detect object center (x, y)
* [ ] Draw bounding circle
* [ ] Add simple control logic:

  * Move left/right if object is off-center
  * Move forward if centered
* [ ] Simulate robot movement

---

## 🎯 Why This Project?

This project demonstrates:

* Practical computer vision skills
* Understanding of perception pipelines in robotics
* Ability to build working prototypes quickly

---

## 📌 Future Extensions

* Replace color detection with ML-based object detection
* Integrate with a real robot (e.g. Raspberry Pi + motors)
* Add ROS for modular robotics architecture

---

## 🧑‍💻 Author

Robin Jens Bartels

---

## 📄 License

MIT (or choose your preferred license)
