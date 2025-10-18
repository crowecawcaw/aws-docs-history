# Create alarms for metrics

In the CloudFront console, you can set alarms to notify you by Amazon Simple Notification Service (Amazon SNS) based on
 specific CloudFront metrics.

###### To create alarms for metrics

1. Sign in to the AWS Management Console and open the CloudFront console at
 [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. In the navigation pane, choose **Alarms**.
3. Choose **Create alarm**.
4. For **Details**, specify the following: 


	1. **Alarm name** – A name for the alarm.
	2. **Distribution** – The CloudFront distribution that
	 you're creating the alarm for.
5. For **Condition**, specify the following:


	1. **Metric** – The metric that you're creating
	 the alarm for.
	2. **"IF" <condition>** – The threshold when
	 CloudWatch should trigger an alarm and send a notification to the Amazon SNS topic.
	 For example, to receive a notification when the `5xx` error
	 rate exceeds 1%, specify the following:
	
	
	**5xx error rate**
	**> 1**
	3. **"FOR" consecutive periods** – The period of
	 time that the condition must be met before triggering an alarm. When you
	 choose a value, aim for an appropriate balance between a value that
	 doesn't alarm for temporary problems, but will alarm for sustained or
	 real problems.
	4. (Optional) **Notify** – The Amazon SNS topic to
	 send notification to if this metric triggers an alarm.
6. Choose **Create alarm**.
###### Notes


* When you enter the values for the condition, use whole numbers without
 punctuation. For example, to specify one thousand, enter
 `1000`.
* For `4xx`, `5xx`, and total error rates, the value
 that you specify is a percentage.
* For requests, bytes downloaded, and bytes uploaded, the value that you
 specify is units. For example, 1073742000 bytes.
For more information about creating Amazon SNS topics, see [Creating an Amazon SNS topic](https://docs.aws.amazon.com/sns/latest/dg/sns-create-topic.html "https://docs.aws.amazon.com/sns/latest/dg/sns-create-topic.html") in the
 *Amazon Simple Notification Service Developer Guide*.
