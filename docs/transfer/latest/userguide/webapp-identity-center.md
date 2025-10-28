# Configure your identity provider for Transfer Family web

apps

The following section describes how to configure your identity provider.

To begin, you must have an identity source. You can use an IAM Identity Center directory,
AWS Directory Service for Microsoft Active Directory, or an external identity provider. Transfer Family uses IAM Identity Center as a federated
identity provider, which is a system that stores user credentials and authenticates
users across multiple organizations.

If you're not using an IAM Identity Center directory as your identity source, see the following
topics:

- [Manage an external identity provider](../../../singlesignon/latest/userguide/manage-your-identity-source-idp.md "../../../singlesignon/latest/userguide/manage-your-identity-source-idp.md")
- [Connect to a Microsoft AD directory](../../../singlesignon/latest/userguide/manage-your-identity-source-ad.md "../../../singlesignon/latest/userguide/manage-your-identity-source-ad.md")
- [Organization and account instances of IAM Identity Center](../../../singlesignon/latest/userguide/identity-center-instances.md "../../../singlesignon/latest/userguide/identity-center-instances.md")
- [IAM Identity Center identity source tutorials](../../../singlesignon/latest/userguide/tutorials.md "../../../singlesignon/latest/userguide/tutorials.md")

###### Note

You can only have one identity source in IAM Identity Center, per instance, per AWS Region.
For details, see [IAM Identity Center
prerequisites and considerations](../../../singlesignon/latest/userguide/identity-center-prerequisites.md "../../../singlesignon/latest/userguide/identity-center-prerequisites.md").

If you plan to use the IAM Identity Center directory as your identity source, and want a quick
setup, you can skip this topic and go to [Create a Transfer Family web app](webapp-configure.md#web-app-create "webapp-configure.md#web-app-create") to create an IAM Identity Center instance from the wizard.

###### To configure AWS IAM Identity Center for use with Transfer Family web apps

1. Sign in to the AWS Management Console and open the AWS IAM Identity Center console at [https://console.aws.amazon.com/singlesignon/](https://console.aws.amazon.com/singlesignon/ "https://console.aws.amazon.com/singlesignon/").
2. You can create and use either an account instance or an organization instance
   of AWS IAM Identity Center.
   - For details about account instances, see [Create an account
     instance of AWS IAM Identity Center](../../../singlesignon/latest/userguide/create-account-instance.md "../../../singlesignon/latest/userguide/create-account-instance.md"). With an account instance of IAM Identity Center,
     you can deploy supported AWS managed applications and OpenID Connect
     (OIDC)-based customer managed applications. Account instances support
     isolated deployments of applications in a single AWS account,
     leveraging IAM Identity Center workforce identity and access portal features.
   - For details about organization instances, see [Organization instances of IAM Identity Center](../../../singlesignon/latest/userguide/organization-instances-identity-center.md "../../../singlesignon/latest/userguide/organization-instances-identity-center.md"). You can centrally manage
     the access of users and groups with a single organization
     instance.

3. On
   the IAM Identity Center **Settings** page, note down your Instance ARN. You
   will need this value when you create an **Amazon S3 Access Grant**
   instance.

![Console screenshot from AWS IAM Identity Center showing the Settings page with the Instance ARN circled.](images/webapp-identity-center.png) 4. Create one or more users and, optionally, groups, to use with your Transfer Family
web app. If you're using an IAM Identity Center directory as your identity provider, you can
also add users directly from the web app itself. For more information, see [Assign or add users or groups to Transfer Family
web app](webapp-configure.md#webapp-add-users "webapp-configure.md#webapp-add-users").
