

# Enhanced Container Insights (Classic) metric reference
<a name="container-insights-eks-classic-metrics"></a>

Enhanced Container Insights (Classic) publishes metrics to the `ContainerInsights` namespace in CloudWatch. The following tables list all metrics by category, along with their dimensions and descriptions.

**Note**  
For OTel Container Insights metrics, see [OTel Container Insights (Recommended)](container-insights-eks-otel.md), which lists open-source metric names.

## Cluster metrics
<a name="container-insights-eks-classic-metrics-cluster"></a>

The following metrics measure the overall health and capacity of your Amazon EKS cluster.


| Metric Name | Dimensions | Description | 
| --- | --- | --- | 
| cluster\_failed\_node\_count | ClusterName | The number of failed worker nodes in the cluster. | 
| cluster\_node\_count | ClusterName | The total number of worker nodes in the cluster. | 

## Node metrics
<a name="container-insights-eks-classic-metrics-node"></a>

The following metrics measure resource usage and capacity at the node level.


| Metric Name | Dimensions | Description | 
| --- | --- | --- | 
| node\_cpu\_limit | ClusterName, InstanceId, NodeName | The maximum number of CPU units that can be assigned to the node. | 
| node\_cpu\_reserved\_capacity | ClusterName, InstanceId, NodeName | The percentage of CPU units reserved on the node. | 
| node\_cpu\_usage\_total | ClusterName, InstanceId, NodeName | The number of CPU units used on the node. | 
| node\_cpu\_utilization | ClusterName, InstanceId, NodeName | The percentage of CPU units used on the node. | 
| node\_filesystem\_utilization | ClusterName, InstanceId, NodeName | The percentage of filesystem capacity used on the node. | 
| node\_memory\_limit | ClusterName, InstanceId, NodeName | The maximum amount of memory, in bytes, that can be assigned to the node. | 
| node\_memory\_reserved\_capacity | ClusterName, InstanceId, NodeName | The percentage of memory reserved on the node. | 
| node\_memory\_utilization | ClusterName, InstanceId, NodeName | The percentage of memory used on the node. | 
| node\_memory\_working\_set | ClusterName, InstanceId, NodeName | The amount of memory, in bytes, in the working set of the node. | 
| node\_network\_total\_bytes | ClusterName, InstanceId, NodeName | The total number of bytes per second transmitted and received over the network on the node. | 
| node\_number\_of\_running\_containers | ClusterName, InstanceId, NodeName | The number of running containers on the node. | 
| node\_number\_of\_running\_pods | ClusterName, InstanceId, NodeName | The number of running pods on the node. | 

## Pod metrics
<a name="container-insights-eks-classic-metrics-pod"></a>

The following metrics measure resource usage at the pod level.


| Metric Name | Dimensions | Description | 
| --- | --- | --- | 
| pod\_cpu\_utilization | ClusterName, Namespace, PodName | The percentage of CPU units used by the pod. | 
| pod\_cpu\_utilization\_over\_pod\_limit | ClusterName, Namespace, PodName | The percentage of CPU units used relative to the pod limit. | 
| pod\_cpu\_usage\_total | ClusterName, Namespace, PodName | The number of CPU units used by the pod. | 
| pod\_memory\_utilization | ClusterName, Namespace, PodName | The percentage of memory used by the pod. | 
| pod\_memory\_utilization\_over\_pod\_limit | ClusterName, Namespace, PodName | The percentage of memory used relative to the pod limit. | 
| pod\_memory\_working\_set | ClusterName, Namespace, PodName | The amount of memory, in bytes, in the working set of the pod. | 
| pod\_network\_rx\_bytes | ClusterName, Namespace, PodName | The number of bytes received per second over the network by the pod. | 
| pod\_network\_tx\_bytes | ClusterName, Namespace, PodName | The number of bytes transmitted per second over the network by the pod. | 
| pod\_number\_of\_container\_restarts | ClusterName, Namespace, PodName | The total number of container restarts in the pod. | 

## Container metrics
<a name="container-insights-eks-classic-metrics-container"></a>

The following metrics measure resource usage at the container level.


| Metric Name | Dimensions | Description | 
| --- | --- | --- | 
| container\_cpu\_utilization | ClusterName, Namespace, PodName, ContainerName | The percentage of CPU units used by the container. | 
| container\_memory\_utilization | ClusterName, Namespace, PodName, ContainerName | The percentage of memory used by the container. | 

## Service and namespace metrics
<a name="container-insights-eks-classic-metrics-service"></a>

The following metrics measure pod counts at the service and namespace level.


| Metric Name | Dimensions | Description | 
| --- | --- | --- | 
| service\_number\_of\_running\_pods | ClusterName, Namespace, Service | The number of running pods for the service. | 
| namespace\_number\_of\_running\_pods | ClusterName, Namespace | The number of running pods in the namespace. | 

## NVIDIA GPU metrics
<a name="container-insights-eks-classic-metrics-gpu"></a>

The following metrics are collected when your cluster has NVIDIA GPU-equipped nodes. These metrics help you monitor GPU compute and memory utilization across nodes, pods, and containers.


| Metric Name | Dimensions | Description | 
| --- | --- | --- | 
| node\_gpu\_utilization | ClusterName, InstanceId, NodeName | The percentage of GPU compute capacity used on the node. | 
| node\_gpu\_memory\_utilization | ClusterName, InstanceId, NodeName | The percentage of GPU memory used on the node. | 
| node\_gpu\_temperature | ClusterName, InstanceId, NodeName | The GPU temperature in degrees Celsius on the node. | 
| pod\_gpu\_utilization | ClusterName, Namespace, PodName | The percentage of GPU compute capacity used by the pod. | 
| container\_gpu\_utilization | ClusterName, Namespace, PodName, ContainerName | The percentage of GPU compute capacity used by the container. | 

## AWS Neuron metrics
<a name="container-insights-eks-classic-metrics-neuron"></a>

The following metrics are collected when your cluster has AWS Neuron-equipped instances, such as Inf1 or Inf2. These metrics help you monitor NeuronCore utilization at the node and pod level.


| Metric Name | Dimensions | Description | 
| --- | --- | --- | 
| node\_neuroncore\_utilization | ClusterName, InstanceId, NodeName | The percentage of NeuronCore compute capacity used on the node. | 
| pod\_neuroncore\_utilization | ClusterName, Namespace, PodName | The percentage of NeuronCore compute capacity used by the pod. | 

## Kubernetes API server metrics
<a name="container-insights-eks-classic-metrics-apiserver"></a>

The following metrics are collected from the Kubernetes API server. These metrics help you monitor the health and performance of the control plane.


| Metric Name | Dimensions | Description | 
| --- | --- | --- | 
| apiserver\_storage\_objects | ClusterName | The number of objects stored in etcd by the API server. | 
| apiserver\_request\_total | ClusterName | The total number of requests received by the API server. | 
| apiserver\_request\_duration\_seconds | ClusterName | The latency of API server requests, in seconds. | 