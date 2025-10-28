# Instance type allocation strategies for AWS Batch

When a managed compute environment is created, AWS Batch selects instance types from the
`instanceTypes` specified that best fit the needs of the jobs. The allocation
strategy defines behavior when AWS Batch needs additional capacity. This parameter isn't applicable
to jobs that run on Fargate resources. Don't specify this parameter.

`BEST_FIT` (default)

AWS Batch selects an instance type that best fits the needs of the jobs with a preference
for the lowest-cost instance type. If additional instances of the selected instance type aren't
available, AWS Batch waits for the additional instances to be available. If there aren't enough
instances available, or if the user is reaching the [Amazon EC2 service quotas](../../../AWSEC2/latest/UserGuide/ec2-resource-limits.md "../../../AWSEC2/latest/UserGuide/ec2-resource-limits.md"), then
additional jobs don't run until currently running jobs are complete. This allocation strategy
keeps costs lower but can limit scaling. If you're using Spot Fleets with
`BEST_FIT`, the Spot Fleet IAM Role must be specified. `BEST_FIT` isn't
supported when updating compute environments. For more information, see [Update a compute environment in
AWS Batch](updating-compute-environments.md "updating-compute-environments.md").

###### Note

AWS Batch manages AWS resources in your account. Compute environments with the BEST_FIT
allocation strategy originally utilized launch configurations by default. However, the use of
launch configurations with new AWS accounts will be restricted over time. Therefore,
beginning in late April 2024, newly-created BEST_FIT compute environments will default to launch
templates. If your service role lacks permissions to manage launch templates, AWS Batch may
continue to utilize launch configurations. Existing compute environments will continue to use
launch configurations.

`BEST_FIT_PROGRESSIVE`

AWS Batch selects additional instance types that are large enough to meet the requirements
of the jobs in the queue. Instance types with a lower cost for each unit vCPU are preferred. If
additional instances of the previously selected instance types aren't available, AWS Batch
selects new instance types.

###### Note

For [multi-node parallel jobs](multi-node-parallel-jobs.md#multi-node-parallel-jobs.title "multi-node-parallel-jobs.md#multi-node-parallel-jobs.title")
AWS Batch chooses the optimal instance type available. If the instance type becomes unavailable
due to insufficient capacity, other instance types within the family are not launched.

`SPOT_CAPACITY_OPTIMIZED`

AWS Batch selects one or more instance types that are large enough to meet the requirements
of the jobs in the queue. Instance types that are less likely to be interrupted are preferred.
This allocation strategy is only available for Spot Instance compute resources.

`SPOT_PRICE_CAPACITY_OPTIMIZED`

The price and capacity optimized allocation strategy looks at both price and capacity to
select the Spot Instance pools that are the least likely to be interrupted and have the lowest
possible price. This allocation strategy is only available for Spot Instance compute
resources.

###### Note

We recommend that you use `SPOT_PRICE_CAPACITY_OPTIMIZED` rather than
`SPOT_CAPACITY_OPTIMIZED` in most instances.

The `BEST_FIT_PROGRESSIVE` and `BEST_FIT` strategies use On-Demand or
Spot Instances, and the `SPOT_CAPACITY_OPTIMIZED` and `SPOT_PRICE_CAPACITY_OPTIMIZED`
strategies use Spot Instances. However, AWS Batch might need to exceed `maxvCpus` to meet your
capacity requirements. In this event, AWS Batch never exceeds `maxvCpus` by more than a
single instance.
