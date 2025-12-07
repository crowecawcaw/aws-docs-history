# Prepare your training data and reward functions for reinforcement fine-tuning

To create a reinforcement fine-tuning job, you need training data and reward functions that evaluate response
quality. Unlike traditional fine-tuning that requires input-output pairs, RFT uses prompts and reward signals to
guide model learning.

You can use existing Amazon Bedrock API invocation logs as training data or upload new datasets. Reward functions define what makes a
good response and can use rule-based verification (RLVR) or AI-based judgment (RLAIF).

###### Important

You can provide a maximum of 20K prompts to Amazon Bedrock for reinforcement fine-tuning the model.

###### Topics

- [Option 1: Provide your own prompts for data preparation](rft-option-1.md "rft-option-1.md")
- [Option 2: Use invocation logs for data preparation](rft-option-2.md "rft-option-2.md")
- [Requirements for training data sources](rft-training-data-sources.md "rft-training-data-sources.md")
- [Setting up reward functions](reward-functions.md "reward-functions.md")
