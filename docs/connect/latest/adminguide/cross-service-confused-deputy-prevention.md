# Cross-service confused deputy

prevention in AWS

The confused deputy problem is a security issue where an entity that doesn't have permission
to perform an action can coerce a more-privileged entity to perform the action. In AWS,
cross-service impersonation can result in the confused deputy problem. Cross-service
impersonation can occur when one service (the _calling service_) calls
another service (the _called service_). The calling service can be
manipulated to use its permissions to act on another customer's resources in a way it should not
otherwise have permission to access. To prevent this, AWS provides tools that help you protect
your data for all services with service principals that have been given access to resources in
your account.

We recommend using the [`aws:SourceArn`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn") and [`aws:SourceAccount`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount") global condition context keys in resource policies
to limit the permissions that Amazon Connect gives another service to the resource. If you
use both global condition context keys, the `aws:SourceAccount` value and the account
in the `aws:SourceArn` value must use the same account ID when used in the same
policy statement.

The most effective way to protect against the confused deputy problem is to use the exact
Amazon Resource Name (ARN) of the resource you want to allow. If you don't know the full ARN of
the resource or if you are specifying multiple resources, use the `aws:SourceArn`
global context condition key with wildcards (`*`) for the unknown portions of the
ARN. For example,
`arn:aws:`servicename`::`region-name`::`your
AWS account ID`:*`.

## Amazon Connect Customer Profiles cross-service

confused deputy prevention

The following examples show policies that apply to cases where someone else is set up as
the administrator for Amazon Connect Customer Profiles. Use these policies to prevent the confused deputy
problem.

**Example Amazon Connect Customer Profiles policy to create Customer Profile
domains**

**Example Amazon Connect Customer Profiles policy to create Customer Profiles object
types**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Sid": "ConfusedDeputyPreventionExamplePolicy",
 "Effect": "Allow",
 "Principal": {
 "Service": "profile.amazonaws.com"
 },
 "Action": [
 "kms:GenerateDataKey",
 "kms:CreateGrant",
 "kms:Decrypt"
 ],
 "Resource": [
 "arn:aws:kms:`us-east-1`:`111122223333`:key/`KeyId`"
 ],
 "Condition": {
 "ArnEquals": {
 "aws:SourceArn": "arn:aws:profile:`us-east-1`:`111122223333`:domains/`CustomerProfilesDomainName`/objects/`YourObjectType`"
 },
 "StringEquals": {
 "aws:SourceAccount": "`111122223333`"
 }
 }
 }
}`

```

**Example Amazon Connect Customer Profiles policy to create and update dead-letter
queues**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Allow Customer Profiles to publish messages to your queue",
 "Effect": "Allow",
 "Principal": {
 "Service": "profile.amazonaws.com"
 },
 "Action": "sqs:SendMessage",
 "Resource": "arn:aws:sqs:`us-east-1`:`111122223333`:`YourDeadLetterQueueName`",

 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`111122223333`",
 "aws:SourceArn": "arn:aws:profile:`us-east-1`:`111122223333`:domains/`CustomerProfileDomainName`"
 }
 }
 }
 ]
}`

```

**Example Amazon Connect Customer Profiles policy to protect the Amazon S3 bucket used as part of
the Identity Resolution process**

```
{
    "Sid": "Allow Amazon Connect Customer Profiles to put S3 objects to your bucket",
    "Effect": "Allow",
    "Principal": {
        "Service": "profile.amazonaws.com"
    },
    "Action": "s3:PutObject",
    "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`/*",
    "Condition": {
        "StringEquals": {
            "aws:SourceAccount": "`your AWS account ID`"
        },
        "ArnEquals": {
            "aws:SourceArn": "arn:aws:profile:`your region name`:`your AWS account ID`:domains/*"
        }
    }
}
```

## Amazon Connect Voice ID cross-service confused deputy

prevention

The following Voice ID example shows a resource policy to apply to prevent the confused
deputy problem.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Sid": "ConfusedDeputyPreventionExamplePolicy",
 "Effect": "Allow",
 "Principal": {
 "Service": "voiceid.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "ArnEquals": {
 "aws:SourceArn": "arn:aws:voiceid:`us-east-1`:`111122223333`:domain/`YourVoiceIDDomain`"
 },
 "StringEquals": {
 "aws:SourceAccount": "`111122223333`"
 }
 }
 }
}`

```

## Amazon Connect chat message streaming

cross-service confused deputy prevention

The following Amazon Connect example shows a resource policy to apply to prevent the confused
deputy problem.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "Service":"connect.amazonaws.com"
 },
 "Action":"sns:Publish",
 "Resource":"arn:aws:sns:`us-east-1`:`111122223333`:`TopicName`",
 "Condition":{
 "StringEquals":{
 "aws:SourceAccount":"`111122223333`"
 },
 "ArnEquals":{
 "aws:SourceArn":"arn:aws:connect:`us-east-1`:`111122223333`:instance/`InstanceId`"
 }
 }
 }
 ]
}`

```
