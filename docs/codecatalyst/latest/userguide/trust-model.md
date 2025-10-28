Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Understanding the CodeCatalyst trust model

The Amazon CodeCatalyst trust model allows CodeCatalyst to assume the service role in the connected
AWS account. The model connects the IAM role, the CodeCatalyst service principals, and the
CodeCatalyst space. The trust policy uses the `aws:SourceArn` condition key to
grant permissions to the CodeCatalyst space specified in the condition key. For more
information about this condition key, see [aws:SourceArn](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn") in the _IAM User
Guide_.

A trust policy is a JSON policy document in which you define the principals that you trust
to assume the role. A role trust policy is a required resource-based policy that is attached
to a role in IAM. For more information, see [Terms and concepts](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md")
in the _IAM User Guide_. For details about the service
principals for CodeCatalyst, see [Service principals for CodeCatalyst](#service-principals "#service-principals").

In the following trust policy, the service principals listed in the `Principal`
element are granted permissions from the resource-based policy, and the
`Condition` block is used to limit access to the scoped-down resource.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "codecatalyst-runner.amazonaws.com",
 "codecatalyst.amazonaws.com"
 ]
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "ArnLike": {
 "aws:SourceArn": "arn:aws:codecatalyst:::space/`spaceId`/project/*"
 }
 }
 }
 ]
}`

```

In the trust policy, the CodeCatalyst service principals are given access through the
`aws:SourceArn` condition key, which contains the Amazon Resource Name (ARN)
for the CodeCatalyst space ID. The ARN uses the following format:

```
arn:aws:codecatalyst:::space/`spaceId`/project/*
```

###### Important

Use the space ID only in condition keys, such as `aws:SourceArn`. Do
not use the space ID in IAM policy statements as a resource ARN.

As a best practice, scope down permissions as much as possible in the policy.

- You can use the wildcard (\*) in the `aws:SourceArn` condition key for
  specifying all projects in the space with `project/*`.
- You can specify resource-level permissions in the `aws:SourceArn`
  condition key for a specific project in the space with
  `project/`projectId``.

## Service principals for CodeCatalyst

You use the `Principal` element in a resource-based JSON policy to specify
the principal that is allowed or denied access to a resource. The principals that you
can specify in the trust policy include users, roles, accounts, and services. You cannot
use the `Principal` element in an identity-based policy; similarly, you
cannot identify a user group as a principal in a policy (such as a resource-based
policy) because groups relate to permissions, not authentication, and principals are
authenticated IAM entities.

In the trust policy, you can specify AWS services in the `Principal`
element of a resource-based policy or in condition keys that support principals. Service
principals are defined by the service. The following are the service principals defined
for CodeCatalyst:

- **codecatalyst.amazonaws.com** - This service principal is
  used for a role that will grant CodeCatalyst access to AWS.
- **codecatalyst-runner.amazonaws.com** - This service
  principal is used for a role that will grant CodeCatalyst access to AWS resources in
  deployments for CodeCatalyst workflows.

For more information, see [AWS JSON
policy elements: Principal](../../../IAM/latest/UserGuide/reference_policies_elements_principal.md "../../../IAM/latest/UserGuide/reference_policies_elements_principal.md") in the _IAM User
Guide_.
