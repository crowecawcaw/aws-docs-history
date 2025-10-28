# Amazon Titan Multimodal Embeddings G1 customization

hyperparameters

The Amazon Titan Multimodal Embeddings G1 model supports the following hyperparameters for model customization. The number of epochs you specify increases your model customization cost by processing more tokens. Each epoch processes the entire training dataset once. For information about pricing, see [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing "https://aws.amazon.com/bedrock/pricing").

###### Note

`epochCount` has no default value and must be specified. `epochCount` supports the value `Auto`. `Auto` prioritizes model performance over training cost by automatically determining a number based on the size of your dataset. Training job costs depend on the number that `Auto` determines. To understand how job cost is calculated and to see examples, see [Amazon Bedrock Pricing](https://aws.amazon.com/bedrock/pricing "https://aws.amazon.com/bedrock/pricing").

| Hyperparameter (console) | Hyperparameter (API) | Definition                                                       | Type    | Minimum | Maximum | Default |
| ------------------------ | -------------------- | ---------------------------------------------------------------- | ------- | ------- | ------- | ------- |
| Epochs                   | epochCount           | The number of iterations through the entire training dataset     | integer | 1       | 100     | N/A     |
| Batch size               | batchSize            | The number of samples processed before updating model parameters | integer | 256     | 9,216   | 576     |
| Learning rate            | learningRate         | The rate at which model parameters are updated after each batch  | float   | 5.00E-8 | 1       | 5.00E-5 |
