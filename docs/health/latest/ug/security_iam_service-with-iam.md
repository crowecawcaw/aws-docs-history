# How AWS Health works with

IAM

Before you use IAM to manage access to AWS Health, you should understand what
IAM features are available to use with AWS Health. To get a high-level view of how
AWS Health and other AWS services work with IAM, see [AWS Services That
Work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

###### Topics

- [AWS Health
  identity-based policies](#security_iam_service-with-iam-id-based-policies "#security_iam_service-with-iam-id-based-policies")
- [AWS Health
  resource-based policies](#security_iam_service-with-iam-resource-based-policies "#security_iam_service-with-iam-resource-based-policies")
- [Authorization based on
  AWS Health tags](#security_iam_service-with-iam-tags "#security_iam_service-with-iam-tags")
- [AWS Health IAM
  roles](#security_iam_service-with-iam-roles "#security_iam_service-with-iam-roles")

## AWS Health

identity-based policies

With IAM identity-based policies, you can specify allowed or denied actions and
resources as well as the conditions under which actions are allowed or denied.
AWS Health supports specific actions, resources, and condition keys. To learn
about all of the elements that you use in a JSON policy, see [IAM JSON Policy Elements
Reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the _IAM User Guide_.

### Actions

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the
actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

Policy actions in AWS Health use the following prefix before the action:
`health:`. For example, to grant someone permission to view
detailed information about specified events with the [DescribeEventDetails](../APIReference/API_DescribeEventDetails.md "../APIReference/API_DescribeEventDetails.md") API operation, you include the
`heath:DescribeEventDetails` action in the policy.

Policy statements must include an `Action` or `NotAction`
element. AWS Health defines its own set of actions that describe tasks that you
can perform with this service.

To specify multiple actions in a single statement, separate them with commas as
follows.

```
"Action": [
      "health:*action1*",
      "health:*action2*"
```

You can specify multiple actions using wildcards (\*). For example, to specify all
actions that begin with the word `Describe`, include the following
action.

```
`"Action": "health:Describe*"`
```

To see a list of AWS Health actions, see [Actions Defined by AWS Health](../../../IAM/latest/UserGuide/list_awshealthapisandnotifications.md#awshealthapisandnotifications-actions-as-permissions "../../../IAM/latest/UserGuide/list_awshealthapisandnotifications.md#awshealthapisandnotifications-actions-as-permissions") in the
_IAM User Guide_.

### Resources

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md"). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

An AWS Health event has the following Amazon Resource Name (ARN) format.

```
arn:${Partition}:health:*::event/`service`/`event-type-code`/`event-ID`
```

For example, to specify the
`EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-DEF456` event in your
statement, use the following ARN.

```
"Resource": "arn:aws:health:*::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-DEF456"
```

To specify all AWS Health events for Amazon EC2 that belong to a specific account, use
the wildcard (\*).

```
"Resource": "arn:aws:health:*::event/EC2/*/*"
```

For more information about the format of ARNs, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md").

Some AWS Health actions can't be performed on a specific resource. In those
cases, you must use the wildcard (\*).

```
"Resource": "*"
```

AWS Health API operations can involve multiple resources. For example, the [DescribeEvents](../APIReference/API_DescribeEvents.md "../APIReference/API_DescribeEvents.md") operation returns information about events that meet a
specified filter criteria. This means that an IAM user must have permissions to
view this event.

To specify multiple resources in a single statement, separate the ARNs with
commas.

```
"Resource": [
      "*resource1*",
      "*resource2*"
```

AWS Health supports only resource-level permissions for health events and only
for the [DescribeAffectedEntities](../APIReference/API_DescribeAffectedEntities.md "../APIReference/API_DescribeAffectedEntities.md") and [DescribeEventDetails](../APIReference/API_DescribeEventDetails.md "../APIReference/API_DescribeEventDetails.md") API operations. For more information, see [Resource- and action-based
conditions](security_iam_id-based-policy-examples.md#resource-action-based-conditions "security_iam_id-based-policy-examples.md#resource-action-based-conditions").

To see a list of AWS Health resource types and their ARNs, see
[Resources Defined by AWS Health](../../../IAM/latest/UserGuide/list_awshealthapisandnotifications.md#awshealthapisandnotifications-resources-for-iam-policies "../../../IAM/latest/UserGuide/list_awshealthapisandnotifications.md#awshealthapisandnotifications-resources-for-iam-policies") in the _IAM User Guide_. To learn
with which actions you can specify the ARN of each resource, see
[Actions Defined by AWS Health](../../../IAM/latest/UserGuide/list_awshealthapisandnotifications.md#awshealthapisandnotifications-actions-as-permissions "../../../IAM/latest/UserGuide/list_awshealthapisandnotifications.md#awshealthapisandnotifications-actions-as-permissions").

### Condition keys

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition
operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md"), such as equals or less than, to match the condition in the
policy with values in the request. To see all AWS global
condition keys, see [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

AWS Health defines its own set of condition keys and also supports using
some global condition keys. To see all AWS global condition keys, see [AWS Global Condition
Context Keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the _IAM User Guide_.

The [DescribeAffectedEntities](../APIReference/API_DescribeAffectedEntities.md "../APIReference/API_DescribeAffectedEntities.md") and [DescribeEventDetails](../APIReference/API_DescribeEventDetails.md "../APIReference/API_DescribeEventDetails.md") API operations support the
`health:eventTypeCode` and `health:service` condition
keys.

To see a list of AWS Health condition keys, see [Condition Keys for AWS Health](../../../IAM/latest/UserGuide/list_awshealthapisandnotifications.md#awshealthapisandnotifications-policy-keys "../../../IAM/latest/UserGuide/list_awshealthapisandnotifications.md#awshealthapisandnotifications-policy-keys")
in the _IAM User Guide_. To learn with which actions and
resources you can use a condition key, see [Actions Defined by AWS Health](../../../IAM/latest/UserGuide/list_awshealthapisandnotifications.md#awshealthapisandnotifications-actions-as-permissions "../../../IAM/latest/UserGuide/list_awshealthapisandnotifications.md#awshealthapisandnotifications-actions-as-permissions").

### Examples

To view examples of AWS Health identity-based policies, see [AWS Health identity-based
policy examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## AWS Health

resource-based policies

Resource-based policies are JSON policy documents that specify what actions a
specified principal can perform on the AWS Health resource and under what
conditions. AWS Health supports resource-based permissions policies for health events.
Resource-based policies let you grant usage permission to other accounts on a
per-resource basis. You can also use a resource-based policy to allow an AWS service
to access your AWS Health events.

To enable cross-account access, you can specify an entire account or IAM entities
in another account as the [principal in a
resource-based policy](../../../IAM/latest/UserGuide/reference_policies_elements_principal.md "../../../IAM/latest/UserGuide/reference_policies_elements_principal.md"). Adding a cross-account principal to a resource-based
policy is only half of establishing the trust relationship. When the principal and the
resource are in different AWS accounts, you must also grant the principal entity
permission to access the resource. Grant permission by attaching an identity-based
policy to the entity. However, if a resource-based policy grants access to a principal
in the same account, no additional identity-based policy is required. For more
information, see [How
IAM Roles Differ from Resource-based Policies](../../../IAM/latest/UserGuide/id_roles_compare-resource-policies.md "../../../IAM/latest/UserGuide/id_roles_compare-resource-policies.md") in the
_IAM User Guide_.

AWS Health supports only resource-based policies for the [DescribeAffectedEntities](../APIReference/API_DescribeAffectedEntities.md "../APIReference/API_DescribeAffectedEntities.md") and [DescribeEventDetails](../APIReference/API_DescribeEventDetails.md "../APIReference/API_DescribeEventDetails.md") API operations. You can specify these actions in a
policy to define which principal entities (accounts, users, roles, and federated users)
can perform actions on the AWS Health event.

### Examples

To view examples of AWS Health resource-based policies, see [Resource- and action-based
conditions](security_iam_id-based-policy-examples.md#resource-action-based-conditions "security_iam_id-based-policy-examples.md#resource-action-based-conditions").

## Authorization based on

AWS Health tags

AWS Health doesn't support tagging resources or controlling access based on
tags.

## AWS Health IAM

roles

An [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") is an entity within
your AWS account that has specific permissions.

### Using temporary

credentials with AWS Health

You can use temporary credentials to sign in with federation, assume an IAM
role, or to assume a cross-account role. You obtain temporary security credentials by
calling AWS STS API operations such as [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") or [GetFederationToken](../../../STS/latest/APIReference/API_GetFederationToken.md "../../../STS/latest/APIReference/API_GetFederationToken.md").

AWS Health supports using temporary credentials.

### Service-linked

roles

[Service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role") allow AWS services to access resources in other
services to complete an action on your behalf. Service-linked roles appear in your
IAM account and are owned by the service. An IAM administrator can view but not
edit the permissions for service-linked roles.

AWS Health supports service-linked roles to integrate with AWS Organizations. The
service-linked role is named `AWSServiceRoleForHealth_Organizations`.
Attached to the role is the [Health_OrganizationsServiceRolePolicy](https://console.aws.amazon.com//iam/home?#/policies/arn:aws:iam::aws:policy/aws-service-role/Health_OrganizationsServiceRolePolicy "https://console.aws.amazon.com//iam/home?#/policies/arn:aws:iam::aws:policy/aws-service-role/Health_OrganizationsServiceRolePolicy") AWS managed policy. The AWS
managed policy allows AWS Health to access health events from other AWS accounts
in the organization.

You can use the [EnableHealthServiceAccessForOrganization](../APIReference/API_EnableHealthServiceAccessForOrganization.md "../APIReference/API_EnableHealthServiceAccessForOrganization.md") operation to create the
service-linked role in the account. However, if you want to disable this feature, you
must first call the [DisableHealthServiceAccessForOrganization](../APIReference/API_DisableHealthServiceAccessForOrganization.md "../APIReference/API_DisableHealthServiceAccessForOrganization.md") operation. You can then delete
the role through the IAM console, IAM API, or AWS Command Line Interface (AWS CLI). For more
information, see [Using service-linked
roles](../../../IAM/latest/UserGuide/using-service-linked-roles.md "../../../IAM/latest/UserGuide/using-service-linked-roles.md") in the _IAM User Guide_.

For more information, see [Aggregating AWS Health events across accounts](aggregate-events.md "aggregate-events.md").

### Service roles

This feature allows a service to assume a [service
role](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-role") on your behalf. This role allows the service to access resources in
other services to complete an action on your behalf. Service roles appear in your
IAM account and are owned by the account. This means that an IAM administrator
can change the permissions for this role. However, doing so might break the
functionality of the service.

AWS Health doesn't support service roles.
