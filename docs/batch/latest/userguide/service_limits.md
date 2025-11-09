# Resource: AWS Batch service quotas

The following table provides the service quotas for AWS Batch that can't be changed. Each quota is Region
specific.

| Resource                                                                                                                                                                                    | Quota   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| Maximum number of job queues. For more information, see [Job queues](job_queues.md "job_queues.md").                                                                                        | 50      |
| Maximum number of compute environments across Amazon ECS and Amazon EKS. For more information, see [Compute environments for AWS Batch](compute_environments.md "compute_environments.md"). | 50      |
| Maximum number of compute environments per Amazon EKS cluster.                                                                                                                              | 5       |
| Maximum number of compute environments for each job queue                                                                                                                                   | 3       |
| Maximum number of job dependencies for a job                                                                                                                                                | 20      |
| Maximum job definition size (for [`RegisterJobDefinition`](../APIReference/API_RegisterJobDefinition.md "../APIReference/API_RegisterJobDefinition.md") API<br>operations)                  | 24 KiB  |
| Maximum job payload size (for [`SubmitJob`](../APIReference/API_SubmitJob.md "../APIReference/API_SubmitJob.md") API operations)                                                            | 30 KiB  |
| Maximum array size for array jobs                                                                                                                                                           | 10000   |
| Maximum number of jobs in `SUBMITTED` state                                                                                                                                                 | 1000000 |
| Maximum number of transactions per second (TPS) for each account for [`SubmitJob`](../APIReference/API_SubmitJob.md "../APIReference/API_SubmitJob.md") operations                          | 50      |
| Maximum number of [consumable resources](resource-aware-scheduling.md "resource-aware-scheduling.md")                                                                                       | 50k     |
| Maximum number of service environments. For more information, see [Service environments for AWS Batch](service-environments.md "service-environments.md").                                  | 50      |
| Maximum number of service environments for each job queue                                                                                                                                   | 1       |
| Maximum size of [`SubmitServiceJob`](../APIReference/API_SubmitServiceJob.md "../APIReference/API_SubmitServiceJob.md") request                                                             | 30 KiB  |
| Maximum job service request payload size (for [`SubmitServiceJob`](../APIReference/API_SubmitServiceJob.md "../APIReference/API_SubmitServiceJob.md") API operations)                       | 10 KiB  |
| Maximum number of transactions per second (TPS) for each account for [`SubmitServiceJob`](../APIReference/API_SubmitServiceJob.md "../APIReference/API_SubmitServiceJob.md") operations     | 5       |
| Maximum number of attempts with retry strategy for a service job                                                                                                                            | 10      |

Depending on how you use AWS Batch, additional quotas might apply. To learn about Amazon EC2 quotas, see [Amazon EC2 Service Quotas](../../../general/latest/gr/ec2-service.md#limits_ec2 "../../../general/latest/gr/ec2-service.md#limits_ec2") in the
_AWS General Reference_. For more information about Amazon ECS quotas, see [Amazon ECS Service Quotas](../../../general/latest/gr/ecs-service.md#limits_ecs "../../../general/latest/gr/ecs-service.md#limits_ecs") in the
_AWS General Reference_. For more information about Amazon EKS quotas, see [Amazon EKS Service Quotas](../../../general/latest/gr/eks.md#limits_eks "../../../general/latest/gr/eks.md#limits_eks") in the
_AWS General Reference_.
