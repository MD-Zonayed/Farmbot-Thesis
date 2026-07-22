# 🌱 Machine Learning-Based IoT-Enabled Farmbot for Smart Farming

<p align="center">
  </p><img width="800" height="750" alt="Farmbot Picture" src="https://github.com/user-attachments/assets/38ca3724-9673-4cc0-91dd-26e34bd856f2" />
</p>

<p align="center">

<img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge"/>

<img src="https://img.shields.io/badge/Research-AI%20%7C%20Robotics-blue?style=for-the-badge"/>

<img src="https://img.shields.io/badge/Python-3.10-yellow?style=for-the-badge"/>

<img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-green?style=for-the-badge"/>

<img src="https://img.shields.io/badge/YOLOv8-Object%20Detection-red?style=for-the-badge"/>

<img src="https://img.shields.io/badge/IoT-MQTT%20%7C%20ThingSpeak-orange?style=for-the-badge"/>

<img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge"/>

</p>

---

# 📖 Project Overview

This repository contains my undergraduate thesis titled:

> **Machine Learning-Based IoT-Enabled Farmbot for Smart Farming**

Completed as part of the **Bachelor of Science in Mechatronics Engineering** at the **World University of Bangladesh**.

The project presents the design, development, and implementation of a fully automated CNC-based Farmbot capable of performing intelligent agricultural operations through the integration of **Artificial Intelligence (AI)**, **Machine Learning (ML)**, **Computer Vision (CV)**, **Internet of Things (IoT)**, and **CNC Automation**.

Unlike conventional farming systems, the proposed Farmbot continuously monitors crop health, automates agricultural tasks, and provides real-time remote monitoring using IoT technologies. The system integrates computer vision with deep learning for plant disease detection and weed identification while utilizing MQTT communication and ThingSpeak cloud services for smart farm management.

The project demonstrates how modern intelligent technologies can improve agricultural productivity, reduce manual labor, optimize resource utilization, and support sustainable farming practices.

---

# 🎯 Research Objectives

The primary objectives of this research were to:

- Develop a fully autonomous CNC-based Farmbot.
- Integrate Machine Learning for intelligent crop monitoring.
- Implement Computer Vision for tomato disease detection.
- Detect weeds using deep learning.
- Monitor environmental conditions through IoT sensors.
- Enable remote monitoring using MQTT and ThingSpeak.
- Develop an intuitive graphical user interface (GUI).
- Improve precision agriculture through intelligent automation.
- Reduce labor costs and increase farming efficiency.

---

# ✨ Key Features

✅ Autonomous CNC-based Farming Robot

✅ AI-powered Tomato Disease Detection

✅ Deep Learning-Based Weed Detection

✅ Real-Time Environmental Monitoring

✅ IoT Remote Monitoring Dashboard

✅ MQTT Communication

✅ ThingSpeak Cloud Integration

✅ Streamlit Dashboard

✅ MATLAB GUI

✅ Raspberry Pi-Based Control System

✅ Arduino Mega Motion Controller

✅ Automated Seeding

✅ Automated Watering

✅ Automated Weeding

✅ Image Stitching for Large Farm Visualization

✅ Soil Moisture Monitoring

✅ Temperature & Humidity Monitoring

✅ Water Tank Level Detection

✅ pH Monitoring

✅ Camera-Based Crop Monitoring

---

# 🏗 System Architecture

<p align="center">

<img width="486" height="612" alt="Farmbot Block Dia" src="https://github.com/user-attachments/assets/e17e47f1-e5e7-4e5f-a7a9-4dba77ac2b88" />

</p>

The proposed Farmbot consists of five major subsystems:

- Mechanical Structure
- CNC Motion Control System
- Embedded Control System
- Computer Vision System
- IoT Monitoring System

The Raspberry Pi acts as the primary computing unit responsible for AI inference, image processing, MQTT communication, and cloud connectivity, while the Arduino Mega controls the CNC motion system using Marlin firmware and G-code instructions.

---

# 📂 Repository Structure

```text
Farmbot-Smart-Farming/
│
├── README.md
├── LICENSE
├── CITATION.cff
├── requirements.txt
│
├── docs/
│
├── images/
│
├── hardware/
│
├── firmware/
│
├── software/
│
├── computer_vision/
│
├── datasets/
│
├── videos/
│
└── results/
```

---

# ⚙️ Hardware Components

| Component | Purpose |
|-----------|---------|
| Raspberry Pi 4B+ | Main processing unit for AI, Computer Vision, MQTT and IoT |
| Arduino Mega 2560 | Motion control and hardware interface |
| RAMPS 1.6 Shield | CNC motor driver controller |
| NEMA 17 Stepper Motors | X, Y and Z axis movement |
| A4988 Stepper Drivers | Motor driving and motion control |
| ESP32 | Wireless IoT communication |
| Raspberry Pi Camera | Image acquisition |
| DHT11 Sensor | Temperature and humidity monitoring |
| Soil Moisture Sensor | Soil moisture measurement |
| pH Sensor | Soil pH monitoring |
| Ultrasonic Sensor | Water tank level measurement |
| Water Pump | Automatic irrigation |
| Vacuum Pump | Seed dispensing mechanism |
| Solenoid Valve | Water flow control |
| LCD Display | Local monitoring |
| Relay Module | Switching high-power devices |
| Solar Panel | Renewable energy source |
| Rechargeable Battery | Backup power supply |

---

# 💻 Software & Development Tools

| Software | Purpose |
|-----------|---------|
| Python | Main programming language |
| Arduino IDE | Microcontroller programming |
| MATLAB App Designer | GUI development |
| Streamlit | Web dashboard |
| OpenCV | Computer vision algorithms |
| YOLOv8 | Tomato and weed detection |
| MQTT | IoT communication |
| ThingSpeak | Cloud monitoring platform |
| Marlin Firmware | CNC motion control |
| G-code & M-code | CNC path planning |
| SolidWorks | Mechanical design |
| Proteus | Circuit simulation |
| Git & GitHub | Version control |
| Jupyter Notebook | Machine learning experiments |

---

# 🧩 Mechanical Design

<p align="center">

<img width="450" height="400" alt="Farmbot Design 1" src="https://github.com/user-attachments/assets/10b719c1-c1e0-488e-b789-0f4793985a10" />
<img width="500" height="450" alt="Farmbot Design 2 png" src="https://github.com/user-attachments/assets/6c34a518-e5fc-4926-8d39-dd50fb4a9122" /> <img width="500" height="450" alt="Farmbot Design 3 png" src="https://github.com/user-attachments/assets/0c1d5a23-a13b-4167-9d13-255ae8f2ca3c" />

</p>

The Farmbot adopts a Cartesian CNC architecture designed in **SolidWorks**. The mechanical structure consists of aluminum extrusion frames, 3D-printed PETG components, timing belts, linear guides, and a modular tool head capable of performing seeding, watering, and crop monitoring operations.

The lightweight and modular design enables easy maintenance, scalability, and adaptation to different agricultural environments.

---

# 🤖 Machine Learning & Artificial Intelligence

Artificial Intelligence is one of the core components of this Farmbot. Machine Learning and Deep Learning techniques enable the robot to autonomously identify crops, detect diseases, recognize weeds, and support precision agriculture with minimal human intervention.

## AI Capabilities

- 🍅 Tomato Disease Detection
- 🌿 Weed Detection
- 🧠 Deep Learning-Based Object Detection
- 📸 Real-Time Image Processing
- 🤖 Intelligent Decision Making

### Machine Learning Pipeline

```text
Image Acquisition
        │
        ▼
 Image Preprocessing
        │
        ▼
 YOLOv8 Inference
        │
        ▼
 Disease / Weed Detection
        │
        ▼
 Decision Making
        │
        ▼
 Farmbot Action
```

---

# 👁️ Computer Vision

Computer Vision enables the Farmbot to understand the surrounding agricultural environment by processing images captured using the Raspberry Pi Camera.

## Computer Vision Tasks

- Tomato Detection
- Tomato Disease Identification
- Weed Detection
- Image Stitching
- Crop Monitoring
- Object Localization

## Computer Vision Workflow

```text
Camera
   │
   ▼
Image Capture
   │
   ▼
OpenCV Processing
   │
   ▼
YOLOv8 Detection
   │
   ▼
Visualization
   │
   ▼
Farmbot Response
```

<p align="center">
<img width="500" height="350" alt="Tomato detection" src="https://github.com/user-attachments/assets/bde5de3e-71ce-4227-ba62-0d3f1d539ac5" />
</p>

<p align="center">
<img width="500" height="350" alt="Weed Detection" src="https://github.com/user-attachments/assets/7a43042e-c2f6-4bf3-b53e-c94d660296f6" />
</p>

<p align="center">
<img width="500" height="350" alt="Image stitching" src="https://github.com/user-attachments/assets/f3a5a0d8-e718-4cff-88d4-c62d62de87dd" />
</p>

---

# 🌐 Internet of Things (IoT)

The Farmbot integrates IoT technologies to enable remote monitoring, real-time data visualization, and intelligent farm management.

The Raspberry Pi collects data from environmental sensors and communicates with cloud services using MQTT. Sensor readings are continuously uploaded to ThingSpeak, allowing farmers to monitor crop conditions remotely.

## IoT Features

- Remote Monitoring
- MQTT Communication
- ThingSpeak Cloud
- Streamlit Dashboard
- Environmental Monitoring
- Real-Time Alerts
- Wireless Communication

## IoT Architecture

```text
Sensors
     │
     ▼
ESP32
     │
     ▼
MQTT Broker
     │
     ▼
Raspberry Pi
     │
     ▼
ThingSpeak Cloud
     │
     ▼
Streamlit Dashboard
```

<p align="center">
<img width="700" height="550" alt="thingspeak" src="https://github.com/user-attachments/assets/f5e5d7e0-dca2-45f2-9883-6291e0eadef9" />
</p>

<p align="center">
<img width="725" height="700" alt="streamlit" src="https://github.com/user-attachments/assets/48632fe3-c45d-4a39-b7c2-3b9ceec969ab" />
</p>

---

# ⚙️ CNC Automation

The Farmbot is built upon a Cartesian CNC platform that allows highly accurate positioning of agricultural tools.

The Arduino Mega, RAMPS 1.6 shield, and Marlin Firmware control the X, Y, and Z axes using G-code instructions.

## CNC Features

- Cartesian Motion System
- G-Code Interpreter
- Marlin Firmware
- Automated Positioning
- High Precision Motion
- Modular Tool Head

## CNC Workflow

```text
GUI
   │
   ▼
G-Code
   │
   ▼
Arduino Mega
   │
   ▼
RAMPS 1.6
   │
   ▼
Stepper Drivers
   │
   ▼
NEMA17 Motors
   │
   ▼
Farmbot Motion
```

---

# 🔌 Embedded System

The Farmbot integrates multiple embedded devices working together to achieve intelligent automation.

## Embedded Components

- Raspberry Pi 4B+
- Arduino Mega 2560
- ESP32
- RAMPS 1.6
- Stepper Drivers
- Environmental Sensors
- Camera Module
- LCD Display
- Relay Modules

The Raspberry Pi executes AI algorithms while the Arduino Mega performs deterministic motion control for CNC operations.

---

# 🔋 Sensor Network

The Farmbot continuously monitors environmental conditions using multiple sensors.

| Sensor | Function |
|---------|----------|
| DHT11 | Temperature & Humidity |
| Soil Moisture | Soil Water Content |
| pH Sensor | Soil pH Measurement |
| Ultrasonic Sensor | Water Tank Level |
| Raspberry Pi Camera | Crop Monitoring |

---

# 🖥️ Graphical User Interface

Two interfaces were developed to simplify Farmbot operation.

## MATLAB GUI

Features include:

- Manual Motion Control
- Sensor Monitoring
- Camera Control
- Farmbot Status
- Automatic Operation

<p align="center">
<img width="700" height="500" alt="Matlab GUI" src="https://github.com/user-attachments/assets/a17a5fda-e8f6-4acf-9e13-30999a665f2a" />
</p>

---

## Streamlit Dashboard

Provides

- Remote Monitoring
- Live Sensor Values
- Camera Feed
- Cloud Data Visualization
- Device Status

---

# 🧪 Experimental Results

The developed Farmbot successfully demonstrated:

✅ Autonomous Movement

✅ Automatic Seeding

✅ Intelligent Watering

✅ Tomato Disease Detection

✅ Weed Detection

✅ Environmental Monitoring

✅ IoT Remote Monitoring

✅ MQTT Communication

✅ ThingSpeak Integration

✅ Image Stitching

✅ GUI-Based Control

---

# 📊 Project Outcomes

The proposed Farmbot successfully integrates Artificial Intelligence, Machine Learning, Computer Vision, IoT, and CNC Automation into a unified precision agriculture platform.

The developed prototype demonstrates the feasibility of intelligent autonomous farming by reducing manual intervention while improving monitoring, decision-making, and resource utilization.

The project serves as a scalable framework for future agricultural robotic systems and highlights the potential of AI-driven automation in sustainable farming.

---

# 📂 Complete Repository Structure

```text
Farmbot-Smart-Farming/
│
├── README.md
├── LICENSE
├── CITATION.cff
├── requirements.txt
│
├── docs/
│   ├── Final_Thesis.pdf
│   ├── Thesis_Presentation.pdf
│   └── Project_Poster.pdf
│
├── images/
│   ├── farmbot_banner.png
│   ├── block_diagram.png
│   ├── mechanical_design.png
│   ├── electrical_design.png
│   ├── sensor_circuit.png
│   ├── gui.png
│   ├── streamlit_dashboard.png
│   ├── thingspeak.png
│   ├── tomato_detection.png
│   ├── weed_detection.png
│   ├── image_stitching.png
│   ├── prototype.jpg
│   └── testing.jpg
│
├── hardware/
│   ├── CAD/
│   ├── STL/
│   ├── SolidWorks/
│   ├── Proteus/
│   └── Circuit_Diagrams/
│
├── firmware/
│   ├── Arduino/
│   ├── ESP32/
│   ├── Marlin/
│   └── GCode/
│
├── software/
│   ├── Streamlit/
│   ├── MATLAB_GUI/
│   ├── MQTT/
│   └── ThingSpeak/
│
├── computer_vision/
│   ├── Tomato_Detection/
│   ├── Weed_Detection/
│   ├── Image_Stitching/
│   └── Dataset/
│
├── datasets/
│
├── videos/
│
└── results/
```

---

# 🚀 Getting Started

## Clone the Repository

```bash
git clone https://github.com/md-zonayed/Farmbot-Smart-Farming.git
```

```bash
cd Farmbot-Smart-Farming
```

---

## Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

## Upload Firmware

1. Open the Arduino IDE.
2. Connect the Arduino Mega 2560.
3. Upload the firmware from:

```text
firmware/Arduino/
```

4. Upload ESP32 code from:

```text
firmware/ESP32/
```

---

## Launch the Streamlit Dashboard

```bash
streamlit run app.py
```

---

## Launch MATLAB GUI

Open

```text
software/MATLAB_GUI/
```

and run the GUI using MATLAB App Designer.

---

# 📂 Source Code Organization

| Folder | Description |
|----------|-------------|
| firmware | Arduino, ESP32, Marlin Firmware |
| software | GUI and Dashboard Applications |
| computer_vision | Computer Vision Algorithms |
| datasets | Training Images and Labels |
| hardware | CAD, Circuit Designs and STL Files |
| results | Experimental Results |
| docs | Thesis, Poster and Presentation |

---

# 📈 Experimental Highlights

The proposed Farmbot successfully demonstrated:

- Autonomous Cartesian CNC Navigation
- Intelligent Tomato Disease Detection
- Deep Learning-Based Weed Detection
- Real-Time Environmental Monitoring
- Remote IoT Monitoring
- Cloud-Based Data Logging
- Automatic Watering
- Automated Seeding
- Image Stitching
- Precision Agriculture Applications

---

# 📊 Technologies Used

| Category | Technologies |
|----------|--------------|
| Programming | Python, C, C++ |
| Robotics | Raspberry Pi, Arduino Mega, Marlin |
| Computer Vision | OpenCV, YOLOv8 |
| Machine Learning | Deep Learning |
| IoT | MQTT, ESP32, ThingSpeak |
| GUI | MATLAB App Designer, Streamlit |
| CAD | SolidWorks |
| Simulation | Proteus |
| CNC | G-code, M-code |
| Version Control | Git, GitHub |

---

# 🌍 Applications

This project can be adapted for:

- Smart Farming
- Precision Agriculture
- Greenhouse Automation
- Research Laboratories
- Educational Robotics
- Autonomous Agricultural Robots
- Crop Health Monitoring
- Smart Irrigation Systems

---

# 🔮 Future Improvements

Several enhancements can further improve the proposed Farmbot:

- Integration of ROS2 for modular robot control
- Reinforcement Learning for autonomous decision-making
- SLAM-based navigation
- Multi-camera perception
- Robotic manipulator for fruit harvesting
- AI-based yield prediction
- Edge AI optimization
- Solar-powered autonomous operation
- Digital Twin integration
- Multi-robot collaborative farming
- Large Language Model (LLM)-assisted farm management

---

# 📚 Related Publications

This repository is associated with several research publications related to precision agriculture, AI, IoT, and intelligent robotic systems.

Some of the major publications include:

- Advancing Precision Agriculture: A Comprehensive Review of Machine Learning Applications with Limitations & Future Prospects
- Design of a Universal IoT-Enabled Wheeled Farmbot for Tomato Plant Disease Detection & Health Monitoring
- Machine Learning and IoT in Healthcare: Recent Advancements, Challenges & Future Direction
- An Ensemble Machine Learning Approach for Viral Infection Prediction using IoMT

---

# 📖 Citation

If you use this repository in your research, please cite:

```bibtex
@thesis{zonayed2023farmbot,
  author={MD Zonayed},
  title={Machine Learning-Based IoT-Enabled Farmbot for Smart Farming},
  school={World University of Bangladesh},
  year={2023}
}
```

---

# 📄 License

This project is released under the **MIT License**.

See the LICENSE file for more information.

---

# 🤝 Acknowledgements

I would like to express my sincere gratitude to:

- Department of Mechatronics Engineering
- World University of Bangladesh
- My thesis supervisor
- My respected teachers
- Dreamers Lab
- All contributors who supported this research

---

# 👨‍💻 Author

## MD Zonayed

Research Assistant | Robotics & AI Researcher | Mechatronics Engineer

### Research Interests

- Robotics
- Artificial Intelligence
- Machine Learning
- Deep Learning
- Computer Vision
- Internet of Things
- Precision Agriculture
- Human-Robot Collaboration
- Industrial Automation

📧 **Email:** iamzunayed@gmail.com

🌐 **LinkedIn**

https://www.linkedin.com/in/md-zonayed-8966a8276

📚 **Google Scholar**

https://scholar.google.com/citations?user=oDymy0IAAAAJ&hl=en

🔬 **ResearchGate**

https://www.researchgate.net/profile/Md-Zonayed

---

# ⭐ Support the Project

If you find this project useful, please consider:

⭐ Starring the repository

🍴 Forking the repository

📝 Citing this work in your research

🤝 Collaborating on future research projects

---

<p align="center">

<b>🌱 Advancing Precision Agriculture through Artificial Intelligence, Robotics, Computer Vision and IoT 🌱</b>


