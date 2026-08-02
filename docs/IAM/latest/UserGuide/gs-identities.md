# Plan access to your AWS account

When setting up AWS, plan how you intend people to access your AWS account and
resources. A well-designed identity management solution keeps your account secure.

**Identity sources**

According to IAM best practices, we recommend that human users and workloads use
temporary credentials to access your AWS resources. You grant temporary credentials
through IAM roles. Both users federated into IAM and user in IAM Identity Center (either federated
or created in the IAM Identity Center directory) use IAM roles to access resources.

Before you start using AWS, plan how to set up your identities by using one
of the following approaches:

- Enabling IAM Identity Center with AWS Organizations and adding users in IAM Identity Center directly to the
  organizational directory.

For instructions on adding users directly to the IAM Identity Center organizational directory, see
[Add users](../../../singlesignon/latest/userguide/addusers.md "../../../singlesignon/latest/userguide/addusers.md")

- Federating your existing external identity provider with either IAM Identity Center or
  IAM.

For instructions on federating an external identity provider to the IAM Identity Center organizational
directory, see the appropriate [Getting started
tutorial](../../../singlesignon/latest/userguide/tutorials.md "../../../singlesignon/latest/userguide/tutorials.md").
**Access management**

Identify the AWS resources and services that your users need. Then define the
access permissions and policies for each user, group, or role.

- If you use IAM Identity Center, an IAM identity provider, IAM roles, and
  permissions policies are created in each AWS account in your organization.
  These roles and permissions match what you specify when you assign people or
  groups to applications or AWS accounts.

For more information, see [Assign user access](../../../singlesignon/latest/userguide/get-started-assign-account-access-user.md "../../../singlesignon/latest/userguide/get-started-assign-account-access-user.md") and [Set up single sign-on access to your applications](../../../singlesignon/latest/userguide/set-up-single-sign-on-access-to-applications.md "../../../singlesignon/latest/userguide/set-up-single-sign-on-access-to-applications.md").

- If you federate your identity provider directly with IAM in your AWS account,
  you must create a role for your users to assume. The role needs a trust
  policy and a permissions policy. The trust policy states who can assume the
  role. The permissions policy states which AWS actions and resources the role
  is allowed or denied access to.

For more information, see [Identity providers and federation into AWS](id_roles_providers.md "id_roles_providers.md")
