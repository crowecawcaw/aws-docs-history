# Logs sent to Firehose

**User permissions**

To enable sending logs to Firehose, you must be signed in with the following
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
 "arn:aws:logs:`us-east-1`:`111122223333`:delivery-source:*",
 "arn:aws:logs:`us-east-1`:`111122223333`:delivery-destination:*"
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
 "Sid": "AllowUpdatesToResourcePolicyFH",
 "Effect": "Allow",
 "Action": [
 "firehose:TagDeliveryStream"
 ],
 "Resource": [
 "arn:aws:firehose:`us-east-1`:`111122223333`:deliverystream/*"
 ]
 },
 {
 "Sid": "CreateServiceLinkedRole",
 "Effect": "Allow",
 "Action": [
 "iam:CreateServiceLinkedRole"
 ],
 "Resource": "arn:aws:iam::`111122223333`:role/aws-service-role/delivery.logs.amazonaws.com/AWSServiceRoleForLogDelivery"
 }
 ]
}`

```

**IAM roles used for resource permissions**

Because Firehose does not use resource policies, AWS uses IAM roles when setting
up these logs to be sent to Firehose. AWS creates a service-linked role named
**AWSServiceRoleForLogDelivery**. This
service-linked role includes the following permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "firehose:PutRecord",
 "firehose:PutRecordBatch",
 "firehose:ListTagsForDeliveryStream"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/LogDeliveryEnabled": "true"
 }
 },
 "Effect": "Allow"
 }
 ]
}`

```

This service-linked role grants permission for all Firehose delivery streams that
have the `LogDeliveryEnabled` tag set to `true`. AWS gives
this tag to the destination delivery stream when you set up the logging.

This service-linked role also has a trust policy that allows the
`delivery.logs.amazonaws.com` service principal to assume the needed
service-linked role. That trust policy is as follows:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "delivery.logs.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```
