# Observability

The SageMaker HyperPod Observability add-on collects Ray metrics and provisions Grafana
dashboards for your Ray workloads. Installing the add-on deploys a collector that scrapes the
Ray head pods, worker pods, and the KubeRay operator. The collector writes the metrics to Amazon Managed
Service for Prometheus, and dashboards are imported into Amazon Managed Grafana. You skip the
manual Prometheus and Grafana setup.

The add-on is not specific to Ray. It also collects cluster metrics for hardware health,
resource utilization, and task performance. The sources include NVIDIA DCGM, Kubernetes node
exporters, Elastic Fabric Adapter, integrated file systems, and Kueue. One installation covers
your Ray workloads and the cluster they run on.

For the general observability setup, see [Observability for Amazon SageMaker HyperPod cluster orchestrated by Amazon EKS](sagemaker-hyperpod-eks-cluster-observability.md "sagemaker-hyperpod-eks-cluster-observability.md").

###### Topics

- [Setting up Ray metrics collection](sagemaker-hyperpod-ray-observability-setup.md "sagemaker-hyperpod-ray-observability-setup.md")
- [Ray Grafana dashboards](sagemaker-hyperpod-ray-observability-dashboards.md "sagemaker-hyperpod-ray-observability-dashboards.md")
- [Ray metrics reference](sagemaker-hyperpod-ray-observability-metrics-reference.md "sagemaker-hyperpod-ray-observability-metrics-reference.md")
