# How Tag Editor works with IAM

Before you use IAM to manage access to Tag Editor, you should understand what IAM
features are available to use with Tag Editor. To get a high-level view of how Tag Editor and
other AWS services work with IAM, see [AWS services that
work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

###### Topics

- [Tag Editor
  identity-based policies](#security_iam_service-with-iam-id-based-policies-arg-te "#security_iam_service-with-iam-id-based-policies-arg-te")
- [Resource-based policies](#security_iam_resource-based-policies "#security_iam_resource-based-policies")
- [Authorization based on tags](#security_iam_tags "#security_iam_tags")
- [Tag Editor IAM roles](#security_iam_roles "#security_iam_roles")

## Tag Editor

identity-based policies

With IAM identity-based policies, you can specify allowed or denied actions and
resources in addition to the conditions under which actions are allowed or denied.
Tag Editor supports specific actions, resources, and condition keys. To learn about all of
the elements that you use in a JSON policy, see [IAM JSON policy elements
reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the _IAM User Guide_.

### Actions

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the
actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

Policy actions in Tag Editor use the following prefix before the action:
`tag:`. Tag Editor actions are performed entirely in the console, but
have the prefix `tag` in log entries.

For example, to grant someone permission to tag a resource with the
`tag:TagResources` API operation, you include the
`tag:TagResources` action in their policy. Policy statements must
include either an `Action` or `NotAction` element. Tag Editor
defines its own set of actions that describe tasks that you can perform with this
service.

To specify multiple tagging actions in a single statement, separate them with
commas as follows.

```
"Action": [
      "tag:*action1*",
      "tag:*action2*",
      "tag:*action3*"
```

You can specify multiple actions using wildcards (\*). For example, to specify all
actions that begin with the word `Get`, include the following
action.

```
`"Action": "tag:Get*"`
```

To see a list of Tag Editor actions, see [Actions,
resources, and condition keys for Tag Editor](../../../service-authorization/latest/reference/list_tageditor.md "../../../service-authorization/latest/reference/list_tageditor.md") in the
_Service Authorization Reference_.

### Resources

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md"). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

Tag Editor does not have any resources of its own. Instead, it manipulates the
metadata (tags) that are attached to resources created by other
AWS services.

### Condition

keys

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition
operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md"), such as equals or less than, to match the condition in the
policy with values in the request. To see all AWS global
condition keys, see [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

Tag Editor does not define any service-specific condition keys.

### Examples

To view examples of Tag Editor identity-based policies, see [Tag Editor identity-based policy
examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Resource-based policies

Tag Editor does not support resource-based policies because it doesn't define any of its
own resources.

## Authorization based on tags

Authorization based on tags is part of the security strategy called attribute-based
access control (ABAC).

To control access to a resource based on its tags, you provide tag information in the
[condition
element](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") of a policy using the
`aws:ResourceTag/`key-name``,
 `aws:RequestTag/`key-name``, or
`aws:TagKeys` condition keys. You can apply tags to a resource when you
are creating or updating the resource.

To view an example identity-based policy for limiting access to a resource based on
the tags on that resource, see [Viewing groups based on
tags](security_iam_id-based-policy-examples.md#security_iam_policy-examples-view-tags "security_iam_id-based-policy-examples.md#security_iam_policy-examples-view-tags"). For more information about
attribute-based access control (ABAC), see [What is
ABAC for AWS?](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") in the _IAM User Guide_.

## Tag Editor IAM roles

An [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md")
is an entity within your AWS account that has specific permissions. Tag Editor does not
have or use service roles.

### Using temporary credentials with

Tag Editor

In Tag Editor, you can use temporary credentials to sign in with federation, assume
an IAM role, or to assume a cross-account role. You obtain temporary security
credentials by calling AWS STS API operations such as [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") or
[GetFederationToken](../../../STS/latest/APIReference/API_GetFederationToken.md "../../../STS/latest/APIReference/API_GetFederationToken.md").

### Service-linked roles

[Service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role") allow AWS services to access resources in other
services to complete an action on your behalf.

Tag Editor does not have or use service-linked roles.

### Service roles

This feature allows a service to assume a [service role](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-role") on your behalf.

Tag Editor does not have or use service roles.
