# Amazon SageMaker HyperPod Slurm metrics

Amazon SageMaker HyperPod provides a set of Amazon CloudWatch metrics that you can use to monitor the health
and performance of your HyperPod clusters. These metrics are collected from the
Slurm workload manager running on your HyperPod clusters and are available in the
`/aws/sagemaker/Clusters` CloudWatch namespace.

## Cluster level metrics

The following cluster-level metrics are available for HyperPod. These metrics use the
`ClusterId` dimension to identify the specific HyperPod cluster.

| CloudWatch metric name       | Notes                                           | Amazon EKS Container Insights metric name |
| ---------------------------- | ----------------------------------------------- | ----------------------------------------- |
| cluster_node_count           | Total number of nodes in the cluster            | cluster_node_count                        |
| cluster_idle_node_count      | Number of idle nodes in the cluster             | N/A                                       |
| cluster_failed_node_count    | Number of failed nodes in the cluster           | cluster_failed_node_count                 |
| cluster_cpu_count            | Total CPU cores in the cluster                  | node_cpu_limit                            |
| cluster_idle_cpu_count       | Number of idle CPU cores in the cluster         | N/A                                       |
| cluster_gpu_count            | Total GPUs in the cluster                       | node_gpu_limit                            |
| cluster_idle_gpu_count       | Number of idle GPUs in the cluster              | N/A                                       |
| cluster_running_task_count   | Number of running Slurm jobs in the cluster     | N/A                                       |
| cluster_pending_task_count   | Number of pending Slurm jobs in the cluster     | N/A                                       |
| cluster_preempted_task_count | Number of preempted Slurm jobs in the cluster   | N/A                                       |
| cluster_avg_task_wait_time   | Average wait time for Slurm jobs in the cluster | N/A                                       |
| cluster_max_task_wait_time   | Maximum wait time for Slurm jobs in the cluster | N/A                                       |

## Instance level metrics

The following instance-level metrics are available for HyperPod. These metrics also
use the `ClusterId` dimension to identify the specific HyperPod cluster.

| CloudWatch metric name      | Notes                                               | Amazon EKS Container Insights metric name |
| --------------------------- | --------------------------------------------------- | ----------------------------------------- |
| node_gpu_utilization        | Average GPU utilization across all instances        | node_gpu_utilization                      |
| node_gpu_memory_utilization | Average GPU memory utilization across all instances | node_gpu_memory_utilization               |
| node_cpu_utilization        | Average CPU utilization across all instances        | node_cpu_utilization                      |
| node_memory_utilization     | Average memory utilization across all instances     | node_memory_utilization                   |
