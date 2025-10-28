# Use AWS DeepRacer to explore reinforcement learning

Reinforcement learning, especially deep reinforcement learning, has proven effective in solving a wide array of autonomous
decision-making problems. It has applications in financial trading, data center cooling,
fleet logistics, and autonomous racing, to name a few.

Reinforcement learning has the potential to solve real-world problems. However, it has
a steep learning curve because of its extensive technological scope and depth.
Real-world experimentation requires that you construct a physical agent, such as an
autonomous racing car. It also requires that you secure a physical environment, such as a
driving track or public road. The environment can be costly, hazardous, and
time-consuming. These requirements go beyond merely understanding reinforcement
learning.

To help reduce the learning curve, AWS DeepRacer simplifies the process in three ways:

- Offering step-by-step guidance when training and evaluating reinforcement learning
  models. The guidance includes pre-defined environments, states, and actions, and
  customizable reward functions.
- Providing a simulator to emulate interactions between a virtual [agent](deepracer-basic-concept.md#term-model-vehicle "deepracer-basic-concept.md#term-model-vehicle") and a virtual environment.
- Using an AWS DeepRacer vehicle as a physical agent. Use the vehicle to evaluate a
  trained model in a physical environment. This closely resembles a real-world use
  case.
  If you are a seasoned machine learning practitioner, you will find AWS DeepRacer a welcome
  opportunity to build reinforcement learning models for autonomous racing in both virtual
  and physical environments. To summarize, use AWS DeepRacer to create reinforcement learning
  models for autonomous racing with the following steps:

1. Train a custom reinforcement learning model for autonomous racing. Do this by using the AWS DeepRacer
   console integrated with SageMaker AI.
2. Use the AWS DeepRacer simulator to evaluate a model and test autonomous racing in a virtual environment.
3. Deploy a trained model to AWS DeepRacer model vehicles to test autonomous racing in a physical
   environment.
