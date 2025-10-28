End of support notice: On May 20, 2026, AWS will end support for
AWS IoT Events. After May 20, 2026, you will no longer be able to access the AWS IoT Events console or AWS IoT Events
resources. For more information, see [AWS IoT Events end of
support](iotevents-end-of-support.md "iotevents-end-of-support.md").

# Example: Access an AWS IoT Events resource in a

specified region

This example demonstrates how to configure an IAM role to access AWS IoT Events resources in a
specific AWS region. By using region-specific ARNs in your IAM policies, you can restrict
access to AWS IoT Events resources across different geographical areas. This approach can help maintain
security and compliance in multi-region deployments. The region in this example is
`us-east-1`.

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
