# RL-BDI: Integration of Deep Reinforcement Learning into the BDI-Agent architecture
This is the implementation of the BDI-DRL architecture proposed in the paper: "TBA" published in "TBA. In this project, the integration of DRL into the cognitive BDI Agent architecture is considered as an hybrid approach to combine symbolic AI and Deep Neural Networks, known s Neuro-Symbolic AI. We integrate Q-Learning (QL) and Deep Q-Learning (DQN) into cognitive BDi Software-Agents implemented in the Jadex Agent Development Framework. Furthermore, we consider Autonomous Ride Hailing as an application scenario, using MATSim as a simulation environment and trip requests from a bike sharing company. In our experiments, we compare the RL-BDI approach with an informed utility based approach evaluating critical domain specific qualitiy measures.


JadeX - How to Start

- `src/`: source folder 
  - `Agent0.java`: Area agent distributing trip reguests to vehicle agents;
  - `Agent1.java`: Vehicle Agent 1 (other configured Agents are also Vehicle Agents);
  - https://github.com/M4rc3l-M/ees-Jadex
  - https://github.com/M4rc3l-M/TrikeFramework

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
















