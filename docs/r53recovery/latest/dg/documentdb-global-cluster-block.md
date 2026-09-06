

# Amazon DocumentDB Global Cluster execution block
<a name="documentdb-global-cluster-block"></a>

The Amazon DocumentDB Global Cluster execution block allows you to perform a *failover* or *switchover* recovery workflow for a global cluster.
+ Failover – Use this approach to recover from an unplanned outage. With this approach, you perform a cross-Region failover to one of the secondary clusters in your Amazon DocumentDB global cluster. The recovery point objective (RPO) for this approach is typically a non-zero value measured in seconds. The amount of data loss depends on the Amazon DocumentDB global cluster replication lag across the AWS Regions at the time of the failure.
+ Switchover – Use this approach for controlled scenarios, such as operational maintenance and other planned operational procedures where all the Amazon DocumentDB clusters are in a healthy state. Because this feature synchronizes secondary clusters with the primary before making any other changes, RPO is 0 (no data loss).

## Configuration
<a name="documentdb-global-cluster-block-config"></a>

To configure a Amazon DocumentDB Global Cluster execution block, enter the following values.

**Important**  
Before you configure the execution block, make sure that the plan's execution role has the correct IAM policy in place. For more information, see [Amazon DocumentDB Global Cluster execution block sample policy](security_iam_region_switch_documentdb.md).

1. **Step name: **Enter a name.

1. **Step description (optional): **Enter a description of the step.

1. **Amazon DocumentDB Global Cluster identifier: **Enter the identifier for the global cluster.

1. **Cluster ARN for *Region*: **Enter the cluster ARN to use in each Region in the plan.

1. **Specify the option for Amazon DocumentDB cluster: **Choose either **Switchover** or **Failover (data loss)**.

1. **Timeout: **Enter a timeout value.

Then, choose **Save step.**

## How it works
<a name="documentdb-global-cluster-block-how"></a>

By configuring a Amazon DocumentDB Global Cluster execution block, you can failover or switchover global clusters as part of your application recovery. If you're using an active/active approach, Region switch uses the other configured Region as the source. That is, if a Region is being deactivated, Region switch uses the other active Region as the source to match for the percent to scale.

This block supports both graceful and ungraceful execution modes. Ungraceful settings perform a Amazon DocumentDB Global Cluster *failover*, which might cause data loss.

During switchover or failover operations, the DNS endpoint that customers use to write will be changed. Customers are responsible for ensuring they are using the correct endpoint after the operation completes.