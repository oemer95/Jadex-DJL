# rl-bdi
Integration of Reinforcement Learning into the bdi architecture


This is the repo for our project integrating DRL into the cognitive bdi agent architecture.

We use Jadex for the cognitve agent architecture and consider trip requests from a bike sharing company. 

We compare the learning integration approach with the informed utility based approach. 

Our results are shown into the following quality measures.






# DAI 2021 submission: Negotiation in ride-hailing between cooperating BDI agents

This program requires a proper Jade (https://jade.tilab.com/) configuration (v4.5.0). Do the following steps: 

1. Add the jade.jar into the  Java project libraries

2. Use the following program arguments in the "run configuration" to define which of the configured agentss will start (e.g. Area Agent (agent0) + Trike Agent 1, 2, 3 for running the 3 Agent configuration):

Program arguments:
-gui Agent0:Agent0;Agent1:Agent1;Agent2:Agent2;Agent3:Agent3;

use the debug.java to define specific parameters and load the data sets
