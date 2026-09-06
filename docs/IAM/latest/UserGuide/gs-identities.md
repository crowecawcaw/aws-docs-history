

# Plan access to your AWS account
<a name="gs-identities"></a>

When setting up AWS, plan how you intend people to access your AWS account and resources. A well-designed identity management solution keeps your account secure. 

## Identity sources
<a name="gs-identities-identity-sources"></a>

According to IAM best practices, we recommend that human users and workloads use temporary credentials to access your AWS resources. You grant temporary credentials through IAM roles. Both users federated into IAM and user in IAM Identity Center (either federated or created in the IAM Identity Center directory) use IAM roles to access resources.

Before you start using AWS, plan how to set up your identities by using one of the following approaches:
+ Enabling IAM Identity Center with AWS Organizations and adding users in IAM Identity Center directly to the organizational directory.

  For instructions on adding users directly to the IAM Identity Center organizational directory, see [Add users](https://docs.aws.amazon.com/singlesignon/latest/userguide/addusers.html)
+ Federating your existing external identity provider with either IAM Identity Center or IAM.

  For instructions on federating an external identity provider to the IAM Identity Center organizational directory, see the appropriate [Getting started tutorial](https://docs.aws.amazon.com/singlesignon/latest/userguide/tutorials.html).

## Access management
<a name="gs-identities-access-management"></a>

Identify the AWS resources and services that your users need. Then define the access permissions and policies for each user, group, or role.
+ If you use IAM Identity Center, an IAM identity provider, IAM roles, and permissions policies are created in each AWS account in your organization. These roles and permissions match what you specify when you assign people or groups to applications or AWS accounts.

  For more information, see [Assign user access](https://docs.aws.amazon.com/singlesignon/latest/userguide/get-started-assign-account-access-user.html) and [Set up single sign-on access to your applications](https://docs.aws.amazon.com/singlesignon/latest/userguide/set-up-single-sign-on-access-to-applications.html).
+ You can use [account access manager](account-access-manager.md) — an IAM feature that lets you assign existing IAM roles you create and manage to IAM Identity Center users and groups. Account access manager gives you access to the full IAM role feature set. You can use it alongside permission sets or on its own.
+ If you federate your identity provider directly with IAM in your AWS account, you must create a role for your users to assume. The role needs a trust policy and a permissions policy. The trust policy states who can assume the role. The permissions policy states which AWS actions and resources the role is allowed or denied access to.

  For more information, see [Identity providers and federation into AWS](id_roles_providers.md)

For instructions on adding an extra layer of security for sign-in, see [Use multi-factor authentication with your identities](gs-identities-mfa.md).