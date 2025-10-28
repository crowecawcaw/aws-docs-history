# Configure authentication methods

for managed login

You can invoke [managed login
pages](cognito-user-pools-managed-login.md "cognito-user-pools-managed-login.md"), a web front end for user pool authentication, when you want users to sign in,
sign out, or reset their password. In this model, your application imports OIDC libraries to
process browser-based authentication attempts with user pool managed login pages. The forms of
authentication that are available to your users are dependent on the configuration of your
user pool and your app client. Implement the `ALLOW_USER_AUTH` flow in your app
client, and Amazon Cognito prompts users to select a sign-in method from the available options.
Implement `ALLOW_USER_PASSWORD_AUTH` and assign a SAML provider, and your login
pages prompt users with the option to enter their username and password or to connect with
their IdP.

The Amazon Cognito user pools console can get you started with setting up managed login authentication for
your application. When you create a new user pool, specify the platform you're developing for
and the console gives you examples for implementation of OIDC and OAuth libraries with starter
code to implement sign-in and sign-out flows. You can build managed login with many OIDC
relying-party implementations. We recommend that you work with [certified OIDC
relying party libraries](https://openid.net/developers/certified-openid-connect-implementations/ "https://openid.net/developers/certified-openid-connect-implementations/") where possible. For more information, see [Getting started with user pools](getting-started-user-pools.md "getting-started-user-pools.md").

Typically, OIDC relying party libraries preiodically check the
`.well-known/openid-configuration` endpoint of your user pool to determine issuer
URLs like the token endpoint and authorization endpoint. As a best practice, implement this
automatic-discovery behavior where you have to option to. Manual configuration of issuer
endpoints introduces potential for error. For example, you might change your user pool domain.
The path to `openid-configuration` isn't linked to your user pool domain, so
applications that autodiscover service endpoints will automatically pick up your domain
change.

## User pool settings

for managed login

You might want to allow sign in with multiple providers for your application, or you might
want to use Amazon Cognito as an independent user directory. You might also want to collect user
attributes, set up and prompt for MFA, or require email addresses as usernames. You can't
directly edit the fields in managed login and the hosted UI. Instead, the configuration of
your user pool automatically sets the handling of managed-login authentication flows.

The following user pool configuration items determine the authentication methods that
Amazon Cognito presents to users in managed login and the hosted UI.

User pool options (Sign-in menu)
The following options are in the **Sign-in** menu of a user pool in
the Amazon Cognito console.

###### Cognito user pool sign-in options

Has options for usernames. Your managed login and hosted UI pages only accept
usernames in the formats that you select. When you, for example, set up a user pool
with **Email** as the only sign-in option, your managed login pages
only accept usernames in an email format.

###### Required attributes

When you set an attribute as required in your user pool, managed login prompts
users for a value for that attribute when they sign up.

###### Options for choice-based sign-in

Has settings for authentication methods in [Choice-based authentication](authentication-flows-selection-sdk.md#authentication-flows-selection-choice "authentication-flows-selection-sdk.md#authentication-flows-selection-choice"). Here, you can turn on or off
authentication methods like [passkey](amazon-cognito-user-pools-authentication-flow-methods.md#amazon-cognito-user-pools-authentication-flow-methods-passkey "amazon-cognito-user-pools-authentication-flow-methods.md#amazon-cognito-user-pools-authentication-flow-methods-passkey") and [passwordless](amazon-cognito-user-pools-authentication-flow-methods.md#amazon-cognito-user-pools-authentication-flow-methods-passwordless "amazon-cognito-user-pools-authentication-flow-methods.md#amazon-cognito-user-pools-authentication-flow-methods-passwordless"). These methods are only available to user pools with [managed login domains](managed-login-branding.md "managed-login-branding.md") and [feature plans](cognito-sign-in-feature-plans.md "cognito-sign-in-feature-plans.md") above the
**Lite** tier.

###### Multi-factor authentication

Managed login and the hosted UI handle registration and authentication operations
for [MFA](user-pool-settings-mfa.md "user-pool-settings-mfa.md"). When MFA is required in your
user pool, your sign-in pages automatically prompt users to set up their additional
factor. They also prompt users who have an MFA configuration to complete
authentication with an MFA code. When MFA is off or optional in your user pool, your
sign-in pages don't prompt to set up MFA.

###### User account recovery

The self-service account
recovery setting of your user pool determines whether your sign-in pages
display a link where users can reset their password.

User pool options (Domain menu)
The following options are in the **Domain** menu of a user pool in
the Amazon Cognito console.

###### Domain

Your choice of a user pool domain sets the path for the link that users open when
you invoke their browsers for authentication.

###### Branding version

Your choice of a branding version determines whether your user pool domain
displays managed login or the hosted UI.

User pool options (Social and external providers menu)
The following option is in the **Social and external providers**
menu of a user pool in the Amazon Cognito console.

###### Providers

The identity providers (IdPs) that you add to your user pool can be left active or
inactive for each app client in the user pool.

App client options
The following options are in the **App clients** menu of a user
pool in the Amazon Cognito console. To review these options, select an app client from the
list.

###### Quick setup guide

The quick setup guide has code examples for a variety of developer environments.
They contain the libraries necessary to integrate managed login authentication with
your application.

###### App client information

Edit this configuration to set assigned IdPs for the application that's
represented by the current app client. On the managed login pages, Amazon Cognito displays
choices for users. These choices are determined from the assigned methods and IdP. For
example, if you assign a SAML 2.0 IdP named `MySAML` and local user pool
login, your managed login pages display authentication-method prompts and a button for
`MySAML`.

###### Authentication settings

Edit this configuration to set authentication methods for your application. On the
managed login pages, Amazon Cognito displays choices for users. These choices are determined
from the availability of the user pool as an IdP, and from the methods that you
assign. For example, if you assign choice-based `ALLOW_USER_AUTH`
authentication, your managed login pages display available choices like entering an
email address and signing in with a passkey. Managed login pages also render buttons
for the assigned IdPs.

###### Login pages

Set the visual effect of your managed login or hosted UI user-interactive pages
with the options available in this tab. For more information, see [Apply branding to managed login pages](managed-login-branding.md "managed-login-branding.md").
