# Creating user accounts as administrator

User pools aren't only a customer identity and access management (CIAM) user directory,
where anyone on the internet can sign up for a user profile in your application. You can disable
self-service sign-up. You might already know your customers and want to only admit those who
have been authorized in advance. You can put manual authentication guardrails around your
application with a [private SAML 2.0 or
OIDC identity provider](cognito-user-pools-identity-federation.md "cognito-user-pools-identity-federation.md"), by [importing
users](cognito-user-pools-import-users.md "cognito-user-pools-import-users.md"), by [screening users at
sign-up](user-pool-lambda-pre-sign-up.md "user-pool-lambda-pre-sign-up.md")—or by creating users with administrative API operations. Your workflow
for administrative creation of users can be programmatic, provisioning users after they register
in another system, or it can be on a case-by-case or testing basis in the Amazon Cognito console.

When you create users as an administrator, Amazon Cognito sets a temporary password for them and
sends a welcome, or invitation, message. They can follow the link in their invitation message
and sign in for the first time, setting a password and confirming their account. The page that
follows describes how to create new users and configure the welcome message. For more
information about user creation with the user pools API and an AWS SDK or CDK, see [AdminCreateUser](../../../cognito-user-identity-pools/latest/APIReference/API_AdminCreateUser.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminCreateUser.md").

After you create your user pool, you can create users using the AWS Management Console, as well as the
AWS Command Line Interface or the Amazon Cognito API. You can create a profile for a new user in a user pool and send a
welcome message with sign-up instructions to the user via SMS or email.

The following are some examples of how administrators can manage users in user pools.

- Create a new user profile in the Amazon Cognito console or with the `AdminCreateUser`
  API operation.
- Make username-and-password, passwordless, passkey, and custom [authentication
  flows](amazon-cognito-user-pools-authentication-flow-methods.md "amazon-cognito-user-pools-authentication-flow-methods.md") available to your user pool and app client.
- Set user attribute values.
- Create custom attributes.
- Set the value of immutable [custom
  attributes](user-pool-settings-attributes.md#user-pool-settings-custom-attributes "user-pool-settings-attributes.md#user-pool-settings-custom-attributes") in `AdminCreateUser` API requests. This feature isn't
  available in the Amazon Cognito console.
- Specify a temporary password, create a user without a password, or allow Amazon Cognito to
  automatically generate a password.
- Create new users and automatically confirm their accounts, verify their email addresses,
  or verify their phone numbers.
- Specify custom SMS and email invitation messages for new users via the AWS Management Console or
  Lambda triggers like [custom message](user-pool-lambda-custom-message.md "user-pool-lambda-custom-message.md"),
  [custom SMS sender](user-pool-lambda-custom-sms-sender.md "user-pool-lambda-custom-sms-sender.md"), and [custom email sender](user-pool-lambda-custom-email-sender.md "user-pool-lambda-custom-email-sender.md").
- Specify whether invitation messages are sent via SMS, email, or both.
- Resend the welcome message to an existing user by calling the
  `AdminCreateUser` API, specifying `RESEND` for the
  `MessageAction` parameter.
- [Suppress](#admincreateuserwalkthrough-step-invitationmessage "#admincreateuserwalkthrough-step-invitationmessage") the
  sending of the invitation message when the user is created.
- Specify an expiration time limit of up to 90 days for new user accounts.
- Allow users to sign themselves up or require that new users only be added by the
  administrator.
  Administrators can also sign users in with AWS credentials in a server-side application.
  For more information, see [Authorization models for API and SDK
  authentication](authentication-flows-public-server-side.md "authentication-flows-public-server-side.md").

## User authentication flows and creating

users

Administrative creation of users has options that differ based on the configuration of
your user pool. The _authentication flows_, or methods
available to users for sign-in and MFA, can change how you create users and the messages that
you send to them. The following are some authentication flows that are available in user
pools.

- Username and password
- Passkeys
- Sign-in with third-party IdPs
- Passwordless with email and SMS one-time passwords (OTPs)
- Multi-factor authentication with email, SMS, and authenticator-app OTPs
- Custom authentication with Lambda triggers

For more information about how to configure these sign-in factors, see [Authentication with Amazon Cognito user pools](authentication.md "authentication.md").

## Create users without

passwords

If you have enabled passwordless sign-in for your user pool, you can create users without
passwords. To create a user without a password, you must provide attribute values for an
available passwordless sign-in factor. For example, if email OTP passwordless sign-in is
available in your user pool, you can create a user with no password and an email address
attribute. If the only authentication flows available to new users require a password, for
example passkey or username-password, you must create or generate a temporary password for
each new user.

###### To create a new user without a password

- Choose **Don't set a password** in the Amazon Cognito console
- Omit or leave blank the `TemporaryPassword` parameter of your
  `AdminCreateUser` API request

###### Users without passwords are automatically confirmed

Normally new users get a temporary password and go into a
`FORCE_CHANGE_PASSWORD` status when you create them. When you create users
without passwords, they immediately go into a `CONFIRMED` state. You can't resend
confirmation codes to these users in the `CONFIRMED` state.

###### Invitation messages change for users without passwords.

By default, Amazon Cognito sends an [invitation
message](cognito-user-pool-settings-message-customizations.md#cognito-user-pool-settings-user-invitation-message-customization "cognito-user-pool-settings-message-customizations.md#cognito-user-pool-settings-user-invitation-message-customization") to new users that says `Your username is {userName} and your password
 is {####}.` When you create users with no password, the message says `Your
 username is {userName}.` Customize your invitation message to reflect whether you
will set passwords for users. Omit out the `{####}` password variable in
passwordless authentication models.

###### You can't autogenerate passwords when passwordless factors are available

If you have configured your user pool to support email or phone OTP passwordless
sign-in, you can't automatically generate a password. For each user who will have a
password, you must set a temporary password when you create their profile.

###### Passwordless users must have values for all required attributes

When you create a user _without_ a password, your
request only succeeds if the user provides values for all attributes that you have marked as
required in your user pool. This applies to any required attribute, not only the phone
number and email attributes required for OTP delivery.

## Creating

users who will provide required-attribute values later

You might want to require attributes in your user pool but collect those attributes after
you administratively create users, during user interaction in your application. Administrators
can omit values for required attributes when they create users _with
temporary passwords_. You can't omit required-attribute values for passwordless
users.

Users with missing values for required attributes and a temporary password get a [NEW_PASSWORD_REQUIRED](../../../cognito-user-identity-pools/latest/APIReference/API_RespondToAuthChallenge.md#CognitoUserPools-RespondToAuthChallenge-request-ChallengeResponses "../../../cognito-user-identity-pools/latest/APIReference/API_RespondToAuthChallenge.md#CognitoUserPools-RespondToAuthChallenge-request-ChallengeResponses") challenge at first sign-in. They can then provide a value for
the missing required attributes in the `requiredAttributes` parameter. You can
create users with passwords and without required attributes only if all required attributes
are [mutable](user-pool-settings-attributes.md#user-pool-settings-custom-attributes "user-pool-settings-attributes.md#user-pool-settings-custom-attributes"). Users can only
complete sign-in with `NEW_PASSWORD_REQUIRED` challenges and required-attribute
values if the required attributes are [writeable](user-pool-settings-client-apps.md#cognito-user-pools-app-idp-settings-about "user-pool-settings-client-apps.md#cognito-user-pools-app-idp-settings-about") from the app client
they sign in with.

When you set a permanent password for an administrator-created user, their status changes
to `CONFIRMED` and your user pool doesn't prompt them for a new password _or_ required attributes at their first sign-in.

## Creating a new user in the

AWS Management Console

You can set user password requirements, configure the invitation and verification messages
sent to users, and add new users with the Amazon Cognito console.

### Set a password policy and enable

self-registration

You can configure settings for minimum password complexity and whether users can sign up
using public APIs in your user pool.

###### Configure a password policy

1. Navigate to the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home"),
   and choose **User Pools**.
2. Choose an existing user pool from the list, or [create a user
   pool](cognito-user-pool-as-user-directory.md "cognito-user-pool-as-user-directory.md").
3. Choose the **Authentication methods** menu and locate
   **Password policy**. Choose **Edit**.
4. Choose a **Password policy mode** of
   **Custom**.
5. Choose a **Password minimum length**. For limits to the password
   length requirement, see [User pools
   resource quotas](limits.md#limits-hard "limits.md#limits-hard").
6. Choose a **Password complexity** requirement.
7. Choose how long password set by administrators should be valid for.
8. Choose **Save changes**.

###### Allow self-service sign-up

1. Navigate to the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home"),
   and choose **User Pools**.
2. Choose an existing user pool from the list, or [create a user
   pool](cognito-user-pool-as-user-directory.md "cognito-user-pool-as-user-directory.md").
3. Choose the **Sign-up** menu and locate **Self-service
   sign-up**. Select **Edit**.
4. Choose whether to **Enable self-registration**. Self-registration
   is typically used with public app clients that need to register new users in your user
   pool without distributing a client secret or AWS Identity and Access Management (IAM) API credentials.

###### Disabling self-registration

If you do not enable self-registration, new users must be created by
administrative API actions using IAM API credentials or by sign-in with federated
providers. 5. Choose **Save changes**.

### Customize email and SMS

messages

###### Customize user messages

You can customize the messages that Amazon Cognito sends to your users when you invite them to
sign in, they sign up for a user account, or they sign in and are prompted for
multi-factor authentication (MFA).

###### Note

An **Invitation message** is sent when you create a user in your
user pool and invite them to sign in. Amazon Cognito sends initial sign-in information to the
user's email address or phone number.

A **Verification message** is sent when a user signs up for a user
account in your user pool. Amazon Cognito sends a code to the user. When the user provides the
code to Amazon Cognito, they verify their contact information and confirm their account for
sign-in. Verification codes are valid for 24 hours.

An **MFA message** is sent when you enable SMS MFA in your user
pool, and a user that has configured SMS MFA signs in and is prompted for MFA.

1. Navigate to the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home"),
   and choose **User Pools**.
2. Choose an existing user pool from the list, or [create a user
   pool](cognito-user-pool-as-user-directory.md "cognito-user-pool-as-user-directory.md").
3. Choose the **Message templates** menu and select
   **Verification message**, **Invitation message**, or
   **MFA message** and choose **Edit**.
4. Customize the messages for the chosen message type.

###### Note

All variables in message templates must be included when you customize the
message. If the variable, for example **{####}**, is not included,
your user will have insufficient information to complete the message action.

For more information, see [Message
templates](cognito-user-pool-settings-message-templates.md "cognito-user-pool-settings-message-templates.md"). 5. 1. **Verification messages** 1. Choose a **Verification type** for
**Email** messages. A **Code** verification
sends a numeric code that the user must enter. A **Link**
verification sends a link the user can click to verify their contact
information. The text in the variable for a **Link** message is
displayed as hyperlink text. For example, a message template using the variable
{##Click here##} is displayed as Click here in the email
message. 2. Enter an **Email subject** for **Email**
messages. 3. Enter a custom **Email message** template for
**Email** messages. You can customize this template with
HTML. 4. Enter a custom **SMS message** template for
**SMS** messages. 5. Choose **Save changes**. 2. **Invitation messages** 1. Enter an **Email subject** for **Email**
messages. 2. Enter a custom **Email message** template for
**Email** messages. You can customize this template with
HTML. 3. Enter a custom **SMS message** template for
**SMS** messages. 4. Choose **Save changes**. 3. **MFA messages** 1. Enter a custom **SMS message** template for
**SMS** messages. 2. Choose **Save changes**.

### Create a user

###### Create a user

You can create new users for your user pool from the Amazon Cognito console. Typically, users
can sign in after they set a password. To sign in with an email address, a user must
verify the `email` attribute. To sign in with a phone number, the user must
verify the `phone_number` attribute. To confirm accounts as an administrator,
you can also use the AWS CLI or API, or create user profiles with a federated identity
provider. For more information, see the [Amazon Cognito API Reference](../../../cognitoidentity/latest/APIReference.md "../../../cognitoidentity/latest/APIReference.md").

1. Navigate to the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home"),
   and choose **User Pools**.
2. Choose an existing user pool from the list, or [create a user
   pool](cognito-user-pool-as-user-directory.md "cognito-user-pool-as-user-directory.md").
3. Choose the **Users** menu, and choose **Create a
   user**.
4. Review the **User pool sign-in and security requirements** for
   guidance on password requirements, available account recovery methods, and alias
   attributes for your user pool.
5. Choose how you want to send an **Invitation message**. Choose SMS
   message, email message, or both. To suppress the invitation message, choose
   **Don't send an invitation**.

###### Note

Before you can send invitation messages, configure a sender and an AWS Region
with Amazon Simple Notification Service and Amazon Simple Email Service in the **Authentication methods** menu
of your user pool . Recipient message and data rates apply. Amazon SES bills you for email
messages separately, and Amazon SNS bills you for SMS messages separately. 6. Choose a **Username** for the new user. 7. Choose if you want to **Create a password** or have Amazon Cognito
**Generate a password** for the user. The option to generate a
password isn't available if [passwordless sign-in](amazon-cognito-user-pools-authentication-flow-methods.md#amazon-cognito-user-pools-authentication-flow-methods-passwordless "amazon-cognito-user-pools-authentication-flow-methods.md#amazon-cognito-user-pools-authentication-flow-methods-passwordless") is available in the user pool. Any temporary password
must adhere to the user pool password policy. 8. Choose **Create**. 9. Choose the **Users** menu and choose the **User
name** entry for the user. Add and edit **User attributes**
and **Group memberships**. Review **User event
history**.
