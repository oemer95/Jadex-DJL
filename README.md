# rl-bdi
Integration of Reinforcement Learning into the bdi architecture


This is the repo for our project integrating DRL into the cognitive bdi agent architecture.

We use Jadex for the cognitve agent architecture and consider trip requests from a bike sharing company. 

We compare the learning integration approach with the informed utility based approach. 

Our results are shown into the following quality measures.




# DAI 2021 submission: Negotiation in ride-hailing between cooperating BDI agents

This program requires a proper Jade (https://jade.tilab.com/) configuration (v4.5.0). Consider the following steps: 

- `src/`: source folder 
  - `Agent0.java`: Area agent distributing trip reguests to vehicle agents;
  - `Agent1.java`: Vehicle Agent 1 (other configured Agents are also Vehicle Agents);
  - `AgentStatus.java`: Status of the Vehicle Agent
  - `Belief.java`: Vehicle Agent Beliefs
  - `Debug.java`: Debug File to change parameters for each single agent carrying out experiments
  - `Desire.java`: Vehicle Agent Desires
  - `Environment.java`: Environment of Vehicle Agents
  - `Event.java`: Events occuring during Agent processing
  - `FilteredTask.java`: Filtered Tasks the Agent wants to process
  - `Intention.java`: Vehicle Agent Intentions
  - `Job.java`: Job to be processed by the Vehicle Agents
  - `Logger.java`: Logger for Simulated Event Trace
  - `MapArea.java`: Map Utilities
  - `Message.java`: ACL Message for Agent communications
  - `Plan.java`: Vehicle Agent Plans
  - `Scheduler.java`: Dummy Schedule for Trip Requests
  - `TripRequest.java`: Customer Trip Request 


# Vehicle Agent cognitive BDI architecture 

![BDI architecture](TrikeAgent_abstract.pdf)


# How to run

1. Add the `jade.jar` into the  Java project libraries

2. Use the following program arguments in the *run configuration* to define which of the configured agentss will start (e.g. Area Agent + Vehicle Agent 1, 2, 3 for running the 3 Agent configuration):

Program arguments:
```bash
-gui Agent0:Agent0;Agent1:Agent1;Agent2:Agent2;Agent3:Agent3;
```
Use the `debug.java` to define specific parameters and load the data sets.



# Dataset information

The data samples were created by modifying the "Call A Bike" data sets from Deutsche Bahn (DB).
https://data.deutschebahn.com/dataset/data-call-a-bike.html 










