

# SageMaker HyperPod cluster metrics
<a name="hyperpod-observability-cluster-metrics"></a>

Amazon SageMaker HyperPod (SageMaker HyperPod) publishes various metrics across 9 distinct categories to your Amazon Managed Service for Prometheus workspace. Not all metrics are enabled by default or displayed in your Amazon Managed Grafana workspace. The following table shows which metrics are enabled by default when you install the observability add-on, which categories have additional metrics that can be enabled for more granular cluster information, and where they appear in the Amazon Managed Grafana workspace.


| Metric category | Enabled by default? | Additional advanced metrics available? | Available under which Grafana dashboards? | 
| --- | --- | --- | --- | 
| Training metrics | Yes | Yes | Training | 
| Inference metrics | Yes | No | Inference | 
| Task governance metrics | No | Yes | None. Query your Amazon Managed Service for Prometheus workspace to build your own dashboard. | 
| Scaling metrics | No | Yes | None. Query your Amazon Managed Service for Prometheus workspace to build your own dashboard. | 
| Cluster metrics | Yes | Yes | Cluster | 
| Instance metrics | Yes | Yes | Cluster | 
| Accelerated compute metrics | Yes | Yes | Task, Cluster | 
| Network metrics | No | Yes | Cluster | 
| File system | Yes | No | File system | 

The following tables describe the metrics available for monitoring your SageMaker HyperPod cluster, organized by category.

## Metrics availability on Restricted Instance Groups
<a name="hyperpod-observability-rig-metrics-availability"></a>

When your cluster contains Restricted Instance Groups, most metrics categories are available on restricted nodes with the following exceptions and considerations. You can also set up alerting on any metric of your choice.


| Metric category | Available on RIG nodes? | Notes | 
| --- | --- | --- | 
| Training metrics | Yes | Kubeflow and Kubernetes pod metrics are collected. Advanced training KPI metrics (from Training Metrics Agent) are not available from the RIG nodes. | 
| Inference metrics | No | Inference workloads are not supported on Restricted Instance Groups. | 
| Task governance metrics | No | Kueue metrics are collected from the standard nodes only, if any. | 
| Scaling metrics | No | KEDA metrics are collected from the standard nodes only, if any. | 
| Cluster metrics | Yes | Kube State Metrics and API server metrics are available. Kube State Metrics is preferentially scheduled on standard nodes but can run on restricted nodes in RIG-only clusters. | 
| Instance metrics | Yes | Node Exporter and cAdvisor metrics are collected on all nodes including restricted nodes. | 
| Accelerated compute metrics | Yes | DCGM Exporter runs on GPU-enabled restricted nodes. Neuron Monitor runs on Neuron-enabled restricted nodes when advanced mode is enabled. | 
| Network metrics | Yes | EFA Exporter runs on EFA-enabled restricted nodes when advanced mode is enabled. | 
| File system metrics | Yes | FSx for Lustre cluster utilization metrics are supported on Restricted Instance Groups. | 

**Note**  
Container log collection with Fluent Bit is not deployed on restricted nodes. Cluster logs from restricted nodes are available through the SageMaker HyperPod platform independently of the observability add-on. You can view these logs in the Cluster Logs dashboard.

## Training metrics
<a name="hyperpod-observability-training-metrics"></a>

Use these metrics to track the performance of training tasks executed on the SageMaker HyperPod cluster.


| Metric name or type | Description | Enabled by default? | Metric source | 
| --- | --- | --- | --- | 
| Kubeflow metrics | [https://github.com/kubeflow/trainer](https://github.com/kubeflow/trainer) | Yes | Kubeflow | 
| Kubernetes pod metrics | [https://github.com/kubernetes/kube-state-metrics](https://github.com/kubernetes/kube-state-metrics) | Yes | Kubernetes | 
| training\_uptime\_percentage | Percentage of training time out of the total window size | No | SageMaker HyperPod training operator | 
| training\_manual\_recovery\_count | Total number of manual restarts performed on the job | No | SageMaker HyperPod training operator | 
| training\_manual\_downtime\_ms | Total time in milliseconds the job was down due to manual interventions | No | SageMaker HyperPod training operator | 
| training\_auto\_recovery\_count | Total number of automatic recoveries | No | SageMaker HyperPod training operator | 
| training\_auto\_recovery\_downtime | Total infrastructure overhead time in milliseconds during fault recovery | No | SageMaker HyperPod training operator | 
| training\_fault\_count | Total number of faults encountered during training | No | SageMaker HyperPod training operator | 
| training\_fault\_type\_count | Distribution of faults by type | No | SageMaker HyperPod training operator | 
| training\_fault\_recovery\_time\_ms | Recovery time in milliseconds for each type of fault | No | SageMaker HyperPod training operator | 
| training\_time\_ms | Total time in milliseconds spent in actual training | No | SageMaker HyperPod training operator | 

## Inference metrics
<a name="hyperpod-observability-inference-metrics"></a>

Use these metrics to track the performance of inference tasks on the SageMaker HyperPod cluster.


| Metric name or type | Description | Enabled by default? | Metric source | 
| --- | --- | --- | --- | 
| model\_invocations\_total | Total number of invocation requests to the model | Yes | SageMaker HyperPod inference operator | 
| model\_errors\_total | Total number of errors during model invocation | Yes | SageMaker HyperPod inference operator | 
| model\_concurrent\_requests | Active concurrent model requests | Yes | SageMaker HyperPod inference operator | 
| model\_latency\_milliseconds | Model invocation latency in milliseconds | Yes | SageMaker HyperPod inference operator | 
| model\_ttfb\_milliseconds | Model time to first byte latency in milliseconds | Yes | SageMaker HyperPod inference operator | 
| TGI | These metrics can be used to monitor the performance of TGI, auto-scale deployment and to help identify bottlenecks. For a detailed list of metrics, see [https://github.com/deepjavalibrary/djl-serving/blob/master/prometheus/README.md](https://github.com/deepjavalibrary/djl-serving/blob/master/prometheus/README.md). | Yes | Model container | 
| LMI | These metrics can be used to monitor the performance of LMI, and to help identify bottlenecks. For a detailed list of metrics, see [https://github.com/deepjavalibrary/djl-serving/blob/master/prometheus/README.md](https://github.com/deepjavalibrary/djl-serving/blob/master/prometheus/README.md). | Yes | Model container | 

## Task governance metrics
<a name="hyperpod-observability-task-governance-metrics"></a>

Use these metrics to monitor task governance and resource allocation on the SageMaker HyperPod cluster.


| Metric name or type | Description | Enabled by default? | Metric source | 
| --- | --- | --- | --- | 
| Kueue | See [https://kueue.sigs.k8s.io/docs/reference/metrics/](https://kueue.sigs.k8s.io/docs/reference/metrics/). | No | Kueue | 

## Scaling metrics
<a name="hyperpod-observability-scaling-metrics"></a>

Use these metrics to monitor auto-scaling behavior and performance on the SageMaker HyperPod cluster.


| Metric name or type | Description | Enabled by default? | Metric source | 
| --- | --- | --- | --- | 
| KEDA Operator Metrics | See [https://keda.sh/docs/2.17/integrations/prometheus/\#operator](https://keda.sh/docs/2.17/integrations/prometheus/#operator). | No | Kubernetes Event-driven Autoscaler (KEDA) | 
| KEDA Webhook Metrics | See [https://keda.sh/docs/2.17/integrations/prometheus/\#admission-webhooks](https://keda.sh/docs/2.17/integrations/prometheus/#admission-webhooks). | No | Kubernetes Event-driven Autoscaler (KEDA) | 
| KEDA Metrics server Metrics | See [https://keda.sh/docs/2.17/integrations/prometheus/\#metrics-server](https://keda.sh/docs/2.17/integrations/prometheus/#metrics-server). | No | Kubernetes Event-driven Autoscaler (KEDA) | 

## Cluster metrics
<a name="hyperpod-observability-cluster-health-metrics"></a>

Use these metrics to monitor overall cluster health and resource allocation.


| Metric name or type | Description | Enabled by default? | Metric source | 
| --- | --- | --- | --- | 
| Cluster health | Kubernetes API server metrics. See [https://kubernetes.io/docs/reference/instrumentation/metrics/](https://kubernetes.io/docs/reference/instrumentation/metrics/). | Yes | Kubernetes | 
| Kubestate | See [https://github.com/kubernetes/kube-state-metrics/tree/main/docs\#default-resources](https://github.com/kubernetes/kube-state-metrics/tree/main/docs#default-resources). | Limited | Kubernetes | 
| KubeState Advanced | See [https://github.com/kubernetes/kube-state-metrics/tree/main/docs\#optional-resources](https://github.com/kubernetes/kube-state-metrics/tree/main/docs#optional-resources). | No | Kubernetes | 

## Instance metrics
<a name="hyperpod-observability-instance-metrics"></a>

Use these metrics to monitor individual instance performance and health.


| Metric name or type | Description | Enabled by default? | Metric source | 
| --- | --- | --- | --- | 
| Node Metrics | See [https://github.com/prometheus/node\_exporter?tab=readme-ov-file\#enabled-by-default](https://github.com/prometheus/node_exporter?tab=readme-ov-file#enabled-by-default). | Yes | Kubernetes | 
| Container Metrics | Container metrics exposed by Cadvisor. See [https://github.com/google/cadvisor](https://github.com/google/cadvisor). | Yes | Kubernetes | 

## Accelerated compute metrics
<a name="hyperpod-observability-accelerated-compute-metrics"></a>

Use these metrics to monitor the performance, health, and utilization of individual accelerated compute devices in your cluster.

**Note**  
When GPU partitioning with MIG (Multi-Instance GPU) is enabled on your cluster, DCGM metrics automatically provide partition-level granularity for monitoring individual MIG instances. Each MIG partition is exposed as a separate GPU device with its own metrics for temperature, power, memory utilization, and compute activity. This allows you to track resource usage and health for each GPU partition independently, enabling precise monitoring of workloads running on fractional GPU resources. For more information about configuring GPU partitioning, see [Using GPU partitions in Amazon SageMaker HyperPod](sagemaker-hyperpod-eks-gpu-partitioning.md).


| Metric name or type | Description | Enabled by default? | Metric source | 
| --- | --- | --- | --- | 
| NVIDIA GPU | DCGM metrics. See [https://github.com/NVIDIA/dcgm-exporter/blob/main/etc/dcp-metrics-included.csv](https://github.com/NVIDIA/dcgm-exporter/blob/main/etc/dcp-metrics-included.csv). | Limited | NVIDIA Data Center GPU Manager (DCGM) | 
| NVIDIA GPU (advanced) | DCGM metrics that are commented out in the following CSV file:[https://github.com/NVIDIA/dcgm-exporter/blob/main/etc/dcp-metrics-included.csv](https://github.com/NVIDIA/dcgm-exporter/blob/main/etc/dcp-metrics-included.csv) | No | NVIDIA Data Center GPU Manager (DCGM) | 
| AWS Trainium | Neuron metrics. See [https://awsdocs-neuron.readthedocs-hosted.com/en/latest/tools/neuron-sys-tools/neuron-monitor-user-guide.html\#neuron-monitor-nc-counters](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/tools/neuron-sys-tools/neuron-monitor-user-guide.html#neuron-monitor-nc-counters). | No | AWS Neuron Monitor | 

## Network metrics
<a name="hyperpod-observability-network-metrics"></a>

Use these metrics to monitor the performance and health of the Elastic Fabric Adapters (EFA) in your cluster.


| Metric name or type | Description | Enabled by default? | Metric source | 
| --- | --- | --- | --- | 
| EFA | See [https://github.com/aws-samples/awsome-distributed-training/blob/main/4.validation\_and\_observability/3.efa-node-exporter/README.md](https://github.com/aws-samples/awsome-distributed-training/blob/main/4.validation_and_observability/3.efa-node-exporter/README.md). | No | Elastic Fabric Adapter | 

## File system metrics
<a name="hyperpod-observability-file-system-metrics"></a>


| Metric name or type | Description | Enabled by default? | Metric source | 
| --- | --- | --- | --- | 
| File system | Amazon FSx for Lustre metrics from Amazon CloudWatch:[Monitoring with Amazon CloudWatch](https://docs.aws.amazon.com/fsx/latest/LustreGuide/monitoring-cloudwatch.html). | Yes | Amazon FSx for Lustre | 