

# Amazon Aurora Global Database execution block
<a name="aurora-global-database-block"></a>

The Amazon Aurora Global Database execution block allows you to perform a *failover* or *switchover* recovery workflow for a global database.
+ Failover – Use this approach to recover from an unplanned outage. With this approach, you perform a cross-Region failover to one of the secondary DB clusters in your Aurora global databases. The recovery point objective (RPO) for this approach is typically a non-zero value measured in seconds. The amount of data loss depends on the Aurora global databases replication lag across the AWS Regions at the time of the failure. For more information, see [ Recovering an Amazon Aurora global database from an unplanned outage](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-disaster-recovery.html#aurora-global-database-failover) in the Amazon Aurora User Guide.
+ Switchover – This operation was previously called *managed planned failover*. Use this approach for controlled scenarios, such as operational maintenance and other planned operational procedures where all the Aurora clusters and other services they interact with are in a healthy state. Because this feature synchronizes secondary DB clusters with the primary before making any other changes, RPO is 0 (no data loss). For more information, see [ Performing switchovers for Amazon Aurora global databases](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-disaster-recovery.html#aurora-global-database-disaster-recovery.managed-failover) in the Amazon Aurora User Guide.

## Configuration
<a name="aurora-global-database-block-config"></a>

To configure an Aurora Global Database execution block, enter the following values.

**Important**  
Before you configure the execution block, make sure that the plan's execution role has the correct IAM policy in place. For more information, see [Aurora Global Database execution block sample policy](security_iam_region_switch_aurora.md).

1. **Step name: **Enter a name.

1. **Step description (optional): **Enter a description of the step.

1. **Aurora Global Database cluster name: **Enter the identifier for the global database.

1. **Cluster ARN for *Region*: **Enter the cluster ARN to use in each Region in the plan.

1. **Specify the option for Aurora database: **Choose the default behavior for the block. **Switchover** performs a zero-data-loss switchover. **Failover (data loss)** performs a failover that might cause data loss. This behavior also applies during graceful execution.

1. **Ungraceful execution (optional): **Choose **Failover (data loss)** to perform a failover during ungraceful execution. If you don't configure this option, Region switch uses the default behavior that you selected.

1. **Timeout: **Enter a timeout value.

Then, choose **Save step.**

## How it works
<a name="aurora-global-database-block-how"></a>

By configuring a Aurora Global Databases execution block, you can failover or switchover global databases as part of your application recovery. If you’re using an active/active approach, Region switch uses the other configured Region as the source. That is, if a Region is being deactivated, Region switch uses the other active Region as the source to match for the percent to scale.

This block supports both graceful and ungraceful execution modes.



| Execution mode | Behavior | 
| --- | --- | 
| Graceful | Region switch uses the default behavior that you configured. Switchover calls the Aurora SwitchoverGlobalCluster API operation. This operation performs a zero-data-loss switchover. Failover (data loss) calls the Aurora FailoverGlobalCluster API operation with AllowDataLoss set to true. This operation might cause data loss. | 
| Ungraceful | If you configure Failover (data loss), Region switch calls FailoverGlobalCluster with AllowDataLoss set to true. This operation might cause data loss. If you don't configure ungraceful behavior, Region switch uses the default behavior. The block then performs the same switchover or failover as in graceful execution. | 

For more information about Aurora Global Database disaster recovery, including failover and switchover, see [ Using switchover or failover in Amazon Aurora global databases](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-disaster-recovery.html) in the Amazon Aurora User Guide.

