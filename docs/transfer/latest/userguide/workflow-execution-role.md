# IAM policies for workflows

When you add a workflow to a server, you must select an execution role. The server
uses this role when it executes the workflow. If the role does not have the proper
permissions, AWS Transfer Family cannot run the workflow.

This section describes one possible set of AWS Identity and Access Management (IAM) permissions that you can
use to execute a workflow. Other examples are described later in this topic.

###### Note

If your Amazon S3 files have tags, you need to add one or two permissions to your IAM policy.

- Add `s3:GetObjectTagging` for an Amazon S3 file that isn't versioned.
- Add `s3:GetObjectVersionTagging` for an Amazon S3 file that is versioned.

###### To create an execution role for your workflow

1. Create a new IAM role, and add the AWS managed policy
   `AWSTransferFullAccess` to the role. For more information about
   creating a new IAM role, see [Create an IAM role and policy](requirements-roles.md "requirements-roles.md").
2. Create another policy with the following permissions, and attach it to your
   role. Replace each `user input
placeholder` with your own information.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ConsoleAccess",
 "Effect": "Allow",
 "Action": "s3:GetBucketLocation",
 "Resource": "*"
 },
 {
 "Sid": "ListObjectsInBucket",
 "Effect": "Allow",
 "Action": "s3:ListBucket",
 "Resource": [
 "arn:aws:s3:::amzn-s3-demo-bucket"
 ]
 },
 {
 "Sid": "AllObjectActions",
 "Effect": "Allow",
 "Action": "s3:*Object",
 "Resource": [
 "arn:aws:s3:::amzn-s3-demo-bucket/*"
 ]
 },
 {
 "Sid": "GetObjectVersion",
 "Effect": "Allow",
 "Action": "s3:GetObjectVersion",
 "Resource": [
 "arn:aws:s3:::amzn-s3-demo-bucket/*"
 ]
 },
 {
 "Sid": "Custom",
 "Effect": "Allow",
 "Action": [
 "lambda:InvokeFunction"
 ],
 "Resource": [
 "arn:aws:lambda:`us-east-1`:`123456789012`:function:`function-name`"
 ]
 },
 {
 "Sid": "Tag",
 "Effect": "Allow",
 "Action": [
 "s3:PutObjectTagging",
 "s3:PutObjectVersionTagging"
 ],
 "Resource": [
 "arn:aws:s3:::amzn-s3-demo-bucket/*"
 ]
 }
 ]
}`

```

3. Save this role and specify it as the execution role when you add a workflow to
   a server.

###### Note

When you're constructing IAM roles, AWS recommends that you restrict
access to your resources as much as is possible for your workflow.

## Workflow trust relationships

Workflow execution roles also require a trust relationship with
`transfer.amazonaws.com`. To establish a trust relationship for
AWS Transfer Family, see [To establish a trust relationship](requirements-roles.md#establish-trust-transfer "requirements-roles.md#establish-trust-transfer").

While you're establishing your trust relationship, you can also take steps to
avoid the _confused deputy_ problem. For a description of this
problem, as well as examples of how to avoid it, see [Cross-service confused deputy prevention](confused-deputy.md "confused-deputy.md").

## Example execution role: Decrypt,

copy, and tag

If you have workflows that include tagging, copying, and decrypt steps, you can
use the following IAM policy. Replace each `user input
 placeholder` with your own information.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "CopyRead",
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:GetObjectTagging",
 "s3:GetObjectVersionTagging"
 ],
 "Resource": "arn:aws:s3:::`amzn-s3-demo-source-bucket`/*"
 },
 {
 "Sid": "CopyWrite",
 "Effect": "Allow",
 "Action": [
 "s3:PutObject",
 "s3:PutObjectTagging"
 ],
 "Resource": "arn:aws:s3:::`amzn-s3-demo-destination-bucket`/*"
 },
 {
 "Sid": "CopyList",
 "Effect": "Allow",
 "Action": "s3:ListBucket",
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-source-bucket`",
 "arn:aws:s3:::`amzn-s3-demo-destination-bucket`"
 ]
 },
 {
 "Sid": "Tag",
 "Effect": "Allow",
 "Action": [
 "s3:PutObjectTagging",
 "s3:PutObjectVersionTagging"
 ],
 "Resource": "arn:aws:s3:::`amzn-s3-demo-destination-bucket`/*",
 "Condition": {
 "StringEquals": {
 "s3:RequestObjectTag/Archive": "yes"
 }
 }
 },
 {
 "Sid": "ListBucket",
 "Effect": "Allow",
 "Action": "s3:ListBucket",
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-destination-bucket`"
 ]
 },
 {
 "Sid": "HomeDirObjectAccess",
 "Effect": "Allow",
 "Action": [
 "s3:PutObject",
 "s3:GetObject",
 "s3:DeleteObjectVersion",
 "s3:DeleteObject",
 "s3:GetObjectVersion"
 ],
 "Resource": "arn:aws:s3:::`amzn-s3-demo-destination-bucket`/*"
 },
 {
 "Sid": "Decrypt",
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetSecretValue"
 ],
 "Resource": "arn:aws:secretsmanager:`us-east-1`:`123456789012`:secret:aws/transfer/*"
 }
 ]
}`

```

## Example execution role: Run

function and delete

In this example, you have a workflow that invokes an AWS Lambda function. If the
workflow deletes the uploaded file and has an exception handler step to act upon a
failed workflow execution in the previous step, use the following IAM policy.
Replace each `user input placeholder` with
your own information.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Delete",
 "Effect": "Allow",
 "Action": [
 "s3:DeleteObject",
 "s3:DeleteObjectVersion"
 ],
 "Resource": "arn:aws:s3:::`bucket-name`"
 },
 {
 "Sid": "Custom",
 "Effect": "Allow",
 "Action": [
 "lambda:InvokeFunction"
 ],
 "Resource": [
 "arn:aws:lambda:`us-east-1`:`123456789012`:function:`function-name`"
 ]
 }
 ]
}`

```
