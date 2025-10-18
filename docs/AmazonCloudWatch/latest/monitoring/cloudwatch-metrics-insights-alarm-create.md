# Creating a Metrics Insights
 CloudWatch alarm

###### To create an alarm on a Metrics Insights query using the console

1. Open the CloudWatch console at
 [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Metrics**, **All metrics**.
3. (Optional) To run a pre-built sample query, choose **Add query** and select the query to run.
 
 Or, you can choose **Editor** to edit the sample query and then choose **Run** to run 
 the modified query.
4. To create your own query, choose **Multi source query**. You can then use the **Builder** view, the **Editor**
 view, and also use a combination of both. You can switch between the two views anytime and see your work in progress
 in both views. 


In the **Builder** view, you can browse and select the metric namespace, metric name, 
 filter, group, and order options. For each of these options, the query builder offers you a list of possible selections
 from your environment to choose from.


In the **Editor** view, you can start writing your query. As you
 type, the editor offers suggestions based on the characters that you have typed so
 far.


For example, when creating your Metrics Insights query for the alarm, you can use tags to filter and group metrics for more targeted monitoring.




	* Filter by tags – Use `WHERE tag.keyName = 'value'` to monitor resources with specific tags
	
	
	
	```
	SELECT MAX(CPUUtilization) FROM "AWS/EC2" WHERE tag.Environment = 'Prod'
	```
	* Combine tags with dimensions – Mix tag filters with existing metric dimensions
	
	
	
	```
	SELECT AVG(Duration) FROM "AWS/Lambda" WHERE tag.Application = 'OrderService' AND FunctionName = 'process%'
	```
###### Note

When using tags, alarms will match the metrics only if the specified tags existed on the associated resources during the evaluated time period.
5. When you are satisfied with your query, choose **Run**.
6. Choose **Create alarm**.
7. Under **Conditions**, specify the following:


	1. For **Whenever `metric` is**, specify whether the metric 
	 must be greater than, less than, or equal 
	 to the threshold. Under **than...**, specify the threshold value.
	2. Choose **Additional configuration**. For
	 **Datapoints to alarm**, specify how many evaluation periods (data
	 points) must be in the `ALARM` state to trigger the alarm. If the two
	 values here match, you create an alarm that goes to `ALARM` state if that
	 many consecutive periods are breaching.
	
	
	To create an M out of N alarm, specify a lower number for the first value than you specify for the second value.
	 For more information, see [Evaluating an alarm](AlarmThatSendsEmail.md#alarm-evaluation "AlarmThatSendsEmail.md#alarm-evaluation").
	3. For **Missing data treatment**, choose how to have the alarm behave when some data points are missing. For more
	 information, see [Configuring how CloudWatch alarms treat missing
	 data](AlarmThatSendsEmail.md#alarms-and-missing-data "AlarmThatSendsEmail.md#alarms-and-missing-data").
8. Choose **Next**.
9. Under **Notification**, select an SNS topic to notify when the alarm is in `ALARM` state, 
 `OK` state, or `INSUFFICIENT_DATA` state.


To have the alarm send multiple notifications for the same alarm state or for different alarm states, 
 choose **Add notification**.


To have the alarm not send notifications, choose **Remove**.
10. To have the alarm perform Auto Scaling, EC2, or Systems Manager actions, choose the appropriate button
 and choose the alarm state and action to perform. Alarms can perform Systems Manager actions only
 when they go into ALARM state. For more information about Systems Manager actions, see  [Configuring CloudWatch to create OpsItems from alarms](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-create-OpsItems-from-CloudWatch-Alarms.html "https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-create-OpsItems-from-CloudWatch-Alarms.html") and [Incident creation](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-creation.html "https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-creation.html").


###### Note

To create an alarm that performs an SSM Incident Manager action, you must have certain 
 permissions. For more information, see [Identity-based policy examples for AWS Systems Manager Incident Manager](https://docs.aws.amazon.com/incident-manager/latest/userguide/security_iam_id-based-policy-examples.html "https://docs.aws.amazon.com/incident-manager/latest/userguide/security_iam_id-based-policy-examples.html").
11. When finished, choose **Next**.
12. Enter a name and description for the alarm. The name must contain only ASCII
 characters. Then choose **Next**.
13. Under **Preview and create**, confirm that the information and conditions are what you want, then 
 choose **Create alarm**.
**To create an alarm on a Metrics Insights query using the AWS CLI**

Use the `put-metric-alarm` command and specify a Metrics Insights query in the `metrics` parameter.
 For example, the following command sets an alarm that goes into ALARM state if any of your instances
 go above 50% in CPU utilization.


```
aws cloudwatch put-metric-alarm —alarm-name Prod-App-CPU-Alarm —evaluation-periods 1 —comparison-operator GreaterThanThreshold —metrics '[{"Id":"m1","Expression":"SELECT MAX(CPUUtilization) FROM \"AWS/EC2\" WHERE tag.Environment = '\''Prod'\'' AND tag.Application = '\''OrderService'\''", "Period":60}]' —threshold 80
```
