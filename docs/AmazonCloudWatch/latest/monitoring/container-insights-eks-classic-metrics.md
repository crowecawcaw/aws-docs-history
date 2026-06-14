# Enhanced Container Insights (Classic) metric reference

Enhanced Container Insights (Classic) publishes metrics to the
`ContainerInsights` namespace in CloudWatch. The following tables list all metrics by
category, along with their dimensions and descriptions.

###### Note

For OTel Container Insights metrics, see [OTel Container Insights (Recommended)](container-insights-eks-otel.md "container-insights-eks-otel.md"), which lists open-source metric names.

## Cluster metrics

The following metrics measure the overall health and capacity of your Amazon EKS cluster.

| Metric Name                 | Dimensions    | Description                                       |
| --------------------------- | ------------- | ------------------------------------------------- |
| `cluster_failed_node_count` | `ClusterName` | The number of failed worker nodes in the cluster. |
| `cluster_node_count`        | `ClusterName` | The total number of worker nodes in the cluster.  |

## Node metrics

The following metrics measure resource usage and capacity at the node level.

| Metric Name                         | Dimensions                                 | Description                                                                                    |
| ----------------------------------- | ------------------------------------------ | ---------------------------------------------------------------------------------------------- |
| `node_cpu_limit`                    | `ClusterName`, `InstanceId`,<br>`NodeName` | The maximum number of CPU units that can be assigned to the node.                              |
| `node_cpu_reserved_capacity`        | `ClusterName`, `InstanceId`,<br>`NodeName` | The percentage of CPU units reserved on the node.                                              |
| `node_cpu_usage_total`              | `ClusterName`, `InstanceId`,<br>`NodeName` | The number of CPU units used on the node.                                                      |
| `node_cpu_utilization`              | `ClusterName`, `InstanceId`,<br>`NodeName` | The percentage of CPU units used on the node.                                                  |
| `node_filesystem_utilization`       | `ClusterName`, `InstanceId`,<br>`NodeName` | The percentage of filesystem capacity used on the node.                                        |
| `node_memory_limit`                 | `ClusterName`, `InstanceId`,<br>`NodeName` | The maximum amount of memory, in bytes, that can be assigned to the<br>node.                   |
| `node_memory_reserved_capacity`     | `ClusterName`, `InstanceId`,<br>`NodeName` | The percentage of memory reserved on the node.                                                 |
| `node_memory_utilization`           | `ClusterName`, `InstanceId`,<br>`NodeName` | The percentage of memory used on the node.                                                     |
| `node_memory_working_set`           | `ClusterName`, `InstanceId`,<br>`NodeName` | The amount of memory, in bytes, in the working set of the node.                                |
| `node_network_total_bytes`          | `ClusterName`, `InstanceId`,<br>`NodeName` | The total number of bytes per second transmitted and received over the<br>network on the node. |
| `node_number_of_running_containers` | `ClusterName`, `InstanceId`,<br>`NodeName` | The number of running containers on the node.                                                  |
| `node_number_of_running_pods`       | `ClusterName`, `InstanceId`,<br>`NodeName` | The number of running pods on the node.                                                        |

## Pod metrics

The following metrics measure resource usage at the pod level.

| Metric Name                             | Dimensions                               | Description                                                                |
| --------------------------------------- | ---------------------------------------- | -------------------------------------------------------------------------- |
| `pod_cpu_utilization`                   | `ClusterName`, `Namespace`,<br>`PodName` | The percentage of CPU units used by the pod.                               |
| `pod_cpu_utilization_over_pod_limit`    | `ClusterName`, `Namespace`,<br>`PodName` | The percentage of CPU units used relative to the pod limit.                |
| `pod_cpu_usage_total`                   | `ClusterName`, `Namespace`,<br>`PodName` | The number of CPU units used by the pod.                                   |
| `pod_memory_utilization`                | `ClusterName`, `Namespace`,<br>`PodName` | The percentage of memory used by the pod.                                  |
| `pod_memory_utilization_over_pod_limit` | `ClusterName`, `Namespace`,<br>`PodName` | The percentage of memory used relative to the pod limit.                   |
| `pod_memory_working_set`                | `ClusterName`, `Namespace`,<br>`PodName` | The amount of memory, in bytes, in the working set of the pod.             |
| `pod_network_rx_bytes`                  | `ClusterName`, `Namespace`,<br>`PodName` | The number of bytes received per second over the network by the pod.       |
| `pod_network_tx_bytes`                  | `ClusterName`, `Namespace`,<br>`PodName` | The number of bytes transmitted per second over the network by the<br>pod. |
| `pod_number_of_container_restarts`      | `ClusterName`, `Namespace`,<br>`PodName` | The total number of container restarts in the pod.                         |

## Container metrics

The following metrics measure resource usage at the container level.

| Metric Name                    | Dimensions                                                | Description                                        |
| ------------------------------ | --------------------------------------------------------- | -------------------------------------------------- |
| `container_cpu_utilization`    | `ClusterName`, `Namespace`, `PodName`,<br>`ContainerName` | The percentage of CPU units used by the container. |
| `container_memory_utilization` | `ClusterName`, `Namespace`, `PodName`,<br>`ContainerName` | The percentage of memory used by the container.    |

## Service and namespace metrics

The following metrics measure pod counts at the service and namespace level.

| Metric Name                        | Dimensions                               | Description                                  |
| ---------------------------------- | ---------------------------------------- | -------------------------------------------- |
| `service_number_of_running_pods`   | `ClusterName`, `Namespace`,<br>`Service` | The number of running pods for the service.  |
| `namespace_number_of_running_pods` | `ClusterName`, `Namespace`               | The number of running pods in the namespace. |

## NVIDIA GPU metrics

The following metrics are collected when your cluster has NVIDIA GPU-equipped nodes. These
metrics help you monitor GPU compute and memory utilization across nodes, pods, and
containers.

| Metric Name                   | Dimensions                                                | Description                                                   |
| ----------------------------- | --------------------------------------------------------- | ------------------------------------------------------------- |
| `node_gpu_utilization`        | `ClusterName`, `InstanceId`,<br>`NodeName`                | The percentage of GPU compute capacity used on the node.      |
| `node_gpu_memory_utilization` | `ClusterName`, `InstanceId`,<br>`NodeName`                | The percentage of GPU memory used on the node.                |
| `node_gpu_temperature`        | `ClusterName`, `InstanceId`,<br>`NodeName`                | The GPU temperature in degrees Celsius on the node.           |
| `pod_gpu_utilization`         | `ClusterName`, `Namespace`,<br>`PodName`                  | The percentage of GPU compute capacity used by the pod.       |
| `container_gpu_utilization`   | `ClusterName`, `Namespace`, `PodName`,<br>`ContainerName` | The percentage of GPU compute capacity used by the container. |

## AWS Neuron metrics

The following metrics are collected when your cluster has AWS Neuron-equipped instances,
such as Inf1 or Inf2. These metrics help you monitor NeuronCore utilization at the node and
pod level.

| Metric Name                   | Dimensions                                 | Description                                                     |
| ----------------------------- | ------------------------------------------ | --------------------------------------------------------------- |
| `node_neuroncore_utilization` | `ClusterName`, `InstanceId`,<br>`NodeName` | The percentage of NeuronCore compute capacity used on the node. |
| `pod_neuroncore_utilization`  | `ClusterName`, `Namespace`,<br>`PodName`   | The percentage of NeuronCore compute capacity used by the pod.  |

## Kubernetes API server metrics

The following metrics are collected from the Kubernetes API server. These metrics help you
monitor the health and performance of the control plane.

| Metric Name                          | Dimensions    | Description                                              |
| ------------------------------------ | ------------- | -------------------------------------------------------- |
| `apiserver_storage_objects`          | `ClusterName` | The number of objects stored in etcd by the API server.  |
| `apiserver_request_total`            | `ClusterName` | The total number of requests received by the API server. |
| `apiserver_request_duration_seconds` | `ClusterName` | The latency of API server requests, in seconds.          |
