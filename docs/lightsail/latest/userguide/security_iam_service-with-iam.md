# How Amazon Lightsail works with IAM

Before you use IAM to manage access to Lightsail, you should understand what IAM
features are available to use with Lightsail. To get a high-level view of how Lightsail
and other AWS services work with IAM, see [AWS Services That Work
with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

## Lightsail

Identity-Based Policies

With IAM identity-based policies, you can specify allowed or denied actions and
resources as well as the conditions under which actions are allowed or denied. Lightsail
supports specific actions, resources, and condition keys. To learn about all of the
elements that you use in a JSON policy, see [IAM JSON Policy Elements
Reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the _IAM User Guide_.

### Actions

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the
actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

Policy actions in Lightsail use the following prefix before the action:
`lightsail:`. For example, to grant someone permission to run a
Lightsail instance with the Lightsail `CreateInstances` API operation,
you include the `lightsail:CreateInstances` action in their policy. Policy
statements must include either an `Action` or `NotAction` element.
Lightsail defines its own set of actions that describe tasks that you can perform with
this service.

To specify multiple actions in a single statement, separate them with commas as
follows:

```
"Action": [
      "lightsail:*action1*",
      "lightsail:*action2*"
```

You can specify multiple actions using wildcards (\*). For example, to specify all
actions that begin with the word `Create`, include the following
action:

```
`"Action": "lightsail:Create*"`
```

To see a list of Lightsail actions, see [Actions Defined by Amazon Lightsail](../../../IAM/latest/UserGuide/list_amazonlightsail.md#amazonlightsail-actions-as-permissions "../../../IAM/latest/UserGuide/list_amazonlightsail.md#amazonlightsail-actions-as-permissions") in the
_IAM User Guide_.

### Resources

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md"). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

###### Important

Lightsail does not support resource-level permissions for some API actions. For
more information, see [Support for
resource-level permissions and authorization based on tags](resource-level-permissions-and-auth-based-on-tags-support.md "resource-level-permissions-and-auth-based-on-tags-support.md").

The Lightsail instance resource has the following ARN:

```
arn:${Partition}:lightsail:${Region}:${Account}:Instance/${InstanceId}
```

For more information about the format of ARNs, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md").

For example, to specify the `ea123456-e6b9-4f1d-b518-3ad1234567e6`
instance in your statement, use the following ARN:

```
"Resource": "arn:aws:lightsail:us-east-1:123456789012:Instance/ea123456-e6b9-4f1d-b518-3ad1234567e6"
```

To specify all instances that belong to a specific account, use the wildcard
(\*):

```
"Resource": "arn:aws:lightsail:us-east-1:123456789012:Instance/*"
```

Some Lightsail actions, such as those for creating resources, cannot be performed
on a specific resource. In those cases, you must use the wildcard (\*).

```
"Resource": "*"
```

Many Lightsail API actions involve multiple resources. For example,
`AttachDisk` attaches a Lightsail block storage disk to an instance, so
an IAM user must have permissions to use the disk and the instance. To specify
multiple resources in a single statement, separate the ARNs with commas.

```
"Resource": [
      "*resource1*",
      "*resource2*"
```

To see a list of Lightsail resource types and their ARNs, see
[Resources Defined by Amazon Lightsail](../../../IAM/latest/UserGuide/list_amazonlightsail.md#amazonlightsail-resources-for-iam-policies "../../../IAM/latest/UserGuide/list_amazonlightsail.md#amazonlightsail-resources-for-iam-policies") in the _IAM User Guide_. To learn with
which actions you can specify the ARN of each resource, see
[Actions Defined by Amazon Lightsail](../../../IAM/latest/UserGuide/list_amazonlightsail.md#amazonlightsail-actions-as-permissions "../../../IAM/latest/UserGuide/list_amazonlightsail.md#amazonlightsail-actions-as-permissions").

### Condition Keys

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition
operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md"), such as equals or less than, to match the condition in the
policy with values in the request. To see all AWS global
condition keys, see [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

Lightsail does not provide any service-specific condition keys, but it does support
using some global condition keys. To see all AWS global condition keys, see [AWS Global Condition
Context Keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the _IAM User Guide_.

To see a list of Lightsail condition keys, see [Condition Keys for Amazon Lightsail](../../../IAM/latest/UserGuide/list_amazonlightsail.md#amazonlightsail-policy-keys "../../../IAM/latest/UserGuide/list_amazonlightsail.md#amazonlightsail-policy-keys") in the
_IAM User Guide_. To learn with which actions and resources you
can use a condition key, see [Actions Defined by Amazon Lightsail](../../../IAM/latest/UserGuide/list_amazonlightsail.md#amazonlightsail-actions-as-permissions "../../../IAM/latest/UserGuide/list_amazonlightsail.md#amazonlightsail-actions-as-permissions").

### Examples

To view examples of Lightsail identity-based policies, see [Amazon Lightsail Identity-Based Policy
Examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Lightsail

Resource-Based Policies

Lightsail does not support resource-based policies.

## Access Control Lists (ACLs)

Lightsail does not support Access Control Lists (ACLs).

## Authorization Based on Lightsail

Tags

You can attach tags to Lightsail resources or pass tags in a request to Lightsail.
To control access based on tags, you provide tag information in the [condition element](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md")
of a policy using the
`lightsail:ResourceTag/`key-name``,
 `aws:RequestTag/`key-name``, or
`aws:TagKeys` condition keys.

###### Important

Lightsail does not support authorization based on tags for some API actions. For
more information, see [Support for
resource-level permissions and authorization based on tags](resource-level-permissions-and-auth-based-on-tags-support.md "resource-level-permissions-and-auth-based-on-tags-support.md").

For more information about tagging Lightsail resources, see [Tags](amazon-lightsail-tags.md "amazon-lightsail-tags.md").

To view an example identity-based policy for limiting access to a resource based on the
tags on that resource, see [Allowing Creation and Deletion of Lightsail Resources Based on Tags](https://lightsail.aws.amazon.com/ls/docs/en_us/articles/security_iam_id-based-policy-examples#security_iam_id-based-policy-examples-view-widget-tags "https://lightsail.aws.amazon.com/ls/docs/en_us/articles/security_iam_id-based-policy-examples#security_iam_id-based-policy-examples-view-widget-tags").

## Lightsail IAM Roles

An [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") is an entity within your
AWS account that has specific permissions.

### Using Temporary

Credentials with Lightsail

You can use temporary credentials to sign in with federation, assume an IAM role,
or to assume a cross-account role. You obtain temporary security credentials by calling
AWS STS API operations such as [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") or [GetFederationToken](../../../STS/latest/APIReference/API_GetFederationToken.md "../../../STS/latest/APIReference/API_GetFederationToken.md").

Lightsail supports using temporary credentials.

### Service-Linked

Roles

[Service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role") allow AWS services to access resources in other
services to complete an action on your behalf. Service-linked roles appear in your IAM
account and are owned by the service. An IAM administrator can view but not edit the
permissions for service-linked roles.

Lightsail supports service-linked roles. For details about creating or managing
Lightsail service-linked roles, see [Service-linked
roles](amazon-lightsail-using-service-linked-roles.md "amazon-lightsail-using-service-linked-roles.md").

### Service Roles

Lightsail does not support service roles.

###### Topics

- [Identity-based policy examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md")
- [Resource-level permissions policy examples](security_iam_resource-based-policy-examples.md "security_iam_resource-based-policy-examples.md")
- [Use service-linked roles](amazon-lightsail-using-service-linked-roles.md "amazon-lightsail-using-service-linked-roles.md")
- [Manage buckets with IAM](amazon-lightsail-bucket-management-policies.md "amazon-lightsail-bucket-management-policies.md")
