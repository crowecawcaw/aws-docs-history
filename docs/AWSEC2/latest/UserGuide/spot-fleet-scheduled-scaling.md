

# Scheduled scaling: Scale Spot Fleet on a schedule
<a name="spot-fleet-scheduled-scaling"></a>

Scaling your fleet on a schedule enables you to scale your application in response to predictable changes in demand. By creating *scheduled actions*, you can instruct Spot Fleet to perform scaling activities at specific times. To create a scheduled action, you must specify an existing Spot Fleet, the time when the scaling activity must occur, and the desired minimum and maximum capacity. Scheduled actions can be configured to scale once or on a recurring schedule. If you needs change, you can edit or delete scheduled actions.

**Prerequisites**
+ Scheduled actions can only be created for existing Spot Fleets. You can't create a scheduled action when you create a Spot Fleet.
+ The Spot Fleet request must have a request type of `maintain`. Automatic scaling is not supported for requests of type `request`.
+ Configure the [IAM permissions required for Spot Fleet automatic scaling](spot-fleet-auto-scaling-IAM.md).
+ Review the [Considerations](spot-fleet-automatic-scaling.md#considerations-for-spot-fleet-automatic-scaling).

**To create a one-time scheduled action**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Spot Requests**.

1. Select your Spot Fleet request.

1. Choose the **Scheduled Scaling** tab near the bottom of the screen. If you selected the link for your Spot Fleet, there is no tab; instead, scroll down to the **Scheduled Scaling** section.

1. Choose **Create scheduled action**.

1. For **Name**, specify a name for the scheduled action.

1. Enter a value for **Minimum capacity**, **Maximum capacity**, or both.

1. For **Recurrence**, choose **Once**.

1. (Optional) Choose a date and time for **Start time**, **End time**, or both.

1. Choose **Create**.

**To create a recurring scheduled action**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Spot Requests**.

1. Select your Spot Fleet request.

1. Choose the **Scheduled Scaling** tab near the bottom of the screen. If you selected the link for your Spot Fleet, there is no tab; instead, scroll down to the **Scheduled Scaling** section.

1. For **Name**, specify a name for the scheduled action.

1. Enter a value for **Minimum capacity**, **Maximum capacity**, or both.

1. For **Recurrence**, choose one of the predefined schedules (for example, **Every day**), or choose **Custom** and enter a cron expression. For more information about the cron expressions supported by scheduled scaling, see [Cron expressions](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-scheduled-rule-pattern.html#eb-cron-expressions) in the *Amazon EventBridge User Guide*.

1. (Optional) Choose a date and time for **Start time**, **End time**, or both.

1. Choose **Submit**.

**To edit a scheduled action**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Spot Requests**.

1. Select your Spot Fleet request.

1. Choose the **Scheduled Scaling** tab near the bottom of the screen. If you selected the link for your Spot Fleet, there is no tab; instead, scroll down to the **Scheduled Scaling** section.

1. Select the scheduled action and choose **Actions**, **Edit**.

1. Make the needed changes and choose **Submit**.

**To delete a scheduled action**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Spot Requests**.

1. Select your Spot Fleet request.

1. Choose the **Scheduled Scaling** tab near the bottom of the screen. If you selected the link for your Spot Fleet, there is no tab; instead, scroll down to the **Scheduled Scaling** section.

1. Select the scheduled action and choose **Actions**, **Delete**.

1. When prompted for confirmation, choose **Delete**.

**To manage scheduled scaling using the AWS CLI**

Use the following commands:
+ [put-scheduled-action](https://docs.aws.amazon.com/cli/latest/reference/application-autoscaling/put-scheduled-action.html)
+ [describe-scheduled-actions](https://docs.aws.amazon.com/cli/latest/reference/application-autoscaling/describe-scheduled-actions.html)
+ [delete-scheduled-action](https://docs.aws.amazon.com/cli/latest/reference/application-autoscaling/delete-scheduled-action.html)