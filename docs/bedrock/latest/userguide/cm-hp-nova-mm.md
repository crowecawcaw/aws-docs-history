# Amazon Nova Understanding model customization hyperparameters

The Amazon Nova Lite, Amazon Nova Micro, and Amazon Nova Pro models support the following three hyperparameters for model customization. For more information, see [Customize your model to improve its performance for your use case](custom-models.md "custom-models.md").

For information about fine tuning Amazon Nova models, see [Fine-tuning Amazon Nova models](../../../nova/latest/userguide/customize-fine-tune.md "../../../nova/latest/userguide/customize-fine-tune.md").

The number of epochs you specify increases your model customization cost by processing more tokens. Each epoch processes the entire training dataset once. For information about pricing, see [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing "https://aws.amazon.com/bedrock/pricing").

| Hyperparameter (console)   | Hyperparameter (API)    | Definition                                                                                         | Type    | Minimum | Maximum | Default |
| -------------------------- | ----------------------- | -------------------------------------------------------------------------------------------------- | ------- | ------- | ------- | ------- |
| Epochs                     | epochCount              | The number of iterations through the entire training dataset                                       | integer | 1       | 5       | 2       |
| Learning rate              | learningRate            | The rate at which model parameters are updated after each batch                                    | float   | 1.00E-6 | 1.00E-4 | 1.00E-5 |
| Learning rate warmup steps | learningRateWarmupSteps | The number of iterations over which the learning rate is gradually increased to the specified rate | integer | 0       | 100     | 10      |

The default epoch number is 2, which works for most cases. In general, larger data sets require fewer epochs to converge, while smaller data sets require more epochs to converge. A faster convergence might also be achieved by increasing the learning rate, but this is less desirable because it might lead to training instability at convergence. We recommend starting with the default hyperparameters, which are based on our assessment across tasks of different complexity and data sizes.

The learning rate will gradually increase to the set value during warm up. Therefore, we recommend that you avoid a large warm up value when the training sample is small because the learning rate might never reach the set value during the training process. We recommend setting the warmup steps by dividing the dataset size by 640 for Amazon Nova Micro, 160 for Amazon Nova Lite, and 320 for Amazon Nova Pro.
