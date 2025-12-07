# Customize your model to improve its performance for your use case

Model customization is the process of providing training data to a model in order to improve its performance for specific use-cases. You can customize Amazon Bedrock foundation models in order to improve their performance and create a better customer experience. Amazon Bedrock currently provides the following customization methods.

- **Distillation**

Use distillation to transfer knowledge from a larger more intelligent model (known as teacher) to a smaller, faster, and cost-efficient model (known as student). Amazon Bedrock automates the distillation process by using the latest data synthesis techniques to generate diverse, high-quality responses from the teacher model, and fine-tunes the student model.

To use distillation, you select a teacher model whose accuracy you want to achieve for your use case, and a student model to fine-tune. Then, you provide use case-specific prompts as input data. Amazon Bedrock generates responses from the teacher model for the given prompts, and then uses the responses to fine-tune the student model. You can optionally provide labeled input data as prompt-response pairs.

For more information about using distillation see [Customize a model with distillation in Amazon Bedrock](model-distillation.md "model-distillation.md").

- **Reinforcement fine-tuning**

Reinforcement fine-tuning improves foundation model alignment with your specific use case through feedback-based
learning. Instead of providing labeled input-output pairs, you define reward functions that evaluate response quality.
The model learns iteratively by receiving feedback scores from these reward functions.

You can use existing Bedrock invocation logs as training data or upload custom prompt datasets. You can define reward functions using
AWS Lambda to evaluate response quality. Amazon Bedrock automates the training workflow and provides real-time metrics to monitor model learning progress.

For more information about using reinforcement fine-tuning,
see [Customize a model with reinforcement fine-tuning in Amazon Bedrock](reinforcement-fine-tuning.md "reinforcement-fine-tuning.md").

- **Supervised fine-tuning**

Provide _labeled_ data in order to train a model to improve performance on specific tasks. By providing a training dataset of labeled examples, the model learns to associate what types of outputs should be generated for certain types of inputs. The model parameters are adjusted in the process and the model's performance is improved for the tasks represented by the training dataset.

- **Continued pre-training**

Provide _unlabeled_ data to pre-train a foundation model by familiarizing it with certain types of inputs. You can provide data from specific topics in order to expose a model to those areas. The Continued Pre-training process will tweak the model parameters to accommodate the input data and improve its domain knowledge.

For example, you can train a model with private data, such as business documents, that are not publicly available for training large language models. Additionally, you can continue to improve the model by retraining the model with more unlabeled data as it becomes available.
For information about model customization quotas, see [Amazon Bedrock endpoints and quotas](../../../general/latest/gr/bedrock.md "../../../general/latest/gr/bedrock.md") in the AWS General Reference. After you customize a model, you can set up inference for the new custom model. For more information, see [Set up inference for a custom model](model-customization-use.md "model-customization-use.md").

###### Note

You are charged for model training based on the number of
tokens processed by the model (number of tokens in training data corpus × number of
epochs) and model storage charged per month per model. For more information, see [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/ "https://aws.amazon.com/bedrock/pricing/").

## Guidelines for model customization

The ideal parameters for customizing a model depend on the dataset and the task
for which the model is intended. You should experiment with values to determine
which parameters work best for your specific case. To help, evaluate your model by
running a model evaluation job. For more information, see [Evaluate the performance of Amazon Bedrock resources](evaluation.md "evaluation.md").

Use the training and validation metrics from the [output files](model-customization-analyze.md "model-customization-analyze.md") generated when you
[submit](model-customization-submit.md "model-customization-submit.md") a model customization
job to help you adjust your parameters. Find these files in the Amazon S3 bucket to which
you wrote the output, or use the [GetCustomModel](../APIReference/API_GetCustomModel.md "../APIReference/API_GetCustomModel.md")
operation.
