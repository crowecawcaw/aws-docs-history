Amazon Monitron is no longer open to new customers. Existing customers can
continue to use the service as normal. For capabilities similar to Amazon
Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron "https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron").

# AWS managed policies for

Amazon Monitron

You can attach AmazonMonitronFullAccess to your IAM entities. This policy
grants _administrative_ permissions that allow access to all
Amazon Monitron resources and operations.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "iam:CreateServiceLinkedRole",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "iam:AWSServiceName": "monitron.amazonaws.com"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "monitron:*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:ListKeys",
 "kms:DescribeKey",
 "kms:ListAliases"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "kms:CreateGrant",
 "Resource": "*",
 "Condition": {
 "StringLike": {
 "kms:ViaService": [
 "monitron.*.amazonaws.com"
 ]
 },
 "Bool": {
 "kms:GrantIsForAWSResource": true
 }
 }
 },
 {
 "Sid": "AWSSSOPermissions",
 "Effect": "Allow",
 "Action": [
 "organizations:DescribeAccount",
 "organizations:DescribeOrganization",
 "ds:DescribeDirectories",
 "ds:DescribeTrusts"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "kinesis:DescribeStream",
 "kinesis:ListStreams"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "logs:DescribeLogGroups",
 "logs:DescribeLogStreams",
 "logs:GetLogEvents",
 "logs:CreateLogGroup"
 ],
 "Resource": "arn:aws:logs:*:*:log-group:/aws/monitron/*"
 }
 ]
}`

```
