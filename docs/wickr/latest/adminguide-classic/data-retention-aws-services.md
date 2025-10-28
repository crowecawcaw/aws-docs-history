This guide documents the classic version of the AWS Wickr administration console, released before March
13, 2025. For documentation on the new AWS Wickr administration console, see [Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# IAM policy to use data retention with

AWS services

If you plan to use other AWS services with the Wickr data retention bot, you must
ensure the host has the appropriate AWS Identity and Access Management (IAM) role and policy to access them.
You can configure the data retention bot to use Secrets Manager, Amazon S3, CloudWatch, Amazon SNS, and AWS KMS. The
following IAM policy allows access to specific actions for these services.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "s3:PutObject",
 "secretsmanager:GetSecretValue",
 "sns:Publish",
 "cloudwatch:PutMetricData",
 "kms:GenerateDataKey"
 ],
 "Resource": "*"
 }
 ]
}`

```

You can create an IAM policy that is more strict by identifying the specific objects
for each service that you want to allow the containers on your host to access. Remove
the actions for the AWS services that you do not intend to use. For example, if you
intent to use only an Amazon S3 bucket, then use the following policy, which removes the
`secretsmanager:GetSecretValue`, `sns:Publish`,
`kms:GenerateDataKey`, and `cloudwatch:PutMetricData`
actions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": "s3:PutObject",
 "Resource": "*"
 }
 ]
}`

```

If you are using an Amazon Elastic Compute Cloud (Amazon EC2) instance to host your data retention bot, create
an IAM role using the Amazon EC2 common case and assign a policy using the policy
definition from above.
