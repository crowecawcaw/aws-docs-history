# Create a load balancer latency alarm that sends
 email

You can set up an Amazon SNS notification and configure an alarm that monitors latency
 exceeding 100 ms for your Classic Load Balancer.


## Setting up a latency alarm using the
 AWS Management Console


Use these steps to use the AWS Management Console to create a load balancer latency alarm.


###### To create a load balancer latency alarm

1. Open the CloudWatch console at
 [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Alarms**, **All
 Alarms**.
3. Choose **Create alarm**.
4. Under **CloudWatch Metrics by Category**, choose the
 **ELB Metrics** category.
5. Select the row with the Classic Load Balancer and the **Latency** metric.
6. For the statistic, choose **Average**, choose one of the
 predefined percentiles, or specify a custom percentile (for example,
 `p95.45`).
7. For the period, choose **1 Minute**.
8. Choose **Next**.
9. Under **Alarm Threshold**, enter a unique name for the alarm (for
 example, `myHighCpuAlarm`) and a description of the alarm (for
 example, `Alarm when Latency exceeds 100s`). Alarm names must
 contain only UTF-8 characters, and can't contain ASCII control characters


The name must contain only UTF-8 characters, and can't contain ASCII control
 characters. The description can include markdown formatting, which is displayed only
 in the alarm **Details** tab in the CloudWatch console. The markdown can be
 useful to add links to runbooks or other internal resources.
10. Under **Whenever**, for **is**, choose
 **>** and enter `0.1`. For
 **for**, enter `3`.
11. Under **Additional settings**, for **Treat missing data
 as**, choose **ignore (maintain alarm state)** so that
 missing data points don't trigger alarm state changes.


For **Percentiles with low samples**, choose **ignore
 (maintain the alarm state)** so that the alarm evaluates only situations
 with adequate numbers of data samples.
12. Under **Actions**, for **Whenever this alarm**,
 choose **State is ALARM**. For **Send notification
 to**, choose an existing SNS topic or create a new one.


To create an SNS topic, choose **New list**. For **Send
 notification to**, enter a name for the SNS topic (for example,
 `myHighCpuAlarm`), and for **Email list**,
 enter a comma-separated list of email addresses to be notified when the alarm changes
 to the `ALARM` state. Each email address is sent a topic subscription
 confirmation email. You must confirm the subscription before notifications can be
 sent.
13. Choose **Create Alarm**.

## Setting up a latency alarm using the
 AWS CLI


Use these steps to use the AWS CLI to create a load balancer latency alarm.


###### To create a load balancer latency alarm

1. Set up an SNS topic. For more information, see [Setting up Amazon SNS notifications](Notify_Users_Alarm_Changes.md#US_SetupSNS "Notify_Users_Alarm_Changes.md#US_SetupSNS").
2. Create the alarm using the [put-metric-alarm](https://docs.aws.amazon.com/cli/latest/reference/cloudwatch/put-metric-alarm.html "https://docs.aws.amazon.com/cli/latest/reference/cloudwatch/put-metric-alarm.html") command
 as follows:



```
`aws cloudwatch put-metric-alarm --alarm-name `lb-mon` --alarm-description "Alarm when Latency exceeds 100s" --metric-name Latency --namespace AWS/ELB --statistic Average --period 60 --threshold 100 --comparison-operator GreaterThanThreshold --dimensions Name=LoadBalancerName,Value=`my-server` --evaluation-periods 3 --alarm-actions arn:aws:sns:`us-east-1`:`111122223333`:`my-topic` --unit Seconds`
```
3. Test the alarm by forcing an alarm state change using the [set-alarm-state](https://docs.aws.amazon.com/cli/latest/reference/cloudwatch/set-alarm-state.html "https://docs.aws.amazon.com/cli/latest/reference/cloudwatch/set-alarm-state.html")
 command.


	1. Change the alarm state from `INSUFFICIENT_DATA` to
	 `OK`.
	
	
	
	```
	`aws cloudwatch set-alarm-state --alarm-name `lb-mon` --state-reason "initializing" --state-value OK`
	```
	2. Change the alarm state from `OK` to `ALARM`.
	
	
	
	```
	`aws cloudwatch set-alarm-state --alarm-name `lb-mon` --state-reason "initializing" --state-value ALARM`
	```
	3. Check that you have received an email notification about the alarm.
