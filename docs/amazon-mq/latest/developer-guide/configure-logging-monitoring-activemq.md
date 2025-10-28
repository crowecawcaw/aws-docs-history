# Configuring Amazon MQ for ActiveMQ logs

To allow Amazon MQ to publish logs to CloudWatch Logs, you must [add a permission to your Amazon MQ user](#security-logging-monitoring-configure-cloudwatch-permissions "#security-logging-monitoring-configure-cloudwatch-permissions")
and also [configure a resource-based policy for Amazon MQ](#security-logging-monitoring-configure-cloudwatch-resource-permissions "#security-logging-monitoring-configure-cloudwatch-resource-permissions") before you create or restart the broker.

###### Note

When you turn on logs and publish messages from the ActiveMQ web console,
the content of the message is sent to CloudWatch and displayed in the logs.

The following describes the steps to configure CloudWatch logs for your ActiveMQ brokers.

###### Topics

- [Understanding the structure of logging in CloudWatch Logs](#security-logging-monitoring-configure-cloudwatch-structure "#security-logging-monitoring-configure-cloudwatch-structure")
- [Add
  the CreateLogGroup permission to your Amazon MQ user](#security-logging-monitoring-configure-cloudwatch-permissions "#security-logging-monitoring-configure-cloudwatch-permissions")
- [Configure a resource-based policy for Amazon MQ](#security-logging-monitoring-configure-cloudwatch-resource-permissions "#security-logging-monitoring-configure-cloudwatch-resource-permissions")
- [Cross-service confused deputy prevention](#security-logging-monitoring-configure-cloudwatch-confused-deputy "#security-logging-monitoring-configure-cloudwatch-confused-deputy")

## Understanding the structure of logging in CloudWatch Logs

You can enable _general_ and _audit_ logging
when you configure advanced broker settings when you create a broker, or when you edit a
broker.

General logging enables the default `INFO` logging level
(`DEBUG` logging isn't supported) and publishes
`activemq.log` to a log group in your CloudWatch account. The log group has
a format similar to the following:

```
/aws/amazonmq/broker/b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9/general
```

[Audit logging](http://activemq.apache.org/audit-logging.html "http://activemq.apache.org/audit-logging.html")
enables logging of management actions taken using JMX or using the ActiveMQ Web
Console and publishes `audit.log` to a log group in your CloudWatch account.
The log group has a format similar to the following:

```
/aws/amazonmq/broker/b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9/audit
```

Depending on whether you have a [single-instance broker](amazon-mq-broker-architecture.md#single-broker-deployment "amazon-mq-broker-architecture.md#single-broker-deployment") or an [active/standby broker](amazon-mq-broker-architecture.md#active-standby-broker-deployment "amazon-mq-broker-architecture.md#active-standby-broker-deployment"), Amazon MQ
creates either one or two log streams within each log group. The log streams have a
format similar to the following.

```
activemq-b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9-1.log
                activemq-b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9-2.log
```

The `-1` and `-2` suffixes denote individual broker
instances. For more information, see [Working with Log
Groups and Log Streams](../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md "../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md") in the _[Amazon CloudWatch Logs User Guide](../../../AmazonCloudWatch/latest/logs.md "../../../AmazonCloudWatch/latest/logs.md")_.

## Add

the `CreateLogGroup` permission to your Amazon MQ user

To allow Amazon MQ to create a CloudWatch Logs log group, you must ensure that the user who
creates or reboots the broker has the `logs:CreateLogGroup`
permission.

###### Important

If you don't add the `CreateLogGroup` permission to your Amazon MQ
user before the user creates or reboots the broker, Amazon MQ doesn't create
the log group.

The following example [IAM-based policy](../../../AmazonCloudWatch/latest/logs/iam-access-control-overview-cwl.md#identity-based-policies-cwl "../../../AmazonCloudWatch/latest/logs/iam-access-control-overview-cwl.md#identity-based-policies-cwl") grants permission for
`logs:CreateLogGroup` for users to whom this policy is attached.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "logs:CreateLogGroup",
 "Resource": "arn:aws:logs:*:*:log-group:/aws/amazonmq/*"
 }
 ]
 }`

```

###### Note

Here, the term user refers to _Users_ and not _Amazon MQ users_,
which are created when a new broker is configured. For more information regarding setting up users and
configuring IAM policies, please refer to the [Identity Management Overview](../../../IAM/latest/UserGuide/introduction_identity-management.md "../../../IAM/latest/UserGuide/introduction_identity-management.md")
section of the IAM User Guide.

For more information, see `CreateLogGroup` in the
_Amazon CloudWatch Logs API Reference_.

## Configure a resource-based policy for Amazon MQ

###### Important

If you don't configure a resource-based policy for Amazon MQ, the broker
can't publish the logs to CloudWatch Logs.

To allow Amazon MQ to publish logs to your CloudWatch Logs log group, configure a resource-based
policy to give Amazon MQ access to the following CloudWatch Logs API actions:

- `CreateLogStream` – Creates a CloudWatch Logs log stream
  for the specified log group.
- `PutLogEvents` – Delivers events to the specified
  CloudWatch Logs log stream.

The following resource-based policy grants permission for `logs:CreateLogStream` and `logs:PutLogEvents` to AWS.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": { "Service": "mq.amazonaws.com" },
 "Action": [ "logs:CreateLogStream", "logs:PutLogEvents" ],
 "Resource": "arn:aws:logs:*:*:log-group:/aws/amazonmq/*"
 }
 ]
 }`

```

This resource-based policy _must_ be configured by using the AWS CLI as shown by the following command. In the example, replace
`us-east-1` with your own information.

```
aws --region `us-east-1` logs put-resource-policy --policy-name AmazonMQ-logs \
                        --policy-document "{\"Version\": \"2012-10-17\", \"Statement\":[{ \"Effect\": \"Allow\", \"Principal\": { \"Service\": \"mq.amazonaws.com\" },
                        \"Action\": [\"logs:CreateLogStream\", \"logs:PutLogEvents\"], \"Resource\": \"arn:aws:logs:*:*:log-group:\/aws\/amazonmq\/*\" }]}"

```

###### Note

Because this example uses the `/aws/amazonmq/` prefix, you need to
configure the resource-based policy only once per AWS account, per
region.

## Cross-service confused deputy prevention

The confused deputy problem is a security issue where an entity that doesn't have permission to perform an action can coerce a
more-privileged entity to perform the action. In AWS, cross-service impersonation can result in the confused deputy problem.
Cross-service impersonation can occur when one service (the _calling service_) calls another service (the _called service_).
The calling service can be manipulated to use its permissions to act on another customer's resources in a way it should not otherwise
have permission to access. To prevent this, AWS provides tools that help you protect your data for all services with service principals
that have been given access to resources in your account.

We recommend using the `aws:SourceArn`
and `aws:SourceAccount`
global condition context keys in your Amazon MQ resource-based policy to limit CloudWatch Logs access to one or more specified brokers.

###### Note

If you use both global condition context keys, the `aws:SourceAccount` value and the account in the `aws:SourceArn` value must use the same account ID
when used in the same policy statement.

The following example demonstrates a resource-based policy that limits CloudWatch Logs access to a single Amazon MQ broker.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "mq.amazonaws.com"
 },
 "Action": [
 "logs:CreateLogStream",
 "logs:PutLogEvents"
 ],
 "Resource": "arn:aws:logs:*:*:log-group:/aws/amazonmq/*",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "123456789012",
 "aws:SourceArn": "arn:aws:mq:us-west-1:123456789012:broker:my-broker:123456789012"
 }
 }
 }
 ]
 }`

```

You can also configure your resource-based policy to limit CloudWatch Logs access to all brokers in an account, as shown in the following.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "mq.amazonaws.com"
 ]
 },
 "Action": [
 "logs:CreateLogStream",
 "logs:PutLogEvents"
 ],
 "Resource": "arn:aws:logs:*:*:log-group:/aws/amazonmq/*",
 "Condition": {
 "ArnLike": {
 "aws:SourceArn": "arn:aws:mq:*:123456789012:broker:*"
 },
 "StringEquals": {
 "aws:SourceAccount": "123456789012"
 }
 }
 }
 ]
 }`

```

For more information about the confused deputy security issue, see
[The confused deputy problem](../../../hIAM/latest/UserGuide/confused-deputy.md "../../../hIAM/latest/UserGuide/confused-deputy.md") in the _User Guide_.
