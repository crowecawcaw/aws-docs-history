# Essentials plan features

The Essentials feature plan has most of the best and latest features of Amazon Cognito user pools. When
you switch from the Lite to the Essentials plan, you get new features for your managed login
pages, multi-factor authentication with email-message one-time passwords, an enhanced
password policy, and custom access tokens. To stay up-to-date with new user pool features,
choose the Essentials plan for your user pools.

The sections that follows present a brief overview of the features that you can add to
your application with the Essentials plan. For detailed information, see the following
pages.

###### Additional resources

- Access token customization: [Pre token generation Lambda
  trigger](user-pool-lambda-pre-token-generation.md "user-pool-lambda-pre-token-generation.md")
- Email MFA: [SMS and email message
  MFA](user-pool-settings-mfa-sms-email-message.md "user-pool-settings-mfa-sms-email-message.md")
- Password history: [Passwords, account recovery, and password
  policies](managing-users-passwords.md "managing-users-passwords.md")
- Enhanced UI: [Apply branding to managed login pages](managed-login-branding.md "managed-login-branding.md")

###### Topics

- [Access token customization](#features-access-token-customization "#features-access-token-customization")
- [Email MFA](#features-email-mfa "#features-email-mfa")
- [Password reuse prevention](#features-password-reuse "#features-password-reuse")
- [Managed login hosted sign-in and authorization
  server](#features-enhanced-ui "#features-enhanced-ui")
- [Choice-based authentication](#features-user-auth "#features-user-auth")

## Access token customization

User pool [access tokens](https://datatracker.ietf.org/doc/html/rfc6749#section-1.4 "https://datatracker.ietf.org/doc/html/rfc6749#section-1.4") grant permissions to applications: to [access an API](cognito-user-pools-define-resource-servers.md "cognito-user-pools-define-resource-servers.md"), to retrieve
user attributes from the [userInfo endpoint](userinfo-endpoint.md "userinfo-endpoint.md"), or to
establish [group membership](cognito-user-pools-user-groups.md "cognito-user-pools-user-groups.md") for an
external system. In advanced scenarios, you might want to add to the default access-token
data from the user pool directory with additional temporary parameters that your
application determines at runtime. For example, you might want to verify a user's API
permissions with [Amazon Verified Permissions](amazon-cognito-authorization-with-avp.md "amazon-cognito-authorization-with-avp.md")
and adjust the scopes in the access token accordingly.

The Essentials plan adds to the existing functions of a [pre token generation trigger](user-pool-lambda-pre-token-generation.md "user-pool-lambda-pre-token-generation.md").
With lower-tier plans, you can customize ID tokens with additional claims, roles, and
group membership. Essentials adds new versions of the trigger input event that customize
access token claims, roles, group membership, and scopes. Access token customization is
available to machine-to-machine (M2M) [client credentials grants](federation-endpoints-oauth-grants.md "federation-endpoints-oauth-grants.md") with event version three.

###### To customize access tokens

1. Select the Essentials or Plus feature plan.
2. Create a Lambda function for your trigger. To use our example function, [configure it for
   Node.js](../../../lambda/latest/dg/lambda-nodejs.md "../../../lambda/latest/dg/lambda-nodejs.md").
3. Populate your Lambda function with our [example code](user-pool-lambda-pre-token-generation.md#aws-lambda-triggers-pre-token-generation-example-version-2-overview "user-pool-lambda-pre-token-generation.md#aws-lambda-triggers-pre-token-generation-example-version-2-overview") or compose your own. You function must process a request object
   from Amazon Cognito and return the changes that you want to include.
4. Assign your new function as a [version two or
   three](user-pool-lambda-pre-token-generation.md#user-pool-lambda-pre-token-generation-event-versions "user-pool-lambda-pre-token-generation.md#user-pool-lambda-pre-token-generation-event-versions") pre token generation trigger. Version two events customize access
   tokens for user identities. Version three customizes access tokens for user and
   machine identities.

###### Learn more

- [Customizing the
  access token](user-pool-lambda-pre-token-generation.md#user-pool-lambda-pre-token-generation-accesstoken "user-pool-lambda-pre-token-generation.md#user-pool-lambda-pre-token-generation-accesstoken")
- [How to customize access tokens in Amazon Cognito user pools](https://aws.amazon.com/blogs/security/how-to-customize-access-tokens-in-amazon-cognito-user-pools/ "https://aws.amazon.com/blogs/security/how-to-customize-access-tokens-in-amazon-cognito-user-pools/")

## Email MFA

Amazon Cognito user pools can be configured to use email as the second factor in multi-factor
authentication (MFA). With email MFA, Amazon Cognito can send users an email with a verification
code that they must enter to complete the authentication process. This adds an important
extra layer of security to the user login flow. To enable email-based MFA, the user pool
must be configured to use the [Amazon SES
email-sending configuration](user-pool-email.md#user-pool-email-developer "user-pool-email.md#user-pool-email-developer") instead of the default email configuration.

When your user selects MFA by email message, Amazon Cognito will send a one-time verification
code to the user's registered email address whenever they attempt to sign in. The user
must then provide this code back to your user pool to complete the authentication flow and
gain access. This ensures that even if a user's username and password are compromised,
they must provide an additional factor—the emailed code—before they can
access your application resources.

For more information, see [SMS and email message
MFA](user-pool-settings-mfa-sms-email-message.md "user-pool-settings-mfa-sms-email-message.md"). The following is an overview of
how to set up your user pool and users for email MFA.

###### To set up email MFA in the Amazon Cognito console

1. Select the Essentials or Plus feature plan.
2. In the **Sign-in** menu of your user pool, edit
   **Multi-factor authentication**.
3. Choose the level of **MFA enforcement** that you want to set up.
   With **Require MFA**, users in the API automatically receive a
   challenge to set up, confirm, and sign in with MFA. In user pools that require MFA,
   managed login prompts them to choose and set up an MFA factor. With **Optional
   MFA**, your application must offer users the option to set up MFA and set
   the user's preference for email MFA.
4. Under **MFA methods**, select **Email message**
   as one of the options.

###### Learn more

- [SMS and email message
  MFA](user-pool-settings-mfa-sms-email-message.md "user-pool-settings-mfa-sms-email-message.md")

## Password reuse prevention

By default, a Amazon Cognito user pools password policy sets password length and character-type
requirements, and temporary-password expiration. The Essentials plan adds the capability
to enforce password history. When a user attempts to reset their password, your user pool
can prevent them from setting it to a previous password. For more information about
configuring the password policy, see [Adding user pool password requirements](managing-users-passwords.md#user-pool-settings-policies "managing-users-passwords.md#user-pool-settings-policies"). The following is an overview of how to set up
your user pool with a password-history policy.

###### To set up password history in the Amazon Cognito console

1. Select the Essentials or Plus feature plan.
2. In the **Authentication methods** menu of your user pool, locate
   **Password policy** and select **Edit**.
3. Configure other available options and set a value for **Prevent use of
   previous passwords**.

###### Learn more

- [Passwords, account recovery, and password
  policies](managing-users-passwords.md "managing-users-passwords.md")

## Managed login hosted sign-in and authorization

server

Amazon Cognito user pools have optional webpages that support the following functions: an OpenID Connect
(OIDC) IdP, a service provider or relying party to third-party IdPs, and public
user-interactive pages for sign-up and sign-in. These pages are collectively called
_managed login_. When you choose a domain for your user
pool, Amazon Cognito automatically activates these pages. Where the Lite plan has the hosted UI,
the Essentials plan opens up this advanced version of sign-up and sign-in pages.

Managed login pages have a clean, up-to-date interface with more features and options
for customizing your branding and styles. The Essentials plan is the lowest plan level
that unlocks access to managed login.

###### To set up managed login in the Amazon Cognito console

1. From the **Settings** menu, select the Essentials or Plus feature
   plan.
2. From the **Domain** menu, [Assign a domain](cognito-user-pools-assign-domain.md "cognito-user-pools-assign-domain.md") to your user pool
   and select a **Branding version** of **Managed
   login**.
3. From the **Managed login** menu, under
   **Styles** tab, choose **Create a style** and
   assign the style to an app client, or create a new app client.

###### Learn more

- [User pool managed login](cognito-user-pools-managed-login.md "cognito-user-pools-managed-login.md")

## Choice-based authentication

The Essentials tier introduces a new _authentication
flow_ for authentication operations in the enhanced UI and SDK-based API
operations.This flow is _choice-based authentication_.
Choice-based authentication is a method where your users' authentication starts not with
an application-side declaration of a sign-in method, but a query of possible sign-in
methods followed by a choice. You can configure your user pool to support choice-based
authentication and unlock username-password, passwordless, and passkey authentication. In
the API, this is the `USER_AUTH` flow.

###### To set up choice-based authentication in the Amazon Cognito console

1. Select the Essentials or Plus feature plan.
2. In the **Sign-in** menu of your user pool, edit **Options
   for choice-based sign-in**. Select and configure the authentication methods
   you want to enable in choice-based authentication.
3. In the **Authentication methods** menu of your user pool, edit
   the configuration of sign-in operations.

###### Learn more

- [Authentication with Amazon Cognito user pools](authentication.md "authentication.md")
