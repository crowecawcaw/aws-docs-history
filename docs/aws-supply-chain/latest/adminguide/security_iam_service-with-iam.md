# How AWS Supply Chain works with IAM

Before you use IAM to manage access to AWS Supply Chain, learn what IAM features are
available to use with AWS Supply Chain.

| IAM features you can use with AWS Supply Chain                                                                                                           | IAM feature | AWS Supply Chain support |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ------------------------ |
| [Identity-based policies](#security_iam_service-with-iam-id-based-policies "#security_iam_service-with-iam-id-based-policies")                           | Yes         |
| [Resource-based policies](#security_iam_service-with-iam-resource-based-policies "#security_iam_service-with-iam-resource-based-policies")               | No          |
| [Policy actions](#security_iam_service-with-iam-id-based-policies-actions "#security_iam_service-with-iam-id-based-policies-actions")                    | Yes         |
| [Policy resources](#security_iam_service-with-iam-id-based-policies-resources "#security_iam_service-with-iam-id-based-policies-resources")              | Yes         |
| [Policy condition keys](#security_iam_service-with-iam-id-based-policies-conditionkeys "#security_iam_service-with-iam-id-based-policies-conditionkeys") | Yes         |
| [Temporary<br>credentials](#security_iam_service-with-iam-roles-tempcreds "#security_iam_service-with-iam-roles-tempcreds")                              | Yes         |
| [Forward access sessions (FAS)](#security_iam_service-with-iam-principal-permissions "#security_iam_service-with-iam-principal-permissions")             | Yes         |
| [Service<br>roles](#security_iam_service-with-iam-roles-service "#security_iam_service-with-iam-roles-service")                                          | Yes         |
| [Service-linked roles](#security_iam_service-with-iam-roles-service-linked "#security_iam_service-with-iam-roles-service-linked")                        | No          |

To get a high-level view of how AWS Supply Chain and other AWS services work with most IAM
features, see [AWS services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the
_IAM User Guide_.

## Identity-based

policies for AWS Supply Chain

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

###

Identity-based policy examples for AWS Supply Chain

To view examples of AWS Supply Chain identity-based policies, see [Identity-based policy examples for
AWS Supply Chain](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Resource-based

policies within AWS Supply Chain

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

## Policy actions

for AWS Supply Chain

**Supports policy actions:**

Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the
actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

Policy actions in AWS Supply Chain use the following prefix before the action:

```
scn
```

To specify multiple actions in a single statement, separate them with commas.

```
"Action": [
      "scn:`action1`",
      "scn:`action2`"
         ]
```

To view examples of AWS Supply Chain identity-based policies, see [Identity-based policy examples for
AWS Supply Chain](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Policy

resources for AWS Supply Chain

**Supports policy resources:**

Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md"). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

To view examples of AWS Supply Chain identity-based policies, see [Identity-based policy examples for
AWS Supply Chain](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Policy

condition keys for AWS Supply Chain

**Supports service-specific policy condition keys:**

Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition
operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md"), such as equals or less than, to match the condition in the
policy with values in the request. To see all AWS global
condition keys, see [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

To view examples of AWS Supply Chain identity-based policies, see [Identity-based policy examples for
AWS Supply Chain](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Using temporary

credentials with AWS Supply Chain

**Supports temporary credentials:**

Yes

Temporary credentials provide short-term access to AWS resources and are automatically created when you use federation or switch roles. AWS recommends that you
dynamically generate temporary credentials instead of using long-term access keys. For
more information, see [Temporary
security credentials in IAM](../../../IAM/latest/UserGuide/id_credentials_temp.md "../../../IAM/latest/UserGuide/id_credentials_temp.md") and [AWS services
that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

## Forward access

sessions for AWS Supply Chain

**Supports forward access sessions (FAS):**

Yes

Forward access sessions (FAS) use the permissions of the principal calling an AWS service, combined with the requesting AWS service to make requests to downstream services. For policy details
when making FAS requests, see [Forward access sessions](../../../IAM/latest/UserGuide/access_forward_access_sessions.md "../../../IAM/latest/UserGuide/access_forward_access_sessions.md").

## Service roles for

AWS Supply Chain

**Supports service roles:**

Yes

A service role is an [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") that a service assumes to perform
actions on your behalf. An IAM administrator can create, modify, and delete a service role from within IAM. For
more information, see [Create a role to delegate permissions to an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the _IAM User Guide_.

###### Warning

Changing the permissions for a service role might break AWS Supply Chain functionality.
Edit service roles only when AWS Supply Chain provides guidance to do so.

## Service-linked

roles for AWS Supply Chain

**Supports service-linked roles:**

No

A service-linked role is a type of service role that is linked to an AWS service. The service can assume the role to perform an action on your behalf.
Service-linked roles appear in your AWS account and are owned by the service. An IAM administrator can view,
but not edit the permissions for service-linked roles.

For details about creating or managing service-linked roles, see [AWS services
that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md"). Find a service in the table that includes a
`Yes` in the **Service-linked role** column. Choose the
**Yes** link to view the service-linked role documentation for that
service.
