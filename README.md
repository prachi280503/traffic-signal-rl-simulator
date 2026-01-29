# 🚦 Traffic Signal Control using Reinforcement Learning

This project implements a **Traffic Signal Control Simulator** using  
**Multi-Agent Reinforcement Learning (MARL)** with live visualization.

The goal is to reduce vehicle congestion and waiting time by allowing
traffic signals to learn optimal signal phases dynamically.

---

## 📊 How It Works

- Each traffic intersection acts as a **Reinforcement Learning agent**
- Agents observe:
  - Queue lengths at each road
  - Neighbor intersection congestion
- Actions:
  - Switch traffic signal phases (NS or EW green)
- Rewards:
  - Negative total waiting time (minimize congestion)
- Performance is compared with **fixed-time traffic signals**

---

## 🛠️ Technologies Used

- Python
- Reinforcement Learning (Q-learning)
- NumPy
- Matplotlib
- Pillow (for GIF generation)

---

## ▶️ How to Run

```bash
pip install numpy matplotlib pillow
python train.py
python visual_compare_multi.py
