End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Cross-service confused deputy

prevention

The [confused deputy problem](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md") is a security issue where an entity that doesn't have
permission to perform an action can trick a more-privileged entity to perform the action.
In AWS, cross-service impersonation can result in the confused deputy problem.
Cross-service impersonation can occur when one service (the _calling
service_) calls another service (the _called service_). The
calling service can be manipulated to use its permissions to act on another customer's
resources in a way it shouldn't otherwise have permission to access. To prevent this, AWS
provides tools that help you protect your data for all services with service principals that
have been given access to resources in your account.

We recommend using the [`aws:SourceArn`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn") and [`aws:SourceAccount`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount") global condition context keys in resource
policies to limit the permissions that AWS SimSpace Weaver gives another service to the
resource. If the `aws:SourceArn` value doesn't contain the account ID, such as
an Amazon S3 bucket Amazon Resource Name (ARN), you must use both global condition context keys
to limit permissions. If you use both global condition context keys and the
`aws:SourceArn` value contains the account ID, the
`aws:SourceAccount` value and the account in the `aws:SourceArn`
value must use the same account ID when used in the same policy statement. Use
`aws:SourceArn` if you want only one resource to be associated with the
cross-service access. Use `aws:SourceAccount` if you want to allow any resource
in that account to be associated with the cross-service use.

The value of `aws:SourceArn` must use the extension's ARN.

The most effective way to protect against the confused deputy problem is to use the
`aws:SourceArn` global condition context key with the full ARN of the
resource. If you don't know the full ARN of the extension or if you are specifying multiple
extensions, use the `aws:SourceArn` global context condition key with wildcards
(`*`) for the unknown portions of the ARN. For example,
`arn:aws:`simspaceweaver`:*:`111122223333`:*`.

The following example shows how you can use the `aws:SourceArn` and
`aws:SourceAccount` global condition context keys in SimSpace Weaver to prevent
the confused deputy problem. This policy will only permit SimSpace Weaver to assume the role when
the request comes from the specified source account, and provided with the specified ARN.
In this case, SimSpace Weaver can only assume the role for requests from simulations in the
requestor's own account (`111122223333`),
and only in the specified Region (`us-west-2`).

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "simspaceweaver.amazonaws.com"
 ]
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "111122223333"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:simspaceweaver:us-west-2:`111122223333`:simulation/*"
 }
 }
 }
 ]
}`

```

A more secure way to write this policy is to include the simulation name in the `aws:SourceArn`,
as shown in the following example, which restricts the policy to a simulation named `MyProjectSimulation_22-10-04_22_10_15`:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "simspaceweaver.amazonaws.com"
 ]
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "111122223333"
 },
 "StringLike": {
 "aws:SourceArn": "arn:aws:simspaceweaver:us-west-2:`111122223333`:simulation/MySimulation"
 }
 }
 }
 ]
}`

```

When your `aws:SourceArn` explicitly includes an account number,
you can leave out the `Condition` element test for the `aws:SourceAccount`
(see the [IAM User Guide](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn") for more information),
such as in the following simplified policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "simspaceweaver.amazonaws.com"
 ]
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringLike": {
 "aws:SourceArn": "arn:aws:simspaceweaver:us-west-2:`111122223333`:simulation/MySimulation"
 }
 }
 }
 ]
}`

```
