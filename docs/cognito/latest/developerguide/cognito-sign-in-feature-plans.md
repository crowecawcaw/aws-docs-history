# User pool feature plans

Understanding the cost is a crucial step in preparing to implement Amazon Cognito user pools
authentication. Amazon Cognito has feature plans for user pools. Each plan has a
set of features and a monthly cost per active user. Each feature plan unlocks access to more
features than the one before it.

User pools have a variety of features that you can turn on and off. For example, you can
turn on multi-factor authentication (MFA) and turn off sign-in with third-party identity
providers (IdPs). Some changes require you to switch your feature plan. The following
characteristics of your user pool determine the cost that AWS bills you monthly for
usage.

- The features that you choose
- The requests per second that your application makes to the user pools API
- The number of users with authentication, update, or query activity in a month, also
  called [monthly active users](quotas.md#monthly-active-users "quotas.md#monthly-active-users") or MAUs
- The number of monthly active users from third-party SAML 2.0 or OpenID Connect (OIDC)
  IdPs
- The number of app clients and user pools that do client-credentials grants for
  machine-to-machine authorization
  For the most current information about user pool pricing, see [Amazon Cognito pricing](https://aws.amazon.com/cognito/pricing "https://aws.amazon.com/cognito/pricing").

Feature-plan selections apply to one user pool. Different user pools in the same
AWS account can have different plan selections. You can't apply separate feature plans to
app clients within a user pool. The default plan selection for new user pools is
Essentials.

You can switch between feature plans at any time to fit the requirements of your
applications. Some changes between plans require that you turn off active features. For more
information, see [Turning off features to change feature
plans](feature-plans-deactivate.md "feature-plans-deactivate.md").

###### User pool feature plans

**Lite**

Lite is a low-cost feature plan for user pools with lower numbers of monthly active
users. This plan is sufficient for user directories with basic authentication features.
It includes sign-in features and the classic hosted UI, a slimmer, less-customizable
predecessor to managed login. Many newer features, like access-token customization and
passkey authentication, aren't included in the Lite plan.

**Essentials**

Essentials has all of the latest user pool authentication features. This plan adds
new options to your applications, whether your login pages are managed login or
custom-built. Essentials has advanced authentication features like [choice-based sign-in](authentication-flows-selection-sdk.md#authentication-flows-selection-choice "authentication-flows-selection-sdk.md#authentication-flows-selection-choice") and [email MFA](user-pool-settings-mfa-sms-email-message.md "user-pool-settings-mfa-sms-email-message.md").

**Plus**

Plus includes everything in the Essentials plan and adds advanced security features
that protect your users. Monitor user sign-in, sign-up, and password-management requests
for indicators of compromise. For example, user pools can detect whether users are
signing in from an unexpected location or using a password that's been part of a public
breach.

User pools with the Plus plan generate logs of user activity details and risk
evaluations. You can apply your own usage and security analysis to these logs when you
export them to external services.

###### Note

Previously, some user pool features were included in an _advanced
security features_ pricing structure. The features that were included in this
structure are now under either the Essentials or Plus plan.

###### Topics

- [Select a feature plan](#cognito-sign-in-feature-plans-choose "#cognito-sign-in-feature-plans-choose")
- [Features by plan](#cognito-sign-in-feature-plans-list "#cognito-sign-in-feature-plans-list")
- [Essentials plan features](feature-plans-features-essentials.md "feature-plans-features-essentials.md")
- [Plus plan features](feature-plans-features-plus.md "feature-plans-features-plus.md")
- [Turning off features to change feature
  plans](feature-plans-deactivate.md "feature-plans-deactivate.md")

## Select a feature plan

AWS Management Console
To choose a feature plan

1. Go to the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home").
   If prompted, enter your AWS credentials.
2. Choose **User Pools**.
3. Choose an existing user pool from the list, or create a user pool.
4. Select the **Settings** menu and review the **Feature
   plans** tab.
5. Review the features available to you in the Lite, Esssentials, and Plus
   plans.
6. To change your plan, select **Switch to Essentials**, or
   **Switch to Plus**. To switch to the **Lite**
   plan, choose **Other plans**, then **Compare with
   Lite**.
7. On the next screen, review your choice and select
   **Confirm**.

CLI/API/SDK
The [CreateUserPool](../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md "../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md") and [UpdateUserPool](../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserPool.md "../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserPool.md") operations set your feature plan in the
`UserPoolTier` parameter. When you don't specify a value for
`UserPoolTier`, your user pool defaults to `Essentials`. If
you set `AdvancedSecurityMode` to `AUDIT` or
`ENFORCED`, your user pool tier must be `PLUS` and default to
`PLUS` when not specified.

See [Examples in CreateUserPool](../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md#API_CreateUserPool_Examples "../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md#API_CreateUserPool_Examples") for syntax. See [See Also in CreateUserPool](../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md#API_CreateUserPool_SeeAlso "../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md#API_CreateUserPool_SeeAlso") for links to this function in of AWS SDKs for
a variety of programming languages.

```
"UserPoolTier": "PLUS"
```

In the AWS CLI, this option is `--user-pool-tier` argument.

```
--user-pool-tier PLUS
```

See [create-user-pool](../../../cli/latest/reference/cognito-idp/create-user-pool.md "../../../cli/latest/reference/cognito-idp/create-user-pool.md") and [update-user-pool](../../../cli/latest/reference/cognito-idp/update-user-pool.md "../../../cli/latest/reference/cognito-idp/update-user-pool.md") in the AWS CLI command reference for more
information.

## Features by plan

| Features and plans in user pools                               | Feature                                                                                                                                                                   | Description              | Feature plan |
| -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ | ------------ |
| Protect against unsafe passwords                               | Check plaintext passwords for indicators of compromise at runtime                                                                                                         | Plus                     |
| Protect against malicious sign-in attempts                     | Check session properties for indicators of compromise at runtime                                                                                                          | Plus                     |
| Log and analyze user activity                                  | Generate logs of user authentication session properties and risk scores                                                                                                   | Plus                     |
| Export user activity logs                                      | Push user session and risk logs to an external AWS service                                                                                                                | Plus                     |
| Customize managed login pages with a visual editor             | Use a visual editor in the Amazon Cognito console to apply branding and style to your managed login pages                                                                 | Essentials + Plus        |
| MFA with email one-time codes                                  | Request or require local users to provide an additional email message sign-in factor after username authentication                                                        | Essentials + Plus        |
| Customize access token scopes and claims at runtime            | Use a Lambda trigger to extend the authorization capabilities of user pool access tokens                                                                                  | Essentials + Plus        |
| Passwordless sign-in with one-time codes                       | Permit users to receive a one-time password by email or SMS as their first authentication factor                                                                          | Essentials + Plus        |
| Passkey sign-in with hardware or software FIDO2 authenticators | Permit users to use a cryptographic key stored on a FIDO2 authenticator as their first authentication factor                                                              | Essentials + Plus        |
| Sign-up and sign-in                                            | Perform authentication operations and let new users register for an account in your application.                                                                          | Lite + Essentials + Plus |
| User groups                                                    | Create logical groupings of users and assign default IAM roles for identity pool operations.                                                                              | Lite + Essentials + Plus |
| Sign-in with social, SAML, and OIDC providers                  | Provide users with the options to sign in directly or with their preferred provider.                                                                                      | Lite + Essentials + Plus |
| OAuth 2.0/OIDC authorization server                            | Act as a OIDC issuer.                                                                                                                                                     | Lite + Essentials + Plus |
| Login pages                                                    | A hosted collection of webpages for authentication. Managed login is available in the Essentials and Plus tiers. The classic hosted UI is available in all feature tiers. | Lite + Essentials + Plus |
| Password, custom, refresh-token, and SRP authentication        | Prompt users for a username and password in your application.                                                                                                             | Lite + Essentials + Plus |
| Machine-to-machine (M2M) with client credentials               | Issue access tokens for authorization of non-human entities.                                                                                                              | Lite + Essentials + Plus |
| API authorization with resource servers                        | Issue access tokens with custom scopes that authorize access to external systems.                                                                                         | Lite + Essentials + Plus |
| User import                                                    | Set up import jobs from CSV files and perform just-in-time migration of users as they sign in.                                                                            | Lite + Essentials + Plus |
| MFA with authenticator apps and SMS one-time codes             | Request or require local users to provide an additional SMS message or authenticator app sign-in factor after username authentication                                     | Lite + Essentials + Plus |
| Customize ID token scopes and claims at runtime                | Use a Lambda trigger to extend the authentication capabilities of user pool identity (ID) tokens                                                                          | Lite + Essentials + Plus |
| Custom runtime actions with Lambda triggers                    | Customize the sign-in process at runtime with Lambda functions that perform external actions and influence authentication                                                 | Lite + Essentials + Plus |
| Customize managed login pages with CSS                         | Download a CSS template and change some styles in your managed login pages                                                                                                | Lite + Essentials + Plus |
