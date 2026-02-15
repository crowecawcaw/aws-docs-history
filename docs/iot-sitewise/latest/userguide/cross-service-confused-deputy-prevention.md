# Cross-service confused deputy

prevention in AWS IoT SiteWise

The confused deputy problem is a security issue where an entity that doesn't have
permission to perform an action can coerce a more-privileged entity to perform the action.
In AWS, cross-service impersonation can result in the confused deputy problem.
Cross-service impersonation can occur when one service (the _calling
service_) calls another service (the _called service_). The
calling service can be manipulated to use its permissions to act on another customer's
resources in a way it shouldn't otherwise have permission to access. To prevent this, AWS
provides tools that help you protect your data for all services with service principals that
have been given access to resources in your account.

We recommend using the [`aws:SourceArn`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn") and [`aws:SourceAccount`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount") global condition context keys in resource
policies to limit the permissions that AWS IoT SiteWise gives another service to the
resource. If the `aws:SourceArn` value doesn't contain the account ID, such as an
Amazon S3 bucket Amazon Resource Name (ARN), you must use both global condition context keys to
limit permissions. If you use both global condition context keys and the
`aws:SourceArn` value contains the account ID, the
`aws:SourceAccount` value and the account in the `aws:SourceArn`
value must use the same account ID when used in the same policy statement.

- Use
  `aws:SourceArn` if you want only one resource to be associated with the
  cross-service access.
- Use `aws:SourceAccount` if you want to allow any resource
  in that account to be associated with the cross-service use.
  The value of `aws:SourceArn` must be the AWS IoT SiteWise customer resource that is
  associated with the `sts:AssumeRole` request.

The most effective way to protect against the confused deputy problem is to use the
`aws:SourceArn` global condition context key with the full ARN of the
resource. If you don't know the full ARN of the resource or if you're specifying multiple
resources, use the `aws:SourceArn` global context condition key with wildcards
(`*`) for the unknown portions of the ARN. For example,
`arn:aws:`servicename`:*:`123456789012`:*`.

###### Example– Confused Deputy Prevention

The following example shows how you can use the `aws:SourceArn` and
`aws:SourceAccount` global condition context keys in AWS IoT SiteWise to prevent
the confused deputy problem.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Sid": "ConfusedDeputyPreventionExamplePolicy",
 "Effect": "Allow",
 "Principal": {
 "Service": "`iotsitewise`.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "ArnLike": {
 "aws:SourceArn": "arn:aws:`iotsitewise`:*:`123456789012`:*"
 },
 "StringEquals": {
 "aws:SourceAccount": "`123456789012`"
 }
 }
 }
}`

```
