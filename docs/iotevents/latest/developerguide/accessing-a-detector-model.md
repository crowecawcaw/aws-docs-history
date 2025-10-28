End of support notice: On May 20, 2026, AWS will end support for
AWS IoT Events. After May 20, 2026, you will no longer be able to access the AWS IoT Events console or AWS IoT Events
resources. For more information, see [AWS IoT Events end of
support](iotevents-end-of-support.md "iotevents-end-of-support.md").

# Example: Secure access to an AWS IoT Events detector

model

This example demonstrates how to create an IAM policy that securely grants access to a
specific detector model in AWS IoT Events. The policy uses conditions to ensure that only the specified
AWS account and AWS IoT Events service can assume the role, adding an extra layer of security. In
this example, the role can only access the detector model named
`WindTurbine01`.

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
 "aws:SourceArn": "arn:aws:iotevents:`us-east-1`:`123456789012`:detectorModel/`WindTurbine01`"
 }
 }
 }
 ]
}`

```
