# Sending AWS Network Firewall logs to Amazon Data Firehose

To send logs to Amazon Data Firehose, you first need to set up a Firehose delivery
stream. As part of that process, you choose a destination for storing your logs.
After you enable logging for your firewall, AWS Network Firewall delivers logs to
the destination through the HTTPS endpoint of Amazon Data Firehose. One AWS Network Firewall
log corresponds to one Amazon Data Firehose record.

Configure an Amazon Data Firehose delivery stream for your firewall
as follows.

- Create it using the same account as you use to manage the
  firewall.
- Create it in the same Region as the firewall.
- Configure it for direct put, which allows applications to access the
  delivery stream directly. In the Amazon Data Firehose console, for the delivery
  stream **Source** setting, choose **Direct PUT
  or other sources**. Through the API, set the delivery
  stream property `DeliveryStreamType` to
  `DirectPut`.
  For information about how to create an Amazon Data Firehose delivery stream and review
  the stored logs, see [Creating an Amazon Data Firehose delivery
  stream](../../../firehose/latest/dev/basic-create.md "../../../firehose/latest/dev/basic-create.md") and [What is
  Amazon Data Firehose?](../../../firehose/latest/dev/what-is-this-service.md "../../../firehose/latest/dev/what-is-this-service.md")

When you successfully enable logging to an Amazon Data Firehose data stream,
Network Firewall creates a service linked role with the necessary permissions to
write logs to it. For more information, see [Using service-linked roles](using-service-linked-roles.md "using-service-linked-roles.md").

## Permissions to publish logs

to Amazon Data Firehose

You must have the following permissions to configure your firewall to send
logs to an Amazon Data Firehose delivery stream.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "logs:CreateLogDelivery",
 "logs:GetLogDelivery",
 "logs:UpdateLogDelivery",
 "logs:DeleteLogDelivery",
 "logs:ListLogDeliveries"
 ],
 "Resource": [
 "*"
 ],
 "Effect": "Allow",
 "Sid": "FirewallLogging"
 },
 {
 "Sid": "FirewallLoggingFH1",
 "Action": [
 "iam:CreateServiceLinkedRole"
 ],
 "Resource": "*",
 "Effect": "Allow"
 },
 {
 "Sid": "FirewallLoggingFH2",
 "Action": [
 "firehose:TagDeliveryStream"
 ],
 "Resource": "arn:aws:firehose:`us-east-1`:`123456789012`:deliverystream/`delivery-stream-name`",
 "Effect": "Allow"
 }
 ]
}`

```
