# Cross-service confused deputy prevention

The confused deputy problem is a security issue where an entity that doesn't have
permission to perform an action can coerce a more-privileged entity to perform the action.
In AWS, cross-service impersonation can result in the confused deputy problem.
Cross-service impersonation can occur when one service (the _calling
service_) calls another service (the _called service_). The
calling service can be manipulated to use its permissions to act on another customer's
resources in a way that it should not otherwise have permission to access. To prevent this,
AWS provides tools that help you protect your data for all services with service
principals that have been given access to resources in your account. For a detailed
description of this problem, see [the confused deputy problem](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md") in
the _IAM User Guide_.

We recommend using the [`aws:SourceArn`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn") and [`aws:SourceAccount`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount") global condition context keys in resource
policies to limit the permissions that AWS Transfer Family has for the resource. If you use both global
condition context keys, the `aws:SourceAccount` value and the account in the
`aws:SourceArn` value must use the same account ID when used in the same
policy statement.

The most effective way to protect against the confused deputy problem is to use the exact
Amazon Resource Name (ARN) of the resource you want to allow. If you are specifying multiple
resources, use the `aws:SourceArn` global context condition key with wildcard
characters (`*`) for the unknown portions of the ARN. For example,
`arn:aws:transfer::`region`::`account-id`:server/*`.

AWS Transfer Family uses the following types of roles:

- **User role** – Allows service-managed users to access the
  necessary Transfer Family resources. AWS Transfer Family assumes this role in the context of a Transfer Family user
  ARN.
- **Access role** – Provides access to only the Amazon S3 files that are being
  transferred. For inbound AS2 transfers, the access role uses the Amazon Resource Name (ARN) for
  the agreement. For outbound AS2 transfers, the access role uses the ARN for the connector.
- **Invocation role** – For use with Amazon API Gateway as the server's
  custom identity provider. Transfer Family assumes this role in the context of a Transfer Family server
  ARN.
- **Logging role** – Used to log entries into
  Amazon CloudWatch. Transfer Family uses this role to log success and failure
  details along with information about file transfers. Transfer Family assumes this role in the
  context of a Transfer Family server ARN. For outbound AS2 transfers, the logging role uses the connector
  ARN.
- **Execution role** – Allows a Transfer Family user to call and launch
  workflows. Transfer Family assumes this role in the context of a Transfer Family workflow ARN.
  For more information, see [Policies and permissions in
  IAM](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") in the _IAM User Guide_.

###### Note

In the following examples, replace each `user input
 placeholder` with your own information.

###### Note

In our examples, we use both `ArnLike` and `ArnEquals`.
They are functionally identical, and therefore you may use either when you construct your policies.
Transfer Family documentation uses `ArnLike` when the condition contains a wildcard character, and
`ArnEquals` to indicate an exact match condition.

## AWS Transfer Family user role cross-service confused

deputy prevention

The following example policy allows any user of any server in the account to assume
the role.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "",
 "Effect": "Allow",
 "Principal": {
 "Service": "transfer.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`123456789012`"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:transfer:`us-east-1`:`123456789012`:user/*"
 }
 }
 }
 ]
}`

```

The following example policy allows any user of a specific server to assume the
role.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "",
 "Effect": "Allow",
 "Principal": {
 "Service": "transfer.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "123456789012"
 },
 "ArnEquals": {
 "aws:SourceArn": "arn:aws:transfer:us-east-1:123456789012:user/`server-id`/*"
 }
 }
 }
 ]
}`

```

The following example policy allows a specific user of a specific server to assume the
role.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "",
 "Effect": "Allow",
 "Principal": {
 "Service": "transfer.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "ArnLike": {
 "aws:SourceArn": "arn:aws:transfer:us-east-1:123456789012:user/`server-id`/`user-name`"
 }
 }
 }
 ]
}`

```

## AWS Transfer Family workflow role cross-service

confused deputy prevention

The following example policy allows any workflow in the account to assume the role.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "",
 "Effect": "Allow",
 "Principal": {
 "Service": "transfer.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`111122223333`"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:transfer:`us-west-2`:`111122223333`:workflow/*"
 }
 }
 }
 ]
}`

```

The following example policy allows a specific workflow to assume the role.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "",
 "Effect": "Allow",
 "Principal": {
 "Service": "transfer.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "ArnLike": {
 "aws:SourceArn": "arn:aws:transfer:`us-west-2`:`111122223333`:workflow/`workflow-id`"
 }
 }
 }
 ]
}`

```

## AWS Transfer Family connector role cross-service

confused deputy prevention

The following example policy allows any connector in the account to assume the
role.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "",
 "Effect": "Allow",
 "Principal": {
 "Service": "transfer.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`123456789012`"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:transfer:`us-east-1`:`123456789012`:connector/*"
 }
 }
 }
 ]
}`

```

The following example policy allows a specific connector to assume the role.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "",
 "Effect": "Allow",
 "Principal": {
 "Service": "transfer.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "ArnLike": {
 "aws:SourceArn": "arn:aws:transfer:`us-east-1`:`123456789012`:connector/`connector-id`"
 }
 }
 }
 ]
}`

```

## AWS Transfer Family logging and invocation role

cross-service confused deputy prevention

###### Note

The following examples can be used in both logging and invocation roles.

In these examples, you can remove the ARN details for a workflow if your server
doesn't have any workflows attached to it.

The following example logging/invocation policy allows any server (and workflow) in the account to assume the role.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowAllServersWithWorkflowAttached",
 "Effect": "Allow",
 "Principal": {
 "Service": "transfer.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`111122223333`"
 },
 "ArnLike": {
 "aws:SourceArn": [
 "arn:aws:transfer:`us-west-2`:`111122223333`:server/*",
 "arn:aws:transfer:`us-west-2`:`111122223333`:workflow/*"
 ]
 }
 }
 }
 ]
}`

```

The following example logging/invocation policy allows a specific server (and workflow) to assume the role.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowSpecificServerWithWorkflowAttached",
 "Effect": "Allow",
 "Principal": {
 "Service": "transfer.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`111122223333`"
 },
 "ArnEquals": {
 "aws:SourceArn": [
 "arn:aws:transfer:`us-west-2`:`111122223333`:server/`server-id`",
 "arn:aws:transfer:`us-west-2`:`111122223333`:workflow/`workflow-id`"
 ]
 }
 }
 }
 ]
}`

```
