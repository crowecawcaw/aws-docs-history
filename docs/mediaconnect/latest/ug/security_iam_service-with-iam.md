# How AWS Elemental MediaConnect works with

IAM

Before you use IAM to manage access to MediaConnect, you should understand what
IAM features are available to use with MediaConnect. To get a high-level view of
how MediaConnect and other AWS services work with IAM, see [AWS Services
That Work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

###### Topics

- [MediaConnect
  identity-based policies](#security_iam_service-with-iam-id-based-policies "#security_iam_service-with-iam-id-based-policies")
- [MediaConnect resource-based policies](#security_iam_service-with-iam-resource-based-policies "#security_iam_service-with-iam-resource-based-policies")
- [Authorization based on
  MediaConnect tags](#security_iam_service-with-iam-tags "#security_iam_service-with-iam-tags")
- [MediaConnect IAM
  roles](#security_iam_service-with-iam-roles "#security_iam_service-with-iam-roles")

## MediaConnect

identity-based policies

With IAM identity-based policies, you can specify allowed or denied actions and
resources as well as the conditions under which actions are allowed or denied.
MediaConnect supports specific actions, resources, and condition keys. To learn
about all of the elements that you use in a JSON policy, see [IAM JSON Policy Elements
Reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the _IAM User Guide_.

### Actions

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the
actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

Policy actions in MediaConnect use the following prefix before the action:
`mediaconnect:`. For example, to grant someone permission
to view a list of entitlements with the MediaConnect
`ListEntitlements` API operation, you include the
`mediaconnect:ListEntitlements` action in their policy. Policy
statements must include either an `Action` or `NotAction`
element. MediaConnect defines its own set of actions that describe tasks
that you can perform with this service.

To specify multiple actions in a single statement, separate them with commas
as follows:

```
"Action": [
      "mediaconnect:*action1*",
      "mediaconnect:*action2*"
```

You can specify multiple actions using wildcards (\*). For example, to specify
all actions that begin with the word `List`, include the following
action:

```
`"Action": "mediaconnect:List*"`
```

To see a list of MediaConnect actions, see [Actions Defined by AWS Elemental MediaConnect](../../../IAM/latest/UserGuide/list_awselementalmediaconnect.md#awselementalmediaconnect-actions-as-permissions "../../../IAM/latest/UserGuide/list_awselementalmediaconnect.md#awselementalmediaconnect-actions-as-permissions") in the
_IAM User Guide_.

### Resources

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md"). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

MediaConnect has the following ARNs:

```
arn:${Partition}:mediaconnect:${Region}:${Account}:entitlement:${resourceID}:${resourceName}
arn:${Partition}:mediaconnect:${Region}:${Account}:flow:${resourceID}:${resourceName}
arn:${Partition}:mediaconnect:${Region}:${Account}:output:${resourceID}:${resourceName}
arn:${Partition}:mediaconnect:${Region}:${Account}:source:${resourceID}:${resourceName}
```

For more information about the format of ARNs, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md").

For example, to specify the `1-23aBC45dEF67hiJ8-12AbC34DE5fG` flow
in your statement, use the following ARN:

```
"Resource": "arn:aws:mediaconnect:us-east-1:111122223333:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:BasketballGame"
```

To specify all flows that belong to a specific account, use the wildcard
(\*):

```
"Resource": "arn:aws:mediaconnect:us-east-1:111122223333:flow:*"
```

Some MediaConnect actions, such as those for creating resources, can't be
performed on a specific resource. In those cases, you must use the wildcard
(\*).

```
"Resource": "*"
```

Many MediaConnect API actions involve multiple resources. For example,
`RemoveFlowOutput` removes an output from a particular flow, so
an IAM user must have permissions for the flow and the output. To specify
multiple resources in a single statement, separate the ARNs with commas.

```
"Resource": [
      "*resource1*",
      "*resource2*"
```

To see a list of MediaConnect resource types and their ARNs, see
[Resources Defined by AWS Elemental MediaConnect](../../../IAM/latest/UserGuide/list_awskeymanagementservice.md#list_awselementalmediaconnect.html#awselementalmediaconnect-resources-for-iam-policies "../../../IAM/latest/UserGuide/list_awskeymanagementservice.md#list_awselementalmediaconnect.html#awselementalmediaconnect-resources-for-iam-policies") in the _IAM User Guide_. To
learn with which actions you can specify the ARN of each resource, see
[Actions Defined by AWS Elemental MediaConnect](../../../IAM/latest/UserGuide/list_awselementalmediaconnect.md#awselementalmediaconnect-actions-as-permissions "../../../IAM/latest/UserGuide/list_awselementalmediaconnect.md#awselementalmediaconnect-actions-as-permissions").

### Condition keys

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition
operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md"), such as equals or less than, to match the condition in the
policy with values in the request. To see all AWS global
condition keys, see [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

### Examples

To view examples of MediaConnect identity-based policies, see [AWS Elemental MediaConnect
identity-based policy examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## MediaConnect resource-based policies

AWS Elemental MediaConnect does not support resource-based policies.

## Authorization based on

MediaConnect tags

AWS Elemental MediaConnect does not support tagging resources or controlling access based on
tags.

## MediaConnect IAM

roles

An [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") is an entity within
your AWS account that has specific permissions.

### Using temporary

credentials with MediaConnect

You can use temporary credentials to sign in with federation, assume an IAM
role, or to assume a cross-account role. You obtain temporary security
credentials by calling AWS STS API operations such as [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") or [GetFederationToken](../../../STS/latest/APIReference/API_GetFederationToken.md "../../../STS/latest/APIReference/API_GetFederationToken.md").

MediaConnect supports using temporary credentials.

### Service-linked roles

[Service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role") allow AWS services to access resources in
other services to complete an action on your behalf. Service-linked roles appear
in your IAM account and are owned by the service. An IAM administrator can
view but not edit the permissions for service-linked roles.

MediaConnect does not support service-linked roles.

### Service

roles

This feature allows a service to assume a [service role](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-role") on your behalf. This role allows the service to access
resources in other services to complete an action on your behalf. Service roles
appear in your IAM account and are owned by the account. This means that an
IAM administrator can change the permissions for this role. However, doing so
might break the functionality of the service.

MediaConnect does not support service roles.
