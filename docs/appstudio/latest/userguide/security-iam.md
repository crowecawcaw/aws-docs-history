# AWS App Studio and AWS Identity and Access Management (IAM)

In AWS App Studio, you manage access and permissions in the service by assigning groups in IAM Identity Center to the appropriate role in App Studio. The permissions
of the group members are determined by the role that is assigned, and not by configuring users, roles, or permissions directly in AWS Identity and Access Management (IAM). For more information
about managing access and permissions in App Studio, see [Managing access and roles in App Studio](managing-access-and-roles.md "managing-access-and-roles.md").

App Studio does integrate with IAM when verifying an instance for billing
purposes, and when connected to an AWS account to create and use resources in that AWS account. For information about connecting App Studio to other AWS services
for use in your applications, see [Connect to AWS services](add-connector-services.md "add-connector-services.md").

When you create an instance in App Studio, you must connect an AWS account as the billing and management account for your instance. To enable key features,
App Studio also creates [IAM service roles](../../../IAM/latest/UserGuide/id_roles.md#id_roles_terms-and-concepts "../../../IAM/latest/UserGuide/id_roles.md#id_roles_terms-and-concepts")
to provide the service with necessary permissions to carry out tasks on your behalf.

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control access
to AWS resources. IAM administrators control who can be _authenticated_ (signed in) and _authorized_
(have permissions) to use App Studio resources. IAM is an AWS service that you can
use with no additional charge.

###### Topics

- [Identity-based policies for App Studio](#security_iam_service-with-iam-id-based-policies "#security_iam_service-with-iam-id-based-policies")
- [Resource-based policies within App Studio](#security_iam_service-with-iam-resource-based-policies "#security_iam_service-with-iam-resource-based-policies")
- [Policy actions for App Studio](#security_iam_service-with-iam-id-based-policies-actions "#security_iam_service-with-iam-id-based-policies-actions")
- [Policy resources for App Studio](#security_iam_service-with-iam-id-based-policies-resources "#security_iam_service-with-iam-id-based-policies-resources")
- [Policy condition keys for App Studio](#security_iam_service-with-iam-id-based-policies-conditionkeys "#security_iam_service-with-iam-id-based-policies-conditionkeys")
- [ACLs in App Studio](#security_iam_service-with-iam-acls "#security_iam_service-with-iam-acls")
- [ABAC with App Studio](#security_iam_service-with-iam-tags "#security_iam_service-with-iam-tags")
- [Using temporary credentials with App Studio](#security_iam_service-with-iam-roles-tempcreds "#security_iam_service-with-iam-roles-tempcreds")
- [Cross-service principal permissions for App Studio](#security_iam_service-with-iam-principal-permissions "#security_iam_service-with-iam-principal-permissions")
- [Service roles for App Studio](#security_iam_service-with-iam-roles-service "#security_iam_service-with-iam-roles-service")
- [Service-linked roles for App Studio](#security_iam_service-with-iam-roles-service-linked "#security_iam_service-with-iam-roles-service-linked")
- [AWS managed policies for AWS App Studio](security-iam-awsmanpol.md "security-iam-awsmanpol.md")
- [Service-linked roles for App Studio](appstudio-service-linked-roles.md "appstudio-service-linked-roles.md")
- [Identity-based policy examples for AWS App Studio](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md")
  Before you use IAM to manage access to App Studio, learn what IAM features are
  available to use with App Studio.

| IAM features you can use with AWS App Studio                                                                                                             | IAM feature | App Studio support |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ------------------ |
| [Identity-based policies](#security_iam_service-with-iam-id-based-policies "#security_iam_service-with-iam-id-based-policies")                           | Yes         |
| [Resource-based policies](#security_iam_service-with-iam-resource-based-policies "#security_iam_service-with-iam-resource-based-policies")               | No          |
| [Policy actions](#security_iam_service-with-iam-id-based-policies-actions "#security_iam_service-with-iam-id-based-policies-actions")                    | Yes         |
| [Policy resources](#security_iam_service-with-iam-id-based-policies-resources "#security_iam_service-with-iam-id-based-policies-resources")              | Yes         |
| [Policy condition keys](#security_iam_service-with-iam-id-based-policies-conditionkeys "#security_iam_service-with-iam-id-based-policies-conditionkeys") | No          |
| [ACLs](#security_iam_service-with-iam-acls "#security_iam_service-with-iam-acls")                                                                        | No          |
| [ABAC (tags in<br>policies)](#security_iam_service-with-iam-tags "#security_iam_service-with-iam-tags")                                                  | No          |
| [Temporary<br>credentials](#security_iam_service-with-iam-roles-tempcreds "#security_iam_service-with-iam-roles-tempcreds")                              | Yes         |
| [Principal permissions](#security_iam_service-with-iam-principal-permissions "#security_iam_service-with-iam-principal-permissions")                     | Yes         |
| [Service<br>roles](#security_iam_service-with-iam-roles-service "#security_iam_service-with-iam-roles-service")                                          | Yes         |
| [Service-linked roles](#security_iam_service-with-iam-roles-service-linked "#security_iam_service-with-iam-roles-service-linked")                        | Yes         |

To get a high-level view of how App Studio and other AWS services work with most IAM
features, see [AWS services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the
_IAM User Guide_.

## Identity-based policies for App Studio

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

### Identity-based policy examples for App Studio

To view examples of App Studio identity-based policies, see [Identity-based policy examples for AWS App Studio](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Resource-based policies within App Studio

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

## Policy actions for App Studio

**Supports policy actions:**

Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the
actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

To see a list of App Studio actions, see [Actions Defined by AWS App Studio](../../../IAM/latest/UserGuide/list_awsappstudio.md#awsappstudio-actions-as-permissions "../../../IAM/latest/UserGuide/list_awsappstudio.md#awsappstudio-actions-as-permissions") in the
_Service Authorization Reference_.

Policy actions in App Studio use the following prefix before the action:

```
appstudio
```

To specify multiple actions in a single statement, separate them with commas.

```
"Action": [
      "appstudio:`action1`",
      "appstudio:`action2`"
         ]
```

The following statement lists all of the actions in App Studio:

## Policy resources for App Studio

**Supports policy resources:**

Yes

App Studio permissions only support a wildcard (`*`) in the `Resource` element of a policy.

## Policy condition keys for App Studio

**Supports service-specific policy condition keys:**

No

App Studio does not support policy condition keys.

## ACLs in App Studio

**Supports ACLs:**

No

Access control lists (ACLs) control which principals (account members, users, or roles) have permissions to access a resource. ACLs are
similar to resource-based policies, although they do not use the JSON policy document format.

## ABAC with App Studio

**Supports ABAC (tags in policies):**

No

App Studio does not support attribute-based access control (ABAC).

## Using temporary credentials with App Studio

**Supports temporary credentials:**

Yes

Temporary credentials provide short-term access to AWS resources and are automatically created when you use federation or switch roles. AWS recommends that you
dynamically generate temporary credentials instead of using long-term access keys. For
more information, see [Temporary
security credentials in IAM](../../../IAM/latest/UserGuide/id_credentials_temp.md "../../../IAM/latest/UserGuide/id_credentials_temp.md") and [AWS services
that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

## Cross-service principal permissions for App Studio

**Supports forward access sessions (FAS):**

Yes

Forward access sessions (FAS) use the permissions of the principal calling an AWS service, combined with the requesting AWS service to make requests to downstream services. For policy details
when making FAS requests, see [Forward access sessions](../../../IAM/latest/UserGuide/access_forward_access_sessions.md "../../../IAM/latest/UserGuide/access_forward_access_sessions.md").

## Service roles for App Studio

**Supports service roles:**

Yes

A service role is an [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") that a service assumes to perform
actions on your behalf. An IAM administrator can create, modify, and delete a service role from within IAM. For
more information, see [Create a role to delegate permissions to an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the _IAM User Guide_.

AWS App Studio uses [IAM service roles](../../../IAM/latest/UserGuide/id_roles.md#id_roles_terms-and-concepts "../../../IAM/latest/UserGuide/id_roles.md#id_roles_terms-and-concepts") for
some features to give App Studio permission to carry out tasks on your behalf. The console automatically creates service roles for supported features when
you set up App Studio.

###### Warning

Changing the permissions for a service role might break App Studio functionality.
Edit service roles only when App Studio provides guidance to do so.

## Service-linked roles for App Studio

**Supports service-linked roles:**

Yes

A service-linked role is a type of service role that is linked to an AWS service. The service can assume the role to perform an action on your behalf.
Service-linked roles appear in your AWS account and are owned by the service. An IAM administrator can view,
but not edit the permissions for service-linked roles.

For details about creating or managing service-linked roles, see [AWS services
that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md"). Find a service in the table that includes a
`Yes` in the **Service-linked role** column. Choose the
**Yes** link to view the service-linked role documentation for that
service.
