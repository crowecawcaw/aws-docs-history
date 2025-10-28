# Granting access to Neptune graph using `AWSServiceRoleForNeptuneGraphPolicy`

The [AWSServiceRoleForNeptuneGraphPolicy](https://console.aws.amazon.com/iam/home#policies/AWSServiceRoleForNeptuneGraphPolicy "https://console.aws.amazon.com/iam/home#policies/AWSServiceRoleForNeptuneGraphPolicy")
managed policy below gives graphs access to CloudWatch to publish operational
and usage metrics and logs. See [nan-service-linked-roles](../../../neptune-analytics/latest/userguide/nan-service-linked-roles.md "../../../neptune-analytics/latest/userguide/nan-service-linked-roles.md").

###### Note

This policy was released on 2023-11-29.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "GraphMetrics",
 "Effect": "Allow",
 "Action": [
 "cloudwatch:PutMetricData"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "cloudwatch:namespace": [
 "AWS/Neptune",
 "AWS/Usage"
 ]
 }
 }
 },
 {
 "Sid": "GraphLogGroup",
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogGroup"
 ],
 "Resource": [
 "arn:aws:logs:*:*:log-group:/aws/neptune/*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 },
 {
 "Sid": "GraphLogEvents",
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogStream",
 "logs:PutLogEvents",
 "logs:DescribeLogStreams"
 ],
 "Resource": [
 "arn:aws:logs:*:*:log-group:/aws/neptune/*:log-stream:*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 }
 ]
}`

```
