# Target tracking scaling: Scale Spot Fleet by

targeting a value for a specific metric

With target tracking scaling, you create a target tracking scaling policy by
selecting a metric and setting a target value. Spot Fleet then creates and manages the
CloudWatch alarms that trigger the scaling policy, and calculates the scaling adjustment
based on the chosen metric and target value. The scaling policy adjusts capacity by
adding or removing instances as needed to keep the metric at, or close to, the
specified target value. A target tracking policy not only keeps the metric close to
the target value, but also adjusts to the fluctuations in the metric due to a
fluctuating load pattern and minimizes rapid capacity fluctuations.

You can create multiple target tracking scaling policies for a Spot Fleet, provided each
policy uses a different metric. The fleet scales based on the policy that specifies
the largest fleet capacity. This allows you to cover multiple scenarios to ensure
sufficient capacity for your application workloads.

To ensure application availability, the fleet scales out proportionally to the
metric as fast as it can, but scales in more gradually.

When a Spot Fleet terminates a Spot Instance because the target capacity was decreased, the
instance receives a Spot Instance interruption notice.

###### Note

Do not edit or delete the CloudWatch alarms that Spot Fleet manages for a target tracking
scaling policy. Spot Fleet deletes the alarms automatically when you delete the target
tracking scaling policy.

###### Prerequisites

- The Spot Fleet request must have a request type of `maintain`.
  Automatic scaling is not supported for requests of type
  `request`.
- Configure the [IAM permissions required for Spot Fleet
  automatic scaling](spot-fleet-auto-scaling-IAM.md "spot-fleet-auto-scaling-IAM.md").
- Review the [Considerations](spot-fleet-automatic-scaling.md#considerations-for-spot-fleet-automatic-scaling "spot-fleet-automatic-scaling.md#considerations-for-spot-fleet-automatic-scaling").

###### To configure a target tracking policy

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
   maximum capacity for your fleet. Automatic scaling does not scale your fleet
   below the minimum capacity or above the maximum capacity.
7. For **Policy name**, enter a name for the policy.
8. Choose a **Target metric**.
9. Enter a **Target value** for the metric.
10. For **Cooldown period**, specify a new value (in seconds)
    or keep the default.
11. (Optional) To omit creating a scale-in policy based on the current
    configuration, select **Disable scale-in**. You can create
    a scale-in policy using a different configuration.
12. Choose **Save**.

###### To configure a target tracking policy using the AWS CLI

1. Register the Spot Fleet request as a scalable target using the [register-scalable-target](../../../cli/latest/reference/application-autoscaling/register-scalable-target.md "../../../cli/latest/reference/application-autoscaling/register-scalable-target.md") command.
2. Create a scaling policy using the [put-scaling-policy](../../../cli/latest/reference/application-autoscaling/put-scaling-policy.md "../../../cli/latest/reference/application-autoscaling/put-scaling-policy.md") command.
