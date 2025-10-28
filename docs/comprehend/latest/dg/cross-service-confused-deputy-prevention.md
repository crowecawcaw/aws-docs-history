# Cross-service confused deputy prevention

The confused deputy problem is a security issue where an entity that doesn't have
permission to perform an action can coerce a more-privileged entity to perform the action.
In AWS, cross-service impersonation can result in the confused deputy problem.
Cross-service impersonation can occur when one service (the _calling
service_) calls another service (the _called service_). The
calling service can be manipulated to use its permissions to act on another customer's
resources in a way it should not otherwise have permission to access. To prevent this, AWS
provides tools that help you protect your data for all services with service principals that
have been given access to resources in your account.

We recommend using the [`aws:SourceArn`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn") and [`aws:SourceAccount`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount") global condition context keys in resource
policies to limit the permissions that Amazon Comprehend gives another service to the
resource. If you use both global condition context keys, the `aws:SourceAccount`
value and the account in the `aws:SourceArn` value must use the same account ID
when used in the same policy statement.

The most effective way to protect against the confused deputy problem is to use the
`aws:SourceArn` global condition context key with the full ARN of the
resource. If you don't know the full ARN of the resource or if you are specifying multiple
resources, use the `aws:SourceArn` global context condition key with wildcards
(`*`) for the unknown portions of the ARN. For example,
`arn:aws:`servicename`::`123456789012`:*`.

## Using source account

The following example shows how you can use the `aws:SourceAccount` global condition context key in
Amazon Comprehend.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Sid": "ConfusedDeputyPreventionExamplePolicy",
 "Effect": "Allow",
 "Principal": {
 "Service": "comprehend.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount":"`111122223333`"
 }
 }
 }
}`

```

## Trust policy for endpoints of encrypted models

You need to create a trust policy to create or update an endpoint for an encrypted model. Set the
`aws:SourceAccount` value to your account ID. If you use the `ArnEquals` condition, set
the `aws:SourceArn` value to the ARN of the endpoint.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "",
 "Effect": "Allow",
 "Principal": {
 "Service": "comprehend.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`111122223333`"
 },
 "ArnEquals": {
 "aws:SourceArn": "arn:aws:comprehend:`us-west-2:111122223333`:document-classifier-endpoint/`endpoint-name`"
 }
 }
 }
 ]
}`

```

## Create custom model

You need to create a trust policy to create a custom model. Set the `aws:SourceAccount` value to
your account ID. If you use the `ArnEquals` condition, set the `aws:SourceArn` value to the
ARN of the custom model version.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "",
 "Effect": "Allow",
 "Principal": {
 "Service": "comprehend.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`111122223333`"
 },
 "ArnEquals": {
 "aws:SourceArn": "arn:aws:comprehend:`us-west-2:111122223333`:document-classifier/smallest-classifier-test/version/`version-name`"
 }
 }
 }
 ]
}`

```
