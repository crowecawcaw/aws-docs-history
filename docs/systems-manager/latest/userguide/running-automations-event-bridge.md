• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Run automations based on EventBridge

events

You can start an automation by specifying a runbook as the target of an Amazon EventBridge
event. You can start automations according to a schedule, or when a specific AWS
system event occurs. For example, let's say you create a runbook named
_BootStrapInstances_ that installs software on an instance when
an instance starts. To specify the _BootStrapInstances_ runbook (and
corresponding automation) as a target of an EventBridge event, you first create a new EventBridge
rule. (Here's an example rule: **Service name**: EC2, **Event
Type**: EC2 Instance State-change Notification, **Specific
state(s)**: running, **Any instance**.) Then you use the
following procedures to specify the _BootStrapInstances_ runbook as
the target of the event using the EventBridge console and AWS Command Line Interface (AWS CLI). When a new
instance starts, the system runs the automation and installs software.

For information about creating runbooks, see [Creating your own runbooks](automation-documents.md "automation-documents.md").

## Creating an EventBridge event that uses a

runbook (console)

Use the following procedure to configure a runbook as the target of a EventBridge
event.

###### To configure a runbook as a target of a EventBridge event rule

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the navigation pane, choose **Rules**.
3. Choose **Create rule**.
4. Enter a name and description for the rule.

A rule can't have the same name as another rule in the same Region and on
the same event bus. 5. For **Event bus**, choose the event bus that you want to
associate with this rule. If you want this rule to respond to matching
events that come from your own AWS account, select
**default**. When an AWS service in your account
emits an event, it always goes to your account’s default event bus. 6. Choose how the rule is triggered.

| To create a rule based on... | Do this...                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Event                        | 1. For **Rule type**, choose<br>**Rule with an event<br>pattern**.<br>2. Choose **Next**.<br>3. For **Event source**, choose<br>**AWS events or EventBridge partner<br>events**.<br>4. In the **Event pattern**<br>section, do one of the following:<br>• To use a template to create your event<br>pattern, choose **Event pattern<br>form\*<br>• and choose **Event<br>source**, **AWS<br>service**, and **Event<br>type**. If you choose **All<br>Events\*<br>• as the event type, all events<br>emitted by the AWS service will match the<br>rule.<br>To customize the template, choose<br>**Custom pattern (JSON editor)**<br>and make your changes.<br>• To use a custom event pattern, choose<br>**Custom pattern (JSON editor)**<br>and create your event pattern. |
| Schedule                     | 1. For **Rule type**, choose<br>**Schedule**.<br>2. Choose **Next**.<br>3. For **Schedule pattern**, do<br>one of the following:<br>• To use a cron expression to define the<br>schedule, choose **A fine-grained schedule<br>that runs at a specific time, such as 8:00 a.m.<br>PST on the first Monday of every month**<br>and enter the cron expression.<br>• To use a rate expression to define the<br>schedule, choose \*_A schedule that runs at<br>a regular rate, such as every 10<br>minutes_<br>• and enter the rate<br>expression.                                                                                                                                                                                                                              |

7. Choose **Next**.
8. For **Target types**, choose **AWS
   service**.
9. For **Select a target**, choose **Systems Manager
   Automation**.
10. For **Document**, choose a runbook to use when your
    target is invoked.
11. In the **Configure automation parameter(s)** section,
    either keep the default parameter values (if available) or enter your own
    values.

###### Note

To create a target, you must specify a value for each required
parameter. If you don't, the system creates the rule, but the rule won't
run. 12. For many target types, EventBridge needs permissions to send events to the
target. In these cases, EventBridge can create the IAM role needed for your rule
to run. Do one of the following:

    * To create an IAM role automatically, choose **Create a
     new role for this specific resource**.
    * To use an IAM role that you created earlier, choose
     **Use existing role** and select the existing
     role from the dropdown. Note that you might need to update the trust
     policy for your IAM role to include EventBridge. The following is an
     example:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "",
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "`events.amazonaws.com`",
 "ssm.amazonaws.com"
 ]
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

13. Choose **Next**.
14. (Optional) Enter one or more tags for the rule. For more information, see
    [Tagging Your
    Amazon EventBridge Resources](../../../eventbridge/latest/userguide/eventbridge-tagging.md "../../../eventbridge/latest/userguide/eventbridge-tagging.md") in the
    _Amazon EventBridge User Guide_.
15. Choose **Next**.
16. Review the details of the rule and choose **Create
    rule**.

## Create an EventBridge event that uses a

runbook (command line)

The following procedure describes how to use the AWS CLI (on Linux or Windows) or
AWS Tools for PowerShell to create an EventBridge event rule and configure a runbook as the
target.

###### To configure a runbook as a target of an EventBridge event rule

1. Install and configure the AWS CLI or the AWS Tools for PowerShell, if you haven't already.

For information, see [Installing or updating the
latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") and [Installing the
AWS Tools for PowerShell](../../../powershell/latest/userguide/pstools-getting-set-up.md "../../../powershell/latest/userguide/pstools-getting-set-up.md"). 2. Create a command to specify a new EventBridge event rule. Replace each
`example resource placeholder` with your own
information.

_Triggers based on a schedule_

Linux & macOS

```
aws events put-rule \
--name "`rule name`" \
--schedule-expression "`cron or rate expression`"
```

Windows

```
aws events put-rule ^
--name "`rule name`" ^
--schedule-expression "`cron or rate expression`"
```

PowerShell

```
Write-CWERule `
-Name "`rule name`" `
-ScheduleExpression "`cron or rate expression`"
```

The following example creates an EventBridge event rule that starts every day at
9:00 AM (UTC).

Linux & macOS

```
aws events put-rule \
--name "DailyAutomationRule" \
--schedule-expression "cron(0 9 * * ? *)"
```

Windows

```
aws events put-rule ^
--name "DailyAutomationRule" ^
--schedule-expression "cron(0 9 * * ? *)"
```

PowerShell

```
Write-CWERule `
-Name "DailyAutomationRule" `
-ScheduleExpression "cron(0 9 * * ? *)"
```

_Triggers based on an event_

Linux & macOS

```
aws events put-rule \
--name "`rule name`" \
--event-pattern "{\"source\":[\"aws.`service`\"],\"detail-type\":[\"`service event detail type`\"]}"
```

Windows

```
aws events put-rule ^
--name "`rule name`" ^
--event-pattern "{\"source\":[\"aws.`service`\"],\"detail-type\":[\"`service event detail type`\"]}"
```

PowerShell

```
Write-CWERule `
-Name "`rule name`" `
-EventPattern '{"source":["aws.`service`"],"detail-type":["`service event detail type`"]}'
```

The following example creates an EventBridge event rule that starts when any EC2
instance in the Region changes state.

Linux & macOS

```
aws events put-rule \
--name "EC2InstanceStateChanges" \
--event-pattern "{\"source\":[\"aws.ec2\"],\"detail-type\":[\"EC2 Instance State-change Notification\"]}"
```

Windows

```
aws events put-rule ^
--name "EC2InstanceStateChanges" ^
--event-pattern "{\"source\":[\"aws.ec2\"],\"detail-type\":[\"EC2 Instance State-change Notification\"]}"
```

PowerShell

```
Write-CWERule `
-Name "`EC2InstanceStateChanges`" `
-EventPattern '{"source":["aws.ec2"],"detail-type":["EC2 Instance State-change Notification"]}'
```

The command returns details for the new EventBridge rule similar to the
following.

Linux & macOS

```
{
"RuleArn": "arn:aws:events:us-east-1:123456789012:rule/automationrule"
}
```

Windows

```
{
"RuleArn": "arn:aws:events:us-east-1:123456789012:rule/automationrule"
}
```

PowerShell

```
arn:aws:events:us-east-1:123456789012:rule/EC2InstanceStateChanges
```

3. Create a command to specify a runbook as a target of the EventBridge event rule
   you created in step 2. Replace each `example resource
placeholder` with your own information.

Linux & macOS

```
aws events put-targets \
--rule `rule name` \
--targets '{"Arn": " arn:aws:ssm:`region`:`account ID`:automation-definition/`runbook name`","Input":"{\"Message\":[\"{\\\"Key\\\":\\\"`key name`\\\",\\\"Values\\\":[\\\"`value`\\\"]}\"]}","Id": "`target ID`","RoleArn": "arn:aws:iam::`123456789012`:role/service-role/`EventBridge service role`"}'
```

Windows

```
aws events put-targets ^
--rule `rule name` ^
--targets '{"Arn": "arn:aws:ssm:`region`:`account ID`:automation-definition/`runbook name`","Input":"{\"Message\":[\"{\\\"Key\\\":\\\"`key name`\\\",\\\"Values\\\":[\\\"`value`\\\"]}\"]}","Id": "`target ID`","RoleArn": "arn:aws:iam::`123456789012`:role/service-role/`EventBridge service role`"}'
```

PowerShell

```
$Target = New-Object Amazon.CloudWatchEvents.Model.Target
$Target.Id = "`target ID`"
$Target.Arn = "arn:aws:ssm:`region`:`account ID`:automation-definition/`runbook name`"
$Target.RoleArn = "arn:aws:iam::`123456789012`:role/service-role/`EventBridge service role`"
$Target.Input = '{"`input parameter`":["`value`"],"AutomationAssumeRole":["arn:aws:iam::`123456789012`:role/`AutomationServiceRole`"]}'

Write-CWETarget `
-Rule "`rule name`" `
-Target $Target
```

The following example creates an EventBridge event target that starts the
specified instance ID using the runbook
`AWS-StartEC2Instance`.

Linux & macOS

```
aws events put-targets \
--rule DailyAutomationRule \
--targets '{"Arn": "arn:aws:ssm:`region`:*:automation-definition/AWS-StartEC2Instance","Input":"{\"InstanceId\":[\"i-02573cafcfEXAMPLE\"],\"AutomationAssumeRole\":[\"arn:aws:iam::123456789012:role/AutomationServiceRole\"]}","Id": "Target1","RoleArn": "arn:aws:iam::123456789012:role/service-role/AWS_Events_Invoke_Start_Automation_Execution_1213609520"}'
```

Windows

```
aws events put-targets ^
--rule DailyAutomationRule ^
--targets '{"Arn": "arn:aws:ssm:`region`:*:automation-definition/AWS-StartEC2Instance","Input":"{\"InstanceId\":[\"i-02573cafcfEXAMPLE\"],\"AutomationAssumeRole\":[\"arn:aws:iam::123456789012:role/AutomationServiceRole\"]}","Id": "Target1","RoleArn": "arn:aws:iam::123456789012:role/service-role/AWS_Events_Invoke_Start_Automation_Execution_1213609520"}'
```

PowerShell

```
$Target = New-Object Amazon.CloudWatchEvents.Model.Target
$Target.Id = "Target1"
$Target.Arn = "arn:aws:ssm:`region`:*:automation-definition/AWS-StartEC2Instance"
$Target.RoleArn = "arn:aws:iam::123456789012:role/service-role/AWS_Events_Invoke_Start_Automation_Execution_1213609520"
$Target.Input = '{"InstanceId":["i-02573cafcfEXAMPLE"],"AutomationAssumeRole":["arn:aws:iam::123456789012:role/AutomationServiceRole"]}'

Write-CWETarget `
-Rule "DailyAutomationRule" `
-Target $Target
```

The system returns information like the following.

Linux & macOS

```
{
"FailedEntries": [],
"FailedEntryCount": 0
}
```

Windows

```
{
"FailedEntries": [],
"FailedEntryCount": 0
}
```

PowerShell
There is no output if the command succeeds for
PowerShell.
