# Use AWS Identity and Access Management to authenticate

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control access
to AWS resources. IAM administrators control who can be _authenticated_ (signed in) and _authorized_
(have permissions) to use Amazon Location resources. IAM is an AWS service that you can
use with no additional charge.

###### Topics

- [Audience](#security_iam_audience "#security_iam_audience")
- [Authenticating with identities](#security_iam_authentication "#security_iam_authentication")
- [Managing access using policies](#security_iam_access-manage "#security_iam_access-manage")
- [How Amazon Location Service works with
  IAM](#security_iam_service-with-iam "#security_iam_service-with-iam")
- [How Amazon Location Service works with
  unauthenticated users](#security_iam_unauthenticated-users "#security_iam_unauthenticated-users")
- [Identity-based policy examples
  for Amazon Location Service](#security_iam_id-based-policy-examples "#security_iam_id-based-policy-examples")
- [Troubleshooting Amazon Location Service identity and
  access](#security_iam_troubleshoot "#security_iam_troubleshoot")

## Audience

How you use AWS Identity and Access Management (IAM) differs based on your role:

- **Service user** - request permissions from your
  administrator if you cannot access features (see [Troubleshooting Amazon Location Service identity and
  access](#security_iam_troubleshoot "#security_iam_troubleshoot"))
- **Service administrator** - determine user access and
  submit permission requests (see [How Amazon Location Service works with
  IAM](#security_iam_service-with-iam "#security_iam_service-with-iam"))
- **IAM administrator** - write policies to manage
  access (see [Identity-based policy examples
  for Amazon Location Service](#security_iam_id-based-policy-examples "#security_iam_id-based-policy-examples"))

## Authenticating with identities

Authentication is how you sign in to AWS using your identity credentials. You must be authenticated as the AWS account root user, an IAM user, or by assuming an IAM role.

You can sign in as a federated identity using credentials from an identity source like AWS IAM Identity Center (IAM Identity Center), single sign-on authentication, or Google/Facebook credentials. For more information about signing in, see [How to sign in to your AWS account](../../../signin/latest/userguide/how-to-sign-in.md "../../../signin/latest/userguide/how-to-sign-in.md") in the _AWS Sign-In User Guide_.

For programmatic access, AWS provides an SDK and CLI to cryptographically sign requests. For more information, see [AWS Signature Version 4 for API requests](../../../IAM/latest/UserGuide/reference_sigv.md "../../../IAM/latest/UserGuide/reference_sigv.md") in the _IAM User Guide_.

### AWS account root user

When you create an AWS account, you begin with one sign-in identity called the AWS account _root user_ that has complete access to all AWS services and resources. We strongly recommend that you don't use the root user for everyday tasks. For tasks that require root user credentials, see [Tasks that require root user credentials](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks") in the _IAM User Guide_.

### Federated identity

As a best practice, require human users to use federation with an identity provider to access AWS services using temporary credentials.

A _federated identity_ is a user from your enterprise directory, web identity provider, or AWS Directory Service that accesses AWS services using credentials from an identity source. Federated identities assume roles that provide temporary credentials.

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

### Identity-based

policies

Identity-based policies are JSON permissions policy documents that you attach to an identity (user, group, or role). These policies control what actions identities can perform, on which resources, and under what conditions. To learn how to create an identity-based policy, see [Define custom IAM permissions with customer managed policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the _IAM User Guide_.

Identity-based policies can be _inline policies_ (embedded directly into a single identity) or _managed policies_ (standalone policies attached to multiple identities). To learn how to choose between managed and inline policies, see [Choose between managed policies and inline policies](../../../IAM/latest/UserGuide/access_policies-choosing-managed-or-inline.md "../../../IAM/latest/UserGuide/access_policies-choosing-managed-or-inline.md") in the _IAM User Guide_.

### Resource-based

policies

Resource-based policies are JSON policy documents that you attach to a resource. Examples include IAM _role trust policies_ and Amazon S3 _bucket policies_. In services that support resource-based policies, service administrators can use them to control access to a specific resource. You must [specify a principal](../../../IAM/latest/UserGuide/reference_policies_elements_principal.md "../../../IAM/latest/UserGuide/reference_policies_elements_principal.md") in a resource-based policy.

Resource-based policies are inline policies that are located in that service. You can't use AWS managed policies from IAM in a resource-based policy.

### Other policy types

AWS supports additional policy types that can set the maximum permissions granted by more common policy types:

- **Permissions boundaries** – Set the maximum permissions that an identity-based policy can grant to an IAM entity. For more information, see [Permissions boundaries for IAM entities](../../../IAM/latest/UserGuide/access_policies_boundaries.md "../../../IAM/latest/UserGuide/access_policies_boundaries.md") in the _IAM User Guide_.
- **Service control policies (SCPs)** – Specify the maximum permissions for an organization or organizational unit in AWS Organizations. For more information, see [Service control policies](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md") in the _AWS Organizations User Guide_.
- **Resource control policies (RCPs)** – Set the maximum available permissions for resources in your accounts. For more information, see [Resource control policies (RCPs)](../../../organizations/latest/userguide/orgs_manage_policies_rcps.md "../../../organizations/latest/userguide/orgs_manage_policies_rcps.md") in the _AWS Organizations User Guide_.
- **Session policies** – Advanced policies passed as a parameter when creating a temporary session for a role or federated user. For more information, see [Session policies](../../../IAM/latest/UserGuide/access_policies.md#policies_session "../../../IAM/latest/UserGuide/access_policies.md#policies_session") in the _IAM User Guide_.

### Multiple policy

types

When multiple types of policies apply to a request, the resulting permissions are more complicated to understand. To learn how AWS determines whether to allow a request when multiple policy types are involved, see [Policy evaluation logic](../../../IAM/latest/UserGuide/reference_policies_evaluation-logic.md "../../../IAM/latest/UserGuide/reference_policies_evaluation-logic.md") in the _IAM User Guide_.

## How Amazon Location Service works with

IAM

Before you use IAM to manage access to Amazon Location, learn what IAM features are
available to use with Amazon Location.

| IAM features you can use with Amazon Location Service                                                                                                                       | IAM feature | Amazon Location support |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ----------------------- |
| [Identity-based<br>policies for Amazon Location](#security_iam_service-with-iam-id-based-policies "#security_iam_service-with-iam-id-based-policies")                       | Yes         |
| [Resource-based policies](#security_iam_service-with-iam-resource-based-policies "#security_iam_service-with-iam-resource-based-policies")                                  | No          |
| [Policy actions](#security_iam_service-with-iam-id-based-policies-actions "#security_iam_service-with-iam-id-based-policies-actions")                                       | Yes         |
| [Policy resources](#security_iam_service-with-iam-id-based-policies-resources "#security_iam_service-with-iam-id-based-policies-resources")                                 | Yes         |
| [Policy condition keys (service-specific)](#security_iam_service-with-iam-id-based-policies-conditionkeys "#security_iam_service-with-iam-id-based-policies-conditionkeys") | Yes         |
| [ACLs](#security_iam_service-with-iam-acls "#security_iam_service-with-iam-acls")                                                                                           | No          |
| [ABAC (tags in<br>policies)](#security_iam_service-with-iam-tags "#security_iam_service-with-iam-tags")                                                                     | Yes         |
| [Temporary credentials](#security_iam_service-with-iam-roles-tempcreds "#security_iam_service-with-iam-roles-tempcreds")                                                    | Yes         |
| [Principal permissions](#security_iam_service-with-iam-principal-permissions "#security_iam_service-with-iam-principal-permissions")                                        | No          |
| [Service roles](#security_iam_service-with-iam-roles-service "#security_iam_service-with-iam-roles-service")                                                                | No          |
| [Service-linked roles](#security_iam_service-with-iam-roles-service-linked "#security_iam_service-with-iam-roles-service-linked")                                           | No          |

To get a high-level view of how Amazon Location and other AWS services work with most
IAM features, see [AWS services
that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

### Identity-based

policies for Amazon Location

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

####

Identity-based policy examples for Amazon Location

To view examples of Amazon Location identity-based policies, see [Identity-based policy examples
for Amazon Location Service](#security_iam_id-based-policy-examples "#security_iam_id-based-policy-examples").

### Resource-based policies within Amazon Location

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

### Policy

actions for Amazon Location

**Supports policy actions:**

Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the
actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

To see a list of Amazon Location actions, see [Actions Defined by Amazon Location Service](../../../service-authorization/latest/reference/list_amazonlocation.md#amazonlocation-actions-as-permissions "../../../service-authorization/latest/reference/list_amazonlocation.md#amazonlocation-actions-as-permissions") in the
_Service Authorization Reference_.

Policy actions in Amazon Location use the following prefix before the action:

```
geo
```

To specify multiple actions in a single statement, separate them with
commas.

```
"Action": [
      "geo:`action1`",
      "geo:`action2`"
         ]
```

You can specify multiple actions using wildcards (\*). For example, to specify all
actions that begin with the word `Get`, include the following
action:

```
"Action": "geo:Get*"
```

To view examples of Amazon Location identity-based policies, see [Identity-based policy examples
for Amazon Location Service](#security_iam_id-based-policy-examples "#security_iam_id-based-policy-examples").

### Policy

resources for Amazon Location

**Supports policy resources:**

Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md"). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

To see a list of Amazon Location resource types and their ARNs, see
[Resources Defined by Amazon Location Service](../../../service-authorization/latest/reference/list_amazonlocation.md#amazonlocation-resources-for-iam-policies "../../../service-authorization/latest/reference/list_amazonlocation.md#amazonlocation-resources-for-iam-policies") in the _Service Authorization Reference_. To learn with
which actions you can specify the ARN of each resource, see
[Actions Defined by Amazon Location Service](../../../service-authorization/latest/reference/list_amazonlocation.md#amazonlocation-actions-as-permissions "../../../service-authorization/latest/reference/list_amazonlocation.md#amazonlocation-actions-as-permissions").

To view examples of Amazon Location identity-based policies, see [Identity-based policy examples
for Amazon Location Service](#security_iam_id-based-policy-examples "#security_iam_id-based-policy-examples").

### Policy condition keys for Amazon Location

**Supports service-specific policy condition keys:**

Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition
operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md"), such as equals or less than, to match the condition in the
policy with values in the request. To see all AWS global
condition keys, see [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

To see a list of Amazon Location condition keys, see [Condition Keys for Amazon Location Service](../../../service-authorization/latest/reference/list_amazonlocation.md#amazonlocation-policy-keys "../../../service-authorization/latest/reference/list_amazonlocation.md#amazonlocation-policy-keys") in the
_Service Authorization Reference_. To learn with which actions and resources
you can use a condition key, see [Actions Defined by Amazon Location Service](../../../service-authorization/latest/reference/list_amazonlocation.md#amazonlocation-actions-as-permissions "../../../service-authorization/latest/reference/list_amazonlocation.md#amazonlocation-actions-as-permissions").

Amazon Location supports condition keys to allow you to allow or deny access to specific
geofences or devices in your policy statements. The following condition keys are
available:

- `geo:GeofenceIds` for use with Geofence actions. The type is
  `ArrayOfString`.
- `geo:DeviceIds` for use with Tracker actions. The type is
  `ArrayOfString`.

The following actions can be used with `geo:GeofenceIds` in your IAM
policy:

- `BatchDeleteGeofences`
- `BatchPutGeofences`
- `GetGeofence`
- `PutGeofence`

The following actions can be used with `geo:DeviceIds` in your IAM
policy:

- `BatchDeleteDevicePositionHistory`
- `BatchGetDevicePosition`
- `BatchUpdateDevicePosition`
- `GetDevicePosition`
- `GetDevicePositionHistory`

###### Note

You can't use these condition keys with the
`BatchEvaluateGeofences`, `ListGeofences`, or
`ListDevicePosition` actions.

To view examples of Amazon Location identity-based policies, see [Identity-based policy examples
for Amazon Location Service](#security_iam_id-based-policy-examples "#security_iam_id-based-policy-examples").

### ACLs in Amazon Location

**Supports ACLs:**

No

Access control lists (ACLs) control which principals (account members, users, or roles) have permissions to access a resource. ACLs are
similar to resource-based policies, although they do not use the JSON policy document format.

### ABAC with Amazon Location

**Supports ABAC (tags in policies):**

Yes

Attribute-based access control (ABAC) is an authorization strategy that defines permissions
based on attributes called tags. You can attach tags to IAM entities and AWS resources, then design ABAC policies to allow operations when the principal's tag matches the tag on the resource.

To control access based on tags, you provide tag information in the [condition element](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") of a policy using the `aws:ResourceTag/`key-name``, 
 `aws:RequestTag/`key-name``, or `aws:TagKeys` condition keys.

If a service supports all three condition keys for every resource type, then the value is **Yes** for the service. If a service supports all three condition keys for only some resource types, then the value is **Partial**.

For more information about ABAC, see [Define permissions with ABAC authorization](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") in the _IAM User Guide_. To view a tutorial with steps for setting up ABAC, see
[Use attribute-based access control (ABAC)](../../../IAM/latest/UserGuide/tutorial_attribute-based-access-control.md "../../../IAM/latest/UserGuide/tutorial_attribute-based-access-control.md") in the _IAM User Guide_.

For more information about tagging Amazon Location resources, see [How to use tags](manage-resources.md#manage-resources_how-to "manage-resources.md#manage-resources_how-to").

To view an example identity-based policy for limiting access to a resource based
on the tags on that resource, see [Control resource access
based on tags](#security_iam_tag-based-policy-example "#security_iam_tag-based-policy-example").

### Using temporary

credentials with Amazon Location

**Supports temporary credentials:**

Yes

Temporary credentials provide short-term access to AWS resources and are automatically created when you use federation or switch roles. AWS recommends that you
dynamically generate temporary credentials instead of using long-term access keys. For
more information, see [Temporary
security credentials in IAM](../../../IAM/latest/UserGuide/id_credentials_temp.md "../../../IAM/latest/UserGuide/id_credentials_temp.md") and [AWS services
that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

### Cross-service

principal permissions for Amazon Location

**Supports forward access sessions (FAS):**

No

Forward access sessions (FAS) use the permissions of the principal calling an AWS service, combined with the requesting AWS service to make requests to downstream services. For policy details
when making FAS requests, see [Forward access sessions](../../../IAM/latest/UserGuide/access_forward_access_sessions.md "../../../IAM/latest/UserGuide/access_forward_access_sessions.md").

### Service roles for

Amazon Location

**Supports service roles:**

No

A service role is an [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") that a service assumes to perform
actions on your behalf. An IAM administrator can create, modify, and delete a service role from within IAM. For
more information, see [Create a role to delegate permissions to an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the _IAM User Guide_.

###### Warning

Changing the permissions for a service role might break Amazon Location
functionality. Edit service roles only when Amazon Location provides guidance to do
so.

### Service-linked

roles for Amazon Location

**Supports service-linked roles:**

No

A service-linked role is a type of service role that is linked to an AWS service. The service can assume the role to perform an action on your behalf.
Service-linked roles appear in your AWS account and are owned by the service. An IAM administrator can view,
but not edit the permissions for service-linked roles.

For details about creating or managing service-linked roles, see [AWS
services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md"). Find a service in the table that includes
a `Yes` in the **Service-linked role** column. Choose
the **Yes** link to view the service-linked role documentation for
that service.

## How Amazon Location Service works with

unauthenticated users

Many scenarios for using Amazon Location Service, including showing maps on the web or in a mobile
application, require allowing access to users who haven't signed in with IAM. For
these unauthenticated scenarios, you have two options.

- **Use API keys** – To grant
  access to unauthenticated users, you can create API Keys that give read-only
  access to your Amazon Location Service resources. This is useful in a case where you do not want
  to authenticate every user. For example, a web application. For more information
  about API keys, see [Use API keys to authenticate](using-apikeys.md "using-apikeys.md").
- **Use Amazon Cognito** – An alternative to API keys
  is to use Amazon Cognito to grant anonymous access. Amazon Cognito allows you to create a richer
  authorization with IAM policy to define what can be done by the unauthenticated
  users. For more information about using Amazon Cognito, see [Use the Amazon Cognito identity pool in web](authenticating-using-cognito.md#identity-pool-js "authenticating-using-cognito.md#identity-pool-js").

For an overview of providing access to unauthenticated users, see [Authenticate with Amazon Location Service](access.md "access.md").

## Identity-based policy examples

for Amazon Location Service

By default, users and roles don't have permission to create or modify Amazon Location
resources. To grant users permission to perform actions on the
resources that they need, an IAM administrator can create IAM policies.

To learn how to create an IAM identity-based policy by using these example JSON policy
documents, see [Create IAM policies (console)](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") in the
_IAM User Guide_.

For details about actions and resource types defined by Amazon Location, including the format of the ARNs for each of the resource types, see [Actions, Resources, and Condition Keys for Amazon Location Service](../../../service-authorization/latest/reference/list_amazonlocation.md "../../../service-authorization/latest/reference/list_amazonlocation.md") in the _Service Authorization Reference_.

###### Topics

- [Policy best
  practices](#security_iam_service-with-iam-policy-best-practices "#security_iam_service-with-iam-policy-best-practices")
- [Using the Amazon Location
  console](#security_iam_id-based-policy-examples-console "#security_iam_id-based-policy-examples-console")
- [Allow
  users to view their own permissions](#security_iam_id-based-policy-examples-view-own-permissions "#security_iam_id-based-policy-examples-view-own-permissions")
- [Using
  Amazon Location Service resources in policy](#security_iam_id-based-policy-examples-using-resources "#security_iam_id-based-policy-examples-using-resources")
- [Permissions for updating device positions](#security_iam_id-based-policy-examples-update-device-positions "#security_iam_id-based-policy-examples-update-device-positions")
- [Read-only
  policy for tracker resources](#security_iam_id-based-policy-examples-read-only-trackers "#security_iam_id-based-policy-examples-read-only-trackers")
- [Policy for
  creating geofences](#security_iam_id-based-policy-examples-create-geofences "#security_iam_id-based-policy-examples-create-geofences")
- [Read-only policy for geofences](#security_iam_id-based-policy-examples-read-only-geofences "#security_iam_id-based-policy-examples-read-only-geofences")
- [Permissions
  for rendering a map resource](#security_iam_id-based-policy-examples-get-map-tiles "#security_iam_id-based-policy-examples-get-map-tiles")
- [Permissions
  to allow search operations](#security_iam_id-based-policy-examples-search-for-place "#security_iam_id-based-policy-examples-search-for-place")
- [Read-only
  policy for route calculators](#security_iam_id-based-policy-examples-calculate-route "#security_iam_id-based-policy-examples-calculate-route")
- [Control resource access based
  on condition keys](#security_iam_condition-key-example "#security_iam_condition-key-example")
- [Control resource access
  based on tags](#security_iam_tag-based-policy-example "#security_iam_tag-based-policy-example")

### Policy best

practices

Identity-based policies determine whether someone can create, access, or delete Amazon Location resources in your
account. These actions can incur costs for your AWS account. When you create or edit identity-based policies, follow these guidelines and
recommendations:

- **Get started with AWS managed policies and move toward least-privilege permissions**
  – To get started granting permissions to your users and workloads, use the _AWS
  managed policies_ that grant permissions for many common use cases. They are
  available in your AWS account. We recommend that you reduce permissions further by
  defining AWS customer managed policies that are specific to your use cases. For more information, see
  [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") or [AWS managed policies for job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _IAM User Guide_.
- **Apply least-privilege permissions** –
  When you set permissions with IAM policies, grant only the permissions required to
  perform a task. You do this by defining the actions that can be taken on specific resources
  under specific conditions, also known as _least-privilege permissions_.
  For more information about using IAM to apply permissions, see [Policies and permissions in IAM](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") in the _IAM User Guide_.
- **Use conditions in IAM policies to further restrict access**
  – You can add a condition to your policies to limit access to actions and resources. For example, you can write a policy condition to specify that all requests must
  be sent using SSL. You can also use conditions to grant access to service actions
  if they are used through a specific AWS service, such as AWS CloudFormation. For more information, see
  [IAM JSON policy elements: Condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") in the _IAM User Guide_.
- **Use IAM Access Analyzer to validate your IAM policies to ensure secure and functional permissions**
  – IAM Access Analyzer validates new and existing policies so that the policies adhere to the IAM policy language (JSON) and IAM best practices.
  IAM Access Analyzer provides more than 100 policy checks and actionable recommendations to help
  you author secure and functional policies. For more information, see [Validate policies with IAM Access Analyzer](../../../IAM/latest/UserGuide/access-analyzer-policy-validation.md "../../../IAM/latest/UserGuide/access-analyzer-policy-validation.md") in the _IAM User Guide_.
- **Require multi-factor authentication (MFA)** –
  If you have a scenario that requires IAM users or a root user in your AWS account, turn on MFA for additional security. To require
  MFA when API operations are called, add MFA conditions to your policies. For
  more information, see [Secure API access with MFA](../../../IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.md "../../../IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.md") in the _IAM User Guide_.

For more information about best practices in IAM, see [Security best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the _IAM User Guide_.

### Using the Amazon Location

console

To access the Amazon Location Service console, you must have a minimum set of permissions.
These permissions must allow you to list and view details about the Amazon Location resources
in your AWS account. If you create an identity-based policy that is more restrictive
than the minimum required permissions, the console won't function as intended for
entities (users or roles) with that policy.

You don't need to allow minimum console permissions for users that are making calls
only to the AWS CLI or the AWS API. Instead, allow access to only the actions that match
the API operation that they're trying to perform.

To ensure that users and roles can use the Amazon Location console, attach the following
policy to the entities. For more information, see [Adding permissions to a user](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the
_IAM User Guide_.

The following policy gives access to the Amazon Location Service console, to be able to create,
delete, list and view details about Amazon Location resources in your AWS
account.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "GeoPowerUser",
      "Effect": "Allow",
      "Action": [
        "geo:*",
        "geo-maps:*",
        "geo-places:*",
        "geo-routes:*"
      ],
      "Resource": "*"
    }
  ]
}
```

Alternatively, you can grant read-only permissions to facilitate read-only access.
With read-only permissions, an error message will appear if the user attempts write
actions such as creating or deleting resources. As an example, see [Read-only
policy for tracker resources](#security_iam_id-based-policy-examples-read-only-trackers "#security_iam_id-based-policy-examples-read-only-trackers")

### Allow

users to view their own permissions

This example shows how you might create a policy that allows IAM users to view the inline and managed policies that are attached to their user
identity. This policy includes permissions to complete this action on the console or programmatically using the AWS CLI or AWS API.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ViewOwnUserInfo",
            "Effect": "Allow",
            "Action": [
                "iam:GetUserPolicy",
                "iam:ListGroupsForUser",
                "iam:ListAttachedUserPolicies",
                "iam:ListUserPolicies",
                "iam:GetUser"
            ],
            "Resource": ["arn:aws:iam::*:user/${aws:username}"]
        },
        {
            "Sid": "NavigateInConsole",
            "Effect": "Allow",
            "Action": [
                "iam:GetGroupPolicy",
                "iam:GetPolicyVersion",
                "iam:GetPolicy",
                "iam:ListAttachedGroupPolicies",
                "iam:ListGroupPolicies",
                "iam:ListPolicyVersions",
                "iam:ListPolicies",
                "iam:ListUsers"
            ],
            "Resource": "*"
        }
    ]
}
```

### Using

Amazon Location Service resources in policy

Amazon Location Service uses the following prefixes for resources:

| Amazon Location resource prefix | Resource              | Resource prefix |
| ------------------------------- | --------------------- | --------------- |
| Map resources                   | `map`                 |
| Place resources                 | `place-index`         |
| Route resources                 | `route-calculator`    |
| Tracking resources              | `tracker`             |
| Geofence Collection resources   | `geofence-collection` |

Use the following ARN syntax:

```
arn:`Partition`:geo:`Region`:`Account`:`ResourcePrefix`/`ResourceName`
```

For more information about the format of ARNs, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md").

**Examples**

- Use the following ARN to allow access to a specified map resource.

```
"Resource": "arn:aws:geo:us-west-2:`account-id`:map/`map-resource-name`"
```

- To specify access to all `map` resources that belong to a
  specific account, use the wildcard (\*):

```
"Resource": "arn:aws:geo:us-west-2:`account-id`:map/*"
```

- Some Amazon Location actions, such as those for creating resources, can't be
  performed on a specific resource. In those cases, you must use the wildcard
  (\*).

```
"Resource": "*"
```

To see a list of Amazon Location resource types and their ARNs, see
[Resources Defined by Amazon Location Service](../../../service-authorization/latest/reference/list_amazonlocation.md#amazonlocation-resources-for-iam-policies "../../../service-authorization/latest/reference/list_amazonlocation.md#amazonlocation-resources-for-iam-policies") in the _Service Authorization
Reference_. To learn with which actions you can specify the ARN of
each resource, see [Actions Defined by Amazon Location Service](../../../service-authorization/latest/reference/list_amazonlocation.md#amazonlocation-actions-as-permissions "../../../service-authorization/latest/reference/list_amazonlocation.md#amazonlocation-actions-as-permissions").

### Permissions for updating device positions

To update device positions for multiple trackers, you'll want to grant a user
access to one or more of your tracker resources. You will also want to allow the
user to update a batch of device positions.

In this example, in addition to granting access to the
`Tracker1` and `Tracker2`
resources, the following policy grants permission to use the
`geo:BatchUpdateDevicePosition` action against the
`Tracker1` and `Tracker2`
resources.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "UpdateDevicePositions",
      "Effect": "Allow",
      "Action": [
        "geo:BatchUpdateDevicePosition"
      ],
      "Resource": [
        "arn:aws:geo:us-west-2:`account-id`:tracker/`Tracker1`",
        "arn:aws:geo:us-west-2:`account-id`:tracker/`Tracker2`"
      ]
    }
  ]
}
```

If you want to limit the user to only be able to update device positions for a
specific device, you can add a condition key for that device id.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "UpdateDevicePositions",
      "Effect": "Allow",
      "Action": [
        "geo:BatchUpdateDevicePosition"
      ],
      "Resource": [
        "arn:aws:geo:us-west-2:`account-id`:tracker/`Tracker1`",
        "arn:aws:geo:us-west-2:`account-id`:tracker/`Tracker2`"
      ],
      "Condition":{
        "ForAllValues:StringLike":{
          "geo:DeviceIds":[
            "`deviceId`"
          ]
        }
      }
    }
  ]
}
```

### Read-only

policy for tracker resources

To create a read-only policy for all tracker resources in your AWS account,
you'll need to grant access to all tracker resources. You'll also want to grant a
user access to actions that allow them to get the device position for multiple
devices, get the device position from a single device and get the position
history.

In this example, the following policy grants permission to the following
actions:

- `geo:BatchGetDevicePosition` to retrieve the
  position of multiple devices.
- `geo:GetDevicePosition` to retrieve the position
  of a single device.
- `geo:GetDevicePositionHistory` to retrieve the
  position history of a device.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "GetDevicePositions",
      "Effect": "Allow",
      "Action": [
        "geo:BatchGetDevicePosition",
        "geo:GetDevicePosition",
        "geo:GetDevicePositionHistory"
      ],
      "Resource": "arn:aws:geo:us-west-2:`account-id`:tracker/*"
    }
  ]
}
```

### Policy for

creating geofences

To create a policy to allow a user to create geofences, you'll need to grant
access to specific actions that allow users to create one or more geofences on a
geofence collection.

The policy below grants permission to the following actions on
`Collection`:

- `geo:BatchPutGeofence` to create multiple
  geofences.
- `geo:PutGeofence` to create a single
  geofence.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "CreateGeofences",
      "Effect": "Allow",
      "Action": [
        "geo:BatchPutGeofence",
        "geo:PutGeofence"
      ],
      "Resource": "arn:aws:geo:us-west-2:`account-id`:geofence-collection/`Collection`"
    }
  ]
}
```

### Read-only policy for geofences

To create a read-only policy for geofences stored in a geofence collection in your
AWS account, you'll need to grant access to actions that read from the geofence
collection storing the geofences.

The policy below grants permission to the following actions on
`Collection`:

- `geo:ListGeofences` to list geofences in the
  specified geofence collection.
- `geo:GetGeofence` to retrieve a geofence from
  the geofence collection.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "GetGeofences",
      "Effect": "Allow",
      "Action": [
        "geo:ListGeofences",
        "geo:GetGeofence"
      ],
      "Resource": "arn:aws:geo:us-west-2:`account-id`:geofence-collection/`Collection`"
    }
  ]
}
```

### Permissions

for rendering a map resource

To grant sufficient permissions to render maps, you'll need to grant access to map
tiles, sprites, glyphs, and the style descriptor:

- `geo:GetMapTile` retrieves map tiles used to
  selectively render features on a map.
- `geo:GetMapSprites` retrieves the PNG sprite
  sheet and corresponding JSON document describing offsets within it.
- `geo:GetMapGlyphs` retrieves the glyphs used for
  displaying text.
- `geo:GetMapStyleDescriptor` retrieves the map’s
  style descriptor, containing rendering rules.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "GetTiles",
      "Effect": "Allow",
      "Action": [
        "geo:GetMapTile",
        "geo:GetMapSprites",
        "geo:GetMapGlyphs",
        "geo:GetMapStyleDescriptor"
      ],
      "Resource": "arn:aws:geo:us-west-2:`account-id`:map/`Map`"
    }
  ]
}
```

### Permissions

to allow search operations

To create a policy to allow search operations, you'll first need to grant access
to the place index resource in your AWS account. You'll also want to grant access
to actions that let the user search using text by geocoding and search using a
position by reverse geocoding.

In this example, in addition to granting access to
`PlaceIndex`, the following policy also grants
permission to the following actions:

- `geo:SearchPlaceIndexForPosition` allows you to
  search for places, or points of interest near a given position.
- `geo:SearchPlaceIndexForText` allows you to
  search for an address, name, city or region using free-form text.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "Search",
      "Effect": "Allow",
      "Action": [
        "geo:SearchPlaceIndexForPosition",
        "geo:SearchPlaceIndexForText"
      ],
      "Resource": "arn:aws:geo:us-west-2:`account-id`:place-index/`PlaceIndex`"
    }
  ]
}
```

### Read-only

policy for route calculators

You can create a read-only policy to allow a user access to a route calculator
resource to calculate a route.

In this example, in addition to granting access to
`ExampleCalculator`, the following policy grants
permission to the following operation:

- `geo:CalculateRoute` calculates a route given a
  departure position, destination positon, and a list of waypoint positions.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "RoutesReadOnly",
      "Effect": "Allow",
      "Action": [
        "geo:CalculateRoute"
      ],
      "Resource": "arn:aws:geo:us-west-2:`accountID`:route-calculator/`ExampleCalculator`"
    }
  ]
}
```

### Control resource access based

on condition keys

When you create an IAM policy to grant access to use geofences or device
positions, you can use [Condition operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md") for more precise control over which geofences or
devices a user can access. You can do this by including the geofence id or device id
in the `Condition` element of your policy.

The following example policy shows how you might create a policy that allows a
user to update device positions for a specific device.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "UpdateDevicePositions",
      "Effect": "Allow",
      "Action": [
        "geo:BatchUpdateDevicePosition"
      ],
      "Resource": [
        "arn:aws:geo:us-west-2:`account-id`:tracker/`Tracker`"
      ],
      "Condition":{
        "ForAllValues:StringLike":{
          "geo:DeviceIds":[
            "`deviceId`"
          ]
        }
      }
    }
  ]
}
```

### Control resource access

based on tags

When you create an IAM policy to grant access to use your Amazon Location resources,
you can use [attribute-based access control](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") for better control over which resources
a user can modify, use, or delete. You can do this by including tag information in
the `Condition` element of your policy to control access based on your
resource [tags](manage-resources.md#manage-resources_how-to "manage-resources.md#manage-resources_how-to").

The following example policy shows how you might create a policy that allows a
user to create geofences. This grants the permission to the following actions to
create one or more geofences on a geofence collection called
`Collection`:

- `geo:BatchPutGeofence` to create multiple
  geofences.
- `geo:PutGeofence` to create a single
  geofence.

However, this policy uses the `Condition` element to grant the
permission only if the `Collection` tag,
`Owner`, has the value of that user's user name.

- For example, if a user named `richard-roe` attempts to view an
  Amazon Location `Collection`, the
  `Collection` must be tagged
  `Owner=richard-roe` or `owner=richard-roe`.
  Otherwise the user is denied access.

###### Note

The condition tag key `Owner` matches both
`Owner` and `owner` because condition key
names are not case-sensitive. For more information, see [IAM
JSON Policy Elements: Condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") in the _IAM User Guide_.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "CreateGeofencesIfOwner",
      "Effect": "Allow",
      "Action": [
        "geo:BatchPutGeofence",
        "geo:PutGeofence"
      ],
      "Resource": "arn:aws:geo:us-west-2:`account-id`:geofence-collection/`Collection`",
      "Condition": {
                "StringEquals": {"geo:ResourceTag/Owner": "${aws:`username`}"}
      }
    }
  ]
}
```

For a tutorial about [how to
define permissions to access AWS resources based on tags](../../../IAM/latest/UserGuide/tutorial_attribute-based-access-control.md "../../../IAM/latest/UserGuide/tutorial_attribute-based-access-control.md"), see the
_AWS Identity and Access Management User Guide_.

## Troubleshooting Amazon Location Service identity and

access

Use the following information to help you diagnose and fix common issues that you might
encounter when working with Amazon Location and IAM.

###### Topics

- [I am not authorized to
  perform an action in Amazon Location](#security_iam_troubleshoot-no-permissions "#security_iam_troubleshoot-no-permissions")
- [I am not authorized to perform
  iam:PassRole](#security_iam_troubleshoot-passrole "#security_iam_troubleshoot-passrole")
- [I want to allow
  people outside of my AWS account to access my Amazon Location resources](#security_iam_troubleshoot-cross-account-access "#security_iam_troubleshoot-cross-account-access")

### I am not authorized to

perform an action in Amazon Location

If you receive an error that you're not authorized to perform an action, your
policies must be updated to allow you to perform the action.

The following example error occurs when the `mateojackson` IAM user
tries to use the console to view details about a fictional
`my-example-widget` resource but doesn't
have the fictional `geo:`GetWidget`` permissions.

```
User: arn:aws:iam::123456789012:user/mateojackson is not authorized to perform: geo:GetWidget on resource: my-example-widget
```

In this case, the policy for the `mateojackson` user must be updated to allow access to the
`my-example-widget` resource by using the
`geo:`GetWidget`` action.

If you need help, contact your AWS administrator. Your administrator is the person who provided you with your sign-in credentials.

### I am not authorized to perform

iam:PassRole

If you receive an error that you're not authorized to perform the `iam:PassRole` action, your policies must be updated to allow you to pass a role to Amazon Location.

Some AWS services allow you to pass an existing role to that service instead of creating a new service role or service-linked role. To do
this, you must have permissions to pass the role to the service.

The following example error occurs when an IAM user named `marymajor` tries to use the console to perform an action in
Amazon Location. However, the action requires the service to have permissions that are granted by a service role. Mary does not have permissions to pass the
role to the service.

```
User: arn:aws:iam::123456789012:user/`marymajor` is not authorized to perform: iam:PassRole
```

In this case, Mary's policies must be updated to allow her to perform the `iam:PassRole` action.

If you need help, contact your AWS administrator. Your administrator is the person who provided you with your sign-in credentials.

### I want to allow

people outside of my AWS account to access my Amazon Location resources

You can create a role that users in other accounts or people outside of your organization can use to access your resources. You can specify who
is trusted to assume the role. For services that support resource-based policies or access control lists (ACLs), you can use those policies to grant
people access to your resources.

To learn more, consult the following:

- To learn whether Amazon Location supports these features, see [How Amazon Location Service works with
  IAM](#security_iam_service-with-iam "#security_iam_service-with-iam").
- To learn how to provide access to your resources across AWS accounts that you own, see [Providing access to an IAM user in another AWS account that you
  own](../../../IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.md") in the _IAM User Guide_.
- To learn how to provide access to your resources to third-party AWS accounts, see [Providing access to AWS accounts owned by third parties](../../../IAM/latest/UserGuide/id_roles_common-scenarios_third-party.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_third-party.md") in the
  _IAM User Guide_.
- To learn how to provide access through identity federation, see [Providing access to externally authenticated users (identity federation)](../../../IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.md") in the _IAM User Guide_.
- To learn the difference between using roles and resource-based policies for cross-account access, see [Cross account resource access in IAM](../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md "../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md") in the
  _IAM User Guide_.
