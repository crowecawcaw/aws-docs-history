# Accessing customization-related messages in Amazon CloudWatch Logs

You can store information about the creation of your customizations in [Amazon CloudWatch Logs](../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md").

You can authorize your Amazon Q Developer administrator to view those logs with the following
permission set.

To learn more about the permissions required to delivery logs to multiple resources,
see [Logging that requires additional permissions [V2]](../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-vended-logs-permissions-V2 "../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-vended-logs-permissions-V2") in the _Amazon CloudWatch Logs
User Guide_.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowLogDeliveryActions",
 "Effect": "Allow",
 "Action": [
 "logs:PutDeliverySource",
 "logs:GetDeliverySource",
 "logs:DeleteDeliverySource",
 "logs:DescribeDeliverySources",
 "logs:PutDeliveryDestination",
 "logs:GetDeliveryDestination",
 "logs:DeleteDeliveryDestination",
 "logs:DescribeDeliveryDestinations",
 "logs:CreateDelivery",
 "logs:GetDelivery",
 "logs:DeleteDelivery",
 "logs:DescribeDeliveries",
 "firehose:ListDeliveryStreams",
 "firehose:DescribeDeliveryStream",
 "s3:ListAllMyBuckets",
 "s3:ListBucket",
 "s3:GetBucketLocation"
 ],
 "Resource": [
 "arn:aws:logs:us-east-1:`111122223333`:log-group:*",
 "arn:aws:firehose:us-east-1:`111122223333`:deliverystream/*",
 "arn:aws:s3:::*"
 ]
 }
 ]
}`

```
