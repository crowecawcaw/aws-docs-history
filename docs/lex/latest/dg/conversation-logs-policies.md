End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# IAM Policies for Conversation

Logs

Depending on the type of logging that you select, Amazon Lex requires
permission to use Amazon CloudWatch Logs and Amazon Simple Storage Service (S3) buckets to store your logs. You
must create AWS Identity and Access Management roles and permissions to enable Amazon Lex to access these
resources.

## Creating an IAM Role and

Policies for Conversation Logs

To enable conversation logs, you must grant write permission for CloudWatch Logs
and Amazon S3. If you enable object encryption for your S3 objects, you need to
grant access permission to the AWS KMS keys used to encrypt the objects.

You can use the IAM AWS Management Console, the IAM API, or the AWS Command Line Interface to
create the role and policies. These instructions use the AWS CLI to create the
role and policies. For information about creating policies with the console,
see [Creating policies on the JSON tab](../../../IAM/latest/UserGuide/access_policies_create-console.md#access_policies_create-json-editor "../../../IAM/latest/UserGuide/access_policies_create-console.md#access_policies_create-json-editor") in the _AWS Identity
and Access Management User Guide_.

###### Note

The following code is formatted for Linux and MacOS. For Windows,
replace the Linux line continuation character (\) with a caret (^).

###### To create an IAM role for conversation logs

1. Create a document in the current directory called
   `LexConversationLogsAssumeRolePolicyDocument.json`,
   add the following code to it, and save it. This policy document adds Amazon Lex
   as a trusted entity to the role. This allows Lex to assume the role to
   deliver logs to the resources configured for conversation logs.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "lex.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

2. In the AWS CLI, run the following command to create the IAM role for
   conversation logs.

```
aws iam create-role \
    --role-name `role-name` \
    --assume-role-policy-document file://LexConversationLogsAssumeRolePolicyDocument.json

```

Next, create and attach a policy to the role that enables Amazon Lex to
write to CloudWatch Logs.

###### To create an IAM policy for logging conversation text to

CloudWatch Logs

1. Create a document in the current directory called
   `LexConversationLogsCloudWatchLogsPolicy.json`, add
   the following IAM policy to it, and save it.
2. In the AWS CLI, create the IAM policy that grants write permission to
   the CloudWatch Logs log group.

```
aws iam create-policy \
    --policy-name `cloudwatch-policy-name` \
    --policy-document file://LexConversationLogsCloudWatchLogsPolicy.json

```

3. Attach the policy to the IAM role that you created for conversation
   logs.

```
aws iam attach-role-policy \
    --policy-arn arn:aws:iam::`account-id`:policy/`cloudwatch-policy-name` \
    --role-name `role-name`

```

If you are logging audio to an S3 bucket, create a policy that enables
Amazon Lex to write to the bucket.

###### To create an IAM policy for audio logging to an S3 bucket

1. Create a document in the current directory called
   `LexConversationLogsS3Policy.json`, add the
   following policy to it, and save it.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:PutObject"
 ],
 "Resource": "arn:aws:s3:::`bucket-name`/*"
 }
 ]
}`

```

2. In the AWS CLI, create the IAM policy that grants write permission to
   your S3 bucket.

```
aws iam create-policy \
    --policy-name `s3-policy-name` \
    --policy-document file://LexConversationLogsS3Policy.json
```

3. Attach the policy to the role that you created for conversation
   logs.

```
aws iam attach-role-policy \
    --policy-arn arn:aws:iam::`account-id`:policy/`s3-policy-name` \
    --role-name `role-name`
```

## Granting Permission to Pass an

IAM Role

When you use the console, the AWS Command Line Interface, or an AWS SDK to specify an
IAM role to use for conversation logs, the user specifying the
conversation logs IAM role must have permission to pass the role to Amazon Lex.
To allow the user to pass the role to Amazon Lex, you must grant
`PassRole` permission to the user, role, or group.

The following policy defines the permission to grant to the user, role,
or group. You can use the `iam:AssociatedResourceArn` and
`iam:PassedToService` condition keys to limit the scope of the
permission. For more information, see [Granting a User
Permissions to Pass a Role to an AWS Service](../../../IAM/latest/UserGuide/id_roles_use_passrole.md "../../../IAM/latest/UserGuide/id_roles_use_passrole.md") and [IAM and AWS STS Condition Context Keys](../../../IAM/latest/UserGuide/reference_policies_iam-condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_iam-condition-keys.md") in the _AWS Identity and Access Management
User Guide_.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": "arn:aws:iam::`111122223333`:role/`role-name`",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "lex.amazonaws.com"
 },
 "StringLike": {
 "iam:AssociatedResourceARN": "arn:aws:lex:`region`:`account-id`:bot:`bot-name`:`bot-alias`"
 }
 }
 }
 ]
}`

```
