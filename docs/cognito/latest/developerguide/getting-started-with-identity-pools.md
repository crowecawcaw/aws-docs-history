# Getting started with Amazon Cognito identity

pools

With Amazon Cognito identity pools, you can create unique identities and assign permissions for
users. Your identity pool can bring in identities from the following types of authentication
services:

- Users in an Amazon Cognito user pool
- Users who authenticate with external identity providers such as Facebook, Google,
  Apple, or an OIDC or SAML identity provider.
- Users authenticated via your own existing authentication process
  After users authenticate with their provider and present authorization to an identity
  pool, they get temporary AWS credentials. Users' credentials have permissions that you
  define for access to other AWS services.

###### Topics

- [Create an identity pool in Amazon Cognito](#create-identity-pool "#create-identity-pool")
- [Set up an SDK](#install-the-mobile-or-javascript-sdk "#install-the-mobile-or-javascript-sdk")
- [Integrate the identity providers](#integrate-the-identity-providers "#integrate-the-identity-providers")
- [Get credentials](#get-credentials "#get-credentials")
- [Example application for
  identity pools](getting-started-identity-pools-application.md "getting-started-identity-pools-application.md")

## Create an identity pool in Amazon Cognito

You can create an identity pool through the Amazon Cognito console, or you can use the
AWS Command Line Interface (CLI) or the Amazon Cognito APIs. The following procedure is a general guide to create
a new identity pool in the console. You can also [skip straight to the console](https://console.aws.amazon.com/cognito/v2/identity/identity-pools "https://console.aws.amazon.com/cognito/v2/identity/identity-pools") and
follow the guided experience and inline help content.

###### To create a new identity pool in the console

1. Sign in to the [Amazon Cognito
   console](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home") and select **Identity pools**. To assign
   permissions to your IAM principal so that they can create and manage Amazon Cognito
   resources, refer to [AWS managed policies for Amazon Cognito](security-iam-awsmanpol.md "security-iam-awsmanpol.md"). The `AmazonCognitoPowerUser`
   policy is sufficient for the creation of identity pools.
2. Choose **Create identity pool**.
3. In **Configure identity pool trust**, choose to set up your
   identity pool for **Authenticated access**, **Guest
   access**, or both.
   1. If you chose **Authenticated access**, select one or more
      **Identity types** that you want to set as the source of
      authenticated identities in your identity pool. If you configure a **Custom
      developer provider**, you can't modify or delete it after you create your
      identity pool.

4. In **Configure permissions**, choose a default IAM role for
   authenticated or guest users in your identity pool.
   1. Choose to **Create a new IAM role** if you want Amazon Cognito to
      create a new role for you with basic permissions and a trust relationship with your
      identity pool. Enter an **IAM role name** to identify your new
      role, for example `myidentitypool_authenticatedrole`. Select
      **View policy document** to review the permissions that Amazon Cognito
      will assign to your new IAM role.
   2. You can choose to **Use an existing IAM role** if you already
      have a role in your AWS account that you want to use. You must configure your
      IAM role trust policy to include `cognito-identity.amazonaws.com`.
      Configure your role trust policy to only allow Amazon Cognito to assume the role when it
      presents evidence that the request originated from an authenticated user in your
      specific identity pool. For more information, see [Role trust and permissions](iam-roles.md#role-trust-and-permissions "iam-roles.md#role-trust-and-permissions").

5. In **Connect identity providers**, enter the details of the
   identity providers (IdPs) that you chose in **Configure identity pool
   trust**. You might be asked to provide OAuth app client information, choose
   an Amazon Cognito user pool, choose an IAM IdP, or enter a custom identifier for a developer
   provider.
   1. Choose the **Role settings** for each IdP. You can assign users
      from that IdP the **Default role** that you set up when you
      configured your **Authenticated role**, or you can **Choose
      role with rules**. With an Amazon Cognito user pool IdP, you can also
      **Choose role with preferred_role in tokens**. For more
      information about the `cognito:preferred_role` claim, see [Assigning precedence values to
      groups](cognito-user-pools-user-groups.md#assigning-precedence-values-to-groups "cognito-user-pools-user-groups.md#assigning-precedence-values-to-groups").
      1. If you chose **Choose role with rules**, enter the source
         **Claim** from your user's authentication, the
         **Operator** that you want to compare the claim by, the
         **Value** that will cause a match to this role choice, and
         the **Role** that you want to assign when the **Role
         assignment** matches. Select **Add another** to
         create an additional rule based on a different condition.
      2. Choose a **Role resolution**. When your user's claims don't
         match your rules, you can deny credentials or issue credentials for your
         **Authenticated role**.

   2. Configure **Attributes for access control** for each IdP.
      Attributes for access control maps user claims to [principal tags](../../../IAM/latest/UserGuide/access_iam-tags.md "../../../IAM/latest/UserGuide/access_iam-tags.md") that Amazon Cognito
      applies to their temporary session. You can build IAM policies to filter user
      access based on the tags that you apply to their session.
      1. To apply no principal tags, choose **Inactive**.
      2. To apply principal tags based on `sub` and `aud`
         claims, choose **Use default mappings**.
      3. To create your own custom schema of attributes to principal tags, choose
         **Use custom mappings**. Then enter a **Tag
         key** that you want to source from each **Claim**
         that you want to represent in a tag.

6. In **Configure properties**, enter a **Name**
   under **Identity pool name**.
7. Under **Basic (classic) authentication**, choose whether you want
   to **Activate basic flow**. With the basic flow active, you can bypass
   the role selections you made for your IdPs and call [AssumeRoleWithWebIdentity](../../../STS/latest/APIReference/API_AssumeRoleWithWebIdentity.md "../../../STS/latest/APIReference/API_AssumeRoleWithWebIdentity.md") directly. For more information, see [Identity pools authentication flow](authentication-flow.md "authentication-flow.md").
8. Under **Tags**, choose **Add tag** if you want to
   apply [tags](../../../general/latest/gr/aws_tagging.md "../../../general/latest/gr/aws_tagging.md")
   to your identity pool.
9. In **Review and create**, confirm the selections that you made for
   your new identity pool. Select **Edit** to return to the wizard and
   change any settings. When you're done, select **Create identity
   pool**.

## Set up an SDK

To use Amazon Cognito identity pools, set up AWS Amplify, the AWS SDK for Java, or the SDK for .NET. For
more information, see the following topics.

- [Setting up the
  SDK for JavaScript](../../../sdk-for-javascript/v2/developer-guide/setting-up.md "../../../sdk-for-javascript/v2/developer-guide/setting-up.md") in the _AWS SDK for JavaScript
  Developer Guide_
- [Amplify Documentation](https://docs.amplify.aws/ "https://docs.amplify.aws/") in the
  _Amplify Dev Center_
- [Amazon Cognito credentials provider](../../../sdk-for-net/v3/developer-guide/cognito-creds-provider.md "../../../sdk-for-net/v3/developer-guide/cognito-creds-provider.md") in the _SDK for .NET Developer Guide_

## Integrate the identity providers

Amazon Cognito identity pools (federated identities) support user authentication through Amazon Cognito
user pools, federated identity providers—including Amazon, Facebook, Google, Apple,
and SAML identity providers—and unauthenticated identities. This feature also
supports [Developer-authenticated identities](developer-authenticated-identities.md "developer-authenticated-identities.md"), which lets you register and authenticate
users via your own backend authentication process.

To learn more about using an Amazon Cognito user pool to create your own user directory, see
[Amazon Cognito user pools](cognito-user-pools.md "cognito-user-pools.md")
and [Accessing
AWS services using an identity pool after sign-in](amazon-cognito-integrating-user-pools-with-identity-pools.md "amazon-cognito-integrating-user-pools-with-identity-pools.md").

To learn more about using external identity providers, see [Identity pools third-party identity
providers](external-identity-providers.md "external-identity-providers.md").

To learn more about integrating your own backend authentication process, see [Developer-authenticated identities](developer-authenticated-identities.md "developer-authenticated-identities.md").

## Get credentials

Amazon Cognito identity pools provide temporary AWS credentials for users who are guests
(unauthenticated) and for users who have authenticated and received a token. With those
AWS credentials, your app can securely access a backend in AWS or outside AWS through
Amazon API Gateway. See [Getting credentials](getting-credentials.md "getting-credentials.md").
