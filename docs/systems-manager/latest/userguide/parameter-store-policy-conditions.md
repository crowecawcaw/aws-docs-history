AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Preventing access to Parameter Store

API operations

Using service-specific _[conditions](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md")_ supported by Systems Manager for AWS Identity and Access Management (IAM)
policies, you can explicity allow or deny access to Parameter Store API operations and
content. By using these conditions, you can allow only certain IAM Entities (users
and roles) in your organization to call certain API actions, or prevent certain
IAM Entities from running them. This includes actions run through the Parameter Store
console, the AWS Command Line Interface (AWS CLI), and SDKs.

Systems Manager currently supports three conditions that are specific to Parameter Store.

###### Topics

- [Preventing changes to existing parameters
  using ssm:Overwrite](#overwrite-condition "#overwrite-condition")
- [Preventing creation or updates to
  parameters that use a parameter policy using
  ssm:Policies](#parameter-policies-condition "#parameter-policies-condition")
- [Preventing access to levels in a
  hierarchical parameter using ssm:Recursive](#recursive-condition "#recursive-condition")

## Preventing changes to existing parameters

using `ssm:Overwrite`

Use the `ssm:Overwrite` condition to control whether IAM Entities
can update existing parameters.

In the following sample policy, the `"Allow"` statement grants
permission to create parameters by running the `PutParameter` API
operation in the AWS account 123456789012 in the US East (Ohio) Region
(us-east-2).

However, the `"Deny"` statement prevents Entities from changing
values of _existing_ parameters because the
`Overwrite` option is explicitly denied for the
`PutParameter` operation. Therefore, Entities that are assigned
this policy can create parameters, but not make changes to existing
parameters.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ssm:PutParameter"
 ],
 "Resource": "arn:aws:ssm:`us-east-1`:`111122223333`:parameter/*"
 },
 {
 "Effect": "Deny",
 "Action": [
 "ssm:PutParameter"
 ],
 "Condition": {
 "StringEquals": {
 "ssm:Overwrite": [
 "true"
 ]
 }
 },
 "Resource": "arn:aws:ssm:`us-east-1`:`111122223333`:parameter/*"
 }
 ]
}`

```

## Preventing creation or updates to

parameters that use a parameter policy using
`ssm:Policies`

User the `ssm:Policies` condition to control whether Entities can
create parameters that include a parameter policy and update existing parameters
that include a parameter policy.

In the following policy example, the `"Allow"` statement grants
general permission to create parameters, but the `"Deny"` statement
prevents Entities from creating or updating parameters that include a parameter
policy in the the AWS account 123456789012 in the US East (Ohio) Region
(us-east-2). Entities can still create or update parameters that aren't assigned
a parameter policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ssm:PutParameter"
 ],
 "Resource": "arn:aws:ssm:`us-east-1`:`111122223333`:parameter/*"
 },
 {
 "Effect": "Deny",
 "Action": [
 "ssm:PutParameter"
 ],
 "Condition": {
 "StringEquals": {
 "ssm:Policies": [
 "true"
 ]
 }
 },
 "Resource": "arn:aws:ssm:`us-east-1`:`111122223333`:parameter/*"
 }
 ]
}`

```

## Preventing access to levels in a

hierarchical parameter using `ssm:Recursive`

Use the `ssm:Recursive` condition to control whether IAM Entities
can view or reference levels in a hierarchical parameter. You can provide or
restrict access to all parameters beyond a specific level of a hierarchy.

In the following example policy, the `"Allow"` statement provides
access to Parameter Store operations on all parameters in the path
`/Code/Departments/Finance/*` for the AWS account
123456789012 in the US East (Ohio) Region (us-east-2).

After this, the `"Deny"` statement prevents IAM Entities from
viewing or retrieving parameter data at or below the level of
`/Code/Departments/*`. Entities can still, however, still
create or update parameters in that path. The example has been constructed to
illustrate that recursively denying access below a certain level in a parameter
hierarchy takes precedence over more permissive access in the same
policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ssm:*"
 ],
 "Resource": "arn:aws:ssm:`us-east-1`:`111122223333`:parameter`/*`"
 },
 {
 "Effect": "Deny",
 "Action": [
 "ssm:GetParametersByPath"
 ],
 "Condition": {
 "StringEquals": {
 "ssm:Recursive": [
 "true"
 ]
 }
 },
 "Resource": "arn:aws:ssm:`us-east-1`:`111122223333`:parameter/Code/Departments/*"
 }
 ]
}`

```

###### Important

If a user has access to a path, then the user can access all levels of
that path. For example, if a user has permission to access path
`/a`, then the user can also access
`/a/b`. This is true unless the user has explicitly
been denied access in IAM for parameter `/b`, as
illustrated above.
