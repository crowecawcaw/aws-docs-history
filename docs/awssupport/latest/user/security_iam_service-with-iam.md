# How AWS Support works with

IAM

Before you use IAM to manage access to Support, you should understand what
IAM features are available to use with Support. To get a high-level view of how
Support and other AWS services work with IAM, see [AWS services that
work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

For information about how to manage access for Support using IAM, see
[Manage access for Support](accessing-support.md#iam "accessing-support.md#iam").

###### Topics

- [Support
  identity-based policies](#security_iam_service-with-iam-id-based-policies "#security_iam_service-with-iam-id-based-policies")
- [Support IAM
  roles](#security_iam_service-with-iam-roles "#security_iam_service-with-iam-roles")

## Support

identity-based policies

With IAM identity-based policies, you can specify allowed or denied actions and
resources as well as the conditions under which actions are allowed or denied.
Support supports specific actions. To learn about the elements that you use in
a JSON policy, see [IAM
JSON policy elements reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the
_IAM User Guide_.

### Actions

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the
actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

Policy actions in Support use
the following prefix before the action: `support:`. For
example, to grant someone permission to run an Amazon EC2 instance with the Amazon EC2
`RunInstances` API operation, you include the
`ec2:RunInstances` action in their policy. Policy statements must
include either an `Action` or `NotAction` element.
Support defines its own set of actions that describe tasks that you can
perform with this service.

To specify multiple actions in a single statement, separate them with commas as
follows:

```
"Action": [
      "ec2:*action1*",
      "ec2:*action2*"
```

You can specify multiple actions using wildcards (\*). For example, to specify all
actions that begin with the word `Describe`, include the following
action:

```
`"Action": "ec2:Describe*"`
```

To see a list of Support actions, see [Actions Defined by AWS Support](../../../IAM/latest/UserGuide/list_awssupport.md#awssupport-actions-as-permissions "../../../IAM/latest/UserGuide/list_awssupport.md#awssupport-actions-as-permissions") in the
_IAM User Guide_.

### Examples

To view examples of Support identity-based policies, see [AWS Support identity-based
policy examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Support IAM

roles

An [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") is an entity within
your AWS account that has specific permissions.

### Using temporary

credentials with Support

You can use temporary credentials to sign in with federation, assume an IAM
role, or to assume a cross-account role. You obtain temporary security credentials by
calling AWS STS API operations such as [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") or [GetFederationToken](../../../STS/latest/APIReference/API_GetFederationToken.md "../../../STS/latest/APIReference/API_GetFederationToken.md").

Support supports using temporary credentials.

### Service-linked

roles

[Service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role") allow AWS services to access resources in other
services to complete an action on your behalf. Service-linked roles appear in your
IAM account and are owned by the service. An IAM administrator can view but not
edit the permissions for service-linked roles.

Support supports service-linked roles. For details about creating or
managing Support service-linked roles, see [Using service-linked roles for
AWS Support](using-service-linked-roles-sup.md "using-service-linked-roles-sup.md").

### Service roles

This feature allows a service to assume a [service
role](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-role") on your behalf. This role allows the service to access resources in
other services to complete an action on your behalf. Service roles appear in your
IAM account and are owned by the account. This means that an IAM administrator
can change the permissions for this role. However, doing so might break the
functionality of the service.

Support supports service roles.
