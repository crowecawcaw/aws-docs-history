# Amazon DocumentDB Global Cluster execution block

The Amazon DocumentDB Global Cluster execution block allows you to perform a _failover_ or
_switchover_ recovery workflow for a global cluster.

- Failover – Use this approach to recover from an unplanned outage. With this
  approach, you perform a cross-Region failover to one of the
  secondary clusters in your Amazon DocumentDB global cluster. The recovery point objective (RPO) for this approach is typically
  a non-zero value measured in seconds. The amount of data loss
  depends on the Amazon DocumentDB global cluster replication lag across the AWS Regions at the time
  of the failure.
- Switchover – Use this approach for controlled scenarios, such as operational maintenance and other planned
  operational procedures where all the Amazon DocumentDB clusters are
  in a healthy state. Because this feature synchronizes secondary clusters with the primary
  before making any other changes, RPO is 0 (no data loss).

## Configuration

To configure a Amazon DocumentDB Global Cluster execution block, enter the following values.

###### Important

Before you configure the execution block, make sure that you have the correct IAM policy in place.
For more information, see [Amazon DocumentDB Global Cluster execution block sample policy](security_iam_region_switch_documentdb.md "security_iam_region_switch_documentdb.md").

1. **Step name:** Enter a name.
2. **Step description (optional):** Enter a description of the step.
3. **Amazon DocumentDB Global Cluster identifier:** Enter the identifier for
   the global cluster.
4. **Cluster ARN for _Region_:** Enter the
   cluster ARN to use in each Region in the plan.
5. **Specify the option for Amazon DocumentDB cluster:** Choose
   either **Switchover** or **Failover (data loss)**.
6. **Timeout:** Enter a timeout value.

Then, choose **Save step.**

## How it works

By configuring a Amazon DocumentDB Global Cluster execution block, you can failover or switchover global
clusters as part of your application recovery. If you're using an active/active approach, Region switch
uses the other configured Region as the source. That is, if a Region is being deactivated, Region switch
uses the other active Region as the source to match for the percent to scale.

This block supports both graceful and ungraceful execution modes. Ungraceful
settings perform a Amazon DocumentDB Global Cluster _failover_, which might cause data loss.

During switchover or failover operations, the DNS endpoint that customers use to write will be changed.
Customers are responsible for ensuring they are using the correct endpoint after the operation completes.

## What is evaluated as part of plan evaluation

When Region switch evaluates your plan, Region switch performs several checks on your Amazon DocumentDB execution block configuration
and permissions. Region switch verifies that the following is correct:

- The Amazon DocumentDB global cluster specified in the configuration exists.
- There are Amazon DocumentDB clusters in both the source and destination Regions.
- The source and destination clusters are in an available state.
- There are instances in both the source and destination clusters.
- The global cluster engine versions are compatible.

Region switch also validates that the plan's IAM role has the required permissions for Amazon DocumentDB failover and switchover.
For more information about the required permissions for Region switch execution
blocks, see [Identity-based policy
examples for Region switch in ARC](security_iam_id-based-policy-examples-region-switch.md "security_iam_id-based-policy-examples-region-switch.md").

The correct IAM permissions are essential for the proper functioning of the Amazon DocumentDB execution block. If
any of these validations fail, Region switch returns warnings that there are issues, and provides specific error messages to help
you resolve the permissions or configuration issues. This ensures that your plan has the necessary access to manage
and interact with Amazon DocumentDB during when this step runs during a plan execution.
