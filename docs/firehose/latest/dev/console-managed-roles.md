# Manage IAM roles through Amazon Data Firehose console

Amazon Data Firehose is a fully managed service that delivers real-time streaming data to
destinations. You can also configure Firehose to transform and convert the format of your data
before delivery. To use these features, you must first provide IAM roles to grant
permissions to Firehose when you create or edit a Firehose stream. Firehose uses this IAM role for all
the permissions that the Firehose stream needs.

For example, consider a scenario where you create a Firehose stream that delivers data to Amazon S3,
and this Firehose stream has Transform source records with AWS Lambda feature enabled. In this
case, you must provide IAM roles to grant Firehose permissions to access the S3 bucket and
invoke the Lambda function, as shown in the following.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Sid": "lambdaProcessing",
 "Effect": "Allow",
 "Action": ["lambda:InvokeFunction", "lambda:GetFunctionConfiguration"],
 "Resource": "`arn:aws:`lambda:`us-east-1`:`123456789012`:function:`<lambda function name>`:`<lambda function version>`"
 }, {
 "Sid": "s3Permissions",
 "Effect": "Allow",
 "Action": ["s3:AbortMultipartUpload", "s3:GetBucketLocation", "s3:GetObject", "s3:ListBucket", "s3:ListBucketMultipartUploads", "s3:PutObject"],
 "Resource": ["`arn:aws:`s3:::`<bucket name>`", "`arn:aws:`s3:::`<bucket name>`/*"]
 }]
}`

```

Firehose console allows you to choose how you want to provide these roles. You can choose
from one of the following options.

- [Choose an existing IAM role](console-managed-iam-existing-roles.md "console-managed-iam-existing-roles.md")
- [Create a new IAM role from console](console-managed-iam-create-new-roles.md "console-managed-iam-create-new-roles.md")
