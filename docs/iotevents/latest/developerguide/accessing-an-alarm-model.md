End of support notice: On May 20, 2026, AWS will end support for
AWS IoT Events. After May 20, 2026, you will no longer be able to access the AWS IoT Events console or AWS IoT Events
resources. For more information, see [AWS IoT Events end of
support](iotevents-end-of-support.md "iotevents-end-of-support.md").

# Example: Secure access to an AWS IoT Events alarm model

This example demonstrates how to create an IAM policy that allows AWS IoT Events to securely
access alarm models. The policy uses conditions to ensure that only the specified AWS
account and AWS IoT Events service can assume the role.

In this example, the role can access any alarm model within the specified AWS account,
as indicated by the `*` wildcard in the alarm model ARN. The
`aws:SourceAccount` and `aws:SourceArn` conditions work together to
prevent the confused deputy problem.

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
 "aws:SourceArn": "arn:aws:iotevents:`us-east-1`:`123456789012`:alarmModel/*"
 }
 }
 }
 ]
}`

```
