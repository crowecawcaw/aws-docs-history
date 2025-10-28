# Hyperparameters for Creative Content Generation models

The Amazon Nova Canvas model supports the following hyperparameters for model customization. Amazon Nova Reel doesn't support fine-tuning.

| Hyperparameter (console) | Hyperparameter (API) | Definition                                                   | Minimum | Maximum | Default |
| ------------------------ | -------------------- | ------------------------------------------------------------ | ------- | ------- | ------- |
| Batch size               | batchSize            | Number of samples processed before updating model parameters | 8       | 192     | 8       |
| Steps                    | stepCount            | Number of times the model is exposed to each batch           | 10      | 20,000  | 500     |
| Learning rate            | learningRate         | Rate at which model parameters are updated after each batch  | 1.00E-7 | 1.00E-4 | 1.00E-5 |
