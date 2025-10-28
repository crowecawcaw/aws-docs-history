# Logs sent to

CloudWatch Logs

**User permissions**

To enable sending logs to CloudWatch Logs, you must be signed in with the following
permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ReadWriteAccessForLogDeliveryActions",
 "Effect": "Allow",
 "Action": [
 "logs:GetDelivery",
 "logs:GetDeliverySource",
 "logs:PutDeliveryDestination",
 "logs:GetDeliveryDestinationPolicy",
 "logs:DeleteDeliverySource",
 "logs:PutDeliveryDestinationPolicy",
 "logs:CreateDelivery",
 "logs:GetDeliveryDestination",
 "logs:PutDeliverySource",
 "logs:DeleteDeliveryDestination",
 "logs:DeleteDeliveryDestinationPolicy",
 "logs:DeleteDelivery",
 "logs:UpdateDeliveryConfiguration"
 ],
 "Resource": [
 "arn:aws:logs:`us-east-1`:`111122223333`:delivery:*",
 "arn:aws:logs:`us-east-1`:`444455556666`:delivery-source:*",
 "arn:aws:logs:`us-east-1`:`777788889999`:delivery-destination:*"
 ]
 },
 {
 "Sid": "ListAccessForLogDeliveryActions",
 "Effect": "Allow",
 "Action": [
 "logs:DescribeDeliveryDestinations",
 "logs:DescribeDeliverySources",
 "logs:DescribeDeliveries",
 "logs:DescribeConfigurationTemplates"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowUpdatesToResourcePolicyCWL",
 "Effect": "Allow",
 "Action": [
 "logs:PutResourcePolicy",
 "logs:DescribeResourcePolicies",
 "logs:DescribeLogGroups"
 ],
 "Resource": [
 "arn:aws:logs:`us-east-1`:`123456789012`:*"
 ]
 }
 ]
}`

```

**Log group resource policy**

The log group where the logs are being sent must have a resource policy that
includes certain permissions. If the log group currently does not have a resource
policy, and the user setting up the logging has the
`logs:PutResourcePolicy`, `logs:DescribeResourcePolicies`,
and `logs:DescribeLogGroups` permissions for the log group, then AWS
automatically creates the following policy for it when you begin sending the logs to
CloudWatch Logs.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AWSLogDeliveryWrite20150319",
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "delivery.logs.amazonaws.com"
 ]
 },
 "Action": [
 "logs:CreateLogStream",
 "logs:PutLogEvents"
 ],
 "Resource": [
 "arn:aws:logs:`us-east-1`:`111122223333`:log-group:`my-log-group`:log-stream:*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": [
 "`0123456789`"
 ]
 },
 "ArnLike": {
 "aws:SourceArn": [
 "arn:aws:logs:`us-east-1`:`111122223333`:*"
 ]
 }
 }
 }
 ]
}`

```
