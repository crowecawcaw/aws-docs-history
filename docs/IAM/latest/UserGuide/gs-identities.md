# Plan access to your AWS account

When setting up AWS, plan how you intend people to access your AWS account and
resources to set up a well-designed and secure identity management solution.

**Identity sources**

According to IAM best practices human users and workloads should use temporary
credentials when they access your AWS resources. Temporary credentials are granted to
identities who access your resources using an IAM role. Both users federated into IAM
and user in IAM Identity Center (either federated or created in the IAM Identity Center directory) use IAM roles to
access resources.

Before you get started using AWS, plan how to set up your identities either by:

- Enabling IAM Identity Center with AWS Organizations and adding users in IAM Identity Center directly to the organizational
  directory.

To learn how to add users directly to the IAM Identity Center organizational directory, see
[Add users](../../../singlesignon/latest/userguide/addusers.md "../../../singlesignon/latest/userguide/addusers.md")

- Federating your existing external identity provider with either IAM Identity Center or
  IAM.

To learn how to federate an external identity provider to the IAM Identity Center organizational
directory, use the appropriate [Getting started
tutorial](../../../singlesignon/latest/userguide/tutorials.md "../../../singlesignon/latest/userguide/tutorials.md").
**Access management**

Identify the AWS resources and services that your users will access and define the
access permissions and policies required for each user, group, or role.

- If you use IAM Identity Center, an IAM identity provider as well as IAM roles and
  permissions policies are automatically created in each AWS account in your
  organization. These roles and permissions align with the permissions you specify
  when you assign people or groups to specific applications or AWS accounts.

For more information, see [Assign user access](../../../singlesignon/latest/userguide/get-started-assign-account-access-user.md "../../../singlesignon/latest/userguide/get-started-assign-account-access-user.md") and [Set up single sign-on access to your applications](../../../singlesignon/latest/userguide/set-up-single-sign-on-access-to-applications.md "../../../singlesignon/latest/userguide/set-up-single-sign-on-access-to-applications.md").

- If you federate your identity provider directly with IAM in your AWS account,
  you have to create a role for your users to assume and two policies; a trust policy
  that specifies who can assume the role, and a permissions policy that specifies the
  AWS actions and resources that the person assuming the role is allowed or denied
  access to.

For more information, see [Identity providers and federation](id_roles_providers.md "id_roles_providers.md")
