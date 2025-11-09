# Deploy foundation models

and custom fine-tuned models

Whether you're deploying pre-trained foundation open-weights or gated models from
Amazon SageMaker JumpStart or your own custom or fine-tuned models stored in Amazon S3 or Amazon FSx,
SageMaker HyperPod provides the flexible, scalable infrastructure you need for production
inference workloads.

|                        | Deploy open-weights and gated foundation models from<br>JumpStart                                                                                                                                                                             | Deploy custom and fine-tuned models from Amazon S3 and Amazon FSx                                                                                                                                                                                        |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description**        | Deploy from a comprehensive catalog of pre-trained foundation<br>models with automatic optimization and scaling policies tailored to<br>each model family.                                                                                    | Bring your own custom and fine-tuned models and leverage<br>SageMaker HyperPod's enterprise infrastructure for production-scale inference.<br>Choose between cost-effective storage with Amazon S3 or a high-performance<br>file system with Amazon FSx. |
| **Key benefits**       | • One-click deployment through Amazon SageMaker Studio UI<br>• Auto-scaling based on incoming requests automatically<br>enabled<br>• Pre-optimized containers and configurations for each model<br>family<br>• EULA handling for gated models | • Support for multiple storage backends: Amazon S3, Amazon FSx<br>• Flexible container and framework support<br>• Custom scaling policies based on your model's<br>characteristics                                                                       |
| **Deployment options** | • Amazon SageMaker Studio for visual deployment<br>• kubectl for Kubernetes-native operations<br>• Python SDK for programmatic integration<br>• HyperPod CLI for command-line automation                                                      | • kubectl for Kubernetes-native operations<br>• Python SDK for programmatic integration<br>• HyperPod CLI for command-line automation                                                                                                                    |

The following sections step you through deploying models from Amazon SageMaker JumpStart and
from Amazon S3 and Amazon FSx.

###### Topics

- [Deploy models
  from JumpStart using Amazon SageMaker Studio](sagemaker-hyperpod-model-deployment-deploy-js-ui.md "sagemaker-hyperpod-model-deployment-deploy-js-ui.md")
- [Deploy
  models from JumpStart using kubectl](sagemaker-hyperpod-model-deployment-deploy-js-kubectl.md "sagemaker-hyperpod-model-deployment-deploy-js-kubectl.md")
- [Deploy custom
  fine-tuned models from Amazon S3 and Amazon FSx using kubectl](sagemaker-hyperpod-model-deployment-deploy-ftm.md "sagemaker-hyperpod-model-deployment-deploy-ftm.md")

- [Deploy custom fine-tuned models using the
  Python SDK and HPCLI](deploy-trained-model.md "deploy-trained-model.md")
- [Deploy models from Amazon SageMaker JumpStart
  using the Python SDK and HPCLI](deploy-jumpstart-model.md "deploy-jumpstart-model.md")
