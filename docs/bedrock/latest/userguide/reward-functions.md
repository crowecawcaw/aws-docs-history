# Setting up reward functions

Reward functions evaluate response quality and provide feedback signals for model training. Choose the approach
that matches your task requirements.

## Reinforcement Learning via Verifiable Rewards (RLVR)

RLVR enables you to optimize models for objective tasks such as code generation or math reasoning.
You can define reward functions using verifiable rule-based graders or use ready-to-use templates for common
use cases such as format checks, summarization, and text similarity.

You have two options for RLVR (Custom Code):

- Use console-provided templates - The Amazon Bedrock console provides sample templates for grader Lambda functions:

      + Mathematical reasoning with ground truth verification
      + Format validation and constraint checking
      + Generic grader Lambda template with boilerplate code for your grader Lambda function

  Before setting up your Lambda function, follow the instructions in the provided template on the **Create RFT job** page
  in the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock").

- Bring your own Lambda function — Create custom reward functions executed through Lambda functions
  using your own Lambda ARN. You can combine multiple graders to produce a single score.

## Reinforcement Learning via AI Feedback (RLAIF)

RLAIF enables optimization for subjective tasks such as instruction following or chatbot interactions.
You can use AI-based judges with ready-to-use templates for common use cases to evaluate response quality
based on criteria you define.

**For RLAIF (Model as Judge):**

- Select an Amazon Bedrock hosted base Model as Judge
- Configure instructions for evaluation
- Define evaluation criteria and scoring guidelines

You can use the LLM-as-Judge prompt templates provided in the Amazon Bedrock console:

- Instruction following (Judge model training)
- Summarization (Multi-turn dialogs)
- Reasoning evaluation (CoT for specialized domains)
- RAG faithfulness (Context-grounded Q&A)

###### Note

- When you use the console's **Model as Judge** option, Amazon Bedrock automatically converts your configuration into a
  Lambda function that executes during training.
- If you bring your own Lambda function, the Lambda execution role needs necessary permissions to invoke models with model ID or
  inference profile as described in [Grader Lambda function permissions for RLAIF](rft-access-security.md#rft-bedrock-permissions "rft-access-security.md#rft-bedrock-permissions").
