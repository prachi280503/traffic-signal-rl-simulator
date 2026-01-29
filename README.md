# 🚦 Traffic Signal Control using Reinforcement Learning

This project implements a **traffic signal control simulator** using **Multi-Agent Reinforcement Learning (MARL)**.
Each traffic signal learns to adapt its green phases dynamically based on vehicle congestion.

## 🔥 Features
- Custom traffic simulator (Python)
- Multi-intersection environment
- Inter-agent communication
- Reinforcement Learning vs Fixed-time signals
- Live visual animation
- GIF/MP4 export for demo

## 🧠 Technologies Used
- Python
- Reinforcement Learning (Q-learning)
- NumPy
- Matplotlib

## 📊 How It Works
- Each intersection acts as an RL agent
- Agents observe queue lengths and neighbor congestion
- Rewards are based on minimizing waiting time
- Performance is compared with fixed-time signals

## ▶️ How to Run
```bash
pip install numpy matplotlib pillow
python train.py
python visual_compare_multi.py
