# Cross-service confused deputy

prevention

The confused deputy problem is a security issue where an entity that doesn't have permission
to perform an action can coerce a more-privileged entity to perform the action. In AWS,
cross-service impersonation can result in the confused deputy problem. Cross-service
impersonation can occur when one service (the _calling service_) calls
another service (the _called service_). The calling service can be
manipulated to use its permissions to act on another customer's resources in a way it shouldn't
otherwise have permission to access. To prevent this, AWS provides tools that help you protect
your data for all services with service principals that have been given access to resources in
your account.

We recommend using the [aws:SourceArn](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn") and [aws:SourceAccount](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount") global condition context keys in resource policies
to limit the permissions that CloudFormation gives another service to a specific resource,
such as a CloudFormation extension. Use `aws:SourceArn` if you want only one resource
to be associated with the cross-service access. Use `aws:SourceAccount` if you want
to allow any resource in that account to be associated with the cross-service use.

Make sure that the value of `aws:SourceArn` is an ARN of the resource that
CloudFormation stores.

The most effective way to protect against the confused deputy problem is to use the
`aws:SourceArn` global condition context key with the full ARN of the resource. If
you don't know the full ARN of the resource or if you are specifying multiple resources, use the
`aws:SourceArn` global context condition key with wildcards (`*`) for
the unknown portions of the ARN. For example,
`arn:aws:`cloudformation`:*:`123456789012`:*`.

If the `aws:SourceArn` value doesn't contain the account ID, you must use both
global condition context keys to limit permissions.

The following example shows how you can use the `aws:SourceArn` and
`aws:SourceAccount` global condition context keys in CloudFormation to prevent the
confused deputy problem.

## Example trust policy that

uses `aws:SourceArn` and `aws:SourceAccount` condition keys

For registry services, CloudFormation makes calls to AWS Security Token Service (AWS STS) to assume a service
role in your account. This role is configured for `ExecutionRoleArn` in the [RegisterType](../APIReference/API_RegisterType.md "../APIReference/API_RegisterType.md") operation and `LogRoleArn` set in the
[LoggingConfig](../APIReference/API_LoggingConfig.md "../APIReference/API_LoggingConfig.md") operation. For more information, see [Configure an execution role
with IAM permissions and a trust policy for public extension access](registry-public.md#registry-public-enable-execution-role "registry-public.md#registry-public-enable-execution-role").

This example role trust policy uses condition statements to limit the
`AssumeRole` capability on the service role to only actions on the specified
CloudFormation extension in the specified account. The `aws:SourceArn` and
`aws:SourceAccount` conditions are evaluated independently. Any request to use
the service role must satisfy both conditions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "resources.cloudformation.amazonaws.com"
 ]
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`123456789012`"
 },
 "ArnLike": {
 "aws:SourceArn": "`arn:aws:cloudformation:us-east-1:123456789012:type/resource/Organization-Service-Resource`"
 }
 }
 }
 ]
}`

```

## Additional

information

For example policies that use the `aws:SourceArn` and
`aws:SourceAccount` global condition context keys for a service role used by
StackSets, see [Set up global keys to mitigate confused
deputy problems](stacksets-prereqs-self-managed.md#confused-deputy-mitigation "stacksets-prereqs-self-managed.md#confused-deputy-mitigation").

For more information, see [Update a role trust
policy](../../../IAM/latest/UserGuide/id_roles_update-role-trust-policy.md "../../../IAM/latest/UserGuide/id_roles_update-role-trust-policy.md") in the _IAM User Guide_.
