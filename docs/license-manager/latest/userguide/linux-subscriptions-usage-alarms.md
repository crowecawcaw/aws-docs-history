# Manage Amazon CloudWatch alarms for Linux

subscriptions in License Manager

The **Linux subscriptions** list page in the License Manager console
shows the following key details, including the Amazon CloudWatch alarms that you have configured
for each Linux subscription that License Manager found on your instances.

- Subscription name
- Subscription type
- Number of running instances per subscription
- Configured Amazon CloudWatch alarms
  When you choose a Linux subscription from the list page, the **Usage metrics and
  alarms** tab displays data for that subscription. In this tab, Amazon CloudWatch dashboards
  display for the chosen subscription within the License Manager console. You can adjust the dashboard to
  encompass a certain time frame, or _evaluation range,_ in hours,
  days, or a week from a selected date.

In the **Usage metrics and alarms** tab, each subscription has an
**Alarms** section with the following details:

- **Alarm name** – The name of the alarm.
- **State** – The state of the alarm.
- **Dimension** – The dimensions of the alarm. The
  dimension will include the AWS Region and instance type that was defined.
- **Condition** – The condition of the alarm. The
  condition will include the comparison operator and alarm threshold value that was
  defined.
  You can create CloudWatch alarms using the dimensions and conditions you define to track and alert
  based on your current subscription utilization. The Linux subscriptions console displays a
  summary of the subscription names in use, the subscription types, amount of running instances for
  each, and the alarm status.

The following are possible CloudWatch alarm states:

- **OK** – The metric or expression is within the
  defined threshold.
- **ALARM** – The metric or expression is outside of
  the defined threshold.
- **INSUFFICIENT_DATA** – The alarm has just started,
  the metric is not available, or not enough data is available for the metric to determine the
  alarm state.

###### Topics

- [Create a CloudWatch alarm for Linux
  subscriptions](#linux-subscriptions-alarms-create "#linux-subscriptions-alarms-create")
- [Modify a CloudWatch alarm for Linux
  subscriptions](#linux-subscriptions-alarms-modify "#linux-subscriptions-alarms-modify")
- [Delete a CloudWatch alarm for Linux
  subscriptions](#linux-subscriptions-alarms-delete "#linux-subscriptions-alarms-delete")

## Create a CloudWatch alarm for Linux

subscriptions

You can create alarms for each commercial Linux subscription that you have discovered on
your running EC2 instances. If necessary, you can create multiple alarms with different
dimensions and conditions for each subscription.

###### To create a CloudWatch alarm for Linux subscriptions from the console

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/ "https://console.aws.amazon.com/license-manager/").
2. In the left navigation pane, under Linux subscriptions, choose
   **Subscriptions**.
3. Under the **Subscription name** column, choose the subscription to
   create an alarm for, then choose **Create alarm**.
4. Specify the following for the alarm:
   - **Alarm name** – specify a name which resembles
     `AWS-LM-LS-`AlarmName``.
   - Instance type – choose an instance type that will be using the subscription
     that was selected.
   - Usage Region – choose the Regions to create the alarms for.
   - Comparison operator – the comparison operator for the alarm threshold.
   - Alarm threshold value – the value for the alarm threshold.

5. Choose **Create** to create the alarm.

## Modify a CloudWatch alarm for Linux

subscriptions

You can modify existing CloudWatch alarms from the License Manager console to adapt to
changing requirements.

###### To modify a CloudWatch alarm for Linux subscriptions from the console

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/ "https://console.aws.amazon.com/license-manager/").
2. In the left navigation pane, under Linux subscriptions, choose
   **Subscriptions**.
3. Under the **Subscription name** column, choose the subscription to
   modify, then choose **Edit**.
4. Modify the defined values as required.
5. Choose **Edit** to modify the alarm.

## Delete a CloudWatch alarm for Linux

subscriptions

You can delete existing CloudWatch alarms from the License Manager console to adapt to
changing requirements.

###### To delete a CloudWatch alarm for Linux subscriptions from the console

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/ "https://console.aws.amazon.com/license-manager/").
2. In the left navigation pane, under Linux subscriptions, choose
   **Subscriptions**.
3. Under the **Subscription name** column, choose the subscription to
   modify, then choose **Delete**.
