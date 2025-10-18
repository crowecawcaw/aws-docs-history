# Creating CloudWatch alarms for CloudTrail events: examples

This topic describes how to configure alarms for CloudTrail events, and includes examples.

###### Topics

* [Prerequisites](#cloudwatch-alarms-prerequisites "#cloudwatch-alarms-prerequisites")
* [Create a metric filter and create an alarm](#cloudwatch-alarms-metric-filter-alarm "#cloudwatch-alarms-metric-filter-alarm")
* [Example security group configuration changes](#cloudwatch-alarms-for-cloudtrail-security-group "#cloudwatch-alarms-for-cloudtrail-security-group")
* [Example AWS Management Console sign-in failures](#cloudwatch-alarms-for-cloudtrail-signin "#cloudwatch-alarms-for-cloudtrail-signin")
* [Example: IAM policy changes](#cloudwatch-alarms-for-cloudtrail-iam-policy-changes "#cloudwatch-alarms-for-cloudtrail-iam-policy-changes")
* [Configuring notifications for CloudWatch Logs alarms](#cloudtrail-configure-notifications-for-cloudwatch-logs-alarms "#cloudtrail-configure-notifications-for-cloudwatch-logs-alarms")

## Prerequisites


Before you can use the examples in this topic, you must:



* Create a trail with the console or CLI.
* Create a log group, which you can do as part of creating a trail. For more information about creating a trail, 
 see [Creating a trail with the CloudTrail console](cloudtrail-create-a-trail-using-the-console-first-time.md "cloudtrail-create-a-trail-using-the-console-first-time.md").
* Specify or create an IAM role that grants CloudTrail the permissions to create a
 CloudWatch Logs log stream in the log group that you specify and to deliver CloudTrail events to
 that log stream. The default `CloudTrail_CloudWatchLogs_Role` does
 this for you.

For more information, see [Sending events to CloudWatch Logs](send-cloudtrail-events-to-cloudwatch-logs.md "send-cloudtrail-events-to-cloudwatch-logs.md"). Examples in this
 section are performed in the Amazon CloudWatch Logs console. For more information about how to create
 metric filters and alarms, see [Creating metrics from log events using filters](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/MonitoringLogData.html "https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/MonitoringLogData.html") and [Using Amazon CloudWatch alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md") in the
 *Amazon CloudWatch User Guide*.


## Create a metric filter and create an alarm


To create an alarm, you must first create a metric filter, and then configure an alarm
 based on the filter. The procedures are shown for all examples. For more information
 about syntax for metric filters and patterns for CloudTrail log events, see the JSON-related
 sections of [Filter and pattern
 syntax](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html "https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html") in the *Amazon CloudWatch Logs User Guide*.


## Example security group configuration changes


Follow this procedure to create an Amazon CloudWatch alarm that is triggered when configuration
 changes occur on security groups.


### Create a metric filter


1. Open the CloudWatch console at
 [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, under **Logs**, choose **Log groups**.
3. In the list of log groups, choose the log group that you created for your trail.
4. From the **Metric filters** or **Actions** menu, choose **Create metric
 filter**.
5. On the **Define pattern** page, in **Create filter
 pattern**, enter the following for **Filter
 pattern**.



```
{ ($.eventName = AuthorizeSecurityGroupIngress) || ($.eventName = AuthorizeSecurityGroupEgress) || ($.eventName = RevokeSecurityGroupIngress) || ($.eventName = RevokeSecurityGroupEgress) || ($.eventName = CreateSecurityGroup) || ($.eventName = DeleteSecurityGroup) }
```
6. In **Test pattern**, leave defaults. Choose
 **Next**.
7. On the **Assign metric** page, for **Filter name**,
 enter `SecurityGroupEvents`.
8. In **Metric details**, turn on **Create new**, and then
 enter `CloudTrailMetrics` for **Metric
 namespace**.
9. For **Metric name**, type
 `SecurityGroupEventCount`.
10. For **Metric value**, type `1`.
11. Leave **Default value** blank.
12. Choose **Next**.
13. On the **Review and create** page, review your choices.
 Choose **Create metric filter** to create the filter, or
 choose **Edit** to go back and change values.

### Create an alarm


After you create the metric filter, the CloudWatch Logs log group details page for your CloudTrail trail
 log group opens. Follow this procedure to create an alarm.


1. On the **Metric filters** tab, find the metric filter you created in
 [Create a metric filter](#cloudwatch-alarms-for-cloudtrail-security-group-metric-filter "#cloudwatch-alarms-for-cloudtrail-security-group-metric-filter"). Fill the check box for the metric filter. In the **Metric
 filters** bar, choose **Create alarm**.
2. For **Specify metric and
 conditions**, enter the following.


	1. For **Graph**, the line is set at
	 `1` based on other settings you make when
	 you create your alarm.
	2. For **Metric name**, keep the current metric
	 name, `SecurityGroupEventCount`.
	3. For **Statistic**, keep the default,
	 `Sum`.
	4. For **Period**, keep the default, `5
	 minutes`.
	5. In **Conditions**, for **Threshold
	 type**, choose **Static**.
	6. For **Whenever `metric_name`
	 is**, choose **Greater/Equal**.
	7. For the threshold value, enter
	 `1`.
	8. In **Additional configuration**, leave defaults.
	 Choose **Next**.
3. On the **Configure actions** page, choose **Notification**, and then choose **In
 alarm**, which indicates that the action is taken when the
 threshold of 1 change event in 5 minutes is crossed, and
 **SecurityGroupEventCount** is in an alarm
 state.


	1. For **Send a notification to the following SNS topic**, choose
	 **Create new topic**.
	2. Enter `SecurityGroupChanges_CloudWatch_Alarms_Topic`
	 as the name for the new Amazon SNS topic.
	3. In **Email endpoints that will receive the
	 notification**, enter the email addresses of users whom you
	 want to receive notifications if this alarm is raised. Separate
	 email addresses with commas.
	
	
	Each email recipient will receive an email asking them to
	 confirm that they want to be subscribed to the Amazon SNS topic.
	4. Choose **Create topic**.
4. For this example, skip the other action types. Choose
 **Next**.
5. On the **Add name and description** page, enter a
 friendly name for the alarm, and a description. For this example, enter
 `Security group configuration changes` for the
 name, and `Raises alarms if security group configuration changes
 occur` for the description. Choose
 **Next**.
6. On the **Preview and create** page, review your choices.
 Choose **Edit** to make changes, or choose **Create
 alarm** to create the alarm.


After you create the alarm, CloudWatch opens the **Alarms**
 page. The alarm's **Actions** column shows
 **Pending confirmation** until all email recipients on
 the SNS topic have confirmed that they want to subscribe to SNS
 notifications.

## Example AWS Management Console sign-in failures


Follow this procedure to create an Amazon CloudWatch alarm that is triggered when there are three or
 more AWS Management Console sign-in failures during a five minute period.


### Create a metric filter


1. Open the CloudWatch console at
 [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, under **Logs**, choose **Log groups**.
3. In the list of log groups, choose the log group that you created for your trail.
4. From the **Metric filters** or **Actions** menu, choose **Create metric
 filter**.
5. On the **Define pattern** page, in **Create
 filter pattern**, enter the following for **Filter
 pattern**.



```
{ ($.eventName = ConsoleLogin) && ($.errorMessage = "Failed authentication") }
```
6. In **Test pattern**, leave defaults. Choose
 **Next**.
7. On the **Assign metric** page, for **Filter
 name**, enter
 `ConsoleSignInFailures`.
8. In **Metric details**, turn on **Create
 new**, and then enter `CloudTrailMetrics`
 for **Metric namespace**.
9. For **Metric name**, type
 `ConsoleSigninFailureCount`.
10. For **Metric value**, type `1`.
11. Leave **Default value** blank.
12. Choose **Next**.
13. On the **Review and create** page, review your choices.
 Choose **Create metric filter** to create the filter, or
 choose **Edit** to go back and change values.

### Create an alarm


After you create the metric filter, the CloudWatch Logs log group details page for your CloudTrail
 trail log group opens. Follow this procedure to create an alarm.


1. On the **Metric filters** tab, find the metric filter you
 created in [Create a metric filter](#cloudwatch-alarms-for-cloudtrail-signin-metric-filter "#cloudwatch-alarms-for-cloudtrail-signin-metric-filter"). Fill
 the check box for the metric filter. In the **Metric
 filters** bar, choose **Create alarm**.
2. On the **Create Alarm** page, in **Specify metric
 and conditions**, enter the following.


	1. For **Graph**, the line is set at
	 `3` based on other settings you make when
	 you create your alarm.
	2. For **Metric name**, keep the current metric
	 name, `ConsoleSigninFailureCount`.
	3. For **Statistic**, keep the default,
	 `Sum`.
	4. For **Period**, keep the default, `5
	 minutes`.
	5. In **Conditions**, for **Threshold
	 type**, choose **Static**.
	6. For **Whenever `metric_name`
	 is**, choose **Greater/Equal**.
	7. For the threshold value, enter
	 `3`.
	8. In **Additional configuration**, leave defaults.
	 Choose **Next**.
3. On the **Configure actions** page, for **Notification**, choose **In
 alarm**, which indicates that the action is taken when the
 threshold of 3 change events in 5 minutes is crossed, and
 **ConsoleSigninFailureCount** is in an alarm
 state.


	1. For **Send a notification to the following SNS topic**, choose
	 **Create new topic**.
	2. Enter
	 `ConsoleSignInFailures_CloudWatch_Alarms_Topic`
	 as the name for the new Amazon SNS topic.
	3. In **Email endpoints that will receive the
	 notification**, enter the email addresses of users whom you
	 want to receive notifications if this alarm is raised. Separate
	 email addresses with commas.
	
	
	Each email recipient will receive an email asking them to
	 confirm that they want to be subscribed to the Amazon SNS topic.
	4. Choose **Create topic**.
4. For this example, skip the other action types. Choose
 **Next**.
5. On the **Add name and description** page, enter a
 friendly name for the alarm, and a description. For this example, enter
 `Console sign-in failures` for the name, and
 `Raises alarms if more than 3 console sign-in failures occur
 in 5 minutes` for the description. Choose
 **Next**.
6. On the **Preview and create** page, review your choices.
 Choose **Edit** to make changes, or choose **Create
 alarm** to create the alarm.


After you create the alarm, CloudWatch opens the **Alarms**
 page. The alarm's **Actions** column shows
 **Pending confirmation** until all email recipients on
 the SNS topic have confirmed that they want to subscribe to SNS
 notifications.

## Example: IAM policy changes


Follow this procedure to create an Amazon CloudWatch alarm that is triggered when an API call is made
 to change an IAM policy.


### Create a metric filter


1. Open the CloudWatch console at
 [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Logs**.
3. In the list of log groups, choose the log group that you created for your trail.
4. Choose **Actions**, and then choose **Create
 metric filter**.
5. On the **Define pattern** page, in **Create
 filter pattern**, enter the following for **Filter
 pattern**.



```
{($.eventName=DeleteGroupPolicy)||($.eventName=DeleteRolePolicy)||($.eventName=DeleteUserPolicy)||($.eventName=PutGroupPolicy)||($.eventName=PutRolePolicy)||($.eventName=PutUserPolicy)||($.eventName=CreatePolicy)||($.eventName=DeletePolicy)||($.eventName=CreatePolicyVersion)||($.eventName=DeletePolicyVersion)||($.eventName=AttachRolePolicy)||($.eventName=DetachRolePolicy)||($.eventName=AttachUserPolicy)||($.eventName=DetachUserPolicy)||($.eventName=AttachGroupPolicy)||($.eventName=DetachGroupPolicy)}
```
6. In **Test pattern**, leave defaults. Choose
 **Next**.
7. On the **Assign metric** page, for **Filter
 name**, enter `IAMPolicyChanges`.
8. In **Metric details**, turn on **Create
 new**, and then enter `CloudTrailMetrics`
 for **Metric namespace**.
9. For **Metric name**, type
 `IAMPolicyEventCount`.
10. For **Metric value**, type `1`.
11. Leave **Default value** blank.
12. Choose **Next**.
13. On the **Review and create** page, review your choices.
 Choose **Create metric filter** to create the filter, or
 choose **Edit** to go back and change values.

### Create an alarm


After you create the metric filter, the CloudWatch Logs log group details page for your CloudTrail
 trail log group opens. Follow this procedure to create an alarm.


1. On the **Metric filters** tab, find the metric filter you
 created in [Create a metric filter](#cloudwatch-alarms-for-cloudtrail-iam-policy-changes-metric-filter "#cloudwatch-alarms-for-cloudtrail-iam-policy-changes-metric-filter"). Fill the check box for the metric filter. In the **Metric
 filters** bar, choose **Create alarm**.
2. On the **Create Alarm** page, in **Specify metric
 and conditions**, enter the following.


	1. For **Graph**, the line is set at
	 `1` based on other settings you make when
	 you create your alarm.
	2. For **Metric name**, keep the current metric
	 name, `IAMPolicyEventCount`.
	3. For **Statistic**, keep the default,
	 `Sum`.
	4. For **Period**, keep the default, `5
	 minutes`.
	5. In **Conditions**, for **Threshold
	 type**, choose **Static**.
	6. For **Whenever `metric_name`
	 is**, choose **Greater/Equal**.
	7. For the threshold value, enter
	 `1`.
	8. In **Additional configuration**, leave defaults.
	 Choose **Next**.
	9.
3. On the **Configure actions** page, for **Notification**, choose **In
 alarm**, which indicates that the action is taken when the
 threshold of 1 change event in 5 minutes is crossed, and
 **IAMPolicyEventCount** is in an alarm state.


	1. For **Send a notification to the following SNS topic**, choose
	 **Create new topic**.
	2. Enter
	 `IAM_Policy_Changes_CloudWatch_Alarms_Topic`
	 as the name for the new Amazon SNS topic.
	3. In **Email endpoints that will receive the
	 notification**, enter the email addresses of users whom you
	 want to receive notifications if this alarm is raised. Separate
	 email addresses with commas.
	
	
	Each email recipient will receive an email asking them to
	 confirm that they want to be subscribed to the Amazon SNS topic.
	4. Choose **Create topic**.
4. For this example, skip the other action types. Choose
 **Next**.
5. On the **Add name and description** page, enter a
 friendly name for the alarm, and a description. For this example, enter
 `IAM Policy Changes` for the name, and
 `Raises alarms if IAM policy changes occur` for the
 description. Choose **Next**.
6. On the **Preview and create** page, review your choices.
 Choose **Edit** to make changes, or choose **Create
 alarm** to create the alarm.


After you create the alarm, CloudWatch opens the **Alarms**
 page. The alarm's **Actions** column shows
 **Pending confirmation** until all email recipients on
 the SNS topic have confirmed that they want to subscribe to SNS
 notifications.

## Configuring notifications for CloudWatch Logs alarms


You can configure CloudWatch Logs to send a notification whenever an alarm is triggered for CloudTrail.
 Doing so enables you to respond quickly to critical operational events captured in CloudTrail
 events and detected by CloudWatch Logs. CloudWatch uses Amazon Simple Notification Service (SNS) to send email. For more information,
 see [Setting up Amazon SNS notifications](../../../AmazonCloudWatch/latest/monitoring/Notify_Users_Alarm_Changes.md#US_SetupSNS "../../../AmazonCloudWatch/latest/monitoring/Notify_Users_Alarm_Changes.md#US_SetupSNS") in the *CloudWatch User Guide*.
