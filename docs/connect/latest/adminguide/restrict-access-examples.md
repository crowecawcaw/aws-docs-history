# Restrict AWS resources that can be associated with Connect Customer

Each Connect Customer instance is associated with an IAM [service-linked role](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role") when the instance is created. Connect Customer can integrate with other
AWS services for use cases such as call recording storage (Amazon S3 bucket), natural language
bots (Amazon Lex bots), and data streaming (Amazon Kinesis Data Streams). Connect Customer assumes the service-linked role to
interact with these other services. The policy is first added to the service-linked role as
part of corresponding APIs on the Connect Customer service (that are in turn called by the AWS admin
console). For example, if you want to use a certain Amazon S3 bucket with your Connect Customer instance,
the bucket must be passed to the [AssociateInstanceStorageConfig](../APIReference/API_AssociateInstanceStorageConfig.md "../APIReference/API_AssociateInstanceStorageConfig.md") API.

For the set of IAM actions defined by Connect Customer, see [Actions defined by Connect Customer](../../../service-authorization/latest/reference/list_amazonconnect.md#amazonconnect-actions-as-permissions "../../../service-authorization/latest/reference/list_amazonconnect.md#amazonconnect-actions-as-permissions").

Following are some examples of how to restrict access to other resources that might be
associated with a Connect Customer instance. They should be applied to the User or Role that is
interacting with Connect Customer APIs or the Connect Customer console.

###### Note

A policy with an explicit `Deny` would override the `Allow`
policy in these examples.

For more information about what resources, condition keys, and dependent APIs you can
use to restrict access, see [Actions, resources,
and condition keys for Connect Customer](../../../service-authorization/latest/reference/list_amazonconnect.md "../../../service-authorization/latest/reference/list_amazonconnect.md").

## Example 1: Restrict which Amazon S3 buckets can be associated with a Connect Customer instance

This example allows an IAM principal to associate an Amazon S3 bucket for call
recordings for the given Connect Customer instance ARN, and a specific Amazon S3 bucket named
`my-connect-recording-bucket`. The `AttachRolePolicy` and
`PutRolePolicy` actions are scoped to the Connect Customer service-linked role (a
wildcard is used in this example, but you can provide the role ARN for the instance if
needed).

###### Note

To use an AWS KMS key to encrypt recordings in this bucket, an additional policy is
needed.

## Example 2: Restrict which AWS Lambda functions can be associated with a Connect Customer instance

AWS Lambda functions are associated with a Connect Customer instance, but the Connect Customer
service-linked role is not used to invoke them, and so is not modified. Instead, a
policy is added to the function through the `lambda:AddPermission` API that
allows the given Connect Customer instance to invoke the function.

To restrict which functions can be associated with a Connect Customer instance, you specify the
Lambda function ARN that a user can use to invoke `lambda:AddPermission`:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "connect:AssociateLambdaFunction",
 "lambda:AddPermission"
 ],
 "Resource": [
 "arn:aws:connect:`us-east-1`:`111122223333`:instance/`instance-id`",
 "arn:aws:lambda:*:*:function:`my-function`"
 ]
 }
 ]
}`

```

## Example 3: Restrict which Amazon Kinesis Data Streams can be associated with a Connect Customer instance

This example follows a similar model to the Amazon S3 example. It restricts which specific
Kinesis Data Streams might be associated with a given Connect Customer instance for delivering contact
records.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "connect:UpdateInstanceStorageConfig",
 "connect:AssociateInstanceStorageConfig"
 ],
 "Resource": "arn:aws:connect:`us-east-1`:`111122223333`:instance/`instance-id`",
 "Condition": {
 "StringEquals": {
 "connect:StorageResourceType": "CONTACT_TRACE_RECORDS"
 }
 }
 },
 {
 "Sid": "VisualEditor1",
 "Effect": "Allow",
 "Action": [
 "kinesis:DescribeStream",
 "iam:PutRolePolicy"
 ],
 "Resource": [
 "arn:aws:iam::`111122223333`:role/aws-service-role/connect.amazonaws.com/*",
 "arn:aws:kinesis:*:`111122223333`:stream/`stream-name`"
 ]
 },
 {
 "Sid": "VisualEditor2",
 "Effect": "Allow",
 "Action": "kinesis:ListStreams",
 "Resource": "*"
 }
 ]
}`

```
