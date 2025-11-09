AWS Application Discovery Service is no longer open to new customers. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](application-discovery-service-availability-change.md "application-discovery-service-availability-change.md").

# How AWS Application Discovery Service works with

IAM

Before you use IAM to manage access to Application Discovery Service, you should understand what
IAM features are available to use with Application Discovery Service. To get a high-level view of how
Application Discovery Service and other AWS services work with IAM, see [AWS Services That
Work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

###### Topics

- [Application Discovery Service
  identity-based policies](#security_iam_service-with-iam-id-based-policies "#security_iam_service-with-iam-id-based-policies")
- [Application Discovery Service
  resource-based policies](#security_iam_service-with-iam-resource-based-policies "#security_iam_service-with-iam-resource-based-policies")
- [Authorization based on
  Application Discovery Service tags](#security_iam_service-with-iam-tags "#security_iam_service-with-iam-tags")
- [Application Discovery Service IAM
  roles](#security_iam_service-with-iam-roles "#security_iam_service-with-iam-roles")

## Application Discovery Service

identity-based policies

With IAM identity-based policies, you can specify allowed or denied actions and
resources as well as the conditions under which actions are allowed or denied.
Application Discovery Service supports specific actions, resources, and condition keys. To learn
about all of the elements that you use in a JSON policy, see [IAM JSON Policy Elements
Reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the _IAM User Guide_.

### Actions

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the
actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

Policy actions in Application Discovery Service use the following prefix before the action:
`discovery:`. Policy statements must include either an
`Action` or `NotAction` element. Application Discovery Service defines
its own set of actions that describe tasks that you can perform with this
service.

To specify multiple actions in a single statement, separate them with commas as
follows:

```
"Action": [
      "discovery:*action1*",
      "discovery:*action2*"
```

You can specify multiple actions using wildcards (\*). For example, to specify all
actions that begin with the word `Describe`, include the following
action:

```
`"Action": "discovery:Describe*"`
```

To see a list of Application Discovery Service actions, see [Actions Defined by AWS Application Discovery Service](../../../IAM/latest/UserGuide/list_applicationdiscovery.md#awskeymanagementservice-actions-as-permissions "../../../IAM/latest/UserGuide/list_applicationdiscovery.md#awskeymanagementservice-actions-as-permissions") in the
_IAM User Guide_.

### Resources

Application Discovery Service does not support specifying resource ARNs in a policy. To separate access, create and use separate AWS accounts.

### Condition keys

Application Discovery Service does not provide any service-specific condition keys, but it does
support using some global condition keys. To see all AWS global condition keys, see
[AWS Global
Condition Context Keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

### Examples

To view examples of Application Discovery Service identity-based policies, see [AWS Application Discovery Service identity-based
policy examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Application Discovery Service

resource-based policies

Application Discovery Service does not support resource-based policies.

## Authorization based on

Application Discovery Service tags

Application Discovery Service does not support tagging resources or controlling access based on
tags.

## Application Discovery Service IAM

roles

An [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") is an entity within
your AWS account that has specific permissions.

### Using temporary

credentials with Application Discovery Service

Application Discovery Service does not support using temporary credentials.

### Service-linked

roles

[Service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role") allow AWS services to access resources in other
services to complete an action on your behalf. Service-linked roles appear in your
IAM account and are owned by the service. An IAM administrator can view but not
edit the permissions for service-linked roles.

Application Discovery Service supports service-linked roles. For details about creating or
managing Application Discovery Service service-linked roles, see [Using service-linked roles for Application Discovery Service](using-service-linked-roles.md "using-service-linked-roles.md").

### Service roles

This feature allows a service to assume a [service
role](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-role") on your behalf. This role allows the service to access resources in
other services to complete an action on your behalf. Service roles appear in your
IAM account and are owned by the account. This means that an IAM administrator
can change the permissions for this role. However, doing so might break the
functionality of the service.

Application Discovery Service supports service roles.
