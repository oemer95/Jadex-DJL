# rl-bdi
Integration of Reinforcement Learning into the bdi architecture

This is the repo for our project integrating DRL into the cognitive bdi agent architecture.

We use Jadex for the cognitve agent architecture and consider trip requests from a bike sharing company. 

We compare the learning integration approach with the informed utility based approach. 

Our results are shown into the following quality measures.


- `src/`: source folder 
  - `Agent0.java`: Area agent distributing trip reguests to vehicle agents;
  - `Agent1.java`: Vehicle Agent 1 (other configured Agents are also Vehicle Agents);

![BDI architecture](TrikeAgent_abstract.pdf)

# How to run

1. Add the `jade.jar` into 
2.  in the *run configuration*

Program arguments:
```bash
-gui Agent0:Agent0;Agent1:Agent1;Agent2:Agent2;Agent3:Agent3;
```
# Dataset information

The data samples were created by modifying the "Call A Bike" data sets from Deutsche Bahn (DB).
https://data.deutschebahn.com/dataset/data-call-a-bike.html 




#Running DRl and RL 

To configure different running scenarios, use the Run.py  













