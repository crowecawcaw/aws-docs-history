

# SageMaker Inference
<a name="nova-model-sagemaker-inference"></a>

Custom Amazon Nova models are now available on SageMaker inference. With Amazon Nova on SageMaker, you can start getting predictions, or inferences, from your trained custom Amazon Nova models. SageMaker provides a broad selection of ML infrastructure and model deployment options to help meet all your ML inference needs. With SageMaker inference, you can scale your model deployment, manage models more effectively in production, and reduce operational burden.

SageMaker provides you with various inference options, such as real-time endpoints for getting low latency inference, and asynchronous endpoints for batches of requests. By leveraging the appropriate inference option for your use case, you can ensure efficient model deployment and inference. For more information on SageMaker inference, see [Deploy models for inference](https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model.html).

**Important**  
Only full-rank custom models and LoRA-merged models are supported on SageMaker inference. For unmerged LoRA models and base models, use Amazon Bedrock.

## Features
<a name="nova-sagemaker-inference-features"></a>

The following features are available for Amazon Nova models on SageMaker inference:

**Model Capabilities**
+ Text generation

**Deployment and Scaling**
+ Real-time endpoints with custom instance selection
+ Auto Scaling – Automatically adjust capacity based on traffic patterns to optimize costs and GPU utilization. For more information, see [Automatically Scale Amazon SageMaker Models](https://docs.aws.amazon.com/sagemaker/latest/dg/endpoint-auto-scaling.html).
+ Streaming API support for real-time token generation

**Monitoring and Optimization**
+ Amazon CloudWatch integration for monitoring and alerts
+ Availability Zone-aware latency optimization through VPC configuration

**Development Tools**
+ AWS CLI support – For more information, see [AWS CLI Command Reference for SageMaker](https://docs.aws.amazon.com/cli/latest/reference/sagemaker/).
+ Jupyter Notebook integration via SDK support

## Supported models and instances
<a name="nova-sagemaker-inference-supported"></a>

When creating your SageMaker inference endpoints, you can set two environment variables to configure your deployment: `CONTEXT_LENGTH` and `MAX_CONCURRENCY`.
+ `CONTEXT_LENGTH` – Maximum total token length (input \+ output) per request
+ `MAX_CONCURRENCY` – Maximum number of concurrent requests the endpoint will serve

The following table lists the supported Amazon Nova models, instance types, and supported configurations. The MAX\_CONCURRENCY values represent the maximum supported concurrency for each CONTEXT\_LENGTH setting:




- **Amazon Nova Micro**
  - **Instance Type:** ml.g5.12xlarge / **Supported Configurations:** CONTEXT\_LENGTH: 4000, MAX\_CONCURRENCY: 12<br />CONTEXT\_LENGTH: 8000, MAX\_CONCURRENCY: 6 / **FP8 Quantization Required:** No
  - **Instance Type:** ml.g5.24xlarge / **Supported Configurations:** CONTEXT\_LENGTH: 8000, MAX\_CONCURRENCY: 8 / **FP8 Quantization Required:** No
  - **Instance Type:** ml.g6e.xlarge / **Supported Configurations:** CONTEXT\_LENGTH: 8000, MAX\_CONCURRENCY: 2 / **FP8 Quantization Required:** No
  - **Instance Type:** ml.g6e.2xlarge / **Supported Configurations:** CONTEXT\_LENGTH: 8000, MAX\_CONCURRENCY: 2 / **FP8 Quantization Required:** No
  - **Instance Type:** ml.g6e.4xlarge / **Supported Configurations:** CONTEXT\_LENGTH: 8000, MAX\_CONCURRENCY: 4 / **FP8 Quantization Required:** No
  - **Instance Type:** ml.g6.12xlarge / **Supported Configurations:** CONTEXT\_LENGTH: 4000, MAX\_CONCURRENCY: 12<br />CONTEXT\_LENGTH: 8000, MAX\_CONCURRENCY: 6 / **FP8 Quantization Required:** No
  - **Instance Type:** ml.g6.24xlarge / **Supported Configurations:** CONTEXT\_LENGTH: 8000, MAX\_CONCURRENCY: 8 / **FP8 Quantization Required:** No
  - **Instance Type:** ml.g6.48xlarge / **Supported Configurations:** CONTEXT\_LENGTH: 8000, MAX\_CONCURRENCY: 12 / **FP8 Quantization Required:** No
  - **Instance Type:** ml.p5.48xlarge / **Supported Configurations:** CONTEXT\_LENGTH: 16000, MAX\_CONCURRENCY: 128<br />CONTEXT\_LENGTH: 64000, MAX\_CONCURRENCY: 32<br />CONTEXT\_LENGTH: 128000, MAX\_CONCURRENCY: 8 / **FP8 Quantization Required:** No

- **Amazon Nova Lite**
  - **Instance Type:** ml.g6.12xlarge / **Supported Configurations:** CONTEXT\_LENGTH: 8000, MAX\_CONCURRENCY: 2 / **FP8 Quantization Required:** Yes - Enabled By Default
  - **Instance Type:** ml.g6.24xlarge / **Supported Configurations:** CONTEXT\_LENGTH: 8000, MAX\_CONCURRENCY: 4 / **FP8 Quantization Required:** Yes - Enabled By Default
  - **Instance Type:** ml.g6.48xlarge / **Supported Configurations:** CONTEXT\_LENGTH: 4000, MAX\_CONCURRENCY: 16<br />CONTEXT\_LENGTH: 8000, MAX\_CONCURRENCY: 8 / **FP8 Quantization Required:** No
  - **Instance Type:** ml.p5.48xlarge / **Supported Configurations:** CONTEXT\_LENGTH: 16000, MAX\_CONCURRENCY: 128<br />CONTEXT\_LENGTH: 60000, MAX\_CONCURRENCY: 8 / **FP8 Quantization Required:** No

- **Nova 2 Lite**
  - **Instance Type:** ml.g6.48xlarge / **Supported Configurations:** CONTEXT\_LENGTH: 8000, MAX\_CONCURRENCY: 8 / **FP8 Quantization Required:** Yes - Enabled By Default
  - **Instance Type:** ml.p5.48xlarge / **Supported Configurations:** CONTEXT\_LENGTH: 16000, MAX\_CONCURRENCY: 128<br />CONTEXT\_LENGTH: 64000, MAX\_CONCURRENCY: 32<br />CONTEXT\_LENGTH: 128000, MAX\_CONCURRENCY: 8<br />CONTEXT\_LENGTH: 256000, MAX\_CONCURRENCY: 2 / **FP8 Quantization Required:** No



**Note**  
For instances where FP8 quantization is required, it will be enabled by default.  
The MAX\_CONCURRENCY values shown are upper bounds for each CONTEXT\_LENGTH setting. You can use lower context lengths with the same concurrency, but exceeding these values will cause SageMaker endpoint creation to fail.  
For example, on Amazon Nova Micro with a ml.g5.12xlarge:  
`CONTEXT_LENGTH=2000`, `MAX_CONCURRENCY=12` → Valid
`CONTEXT_LENGTH=8000`, `MAX_CONCURRENCY=12` → Rejected (concurrency limit is 6 at context length 8000)
`CONTEXT_LENGTH=8000`, `MAX_CONCURRENCY=4` → Valid
`CONTEXT_LENGTH=8000`, `MAX_CONCURRENCY=6` → Valid
`CONTEXT_LENGTH=10000` → Rejected (max context length is 8000 on this instance)

## Inference components
<a name="nova-sagemaker-inference-components"></a>

You can deploy Amazon Nova models using SageMaker inference components, which allow you to host multiple models on a single endpoint and optimize resource utilization. Inference components let you specify the compute resources (CPU, memory, GPU) required for each model, enabling efficient multi-model hosting on shared infrastructure.

The following table lists the minimum compute resource requirements for each Amazon Nova model when using inference components:



| Model | Min CPU Cores | Min Memory (MB) | Min GPU Count | 
| --- | --- | --- | --- | 
| Amazon Nova Micro | 15 | 25000 | 4 | 
| Amazon Nova Lite | 20 | 35000 | 4 | 
| Nova 2 Lite | 20 | 100000 | 4 | 

**Note**  
The `ComputeResourceRequirements` values must meet or exceed the minimum requirements listed in the table above for the model you are deploying. Using values below the minimums will cause the inference component creation to fail.  
You can deploy multiple inference components on the same endpoint, as long as the total resource requirements do not exceed the capacity of the instance.  
The number of inference components you can host on a single endpoint depends on the instance type's available resources and each model's minimum requirements. For example, on a `ml.p5.48xlarge` (8 GPUs, 192 vCPUs, \~1 TB memory):  
1 Amazon Nova Micro inference component (4 GPUs, 15 CPU cores, 25000 MB) → Valid
2 Amazon Nova Micro inference components (8 GPUs total, 30 CPU cores, 50000 MB) → Valid (fits within instance capacity)
1 Nova 2 Lite inference component (4 GPUs, 20 CPU cores, 100000 MB) → Valid
2 Nova 2 Lite inference components (8 GPUs total, 40 CPU cores, 200000 MB) → Valid
3 Amazon Nova Micro inference components (12 GPUs total) → Rejected (exceeds 8 available GPUs)

## Supported AWS Regions
<a name="nova-sagemaker-inference-regions"></a>

The following table lists the AWS Regions where Amazon Nova models are available on SageMaker inference:



| Region Name | Region Code | Availability | 
| --- | --- | --- | 
| US East (N. Virginia) | us-east-1 | Available | 
| US West (Oregon) | us-west-2 | Available | 

## Supported Container Images
<a name="nova-sagemaker-inference-container-images"></a>

The following table lists the container image URIs for Amazon Nova models on SageMaker inference by region. The `SM-Inference-latest` tag currently points to `v1.4`.



| Region | Container Image URIs | 
| --- | --- | 
| us-east-1 | 708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-inference-repo:SM-Inference-latest | 
| us-west-2 | 176779409107.dkr.ecr.us-west-2.amazonaws.com/nova-inference-repo:SM-Inference-latest | 

## Best Practices
<a name="nova-sagemaker-inference-best-practices"></a>

For best practices on deploying and managing models on SageMaker, see [Best Practices for SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/best-practices.html).

## Support
<a name="nova-sagemaker-inference-support"></a>

For issues and support with Amazon Nova models on SageMaker inference, contact AWS Support through the Console or your AWS account manager.

**Topics**
+ [Features](#nova-sagemaker-inference-features)
+ [Supported models and instances](#nova-sagemaker-inference-supported)
+ [Inference components](#nova-sagemaker-inference-components)
+ [Supported AWS Regions](#nova-sagemaker-inference-regions)
+ [Supported Container Images](#nova-sagemaker-inference-container-images)
+ [Best Practices](#nova-sagemaker-inference-best-practices)
+ [Support](#nova-sagemaker-inference-support)
+ [Getting Started](nova-sagemaker-inference-getting-started.md)
+ [Inference Container Features](nova-sagemaker-inference-container-features.md)
+ [API Reference](nova-sagemaker-inference-api-reference.md)
+ [Deployment of Amazon Nova Forge Models in Amazon SageMaker Inference abuse detection](nova-sagemaker-inference-abuse-detection.md)