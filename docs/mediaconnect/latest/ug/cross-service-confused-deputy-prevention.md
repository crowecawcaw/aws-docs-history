# Cross-service confused deputy

prevention

The confused deputy problem is a security issue where an entity that doesn't have
permission to perform an action can coerce a more-privileged entity to perform the action.
In AWS, cross-service impersonation can result in the confused deputy problem.
Cross-service impersonation can occur when one service (the _calling
service_) calls another service (the _called service_). The
calling service can be manipulated to use its permissions to act on another customer's
resources in a way it should not otherwise have permission to access. To prevent this, AWS
provides tools that help you protect your data for all services with service principals that
have been given access to resources in your account.

We recommend using the [`aws:SourceArn`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn") of the flow and [`aws:SourceAccount`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount") global condition context keys in resource
policies to limit the permissions that AWS Elemental MediaConnect gives another service to the
resource. Use the flow's `aws:SourceArn` if you want only one resource to be
associated with the cross-service access. Use `aws:SourceAccount` if you want to
allow any resource in that account to be associated with the cross-service use.

The most effective way to protect against the confused deputy problem is to use the
`aws:SourceArn` global condition context key with the full ARN of the flow.
If you don't know the full ARN of the flow or if you are specifying multiple flows, use the
`aws:SourceArn` global context condition key with wildcard characters
(`*`) for the unknown portions of the ARN. For example,
`arn:aws:mediaconnect:*:`111122223333`:*`.

The following example shows how you can use the `aws:SourceArn` and
`aws:SourceAccount` global condition context keys in MediaConnect to prevent
the confused deputy problem.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "mediaconnect.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`111122223333`"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:mediaconnect:`us-west-2`:`111122223333`:flow:`1-ABCDEFGHJxyzMNoP-a1234bc12345`:`flow-name`"
 }
 }
 }
 ]
}`

```
