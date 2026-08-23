# Getting started

Ray on HyperPod runs on the open source KubeRay operator and its custom
resources, unchanged. To get started you need only a HyperPod cluster orchestrated
by Amazon EKS and the KubeRay operator installed on it. HyperPod then adds features
around Ray that you adopt in one of two ways.

## Get started

These two steps are all you need to run Ray on HyperPod.

1. Create a HyperPod cluster orchestrated by Amazon EKS. For more
   information, see [Creating a SageMaker HyperPod cluster with Amazon EKS orchestration](sagemaker-hyperpod-eks-operate-console-ui-create-cluster.md "sagemaker-hyperpod-eks-operate-console-ui-create-cluster.md").
2. Install the KubeRay operator on the cluster. It manages every Ray custom
   resource. For more information, see [Installing KubeRay on HyperPod Amazon EKS](sagemaker-hyperpod-ray-install-kuberay.md "sagemaker-hyperpod-ray-install-kuberay.md").

## Ray features on HyperPod

HyperPod adds features around Ray, and there are two ways to adopt them. The
setup is the same either way, and both run the same open source Ray and the same KubeRay
custom resources. What differs is how your teams consume the features, and you can start
with one and add the other later.

**Purpose-built data scientist experience.**
Amazon SageMaker Studio brings these features together in one interface. You create and manage
Ray clusters, develop interactively in an attached space, reach the Ray Dashboard
through a browser link, and open Grafana dashboards, without writing Kubernetes
manifests. Set up Amazon SageMaker Studio for Ray first. For more information, see [Setting up Studio for Ray](sagemaker-hyperpod-ray-studio-setup.md "sagemaker-hyperpod-ray-studio-setup.md"). You can then opt in to each feature
individually, such as the SageMaker AI Spaces add-on for interactive development and the
HyperPod Observability add-on for dashboards.

**Integrating capabilities into your existing internal ML
platform.** Choose this if you run your own internal ML platform on Amazon EKS
and want to keep your tooling and workflows. You attach HyperPod compute to
your Amazon EKS cluster and adopt only the capabilities you are missing. Nothing requires
Amazon SageMaker Studio. Each capability is a separate add-on or a Python package, so you can
adopt one and stop.

Every feature is available both ways. The purpose-built experience wraps each one in a
web interface, and on your own platform you drive the same features with
`kubectl`.

| Feature                                                                                                                                                                                | Purpose-built experience in Amazon SageMaker Studio                                                     | Your own platform                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| [Managing Ray<br>workloads](sagemaker-hyperpod-ray-manage-workloads.md "sagemaker-hyperpod-ray-manage-workloads.md")                                                                   | Create and manage Ray clusters in the Amazon SageMaker Studio web<br>interface                          | `kubectl` and your own `RayCluster`<br>manifests   |
| [IDE and<br>notebooks](sagemaker-hyperpod-ray-ide-notebooks.md "sagemaker-hyperpod-ray-ide-notebooks.md")                                                                              | Web UI to create Ray development environments                                                           | Attach a space with `kubectl`                      |
| [Ray Dashboard access<br>and job submission](sagemaker-hyperpod-ray-dashboard.md "sagemaker-hyperpod-ray-dashboard.md")                                                                | One-click authenticated access and remote job submission from<br>Studio space notebooks and Code Editor | `kubectl` commands to generate Ray Dashboard links |
| [Observability](sagemaker-hyperpod-ray-observability.md "sagemaker-hyperpod-ray-observability.md")                                                                                     | Grafana dashboards from the HyperPod Observability<br>add-on                                            | The same add-on, or your own Prometheus            |
| Resource sharing and job queueing with [Task<br>governance](sagemaker-hyperpod-ray-task-governance.md "sagemaker-hyperpod-ray-task-governance.md")                                     | View resource allocation metrics during Ray workload creation and<br>submit to a queue from the UI      | via `kubectl`                                      |
| [Resilient<br>training](sagemaker-hyperpod-ray-resilient-training.md "sagemaker-hyperpod-ray-resilient-training.md") (node auto recovery, hung job detection, tiered<br>checkpointing) | Supported at the infrastructure layer                                                                   | Supported at the infrastructure layer              |
| [Accelerated<br>inference](sagemaker-hyperpod-ray-accelerated-inference.md "sagemaker-hyperpod-ray-accelerated-inference.md") (Ray Serve, managed tiered KV cache,<br>autoscaling)     | Supported at the infrastructure layer                                                                   | Supported at the infrastructure layer              |
