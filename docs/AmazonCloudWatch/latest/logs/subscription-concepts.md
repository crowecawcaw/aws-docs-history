# Concepts

Each subscription filter is made up of the following key elements:

**filter pattern**

A symbolic description of how CloudWatch Logs should interpret the data in each log
event, along with filtering expressions that restrict what gets delivered to
the destination AWS resource. For more information about the filter
pattern syntax, see [Filter pattern syntax for metric filters,
subscription filters, filter log events, and Live Tail](FilterAndPatternSyntax.md "FilterAndPatternSyntax.md").

**destination arn**

The Amazon Resource Name (ARN) of the Kinesis Data Streams stream, Firehose stream, or Lambda
function you want to use as the destination of the subscription feed.

**role arn**

An IAM role that grants CloudWatch Logs the necessary permissions to put data into
the chosen destination. This role is not needed for Lambda destinations
because CloudWatch Logs can get the necessary permissions from access control settings
on the Lambda function itself.

**distribution**

The method used to distribute log data to the destination, when the
destination is a stream in Amazon Kinesis Data Streams. By default, log data is grouped by log
stream. For a more even distribution, you can group log data
randomly.

For log group-level subscriptions, the following key element is also included:

**log group name**

The log group to associate the subscription filter with. All log events
uploaded to this log group would be subject to the subscription filter, and
those that match the filter are delivered to the destination service that is
receiving the matching log events.

For account-level subscriptions, the following key element is also included:

**selection criteria**

The criteria used for selecting which log groups have the account-level
subscription filter applied. If you don't specify this, the account-level
subscription filter is applied to all log groups in the account. This field
is used to prevent infinite log loops. For more information about the
infinite log loop issue, see [Log recursion prevention](Subscriptions-recursion-prevention.md "Subscriptions-recursion-prevention.md").

Selection criteria has a size limit of 25 KB.

For centralized log groups, the following key elements are also included. These
elements can be used as field selection criteria to help in identifying the source of log data, allowing for more granular
filtering and analysis of metrics derived from centralized logs.

**@aws.account**

This field identifies the AWS account ID from which the log event
originated.

**@aws.region**

This field identifies the AWS Region where the log event
was generated.
