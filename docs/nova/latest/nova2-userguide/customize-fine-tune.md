# Fine-tuning Amazon Nova models

You can customize the Amazon Nova models using the [_fine-tuning_ method](../../../bedrock/latest/userguide/custom-models.md "../../../bedrock/latest/userguide/custom-models.md") with labeled proprietary data on Amazon Bedrock to gain more performance for your use case than the models provide out-of-the-box. That is, fine-tuning provides enhancements beyond what is gained with zero- or
few-shot invocation and other prompt engineering techniques. You can fine-tune Amazon Nova
models when a sufficient amount of high-quality, labeled training data that is available for
the following use cases:

- When you have a niche or specialized tasks in a specific domain.
- When you want model outputs aligned with brand tone, company policies, or proprietary
  workflows.
- When you need better results across a wide number of tasks and thus need to introduce
  examples in training. This situation is in contrast to providing instructions and
  examples in prompts, which also impacts token cost and request latency.
- When you have tight latency requirements and can benefit from smaller models that are
  tailored to a specific use case.

###### Topics

- [Available models](#custom-fine-tune-models "#custom-fine-tune-models")
- [Performing custom fine-tuning](#customize-fine-tune-steps "#customize-fine-tune-steps")
- [Encryption of Amazon Nova model customization jobs and artifacts](customize-fine-tune-encrypt.md "customize-fine-tune-encrypt.md")
- [Preparing data for fine-tuning Understanding models](fine-tune-prepare-data-understanding.md "fine-tune-prepare-data-understanding.md")
- [Selecting hyperparameters](customize-fine-tune-hyperparameters.md "customize-fine-tune-hyperparameters.md")

## Available models

Fine-tuning is available for the Nova 2 Lite Amazon Nova 2.0 model and
their supported text, image and video modalities.

## Performing custom fine-tuning

To perform custom fine-tuning with Amazon Nova models, you do the following:

1. Create a training dataset and a
   validation dataset (if applicable) for your customization task. For more information about preparing data, see [Preparing data for fine-tuning Understanding models](fine-tune-prepare-data-understanding.md "fine-tune-prepare-data-understanding.md").
2. If you plan to use a new custom IAM role, follow the instructions in [Create a service role for model customization](../../../bedrock/latest/userguide/model-customization-iam-role.md "../../../bedrock/latest/userguide/model-customization-iam-role.md")
   to create an IAM role with access to your data in Amazon S3 buckets. Or you can use an existing role or let the
   console automatically create a role with the proper permissions.
3. (Optional) Configure [Encryption of Amazon Nova model customization jobs and artifacts](customize-fine-tune-encrypt.md "customize-fine-tune-encrypt.md"), [VPC](../../../bedrock/latest/userguide/vpc-model-customization.md "../../../bedrock/latest/userguide/vpc-model-customization.md"), or both, for extra security.
4. [Create a
   Fine-tuning job](../../../bedrock/latest/userguide/model-customization-submit.md "../../../bedrock/latest/userguide/model-customization-submit.md"), controlling the training process by adjusting the [hyperparameter](customize-fine-tune-hyperparameters.md "customize-fine-tune-hyperparameters.md") values.
5. [Analyze the
   results](../../../bedrock/latest/userguide/model-customization-analyze.md "../../../bedrock/latest/userguide/model-customization-analyze.md") by looking at the training or validation metrics or by using model evaluation.
6. [Purchase
   Provisioned Throughput](../../../bedrock/latest/userguide/model-customization-use.md "../../../bedrock/latest/userguide/model-customization-use.md") or [On-demand inference on Custom Models](custom-fine-tune-odi.md "custom-fine-tune-odi.md") for your newly created custom model.
7. [Use your custom
   model](../../../bedrock/latest/userguide/model-customization-use.md "../../../bedrock/latest/userguide/model-customization-use.md") as you would a base model in Amazon Bedrock tasks, such as model inference.
