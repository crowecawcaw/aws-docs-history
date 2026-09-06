

# Update a compute environment in AWS Batch
<a name="updating-compute-environments"></a>

AWS Batch provides multiple strategies for updating compute environments, each designed for specific update scenarios and requirements. These approaches use the same underlying update API but represent different prescriptive methods for managing updates effectively. You can manage these updates using the AWS Batch console or the AWS CLI. Understanding these strategies helps you choose the most appropriate method for your needs while minimizing disruption to your workloads.

This topic provides an overview of the available update strategies and guidance on when to use each approach. For detailed procedures, see the individual sections for each update strategy.

**Important**  
AWS Batch creates and manages multiple AWS resources on your behalf and within your account, including Amazon EC2 Launch Templates, Amazon EC2 Auto Scaling Groups, Amazon EC2 Spot Fleets, and Amazon ECS Clusters. These managed resources are configured specifically to ensure optimal AWS Batch operation. Manually modifying these AWS Batch-managed resources, unless explicitly stated in AWS Batch documentation, can result in unexpected behavior, including `INVALID` compute environments, suboptimal instance scaling behavior, delayed workload processing, or unexpected costs. These manual modifications can't be deterministically supported by the AWS Batch service. Always use the supported AWS Batch APIs or the AWS Batch console to manage your compute environments.  
Unsupported manual modifications include running your own Amazon ECS tasks or services on AWS Batch-managed Amazon ECS clusters, or starting additional processes, daemons, or services directly on AWS Batch-managed instances. AWS Batch assumes full control of the compute resources in a managed compute environment and can terminate instances, stop tasks, or scale the cluster at any time. Any workloads you run outside of AWS Batch job submissions on these managed resources can be interrupted without warning. Running non-AWS Batch workloads on AWS Batch-managed clusters and instances can also interfere with AWS Batch job scheduling and instance scaling.

**Topics**
+ [Compute environment update strategies](#update-strategies)
+ [Choosing the right update strategy](#choosing-update-strategies)
+ [AMI update considerations](#ami-update-considerations)
+ [Perform scaling updates](scaling-updates.md)
+ [Perform infrastructure updates](infrastructure-updates.md)
+ [Perform blue/green updates for compute environments](blue-green-updates.md)

## Compute environment update strategies
<a name="update-strategies"></a>

When you use scaling or infrastructure updates your compute environment is updated in place. For the blue/green update strategy you are creating a new compute environment (green) and then migrating your workload from the old compute environment (blue) to the new compute environment (green).

AWS Batch provides three different strategies for compute environment updates:

Scaling updates  
Scaling updates adjust the capacity of your compute environment by adding or removing instances without replacing existing instances. This is the fastest update scenario and requires no downtime. Use scaling updates when you need to change capacity settings (vCPUs). These updates typically complete within minutes.  
Fargate updates are performed using the same procedures as scaling updates. For more information, see [Perform scaling updates](scaling-updates.md).

Infrastructure updates  
Infrastructure updates replace instances in your compute environment with new instances that have updated settings. These updates require specific service role and allocation strategy configurations but provide minimal downtime, with running jobs potentially interrupted. Use infrastructure updates when you need to modify instance types, AMI configuration, networking settings, service role, environment state, or other infrastructure components. These updates typically complete in 10-30 minutes depending on job completion.  
For more information, see [Perform infrastructure updates](infrastructure-updates.md).

Blue/green updates  
Blue/green updates create a new compute environment alongside your existing environment, allowing gradual workload transition with zero downtime. This approach provides the safest update path but requires running two environments temporarily. Use blue/green updates when you need zero downtime, want to test changes before full deployment, require quick rollback capability, or are using unsupported configurations for infrastructure updates. The time to complete is variable and controlled by you.  
For more information, see [Perform blue/green updates for compute environments](blue-green-updates.md).

## Choosing the right update strategy
<a name="choosing-update-strategies"></a>

Use this decision guide to select the most appropriate update strategy for your needs:

### Choose scaling updates when
<a name="scaling-updates-when"></a>

Choose the scaling update strategy when you only need to adjust compute capacity (vCPUs). Scaling updates are ideal when you need quick updates with no downtime and no infrastructure configuration changes are needed.

For detailed procedures, see [Perform scaling updates](scaling-updates.md).

### Choose infrastructure updates when
<a name="infrastructure-updates-when"></a>

Choose the infrastructure update strategy when you need to modify instance types, AMI settings, service role, environment state, or networking configuration. Your environment must use the *AWSServiceRoleForBatch* service-linked role and an allocation strategy of `BEST_FIT_PROGRESSIVE`, `BEST_FIT_PROGRESSIVE_ORDERED`, `SPOT_CAPACITY_OPTIMIZED`, `SPOT_PRICE_CAPACITY_OPTIMIZED`, or `SPOT_CAPACITY_OPTIMIZED_PRIORITIZED`. Infrastructure updates work well when some job interruption is acceptable during the update and you want automatic updates to the latest Amazon ECS-optimized AMI.

For detailed procedures, see [Perform infrastructure updates](infrastructure-updates.md).

### Choose blue/green updates when
<a name="blue-green-updates-when"></a>

Choose the blue/green update strategy when zero downtime is required for your workloads or you need to test changes before transitioning production workloads. This approach is essential when quick rollback capability is important, your environment uses `BEST_FIT` allocation strategy, or your environment doesn't use the *AWSServiceRoleForBatch* service-linked role. Blue/green updates are also the best choice when you're using custom AMIs that require manual updates or need to make major configuration changes.

For detailed procedures, see [Perform blue/green updates for compute environments](blue-green-updates.md).

## AMI update considerations
<a name="ami-update-considerations"></a>

The approach for updating AMIs depends on your compute environment configuration.

### Updating the AWS Batch provided default AMI to latest
<a name="automatic-ami-updates"></a>

AWS Batch can update to the latest Amazon ECS-optimized AMI during [infrastructure](infrastructure-updates.md) updates when all of these conditions are met:

**Note**  
After the infrastructure update has completed `updateToLatestImageVersion` is set to `false`. To initiate another update `updateToLatestImageVersion` has to be set to `true`.
+ The compute environment uses the *AWSServiceRoleForBatch* service-linked role.
+ The allocation strategy is set to `BEST_FIT_PROGRESSIVE`, `BEST_FIT_PROGRESSIVE_ORDERED`, `SPOT_CAPACITY_OPTIMIZED`, `SPOT_PRICE_CAPACITY_OPTIMIZED`, or `SPOT_CAPACITY_OPTIMIZED_PRIORITIZED`.
+ No AMI ID is explicitly specified in `imageId`, `imageIdOverride`, or launch template.
+ The `updateToLatestImageVersion` is set to `true`.

### AMI updates using blue/green deployment
<a name="manual-ami-updates-blue-green"></a>

You must use blue/green deployment to update AMIs in these scenarios:
+ When using a specific version of the Amazon ECS-optimized AMI.
+ When the AMI ID is specified in any of:
  + Launch template (must update the template or remove it).
  + The `imageId` parameter.
  + The `imageIdOverride` parameter in EC2 configuration.
+ When using the `BEST_FIT` allocation strategy (doesn't support infrastructure updates).
+ When not using the *AWSServiceRoleForBatch* [service-linked role](using-service-linked-roles-batch-general.md).

### AMI updates for a custom AMI
<a name="manual-ami-updates-custom-ami"></a>

If you specify a custom AMI in the compute environment's launch template, the `imageId` parameter or the `imageIdOverride` parameter in EC2 configuration, AWS Batch will not automatically update your custom AMI during infrastructure updates. You can update a custom AMI id by specifying the new id in the parameter originally used during Compute Environment creation. If you wish to switch to using an AWS Batch-provided AMI, you can do so by removing the custom AMI ID in your compute environment update. 