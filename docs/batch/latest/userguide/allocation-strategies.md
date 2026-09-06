

# Instance type allocation strategies for AWS Batch
<a name="allocation-strategies"></a>

When a managed compute environment is created, AWS Batch selects instance types from the `[instanceTypes](https://docs.aws.amazon.com/batch/latest/APIReference/API_ComputeResource.html#Batch-Type-ComputeResource-instanceTypes)` specified that best fit the needs of the jobs. The allocation strategy defines behavior when AWS Batch needs additional capacity. This parameter isn't applicable to jobs that run on Fargate resources or Amazon ECS Managed Instances. Don't specify this parameter for those compute environment types.

**Note**  
For Amazon ECS Managed Instances compute environments, instance type selection is managed by Amazon ECS based on the `instanceRequirements` configuration in the `managedInstancesProvider`. No allocation strategy is needed. For more information, see [Amazon ECS Managed Instances compute environments](ecs_managed_instances.md).

`BEST_FIT` (default)  
AWS Batch selects an instance type that best fits the needs of the jobs with a preference for the lowest-cost instance type. If additional instances of the selected instance type aren't available, AWS Batch waits for the additional instances to be available. If there aren't enough instances available, or if the user is reaching the [Amazon EC2 service quotas](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html), then additional jobs don't run until currently running jobs are complete. This allocation strategy keeps costs lower but can limit scaling. If you're using Spot Fleets with `BEST_FIT`, the Spot Fleet IAM Role must be specified. `BEST_FIT` isn't supported when updating compute environments. For more information, see [Update a compute environment in AWS Batch](updating-compute-environments.md).  
AWS Batch manages AWS resources in your account. Compute environments with the BEST\_FIT allocation strategy originally utilized launch configurations by default. However, the use of launch configurations with new AWS accounts will be restricted over time. Therefore, beginning in late April 2024, newly-created BEST\_FIT compute environments will default to launch templates. If your service role lacks permissions to manage launch templates, AWS Batch may continue to utilize launch configurations. Existing compute environments will continue to use launch configurations.

`BEST_FIT_PROGRESSIVE`  
AWS Batch selects additional instance types that are large enough to meet the requirements of the jobs in the queue. Instance types with a lower cost for each unit vCPU are preferred. If additional instances of the previously selected instance types aren't available, AWS Batch selects new instance types.  
For [multi-node parallel jobs](multi-node-parallel-jobs.md) AWS Batch chooses the optimal instance type available. If the instance type becomes unavailable due to insufficient capacity, other instance types within the family are not launched.

`BEST_FIT_PROGRESSIVE_ORDERED`  
This is an advanced allocation strategy only for customers who want to control which instance types are preferred during scaling.  
Placing large instance types at the top of the list may result in **over-provisioning** for small jobs. Placing small instance types at the top may cause the compute environment to reach Amazon EC2 instance count limits before reaching `maxvCpus`.
AWS Batch selects instance types in the order they appear in the `instanceTypes` list. When an instance family is specified, sizes within that family are expanded using `BEST_FIT_PROGRESSIVE` logic—preferring sizes that best fit the jobs, with larger sizes as fallback. Instance types that cannot meet the resource requirements of the jobs are skipped. This strategy is only available for On-Demand Instance (`EC2`) compute resources.  
If an instance family and an explicit instance type from that family both appear in `instanceTypes`, the explicit type takes its listed position and is excluded from the family expansion. For example, in `["m7a.4xlarge", "m7a", "m6a"]`, `m7a.4xlarge` is always placed first and is excluded from the `m7a` family expansion.

`SPOT_CAPACITY_OPTIMIZED`  
AWS Batch selects one or more instance types that are large enough to meet the requirements of the jobs in the queue. Instance types that are less likely to be interrupted are preferred. This allocation strategy is only available for Spot Instance compute resources.

`SPOT_PRICE_CAPACITY_OPTIMIZED`  
The price and capacity optimized allocation strategy looks at both price and capacity to select the Spot Instance pools that are the least likely to be interrupted and have the lowest possible price. This allocation strategy is only available for Spot Instance compute resources.  
We recommend that you use `SPOT_PRICE_CAPACITY_OPTIMIZED` rather than `SPOT_CAPACITY_OPTIMIZED` in most instances.

`SPOT_CAPACITY_OPTIMIZED_PRIORITIZED`  
This is an advanced allocation strategy for customers who want to influence instance type selection during scaling. This strategy optimizes for **capacity first**, and honors instance type priorities on a best-effort basis (priorities are honored when they do not significantly reduce available Spot capacity).  
Placing large instance types at the top of the list may result in **over-provisioning** for small jobs. Placing small instance types at the top may cause the compute environment to reach Amazon EC2 instance count limits before reaching `maxvCpus`.
AWS Batch selects instance types in the order they appear in the `instanceTypes` list, but **optimizes for capacity first**. The customer-defined priority is honored on a best-effort basis. When Spot Instance capacity pools are similarly available, priority order is respected. When capacity is constrained, AWS Batch selects from the most available pools regardless of priority to minimize the likelihood of Spot Instance interruptions. This strategy is only available for Spot Instance compute resources.

With any allocation strategy except `BEST_FIT` using On-Demand (`EC2`) compute resources, AWS Batch might need to exceed `maxvCpus` to meet your capacity requirements. In this event, AWS Batch never exceeds `maxvCpus` by more than a single instance.