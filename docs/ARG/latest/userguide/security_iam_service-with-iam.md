# How Resource Groups works with IAM

Before you use IAM to manage access to Resource Groups, you should understand what IAM features
are available to use with Resource Groups. To get a high-level view of how Resource Groups and other AWS
services work with IAM, see [AWS Services That
Work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

###### Topics

- [Resource Groups identity-based policies](#security_iam_service-with-iam-id-based-policies-arg-te "#security_iam_service-with-iam-id-based-policies-arg-te")
- [Resource-based policies](#security_iam_resource-based-policies "#security_iam_resource-based-policies")
- [Authorization based on Resource Groups tags](#security_iam_tags "#security_iam_tags")
- [Resource Groups IAM roles](#security_iam_roles "#security_iam_roles")

## Resource Groups identity-based policies

With IAM identity-based policies, you can specify allowed or denied actions and
resources as well as the conditions under which actions are allowed or denied. Resource Groups
supports specific actions, resources, and condition keys. To learn about all of the
elements that you use in a JSON policy, see [IAM JSON Policy Elements
Reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the _IAM User Guide_.

### Actions

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the
actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

Policy actions in Resource Groups use the following prefix before the action:
`resource-groups:`. Tag Editor actions are performed entirely in the
console, but have the prefix `resource-explorer` in log entries.

For example, to grant someone permission to create a Resource Groups group with the Resource Groups
`CreateGroup` API operation, you include the
`resource-groups:CreateGroup` action in their policy. Policy
statements must include either an `Action` or `NotAction`
element. Resource Groups defines its own set of actions that describe tasks that you can
perform with this service.

To specify multiple Resource Groups and Tag Editor actions in a single statement, separate them
with commas as follows:

```
"Action": [
      "resource-groups:*action1*",
      "resource-groups:*action2*",
      "resource-explorer:*action3*"
```

You can specify multiple actions using wildcards (\*). For example, to specify all
actions that begin with the word `List`, include the following
action:

```
`"Action": "resource-groups:List*"`
```

To see a list of Resource Groups actions, see [Actions, Resources, and
Condition Keys for AWS Resource Groups](../../../IAM/latest/UserGuide/list_awsresourcegroups.md "../../../IAM/latest/UserGuide/list_awsresourcegroups.md") in the
_IAM User Guide_.

### Resources

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md"). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

The only Resource Groups resource is a _group_. The group resource has an
ARN in the following format:

```
arn:${Partition}:resource-groups:${Region}:${Account}:group/${GroupName}
```

For more information about the format of ARNs, see [Amazon Resource Names (ARNs)
and AWS Service Namespaces](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md").

For example, to specify the `my-test-group` resource group in your
statement, use the following ARN:

```
"Resource": "arn:aws:resource-groups:us-east-1:123456789012:group/my-test-group"
```

To specify all groups that belong to a specific account, use the wildcard
(\*):

```
"Resource": "arn:aws:resource-groups:us-east-1:123456789012:group/*"
```

Some Resource Groups actions, such as those for creating resources, cannot be performed on a
specific resource. In those cases, you must use the wildcard (\*).

```
"Resource": "*"
```

Some Resource Groups API actions can involve multiple resources. For example,
`DeleteGroup` deletes groups, so a calling principal must have
permissions to delete a specific group or all groups. To specify multiple resources
in a single statement, separate the ARNs with commas.

```
"Resource": [
  "*resource1*",
  "*resource2*"
]
```

To see a list of Resource Groups resource types and their ARNs, and learn with which actions
you can specify the ARN of each resource, see [Actions, Resources, and
Condition Keys for AWS Resource Groups](../../../IAM/latest/UserGuide/list_awsresourcegroups.md "../../../IAM/latest/UserGuide/list_awsresourcegroups.md") in the
_IAM User Guide_.

### Condition keys

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition
operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md"), such as equals or less than, to match the condition in the
policy with values in the request. To see all AWS global
condition keys, see [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

Resource Groups defines its own set of condition keys and also supports using some global
condition keys. To see all AWS global condition keys, see [AWS Global
Condition Context Keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

To see a list of Resource Groups condition keys, and learn with which actions and resources
you can use a condition key, see [Actions, Resources, and
Condition Keys for AWS Resource Groups](../../../IAM/latest/UserGuide/list_awsresourcegroups.md "../../../IAM/latest/UserGuide/list_awsresourcegroups.md") in the
_IAM User Guide_.

### Examples

To view examples of Resource Groups identity-based policies, see [AWS Resource Groups identity-based policy examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Resource-based policies

Resource Groups does not support resource-based policies.

## Authorization based on Resource Groups tags

You can attach tags to groups in Resource Groups, or pass tags in a request to Resource Groups. To control
access based on tags, you provide tag information in the [condition
element](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") of a policy using the
`aws:ResourceTag/`key-name``,
 `aws:RequestTag/`key-name``, or
`aws:TagKeys` condition keys. You can apply tags to a group when you are
creating or updating the group. For more information about tagging a group in Resource Groups, see
[Creating query-based groups in AWS Resource Groups](gettingstarted-query.md "gettingstarted-query.md") and
[Updating groups in AWS Resource Groups](updating-resource-groups.md "updating-resource-groups.md")
in this guide.

To view an example identity-based policy for limiting access to a resource based on
the tags on that resource, see [Viewing groups based on tags](security_iam_id-based-policy-examples.md#security_iam_policy-examples-view-tags "security_iam_id-based-policy-examples.md#security_iam_policy-examples-view-tags").

## Resource Groups IAM roles

An [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md")
is an entity within your AWS account that has specific permissions. Resource Groups does not
have or use service roles.

### Using temporary credentials with Resource Groups

In Resource Groups, you can use temporary credentials to sign in with federation, assume an
IAM role, or to assume a cross-account role. You obtain temporary security
credentials by calling AWS STS API operations such as [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") or [GetFederationToken](../../../STS/latest/APIReference/API_GetFederationToken.md "../../../STS/latest/APIReference/API_GetFederationToken.md").

### Service-linked roles

[Service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role") allow AWS services to access resources in other
services to complete an action on your behalf.

Resource Groups does not have or use service-linked roles.

### Service roles

This feature allows a service to assume a [service role](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-role") on your behalf.

Resource Groups does not have or use service roles.
