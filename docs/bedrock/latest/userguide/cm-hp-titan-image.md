# Amazon Titan Image Generator G1 models customization hyperparameters

The Amazon Titan Image Generator G1 model supports the following hyperparameters for model customization.

###### Note

`stepCount` has no default value and must be specified. `stepCount` supports the value `auto`.
`auto` prioritizes model performance over training cost by automatically determining a number based on the size of your dataset.
Training job costs depend on the number that `auto` determines. To understand how job cost is calculated and to see examples,
see [Amazon Bedrock Pricing](https://aws.amazon.com/bedrock/pricing "https://aws.amazon.com/bedrock/pricing").

| Hyperparameter (console) | Hyperparameter (API) | Definition                                                   | Minimum | Maximum | Default |
| ------------------------ | -------------------- | ------------------------------------------------------------ | ------- | ------- | ------- |
| Batch size               | batchSize            | Number of samples processed before updating model parameters | 8       | 192     | 8       |
| Steps                    | stepCount            | Number of times the model is exposed to each batch           | 10      | 40,000  | N/A     |
| Learning rate            | learningRate         | Rate at which model parameters are updated after each batch  | 1.00E-7 | 1       | 1.00E-5 |
