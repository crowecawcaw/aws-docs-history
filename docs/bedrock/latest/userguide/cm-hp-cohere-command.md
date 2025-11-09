# Cohere Command model customization hyperparameters

The Cohere Command and Cohere Command Light models support the following hyperparameters for
model customization. The number of epochs you specify increases your model customization cost by processing more tokens. Each epoch processes the entire training dataset once. For information about pricing, see [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing "https://aws.amazon.com/bedrock/pricing"). For more information, see [Customize your model to improve its performance for your use case](custom-models.md "custom-models.md").

For information about fine tuning Cohere models, see the Cohere documentation at [https://docs.cohere.com/docs/fine-tuning](https://docs.cohere.com/docs/fine-tuning "https://docs.cohere.com/docs/fine-tuning").

###### Note

The `epochCount` quota is adjustable.

| Hyperparameter (console) | Hyperparameter (API)   | Definition                                                                                                                                                              | Type    | Minimum | Maximum               | Default |
| ------------------------ | ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ------- | --------------------- | ------- |
| Epochs                   | epochCount             | The number of iterations through the entire training dataset                                                                                                            | integer | 1       | 100                   | 1       |
| Batch size               | batchSize              | The number of samples processed before updating model parameters                                                                                                        | integer | 8       | 8 (Command)32 (Light) | 8       |
| Learning rate            | learningRate           | The rate at which model parameters are updated after each batch. If you use a<br>validation dataset, we recommend that you don't provide a value for<br>`learningRate`. | float   | 5.00E-6 | 0.1                   | 1.00E-5 |
| Early stopping threshold | earlyStoppingThreshold | The minimum improvement in loss required to prevent premature termination of the<br>training process                                                                    | float   | 0       | 0.1                   | 0.01    |
| Early stopping patience  | earlyStoppingPatience  | The tolerance for stagnation in the loss metric before stopping the training<br>process                                                                                 | integer | 1       | 10                    | 6       |
| Evaluation percentage    | evalPercentage         | The percentage of the dataset allocated for model evaluation, if you don't provide<br>a separate validation dataset                                                     | float   | 5       | 50                    | 20      |
