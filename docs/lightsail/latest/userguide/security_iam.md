# Identity and access management for Amazon Lightsail

## Audience

How you use AWS Identity and Access Management (IAM) differs, depending on the work you do in
Amazon Lightsail.

**Service user** – If you use the Amazon Lightsail
service to do your job, then your administrator provides you with the credentials and
permissions that you need. As you use more Amazon Lightsail features to do your work, you
might need additional permissions. Understanding how access is managed can help you request
the right permissions from your administrator. If you cannot access a feature in
Amazon Lightsail, see [Troubleshoot Identity and
Access Management (IAM)](security_iam_troubleshoot.md "security_iam_troubleshoot.md").

**Service administrator** – If you're in charge
of Amazon Lightsail resources at your company, you probably have full access to
Amazon Lightsail. It's your job to determine which Amazon Lightsail features and
resources your employees should access. You must then submit requests to your IAM
administrator to change the permissions of your service users. Review the information on
this page to understand the basic concepts of IAM. To learn more about how your company
can use IAM with Amazon Lightsail, see [How
Amazon Lightsail Works with IAM](security_iam_service-with-iam.md "security_iam_service-with-iam.md").

**IAM administrator** – If you're an IAM
administrator, you might want to learn details about how you can write policies to manage
access to Amazon Lightsail. To view example Amazon Lightsail identity-based policies that
you can use in IAM, see [Amazon Lightsail Identity-Based Policy Examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Authenticating With Identities

Authentication is how you sign in to AWS using your identity credentials. For more
information about signing in using the AWS Management Console, see [The IAM Console
and Sign-in Page](../../../IAM/latest/UserGuide/console.md "../../../IAM/latest/UserGuide/console.md") in the _IAM User Guide_.

You must be _authenticated_ (signed in to AWS) as the
AWS account root user, an IAM user, or by assuming an IAM role. You can also use your
company's single sign-on authentication, or even sign in using Google or Facebook. In
these cases, your administrator previously set up identity federation using IAM roles.
When you access AWS using credentials from another company, you are assuming a role
indirectly.

To sign in directly to the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/"), use your password with your root user email or your IAM user name.
You can access AWS programmatically using your root user or IAM user access keys. AWS
provides SDK and command line tools to cryptographically sign your request using your
credentials. If you don’t use AWS tools, you must sign the request yourself. Do this
using _Signature Version 4_, a protocol for authenticating inbound API
requests. For more information about authenticating requests, see [Signature
Version 4 Signing Process](../../../general/latest/gr/signature-version-4.md "../../../general/latest/gr/signature-version-4.md") in the _AWS General Reference_.

Regardless of the authentication method that you use, you might also be required to
provide additional security information. For example, AWS recommends that you use
multi-factor authentication (MFA) to increase the security of your account. To learn more,
see [Using Multi-Factor Authentication (MFA) in AWS](../../../IAM/latest/UserGuide/id_credentials_mfa.md "../../../IAM/latest/UserGuide/id_credentials_mfa.md") in the
_IAM User Guide_.

### AWS account root user

When you create an AWS account, you begin with one sign-in identity called the AWS account _root user_ that has complete access to all AWS services and resources. We strongly recommend that you don't use the root user for everyday tasks. For tasks that require root user credentials, see [Tasks that require root user credentials](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks") in the _IAM User Guide_.

### IAM Users and Groups

An _[IAM user](../../../IAM/latest/UserGuide/id_users.md "../../../IAM/latest/UserGuide/id_users.md")_ is an identity with specific permissions for a single person or application. We recommend using temporary credentials instead of IAM users with long-term credentials. For more information, see [Require human users to use federation with an identity provider to access AWS using temporary credentials](../../../IAM/latest/UserGuide/best-practices.md#bp-users-federation-idp "../../../IAM/latest/UserGuide/best-practices.md#bp-users-federation-idp") in the _IAM User Guide_.

An [_IAM group_](../../../IAM/latest/UserGuide/id_groups.md "../../../IAM/latest/UserGuide/id_groups.md") specifies a collection of IAM users and makes permissions easier to manage for large sets of users. For more information, see [Use cases for IAM users](../../../IAM/latest/UserGuide/gs-identities-iam-users.md "../../../IAM/latest/UserGuide/gs-identities-iam-users.md") in the _IAM User Guide_.

### IAM Roles

An _[IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md")_ is an identity with specific permissions that provides temporary credentials. You can assume a role by [switching from a user to an IAM role (console)](../../../IAM/latest/UserGuide/id_roles_use_switch-role-console.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-console.md") or by calling an AWS CLI or AWS API operation. For more information, see [Methods to assume a role](../../../IAM/latest/UserGuide/id_roles_manage-assume.md "../../../IAM/latest/UserGuide/id_roles_manage-assume.md") in the _IAM User Guide_.

IAM roles are useful for federated user access, temporary IAM user permissions, cross-account access, cross-service access, and applications running on Amazon EC2. For more information, see [Cross account resource access in IAM](../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md "../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md") in the _IAM User Guide_.

IAM roles with temporary credentials are useful in the following situations:

- **Temporary IAM user permissions** – An
  IAM user can assume an IAM role to temporarily take on different permissions
  for a specific task.
- **Federated user access** –

To assign permissions to a federated identity, you create a role and define permissions for the role. When a federated identity authenticates, the identity is associated with the role and is granted the permissions that are defined by the role. For information about roles for federation, see [Create a role for a third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md") in the _IAM User Guide_.

If you use IAM Identity Center, you configure a permission set. To control what your identities can access after they authenticate, IAM Identity Center correlates the permission set to a role in IAM.
For information about permissions sets, see [Permission sets](../../../singlesignon/latest/userguide/permissionsetsconcept.md "../../../singlesignon/latest/userguide/permissionsetsconcept.md") in the _AWS IAM Identity Center User Guide_.

- **Cross-account access** – You can use an
  IAM role to allow someone (a trusted principal) in a different account to access
  resources in your account. Roles are the primary way to grant cross-account
  access. However, with some AWS services, you can attach a policy
  directly to a resource (instead of using a role as a proxy). To learn the
  difference between roles and resource-based policies for cross-account access, see
  [How IAM roles differ from resource-based policies](../../../IAM/latest/UserGuide/id_roles_compare-resource-policies.md "../../../IAM/latest/UserGuide/id_roles_compare-resource-policies.md") in the
  _IAM User Guide_.
- **Cross-service access** –

Some AWS services use features in other AWS services. For example, when you make a call in a service,
it's common for that service to run applications in Amazon EC2 or store objects in Amazon S3. A service might do this
using the calling principal's permissions, using a service role, or using a service-linked role.

    + **Forward access sessions (FAS)** –
     When you use an IAM user or role to perform actions in AWS, you are
     considered a principal. Policies grant permissions to a principal. When you
     use some services, you might perform an action that then triggers another
     action in a different service. In this case, you must have permissions to
     perform both actions. To see whether an action requires additional dependent
     actions in a policy, see [Actions, Resources, and Condition Keys for Amazon Lightsail](../../../IAM/latest/UserGuide/list_amazonlightsail.md "../../../IAM/latest/UserGuide/list_amazonlightsail.md") in the *Service
     Authorization Reference*.
    + **Service role** –


     A service role is an [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") that a service assumes to perform
     actions on your behalf. An IAM administrator can create, modify, and delete a service role from within IAM. For
     more information, see [Create a role to delegate permissions to an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the *IAM User Guide*.
    + **Service-linked role** –


     A service-linked role is a type of service role that is linked to an AWS service. The service can assume the role to perform an action on your behalf.
     Service-linked roles appear in your AWS account and are owned by the service. An IAM administrator can view,
     but not edit the permissions for service-linked roles.

- **Applications running on Amazon EC2** –

You can use an IAM role to manage temporary credentials for applications that are running on an EC2 instance and making AWS CLI or AWS API requests.
This is preferable to storing access keys within the EC2 instance. To assign an AWS role to an EC2 instance and make it
available to all of its applications, you create an instance profile that is attached to the
instance. An instance profile contains the role and enables programs that are running on the EC2 instance to
get temporary credentials. For more information, see [Use an IAM role to grant permissions to applications running on Amazon EC2 instances](../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2.md") in the
_IAM User Guide_.

To learn whether to use IAM roles or IAM users, see [When to create an IAM role (instead of a user)](../../../IAM/latest/UserGuide/id.md#id_which-to-choose_role "../../../IAM/latest/UserGuide/id.md#id_which-to-choose_role") in the
_IAM User Guide_.

## Managing Access Using Policies

You control access in AWS by creating policies and attaching them to AWS identities or resources. A policy defines permissions when associated with an identity or resource. AWS evaluates these policies when a principal makes a request. Most policies are stored in AWS as JSON documents. For more information about JSON policy documents, see [Overview of JSON policies](../../../IAM/latest/UserGuide/access_policies.md#access_policies-json "../../../IAM/latest/UserGuide/access_policies.md#access_policies-json") in the _IAM User Guide_.

Using policies, administrators specify who has access to what by defining which **principal** can perform **actions** on what **resources**, and under what **conditions**.

By default, users and roles have no permissions. An IAM administrator creates IAM policies and adds them to roles, which users can then assume. IAM policies define permissions regardless of the method used to perform the operation.

Administrators can use AWS JSON policies to specify who has access to what. That is,
which **principal** can perform **actions** on what **resources**, and under what
**conditions**.

Every IAM entity (user or role) starts with no permissions. In other words, by
default, users can do nothing, not even change their own password. To give a user
permission to do something, an administrator must attach a permissions policy to a user. Or
the administrator can add the user to a group that has the intended permissions. When an
administrator gives permissions to a group, all users in that group are granted those
permissions.

IAM policies define permissions for an action regardless of the method that you use to
perform the operation. For example, suppose that you have a policy that allows the
`iam:GetRole` action. A user with that policy can get role information from
the AWS Management Console, the AWS CLI, or the AWS API.

### Identity-Based

Policies

Identity-based policies are JSON permissions policy documents that you attach to an identity (user, group, or role). These policies control what actions identities can perform, on which resources, and under what conditions. To learn how to create an identity-based policy, see [Define custom IAM permissions with customer managed policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the _IAM User Guide_.

Identity-based policies can be _inline policies_ (embedded directly into a single identity) or _managed policies_ (standalone policies attached to multiple identities). To learn how to choose between managed and inline policies, see [Choose between managed policies and inline policies](../../../IAM/latest/UserGuide/access_policies-choosing-managed-or-inline.md "../../../IAM/latest/UserGuide/access_policies-choosing-managed-or-inline.md") in the _IAM User Guide_.

Identity-based policies are JSON permissions policy documents that you can attach to an identity, such as an IAM user, group of users, or role. These
policies control what actions users and roles can perform, on which resources, and under what conditions. To learn how to create an identity-based
policy, see [Define custom IAM permissions with customer managed policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the
_IAM User Guide_.

### Resource-Based

Policies

Resource-based policies are JSON policy documents that you attach to a resource. Examples include IAM _role trust policies_ and Amazon S3 _bucket policies_. In services that support resource-based policies, service administrators can use them to control access to a specific resource. You must [specify a principal](../../../IAM/latest/UserGuide/reference_policies_elements_principal.md "../../../IAM/latest/UserGuide/reference_policies_elements_principal.md") in a resource-based policy.

Resource-based policies are inline policies that are located in that service. You can't use AWS managed policies from IAM in a resource-based policy.

Resource-based policies are JSON policy documents that you attach to a resource. Examples of resource-based policies are
IAM _role trust policies_ and Amazon S3 _bucket policies_. In services that support resource-based policies, service
administrators can use them to control access to a specific resource. For the resource where the policy is attached, the policy defines what actions
a specified principal can perform on that resource and under what conditions. You must [specify a principal](../../../IAM/latest/UserGuide/reference_policies_elements_principal.md "../../../IAM/latest/UserGuide/reference_policies_elements_principal.md") in a resource-based policy. Principals
can include accounts, users, roles, federated users, or AWS services.

### Access Control Lists (ACLs)

Access control lists (ACLs) control which principals (account members, users, or roles) have permissions to access a resource. ACLs are
similar to resource-based policies, although they do not use the JSON policy document format.

Amazon S3, AWS WAF, and Amazon VPC
are examples of services that support ACLs. To learn more about ACLs, see [Access control list (ACL)
overview](../../../AmazonS3/latest/userguide/acl-overview.md "../../../AmazonS3/latest/userguide/acl-overview.md") in the _Amazon Simple Storage Service Developer Guide_.

Access control lists (ACLs) control which principals (account members, users, or roles) have permissions to access a resource. ACLs are
similar to resource-based policies, although they do not use the JSON policy document format.

### Other Policy Types

AWS supports additional policy types that can set the maximum permissions granted by more common policy types:

- **Permissions boundaries** – Set the maximum permissions that an identity-based policy can grant to an IAM entity. For more information, see [Permissions boundaries for IAM entities](../../../IAM/latest/UserGuide/access_policies_boundaries.md "../../../IAM/latest/UserGuide/access_policies_boundaries.md") in the _IAM User Guide_.
- **Service control policies (SCPs)** – Specify the maximum permissions for an organization or organizational unit in AWS Organizations. For more information, see [Service control policies](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md") in the _AWS Organizations User Guide_.
- **Resource control policies (RCPs)** – Set the maximum available permissions for resources in your accounts. For more information, see [Resource control policies (RCPs)](../../../organizations/latest/userguide/orgs_manage_policies_rcps.md "../../../organizations/latest/userguide/orgs_manage_policies_rcps.md") in the _AWS Organizations User Guide_.
- **Session policies** – Advanced policies passed as a parameter when creating a temporary session for a role or federated user. For more information, see [Session policies](../../../IAM/latest/UserGuide/access_policies.md#policies_session "../../../IAM/latest/UserGuide/access_policies.md#policies_session") in the _IAM User Guide_.

- **Permissions boundaries** – A permissions
  boundary is an advanced feature in which you set the maximum permissions that an
  identity-based policy can grant to an IAM entity (IAM user or role). You can
  set a permissions boundary for an entity. The resulting permissions are the
  intersection of entity's identity-based policies and its permissions
  boundaries. Resource-based policies that specify the user or role in the
  `Principal` field are not limited by the permissions boundary. An
  explicit deny in any of these policies overrides the allow. For more information
  about permissions boundaries, see [Permissions boundaries for IAM entities](../../../IAM/latest/UserGuide/access_policies_boundaries.md "../../../IAM/latest/UserGuide/access_policies_boundaries.md") in the
  _IAM User Guide_.
- **Service control policies (SCPs)** – SCPs
  are JSON policies that specify the maximum permissions for an organization or
  organizational unit (OU) in AWS Organizations. AWS Organizations is a service for grouping and
  centrally managing multiple AWS accounts that your business owns.
  If you enable all features in an organization, then you can apply service control
  policies (SCPs) to any or all of your accounts. The SCP limits permissions for
  entities in member accounts, including each AWS account root user.
  For more information about Organizations and SCPs, see [How SCPs work](../../../organizations/latest/userguide/orgs_manage_policies_about-scps.md "../../../organizations/latest/userguide/orgs_manage_policies_about-scps.md") in the _AWS Organizations User Guide_.
- **Session policies** – Session policies are
  advanced policies that you pass as a parameter when you programmatically create a
  temporary session for a role or federated user. The resulting session's
  permissions are the intersection of the user or role's identity-based
  policies and the session policies. Permissions can also come from a resource-based
  policy. An explicit deny in any of these policies overrides the allow. For more
  information, see [Session policies](../../../IAM/latest/UserGuide/access_policies.md#policies_session "../../../IAM/latest/UserGuide/access_policies.md#policies_session") in the _IAM User Guide_.

### Multiple Policy

Types

When multiple types of policies apply to a request, the resulting permissions are more complicated to understand. To learn how AWS determines whether to allow a request when multiple policy types are involved, see [Policy evaluation logic](../../../IAM/latest/UserGuide/reference_policies_evaluation-logic.md "../../../IAM/latest/UserGuide/reference_policies_evaluation-logic.md") in the _IAM User Guide_.

###### Topics

- [AWS managed policies](security-iam-awsmanpol.md "security-iam-awsmanpol.md")
- [Lightsail policies and roles](security_iam_service-with-iam.md "security_iam_service-with-iam.md")
- [Manage IAM user access](amazon-lightsail-managing-access-for-an-iam-user.md "amazon-lightsail-managing-access-for-an-iam-user.md")
