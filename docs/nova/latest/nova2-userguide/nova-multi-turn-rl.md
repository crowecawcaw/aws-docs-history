# Multi-turn Reinforcement Learning

## Overview

Multi-turn reinforcement learning (multi-turn RL) trains a model to improve across a sequence of interactions rather than grading a single response. Instead of evaluating one reply in isolation, multi-turn RL evaluates the entire trajectory of steps the model takes—including tool calls, code execution, and web searches—to reach a final outcome.

Consider a customer service agent that must resolve a billing dispute. Success depends not on any single message, but on the full sequence: looking up the account, identifying the charge, checking policy, and communicating the resolution. Multi-turn RL trains the model to optimize this end-to-end sequence, so each step contributes to a successful outcome.

This approach is particularly valuable for agentic workflows where the model must coordinate multiple actions over several turns and recover from intermediate mistakes to achieve a goal.

## When to use multi-turn RL

Multi-turn RL is ideal for scenarios where:

- The task requires back-and-forth interaction between the model and an environment or user.
- Quality depends on the sequence of actions taken, not just a single response.
- The model uses tools across multiple steps to accomplish a goal.
- Mistakes at intermediate steps can be recovered from in later turns.
- The model performs well on individual turns but produces poor end-to-end results.

## Supported models

The following table lists the models and AWS Regions that support multi-turn RL.

| Model         | Supported Regions    |
| ------------- | -------------------- |
| Nova Lite 2.0 | us-east-1, us-west-2 |

For complete instructions on setting up prerequisites, preparing your agent, formatting training data, launching and monitoring training jobs, deploying trained models, and evaluating results, see [Multi-turn reinforcement learning](../../../sagemaker/latest/dg/model-customize-mtrl.md "../../../sagemaker/latest/dg/model-customize-mtrl.md") in the SageMaker Developer Guide.
