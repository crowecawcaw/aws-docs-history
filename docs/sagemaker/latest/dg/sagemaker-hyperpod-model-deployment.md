# Deploying models on

Amazon SageMaker HyperPod

Amazon SageMaker HyperPod now extends beyond training to deliver a comprehensive inference platform
that combines the flexibility of Kubernetes with the operational excellence of AWS managed
services. Deploy, scale, and optimize your machine learning models with enterprise-grade
reliability using the same HyperPod compute throughout the entire model
lifecycle.

Amazon SageMaker HyperPod offers flexible deployment interfaces that allow you to deploy models
through multiple methods including kubectl, Python SDK, Amazon SageMaker Studio UI, or HyperPod CLI.
The service provides advanced autoscaling capabilities with dynamic resource allocation that
automatically adjusts based on demand. Additionally, it includes comprehensive observability
and monitoring features that track critical metrics such as time-to-first-token, latency,
and GPU utilization to help you optimize performance.

**Unified infrastructure for training and inference**

Maximize your GPU utilization by seamlessly transitioning compute resources between
training and inference workloads. This reduces the total cost of ownership while maintaining
operational continuity.

**Enterprise-ready deployment options**

Deploy models from multiple sources including open-weights and gated models from
Amazon SageMaker JumpStart and custom models from Amazon S3 and Amazon FSx with support for both single-node
and multi-node inference architectures.

###### Topics

- [Setting up your
  HyperPod clusters for model deployment](sagemaker-hyperpod-model-deployment-setup.md "sagemaker-hyperpod-model-deployment-setup.md")
- [Deploy foundation models
  and custom fine-tuned models](sagemaker-hyperpod-model-deployment-deploy.md "sagemaker-hyperpod-model-deployment-deploy.md")
- [Autoscaling policies
  for your HyperPod inference model deployment](sagemaker-hyperpod-model-deployment-autoscaling.md "sagemaker-hyperpod-model-deployment-autoscaling.md")
- [Implementing
  inference observability on HyperPod clusters](sagemaker-hyperpod-model-deployment-observability.md "sagemaker-hyperpod-model-deployment-observability.md")
- [Task governance for model
  deployment on HyperPod](sagemaker-hyperpod-model-deployment-task-gov.md "sagemaker-hyperpod-model-deployment-task-gov.md")
- [HyperPod inference
  troubleshooting](sagemaker-hyperpod-model-deployment-ts.md "sagemaker-hyperpod-model-deployment-ts.md")
