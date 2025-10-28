# Manage SageMaker AI resources with AWS Batch

This policy allows AWS Batch to manage SageMaker AI resources.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "batch:*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:CreateServiceLinkedRole"
 ],
 "Resource": "arn:aws:iam::*:role/*AWSServiceRoleForAWSBatchWithSagemaker",
 "Condition": {
 "StringEquals": {
 "iam:AWSServiceName": "sagemaker-queuing.batch.amazonaws.com"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": [
 "sagemaker.amazonaws.com"
 ]
 }
 }
 }
 ]
}`

```
