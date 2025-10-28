AWS Cloud9 is no longer available to new customers. Existing customers of
AWS Cloud9 can continue to use the service as normal.
[Learn more](https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/ "https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/")

# Viewing CloudWatch log groups and log streams using the

AWS Toolkit

A _log stream_ is a sequence of log events that share the same source.
Each separate source of logs into CloudWatch Logs makes up a separate log stream.

A _log group_ is a group of log streams that share the same retention,
monitoring, and access control settings. You can define log groups and specify which streams to
put into each group. There's no limit on the number of log streams that can belong to one log
group.

For more information, see [Working with Log Groups and Log Streams](../../../AmazonCloudWatch/latest/monitoring/Working-with-log-groups-and-streams.md "../../../AmazonCloudWatch/latest/monitoring/Working-with-log-groups-and-streams.md") in the
_Amazon CloudWatch User Guide_.

###### Topics

- [Viewing log groups and log streams with the
  CloudWatch Logs node](#viewing-log-groups "#viewing-log-groups")

## Viewing log groups and log streams with the

**CloudWatch Logs** node

1. Open AWS Explorer, if it isn't already open.
2. Click the **CloudWatch Logs** node to expand the list of log groups.

The log groups for the current AWS Region are displayed under the
**CloudWatch Logs** node. 3. To view the log streams in a specific log group, open the context (right-click) menu
for the name of the log group, and then choose **View Log
Streams**. 4. The log group's contents are displayed under the **Select a log
stream** heading.

You can choose a specific stream from the list or filter the streams by entering text
in the field.

After you choose a stream, the events in that stream are displayed in the IDE's
**Log Streams** window. For information about interacting with the log
events in each stream, see [Working with CloudWatch log events](working-CloudWatch-log-events.md "working-CloudWatch-log-events.md").
