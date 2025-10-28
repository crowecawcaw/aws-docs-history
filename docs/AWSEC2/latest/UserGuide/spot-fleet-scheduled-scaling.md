# Scheduled scaling: Scale Spot Fleet on a

schedule

Scaling your fleet on a schedule enables you to scale your application in response
to predictable changes in demand. By creating _scheduled
actions_, you can instruct Spot Fleet to perform scaling activities at specific
times. To create a scheduled action, you must specify an existing Spot Fleet, the time
when the scaling activity must occur, and the desired minimum and maximum capacity.
Scheduled actions can be configured to scale once or on a recurring schedule. If you
needs change, you can edit or delete scheduled actions.

###### Prerequisites

- Scheduled actions can only be created for existing Spot Fleets. You can't create
  a scheduled action when you create a Spot Fleet.
- The Spot Fleet request must have a request type of `maintain`.
  Automatic scaling is not supported for requests of type
  `request`.
- Configure the [IAM permissions required for Spot Fleet
  automatic scaling](spot-fleet-auto-scaling-IAM.md "spot-fleet-auto-scaling-IAM.md").
- Review the [Considerations](spot-fleet-automatic-scaling.md#considerations-for-spot-fleet-automatic-scaling "spot-fleet-automatic-scaling.md#considerations-for-spot-fleet-automatic-scaling").

###### To create a one-time scheduled action

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Spot Requests**.
3. Select your Spot Fleet request.
4. Choose the **Scheduled Scaling** tab near the bottom of
   the screen. If you selected the link for your Spot Fleet, there is no tab;
   instead, scroll down to the **Scheduled Scaling**
   section.
5. Choose **Create scheduled action**.
6. For **Name**, specify a name for the scheduled
   action.
7. Enter a value for **Minimum capacity**, **Maximum
   capacity**, or both.
8. For **Recurrence**, choose
   **Once**.
9. (Optional) Choose a date and time for **Start time**,
   **End time**, or both.
10. Choose **Create**.

###### To create a recurring scheduled action

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Spot Requests**.
3. Select your Spot Fleet request.
4. Choose the **Scheduled Scaling** tab near the bottom of
   the screen. If you selected the link for your Spot Fleet, there is no tab;
   instead, scroll down to the **Scheduled Scaling**
   section.
5. For **Name**, specify a name for the scheduled
   action.
6. Enter a value for **Minimum capacity**, **Maximum
   capacity**, or both.
7. For **Recurrence**, choose one of the predefined
   schedules (for example, **Every day**), or choose
   **Custom** and enter a cron expression. For more
   information about the cron expressions supported by scheduled scaling, see
   [Cron expressions](../../../eventbridge/latest/userguide/eb-scheduled-rule-pattern.md#eb-cron-expressions "../../../eventbridge/latest/userguide/eb-scheduled-rule-pattern.md#eb-cron-expressions") in the
   _Amazon EventBridge User Guide_.
8. (Optional) Choose a date and time for **Start time**,
   **End time**, or both.
9. Choose **Submit**.

###### To edit a scheduled action

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Spot Requests**.
3. Select your Spot Fleet request.
4. Choose the **Scheduled Scaling** tab near the bottom of
   the screen. If you selected the link for your Spot Fleet, there is no tab;
   instead, scroll down to the **Scheduled Scaling**
   section.
5. Select the scheduled action and choose **Actions**,
   **Edit**.
6. Make the needed changes and choose **Submit**.

###### To delete a scheduled action

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Spot Requests**.
3. Select your Spot Fleet request.
4. Choose the **Scheduled Scaling** tab near the bottom of
   the screen. If you selected the link for your Spot Fleet, there is no tab;
   instead, scroll down to the **Scheduled Scaling**
   section.
5. Select the scheduled action and choose **Actions**,
   **Delete**.
6. When prompted for confirmation, choose **Delete**.

###### To manage scheduled scaling using the AWS CLI

Use the following commands:

- [put-scheduled-action](../../../cli/latest/reference/application-autoscaling/put-scheduled-action.md "../../../cli/latest/reference/application-autoscaling/put-scheduled-action.md")
- [describe-scheduled-actions](../../../cli/latest/reference/application-autoscaling/describe-scheduled-actions.md "../../../cli/latest/reference/application-autoscaling/describe-scheduled-actions.md")
- [delete-scheduled-action](../../../cli/latest/reference/application-autoscaling/delete-scheduled-action.md "../../../cli/latest/reference/application-autoscaling/delete-scheduled-action.md")
