# Amazon Cognito user pools

An Amazon Cognito user pool is a user directory for web and mobile app authentication and
authorization. From the perspective of your app, an Amazon Cognito user pool is an OpenID Connect (OIDC)
identity provider (IdP). A user pool adds layers of additional features for security, identity
federation, app integration, and customization of the user experience.

You can, for example, verify that your users’ sessions are from trusted sources. You can
combine the Amazon Cognito directory with an external identity provider. With your preferred AWS SDK,
you can choose the API authorization model that works best for your app. And you can add
AWS Lambda functions that modify or overhaul the default behavior of Amazon Cognito.

![A diagram with a high-level overview of how user pools work. Clients can sign in with applications build using an AWS SDK or with the OIDC IdP built in to user pools. User pools also unify sign-in processes for multiple social, OpenID Connect, and SAML 2.0 identity providers.](images/scenario-authentication-cup.png)

###### Topics

- [Features](#cognito-user-pools-features "#cognito-user-pools-features")
- [User pool feature plans](cognito-sign-in-feature-plans.md "cognito-sign-in-feature-plans.md")
- [Security best practices for Amazon Cognito user pools](user-pool-security-best-practices.md "user-pool-security-best-practices.md")
- [Authentication with Amazon Cognito user pools](authentication.md "authentication.md")
- [User pool sign-in with third party
  identity providers](cognito-user-pools-identity-federation.md "cognito-user-pools-identity-federation.md")
- [User pool managed login](cognito-user-pools-managed-login.md "cognito-user-pools-managed-login.md")
- [Customizing user pool
  workflows with Lambda triggers](cognito-user-pools-working-with-lambda-triggers.md "cognito-user-pools-working-with-lambda-triggers.md")
- [Managing users in your user pool](managing-users.md "managing-users.md")
- [Understanding
  user pool JSON web tokens (JWTs)](amazon-cognito-user-pools-using-tokens-with-identity-providers.md "amazon-cognito-user-pools-using-tokens-with-identity-providers.md")
- [Accessing resources after successful sign-in](accessing-resources.md "accessing-resources.md")
- [Scopes, M2M, and resource
  servers](cognito-user-pools-define-resource-servers.md "cognito-user-pools-define-resource-servers.md")
- [Configure user pool features](user-pools-configure-features.md "user-pools-configure-features.md")
- [Using Amazon Cognito user pools security features](managing-security.md "managing-security.md")
- [User pool endpoints and
  managed login reference](cognito-userpools-server-contract-reference.md "cognito-userpools-server-contract-reference.md")

## Features

Amazon Cognito user pools have the following features.

### Sign-up

Amazon Cognito user pools have user-driven, administrator-driven, and programmatic methods to add user
profiles to your user pool. Amazon Cognito user pools supports the following sign-up models. You can use any
combination of these models in your app.

###### Important

If you activate user sign-up in your user pool, anyone on the internet can
sign up for an account and sign into your apps. Don't enable self-registration
in your user pool unless you want to open your app to public
sign-up. To change this setting, update **Self-service sign-up**
in the **Sign-up** menu under **Authentication**
in the user pool console, or update the value of [AllowAdminCreateUserOnly](../../../cognito-user-identity-pools/latest/APIReference/API_AdminCreateUserConfigType.md#CognitoUserPools-Type-AdminCreateUserConfigType-AllowAdminCreateUserOnly "../../../cognito-user-identity-pools/latest/APIReference/API_AdminCreateUserConfigType.md#CognitoUserPools-Type-AdminCreateUserConfigType-AllowAdminCreateUserOnly") in a [CreateUserPool](../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md "../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md") or [UpdateUserPool](../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserPool.md "../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserPool.md") API request.

For information about security features that you
can set up in your user pools, see [Using Amazon Cognito user pools security features](managing-security.md "managing-security.md").

1. Your users can enter their information in your app and create a user profile that’s
   native to your user pool. You can call API sign-up operations to register users in your
   user pool. You can open these sign-up operations to anyone, or you can authorize them
   with a client secret or AWS credentials.
2. You can redirect users to a third-party IdP that they can authorize to pass their
   information to Amazon Cognito. Amazon Cognito processes OIDC id tokens, OAuth 2.0 `userInfo`
   data, and SAML 2.0 assertions into user profiles in your user pool. You control the
   attributes that you want Amazon Cognito to receive based on attribute-mapping rules.
3. You can skip public or federated sign-up, and create users based on your own data
   source and schema. Add users directly in the Amazon Cognito console or API. Import users from a
   CSV file. Run a just-in-time AWS Lambda function that looks up your new user in an
   existing directory, and populates their user profile from existing data.

After your users sign up, you can add them to groups that Amazon Cognito lists in the access and
ID tokens. You can also link user pool groups to IAM roles when you pass the ID token to
an identity pool.

###### Related topics

- [Managing users in your user pool](managing-users.md "managing-users.md")
- [Understanding API, OIDC, and managed login pages
  authentication](authentication-flows-public-server-side.md#user-pools-API-operations "authentication-flows-public-server-side.md#user-pools-API-operations")
- [Code examples for Amazon Cognito Identity Provider using AWS SDKs](service_code_examples_cognito-identity-provider.md "service_code_examples_cognito-identity-provider.md")

### Sign-in

Amazon Cognito can be a standalone user directory and identity provider (IdP) to your app. Your
users can sign in with managed login pages that are hosted by Amazon Cognito, or with a custom-built
user authentication service through the Amazon Cognito user pools API. The application tier behind your
custom-built front end can authorize requests on the back end with any of several methods to
confirm legitimate requests.

Users can set up and sign with usernames and passwords, passkeys, and email and SMS
message one-time passwords. You can offer consolidate sign in with external user
directories, multi-factor authentication (MFA) after sign-in, trust remembered devices, and
custom authentication flows that you design.

To sign in users with an external directory, optionally combined with the user directory
built in to Amazon Cognito, you can add the following integrations.

1. Sign in and import customer user data with OAuth 2.0 social sign-in. Amazon Cognito supports
   sign-in with Google, Facebook, Amazon, and Apple through OAuth 2.0.
2. Sign in and import work and school user data with SAML and OIDC sign-in. You can
   also configure Amazon Cognito to accept claims from any SAML or OpenID Connect (OIDC) identity
   provider (IdP).
3. Link external user profiles to native user profiles. A linked user can sign in with
   a third-party user identity and receive access that you assign to a user in the built-in
   directory.

###### Related topics

- [User pool sign-in with third party
  identity providers](cognito-user-pools-identity-federation.md "cognito-user-pools-identity-federation.md")
- [Linking
  federated users to an existing user profile](cognito-user-pools-identity-federation-consolidate-users.md "cognito-user-pools-identity-federation-consolidate-users.md")

###### Machine-to-machine authorization

Some sessions aren’t a human-to-machine interaction. You might need a service account
that can authorize a request to an API by an automated process. To generate access tokens
for machine-to-machine authorization with OAuth 2.0 scopes, you can add an app client that
generates [client-credentials grants](https://www.rfc-editor.org/rfc/rfc6749#section-4.4 "https://www.rfc-editor.org/rfc/rfc6749#section-4.4").

###### Related topics

- [Scopes, M2M, and resource
  servers](cognito-user-pools-define-resource-servers.md "cognito-user-pools-define-resource-servers.md")

### Managed login

When you don’t want to build a user interface, you can present your users with a
customized managed login pages. Managed login is a set of web pages for sign-up, sign-in,
multi-factor authentication (MFA), and password reset. You can add managed login to your
existing domain, or use a prefix identifier in an AWS subdomain.

###### Related topics

- [User pool managed login](cognito-user-pools-managed-login.md "cognito-user-pools-managed-login.md")
- [Configuring a user pool domain](cognito-user-pools-assign-domain.md "cognito-user-pools-assign-domain.md")

### Security

Your local users can provide an additional authentication factor with a code from an SMS
or email message, or an app that generates multi-factor authentication (MFA) codes. You can
build mechanisms to set up and process MFA in your application, or you can let managed login
manage it. Amazon Cognito user pools can bypass MFA when your users sign in from trusted
devices.

If you don’t want to initially require MFA from your users, you can require it
conditionally. With adaptive authentication, Amazon Cognito can detect potential malicious activity
and require your user to set up MFA, or block sign-in.

If network traffic to your user pool might be malicious, you can monitor it and take
action with AWS WAF web ACLs.

###### Related topics

- [Adding MFA to a user pool](user-pool-settings-mfa.md "user-pool-settings-mfa.md")
- [Advanced security with threat
  protection](cognito-user-pool-settings-threat-protection.md "cognito-user-pool-settings-threat-protection.md")
- [Associate an AWS WAF web ACL with a user pool](user-pool-waf.md "user-pool-waf.md")

### Custom user experience

At most stages of a user’s sign-up, sign-in, or profile update, you can customize how
Amazon Cognito handles the request. With Lambda triggers, you can modify an ID token or reject a
sign-up request based on custom conditions. You can create your own custom authentication
flow.

You can upload custom CSS and logos to give managed login a familiar look and feel to
your users.

###### Related topics

- [Customizing user pool
  workflows with Lambda triggers](cognito-user-pools-working-with-lambda-triggers.md "cognito-user-pools-working-with-lambda-triggers.md")
- [Custom authentication challenge Lambda
  triggers](user-pool-lambda-challenge.md "user-pool-lambda-challenge.md")
- [Apply branding to managed login pages](managed-login-branding.md "managed-login-branding.md")

### Monitoring and

analytics

Amazon Cognito user pools log API requests, including requests to managed login, to AWS CloudTrail. You can
review performance metrics in Amazon CloudWatch Logs, push custom logs to CloudWatch with Lambda triggers,
monitor email and SMS message delivery, and monitor API request volume in the Service Quotas
console.

With the Plus [feature plan](cognito-sign-in-feature-plans.md "cognito-sign-in-feature-plans.md"), you can
monitor user authentication attempts for indicators of compromise with automated-learning
technology and immediately remediate risks. These advanced security features also log user
activity to your user pool and optionally, to Amazon S3, CloudWatch Logs, or Amazon Data Firehose.

You can also log device and session data from your API requests to an Amazon Pinpoint
campaign. With Amazon Pinpoint, you can send push notifications from your app based on your analysis
of user activity.

###### Related topics

- [Amazon Cognito logging in AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md")
- [Tracking quotas
  and usage in CloudWatch and Service Quotas](tracking-quotas-and-usage-in-cloud-watch-and-service-quotas.md "tracking-quotas-and-usage-in-cloud-watch-and-service-quotas.md")
- [Exporting logs from Amazon Cognito user pools](exporting-quotas-and-usage.md "exporting-quotas-and-usage.md")
- [Using Amazon Pinpoint for user pool
  analytics](cognito-user-pools-pinpoint-integration.md "cognito-user-pools-pinpoint-integration.md")

### Amazon Cognito identity

pools integration

The other half of Amazon Cognito is identity pools. Identity pools provide credentials that
authorize and monitor API requests to AWS services, for example Amazon DynamoDB or Amazon S3, from
your users. You can build identity-based access policies that protect your data based on how
you classify the users in your user pool. Identity pools can also accept tokens and SAML 2.0
assertions from a variety of identity providers, independently of user pool
authentication.

###### Related topics

- [Accessing
  AWS services using an identity pool after sign-in](amazon-cognito-integrating-user-pools-with-identity-pools.md "amazon-cognito-integrating-user-pools-with-identity-pools.md")
- [Amazon Cognito identity pools](cognito-identity.md "cognito-identity.md")
