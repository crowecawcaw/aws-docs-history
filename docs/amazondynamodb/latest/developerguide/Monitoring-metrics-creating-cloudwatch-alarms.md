# Creating CloudWatch alarms in DynamoDB

A [CloudWatch alarm](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md") watches a single metric over a specified time period, and performs one or
more specified actions, based on the value of the metric relative to a threshold over time. The
action is a notification sent to an Amazon SNS topic or Amazon EC2 Auto Scaling policy. You can also add alarms to
dashboards so you can monitor and receive alerts about your AWS resources and applications across
multiple regions. There is no limit to the number of alarms you can create. CloudWatch alarms do not
invoke actions simply because they are in a particular state; the state must have changed and been
maintained for a specified number of periods. For a list of recommended DynamoDB alarms, see [Recommended alarms](../../../AmazonCloudWatch/latest/monitoring/Best_Practice_Recommended_Alarms_AWS_Services.md#DynamoDB "../../../AmazonCloudWatch/latest/monitoring/Best_Practice_Recommended_Alarms_AWS_Services.md#DynamoDB").

###### Note

You must specify all the required dimensions when creating your CloudWatch alarm,
since CloudWatch will not aggregate metrics for a missing dimension. Creating a CloudWatch
alarm with a missing dimension will not result in an error, when creating the
alarm.

Assume you have a provisioned table with five read capacity units. You want to be notified
before you consume the entire provisioned read capacity, so you decide to create a CloudWatch alarm
to get notified when the consumed capacity reaches 80% of what you have provisioned for the table.
You can create alarms in the CloudWatch console or using the AWS CLI.

## Creating an alarm in the CloudWatch console

###### To create an alarm in the CloudWatch console

1. Sign in to the AWS Management Console and open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Alarms**, **All
   alarms**.
3. Choose **Create alarm**.
4. Find the row with the table that you want to monitor and **`ConsumeReadCapacityUnits`**
   in the **Metric Name** column. Select the check box next to this row and choose **Select metric**.
5. Under **Specify metric and conditions**, for **Statistic** choose **Sum**.
   Choose a **Period** of **1 minute**.
6. Under **Conditions**, specify the following:
   1. For **Threshold type**, choose **Static**.
   2. For **Whenever `ConsumedReadCapacityUnits` is**, choose
      **Greater/Equal** and specify the threshold as 240.

7. Choose **Next**.
8. Under **Notification**, choose **`In alarm`**
   and select an SNS topic to notify when the alarm is in `ALARM` state.
9. When finished, choose **Next**.
10. Enter a name and description for the alarm and choose **Next**.
11. Under **Preview and create**, confirm that the information and conditions are what you want,
    then choose **Create alarm**.

## Creating an alarm in the AWS CLI

```
aws cloudwatch put-metric-alarm \
    -\-alarm-name ReadCapacityUnitsLimitAlarm \
    -\-alarm-description "Alarm when read capacity reaches 80% of my provisioned read capacity" \
    -\-namespace AWS/DynamoDB \
    -\-metric-name ConsumedReadCapacityUnits \
    -\-dimensions Name=TableName,Value=myTable \
    -\-statistic Sum \
    -\-threshold 240 \
    -\-comparison-operator GreaterThanOrEqualToThreshold \
    -\-period 60 \
    -\-evaluation-periods 1 \
    -\-alarm-actions arn:aws:sns:us-east-1:123456789012:capacity-alarm
```

Test the alarm.

```
aws cloudwatch set-alarm-state -\-alarm-name ReadCapacityUnitsLimitAlarm -\-state-reason "initializing" -\-state-value OK
```

```
aws cloudwatch set-alarm-state -\-alarm-name ReadCapacityUnitsLimitAlarm -\-state-reason "initializing" -\-state-value ALARM
```

## More AWS CLI examples

The following procedure describes how you're notified if you have requests that exceed the provisioned througput
quotas of a table.

1. Create an Amazon SNS topic `arn:aws:sns:us-east-1:123456789012:requests-exceeding-throughput`. For
   more information, see [Set up Amazon Simple Notification Service](../../../AmazonCloudWatch/latest/monitoring/US_SetupSNS.md "../../../AmazonCloudWatch/latest/monitoring/US_SetupSNS.md").
2. Create the alarm.

```
aws cloudwatch put-metric-alarm \
        -\-alarm-name ReadCapacityUnitsLimitAlarm \
        -\-alarm-description "Alarm when read capacity reaches 80% of my provisioned read capacity" \
        -\-namespace AWS/DynamoDB \
        -\-metric-name ConsumedReadCapacityUnits \
        -\-dimensions Name=TableName,Value=myTable \
        -\-statistic Sum \
        -\-threshold 240 \
        -\-comparison-operator GreaterThanOrEqualToThreshold \
        -\-period 60 \
        -\-evaluation-periods 1 \
        -\-alarm-actions arn:aws:sns:us-east-1:123456789012:capacity-alarm
```

3. Test the alarm.

```
aws cloudwatch set-alarm-state --alarm-name RequestsExceedingThroughputAlarm --state-reason "initializing" --state-value OK
```

```
aws cloudwatch set-alarm-state --alarm-name RequestsExceedingThroughputAlarm --state-reason "initializing" --state-value ALARM
```

The following procedure describes how you're notified if you get system errors.

1. Create an Amazon SNS topic `arn:aws:sns:us-east-1:123456789012:notify-on-system-errors`. For
   more information, see [Set up Amazon Simple Notification Service](../../../AmazonCloudWatch/latest/monitoring/US_SetupSNS.md "../../../AmazonCloudWatch/latest/monitoring/US_SetupSNS.md").
2. Create the alarm.

```
aws cloudwatch put-metric-alarm \
    --alarm-name SystemErrorsAlarm \
    --alarm-description "Alarm when system errors occur" \
    --namespace AWS/DynamoDB \
    --metric-name SystemErrors \
    --dimensions Name=TableName,Value=myTable Name=Operation,Value=aDynamoDBOperation \
    --statistic Sum \
    --threshold 0 \
    --comparison-operator GreaterThanThreshold \
    --period 60 \
    --unit Count \
    --evaluation-periods 1 \
    --treat-missing-data breaching \
    --alarm-actions arn:aws:sns:us-east-1:123456789012:notify-on-system-errors
```

3. Test the alarm.

```
aws cloudwatch set-alarm-state --alarm-name SystemErrorsAlarm --state-reason "initializing" --state-value OK
```

```
aws cloudwatch set-alarm-state --alarm-name SystemErrorsAlarm --state-reason "initializing" --state-value ALARM
```
