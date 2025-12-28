# Working with log groups and log

streams

A log stream is a sequence of log events that share the same source.
Each separate source of logs in CloudWatch Logs makes up a separate log stream.

A log group is a group of log streams that share the same retention, monitoring, and access control settings.
You can define log groups and specify which streams to put into each group.
There is no limit on the number of log streams that can belong to one log group.

For organizations that need to consolidate log data from multiple accounts and regions,
you can use CloudWatch Logs Centralization to automatically replicate log groups to a central account.
For more information, see [Cross-account cross-Region log
centralization](CloudWatchLogs_Centralization.md "CloudWatchLogs_Centralization.md").

You can use the procedures in this section to work with log groups and log streams.

## Create a log group in CloudWatch Logs

When you install the CloudWatch Logs agent on an Amazon EC2 instance using the steps in previous sections of the Amazon CloudWatch Logs User Guide, the log group is created as
part of that process. You can also create a log group directly in the CloudWatch console.

######

To create a log group

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane,
   choose **Log Management**.
3. Choose **Actions**,
   and then choose **Create log group**.
4. Enter a name
   for the log group,
   and then choose **Create log group**.

###### Tip

You can favorite log groups, as well as dashboards and alarms,
from the **_Favorites and recents_** menu
in the navigation pane.
Under the **_Recently visited_** column,
hover
over the log group
that you want to favorite,
and choose the star symbol next
to it.

## Send logs to a log group

CloudWatch Logs automatically receives log events from several AWS services. You can also
send other log events to CloudWatch Logs using one of the following methods:

- **CloudWatch agent**— The unified CloudWatch agent can send both metrics and logs
  to CloudWatch Logs. For information about installing and using the CloudWatch agent, see
  [Collecting Metrics and Logs from Amazon EC2 Instances and On-Premises Servers with the CloudWatch Agent](../monitoring/Install-CloudWatch-Agent.md "../monitoring/Install-CloudWatch-Agent.md") in the
  _Amazon CloudWatch User Guide_.
- **AWS CLI**—The [put-log-events](../../../cli/latest/reference/logs/put-log-events.md "../../../cli/latest/reference/logs/put-log-events.md")
  uploads batches of log events to CloudWatch Logs.
- **Programmatically**— The [PutLogEvents](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutLogEvents.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutLogEvents.md")
  API enables you to programmatically upload batches of log events to CloudWatch Logs.

## View log data sent to CloudWatch Logs

You can view and scroll through log data on a stream-by-stream basis as sent to CloudWatch Logs
by the CloudWatch Logs agent. You can specify the time range for the log data to view.

###### To view log data

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Log Management**.
3. For **Log Groups**, choose the log group to view the streams.
4. In the list of log groups, choose the name of the log group that you want to view.
5. In the list of log streams, choose the name of the log stream that you want to view.
6. To change how the log data is displayed, do one of the following:
   - To expand a single log event, choose the arrow next to that log event.
   - To expand all log events and view them as plain text, above the list
     of log events, choose **Text**.
   - To filter the log events, enter the desired search filter in the search field.
     For more information, see [Creating metrics from log events using filters](MonitoringLogData.md "MonitoringLogData.md").
   - To view log data for a specified date and time range, next to the
     search filter, choose the arrow next to the date and time. To specify a
     date and time range, choose **Absolute**. To choose a
     predefined number of minutes, hours, days, or weeks, choose
     **Relative**. You can also switch between UTC and
     local time zone.

## Change log data retention in CloudWatch Logs

By default, log data is stored in CloudWatch Logs indefinitely. However, you can configure how
long to store log data in a log group. Any data older than the current retention setting
is deleted. You can change the log retention for each log group at any
time.

###### Note

CloudWatch Logs doesn’t immediately delete log events when they reach their retention setting.
It typically takes up to 72 hours after that before log events are deleted, but in rare situations might take longer.

This means that if you change a log group to have a longer retention setting when it contains log events
that are past the expiration date, but haven’t been actually deleted, those log events will take
up to 72 hours to be deleted after the new retention date is reached. To make sure
that log data is deleted permanently, keep a log group at its lower retention setting until 72 hours has passed
after the end of the previous
retention period, or you have confirmed that the older log events are deleted.

When log events reach their retention setting they are marked for deletion. After
they are marked for deletion, they do not add to your archival storage costs anymore, even if
they are not actually deleted until later. These log events marked for deletion are also not
included when you use an API to retrieve the `storedBytes` value to see how many bytes a log group is storing.

###### To change the logs retention setting

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Logs**, **Log groups**.
3. Find the log group to update.
4. In the **Retention** column for that log group,
   choose the current retention setting, such as **Never
   Expire**.
5. In **Retention setting**, for **Expire events after**,
   choose a log retention value, and then choose **Save**.

## Protecting log groups from deletion

You can optionally enable deletion protection to prevent accidental deletion of important log groups.
For detailed information about deletion protection, see [Protecting log groups from deletion](protecting-log-groups-from-deletion.md "protecting-log-groups-from-deletion.md").

## Tag log groups in Amazon CloudWatch Logs

You can assign your own metadata to the log groups you create in Amazon CloudWatch Logs in the form of
_tags_. A tag is a key-value pair that you define for a log group. Using
tags is a simple yet powerful way to manage AWS resources and organize data, including
billing data.

###### Note

You can use tags to control access to CloudWatch Logs resources, including log groups and
destinations. Access to log streams is controlled at the log group level, because of the hierarchical relation
between log groups and log streams. For more information about using tags to control access, see
[Controlling access to Amazon Web Services resources using tags](../../../IAM/latest/UserGuide/access_tags.md "../../../IAM/latest/UserGuide/access_tags.md").

###### Contents

- [Tag basics](#tagging-basics "#tagging-basics")
- [Tracking costs using tagging](#tagging-billing "#tagging-billing")
- [Tag restrictions](#tagging-restrictions "#tagging-restrictions")
- [Tagging log groups using the AWS CLI](#log-group-tagging-cli "#log-group-tagging-cli")
- [Tagging log groups using the CloudWatch Logs API](#log-group-tagging-api "#log-group-tagging-api")

### Tag basics

You use AWS CloudFormation the AWS CLI, or CloudWatch Logs API to complete the following tasks:

- Add tags to a log group when you create it.
- Add tags to an existing log group.
- List the tags for a log group.
- Remove tags from a log group.

You can use tags to categorize your log groups. For example, you can categorize them
by purpose, owner, or environment. Because you define the key and value for each tag,
you can create a custom set of categories to meet your specific needs. For example, you
might define a set of tags that helps you track log groups by owner and associated
application. Here are several examples of tags:

- Project: Project name
- Owner: Name
- Purpose: Load testing
- Application: Application name
- Environment: Production

### Tracking costs using tagging

You can use tags to categorize and track your AWS costs. When you apply tags to your
AWS resources, including log groups, your AWS cost allocation report includes usage and
costs aggregated by tags. You can apply tags that represent business categories (such as
cost centers, application names, or owners) to organize your costs across multiple
services. For more information, see [Use
Cost Allocation Tags for Custom Billing Reports](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md") in the
_AWS Billing User Guide_.

### Tag restrictions

The following restrictions apply to tags.

###### Basic restrictions

- The maximum number of tags per log group is 50.
- Tag keys and values are case sensitive.
- You can't change or edit tags for a deleted log group.

###### Tag key restrictions

- Each tag key must be unique. If you add a tag with a key that's already in
  use, your new tag overwrites the existing key-value pair.
- You can't start a tag key with `aws:` because this prefix is
  reserved for use by AWS. AWS creates tags that begin with this prefix on your
  behalf, but you can't edit or delete them.
- Tag keys must be between 1 and 128 Unicode characters in length.
- Tag keys must consist of the following characters: Unicode letters, digits,
  white space, and the following special characters: `_ . / = + -
@`.

###### Tag value restrictions

- Tag values must be between 0 and 255 Unicode characters in length.
- Tag values can be blank. Otherwise, they must consist of the following
  characters: Unicode letters, digits, white space, and any of the following
  special characters: `_ . / = + - @`.

### Tagging log groups using the AWS CLI

You can add, list, and remove tags using the AWS CLI. For examples, see the following
documentation:

[create-log-group](../../../cli/latest/reference/logs/create-log-group.md "../../../cli/latest/reference/logs/create-log-group.md")

Creates a log group. You can optionally add tags when you create the log group.

[tag-resource](../../../cli/latest/reference/logs/tag-resource.md "../../../cli/latest/reference/logs/tag-resource.md")

Assigns one or more tags (key-value pairs) to the specified CloudWatch Logs resource.

[list-tags-for-resource](../../../cli/latest/reference/logs/list-tags-for-resource.md "../../../cli/latest/reference/logs/list-tags-for-resource.md")

Displays the tags the are associated with a CloudWatch Logs resource.

[untag-resource](../../../cli/latest/reference/logs/untag-log-group.md "../../../cli/latest/reference/logs/untag-log-group.md")

Removes one or more tags from the specified CloudWatch Logs resource.

### Tagging log groups using the CloudWatch Logs API

You can add, list, and remove tags using the CloudWatch Logs API. For examples, see the
following documentation:

[CreateLogGroup](../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLogGroup.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLogGroup.md")

Creates a log group. You can optionally add tags when you create the log group.

[TagResource](../../../AmazonCloudWatchLogs/latest/APIReference/API_TagResource.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_TagResource.md")

Assigns one or more tags (key-value pairs) to the specified CloudWatch Logs resource.

[ListTagsForResource](../../../AmazonCloudWatchLogs/latest/APIReference/API_ListTagsForResource.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_ListTagsForResource.md")

Displays the tags the are associated with a CloudWatch Logs resource.

[UntagResource](../../../AmazonCloudWatchLogs/latest/APIReference/API_UntagLogGroup.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_UntagLogGroup.md")

Removes one or more tags from the specified CloudWatch Logs resource.
