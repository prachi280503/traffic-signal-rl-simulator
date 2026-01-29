# 🚦 Traffic Signal Control using Reinforcement Learning

This project implements a **Traffic Signal Control Simulator** using  
**Multi-Agent Reinforcement Learning (MARL)** with live visualization.

---

## 📊 How It Works

- Each intersection acts as a Reinforcement Learning agent
- Agents observe queue lengths and neighbor congestion
- Rewards are based on minimizing waiting time
- Performance is compared with fixed-time signals

---

## 🛠️ Technologies Used

- Python
- Reinforcement Learning (Q-learning)
- NumPy
- Matplotlib
- Pillow

---

## ▶️ How to Run

```bash
pip install numpy matplotlib pillow
python train.py
python visual_compare_multi.py
