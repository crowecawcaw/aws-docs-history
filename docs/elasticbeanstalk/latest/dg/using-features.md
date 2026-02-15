# Manage alarms

This topic walks you through the steps to create alarms for metrics that you're monitoring. It also provides instructions to view your existing alarms
and to check their state.

You can create alarms for metrics that you are monitoring by using the Elastic Beanstalk console. Alarms help you monitor changes to your AWS Elastic Beanstalk environment so
that you can easily identify and mitigate problems before they occur. For example, you can set an alarm that notifies you when CPU utilization in an
environment exceeds a certain threshold, ensuring that you are notified before a potential problem occurs. For more information, see [Using Elastic Beanstalk with Amazon CloudWatch](AWSHowTo.md "AWSHowTo.md").

###### Note

Elastic Beanstalk uses CloudWatch for monitoring and alarms, meaning CloudWatch costs are applied to your AWS account for any alarms that you use.

For more information about monitoring specific metrics, see [Basic health reporting](using-features.md "using-features.md").

###### To check the state of your alarms

1. Open the [Elastic Beanstalk console](https://console.aws.amazon.com/elasticbeanstalk "https://console.aws.amazon.com/elasticbeanstalk"),
   and in the **Regions** list, select your AWS Region.
2. In the navigation pane, choose **Environments**, and then choose the name of your environment from the list.
3. In the navigation pane, choose **Alarms**.

The page displays a list of existing alarms. If any alarms are in the alarm state, they are flagged with the warning icon (
![Image of the warning icon.](images/warning.png)
). 4. To filter alarms, choose the drop-down menu, and then select a filter. 5. To edit or delete an alarm, choose the edit icon (
![Image of a cog, which serves as the edit icon.](images/cog.png)
) or the delete icon (
![Image of an x, which servers as the delete icon.](images/x.png)
), respectively.

###### To create an alarm

1. Open the [Elastic Beanstalk console](https://console.aws.amazon.com/elasticbeanstalk "https://console.aws.amazon.com/elasticbeanstalk"),
   and in the **Regions** list, select your AWS Region.
2. In the navigation pane, choose **Environments**, and then choose the name of your environment from the list.
3. In the navigation pane, choose **Monitoring**.
4. Locate the metric for which you want to create an alarm, and then choose the alarm icon (
   ![Image of a bell, which serves as the alarm icon.](images/bell.png)
   ). The **Add alarm** page is displayed.
5. Enter details about the alarm:
   - **Name**: A name for this alarm.
   - **Description** (optional): A short description of what this alarm is.
   - **Period**: The time interval between readings.
   - **Threshold**: Describes the behavior and value that the metric must exceed in order to trigger an alarm.
   - **Change state after**: The amount a time after a threshold has been exceed that triggers a change in state of the
     alarm.
   - **Notify**: The Amazon SNS topic that is notified when an alarm changes state.
   - **Notify when state changes to**:
     - **OK**: The metric is within the defined threshold.
     - **Alarm**: The metric exceeded the defined threshold.
     - **Insufficient data**: The alarm has just started, the metric is not available, or not enough data is available for the
       metric to determine the alarm state.

6. Choose **Add**. The environment status changes to gray while the environment updates. You can view the alarm that you created by
   choosing **Alarms** in the navigation pane.
