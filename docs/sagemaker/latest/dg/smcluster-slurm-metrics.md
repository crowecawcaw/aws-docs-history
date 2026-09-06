

# Amazon SageMaker HyperPod Slurm metrics
<a name="smcluster-slurm-metrics"></a>

Amazon SageMaker HyperPod provides a set of Amazon CloudWatch metrics that you can use to monitor the health and performance of your HyperPod clusters. These metrics are collected from the Slurm workload manager running on your HyperPod clusters and are available in the `/aws/sagemaker/Clusters` CloudWatch namespace.

## Cluster level metrics
<a name="smcluster-slurm-metrics-cluster"></a>

The following cluster-level metrics are available for HyperPod. These metrics use the `ClusterId` dimension to identify the specific HyperPod cluster.


| CloudWatch metric name | Notes | Amazon EKS Container Insights metric name | 
| --- | --- | --- | 
| cluster\_node\_count | Total number of nodes in the cluster | cluster\_node\_count | 
| cluster\_idle\_node\_count | Number of idle nodes in the cluster | N/A | 
| cluster\_failed\_node\_count | Number of failed nodes in the cluster | cluster\_failed\_node\_count | 
| cluster\_cpu\_count | Total CPU cores in the cluster | node\_cpu\_limit | 
| cluster\_idle\_cpu\_count | Number of idle CPU cores in the cluster | N/A | 
| cluster\_gpu\_count | Total GPUs in the cluster | node\_gpu\_limit | 
| cluster\_idle\_gpu\_count | Number of idle GPUs in the cluster | N/A | 
| cluster\_running\_task\_count | Number of running Slurm jobs in the cluster | N/A | 
| cluster\_pending\_task\_count | Number of pending Slurm jobs in the cluster | N/A | 
| cluster\_preempted\_task\_count | Number of preempted Slurm jobs in the cluster | N/A | 
| cluster\_avg\_task\_wait\_time | Average wait time for Slurm jobs in the cluster | N/A | 
| cluster\_max\_task\_wait\_time | Maximum wait time for Slurm jobs in the cluster | N/A | 

## Instance level metrics
<a name="smcluster-slurm-metrics-instance"></a>

The following instance-level metrics are available for HyperPod. These metrics also use the `ClusterId` dimension to identify the specific HyperPod cluster.


| CloudWatch metric name | Notes | Amazon EKS Container Insights metric name | 
| --- | --- | --- | 
| node\_gpu\_utilization | Average GPU utilization across all instances | node\_gpu\_utilization | 
| node\_gpu\_memory\_utilization | Average GPU memory utilization across all instances | node\_gpu\_memory\_utilization | 
| node\_cpu\_utilization | Average CPU utilization across all instances | node\_cpu\_utilization | 
| node\_memory\_utilization | Average memory utilization across all instances | node\_memory\_utilization | 