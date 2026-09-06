

# Resource: AWS Batch service quotas
<a name="service_limits"></a>

The following table provides the service quotas for AWS Batch that can't be changed. Each quota is Region specific.


| Resource | Quota | 
| --- | --- | 
| Maximum number of job queues. For more information, see [Job queues](job_queues.md). | 50 | 
| Maximum number of compute environments across Amazon ECS and Amazon EKS. For more information, see [Compute environments for AWS Batch](compute_environments.md). | 50 | 
| Maximum number of compute environments per Amazon EKS cluster. | 5 | 
| Maximum number of compute environments for each job queue | 3 | 
| Maximum number of job dependencies for a job | 20 | 
| Maximum job definition size (for [`RegisterJobDefinition`](https://docs.aws.amazon.com/batch/latest/APIReference/API_RegisterJobDefinition.html) API operations) | 24 KiB | 
| Maximum job payload size (for [`SubmitJob`](https://docs.aws.amazon.com/batch/latest/APIReference/API_SubmitJob.html) API operations) | 30 KiB | 
| Maximum array size for array jobs | 10000 | 
| Maximum number of jobs in SUBMITTED state | 1000000 | 
| Maximum number of transactions per second (TPS) for each account for [`SubmitJob`](https://docs.aws.amazon.com/batch/latest/APIReference/API_SubmitJob.html) operations | 50 | 
| Maximum number of [consumable resources](resource-aware-scheduling.md)  | 50k | 
| Maximum number of service environments. For more information, see [Service environments for AWS Batch](service-environments.md). | 50 | 
| Maximum number of service environments for each job queue | 1 | 
| Maximum number of job queues associated for each quota management enabled service environment. For more information see [Quota management](quota-management.md). | 1 | 
| Maximum number of quota shares for each quota management job queue. For more information see [Quota management](quota-management.md). | 20 | 
| Maximum size of [`SubmitServiceJob`](https://docs.aws.amazon.com/batch/latest/APIReference/API_SubmitServiceJob.html) request | 30 KiB | 
| Maximum job service request payload size (for [`SubmitServiceJob`](https://docs.aws.amazon.com/batch/latest/APIReference/API_SubmitServiceJob.html) API operations) | 10 KiB | 
| Maximum number of transactions per second (TPS) for each account for [`SubmitServiceJob`](https://docs.aws.amazon.com/batch/latest/APIReference/API_SubmitServiceJob.html) operations | 5 | 
| Maximum number of attempts with retry strategy for a service job | 10 | 

Depending on how you use AWS Batch, additional quotas might apply. To learn about Amazon EC2 quotas, see [Amazon EC2 Service Quotas](https://docs.aws.amazon.com/general/latest/gr/ec2-service.html#limits_ec2) in the *AWS General Reference*. For more information about Amazon ECS quotas, see [Amazon ECS Service Quotas](https://docs.aws.amazon.com/general/latest/gr/ecs-service.html#limits_ecs) in the *AWS General Reference*. For more information about Amazon EKS quotas, see [Amazon EKS Service Quotas](https://docs.aws.amazon.com/general/latest/gr/eks.html#limits_eks) in the *AWS General Reference*.