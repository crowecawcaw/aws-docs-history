End of support notice: On May 20, 2026, AWS will end support for
AWS IoT Events. After May 20, 2026, you will no longer be able to access the AWS IoT Events console or AWS IoT Events
resources. For more information, see [AWS IoT Events end of
support](iotevents-end-of-support.md "iotevents-end-of-support.md").

# Example: Configure logging options for AWS IoT Events

Proper logging is important for monitoring, debugging, and auditing your AWS IoT Events
applications. This section provides an overview of logging options available in AWS IoT Events.

This example demonstrates how to configure an IAM role that allows AWS IoT Events to log data to
CloudWatch Logs. The use of wildcards (`*`) in the resource ARN allows for comprehensive
logging across your AWS IoT Events infrastructure.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "iotevents.amazonaws.com"
 ]
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`123456789012`"
 },
 "ArnEquals": {
 "aws:SourceArn": "arn:aws:iotevents:`us-east-1`:`123456789012`:*"
 }
 }
 }
 ]
}`

```
