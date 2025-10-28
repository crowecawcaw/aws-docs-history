# AWS

managed policy: AmazonSageMakerClusterInstanceRolePolicy

This policy grants permissions commonly needed to use Amazon SageMaker HyperPod.

**Permissions details**

This AWS managed policy includes the following permissions.

- `cloudwatch` – Allows principals to post Amazon CloudWatch metrics.
- `logs` – Allows principals to publish CloudWatch log streams.
- `s3` – Allows principals to list and retrieve lifecycle script files
  from an Amazon S3 bucket in your account. These buckets are limited to those whose name starts
  with "sagemaker-".
- `ssmmessages` – Allows principals to open a connection to
  AWS Systems Manager.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement" : [
 {
 "Sid" : "CloudwatchLogStreamPublishPermissions",
 "Effect" : "Allow",
 "Action" : [
 "logs:PutLogEvents",
 "logs:CreateLogStream",
 "logs:DescribeLogStreams"
 ],
 "Resource" : [
 "arn:aws:logs:*:*:log-group:/aws/sagemaker/Clusters/*:log-stream:*"
 ]
 },
 {
 "Sid" : "CloudwatchLogGroupCreationPermissions",
 "Effect" : "Allow",
 "Action" : [
 "logs:CreateLogGroup"
 ],
 "Resource" : [
 "arn:aws:logs:*:*:log-group:/aws/sagemaker/Clusters/*"
 ]
 },
 {
 "Sid" : "CloudwatchPutMetricDataAccess",
 "Effect" : "Allow",
 "Action" : [
 "cloudwatch:PutMetricData"
 ],
 "Resource" : [
 "*"
 ],
 "Condition" : {
 "StringEquals" : {
 "cloudwatch:namespace" : "/aws/sagemaker/Clusters"
 }
 }
 },
 {
 "Sid" : "DataRetrievalFromS3BucketPermissions",
 "Effect" : "Allow",
 "Action" : [
 "s3:ListBucket",
 "s3:GetObject"
 ],
 "Resource" : [
 "arn:aws:s3:::sagemaker-*"
 ],
 "Condition" : {
 "StringEquals" : {
 "aws:ResourceAccount" : "${aws:PrincipalAccount}"
 }
 }
 },
 {
 "Sid" : "SSMConnectivityPermissions",
 "Effect" : "Allow",
 "Action" : [
 "ssmmessages:CreateControlChannel",
 "ssmmessages:CreateDataChannel",
 "ssmmessages:OpenControlChannel",
 "ssmmessages:OpenDataChannel"
 ],
 "Resource" : "*"
 }
 ]
}`

```
