# Cross-service confused deputy

prevention

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
to limit the permissions that AWS Lake Formation gives another service to the resource. If
you use both global condition context keys, the `aws:SourceAccount` value and the
account in the `aws:SourceArn` value must use the same account ID when used in the
same policy statement.

Currently, Lake Formation only supports `aws:SourceArn` in the following format:

```
arn:aws:lakeformation:`aws-region`:`account-id`:`*`
```

The following example shows how you can use the `aws:SourceArn` and
`aws:SourceAccount` global condition context keys in Lake Formation to prevent the confused
deputy problem.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ConfusedDeputyPreventionExamplePolicy",
 "Effect": "Allow",
 "Principal": {
 "Service": "lakeformation.amazonaws.com"
 },
 "Action": [
 "sts:AssumeRole"
 ],
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`123456789012`"
 },
 "ArnEquals": {
 "aws:SourceArn": "arn:aws:lakeformation:`aws-region`:`123456789012`:*"
 }
 }
 }
 ]
}`

```
