# Ray on SageMaker HyperPod

Ray is an open source unified framework for scaling AI and Python applications. It
provides the compute layer for parallel processing, so you do not need to be a distributed
systems expert to run work across a cluster. Ray Core distributes the work, and the Ray AI
libraries cover data processing, distributed training, hyperparameter tuning, reinforcement
learning, and model serving. For more information, see [Overview](https://docs.ray.io/en/latest/ray-overview/index.html "https://docs.ray.io/en/latest/ray-overview/index.html") in the Ray
documentation.

Ray on SageMaker HyperPod runs your Ray workloads on HyperPod compute orchestrated by
Amazon EKS, using the open source KubeRay operator. Your Ray code, the Ray APIs, and the KubeRay
custom resources are unchanged.

Staying fully aligned with open source Ray, HyperPod adds capabilities around it
rather than replacing any part of it:

- A purpose-built web interface to operate Ray workloads in Amazon SageMaker Studio that
  brings all the capabilities below under a single interface.
- Interactive development, where a JupyterLab, Code Editor, or remote IDE session attaches
  to a Ray cluster and `ray.init()` connects.
- Secure Ray Dashboard access through an authenticated browser link, without
  `kubectl port-forward`.
- A managed tiered KV cache that lowers time to first token, JumpStart model
  deployment, and managed Karpenter autoscaling for Ray Serve.
- Team compute allocations, priority-based scheduling, and lending and borrowing of
  idle compute through HyperPod Task Governance.
- Ray metrics and Grafana dashboards provisioned by the HyperPod
  Observability add-on.
- Resilient training with automatic node recovery, hung job detection, and tiered
  checkpointing at the infrastructure layer.
  You can adopt all of this, or install only the capabilities you are missing. For more
  information about the two approaches, see [Getting started](sagemaker-hyperpod-ray-getting-started.md "sagemaker-hyperpod-ray-getting-started.md").

## Prerequisites

Ray on HyperPod requires a HyperPod cluster orchestrated by Amazon EKS.
For more information about creating one, see [Creating a SageMaker HyperPod cluster with Amazon EKS orchestration](sagemaker-hyperpod-eks-operate-console-ui-create-cluster.md "sagemaker-hyperpod-eks-operate-console-ui-create-cluster.md").

## Regions

Ray on HyperPod is available in all AWS Regions where SageMaker HyperPod
supports Amazon EKS orchestration. For the list of Regions, see [AWS Regions supported by SageMaker HyperPod](sagemaker-hyperpod.md#sagemaker-hyperpod-available-regions "sagemaker-hyperpod.md#sagemaker-hyperpod-available-regions").

###### Topics

- [What is Ray](sagemaker-hyperpod-ray-what-is-ray.md "sagemaker-hyperpod-ray-what-is-ray.md")
- [Getting started](sagemaker-hyperpod-ray-getting-started.md "sagemaker-hyperpod-ray-getting-started.md")
- [Installing KubeRay on HyperPod Amazon EKS](sagemaker-hyperpod-ray-install-kuberay.md "sagemaker-hyperpod-ray-install-kuberay.md")
- [Amazon SageMaker Studio (web-based development)](sagemaker-hyperpod-ray-studio.md "sagemaker-hyperpod-ray-studio.md")
- [Managing Ray workloads](sagemaker-hyperpod-ray-manage-workloads.md "sagemaker-hyperpod-ray-manage-workloads.md")
- [IDE and notebooks with Ray](sagemaker-hyperpod-ray-ide-notebooks.md "sagemaker-hyperpod-ray-ide-notebooks.md")
- [Ray Dashboard access and remote job submission](sagemaker-hyperpod-ray-dashboard.md "sagemaker-hyperpod-ray-dashboard.md")
- [Resilient training](sagemaker-hyperpod-ray-resilient-training.md "sagemaker-hyperpod-ray-resilient-training.md")
- [Queueing with task governance](sagemaker-hyperpod-ray-task-governance.md "sagemaker-hyperpod-ray-task-governance.md")
- [Accelerated inference](sagemaker-hyperpod-ray-accelerated-inference.md "sagemaker-hyperpod-ray-accelerated-inference.md")
- [Observability](sagemaker-hyperpod-ray-observability.md "sagemaker-hyperpod-ray-observability.md")
- [Reference](sagemaker-hyperpod-ray-reference.md "sagemaker-hyperpod-ray-reference.md")
