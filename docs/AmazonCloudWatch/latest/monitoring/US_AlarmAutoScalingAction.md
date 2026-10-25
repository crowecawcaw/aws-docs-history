

# Create an alarm that triggers an Auto Scaling action
<a name="US_AlarmAutoScalingAction"></a>

With a metric alarm, you can trigger an Auto Scaling scaling policy to add or remove capacity when a metric breaches a threshold. This example scales an Auto Scaling group when the average CPU of the group exceeds a threshold.

You first create the scaling policy, and then attach its ARN as the alarm action. This applies to simple and step scaling policies. For target tracking scaling policies, the Auto Scaling service creates and manages the alarms for you.

Composite alarms can't trigger Auto Scaling actions. For more information, see [Auto Scaling actions](alarm-actions.md#alarm-actions-auto-scaling).

## Setting up an Auto Scaling action alarm using the AWS Management Console
<a name="auto-scaling-action-alarm-console"></a>

Use the AWS Management Console to create an alarm that triggers an Auto Scaling action. Because the full workflow has more than seven steps, it is divided into two parts.

**Part 1: Select the metric and set the condition**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Alarms**, **All alarms**.

1. Choose **Create alarm**.

1. Choose **Select metric**.

1. Select the **AWS/EC2** namespace, and then select **By Auto Scaling Group**. Find the row with **CPUUtilization** for the **AutoScalingGroupName** dimension set to your group. Select the check box next to this row, and choose **Select metric**.

1. For **Statistic**, choose **Average**, and choose a period (for example, **5 minutes**).

1. Under **Conditions**, for **Threshold type** choose **Static**. For **Whenever CPUUtilization is**, choose **Greater**, and under **than...** enter **70**. Then choose **Next**.

**Part 2: Configure the action and create the alarm**

1. Under **Notification**, configure an Amazon SNS notification, or choose **Remove** if you don't want one.

1. Choose **Add EC2 Auto Scaling action**. Select the alarm state that triggers the action, select the Auto Scaling group, and then select the scaling policy to run. Then choose **Next**.

1. Under **Name and description**, enter a name and description for the alarm, and choose **Next**.

1. Under **Preview and create**, choose **Create alarm**.

It might take a few minutes for the alarm to become active.

## Setting up an Auto Scaling action alarm using the AWS CLI
<a name="auto-scaling-action-alarm-cli"></a>

Use the AWS CLI to create an alarm that triggers an Auto Scaling action.

**To create an alarm that triggers an Auto Scaling action**

1. Create a simple scaling policy using the [put-scaling-policy](https://docs.aws.amazon.com/cli/latest/reference/autoscaling/put-scaling-policy.html) command. Replace {{my-asg}} and {{scale-out}} with your Auto Scaling group name and policy name.

   ```
   aws autoscaling put-scaling-policy --auto-scaling-group-name {{my-asg}} --policy-name {{scale-out}} --policy-type SimpleScaling --adjustment-type ChangeInCapacity --scaling-adjustment 1 --cooldown 300
   ```

   After the command runs, copy the `PolicyARN` value from the output to use in the next step. The output looks similar to the following:

   ```
   {
       "PolicyARN": "arn:aws:autoscaling:us-east-1:111122223333:scalingPolicy:12345678-1234-1234-1234-123456789012:autoScalingGroupName/my-asg:policyName/scale-out"
   }
   ```

1. Create the alarm using the [put-metric-alarm](https://docs.aws.amazon.com/cli/latest/reference/cloudwatch/put-metric-alarm.html) command. Replace {{my-asg}} with your Auto Scaling group name, and replace the ARN in `--alarm-actions` with the `PolicyARN` value from the previous step.

   ```
   aws cloudwatch put-metric-alarm --alarm-name {{asg-cpu-high}} --alarm-description "Scale out when CPU exceeds 70%" --metric-name CPUUtilization --namespace AWS/EC2 --statistic Average --period 300 --threshold 70 --comparison-operator GreaterThanThreshold --dimensions Name=AutoScalingGroupName,Value={{my-asg}} --evaluation-periods 2 --alarm-actions {{arn:aws:autoscaling:us-east-1:111122223333:scalingPolicy:...:policyName/scale-out}}
   ```

   If the command succeeds, it returns no output.