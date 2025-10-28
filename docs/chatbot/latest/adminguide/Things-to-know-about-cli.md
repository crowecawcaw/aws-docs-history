AWS Chatbot is now Amazon Q Developer. [Learn more](service-rename.md "service-rename.md")

# Running commands using Amazon Q Developer in chat applications

Amazon Q Developer in chat applications tracks your use of command options and prompts you for any missing parameters before
it runs the command you want.

For example, if you enter `@Amazon Q lambda get-function` with no further arguments,
you're prompted for the function name. You can run the `@Amazon Q lambda list-functions`
command, find the function name you need, and re-run the first command with the corrected option.
You can add more parameters for the initial command with `@Amazon Q function-name
 `name``. Amazon Q Developer in chat applications parses your commands and helps you complete the
correct syntax so it can run the complete AWS CLI command.

###### Topics

- [Getting help for AWS services in Amazon Q Developer in chat applications](#getting-help-in-the-chat-window "#getting-help-in-the-chat-window")
- [Formatting data and viewing logs in Amazon Q Developer in chat applications](#formatting-in-the-chat-window.title "#formatting-in-the-chat-window.title")
- [Displaying Amazon CloudWatch Logs information using Amazon Q Developer in chat applications](#logs-in-the-chat-window.title "#logs-in-the-chat-window.title")
- [Creating an AWS Support case using Amazon Q Developer in chat applications](#create-a-support-case "#create-a-support-case")

## Getting help for AWS services in Amazon Q Developer in chat applications

To get help about commands for any AWS service, enter **@Amazon Q** followed by the service name, as shown following:

`@Amazon Q lambda --help`

`@Amazon Q cloudwatch describe-alarms --help`

## Formatting data and viewing logs in Amazon Q Developer in chat applications

To ensure data from Amazon CloudWatch alarms is correctly formatted, attach the **Lambda-Invoke Command Permissions** and **ReadOnly
Commands Permissions** IAM policies to the role in the Amazon Q Developer in chat applications console for users in the
chat channel.

Run the `cloudwatch describe-alarms` command to show CloudWatch alarms in chart form
as follows:

`@Amazon Q cloudwatch describe-alarms`

You can change the command to only include notifications in the alarm state, filtering out
other notifications, by adding the following option:

`@Amazon Q cloudwatch describe-alarms --state ALARM`

To see alarms from a different AWS Region, include that Region in the command:

`@Amazon Q cloudwatch describe-alarms --state ALARM --region us-east-1`

You can also filter AWS CLI output by using the optional `query` parameter. A
query uses JMESPath syntax to create an expression to filter your output to your
specifications. For more information about filtering, see [Filtering AWS CLI output](../../../cli/latest/userguide/cli-usage-filter.md "../../../cli/latest/userguide/cli-usage-filter.md") in the
_AWS Command Line Interface User Guide_. For more information about
JMESPath syntax, see [their website](https://jmespath.org/ "https://jmespath.org/"). The following
example shows how to limit AWS CLI output for the `cloudwatch describe-alarms`
command to just the alarm name, description, state, and reason attributes.

```

@Amazon Q cloudwatch describe-alarms --query
 @.{MetricAlarms:MetricAlarms[*].
 {AlarmName:AlarmName, AlarmDescription:AlarmDescription, StateValue:StateValue,
 StateReason:StateReason, Namespace:Namespace, MetricName:MetricName,
 Dimensions:Dimensions, ComparisonOperator:ComparisonOperator, Threshold:Threshold,
 Period:Period, EvaluationPeriods:EvaluationPeriods, Statistic:Statistic}}
 --region us-east-2

```

## Displaying Amazon CloudWatch Logs information using Amazon Q Developer in chat applications

CloudWatch alarm notifications show buttons in chat client notifications to view logs related to the
alarm. These notifications use the [CloudWatch Log
Insights feature](../../../AmazonCloudWatch/latest/logs/AnalyzingLogData.md "../../../AmazonCloudWatch/latest/logs/AnalyzingLogData.md"). There may be service charges for using this feature to query and show
logs.

You can view CloudWatch logs, including error logs, that are associated with the CloudWatch alarm by
choosing **Show logs** at the bottom of the alarm notification. Amazon Q Developer in chat applications
displays the first 30 log entries from the start of the alarm evaluation period. Amazon Q Developer in chat applications uses CloudWatch
Log Insights to query for logs. The query results contain a link to the CloudWatch Log Insights
console, where a user can dive deeper into logs details.

Choose **Show error logs** to filter search results to log entries
containing Error, Exception, or Fail terms.

The log shows a command that a user can copy, paste, and edit to re-run the query for
viewing logs.

## Creating an AWS Support case using Amazon Q Developer in chat applications

The **AWS Support Command Permissions** policy appears in
the Amazon Q Developer in chat applications console when you configure resources. It's provided in the Amazon Q Developer in chat applications console so that you can set
up new roles for users in your chat client to create AWS support tickets through their chat channels.

You can quickly create a new AWS support case by entering the
following:

`@Amazon Q support create-case`

Follow the prompts from Amazon Q Developer in chat applications to fill out the support case with its needed parameters. When
you complete the case information entry, Amazon Q Developer in chat applications asks for confirmation. You will not be able to
use file attachments.

###### Note

Amazon Q Developer in chat applications requires `UpperCamelCase` for the `--query` parameter. In `UpperCamelCase`, the first letter of every word is capitalized.

For any Amazon Q Developer in chat applications role that creates Support cases, you need to attach the **AWS Support command permissions** policy to the role. For existing roles, you will
need to attach the policy in the IAM console.

In the IAM console, this policy appears as **AWSSupportAccess**.

It is an AWS managed policy. Attach this policy in IAM to any role for Amazon Q Developer in chat applications usage. You
can define your own policy with greater restrictions, using this policy as a template.

The **Support Command Permissions** policy applies only to the
Support service.

The policy's JSON code is shown following:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "support:*"
 ],
 "Resource": "*"
 }
 ]
}`

```
