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

We recommend using the [`aws:SourceArn`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn") and [`aws:SourceAccount`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount") global condition context keys in resource
policies to limit the permissions that AWS DataSync gives another service to the resource. If
you use both global condition context keys and the `aws:SourceArn` value contains
the account ID, the `aws:SourceAccount` value and the account in the
`aws:SourceArn` value must use the same account ID when used in the same
policy statement. Use `aws:SourceArn` if you want only one resource to be
associated with the cross-service access. Use `aws:SourceAccount` if you want any
resource in that account to be associated with the cross-service use.

The value of `aws:SourceArn` must include the DataSync location ARN with which DataSync is allowed to assume the IAM role.

The most effective way to protect against the confused deputy problem is to use the
`aws:SourceArn` key with the full ARN of the resource. If you don't know the
full ARN or if you're specifying multiple resources, use wildcard characters
(`*`) for the unknown portions. Here are some examples of how to do this for
DataSync:

- To limit the trust policy to an existing DataSync location, include the full location
  ARN in the policy. DataSync will assume the IAM role only when dealing with that
  particular location.
- When creating an Amazon S3 location for DataSync, you don't know the location's ARN. In
  these scenarios, use the following format for the `aws:SourceArn` key:
  `arn:aws:datasync:`us-east-2`:`123456789012`:*`.
  This format validates the partition (`aws`), account ID, and
  Region.
  The following full example shows how you can use the `aws:SourceArn` and
  `aws:SourceAccount` global condition context keys in a trust policy to
  prevent the confused deputy problem with DataSync.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "datasync.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`123456789012`"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:datasync:`us-east-2`:`123456789012`:*"
 }
 }
 }
 ]
}`

```

For more example policies that show how you can use the `aws:SourceArn` and
`aws:SourceAccount` global condition context keys with DataSync, see the
following topics:

- [Create a trust relationship that allows
  DataSync to access your Amazon S3 bucket](using-identity-based-policies.md#datasync-example1 "using-identity-based-policies.md#datasync-example1")
- [Configure an IAM role to access
  your Amazon S3 bucket](create-s3-location.md#create-role-manually "create-s3-location.md#create-role-manually")
