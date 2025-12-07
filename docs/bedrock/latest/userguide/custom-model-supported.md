# Supported models and Regions for fine-tuning

and continued pre-training

The following table shows the foundation models that you can fine-tune:

| Provider  | Model                          | Model ID                                    | Single-region model support |
| --------- | ------------------------------ | ------------------------------------------- | --------------------------- |
| Amazon    | Nova 2 Lite                    | amazon.nova-2-lite-v1:0:256k                | us-east-1                   |
| Amazon    | Nova Canvas                    | amazon.nova-canvas-v1:0                     | us-east-1                   |
| Amazon    | Nova Lite                      | amazon.nova-lite-v1:0:300k                  | us-east-1                   |
| Amazon    | Nova Micro                     | amazon.nova-micro-v1:0:128k                 | us-east-1                   |
| Amazon    | Nova Pro                       | amazon.nova-pro-v1:0:300k                   | us-east-1                   |
| Amazon    | Titan Image Generator G1       | amazon.titan-image-generator-v1:0           | us-east-1<br>us-west-2      |
| Amazon    | Titan Image Generator G1 v2    | amazon.titan-image-generator-v2:0           | us-east-1<br>us-west-2      |
| Amazon    | Titan Multimodal Embeddings G1 | amazon.titan-embed-image-v1:0               | us-east-1<br>us-west-2      |
| Amazon    | Titan Text G1<br>• Express     | amazon.titan-text-express-v1:0:8k           | us-east-1<br>us-west-2      |
| Amazon    | Titan Text G1<br>• Lite        | amazon.titan-text-lite-v1:0:4k              | us-east-1<br>us-west-2      |
| Anthropic | Claude 3 Haiku                 | anthropic.claude-3-haiku-20240307-v1:0:200k | us-west-2                   |
| Meta      | Llama 3.1 70B Instruct         | meta.llama3-1-70b-instruct-v1:0:128k        | us-west-2                   |
| Meta      | Llama 3.1 8B Instruct          | meta.llama3-1-8b-instruct-v1:0:128k         | us-west-2                   |
| Meta      | Llama 3.2 11B Instruct         | meta.llama3-2-11b-instruct-v1:0:128k        | us-west-2                   |
| Meta      | Llama 3.2 1B Instruct          | meta.llama3-2-1b-instruct-v1:0:128k         | us-west-2                   |
| Meta      | Llama 3.2 3B Instruct          | meta.llama3-2-3b-instruct-v1:0:128k         | us-west-2                   |
| Meta      | Llama 3.2 90B Instruct         | meta.llama3-2-90b-instruct-v1:0:128k        | us-west-2                   |
| Meta      | Llama 3.3 70B Instruct         | meta.llama3-3-70b-instruct-v1:0:128k        | us-west-2                   |

The following table shows the foundation models that you can continuously pre-train:

| Provider | Model                      | Model ID                          | Single-region model support |
| -------- | -------------------------- | --------------------------------- | --------------------------- |
| Amazon   | Titan Text G1<br>• Express | amazon.titan-text-express-v1:0:8k | us-east-1<br>us-west-2      |
| Amazon   | Titan Text G1<br>• Lite    | amazon.titan-text-lite-v1:0:4k    | us-east-1<br>us-west-2      |

For information about model customization hyperparameters for each model, see [Custom model hyperparameters](custom-models-hp.md "custom-models-hp.md").
