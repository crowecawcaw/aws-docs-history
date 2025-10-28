# What is AWS DeepRacer?

AWS DeepRacer is a fully autonomous 1/18th scale race car driven by [reinforcement learning](deepracer-basic-concept.md#term-rl "deepracer-basic-concept.md#term-rl"). It consists of the following components:

- AWS DeepRacer console: An [AWS Machine Learning](https://aws.amazon.com/machine-learning/ "https://aws.amazon.com/machine-learning/") service
  for [training and evaluating reinforcement
  learning models](create-deepracer-project.md "create-deepracer-project.md") in a three-dimensional simulated autonomous-driving environment.
- AWS DeepRacer vehicle: A 1/18th scale RC car capable of [running inference on a trained AWS DeepRacer model](operate-deepracer-vehicle.md "operate-deepracer-vehicle.md") for autonomous driving.
- AWS DeepRacer League: The world’s first global, autonomous racing league. Race for prizes, glory, and an opportunity to advance to the World Championship Cup. For more information, see the [terms and conditions](https://aws.amazon.com/deepracer/league/ "https://aws.amazon.com/deepracer/league/").

###### Topics

- [The AWS DeepRacer console](#what-is-deepracer-service-console "#what-is-deepracer-service-console")
- [The AWS DeepRacer vehicle](#what-is-deepracer-model-vehicle "#what-is-deepracer-model-vehicle")
- [The AWS DeepRacer League](#what-is-deepracer-racing-series "#what-is-deepracer-racing-series")
- [Use AWS DeepRacer to explore reinforcement learning](deepracer-is-a-learning-environment-for-reinforcement-learning.md "deepracer-is-a-learning-environment-for-reinforcement-learning.md")
- [AWS DeepRacer concepts and terminology](deepracer-basic-concept.md "deepracer-basic-concept.md")

## The AWS DeepRacer console

The AWS DeepRacer console is a graphical user interface for interacting with the AWS DeepRacer service. You
can use the console to train a reinforcement learning model and to evaluate the model
performance in the AWS DeepRacer simulator. In the console, you can also download
a trained model for deployment to your AWS DeepRacer vehicle for autonomous driving in a physical
environment.

In summary, the AWS DeepRacer console supports the following features:

- Create a training job to train a reinforcement learning model with a specified
  reward function, optimization algorithm, environment, and hyperparameters.
- Choose a simulated track to train and evaluate a model by using SageMaker AI.
- Clone a trained model to improve training by tuning hyperparameters to
  optimize your model's performance.
- Download a trained model for deployment to your AWS DeepRacer vehicle so it can drive
  in a physical environment.
- Submit your model to a virtual race and have its performance ranked against
  other models in a virtual leaderboard.

When you use the AWS DeepRacer service console you are charged based on your usage to train or evaluate and store models.

To get you started, AWS DeepRacer provides a [Free Tier](https://aws.amazon.com/free/ "https://aws.amazon.com/free/") to first time AWS DeepRacer users. This is enough time to train and tune your first model and enter the AWS DeepRacer League. There is no cost for submitting a model to take part in any AWS DeepRacer League virtual event.

For details about pricing see the [AWS DeepRacer service detail page](https://aws.amazon.com/deepracer/pricing/ "https://aws.amazon.com/deepracer/pricing/").

## The AWS DeepRacer vehicle

The AWS DeepRacer vehicle is a Wi-Fi enabled, physical vehicle that can drive itself on a
physical track by using a reinforcement learning model.

- You can manually control the vehicle or deploy a model for the vehicle to
  drive autonomously.
- The autonomous mode runs inference on the vehicle's compute module. Inference
  uses images that are captured from the camera that is mounted on the front.
- A Wi-Fi connection allows the vehicle to download software. The connection
  also allows the user to access the device console to operate the vehicle by
  using a computer or mobile device.

## The AWS DeepRacer League

The AWS DeepRacer League is an important component of AWS DeepRacer. The AWS DeepRacer League is intended to foster community and competition.

With the AWS DeepRacer League, you can compare your ML skills with other AWS DeepRacer
developers in a physical or virtual racing event. Not only do you have the opportunity to earn
prizes and achievements, you also have a way to measure your reinforcement learning models. You can compete with other participants, learn from each other,
and inspire each other. If you win achievements for your performance in the AWS DeepRacer League, you can share them with your
community on social media. For more information, see the [terms and conditions](https://aws.amazon.com/deepracer/league/ "https://aws.amazon.com/deepracer/league/").

[Join a race or learn how to train a model in the League](https://console.aws.amazon.com/deepracer "https://console.aws.amazon.com/deepracer").
