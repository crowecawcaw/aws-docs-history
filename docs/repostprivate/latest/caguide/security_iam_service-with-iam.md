# How re:Post Private works with IAM

Before you use IAM to manage access to AWS re:Post Private, you must understand which
IAM features are available to use with re:Post Private. To get a high-level view of how re:Post Private and other AWS services work with IAM, see [AWS services that
work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

## re:Post Private identity-based policies

With IAM identity-based policies, you can specify allowed or denied actions.
re:Post Private supports specific actions. To learn
about the elements that you use in a JSON policy, see [IAM JSON policy elements
reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the _IAM User Guide_.

### Actions

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the
actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

Policy actions in re:Post Private use the following prefix before the action:
`repostspace:`. For example, to grant someone permission to run the re:Post Private `CreateSpace` API operation, you include the `repostspace:CreateSpace` action in their policy. Policy statements must include either an `Action` or `NotAction` element.
re:Post Private defines its own set of actions that describe tasks that you can
perform with this service.

To specify multiple actions in a single statement, separate them with commas as
follows:

```
"Action": [
      "repostspace:*CreateSpace*",
      "repostspace:*DeleteSpace*"
```

You can specify multiple actions using wildcards (\*). For example, to specify all
actions that begin with the word `Describe`, include the following
action:

```
`"Action": "repostspace:Describe*"`
```

To see a list of re:Post Private actions, see [Actions defined by re:Post Private](../../../IAM/latest/UserGuide/list_amazonworkdocs.md#amazonworkdocs-actions-as-permissions "../../../IAM/latest/UserGuide/list_amazonworkdocs.md#amazonworkdocs-actions-as-permissions") in the _IAM User Guide_.

### Resources

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md"). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

### Condition keys

re:Post Private doesn't provide any service-specific condition keys, but it supports using global condition keys. To see all AWS global condition keys, see [AWS global condition
context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the _IAM User Guide_.

### Examples

To view examples of re:Post Private identity-based policies, see [AWS re:Post Private identity-based
policy examples](security-iam-policy-examples.md "security-iam-policy-examples.md").

## re:Post Private resource-based policies

Resource-based policies are JSON policy documents that you attach to a resource. Examples of resource-based policies are IAM role trust policies and Amazon S3 bucket policies. In services that support resource-based policies, service administrators can use them to control access to a specific resource. For the resource where the policy is attached, the policy defines what actions a specified principal can perform on that resource and under what conditions. You must [specify a principal](../../../IAM/latest/UserGuide/reference_policies_elements_principal.md "../../../IAM/latest/UserGuide/reference_policies_elements_principal.md") in a resource-based policy. Principals can include accounts, users, roles, federated users, or AWS services. Resource-based policies are inline policies that are located in that service. You can't use AWS managed policies from IAM in a resource-based policy.

re:Post Private doesn't support resource-based policies.

## Authorization based on tags

re:Post Private supports tagging resources or controlling access based on tags. For more information, see [Controlling access to AWS resources using tags](../../../IAM/latest/UserGuide/access_tags.md "../../../IAM/latest/UserGuide/access_tags.md").

## re:Post Private IAM

roles

An [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") is an entity within
your AWS account that has specific permissions.

### Using temporary

credentials with re:Post Private

We strongly recommend using temporary credentials to sign in with federation,
assume an IAM role, or to assume a cross-account role. You obtain
temporary security credentials by calling AWS STS API operations such as
[AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") or
[GetFederationToken](../../../STS/latest/APIReference/API_GetFederationToken.md "../../../STS/latest/APIReference/API_GetFederationToken.md").

re:Post Private supports using temporary credentials.

## Service-linked

roles

[Service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role") allow AWS services to access resources in other
services to complete an action for you. Service-linked roles appear in your
IAM account and are owned by the service. An IAM administrator can view but not
edit the permissions for service-linked roles.

## Service roles

This feature allows a service to assume a [service
role](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-role") for you. This role allows the service to access resources in
other services to complete an action for you. For more information, see [Creating a role to delegate permissions to an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md"). Service roles appear in your IAM account and are owned by the account. This means that an IAM administrator
can change the permissions for this role. However, doing so might break the
functionality of the service.
