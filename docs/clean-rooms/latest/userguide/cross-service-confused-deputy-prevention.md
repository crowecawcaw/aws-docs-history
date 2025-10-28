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

We recommend using the [`aws:SourceArn`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn") global condition context keys in resource
policies to limit the permissions that AWS Clean Rooms gives another service to the resource.
Use `aws:SourceArn` if you want only one resource to be associated with the
cross-service access.

The most effective way to protect against the confused deputy problem is to use the
`aws:SourceArn` global condition context key with the full ARN of the
resource. In AWS Clean Rooms, you also have to compare against the `sts:ExternalId`
condition key.

The value of `aws:SourceArn` must be set to the ARN of the membership of the assumed role.

The following example shows how you can use the `aws:SourceArn` global condition context key in AWS Clean Rooms to prevent
the confused deputy problem.

###### Note

The example policy applies to the trust policy of the service role that AWS Clean Rooms uses to
access data and metadata for a configured table.

The value for `<query-runner-membership-id>` needs to
be set to the membership ID of the query runner.

All members of the collaboration can view the configured table matadata so each
membership ARN must be included in the list of membership ARNs.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowIfExternalIdMatches",
 "Effect": "Allow",
 "Principal": {
 "Service": "cleanrooms.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringLike": {
 "sts:ExternalId": "arn:aws:*:`us-east-1`:*:dbuser:*/`<query-runner-membership-id>`*"
 }
 }
 },
 {
 "Sid": "AllowIfSourceArnMatches",
 "Effect": "Allow",
 "Principal": {
 "Service": "cleanrooms.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "ForAnyValue:ArnEquals": {
 "aws:SourceArn": [
 "arn:aws:cleanrooms:`us-east-1`:`111122223333`:membership/`<member-1-membership-id>`",
 "arn:aws:cleanrooms:`us-east-1`:`444455556666`:membership/`<member-2-membership-id>`"
 ]
 }
 }
 }
 ]
}`

```
