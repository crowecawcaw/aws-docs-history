# Meta Llama 3.2 model customization hyperparameters

The Meta Llama 3.2 1B, 3B, 11B, and 90B models support the following hyperparameters for model
customization. The number of epochs you specify increases your model customization cost by processing more tokens. Each epoch processes the entire training dataset once. For information about pricing, see [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing "https://aws.amazon.com/bedrock/pricing"). For more information, see [Customize your model to improve its performance for your use case](custom-models.md "custom-models.md").

For information about fine tuning Meta Llama models, see the Meta documentation at [https://ai.meta.com/llama/get-started/#fine-tuning](https://ai.meta.com/llama/get-started/#fine-tuning "https://ai.meta.com/llama/get-started/#fine-tuning").

| Hyperparameter (console) | Hyperparameter (API) | Definition                                                       | Minimum | Maximum | Default |
| ------------------------ | -------------------- | ---------------------------------------------------------------- | ------- | ------- | ------- |
| Epochs                   | epochCount           | The number of iterations through the entire training dataset     | 1       | 10      | 5       |
| Batch size               | batchSize            | The number of samples processed before updating model parameters | 1       | 1       | 1       |
| Learning rate            | learningRate         | The rate at which model parameters are updated after each batch  | 5.00E-6 | 0.1     | 1.00E-4 |
