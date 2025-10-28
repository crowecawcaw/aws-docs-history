# Step scaling: Scale Spot Fleet using step

scaling policies

With step scaling policies, you specify CloudWatch alarms to trigger the scaling
process. For example, if you want to scale out when CPU utilization reaches a
certain level, create an alarm using the `CPUUtilization` metric provided
by Amazon EC2.

When you create a step scaling policy, you must specify one of the following
scaling adjustment types:

- **Add** – Increase the target capacity of the fleet
  by a specified number of capacity units or a specified percentage of the
  current capacity.
- **Remove** – Decrease the target capacity of the
  fleet by a specified number of capacity units or a specified percentage of
  the current capacity.
- **Set to** – Set the target capacity of the fleet
  to the specified number of capacity units.
  When an alarm is triggered, the automatic scaling process calculates the new
  target capacity using the fulfilled capacity and the scaling policy, and then
  updates the target capacity accordingly. For example, suppose that the target
  capacity and fulfilled capacity are 10 and the scaling policy adds 1. When the alarm
  is triggered, the automatic scaling process adds 1 to 10 to get 11, so Spot Fleet launches
  1 instance.

When a Spot Fleet terminates a Spot Instance because the target capacity was decreased, the
instance receives a Spot Instance interruption notice.

###### Prerequisites

- The Spot Fleet request must have a request type of `maintain`.
  Automatic scaling is not supported for requests of type
  `request`.
- Configure the [IAM permissions required for Spot Fleet
  automatic scaling](spot-fleet-auto-scaling-IAM.md "spot-fleet-auto-scaling-IAM.md").
- Consider which CloudWatch metrics are important to your application. You can
  create CloudWatch alarms based on metrics provided by AWS or your own custom
  metrics.
- For the AWS metrics that you will use in your scaling policies, enable
  CloudWatch metrics collection if the service that provides the metrics does not
  enable it by default.
- Review the [Considerations](spot-fleet-automatic-scaling.md#considerations-for-spot-fleet-automatic-scaling "spot-fleet-automatic-scaling.md#considerations-for-spot-fleet-automatic-scaling").

###### To create a CloudWatch alarm

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, expand **Alarms** and choose
   **All alarms**.
3. Choose **Create alarm**.
4. On the **Specify metric and conditions** page, choose
   **Select metric**.
5. Choose **EC2 Spot**, then **Fleet Request
   Metrics**, and then select a metric (for example,
   **TargetCapacity**), and then choose **Select
   metric**.

The **Specify metric and conditions** page appears,
showing a graph and other information about the metric you selected. 6. For **Period**, choose the evaluation period for the
alarm, for example, **1 minute**. When evaluating the
alarm, each period is aggregated into one data point.

###### Note

A shorter period creates a more sensitive alarm. 7. For **Conditions**, define the alarm by defining the
threshold condition. For example, you can define a threshold to trigger the
alarm whenever the value of the metric is greater than or equal to 80
percent. 8. Under **Additional configuration**, for
**Datapoints to alarm**, specify how many datapoints
(evaluation periods) must be in the ALARM state to trigger the alarm, for
example, 1 evaluation period or 2 out of 3 evaluation periods. This creates
an alarm that goes to ALARM state if that many consecutive periods are
breaching. For more information, see [Evaluating
an alarm](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md#alarm-evaluation "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md#alarm-evaluation") in the _Amazon CloudWatch User Guide_. 9. For **Missing data treatment**, choose one of the options
(or leave the default of **Treat missing data as
missing**). For more information, see [Configuring how CloudWatch alarms treat missing data](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md#alarms-and-missing-data "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md#alarms-and-missing-data") in the
_Amazon CloudWatch User Guide_. 10. Choose **Next**. 11. (Optional) To receive notification of a scaling event, for
**Notification**, you can choose or create the Amazon SNS
topic you want to use to receive notifications. Otherwise, you can delete
the notification now and add one later as needed. 12. Choose **Next**. 13. Under **Add name and description**, enter a name and
description for the alarm and choose **Next**. 14. Choose **Create alarm**.

###### To configure a step scaling policy for your Spot Fleet

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Spot Requests**.
3. Select your Spot Fleet request.
4. Choose the **Auto Scaling** tab near the bottom of the
   screen. If you selected the link for your Spot Fleet, there is no tab; instead,
   scroll down to the **Auto Scaling** section.
5. If automatic scaling is not configured, choose
   **Configure**.
6. Use **Scale capacity between** to set the minimum and
   maximum capacity for your fleet. Scaling policies do not scale your fleet
   below the minimum capacity or above the maximum capacity.
7. Under **Scaling policies**, for **Policy
   type**, choose **Step scaling policy**.
8. Initially, **Scaling policies** contain step scaling
   policies named **ScaleUp** and
   **ScaleDown**. You can complete
   these policies, or choose **Remove policy** to delete them.
   You can also choose **Add policy**.
9. To define a policy, do the following:
   1. For **Policy name**, enter a name for the
      policy.
   2. For **Policy trigger**, select an existing alarm,
      or choose **Create alarm** to open the Amazon CloudWatch
      console and create an alarm.
   3. For **Modify capacity**, define the amount by
      which to scale and the lower and upper bound of the step adjustment.
      You can add or remove a specific number of instances or a percentage
      of the existing fleet size, or set the fleet to an exact size.

   For example, to create a step scaling policy that increases the
   capacity of the fleet by 30 percent, choose
   **Add**, enter **30** in the next
   field, and then choose **percent**. By default, the
   lower bound for an add policy is the alarm threshold and the upper
   bound is positive (+) infinity. By default, the upper bound for a
   remove policy is the alarm threshold and the lower bound is negative
   (-) infinity. 4. (Optional) To add another step, choose **Add
   step**. 5. For **Cooldown period**, specify a new value (in
   seconds) or keep the default.

10. Choose **Save**.

###### To configure step scaling policies for your Spot Fleet using the AWS CLI

1. Register the Spot Fleet request as a scalable target using the [register-scalable-target](../../../cli/latest/reference/application-autoscaling/register-scalable-target.md "../../../cli/latest/reference/application-autoscaling/register-scalable-target.md") command.
2. Create a scaling policy using the [put-scaling-policy](../../../cli/latest/reference/application-autoscaling/put-scaling-policy.md "../../../cli/latest/reference/application-autoscaling/put-scaling-policy.md") command.
3. Create an alarm that triggers the scaling policy using the [put-metric-alarm](../../../cli/latest/reference/cloudwatch/put-metric-alarm.md "../../../cli/latest/reference/cloudwatch/put-metric-alarm.md") command.
