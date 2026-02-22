# SageMaker Inference

Custom Amazon Nova models are now available on SageMaker inference. With Amazon Nova on SageMaker, you can start getting predictions, or inferences, from your trained custom Amazon Nova models. SageMaker provides a broad selection of ML infrastructure and model deployment options to help meet all your ML inference needs. With SageMaker inference, you can scale your model deployment, manage models more effectively in production, and reduce operational burden.

SageMaker provides you with various inference options, such as real-time endpoints for getting low latency inference, and asynchronous endpoints for batches of requests. By leveraging the appropriate inference option for your use case, you can ensure efficient model deployment and inference. For more information on SageMaker inference, see [Deploy models for inference](../../../sagemaker/latest/dg/deploy-model.md "../../../sagemaker/latest/dg/deploy-model.md").

###### Important

Only full-rank custom models and LoRA-merged models are supported on SageMaker inference. For unmerged LoRA models and base models, use Amazon Bedrock.

## Features

The following features are available for Amazon Nova models on SageMaker inference:

**Model Capabilities**

- Text generation

**Deployment and Scaling**

- Real-time endpoints with custom instance selection
- Auto Scaling – Automatically adjust capacity based on traffic patterns to optimize costs and GPU utilization. For more information, see [Automatically Scale Amazon SageMaker Models](../../../sagemaker/latest/dg/endpoint-auto-scaling.md "../../../sagemaker/latest/dg/endpoint-auto-scaling.md").
- Streaming API support for real-time token generation

**Monitoring and Optimization**

- Amazon CloudWatch integration for monitoring and alerts
- Availability Zone-aware latency optimization through VPC configuration

**Development Tools**

- AWS CLI support – For more information, see [AWS CLI Command Reference for SageMaker](../../../cli/latest/reference/sagemaker.md "../../../cli/latest/reference/sagemaker.md").
- Notebook integration via SDK support

## Supported models and instances

When creating your SageMaker inference endpoints, you can set two environment variables to configure your deployment: `CONTEXT_LENGTH` and `MAX_CONCURRENCY`.

- `CONTEXT_LENGTH` – Maximum total token length (input + output) per request
- `MAX_CONCURRENCY` – Maximum number of concurrent requests the endpoint will serve

The following table lists the supported Amazon Nova models, instance types, and supported configurations. The MAX_CONCURRENCY values represent the maximum supported concurrency for each CONTEXT_LENGTH setting:

| Model             | Instance Type                                                                                                                       | Supported Configurations                                                                                                            |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Amazon Nova Micro | ml.g5.12xlarge                                                                                                                      | CONTEXT_LENGTH: 4000, MAX_CONCURRENCY: 32<br>CONTEXT_LENGTH: 8000, MAX_CONCURRENCY: 16                                              |
| ml.g5.24xlarge    | CONTEXT_LENGTH: 8000, MAX_CONCURRENCY: 32                                                                                           |
| ml.g6.12xlarge    | CONTEXT_LENGTH: 4000, MAX_CONCURRENCY: 32<br>CONTEXT_LENGTH: 8000, MAX_CONCURRENCY: 16                                              |
| ml.g6.24xlarge    | CONTEXT_LENGTH: 8000, MAX_CONCURRENCY: 32                                                                                           |
| ml.g6.48xlarge    | CONTEXT_LENGTH: 8000, MAX_CONCURRENCY: 32                                                                                           |
| ml.p5.48xlarge    | CONTEXT_LENGTH: 8000, MAX_CONCURRENCY: 32<br>CONTEXT_LENGTH: 16000, MAX_CONCURRENCY: 2<br>CONTEXT_LENGTH: 24000, MAX_CONCURRENCY: 1 |
| Amazon Nova Lite  | ml.g6.48xlarge                                                                                                                      | CONTEXT_LENGTH: 4000, MAX_CONCURRENCY: 32<br>CONTEXT_LENGTH: 8000, MAX_CONCURRENCY: 16                                              |
| ml.p5.48xlarge    | CONTEXT_LENGTH: 8000, MAX_CONCURRENCY: 32<br>CONTEXT_LENGTH: 16000, MAX_CONCURRENCY: 2<br>CONTEXT_LENGTH: 24000, MAX_CONCURRENCY: 1 |
| Nova 2 Lite       | ml.p5.48xlarge                                                                                                                      | CONTEXT_LENGTH: 8000, MAX_CONCURRENCY: 32<br>CONTEXT_LENGTH: 16000, MAX_CONCURRENCY: 2<br>CONTEXT_LENGTH: 24000, MAX_CONCURRENCY: 1 |

###### Note

The MAX_CONCURRENCY values shown are upper bounds for each CONTEXT_LENGTH setting. You can use lower context lengths with the same concurrency, but exceeding these values will cause SageMaker endpoint creation to fail.

For example, on Amazon Nova Micro with a ml.g5.12xlarge:

- `CONTEXT_LENGTH=2000`, `MAX_CONCURRENCY=32` → Valid
- `CONTEXT_LENGTH=8000`, `MAX_CONCURRENCY=32` → Rejected (concurrency limit is 16 at context length 8000)
- `CONTEXT_LENGTH=8000`, `MAX_CONCURRENCY=4` → Valid
- `CONTEXT_LENGTH=8000`, `MAX_CONCURRENCY=16` → Valid
- `CONTEXT_LENGTH=10000` → Rejected (max context is 8000 on this instance)

## Supported AWS Regions

The following table lists the AWS Regions where Amazon Nova models are available on SageMaker inference:

| Region Name           | Region Code | Availability |
| --------------------- | ----------- | ------------ |
| US East (N. Virginia) | us-east-1   | Available    |
| US West (Oregon)      | us-west-2   | Available    |

## Supported Container Images

The following table lists the container image URIs for Amazon Nova models on SageMaker inference by region. Two image tags are available for each region: a versioned tag (`v1.0.0`) and a latest tag (`SM-Inference-latest`). For production deployments, we recommend using the versioned tag.

| Region    | Container Image URIs                                                                                                                                                |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| us-east-1 | `708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-inference-repo:v1.0.0`<br>`708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-inference-repo:SM-Inference-latest` |
| us-west-2 | `176779409107.dkr.ecr.us-west-2.amazonaws.com/nova-inference-repo:v1.0.0`<br>`176779409107.dkr.ecr.us-west-2.amazonaws.com/nova-inference-repo:SM-Inference-latest` |

## Best Practices

For best practices on deploying and managing models on SageMaker, see [Best Practices for SageMaker](../../../sagemaker/latest/dg/best-practices.md "../../../sagemaker/latest/dg/best-practices.md").

## Support

For issues and support with Amazon Nova models on SageMaker inference, contact AWS Support through the Console or your AWS account manager.

###### Topics

- [Getting Started](nova-sagemaker-inference-getting-started.md "nova-sagemaker-inference-getting-started.md")
- [API Reference](nova-sagemaker-inference-api-reference.md "nova-sagemaker-inference-api-reference.md")
- [Evaluate Models Hosted on SageMaker Inference](nova-eval-on-sagemaker-inference.md "nova-eval-on-sagemaker-inference.md")
