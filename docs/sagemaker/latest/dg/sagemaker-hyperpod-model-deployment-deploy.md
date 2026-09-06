

# Deploy foundation models and custom fine-tuned models
<a name="sagemaker-hyperpod-model-deployment-deploy"></a>

Whether you're deploying pre-trained foundation open-weights or gated models from Amazon SageMaker JumpStart or your own custom or fine-tuned models stored in Amazon S3 or Amazon FSx, SageMaker HyperPod provides the flexible, scalable infrastructure you need for production inference workloads.





|  | Deploy open-weights and gated foundation models from JumpStart | Deploy custom and fine-tuned models from Amazon S3 and Amazon FSx | Deploy models from local NVMe storage | 
| --- | --- | --- | --- | 
| Description | Deploy from a comprehensive catalog of pre-trained foundation models with automatic optimization and scaling policies tailored to each model family. | Bring your own custom and fine-tuned models and use SageMaker HyperPod's enterprise infrastructure for production-scale inference. Choose between cost-effective storage with Amazon S3 or a high-performance file system with Amazon FSx. | Load model weights from a node's local NVMe storage to eliminate network latency during pod startup. Useful for autoscaling events, scale-from-zero workloads, and latency-sensitive failovers. | 
| Key benefits | +  One-click deployment through Amazon SageMaker Studio UI  <br />+  Auto-scaling based on incoming requests automatically enabled <br />+  Pre-optimized containers and configurations for each model family <br />+  EULA handling for gated models  |  +  Support for multiple storage backends: Amazon S3, Amazon FSx <br />+  Flexible container and framework support <br />+  Custom scaling policies based on your model's characteristics   |  +  Reduced cold-start time by reading weights locally <br />+  No network dependency for model loading <br />+  Optional fallback to Amazon S3 when NVMe cache is missing <br />+  Custom Kubernetes volumes and initContainers   | 
| Deployment options |  +  Amazon SageMaker Studio for visual deployment  <br />+  kubectl for Kubernetes-native operations <br />+  Python SDK for programmatic integration  <br />+  HyperPod CLI for command-line automation    |  +  kubectl for Kubernetes-native operations <br />+  Python SDK for programmatic integration  <br />+  HyperPod CLI for command-line automation    |  +  kubectl for Kubernetes-native operations <br />+  Python SDK for programmatic integration  <br />+  HyperPod CLI for command-line automation    | 

The following sections step you through deploying models from Amazon SageMaker JumpStart, from Amazon S3 and Amazon FSx, and from local NVMe storage.

**Topics**
+ [Deploy models from JumpStart using Amazon SageMaker Studio](sagemaker-hyperpod-model-deployment-deploy-js-ui.md)
+ [Deploy models from JumpStart using kubectl](sagemaker-hyperpod-model-deployment-deploy-js-kubectl.md)
+ [Deploy models from Amazon S3, Amazon FSx, or Hugging Face Hub using kubectl](sagemaker-hyperpod-model-deployment-deploy-ftm.md)
+ [Deploy models from local NVMe storage using kubectl](sagemaker-hyperpod-model-deployment-deploy-nvme.md)
+ [Deploy custom fine-tuned models using the Python SDK and HPCLI](deploy-trained-model.md) 
+ [Deploy models from Amazon SageMaker JumpStart using the Python SDK and HPCLI](deploy-jumpstart-model.md) 