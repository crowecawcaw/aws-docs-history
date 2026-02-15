# Cross-service confused deputy prevention in HealthImaging

The confused deputy problem is a security issue where an entity that doesn't have permission to
perform an action can coerce a more-privileged entity to perform the action. In AWS, cross-service impersonation
can result in the confused deputy problem. Cross-service impersonation can occur when one service (the _calling service_) calls another service (the _called service_). The calling service can be manipulated to use its permissions
to act on another customer's resources in a way it should not otherwise have permission to access. To prevent this,
AWS provides tools that help you protect your data for all services with service principals that have been given access
to resources in your account.

We recommend using the [`aws:SourceArn`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn") and [`aws:SourceAccount`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount") global condition context keys in your `ImportJobDataAccessRole` IAM role trust relationship policies to limit the permissions that AWS HealthImaging gives another service to your resource. Use `aws:SourceArn` to associate only one resource with cross-service access. Use `aws:SourceAccount` to let any resource in that account be associated with the cross-service use. If you use both global condition context keys, the `aws:SourceAccount` value and the account referenced in the `aws:SourceArn` value must use the same account ID when used in the same policy statement.

The value of `aws:SourceArn` must be the ARN of the affected data store. If you don't know the full ARN of the data store, or if you are specifying multiple data stores, use the `aws:SourceArn` global context condition key with the \* wildcard for the unknown portions of the ARN. For example, you can set `aws:SourceArn` to `arn:aws:medical-imaging:us-west-2:111122223333:datastore/*`.

In the following trust policy example, we use the `aws:SourceArn` and `aws:SourceAccount` condition key to restrict access to the service principal based on the data store's ARN to prevent the confused deputy problem.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "medical-imaging.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "ArnLike": {
 "aws:SourceArn": "arn:aws:medical-imaging:us-east-1:123456789012:datastore/*"
 },
 "StringEquals": {
 "aws:SourceAccount": "123456789012"
 }
 }
 }
 ]
}`

```
