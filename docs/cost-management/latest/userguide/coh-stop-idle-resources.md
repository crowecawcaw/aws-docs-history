

# Stopping idle resources

You can stop idle Amazon EC2 instances directly from their Cost Optimization Hub recommendations on the **Savings opportunities** page. Stop is available only for idle Amazon EC2 instance recommendations, not for other recommendations such as rightsizing.

When you stop an instance, its compute charges end. Stopping doesn't terminate the instance or delete its Amazon EBS volumes. You can start the instance again from the Amazon EC2 console at any time.

There is no charge for this feature.

## Prerequisites and permissions
<a name="coh-stop-idle-resources-prereqs"></a>

You don't need any setup beyond turning on Cost Optimization Hub and AWS Compute Optimizer. For more information, see [Enabling Cost Optimization Hub](coh-getting-started.md#coh-enable) and [Opting in to Compute Optimizer](coh-getting-started.md#coh-compute-optimizer).

To stop an instance, you need permission to do all of the following:
+ View Cost Optimization Hub recommendations, for example with the `CostOptimizationHubReadOnlyAccess` managed policy. For more information, see [Managed policies](billing-permissions-ref.md#managed-policies).
+ View the state of the instance.
+ Stop the instance, with the `ec2:StopInstances` action.

The managed policy doesn't grant Amazon EC2 permissions. For Amazon EC2 actions, see [Actions, resources, and condition keys for Amazon EC2](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonec2.html) in the *Service Authorization Reference*.

The stop runs with your own credentials, so your IAM policies and service control policies (SCPs) apply. If either one doesn't allow the action or denies it, the stop fails. Grant your users only the permissions that they need. AWS CloudTrail logs each stop, including who stopped the instance.

## Stopping an idle instance
<a name="coh-stop-idle-resources-procedure"></a>

Use the following procedure to stop an idle Amazon EC2 instance from its recommendation.

**To stop an idle instance**

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/home#/cost-optimization-hub](https://console.aws.amazon.com/costmanagement/home#/cost-optimization-hub).

1. In Cost Optimization Hub, open the **Savings opportunities** page.

1. Use filters to find the idle Amazon EC2 instance recommendation.

1. Choose **Stop** in the **Actions** column, or select the row to open the split-view panel and choose **Stop instance**.

1. Review the confirmation. It shows the following:
   + The instance, its account, and its Region
   + What the instance loses when it stops, such as instance store data and data in memory
   + What continues to bill, such as Amazon EBS volumes and Elastic IP addresses

1. Choose **Stop** to confirm.

   A confirmation banner appears. The instance usually stops within a few minutes.

After the stop, the **Actions** column shows **Stopped** for the instance. You can then move to the next recommendation.

**Note**  
The recommendation can remain on the **Savings opportunities** page for up to 24 hours, because Cost Optimization Hub refreshes idle resource recommendations once a day. To update the state of the Amazon EC2 instances listed, choose the refresh button in the table header.

When you open Cost Optimization Hub, some idle instances might already show **Stopped**. These instances stopped, from Cost Optimization Hub or elsewhere, after Cost Optimization Hub last refreshed its data.

## What happens to your instance and your bill
<a name="coh-stop-idle-resources-effects"></a>

When you stop an instance:
+ The instance's compute charges end.
+ The instance loses its instance store data, the data in its memory, and its automatically assigned public IPv4 address.
+ Charges for Amazon EBS volumes and Elastic IP addresses continue.
+ A Reserved Instance or Savings Plan that covers the instance continues to bill.

## When Stop isn't available
<a name="coh-stop-idle-resources-unavailable"></a>

For an idle Amazon EC2 instance recommendation, the **Actions** column shows **Stop**. If you can't stop the instance, the console disables the button and shows the reason. Stop isn't available in the following cases:
+ The instance belongs to an Auto Scaling group, or another service manages it.
+ The instance no longer exists.
+ The instance is in another account.
+ The Region isn't responding.

Instances that another service manages include Karpenter nodes, Amazon EMR nodes, and Amazon EC2 managed instances such as those that Amazon EKS Auto Mode and Amazon ECS Managed Instances use.

If you're signed in to a management account, you can see recommendations for member accounts, but you can't stop their instances. To stop an instance, sign in to the account that owns it.

## When a stop doesn't complete
<a name="coh-stop-idle-resources-failure"></a>

If a stop doesn't complete, a banner shows the error and links to the instance in the Amazon EC2 console. Common causes include the following:
+ A missing permission, such as an IAM policy or SCP that denies the stop.
+ Stop protection is turned on for the instance.
+ The instance no longer exists, or its state changed in another console.
+ Your console session expired.
+ Your credentials can't be validated in the Region, for example because it's an opt-in Region that isn't enabled.

## Related cost controls
<a name="coh-stop-idle-resources-related"></a>

You choose when to stop each instance. This feature doesn't run on a schedule, stop resources automatically, or limit your spend. To act when your spend crosses a threshold, use AWS Budgets actions. For more information, see [Configuring budget actions](budgets-controls.md).