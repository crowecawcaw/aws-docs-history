# How AWS Infrastructure Composer works with IAM

AWS Infrastructure Composer requires, at minimum, read-only access to the AWS Management Console. Any user with this
authorization can use all features of Infrastructure Composer. Granular access to specific features of
Infrastructure Composer is not supported.

When you deploy your project template and files to AWS CloudFormation, you will need the necessary
permissions to be in place. To learn more, see [Controlling access with
AWS Identity and Access Management](../../../AWSCloudFormation/latest/UserGuide/using-iam-template.md "../../../AWSCloudFormation/latest/UserGuide/using-iam-template.md") in the _AWS CloudFormation User Guide_.

The following table shows what IAM features can be used with AWS Infrastructure Composer.

| IAM feature                                                                                                                                              | Infrastructure Composer support |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| [Identity-based<br>policies](#security_iam_service-with-iam-id-based-policies "#security_iam_service-with-iam-id-based-policies")                        | No                              |
| [Resource-based policies](#security_iam_service-with-iam-resource-based-policies "#security_iam_service-with-iam-resource-based-policies")               | No                              |
| [Policy<br>actions](#security_iam_service-with-iam-id-based-policies-actions "#security_iam_service-with-iam-id-based-policies-actions")                 | No                              |
| [Policy<br>resources](#security_iam_service-with-iam-id-based-policies-resources "#security_iam_service-with-iam-id-based-policies-resources")           | No                              |
| [Policy condition keys](#security_iam_service-with-iam-id-based-policies-conditionkeys "#security_iam_service-with-iam-id-based-policies-conditionkeys") | No                              |
| [ACLs](#security_iam_service-with-iam-acls "#security_iam_service-with-iam-acls")                                                                        | No                              |
| [ABAC (tags in<br>policies)](#security_iam_service-with-iam-tags "#security_iam_service-with-iam-tags")                                                  | No                              |
| [Temporary<br>credentials](#security_iam_service-with-iam-roles-tempcreds "#security_iam_service-with-iam-roles-tempcreds")                              | Yes                             |
| [Principal<br>permissions](#security_iam_service-with-iam-principal-permissions "#security_iam_service-with-iam-principal-permissions")                  | No                              |
| [Service<br>roles](#security_iam_service-with-iam-roles-service "#security_iam_service-with-iam-roles-service")                                          | No                              |
| [Service-linked roles](#security_iam_service-with-iam-roles-service-linked "#security_iam_service-with-iam-roles-service-linked")                        | No                              |

To get a high-level view of how Infrastructure Composer and other AWS services work with most IAM
features, see [AWS
services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

## Identity-based policies

for Infrastructure Composer

**Supports identity-based policies:**

No

Identity-based policies are JSON permissions policy documents that you can attach to an identity, such as an IAM user, group of users, or role. These
policies control what actions users and roles can perform, on which resources, and under what conditions. To learn how to create an identity-based
policy, see [Define custom IAM permissions with customer managed policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the
_IAM User Guide_.

With IAM identity-based policies, you can specify allowed or denied actions and
resources as well as the conditions under which actions are allowed or denied. To learn about all of the elements that you can use in a
JSON policy, see [IAM JSON
policy elements reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the
_IAM User Guide_.

## Resource-based

policies within Infrastructure Composer

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

## Policy actions for

Infrastructure Composer

**Supports policy actions:**

No

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the
actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

To see a list of Infrastructure Composer actions, see [Actions Defined by AWS Infrastructure Composer](../../../IAM/latest/UserGuide/list_your_service.md#your_service-actions-as-permissions "../../../IAM/latest/UserGuide/list_your_service.md#your_service-actions-as-permissions") in the
_Service Authorization Reference_.

## Policy resources

for Infrastructure Composer

**Supports policy resources:**

No

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md"). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

To see a list of Infrastructure Composer resource types and their ARNs, see [Resources Defined by AWS Infrastructure Composer](../../../IAM/latest/UserGuide/list_your_service.md#your_service-resources-for-iam-policies "../../../IAM/latest/UserGuide/list_your_service.md#your_service-resources-for-iam-policies") in
the _Service Authorization Reference_. To learn with which actions you can specify the
ARN of each resource, see [Actions Defined by AWS Infrastructure Composer](../../../IAM/latest/UserGuide/list_your_service.md#your_service-actions-as-permissions "../../../IAM/latest/UserGuide/list_your_service.md#your_service-actions-as-permissions") .

## Policy

condition keys for Infrastructure Composer

**Supports service-specific policy condition keys:**

No

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition
operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md"), such as equals or less than, to match the condition in the
policy with values in the request. To see all AWS global
condition keys, see [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

To see a list of Infrastructure Composer condition keys, see [Condition Keys for AWS Infrastructure Composer](../../../IAM/latest/UserGuide/list_your_service.md#your_service-policy-keys "../../../IAM/latest/UserGuide/list_your_service.md#your_service-policy-keys") in the
_Service Authorization Reference_. To learn with which actions and resources you can
use a condition key, see [Actions Defined by AWS Infrastructure Composer](../../../IAM/latest/UserGuide/list_your_service.md#your_service-actions-as-permissions "../../../IAM/latest/UserGuide/list_your_service.md#your_service-actions-as-permissions") .

## ACLs in Infrastructure Composer

**Supports ACLs:**

No

Access control lists (ACLs) control which principals (account members, users, or roles) have permissions to access a resource. ACLs are
similar to resource-based policies, although they do not use the JSON policy document format.

## ABAC with Infrastructure Composer

**Supports ABAC (tags in policies):**

No

Attribute-based access control (ABAC) is an authorization strategy that defines permissions
based on attributes called tags. You can attach tags to IAM entities and AWS resources, then design ABAC policies to allow operations when the principal's tag matches the tag on the resource.

To control access based on tags, you provide tag information in the [condition element](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") of a policy using the `aws:ResourceTag/`key-name``, 
 `aws:RequestTag/`key-name``, or `aws:TagKeys` condition keys.

If a service supports all three condition keys for every resource type, then the value is **Yes** for the service. If a service supports all three condition keys for only some resource types, then the value is **Partial**.

For more information about ABAC, see [Define permissions with ABAC authorization](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") in the _IAM User Guide_. To view a tutorial with steps for setting up ABAC, see
[Use attribute-based access control (ABAC)](../../../IAM/latest/UserGuide/tutorial_attribute-based-access-control.md "../../../IAM/latest/UserGuide/tutorial_attribute-based-access-control.md") in the _IAM User Guide_.

## Using temporary credentials

with Infrastructure Composer

**Supports temporary credentials:**

Yes

Temporary credentials provide short-term access to AWS resources and are automatically created when you use federation or switch roles. AWS recommends that you
dynamically generate temporary credentials instead of using long-term access keys. For
more information, see [Temporary
security credentials in IAM](../../../IAM/latest/UserGuide/id_credentials_temp.md "../../../IAM/latest/UserGuide/id_credentials_temp.md") and [AWS services
that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

You can use temporary credentials to access Infrastructure Composer through the AWS Management Console. For an
example, see [Enabling
custom identity broker access to the AWS console](../../../IAM/latest/UserGuide/id_roles_providers_enable-console-custom-url.md "../../../IAM/latest/UserGuide/id_roles_providers_enable-console-custom-url.md") in the
_IAM User Guide_.

## Cross-service

principal permissions for Infrastructure Composer

**Supports forward access sessions (FAS):**

No

Forward access sessions (FAS) use the permissions of the principal calling an AWS service, combined with the requesting AWS service to make requests to downstream services. For policy details
when making FAS requests, see [Forward access sessions](../../../IAM/latest/UserGuide/access_forward_access_sessions.md "../../../IAM/latest/UserGuide/access_forward_access_sessions.md").

## Service roles for

Infrastructure Composer

**Supports service roles:**

No

A service role is an [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") that a service assumes to perform
actions on your behalf. An IAM administrator can create, modify, and delete a service role from within IAM. For
more information, see [Create a role to delegate permissions to an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the _IAM User Guide_.

###### Warning

Changing the permissions for a service role might break Infrastructure Composer functionality. Edit
service roles only when Infrastructure Composer provides guidance to do so.

## Service-linked roles

for Infrastructure Composer

**Supports service-linked roles:**

No

A service-linked role is a type of service role that is linked to an AWS service. The service can assume the role to perform an action on your behalf.
Service-linked roles appear in your AWS account and are owned by the service. An IAM administrator can view,
but not edit the permissions for service-linked roles.

For details about creating or managing service-linked roles, see [AWS services that
work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md"). Find a service in the table that includes a `Yes` in
the **Service-linked role** column. Choose the **Yes**
link to view the service-linked role documentation for that service.
