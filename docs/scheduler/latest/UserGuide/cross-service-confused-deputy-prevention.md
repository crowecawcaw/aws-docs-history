# Confused deputy prevention in EventBridge Scheduler

The confused deputy problem is a security issue where an entity that doesn't have
permission to perform an action can coerce a more-privileged entity to perform the action.
In AWS, cross-service impersonation can result in the confused deputy problem.
Cross-service impersonation can occur when one service (the _calling
service_) calls another service (the _called service_). The
calling service can be manipulated to use its permissions to act on another customer's
resources in a way it should not otherwise have permission to access. To prevent this, AWS
provides tools that help you protect your data for all services with service principals that
have been given access to resources in your account.

We recommend using the [`aws:SourceArn`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn") and [`aws:SourceAccount`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount") global condition context keys in your schedule execution role
to limit the permissions that EventBridge Scheduler gives another service to access the
resource. Use `aws:SourceArn` if you want only one resource to be associated with
the cross-service access. Use `aws:SourceAccount` if you want to allow any
resource in that account to be associated with the cross-service use.

The most effective way to protect against the confused deputy problem is to use the
`aws:SourceArn` global condition context key with the full ARN of the
resource. The following condition is scoped to an individual schedule group:
`arn:aws:scheduler:*:`123456789012`:schedule-group/`your-schedule-group``

If you don't know the full ARN of the resource or if you are specifying multiple
resources, use the `aws:SourceArn` global context condition key with wildcard
characters (`*`) for the unknown portions of the ARN. For example:
`arn:aws:scheduler:*:`123456789012`:schedule-group/*`.

The value of `aws:SourceArn` must be your EventBridge Scheduler schedule group ARN to which you want to scope this condition.

###### Important

Do not scope the `aws:SourceArn` statement to a specific schedule or a schedule name prefix.
The ARN you specify must be a schedule group.

The following example shows how you can use the `aws:SourceArn` and
`aws:SourceAccount` global condition context keys in your execution role trust policy to prevent
the confused deputy problem:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "scheduler.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`123456789012`",
 "aws:SourceArn": "arn:aws:scheduler:`us-west-2`:`123456789012`:schedule-group/`your-schedule-group`"
 }
 }
 }
 ]
}`

```
