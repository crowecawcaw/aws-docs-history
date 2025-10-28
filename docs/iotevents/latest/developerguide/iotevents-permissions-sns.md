End of support notice: On May 20, 2026, AWS will end support for
AWS IoT Events. After May 20, 2026, you will no longer be able to access the AWS IoT Events console or AWS IoT Events
resources. For more information, see [AWS IoT Events end of
support](iotevents-end-of-support.md "iotevents-end-of-support.md").

# Amazon SNS messaging role policy for AWS IoT Events

Integrating AWS IoT Events with Amazon SNS requires careful permission management for secure and
efficient notification delivery. This guide walks you through the process of configuring
IAM roles and policies to allow AWS IoT Events to publish messages to Amazon SNS topics.

The following policy documents provide the role policy and trust policy that allow AWS IoT Events
to send SNS messages.

Role policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "sns:*"
 ],
 "Effect": "Allow",
 "Resource": "`arn:aws:sns:us-east-1:123456789012:testAction`"
 }
 ]
}`

```

Trust policy:

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
 "iotevents.amazonaws.com"
 ]
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```
