

# EBS volume metrics

Compute Optimizer analyzes the following CloudWatch metrics of your EBS volumes.


**Metrics analyzed for EBS volumes**  

| Metric | Description | 
| --- | --- | 
|  VolumeReadBytes  | The read bytes per second of the EBS volume. | 
|  VolumeWriteBytes  | The write bytes per second of the EBS volume. | 
|  VolumeReadOps  | The read operations per second of the EBS volume. | 
|  VolumeWriteOps  | The write operations per second of the EBS volume. | 
|  VolumeIOPSExceededCheck  | Shows whether an application kept trying to exceed the volume's provisioned IOPS in the last minute. The value is 0 if provisioned IOPS was not exceeded. The value is 1 if it was exceeded. This metric is supported for all volume types attached to Nitro instances, except magnetic (standard). It is not supported for Multi-Attach enabled volumes. It is not published for volumes attached to Amazon ECS and Fargate tasks.  | 
|  VolumeThroughputExceededCheck  | Shows whether an application kept trying to exceed the volume's provisioned throughput in the last minute. The value is 0 if provisioned throughput was not exceeded. The value is 1 if it was exceeded. This metric is supported for all volume types attached to Nitro instances, except magnetic (standard). It is not supported for Multi-Attach enabled volumes. It is not published for volumes attached to Amazon ECS and Fargate tasks.  | 

For more information about these metrics, see [Amazon CloudWatch metrics for Amazon EBS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using_cloudwatch_ebs.html) in the *Amazon Elastic Compute Cloud User Guide*.