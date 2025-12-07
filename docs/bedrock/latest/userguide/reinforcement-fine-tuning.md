# Customize a model with reinforcement fine-tuning in Amazon Bedrock

Reinforcement fine-tuning is a model customization technique in Amazon Bedrock. It improves foundation model performance by
teaching models what constitutes a "good" response through feedback signals called rewards. While traditional fine-tuning
methods depend on labeled datasets, reinforcement fine-tuning uses a feedback-driven approach. This allows models to improve
iteratively based on reward signals. Instead of learning from fixed examples, it uses reward functions to evaluate and judge which
responses are considered good for particular business use cases.

Reinforcement fine-tuning teaches models to understand what makes a quality response. You don't need massive amounts
of pre-labeled training data. This makes advanced model customization in Amazon Bedrock more accessible and cost-effective.

The capability supports two approaches to provide flexibility for optimizing models:

- **Reinforcement Learning with Verifiable Rewards (RLVR)** - Uses rule-based graders
  for objective tasks like code generation or math reasoning
- **Reinforcement Learning from AI Feedback (RLAIF)** - Uses AI-based judges for
  subjective tasks like instruction following or content moderation
  For more information, see [Setting up reward functions](reward-functions.md "reward-functions.md").

Reinforcement fine-tuning can provide the following benefits:

- **Improved model performance** - Reinforcement fine-tuning improves model accuracy
  compared to base models. This enables optimization for price and performance by training smaller, faster,
  and more efficient model variants.
- **Flexible training data** - Amazon Bedrock automates much of the complexity. This makes
  reinforcement fine-tuning accessible to developers building AI applications. You can easily train models using
  existing Amazon Bedrock model invocation logs as training data or upload your datasets.
- **Security and compliance** - Your proprietary data never leaves AWS's secure,
  governed environment during the customization process.

###### Topics

- [Supported models for reinforcement fine-tuning](#rft-supported-models "#rft-supported-models")
- [How reinforcement fine-tuning works](#rft-how-it-works "#rft-how-it-works")
- [Reinforcement fine-tuning access and security](rft-access-security.md "rft-access-security.md")
- [Prepare your training data and reward functions for reinforcement fine-tuning](rft-prepare-data.md "rft-prepare-data.md")
- [Create a reinforcement fine-tuning job](rft-submit-job.md "rft-submit-job.md")

## Supported models for reinforcement fine-tuning

The following table shows the foundation models that you can customize with reinforcement fine-tuning:

| Supported models for reinforcement fine-tuning | Provider    | Model                        | Model ID  | Single-region model support |
| ---------------------------------------------- | ----------- | ---------------------------- | --------- | --------------------------- |
| Amazon                                         | Nova 2 Lite | amazon.nova-2-lite-v1:0:256k | us-east-1 |

## How reinforcement fine-tuning works

Amazon Bedrock fully automates the RFT workflow through a three-stage process:

**Stage 1: Response generation**

The actor model (the model being customized) receives prompts from your training dataset and generates responses.
By default, it generates 4 responses per prompt. This stage supports both single-turn and multi-turn interactions,
allowing comprehensive coverage of different use cases.

**Stage 2: Reward computation**

Actor model generated prompt-response pairs are evaluated by your selected optimizing models:

- **RLVR** - Execute through Lambda to compute objective scores
- **RLAIF** - Evaluate responses based on criteria and principles you configure
  (the console converts these into Lambda functions automatically)

**Stage 3: Actor model training**

Amazon Bedrock uses the prompt-response pairs with scores to train the actor model through policy-based learning using Group
Relative Policy Optimization (GRPO). The training loop continues iteratively until the model achieves desired performance
metrics or meets pre-defined stopping criteria.

Amazon Bedrock automatically handles parallel reward computation, training pipeline optimization, and implements safeguards
against common reinforcement learning challenges like reward hacking and policy collapse.
