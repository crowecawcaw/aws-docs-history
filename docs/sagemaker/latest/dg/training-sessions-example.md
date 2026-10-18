

# End-to-end examples
<a name="training-sessions-example"></a>

The [training sessions cookbook](https://github.com/aws/sagemaker-training-sessions-cookbook) on GitHub provides complete, runnable training loops built on the training session APIs. Each recipe covers batching, evaluation, checkpointing with resume, and metrics. Each recipe's README lists the commands, hyperparameters, and expected results.


| Recipe | Description | 
| --- | --- | 
| [Chat SFT](https://github.com/aws/sagemaker-training-sessions-cookbook/tree/main/training_sessions_cookbook/recipes/chat_sft) | Supervised fine-tuning on chat datasets with the cross\_entropy loss. | 
| [GSM8K RL](https://github.com/aws/sagemaker-training-sessions-cookbook/tree/main/training_sessions_cookbook/recipes/gsm8k_rl) | Reinforcement learning on grade-school math problems. | 
| [Code RL](https://github.com/aws/sagemaker-training-sessions-cookbook/tree/main/training_sessions_cookbook/recipes/code_rl) | Reinforcement learning on competitive-programming problems. Generated solutions run against unit tests in a local sandbox and are rewarded on pass rate. | 
| [Preference KTO](https://github.com/aws/sagemaker-training-sessions-cookbook/tree/main/training_sessions_cookbook/recipes/preference_kto) | Preference alignment from binary desirable and undesirable feedback with Kahneman-Tversky optimization (KTO). | 

To deploy a saved checkpoint to a SageMaker AI real-time endpoint, see the [deployment notebook](https://github.com/aws/sagemaker-training-sessions-cookbook/blob/main/notebooks/deploy_to_sagemaker_inference.ipynb) in the cookbook. For the operation definitions, see [Core operations](training-sessions-primitives.md). For client behavior, see [Python SDK reference](training-sessions-sdk.md).