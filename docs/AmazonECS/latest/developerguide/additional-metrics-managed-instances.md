

# Additional metrics for Amazon ECS Managed Instances
<a name="additional-metrics-managed-instances"></a>

The following table lists the additional metrics available for Amazon ECS Managed Instances when using Container Insights.



| Metric | Description | Dimensions | Unit | 
| --- | --- | --- | --- | 
| InstanceOSFilesystemUtilization | The percentage of total disk space that is used (os volume). | `ClusterName` - when ContainerInsights is enabled<br />`ClusterName`, `CapacityProviderName` - when ContainerInsights is enabled<br />`ClusterName`, `CapacityProviderName`, `ContainerInstanceId`, `EC2InstanceId` - when EnhancedContainerInsights is enabled | Percent | 
| InstanceDataFilesystemUtilization | The percentage of total disk space that is used (data volume). | `ClusterName` - when ContainerInsights is enabled<br />`ClusterName`, `CapacityProviderName` - when ContainerInsights is enabled<br />`ClusterName`, `CapacityProviderName`, `ContainerInstanceId`, `EC2InstanceId` - when EnhancedContainerInsights is enabled | Percent | 
| InstanceGPULimit | The total number of GPUs available on the instance. Available only for Amazon ECS Managed Instances running NVIDIA GPU-enabled Amazon EC2 instance types. | `ClusterName` - when EnhancedContainerInsights is enabled<br />`ClusterName`, `CapacityProviderName` - when EnhancedContainerInsights is enabled<br />`ClusterName`, `CapacityProviderName`, `ContainerInstanceId`, `EC2InstanceId` - when EnhancedContainerInsights is enabled | Count | 
| InstanceGPUUsageTotal | The number of GPUs currently allocated to running tasks on the instance. Available only for Amazon ECS Managed Instances running NVIDIA GPU-enabled Amazon EC2 instance types. | `ClusterName` - when EnhancedContainerInsights is enabled<br />`ClusterName`, `CapacityProviderName` - when EnhancedContainerInsights is enabled<br />`ClusterName`, `CapacityProviderName`, `ContainerInstanceId`, `EC2InstanceId` - when EnhancedContainerInsights is enabled | Count | 