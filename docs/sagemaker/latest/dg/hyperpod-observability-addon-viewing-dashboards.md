# Amazon SageMaker HyperPod

observability dashboards

This topic describes how to view metrics dashboards for your Amazon SageMaker HyperPod
(SageMaker HyperPod) clusters and how to add new users to a dashboard. The topic also
describes the different types of dashboards.

## Accessing dashboards

To view your SageMaker HyperPod cluster's metrics in Amazon Managed Grafana, perform the
following steps:

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. Go to your cluster's details page.
3. On the **Dashboard** tab, locate the
   **HyperPod Observability** section,
   and choose **Open dashboard in Grafana**.

## Adding new users

to a Amazon Managed Grafana workspace

For information about how to add users to a Amazon Managed Grafana workspace, see
[Use AWS
IAM Identity Center with your Amazon Managed Grafana workspace](../../../grafana/latest/userguide/authentication-in-AMG-SSO.md "../../../grafana/latest/userguide/authentication-in-AMG-SSO.md") in the
_Amazon Managed Grafana User Guide_.

## Observability

dashboards

The SageMaker HyperPod observability add-on provides five interconnected
dashboards in your default Amazon Managed Grafana workspace. Each dashboard provides
in-depth insights about different resources and tasks in the clusters for
various users such as data scientists, machine learning engineers, and
administrators.

### Task

dashboard

The Task dashboard provides comprehensive monitoring and visualization
of resource utilization metrics for SageMaker HyperPod tasks. The main panel
displays a detailed table grouping resource usage by parent tasks,
showing CPU, GPU, and memory utilization across pods. Interactive
time-series graphs track CPU usage, system memory consumption, GPU
utilization percentages, and GPU memory usage for selected pods,
allowing you to monitor performance trends over time. The dashboard
features powerful filtering capabilities through variables like cluster
name, namespace, task type, and specific pods, making it easy to drill
down into specific workloads. This monitoring solution is essential for
optimizing resource allocation and maintaining performance of machine
learning workloads on SageMaker HyperPod.

### Training dashboard

The training dashboard provides comprehensive monitoring of training
task health, reliability, and fault management metrics. The dashboard
features key performance indicators including task creation counts,
success rates, and uptime percentages, along with detailed tracking of
both automatic and manual restart events. It offers detailed
visualizations of fault patterns through pie charts and heatmaps that
break down incidents by type and remediation latency, enabling you to
identify recurring issues and optimize task reliability. The interface
includes real-time monitoring of critical metrics like system recovery
times and fault detection latencies, making it an essential tool for
maintaining high availability of training workloads. Additionally, the
dashboard's 24-hour trailing window provides historical context for
analyzing trends and patterns in training task performance, helping
teams proactively address potential issues before they impact production
workloads.

### Inference dashboard

The inference dashboard provides comprehensive monitoring of model
deployment performance and health metrics across multiple dimensions. It
features a detailed overview of active deployments, real-time monitoring
of request rates, success percentages, and latency metrics, enabling you
to track model serving performance and identify potential bottlenecks.
The dashboard includes specialized panels for both general inference
metrics and token-specific metrics for language models, such as time to
first token (TTFT) and token throughput, making it particularly valuable
for monitoring large language model deployments. Additionally, it
provides infrastructure insights through pod and node allocation
tracking, while offering detailed error analysis capabilities to help
maintain high availability and performance of inference
workloads.

### Cluster

dashboard

The cluster dashboard provides a comprehensive view of cluster health
and performance, offering real-time visibility into compute, memory,
network, and storage resources across your Amazon SageMaker HyperPod
(SageMaker HyperPod) environment. At a glance, you can view critical metrics
including total instances, GPU utilization, memory usage, and network
performance through an intuitive interface that automatically updates
data every few seconds. The dashboard is organized into logical
sections, starting with a high-level cluster overview that displays key
metrics such as healthy instance percentage and total resource counts,
followed by detailed sections for GPU performance, memory utilization,
network statistics, and storage metrics. Each section features
interactive graphs and panels that allow you to drill down into specific
metrics, with customizable time ranges and filtering options by cluster
name, instance, or GPU ID.

### File

system dashboard

The file-system dashboard provides comprehensive visibility into file
system (Amazon FSx for Lustre) performance and health metrics. The dashboard
displays critical storage metrics including free capacity, deduplication
savings, CPU/memory utilization, disk IOPS, throughput, and client
connections across multiple visualizations. It makes it possible for you
to monitor both system-level performance indicators like CPU and memory
usage, as well as storage-specific metrics such as read/write operations
and disk utilization patterns. The interface includes alert monitoring
capabilities and detailed time-series graphs for tracking performance
trends over time, making it valuable for proactive maintenance and
capacity planning. Additionally, through its comprehensive metrics
coverage, the dashboard helps identify potential bottlenecks, optimize
storage performance, and ensure reliable file system operations for
SageMaker HyperPod workloads.

### GPU partition

dashboard

To monitor GPU partition-specific metrics when using Multi-Instance GPU (MIG)
configurations, you need to install or upgrade to the latest version of the
SageMaker HyperPod Observability addon. This addon provides comprehensive monitoring
capabilities, including MIG-specific metrics such as partition count, memory usage,
and compute utilization per GPU partition.

If you already have SageMaker HyperPod Observability installed but need MIG metrics
support, simply update the addon to the latest version. This process is non-disruptive
and maintains your existing monitoring configuration.

SageMaker HyperPod automatically exposes MIG-specific metrics, including:

- `nvidia_mig_instance_count`: Number of MIG instances per profile
- `nvidia_mig_memory_usage`: Memory utilization per MIG instance
- `nvidia_mig_compute_utilization`: Compute utilization per MIG instance
