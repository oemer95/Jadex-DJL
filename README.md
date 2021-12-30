# rl-bdi Deep Q Learning in JadeX agents
Integration of Reinforcement Learning into the bdi architecture

This is the repo for our project integrating DRL into the cognitive bdi agent architecture.
We use Jadex for the cognitve agent architecture and consider trip requests from a bike sharing company. 
We compare the learning integration approach with the informed utility based approach. 
Our results are shown into the following quality measures. Furthermore, 

JadeX - How to Start

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


#Running DRL and RL 

There are two configurations for the learning process, Q-Leearning as an RL method and Deep-Q-Learning as a DRL method. 
To configure different running scenarios, use the corresponding run.py file and add it to the Jadex platform.



To cite this work, please refer to the corresponding Paper on arxiv. 
Arxiv Link:

Versions of the work are listed below: 

Preprint version available: 
















