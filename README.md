# 🚦 Traffic Signal Control using Reinforcement Learning

An intelligent traffic management system using **Reinforcement Learning (RL)** and **SUMO Simulator** to optimize traffic flow at intersections.

---

## 📌 Project Overview

Traffic congestion is a major problem in urban areas.
This project simulates a traffic intersection where signals are controlled using:

* Fixed-time traffic signals 🚥
* Reinforcement Learning agents 🤖

The RL-based approach learns to reduce vehicle waiting time and improve traffic flow efficiency.

---

## 🎯 Key Features

* 🚗 Real-time traffic simulation using SUMO
* 🤖 Multi-Agent Reinforcement Learning (Q-Learning)
* 📊 Performance comparison with fixed-time signals
* 📈 Visualization using graphs and animations
* 🎥 Demo GIF included

---

## 🛠️ Tech Stack

* Python
* NumPy
* Matplotlib
* SUMO (Simulation of Urban Mobility)
* TraCI (Traffic Control Interface)

---

## 📁 Project Structure

```
traffic-signal-rl-simulator/
│
├── agents/
│   └── rl_agent.py
│
├── env/
│   └── traffic_env.py
│
├── sumo_simulation/
│   ├── sumo_rl.py
│   ├── routes.rou.xml
│   ├── intersection.net.xml
│   ├── simulation.sumocfg
│
├── train.py
├── visual_compare_multi.py
├── compare_fixed.py
├── requirements.txt
├── traffic_rl_vs_fixed.gif
├── README.md
```

---

## ▶️ How to Run

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 2️⃣ Install SUMO

Download from:
👉 https://www.eclipse.org/sumo/

---

### 3️⃣ Set SUMO Path (IMPORTANT)

Make sure SUMO is installed at:

```
C:\Program Files (x86)\Eclipse\Sumo
```

Add it to system PATH or update in code:

```python
SUMO_HOME = r"C:\Program Files (x86)\Eclipse\Sumo"
```

---

### 4️⃣ Run Training

```bash
python train.py
```

---

### 5️⃣ Run Visualization

```bash
python visual_compare_multi.py
```

---

### 6️⃣ Run Real Simulator (SUMO GUI)

```bash
python sumo_simulation/sumo_rl.py
```

---

## 🎥 Demo

![Simulation](traffic_rl_vs_fixed.gif)

---

## 📊 How It Works

* Each intersection acts as an RL agent
* The agent observes traffic queue length
* It selects signal phases (actions)
* Receives rewards based on reduced waiting time
* Learns optimal traffic signal control policy

---

## 🚀 Future Improvements

* Deep Reinforcement Learning (DQN, PPO)
* Multi-intersection city-scale simulation
* Real-world traffic data integration
* Smart city deployment

---

## 🙋‍♀️ Author

**Prachi Birle**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share your feedback!
