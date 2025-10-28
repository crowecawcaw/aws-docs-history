# Anthropic Claude 3 model customization hyperparameters

Anthropic Claude 3 models support the following hyperparameters for model customization. The number of epochs you specify increases your model customization cost by processing more tokens. Each epoch processes the entire training dataset once. For information about pricing, see [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing "https://aws.amazon.com/bedrock/pricing").

| Console Name             | API Name               | Definition                                                                                               | Default | Minimum | Maximum |
| ------------------------ | ---------------------- | -------------------------------------------------------------------------------------------------------- | ------- | ------- | ------- |
| Epoch count              | epochCount             | The maximum number of iterations through the entire training dataset                                     | 2       | 1       | 10      |
| Batch size               | batchSize              | Number of samples processed before updating model parameters                                             | 32      | 4       | 256     |
| Learning rate multiplier | learningRateMultiplier | Multiplier that influences the learning rate at which model parameters are updated after each batch      | 1       | 0.1     | 2       |
| Early stopping threshold | earlyStoppingThreshold | Minimum improvement in validation loss required to prevent premature termination of the training process | 0.001   | 0       | 0.1     |
| Early stopping patience  | earlyStoppingPatience  | Tolerance for stagnation in the validation loss metric before stopping the training process              | 2       | 1       | 10      |
