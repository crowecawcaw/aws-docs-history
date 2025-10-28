# Using the HyperPod training operator

The Amazon SageMaker HyperPod training operator helps you accelerate generative AI model
development by efficiently managing distributed training across large GPU clusters.
It introduces intelligent fault recovery, hang job detection, and process-level management
capabilities that minimize training disruptions and reduce costs.
Unlike traditional training infrastructure that requires complete job restarts when
failures occur, this operator implements surgical process recovery to keep your training jobs running smoothly.

The operator also works with HyperPod's health monitoring and observability functions,
providing real-time visibility into training execution and automatic monitoring of critical
metrics like loss spikes and throughput degradation. You can define recovery policies through
simple YAML configurations without code changes, allowing you to quickly respond to and recover
from unrecoverable training states. These monitoring and recovery capabilities work together to
maintain optimal training performance while minimizing operational overhead.

While Kueue is not required for this training operator, your cluster administrator can install and
configure it for enhanced job scheduling capabilities. For more information, see the [official
documentation for Kueue](https://kueue.sigs.k8s.io/docs/overview/ "https://kueue.sigs.k8s.io/docs/overview/").

###### Note

To use the training operator, you must use the latest [HyperPod AMI release](sagemaker-hyperpod-release-ami-eks.md "sagemaker-hyperpod-release-ami-eks.md"). To upgrade, use the [UpdateClusterSoftware](../APIReference/API_UpdateClusterSoftware.md "../APIReference/API_UpdateClusterSoftware.md")
API operation. If you use [HyperPod task governance](sagemaker-hyperpod-eks-operate-console-ui-governance.md "sagemaker-hyperpod-eks-operate-console-ui-governance.md"), it must also be the latest version.

## Supported versions

The HyperPod training operator works only work with specific versions of Kubernetes,
Kueue, and HyperPod. See the list below for the complete list of compatible versions.

- Supported Kubernetes versions – 1.28, 1.29, 1.30, 1.31, or 1.32
- Suggested Kueue versions – [v.0.12.2](https://github.com/kubernetes-sigs/kueue/releases/tag/v0.12.2 "https://github.com/kubernetes-sigs/kueue/releases/tag/v0.12.2") and [v.0.12.3](https://github.com/kubernetes-sigs/kueue/releases/tag/v0.12.3 "https://github.com/kubernetes-sigs/kueue/releases/tag/v0.12.3")
- The latest HyperPod AMI release. To upgrade to the latest AMI release,
  use the [UpdateClusterSoftware](../APIReference/API_UpdateClusterSoftware.md "../APIReference/API_UpdateClusterSoftware.md") API.
- [PyTorch 2.4.0 – 2.7.1](https://github.com/pytorch/pytorch/releases "https://github.com/pytorch/pytorch/releases")
