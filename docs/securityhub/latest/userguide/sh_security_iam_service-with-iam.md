# How Security Hub works with IAM

Before you use AWS Identity and Access Management (IAM) to manage access to AWS Security Hub, learn which IAM
features are available to use with Security Hub.

| IAM features you can use with AWS Security Hub                                                                                                                 | IAM feature | Security Hub support |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | -------------------- |
| [Identity-based policies](#sh_security_iam_service-with-iam-id-based-policies "#sh_security_iam_service-with-iam-id-based-policies")                           | Yes         |
| [Resource-based policies](#sh_security_iam_service-with-iam-resource-based-policies "#sh_security_iam_service-with-iam-resource-based-policies")               | No          |
| [Policy actions](#sh_security_iam_service-with-iam-id-based-policies-actions "#sh_security_iam_service-with-iam-id-based-policies-actions")                    | Yes         |
| [Policy resources](#sh_security_iam_service-with-iam-id-based-policies-resources "#sh_security_iam_service-with-iam-id-based-policies-resources")              | No          |
| [Policy condition keys](#sh_security_iam_service-with-iam-id-based-policies-conditionkeys "#sh_security_iam_service-with-iam-id-based-policies-conditionkeys") | Yes         |
| [Access control lists (ACLs)](#sh_security_iam_service-with-iam-acls "#sh_security_iam_service-with-iam-acls")                                                 | No          |
| [Attribute-based access control (ABAC) – tags in<br>policies](#sh_security_iam_service-with-iam-tags "#sh_security_iam_service-with-iam-tags")                 | Yes         |
| [Temporary<br>credentials](#sh_security_iam_service-with-iam-roles-tempcreds "#sh_security_iam_service-with-iam-roles-tempcreds")                              | Yes         |
| [Forward access<br>sessions (FAS)](#sh_security_iam_service-with-iam-principal-permissions "#sh_security_iam_service-with-iam-principal-permissions")          | Yes         |
| [Service<br>roles](#sh_security_iam_service-with-iam-roles-service "#sh_security_iam_service-with-iam-roles-service")                                          | No          |
| [Service-linked roles](#sh_security_iam_service-with-iam-roles-service-linked "#sh_security_iam_service-with-iam-roles-service-linked")                        | Yes         |

For a high-level view of how Security Hub and other AWS services work with most IAM features,
see [AWS services
that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

## Identity-based policies for Security Hub

**Supports identity-based policies:**

Yes

Identity-based policies are JSON permissions policy documents that you can attach to an identity, such as an IAM user, group of users, or role. These
policies control what actions users and roles can perform, on which resources, and under what conditions. To learn how to create an identity-based
policy, see [Define custom IAM permissions with customer managed policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the
_IAM User Guide_.

With IAM identity-based policies, you can specify allowed or denied actions and
resources as well as the conditions under which actions are allowed or denied. To learn about all of the elements that you can use in a
JSON policy, see [IAM JSON
policy elements reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the
_IAM User Guide_.

Security Hub supports identity-based policies. For more information, see [Identity-based policy examples for
AWS Security Hub](sh_security_iam_id-based-policy-examples.md "sh_security_iam_id-based-policy-examples.md").

## Resource-based policies for Security Hub

**Supports resource-based policies:**

No

Resource-based policies are JSON policy documents that you attach to a resource. Examples of resource-based policies are
IAM _role trust policies_ and Amazon S3 _bucket policies_. In services that support resource-based policies, service
administrators can use them to control access to a specific resource. For the resource where the policy is attached, the policy defines what actions
a specified principal can perform on that resource and under what conditions. You must [specify a principal](../../../IAM/latest/UserGuide/reference_policies_elements_principal.md "../../../IAM/latest/UserGuide/reference_policies_elements_principal.md") in a resource-based policy. Principals
can include accounts, users, roles, federated users, or AWS services.

To enable cross-account access, you can specify an entire account or IAM entities
in another account as the principal in a resource-based policy. For more information, see [Cross account resource access in IAM](../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md "../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md") in the
_IAM User Guide_.

Security Hub does not support resource-based policies. You can't attach an IAM policy directly to a Security Hub resource.

## Policy actions for Security Hub

**Supports policy actions:**

Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the
actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

Policy actions in Security Hub use the following prefix before the action:

```
securityhub:
```

For example, to grant a user permission to
enable Security Hub, which is an action that corresponds to the `EnableSecurityHubV2` operation of the
Security Hub API, include
the `securityhub:EnableSecurityHubV2` action in their policy.
Policy statements must include either an `Action` or
`NotAction` element. Security Hub defines its own set of actions that
describe tasks that you can perform with this service.

```
"Action": "securityhub:EnableSecurityHubV2"
```

To specify multiple actions in a single statement, separate them with commas. For example:

```
"Action": [
      "securityhub:EnableSecurityHubV2",
      "securityhub:CreateAutomationRuleV2"

```

You can also specify multiple actions using wildcards (\*). For example, to specify
all actions that begin with the word `Get`, include the following action:

```
"Action": "securityhub:Get*"
```

However, as a best practice, you should create policies that follow the principle of least
privilege. In other words, you should create policies that include only the permissions
that are required to perform a specific task.

For a list of Security Hub actions, see [Actions Defined by AWS Security Hub](../../../IAM/latest/UserGuide/list_awssecurityhub.md#awssecurityhub-actions-as-permissions "../../../IAM/latest/UserGuide/list_awssecurityhub.md#awssecurityhub-actions-as-permissions") in the
_Service Authorization Reference_. For examples of policies that specify Security Hub
actions, see [Identity-based policy examples for
AWS Security Hub](sh_security_iam_id-based-policy-examples.md "sh_security_iam_id-based-policy-examples.md").

## Policy resources for Security Hub

**Supports policy resources:**

No

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md"). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

Security Hub defines the following resource types:

- Hub
- Product
- Finding aggregator, also referred to as a _cross-Region aggregator_
- Automation rule

You can specify these types of resources in policies by using ARNs.

For a list of Security Hub resource types and the ARN syntax for each one, see
[Resources Defined by AWS Security Hub](../../../IAM/latest/UserGuide/list_awssecurityhub.md#awssecurityhub-resources-for-iam-policies "../../../IAM/latest/UserGuide/list_awssecurityhub.md#awssecurityhub-resources-for-iam-policies") in the _Service Authorization Reference_. To learn which
actions you can specify for each type of resource, see [Actions Defined by AWS Security Hub](../../../IAM/latest/UserGuide/list_awssecurityhub.md#awssecurityhub-actions-as-permissions "../../../IAM/latest/UserGuide/list_awssecurityhub.md#awssecurityhub-actions-as-permissions") in the
_Service Authorization Reference_. For examples of policies that specify resources, see
[Identity-based policy examples for
AWS Security Hub](sh_security_iam_id-based-policy-examples.md "sh_security_iam_id-based-policy-examples.md").

## Policy condition keys for Security Hub

**Supports service-specific policy condition keys:**

Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition
operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md"), such as equals or less than, to match the condition in the
policy with values in the request. To see all AWS global
condition keys, see [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

For a list of Security Hub condition keys, see [Condition Keys for AWS Security Hub](../../../IAM/latest/UserGuide/list_awssecurityhub.md#awssecurityhub-policy-keys "../../../IAM/latest/UserGuide/list_awssecurityhub.md#awssecurityhub-policy-keys") in the
_Service Authorization Reference_. To learn which actions and resources you can use
a condition key with, see [Actions Defined by AWS Security Hub](../../../IAM/latest/UserGuide/list_awssecurityhub.md#awssecurityhub-actions-as-permissions "../../../IAM/latest/UserGuide/list_awssecurityhub.md#awssecurityhub-actions-as-permissions"). For examples of policies that use
condition keys, see [Identity-based policy examples for
AWS Security Hub](sh_security_iam_id-based-policy-examples.md "sh_security_iam_id-based-policy-examples.md").

## Access control lists (ACLs) in Security Hub

**Supports ACLs:**

No

Access control lists (ACLs) control which principals (account members, users, or roles) have permissions to access a resource. ACLs are
similar to resource-based policies, although they do not use the JSON policy document format.

Security Hub doesn't support ACLs, which means you can't attach an ACL to a Security Hub
resource.

## Attribute-based access control (ABAC) with Security Hub

**Supports ABAC (tags in policies):**

Yes

Attribute-based access control (ABAC) is an authorization strategy that defines permissions
based on attributes called tags. You can attach tags to IAM entities and AWS resources, then design ABAC policies to allow operations when the principal's tag matches the tag on the resource.

To control access based on tags, you provide tag information in the [condition element](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") of a policy using the `aws:ResourceTag/`key-name``, 
 `aws:RequestTag/`key-name``, or `aws:TagKeys` condition keys.

If a service supports all three condition keys for every resource type, then the value is **Yes** for the service. If a service supports all three condition keys for only some resource types, then the value is **Partial**.

For more information about ABAC, see [Define permissions with ABAC authorization](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") in the _IAM User Guide_. To view a tutorial with steps for setting up ABAC, see
[Use attribute-based access control (ABAC)](../../../IAM/latest/UserGuide/tutorial_attribute-based-access-control.md "../../../IAM/latest/UserGuide/tutorial_attribute-based-access-control.md") in the _IAM User Guide_.

You can attach tags to Security Hub resources. You can also control
access to resources by providing tag information in the `Condition`
element of a policy.

For information about tagging Security Hub resources, see [Tagging
Security Hub
resources](tagging-resources.md "tagging-resources.md"). For an example of
an identity-based policy that controls access to a resource based on tags, see [Identity-based policy examples for
AWS Security Hub](sh_security_iam_id-based-policy-examples.md "sh_security_iam_id-based-policy-examples.md").

## Using temporary

credentials with Security Hub

**Supports temporary credentials:**

Yes

Temporary credentials provide short-term access to AWS resources and are automatically created when you use federation or switch roles. AWS recommends that you
dynamically generate temporary credentials instead of using long-term access keys. For
more information, see [Temporary
security credentials in IAM](../../../IAM/latest/UserGuide/id_credentials_temp.md "../../../IAM/latest/UserGuide/id_credentials_temp.md") and [AWS services
that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

You can use temporary credentials to sign in with federation, assume an IAM
role, or to assume a cross-account role. You obtain temporary security
credentials by calling AWS STS API operations such as [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") or [GetFederationToken](../../../STS/latest/APIReference/API_GetFederationToken.md "../../../STS/latest/APIReference/API_GetFederationToken.md").

Security Hub supports the use of temporary credentials.

## Forward access

sessions for Security Hub

**Supports forward access sessions (FAS):**

Yes

Forward access sessions (FAS) use the permissions of the principal calling an AWS service, combined with the requesting AWS service to make requests to downstream services. For policy details
when making FAS requests, see [Forward access sessions](../../../IAM/latest/UserGuide/access_forward_access_sessions.md "../../../IAM/latest/UserGuide/access_forward_access_sessions.md").

For example, Security Hub makes FAS requests to downstream AWS services when you
integrate Security Hub with AWS Organizations and when you designate the delegated Security Hub
administrator account for an organization in Organizations.

For other tasks, Security Hub uses a service-linked role to perform actions on your behalf. For
details about this role, see [Service-linked roles for AWS Security Hub](sh-using-service-linked-roles.md "sh-using-service-linked-roles.md").

## Service roles for Security Hub

Security Hub doesn't assume or use service roles. To perform actions on your behalf,
Security Hub uses a service-linked role. For details about this role, see [Service-linked roles for AWS Security Hub](sh-using-service-linked-roles.md "sh-using-service-linked-roles.md").

###### Warning

Changing the permissions for a service role may create operational issues with
your use of Security Hub. Edit service roles only when Security Hub provides guidance to do
so.

## Service-linked

roles for Security Hub

**Supports service-linked roles:**

Yes

A service-linked role is a type of service role that is linked to an AWS service. The service can assume the role to perform an action on your behalf.
Service-linked roles appear in your AWS account and are owned by the service. An IAM administrator can view,
but not edit the permissions for service-linked roles.

Security Hub uses a service-linked role to perform actions on your behalf. For details about this
role, see [Service-linked roles for AWS Security Hub](sh-using-service-linked-roles.md "sh-using-service-linked-roles.md").
