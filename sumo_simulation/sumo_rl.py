import os
import sys
import time

SUMO_HOME = r"C:\Program Files (x86)\Eclipse\Sumo"
os.environ["SUMO_HOME"] = SUMO_HOME
sys.path.append(os.path.join(SUMO_HOME, "tools"))

import traci


sumoBinary = r"C:\Program Files (x86)\Eclipse\Sumo\bin\sumo-gui.exe"

sumoCmd = [sumoBinary, "-c", "simulation.sumocfg"]

traci.start(sumoCmd)

print("🚦 Simulation started")
for step in range(1000):
    traci.simulationStep()
    vehicles = traci.vehicle.getIDList()
    print("Vehicles:", len(vehicles))
    time.sleep(0.05)

traci.close()
print("✅ Simulation ended")