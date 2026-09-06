

# Alarming on logs
<a name="Alarm-On-Logs"></a>

You can create CloudWatch alarms that monitor your log data in two ways:
+ **Log Alarm approach** — Create a Log Alarm that runs a CloudWatch Logs Insights query on a schedule and evaluates the aggregated results directly against a threshold.
+ **Metric filter approach** — Create a metric filter on a log group, then create a standard metric alarm on the resulting metric.

## Create a Log Alarm
<a name="Create_Log_Alarm"></a>

### Create a Log Alarm
<a name="log-alarm-overview"></a>

You can create a CloudWatch alarm that uses a CloudWatch Logs Insights query to monitor log data directly. The query runs on a schedule using a Scheduled Query, and the alarm evaluates the aggregated results against a threshold. For more information about how Log Alarms work, see [Log alarms](alarm-log.md).

### Prerequisites
<a name="log-alarm-prerequisites"></a>

Before you create a Log Alarm, you must create an IAM role that grants CloudWatch Logs permission to execute the scheduled query. If you also want log lines included in Amazon SNS notifications, you must create a second role.

**Note**  
If you create a Log Alarm from the CloudWatch console, the console helps you create these roles.

#### Scheduled query execution role
<a name="log-alarm-prereq-query-role"></a>

The scheduled query execution role allows CloudWatch Logs to run the query on your behalf. This role is required for all Log Alarms to execute the scheduled query. The role must trust the `logs.amazonaws.com` service principal.

The following example shows the trust policy for the scheduled query execution role.

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "logs.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

The following example shows the permissions policy. Scope the `Resource` to the log group ARNs that the query targets.

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "logs:StartQuery",
                "logs:StopQuery",
                "logs:GetQueryResults",
                "logs:DescribeLogGroups"
            ],
            "Resource": "arn:aws:logs:{{region}}:{{account-id}}:log-group:{{your-log-group}}:*"
        }
    ]
}
```

#### Log lines role (optional)
<a name="log-alarm-prereq-alarm-role"></a>

The log lines role allows CloudWatch to fetch log lines for Amazon SNS email notifications. This role is required only if you set `ActionLogLineCount` to a value greater than 0. The role must trust the `cloudwatch.amazonaws.com` service principal.

The following example shows the trust policy for the log lines role.

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "cloudwatch.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

The following example shows the permissions policy for the log lines role. The `logs:GetQueryResults` permission is required to fetch log lines. Scope the `Resource` to the log group ARNs that the query targets.

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "logs:GetQueryResults"
            ],
            "Resource": "arn:aws:logs:{{region}}:{{account-id}}:log-group:{{your-log-group}}:*"
        }
    ]
}
```

**Note**  
To view Log Alarm query results in the CloudWatch console, the IAM user or role accessing the console must have the `logs:GetScheduledQueryData` permission. This is a console-only API and is not available through the AWS CLI or SDK. CloudTrail logs this API as a data event, so you must configure a trail with data event logging to capture it.

### Creating a Log Alarm using the console
<a name="log-alarm-create-console"></a>

The steps in this section explain how to use the CloudWatch console to create a Log Alarm. You can also use the AWS CLI to create a Log Alarm. For more information, see [Creating a Log Alarm using the AWS CLI](#log-alarm-create-cli).

**To create a Log Alarm**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Alarms**.

1. Choose **Create alarm**.

1. For **Data source**, choose **Logs**.

1. Under **Logs Query**:

   1. Choose **Create query in Log Analytics**. This opens the Log Analytics page where you build your query.

   1. On the Log Analytics page, write your query. When you finish, choose **Continue to Alarms** in the top right to return to the alarm console.

   1. For **Aggregation expression**, specify how to aggregate the query results to return a numerical value for alarm evaluation (for example, `count(*)` or `avg(latency) by endpoint`).

1. Under **Alarm Conditions**:

   1. For **Whenever the aggregated result is...**, choose a comparison operator.

   1. For **than...**, enter the threshold value.

   1. (Optional) Under **Additional Configuration**:

      1. Modify **Datapoints to alarm** to specify the number of breaching results required to trigger `ALARM` out of last N queries.

      1. Modify **Missing data treatment** to specify how to treat missing data.

1. Under **Schedule**:

   1. For **Evaluation Frequency**, choose how often the query runs (for example, every 5 minutes).

   1. For **Start time offset**, the lookback window for each query execution.

   1. For **End time offset** (optional), the end of the query time range as an offset in seconds from the current time.

1. Under **IAM permission**:

   1. Specify the role that is required to execute the scheduled query. You can either choose to create a new role or use an existing role.

1. Choose **Next**.

1. Under **Configure actions**, configure actions and notifications as needed.

   1. To include log lines triggering the alarm transition in Amazon SNS email notifications, under **Include query results in the actions**:

     1. Add **Number of query results** to specify the number of log lines to include.

     1. Create or choose an existing role that is used to get the required query results.

1. Choose **Next**.

1. Enter a **Name** and optional **Description** (supports Markdown).

1. (Optional) Add tags.

1. Choose **Next**.

1. Under **Preview and create**, review your configuration, and then choose **Create alarm**.

### Creating a Log Alarm using the AWS CLI
<a name="log-alarm-create-cli"></a>

You can use the AWS CLI `put-log-alarm` command to create a Log Alarm.

The following example creates a Log Alarm that monitors error counts in a log group and transitions to `ALARM` state when the count exceeds 100 in 3 out of 5 query executions.

```
aws cloudwatch put-log-alarm \
    --alarm-name "HighErrorCount" \
    --alarm-description "Alarm when error count exceeds 100" \
    --comparison-operator GreaterThanThreshold \
    --threshold 100 \
    --query-results-to-evaluate 5 \
    --query-results-to-alarm 3 \
    --treat-missing-data missing \
    --alarm-actions "arn:aws:sns:{{region}}:{{account-id}}:{{topic-name}}" \
    --scheduled-query-configuration '{
        "QueryString": "fields @timestamp, @message | filter @message like /ERROR/",
        "LogGroupIdentifiers": ["/aws/lambda/my-function"],
        "ScheduledQueryRoleARN": "arn:aws:iam::{{account-id}}:role/ScheduledQueryRole",
        "AggregationExpression": "count(*)",
        "ScheduleConfiguration": {
            "ScheduleExpression": "rate(10 minutes)",
            "StartTimeOffset": 600
        }
    }' \
    --action-log-line-count 5 \
    --action-log-line-role-arn "arn:aws:iam::{{account-id}}:role/LogLineRole"
```

The following table describes the key parameters for the `put-log-alarm` command.


| Parameter | Required | Description | 
| --- | --- | --- | 
| --alarm-name | Yes | The name of the alarm. Must contain only UTF-8 characters. | 
| --comparison-operator | Yes | The comparison operator for threshold evaluation. Valid values: GreaterThanThreshold, GreaterThanOrEqualToThreshold, LessThanThreshold, LessThanOrEqualToThreshold. | 
| --threshold | Yes | The numeric threshold value to compare against. | 
| --query-results-to-evaluate | Yes | The number of recent query executions to evaluate (N in M-out-of-N). | 
| --query-results-to-alarm | Yes | The number of breaching results required to trigger ALARM (M in M-out-of-N). | 
| --treat-missing-data | No | How to treat missing data. Valid values: missing (default), notBreaching, breaching, ignore. | 
| --scheduled-query-configuration | Yes | The query configuration including query string, log group identifiers, scheduled query role ARN, aggregation expression, and schedule configuration. | 
| --action-log-line-count | No | The number of log lines to include in Amazon SNS email notifications (0–50). Default is 0. | 
| --action-log-line-role-arn | No | The ARN of the IAM role that trusts cloudwatch.amazonaws.com. Required if action-log-line-count is greater than 0. | 

### Creating a Log Alarm using AWS CloudFormation
<a name="log-alarm-create-cfn"></a>

You can use the `AWS::CloudWatch::LogAlarm` resource type to create a Log Alarm in a AWS CloudFormation template.

The following example template creates a Log Alarm that monitors error counts.

```
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  HighErrorCountAlarm:
    Type: AWS::CloudWatch::LogAlarm
    Properties:
      AlarmName: HighErrorCount
      AlarmDescription: Alarm when error count exceeds 100
      ComparisonOperator: GreaterThanThreshold
      Threshold: 100
      QueryResultsToEvaluate: 5
      QueryResultsToAlarm: 3
      TreatMissingData: missing
      ActionLogLineCount: 5
      ActionLogLineRoleArn: !GetAtt LogLineRole.Arn
      ScheduledQueryConfiguration:
        QueryString: "fields @timestamp, @message | filter @message like /ERROR/"
        LogGroupIdentifiers:
          - /aws/lambda/my-function
        ScheduledQueryRoleARN: !GetAtt ScheduledQueryRole.Arn
        AggregationExpression: "count(*)"
        ScheduleConfiguration:
          ScheduleExpression: "rate(10 minutes)"
          StartTimeOffset: 600
      AlarmActions:
        - !Ref AlarmSNSTopic
```

### Create a CloudWatch alarm based on a log group-metric filter
<a name="Create_alarm_log_group_metric_filter"></a>

 The procedure in this section describes how to create an alarm based on a log group-metric filter. With metric filters, you can look for terms and patterns in log data as the data is sent to CloudWatch. For more information, see [Create metrics from log events using filters](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/MonitoringLogData.html) in the *Amazon CloudWatch Logs User Guide*. Before you create an alarm based on a log group-metric filter, you must complete the following actions: 
+  Create a log group. For more information, see [Working with log groups and log streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html#Create-Log-Group) in the *Amazon CloudWatch Logs User Guide*. 
+  Create a metric filter. For more information, see [Create a metric filter for a log group](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CreateMetricFilterProcedure.html) in the *Amazon CloudWatch Logs User Guide*. 

**To create an alarm based on a log group-metric filter**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1.  From the navigation pane, choose **Logs**, and then choose **Log groups**. 

1.  Choose the log group that includes your metric filter. 

1.  Choose **Metric filters**. 

1.  In the metric filters tab, select the box for the metric filter that you want to base your alarm on. 

1.  Choose **Create alarm**. 

1.  (Optional) Under **Metric**, edit **Metric name**, **Statistic**, and **Period**. 

1.  Under **Conditions**, specify the following: 

   1.  For **Threshold type**, choose **Static** or **Anomaly detection**. 

   1.  For **Whenever {{your-metric-name}} is . . .**, choose **Greater**, **Greater/Equal**, **Lower/Equal** , or **Lower**. 

   1.  For **than . . .**, specify a number for your threshold value. 

1.  Choose **Additional configuration**. 

   1.  For **Data points to alarm**, specify how many data points trigger your alarm to go into the `ALARM` state. If you specify matching values, your alarm goes into the `ALARM` state if that many consecutive periods are breaching. To create an M-out-of-N alarm, specify a number for the first value that's lower than the number you specify for the second value. For more information, see [Alarm evaluation](alarm-evaluation.md). 

   1.  For **Missing data treatment**, select an option to specify how to treat missing data when your alarm is evaluated. 

1.  Choose **Next**. 

1.  For **Notification**, specify an Amazon SNS topic to notify when your alarm is in the `ALARM`, `OK`, or `INSUFFICIENT_DATA` state. 

   1.  (Optional) To send multiple notifications for the same alarm state or for different alarm states, choose **Add notification**. 

   1.  (Optional) To not send notifications, choose **Remove**. 

1. To have the alarm perform Auto Scaling, EC2, Lambda, or Systems Manager actions, choose the appropriate button and choose the alarm state and action to perform. If you choose a Lambda function as an alarm action, you specify the function name or ARN, and you can optionally choose a specific version of the function.

   Alarms can perform Systems Manager actions only when they go into ALARM state. For more information about Systems Manager actions, see see [ Configuring CloudWatch to create OpsItems from alarms](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-create-OpsItems-from-CloudWatch-Alarms.html) and [ Incident creation](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-creation.html).
**Note**  
To create an alarm that performs an SSM Incident Manager action, you must have certain permissions. For more information, see [ Identity-based policy examples for AWS Systems Manager Incident Manager](https://docs.aws.amazon.com/incident-manager/latest/userguide/security_iam_id-based-policy-examples.html).

1.  Choose **Next**. 

1.  For **Name and description**, enter a name and description for your alarm. The name must contain only UTF-8 characters, and can't contain ASCII control characters. The description can include markdown formatting, which is displayed only in the alarm **Details** tab in the CloudWatch console. The markdown can be useful to add links to runbooks or other internal resources. 

1.  For **Preview and create**, check that your configuration is correct, and choose **Create alarm**. 