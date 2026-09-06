

# EBS volume metrics
<a name="ebs-metrics-analyzed"></a>

Compute Optimizer analyzes the following CloudWatch metrics of your EBS volumes.


| Metric | Description | 
| --- | --- | 
|  VolumeReadBytes  | The read bytes per second of the EBS volume. | 
|  VolumeWriteBytes  | The write bytes per second of the EBS volume. | 
|  VolumeReadOps  | The read operations per second of the EBS volume. | 
|  VolumeWriteOps  | The write operations per second of the EBS volume. | 
|  VolumeIOPSExceededCheck  | Reports whether an application consistently attempted to drive IOPS that exceeds the volume's provisioned IOPS performance within the last minute. This metric can be either 0 (provisioned IOPS not exceeded) or 1 (provisioned IOPS exceeded). Supported for all volume types, except magnetic (standard), attached to Nitro instances. Not supported with Multi-Attach enabled volumes. Not published for volumes attached to Amazon ECS and Fargate tasks.  | 
|  VolumeThroughputExceededCheck  | Reports whether an application consistently attempted to drive throughput that exceeds the volume's provisioned throughput performance within the last minute. This metric can be either 0 (provisioned throughput not exceeded) or 1 (provisioned throughput exceeded). Supported for all volume types, except magnetic (standard), attached to Nitro instances. Not supported with Multi-Attach enabled volumes. Not published for volumes attached to Amazon ECS and Fargate tasks.  | 

For more information about these metrics, see [Amazon CloudWatch metrics for Amazon EBS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using_cloudwatch_ebs.html) in the *Amazon Elastic Compute Cloud User Guide*.