# Invoke a Lambda function from an alarm

CloudWatch alarms guarantees an asynchronous invocation of the Lambda function for a given
 state change, except in the following cases:


* When the function doesn't exist.
* When CloudWatch is not authorized to invoke the Lambda function.
If CloudWatch can't reach the Lambda service or the message is rejected for another reason,
 CloudWatch retries until the invocation is successful. Lambda queues the message and handles
 execution retries. For more information about this execution model, including information
 about how Lambda handles errors, see  [Asynchronous invocation](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html "https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html") in the
 AWS Lambda Developer Guide.

You can invoke a Lambda function in the same account, or in other AWS accounts.

When you specify an alarm to invoke a Lambda function as an alarm action, you can choose
 to specify the function name, function alias, or a specific version of a function.

When you specify a Lambda function as an alarm action, you must create a resource policy
 for the function to allow the CloudWatch service principal to invoke the function.

One way to do this is by using the AWS CLI, as in the following example:


```
aws lambda add-permission \
--function-name `my-function-name` \
--statement-id AlarmAction \
--action 'lambda:InvokeFunction' \
--principal lambda.alarms.cloudwatch.amazonaws.com \
--source-account `111122223333` \
--source-arn arn:aws:cloudwatch:`us-east-1`:`111122223333`:alarm:alarm-name
```
Alternatively, you can create a policy similar to one of the following examples and then
 assign it to the function.

The following example specifies the account where the alarm is located, so that only
 alarms in that account (111122223333) can invoke the function.


JSON





```
`{
 "Version":"2012-10-17", 
 "Id": "default",
 "Statement": [{
 "Sid": "AlarmAction",
 "Effect": "Allow",
 "Principal": {
 "Service": "lambda.alarms.cloudwatch.amazonaws.com"
 },
 "Action": "lambda:InvokeFunction",
 "Resource": "arn:aws:lambda:us-east-1:444455556666:function:function-name",
 "Condition": {
 "StringEquals": {
 "AWS:SourceAccount": "111122223333"
 }
 }
 }]
}`

```




The following example has a narrower scope, allowing only the specified alarm in the
 specified account to invoke the function.


JSON





```
`{
 "Version":"2012-10-17", 
 "Id": "default",
 "Statement": [
 {
 "Sid": "AlarmAction",
 "Effect": "Allow",
 "Principal": {
 "Service": "lambda.alarms.cloudwatch.amazonaws.com"
 },
 "Action": "lambda:InvokeFunction",
 "Resource": "arn:aws:lambda:`us-east-1`:`444455556666`:function:`function-name`",
 "Condition": {
 "StringEquals": {
 "AWS:SourceAccount": "`111122223333`",
 "AWS:SourceArn": "arn:aws:cloudwatch:us-east-1:`111122223333`:alarm:`alarm-name`"
 }
 }
 }]
}`

```




We don't recommend creating a policy that doesn't specify a source account, because such
 policies are vulnerable to confused deputy issues.


## Add Lambda metrics to CloudWatch investigations


You can add Lambda metrics to your active CloudWatch investigations. When investigating an issue, Lambda
 metrics can provide valuable insights about function performance and behavior. For
 example, if you're investigating an application performance issue, Lambda metrics such as
 duration, error rates, or throttles might help identify the root cause.


To add Lambda metrics to CloudWatch investigations:



1. Open the AWS Lambda console at
 [https://console.aws.amazon.com/lambda/](https://console.aws.amazon.com/lambda/ "https://console.aws.amazon.com/lambda/").
2. In the **Monitor** section, find the metric.
3. Open the context menu for the metric, choose **Investigate**,
 **Add to investigation**. Then, in the
 **Investigate** pane, select the name of the investigation.

## Event object sent from CloudWatch to Lambda


When you configure a Lambda function as an alarm action, CloudWatch delivers a JSON payload
 to the Lambda function when it invokes the function. This JSON payload serves as the event
 object for the function. You can extract data from this JSON object and use it in your
 function. The following is an example of an event object from a metric alarm.



```
{
  'source': 'aws.cloudwatch',
  'alarmArn': 'arn:aws:cloudwatch:us-east-1:444455556666:alarm:lambda-demo-metric-alarm',
  'accountId': '444455556666',
  'time': '2023-08-04T12:36:15.490+0000',
  'region': 'us-east-1',
  'alarmData': {
    'alarmName': 'lambda-demo-metric-alarm',
    'state': {
      'value': 'ALARM',
      'reason': 'test',
      'timestamp': '2023-08-04T12:36:15.490+0000'
    },
    'previousState': {
      'value': 'INSUFFICIENT_DATA',
      'reason': 'Insufficient Data: 5 datapoints were unknown.',
      'reasonData': '{"version":"1.0","queryDate":"2023-08-04T12:31:29.591+0000","statistic":"Average","period":60,"recentDatapoints":[],"threshold":5.0,"evaluatedDatapoints":[{"timestamp":"2023-08-04T12:30:00.000+0000"},{"timestamp":"2023-08-04T12:29:00.000+0000"},{"timestamp":"2023-08-04T12:28:00.000+0000"},{"timestamp":"2023-08-04T12:27:00.000+0000"},{"timestamp":"2023-08-04T12:26:00.000+0000"}]}',
      'timestamp': '2023-08-04T12:31:29.595+0000'
    },
    'configuration': {
      'description': 'Metric Alarm to test Lambda actions',
      'metrics': [
        {
          'id': '1234e046-06f0-a3da-9534-EXAMPLEe4c',
          'metricStat': {
            'metric': {
              'namespace': 'AWS/Logs',
              'name': 'CallCount',
              'dimensions': {
                'InstanceId': 'i-12345678'
              }
            },
            'period': 60,
            'stat': 'Average',
            'unit': 'Percent'
          },
          'returnData': True
        }
      ]
    }
  }
}
```

The following is an example of an event object from a composite alarm.



```
{
  'source': 'aws.cloudwatch',
  'alarmArn': 'arn:aws:cloudwatch:us-east-1:111122223333:alarm:SuppressionDemo.Main',
  'accountId': '111122223333',
  'time': '2023-08-04T12:56:46.138+0000',
  'region': 'us-east-1',
  'alarmData': {
    'alarmName': 'CompositeDemo.Main',
    'state': {
      'value': 'ALARM',
      'reason': 'arn:aws:cloudwatch:us-east-1:111122223333:alarm:CompositeDemo.FirstChild transitioned to ALARM at Friday 04 August, 2023 12:54:46 UTC',
      'reasonData': '{"triggeringAlarms":[{"arn":"arn:aws:cloudwatch:us-east-1:111122223333:alarm:CompositeDemo.FirstChild","state":{"value":"ALARM","timestamp":"2023-08-04T12:54:46.138+0000"}}]}',
      'timestamp': '2023-08-04T12:56:46.138+0000'
    },
    'previousState': {
      'value': 'ALARM',
      'reason': 'arn:aws:cloudwatch:us-east-1:111122223333:alarm:CompositeDemo.FirstChild transitioned to ALARM at Friday 04 August, 2023 12:54:46 UTC',
      'reasonData': '{"triggeringAlarms":[{"arn":"arn:aws:cloudwatch:us-east-1:111122223333:alarm:CompositeDemo.FirstChild","state":{"value":"ALARM","timestamp":"2023-08-04T12:54:46.138+0000"}}]}',
      'timestamp': '2023-08-04T12:54:46.138+0000',
      'actionsSuppressedBy': 'WaitPeriod',
      'actionsSuppressedReason': 'Actions suppressed by WaitPeriod'
    },
    'configuration': {
      'alarmRule': 'ALARM(CompositeDemo.FirstChild) OR ALARM(CompositeDemo.SecondChild)',
      'actionsSuppressor': 'CompositeDemo.ActionsSuppressor',
      'actionsSuppressorWaitPeriod': 120,
      'actionsSuppressorExtensionPeriod': 180
    }
  }
}
```
