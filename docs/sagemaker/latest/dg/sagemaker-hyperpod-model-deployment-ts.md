

# HyperPod inference troubleshooting
<a name="sagemaker-hyperpod-model-deployment-ts"></a>

This troubleshooting guide addresses common issues that can occur during Amazon SageMaker HyperPod inference deployment and operation. These problems typically involve VPC networking configuration, IAM permissions, Kubernetes resource management, and operator connectivity issues that can prevent successful model deployment or cause deployments to fail or remain in pending states.

This troubleshooting guide uses the following terminology: **Troubleshooting steps** are diagnostic procedures to identify and investigate problems, **Resolution** provides the specific actions to fix identified issues, and **Verification** confirms that the solution worked correctly.

**Topics**
+ [Inference operator installation failures through SageMaker AI console](sagemaker-hyperpod-model-deployment-ts-console-cfn-failures.md)
+ [Inference operator installation failures through AWS CLI](sagemaker-hyperpod-model-deployment-ts-cli.md)
+ [Certificate download timeout](sagemaker-hyperpod-model-deployment-ts-certificate.md)
+ [Model deployment issues](sagemaker-hyperpod-model-deployment-ts-deployment-issues.md)
+ [VPC ENI permission issue](sagemaker-hyperpod-model-deployment-ts-permissions.md)
+ [IAM trust relationship issue](sagemaker-hyperpod-model-deployment-ts-trust.md)
+ [Missing NVIDIA GPU plugin error](sagemaker-hyperpod-model-deployment-ts-gpu.md)
+ [Inference operator fails to start](sagemaker-hyperpod-model-deployment-ts-startup.md)
+ [Hugging Face Hub model deployment failures](sagemaker-hyperpod-model-deployment-ts-huggingface.md)
+ [Disaggregated Prefill and Decode (DPD) deployment issues](sagemaker-hyperpod-model-deployment-ts-dpd.md)