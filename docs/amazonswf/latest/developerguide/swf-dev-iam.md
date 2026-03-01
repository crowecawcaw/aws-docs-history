# Identity and Access Management in Amazon Simple Workflow Service

Access to Amazon SWF requires credentials that AWS can use to authenticate your requests. These
credentials must have permissions to access AWS resources, such as retrieving event data from other AWS resources..
The following sections provide details on how you can use [AWS Identity and Access Management (IAM)](../../../IAM/latest/UserGuide/introduction.md "../../../IAM/latest/UserGuide/introduction.md") and Amazon SWF to help secure your
resources by controlling access to them.

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control access
to AWS resources. IAM administrators control who can be _authenticated_ (signed in) and _authorized_
(have permissions) to use Amazon SWF resources. IAM is an AWS service that you can
use with no additional charge.

###### Topics

- [Audience](#security_iam_audience "#security_iam_audience")
- [Authenticating with identities](#security_iam_authentication "#security_iam_authentication")
- [Managing access using policies](#security_iam_access-manage "#security_iam_access-manage")
- [Access Control](#access-control-swf "#access-control-swf")
- [Policy actions for Amazon SWF](#security_iam_service-with-iam-id-based-policies-actions "#security_iam_service-with-iam-id-based-policies-actions")
- [Policy resources for Amazon SWF](#security_iam_service-with-iam-id-based-policies-resources "#security_iam_service-with-iam-id-based-policies-resources")
- [Policy condition keys for Amazon SWF](#security_iam_service-with-iam-id-based-policies-conditionkeys "#security_iam_service-with-iam-id-based-policies-conditionkeys")
- [ACLs in Amazon SWF](#security_iam_service-with-iam-acls "#security_iam_service-with-iam-acls")
- [ABAC with Amazon SWF](#security_iam_service-with-iam-tags "#security_iam_service-with-iam-tags")
- [Using temporary credentials with Amazon SWF](#security_iam_service-with-iam-roles-tempcreds "#security_iam_service-with-iam-roles-tempcreds")
- [Cross-service principal permissions for Amazon SWF](#security_iam_service-with-iam-principal-permissions "#security_iam_service-with-iam-principal-permissions")
- [Service roles for Amazon SWF](#security_iam_service-with-iam-roles-service "#security_iam_service-with-iam-roles-service")
- [Service-linked roles for Amazon SWF](#security_iam_service-with-iam-roles-service-linked "#security_iam_service-with-iam-roles-service-linked")
- [Identity-based policies for Amazon SWF](#security_iam_service-with-iam-id-based-policies "#security_iam_service-with-iam-id-based-policies")
- [Resource-based policies within Amazon SWF](#security_iam_service-with-iam-resource-based-policies "#security_iam_service-with-iam-resource-based-policies")
- [How Amazon Simple Workflow Service works with IAM](security_iam_service-with-iam.md "security_iam_service-with-iam.md")
- [Identity-based policy examples for Amazon Simple Workflow Service](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md")
- [Basic Principles](swf-dev-iam.md "swf-dev-iam.md")
- [Amazon SWF IAM Policies](swf-dev-iam.md "swf-dev-iam.md")
- [API Summary](swf-dev-iam.md "swf-dev-iam.md")
- [Tag-based Policies](tag-based-policies.md "tag-based-policies.md")
- [Amazon VPC endpoints for Amazon SWF](swf-vpc-endpoints.md "swf-vpc-endpoints.md")
- [Troubleshooting Amazon Simple Workflow Service identity and access](security_iam_troubleshoot.md "security_iam_troubleshoot.md")

## Audience

How you use AWS Identity and Access Management (IAM) differs based on your role:

- **Service user** - request permissions from your
  administrator if you cannot access features (see [Troubleshooting Amazon Simple Workflow Service identity and access](security_iam_troubleshoot.md "security_iam_troubleshoot.md"))
- **Service administrator** - determine user access and
  submit permission requests (see [How Amazon Simple Workflow Service works with IAM](security_iam_service-with-iam.md "security_iam_service-with-iam.md"))
- **IAM administrator** - write policies to manage
  access (see [Identity-based policy examples for Amazon Simple Workflow Service](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md"))

## Authenticating with identities

Authentication is how you sign in to AWS using your identity credentials. You must be authenticated as the AWS account root user, an IAM user, or by assuming an IAM role.

You can sign in as a federated identity using credentials from an identity source like AWS IAM Identity Center (IAM Identity Center), single sign-on authentication, or Google/Facebook credentials. For more information about signing in, see [How to sign in to your AWS account](../../../signin/latest/userguide/how-to-sign-in.md "../../../signin/latest/userguide/how-to-sign-in.md") in the _AWS Sign-In User Guide_.

For programmatic access, AWS provides an SDK and CLI to cryptographically sign requests. For more information, see [AWS Signature Version 4 for API requests](../../../IAM/latest/UserGuide/reference_sigv.md "../../../IAM/latest/UserGuide/reference_sigv.md") in the _IAM User Guide_.

### AWS account root user

When you create an AWS account, you begin with one sign-in identity called the AWS account _root user_ that has complete access to all AWS services and resources. We strongly recommend that you don't use the root user for everyday tasks. For tasks that require root user credentials, see [Tasks that require root user credentials](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks") in the _IAM User Guide_.

### Federated identity

As a best practice, require human users to use federation with an identity provider to access AWS services using temporary credentials.

A _federated identity_ is a user from your enterprise directory, web identity provider, or Directory Service that accesses AWS services using credentials from an identity source. Federated identities assume roles that provide temporary credentials.

For centralized access management, we recommend AWS IAM Identity Center. For more information, see [What is IAM Identity Center?](../../../singlesignon/latest/userguide/what-is.md "../../../singlesignon/latest/userguide/what-is.md") in the _AWS IAM Identity Center User Guide_.

### IAM users and groups

An _[IAM user](../../../IAM/latest/UserGuide/id_users.md "../../../IAM/latest/UserGuide/id_users.md")_ is an identity with specific permissions for a single person or application. We recommend using temporary credentials instead of IAM users with long-term credentials. For more information, see [Require human users to use federation with an identity provider to access AWS using temporary credentials](../../../IAM/latest/UserGuide/best-practices.md#bp-users-federation-idp "../../../IAM/latest/UserGuide/best-practices.md#bp-users-federation-idp") in the _IAM User Guide_.

An [_IAM group_](../../../IAM/latest/UserGuide/id_groups.md "../../../IAM/latest/UserGuide/id_groups.md") specifies a collection of IAM users and makes permissions easier to manage for large sets of users. For more information, see [Use cases for IAM users](../../../IAM/latest/UserGuide/gs-identities-iam-users.md "../../../IAM/latest/UserGuide/gs-identities-iam-users.md") in the _IAM User Guide_.

### IAM roles

An _[IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md")_ is an identity with specific permissions that provides temporary credentials. You can assume a role by [switching from a user to an IAM role (console)](../../../IAM/latest/UserGuide/id_roles_use_switch-role-console.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-console.md") or by calling an AWS CLI or AWS API operation. For more information, see [Methods to assume a role](../../../IAM/latest/UserGuide/id_roles_manage-assume.md "../../../IAM/latest/UserGuide/id_roles_manage-assume.md") in the _IAM User Guide_.

IAM roles are useful for federated user access, temporary IAM user permissions, cross-account access, cross-service access, and applications running on Amazon EC2. For more information, see [Cross account resource access in IAM](../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md "../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md") in the _IAM User Guide_.

## Managing access using policies

You control access in AWS by creating policies and attaching them to AWS identities or resources. A policy defines permissions when associated with an identity or resource. AWS evaluates these policies when a principal makes a request. Most policies are stored in AWS as JSON documents. For more information about JSON policy documents, see [Overview of JSON policies](../../../IAM/latest/UserGuide/access_policies.md#access_policies-json "../../../IAM/latest/UserGuide/access_policies.md#access_policies-json") in the _IAM User Guide_.

Using policies, administrators specify who has access to what by defining which **principal** can perform **actions** on what **resources**, and under what **conditions**.

By default, users and roles have no permissions. An IAM administrator creates IAM policies and adds them to roles, which users can then assume. IAM policies define permissions regardless of the method used to perform the operation.

### Identity-based policies

Identity-based policies are JSON permissions policy documents that you attach to an identity (user, group, or role). These policies control what actions identities can perform, on which resources, and under what conditions. To learn how to create an identity-based policy, see [Define custom IAM permissions with customer managed policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the _IAM User Guide_.

Identity-based policies can be _inline policies_ (embedded directly into a single identity) or _managed policies_ (standalone policies attached to multiple identities). To learn how to choose between managed and inline policies, see [Choose between managed policies and inline policies](../../../IAM/latest/UserGuide/access_policies-choosing-managed-or-inline.md "../../../IAM/latest/UserGuide/access_policies-choosing-managed-or-inline.md") in the _IAM User Guide_.

### Resource-based policies

Resource-based policies are JSON policy documents that you attach to a resource. Examples include IAM _role trust policies_ and Amazon S3 _bucket policies_. In services that support resource-based policies, service administrators can use them to control access to a specific resource. You must [specify a principal](../../../IAM/latest/UserGuide/reference_policies_elements_principal.md "../../../IAM/latest/UserGuide/reference_policies_elements_principal.md") in a resource-based policy.

Resource-based policies are inline policies that are located in that service. You can't use AWS managed policies from IAM in a resource-based policy.

### Other policy types

AWS supports additional policy types that can set the maximum permissions granted by more common policy types:

- **Permissions boundaries** – Set the maximum permissions that an identity-based policy can grant to an IAM entity. For more information, see [Permissions boundaries for IAM entities](../../../IAM/latest/UserGuide/access_policies_boundaries.md "../../../IAM/latest/UserGuide/access_policies_boundaries.md") in the _IAM User Guide_.
- **Service control policies (SCPs)** – Specify the maximum permissions for an organization or organizational unit in AWS Organizations. For more information, see [Service control policies](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md") in the _AWS Organizations User Guide_.
- **Resource control policies (RCPs)** – Set the maximum available permissions for resources in your accounts. For more information, see [Resource control policies (RCPs)](../../../organizations/latest/userguide/orgs_manage_policies_rcps.md "../../../organizations/latest/userguide/orgs_manage_policies_rcps.md") in the _AWS Organizations User Guide_.
- **Session policies** – Advanced policies passed as a parameter when creating a temporary session for a role or federated user. For more information, see [Session policies](../../../IAM/latest/UserGuide/access_policies.md#policies_session "../../../IAM/latest/UserGuide/access_policies.md#policies_session") in the _IAM User Guide_.

### Multiple policy types

When multiple types of policies apply to a request, the resulting permissions are more complicated to understand. To learn how AWS determines whether to allow a request when multiple policy types are involved, see [Policy evaluation logic](../../../IAM/latest/UserGuide/reference_policies_evaluation-logic.md "../../../IAM/latest/UserGuide/reference_policies_evaluation-logic.md") in the _IAM User Guide_.

## Access Control

You can have valid credentials to authenticate your requests, but unless you have
permissions you cannot create or access Amazon SWF resources. For example, you must have
permissions to invoke AWS Lambda, Amazon Simple Notification Service (Amazon SNS), and Amazon Simple Queue Service (Amazon SQS) targets
associated with your Amazon SWF rules.

The following sections describe how to manage permissions for Amazon SWF. We recommend that
you read the overview first.

- [Basic Principles](swf-dev-iam.md "swf-dev-iam.md")
- [Amazon SWF IAM Policies](swf-dev-iam.md "swf-dev-iam.md")
- [Writing policies for Amazon SWF](swf-dev-iam.md#swf-dev-iam.policies.examples "swf-dev-iam.md#swf-dev-iam.policies.examples")

## Policy actions for Amazon SWF

**Supports policy actions:**

Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the
actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

To see a list of Amazon SWF actions, see [Resources Defined by Amazon Simple Workflow Service](../../../IAM/latest/UserGuide/list_amazonsimpleworkflowservice.md#amazonsimpleworkflowservice-resources-for-iam-policies "../../../IAM/latest/UserGuide/list_amazonsimpleworkflowservice.md#amazonsimpleworkflowservice-resources-for-iam-policies") in the
_Service Authorization Reference_.

Policy actions in Amazon SWF use the following prefix before the action:

```
swf
```

To specify multiple actions in a single statement, separate them with commas.

```
"Action": [
      "swf:`action1`",
      "swf:`action2`"
         ]
```

To view examples of Amazon SWF identity-based policies, see [Identity-based policy examples for Amazon Simple Workflow Service](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Policy resources for Amazon SWF

**Supports policy resources:**

Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md"). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

To see a list of Amazon SWF resource types and their ARNs, see [Actions Defined by Amazon Simple Workflow Service](../../../IAM/latest/UserGuide/list_amazonsimpleworkflowservice.md#amazonsimpleworkflowservice-actions-as-permissions "../../../IAM/latest/UserGuide/list_amazonsimpleworkflowservice.md#amazonsimpleworkflowservice-actions-as-permissions")
in the _Service Authorization Reference_. To learn with which actions you can
specify the ARN of each resource, see [Resources Defined by Amazon Simple Workflow Service](../../../IAM/latest/UserGuide/list_amazonsimpleworkflowservice.md#amazonsimpleworkflowservice-resources-for-iam-policies "../../../IAM/latest/UserGuide/list_amazonsimpleworkflowservice.md#amazonsimpleworkflowservice-resources-for-iam-policies").

To view examples of Amazon SWF identity-based policies, see [Identity-based policy examples for Amazon Simple Workflow Service](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Policy condition keys for Amazon SWF

**Supports service-specific policy condition keys:**

Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition
operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md"), such as equals or less than, to match the condition in the
policy with values in the request. To see all AWS global
condition keys, see [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

To see a list of Amazon SWF condition keys, see [Condition Keys for Amazon Simple Workflow Service](../../../IAM/latest/UserGuide/list_amazonsimpleworkflowservice.md#amazonsimpleworkflowservice-policy-keys "../../../IAM/latest/UserGuide/list_amazonsimpleworkflowservice.md#amazonsimpleworkflowservice-policy-keys") in the
_Service Authorization Reference_. To learn with which actions and resources you
can use a condition key, see [Resources Defined by Amazon Simple Workflow Service](../../../IAM/latest/UserGuide/list_amazonsimpleworkflowservice.md#amazonsimpleworkflowservice-resources-for-iam-policies "../../../IAM/latest/UserGuide/list_amazonsimpleworkflowservice.md#amazonsimpleworkflowservice-resources-for-iam-policies").

To view examples of Amazon SWF identity-based policies, see [Identity-based policy examples for Amazon Simple Workflow Service](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## ACLs in Amazon SWF

**Supports ACLs:**

No

Access control lists (ACLs) control which principals (account members, users, or roles) have permissions to access a resource. ACLs are
similar to resource-based policies, although they do not use the JSON policy document format.

## ABAC with Amazon SWF

**Supports ABAC (tags in policies):**

Partial

Attribute-based access control (ABAC) is an authorization strategy that defines permissions
based on attributes called tags. You can attach tags to IAM entities and AWS resources, then design ABAC policies to allow operations when the principal's tag matches the tag on the resource.

To control access based on tags, you provide tag information in the [condition element](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") of a policy using the `aws:ResourceTag/`key-name``, 
 `aws:RequestTag/`key-name``, or `aws:TagKeys` condition keys.

If a service supports all three condition keys for every resource type, then the value is **Yes** for the service. If a service supports all three condition keys for only some resource types, then the value is **Partial**.

For more information about ABAC, see [Define permissions with ABAC authorization](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") in the _IAM User Guide_. To view a tutorial with steps for setting up ABAC, see
[Use attribute-based access control (ABAC)](../../../IAM/latest/UserGuide/tutorial_attribute-based-access-control.md "../../../IAM/latest/UserGuide/tutorial_attribute-based-access-control.md") in the _IAM User Guide_.

## Using temporary credentials with Amazon SWF

**Supports temporary credentials:**

Yes

Temporary credentials provide short-term access to AWS resources and are automatically created when you use federation or switch roles. AWS recommends that you
dynamically generate temporary credentials instead of using long-term access keys. For
more information, see [Temporary
security credentials in IAM](../../../IAM/latest/UserGuide/id_credentials_temp.md "../../../IAM/latest/UserGuide/id_credentials_temp.md") and [AWS services
that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

## Cross-service principal permissions for Amazon SWF

**Supports forward access sessions (FAS):**

Yes

Forward access sessions (FAS) use the permissions of the principal calling an AWS service, combined with the requesting AWS service to make requests to downstream services. For policy details
when making FAS requests, see [Forward access sessions](../../../IAM/latest/UserGuide/access_forward_access_sessions.md "../../../IAM/latest/UserGuide/access_forward_access_sessions.md").

## Service roles for Amazon SWF

**Supports service roles:**

Yes

A service role is an [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") that a service assumes to perform
actions on your behalf. An IAM administrator can create, modify, and delete a service role from within IAM. For
more information, see [Create a role to delegate permissions to an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the _IAM User Guide_.

###### Warning

Changing the permissions for a service role might break Amazon SWF functionality.
Edit service roles only when Amazon SWF provides guidance to do so.

## Service-linked roles for Amazon SWF

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

## Identity-based policies for Amazon SWF

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

### Identity-based policy examples for Amazon SWF

To view examples of Amazon SWF identity-based policies, see [Identity-based policy examples for Amazon Simple Workflow Service](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Resource-based policies within Amazon SWF

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
