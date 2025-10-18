# Managing alarms


## Edit or delete a CloudWatch alarm


You can edit or delete an existing alarm.


You can't change the name of an existing alarm. You can copy an alarm and give the new
 alarm a different name. To copy an alarm, select the check box next to the alarm name in the
 alarm list and choose **Action**, **Copy**.


###### To edit an alarm

1. Open the CloudWatch console at
 [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Alarms**, **All
 Alarms**.
3. Choose the name of the alarm.
4. To add or remove tags, choose the **Tags** tab and then choose
 **Manage tags**.
5. To edit other parts of the alarm, choose **Actions**,
 **Edit**.


The **Specify metric and conditions** page appears, showing a graph
 and other information about the metric and statistic that you selected.
6. To change the metric, choose **Edit**, choose the **All
 metrics** tab, and do one of the following:


	* Choose the service namespace that contains the metric that you want. Continue
	 choosing options as they appear to narrow the choices. When a list of metrics
	 appears, select the check box next to the metric that you want.
	* In the search box, enter the name of a metric, dimension, or resource ID and
	 press Enter. Then choose one of the results and continue until a list of metrics
	 appears. Select the check box next to the metric that you want.Choose **Select metric**.
7. To change other aspects of the alarm, choose the appropriate options. To change how
 many data points must be breaching for the alarm to go into `ALARM` state or
 to change how missing data is treated, choose **Additional
 configuration**.
8. Choose **Next**.
9. Under **Notification**, **Auto Scaling action**,
 and **EC2 action**, optionally edit the actions taken when the alarm is
 triggered. Then choose **Next**.
10. Optionally change the alarm description.


You can't change the name of an existing alarm. You can copy an alarm and give the
 new alarm a different name. To copy an alarm, select the check box next to the alarm
 name in the alarm list and choose **Action**,
 **Copy**.
11. Choose **Next**.
12. Under **Preview and create**, confirm that the information and
 conditions are what you want, then choose **Update alarm**.

###### To update an email notification list that was created using the Amazon SNS console

1. Open the Amazon SNS console at
 [https://console.aws.amazon.com/sns/v3/home](https://console.aws.amazon.com/sns/v3/home "https://console.aws.amazon.com/sns/v3/home").
2. In the navigation pane, choose **Topics** and then select the ARN
 for your notification list (topic).
3. Do one of the following:




	* To add an email address, choose **Create subscription**. For
	 **Protocol**, choose **Email**. For
	 **Endpoint**, enter the email address of the new recipient.
	 Choose **Create subscription**.
	* To remove an email address, choose the **Subscription ID**.
	 Choose **Other subscription actions**, **Delete
	 subscriptions**.
4. Choose **Publish to topic**.

###### To delete an alarm

1. Open the CloudWatch console at
 [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Alarms**.
3. Select the check box to the left of the name of the alarm, and choose
 **Actions**, **Delete**.
4. Choose **Delete**.

## Hide Auto Scaling alarms


When you view your alarms in the AWS Management Console, you can hide the alarms related to both
 Amazon EC2 Auto Scaling and Application Auto Scaling. This feature is available only in the AWS Management Console.


###### To temporarily hide Auto Scaling alarms

1. Open the CloudWatch console at
 [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Alarms**, **All
 alarms**, and select **Hide Auto Scaling alarms**.
