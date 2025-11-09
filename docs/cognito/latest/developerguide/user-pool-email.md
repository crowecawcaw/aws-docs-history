# Email settings for Amazon Cognito user pools

Certain events in your application can cause Amazon Cognito to email your users. For example,
if you configure your user pool to require email verification, Amazon Cognito sends an email when a
user signs up for a new account in your app or resets their password. Depending on the
action that initiates the email, the email contains a verification code or a temporary
password.

To handle email delivery, you can use either of the following options:

- [The default email configuration](#user-pool-email-default "#user-pool-email-default")
  that is built into the Amazon Cognito service.
- [Your Amazon Simple Email Service (Amazon SES)
  configuration](#user-pool-email-developer "#user-pool-email-developer").
  You can change your delivery option after you create your user pool.

Amazon Cognito sends email messages to your users with either a code that they can enter or a URL
link that they can select. The following table shows the events that can generate an email
message.

**Message options**

| Activity                                   | API operation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Delivery options               | Format options | Customizable | [Message<br>template](cognito-user-pool-settings-message-customizations.md "cognito-user-pool-settings-message-customizations.md") |
| ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ | -------------- | ------------ | ---------------------------------------------------------------------------------------------------------------------------------- |
| Forgot password                            | [ForgotPassword](../../../cognito-user-identity-pools/latest/APIReference/API_ForgotPassword.md "../../../cognito-user-identity-pools/latest/APIReference/API_ForgotPassword.md"), [AdminResetUserPassword](../../../cognito-user-identity-pools/latest/APIReference/API_AdminResetUserPassword.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminResetUserPassword.md")                                                                                                                                                                                                                                                                     | Email, SMS                     | code           | Yes          | **Verification message**                                                                                                           |
| Invitation                                 | [AdminCreateUser](../../../cognito-user-identity-pools/latest/APIReference/API_AdminCreateUser.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminCreateUser.md")                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Email, SMS                     | code           | Yes          | **Invitation message**                                                                                                             |
| Self-registration                          | [SignUp](../../../cognito-user-identity-pools/latest/APIReference/API_SignUp.md "../../../cognito-user-identity-pools/latest/APIReference/API_SignUp.md"), [ResendConfirmationCode](../../../cognito-user-identity-pools/latest/APIReference/API_ResendConfirmationCode.md "../../../cognito-user-identity-pools/latest/APIReference/API_ResendConfirmationCode.md")                                                                                                                                                                                                                                                                                             | Email, SMS                     | code, link     | Yes          | **Verification message**                                                                                                           |
| Email address or phone number verification | [UpdateUserAttributes](../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserAttributes.md "../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserAttributes.md"), [AdminUpdateUserAttributes](../../../cognito-user-identity-pools/latest/APIReference/API_AdminUpdateUserAttributes.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminUpdateUserAttributes.md"), [GetUserAttributeVerificationCode](../../../cognito-user-identity-pools/latest/APIReference/API_GetUserAttributeVerificationCode.md "../../../cognito-user-identity-pools/latest/APIReference/API_GetUserAttributeVerificationCode.md") | Email, SMS                     | code           | Yes          | **Verification message**                                                                                                           |
| Multi-factor authentication (MFA)          | [AdminInitiateAuth](../../../cognito-user-identity-pools/latest/APIReference/API_AdminInitiateAuth.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminInitiateAuth.md"), [InitiateAuth](../../../cognito-user-identity-pools/latest/APIReference/API_InitiateAuth.md "../../../cognito-user-identity-pools/latest/APIReference/API_InitiateAuth.md")                                                                                                                                                                                                                                                                                          | Email¹, SMS, authenticator app | code           | Yes²         | **MFA message**                                                                                                                    |
| One-time password authentication (OTP)     | [AdminInitiateAuth](../../../cognito-user-identity-pools/latest/APIReference/API_AdminInitiateAuth.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminInitiateAuth.md"), [InitiateAuth](../../../cognito-user-identity-pools/latest/APIReference/API_InitiateAuth.md "../../../cognito-user-identity-pools/latest/APIReference/API_InitiateAuth.md")                                                                                                                                                                                                                                                                                          | Email¹, SMS                    | code           | Yes          | **MFA message**³                                                                                                                   |

¹ Requires Essentials [feature
plan](cognito-sign-in-feature-plans.md "cognito-sign-in-feature-plans.md") or higher and [Amazon SES email
configuration](#user-pool-email-developer "#user-pool-email-developer").

² For SMS and email messages.

³ You can only customize the MFA message template when MFA is required or optional in
your user pool. When MFA is inactive, Amazon Cognito sends one-time passwords with the default
template.

Amazon SES charges for email messages. For more information, see [Amazon SES pricing](https://aws.amazon.com/ses/pricing/ "https://aws.amazon.com/ses/pricing/").

To learn more about email MFA, see [SMS and email message
MFA](user-pool-settings-mfa-sms-email-message.md "user-pool-settings-mfa-sms-email-message.md").

Amazon Cognito might prevent delivery of additional email or SMS messages to a single destination
in a short time period. If you believe your user pool is affected, configure and review
[logs for message delivery
errors](exporting-quotas-and-usage.md#exporting-quotas-and-usage-messages "exporting-quotas-and-usage.md#exporting-quotas-and-usage-messages") and then contact your account team.

## Default email configuration

Amazon Cognito can use its default email configuration to handle email deliveries for you. When you
use the default option, Amazon Cognito limits the number of emails it sends each day for your user
pool. For information on service limits, see [Quotas in Amazon Cognito](quotas.md "quotas.md"). For typical production environments, the default email limit is below the required
delivery volume. To enable a higher delivery volume, you can use your Amazon SES email
configuration.

When you use the default configuration, you use Amazon SES resources that are managed by AWS
to send email messages. Amazon SES adds email addresses that return a [hard bounce](../../../ses/latest/dg/send-email-concepts-deliverability.md#send-email-concepts-deliverability-bounce "../../../ses/latest/dg/send-email-concepts-deliverability.md#send-email-concepts-deliverability-bounce") to an [account-level suppression list](../../../ses/latest/dg/sending-email-suppression-list.md "../../../ses/latest/dg/sending-email-suppression-list.md") or a [global suppression list](../../../ses/latest/dg/send-email-concepts-deliverability.md#send-email-concepts-deliverability-suppression-list "../../../ses/latest/dg/send-email-concepts-deliverability.md#send-email-concepts-deliverability-suppression-list"). If an undeliverable email address
becomes deliverable later, you can't control its removal from the suppression list while
your user pool is configured to use the default configuration. An email address can remain
on the AWS-managed suppression list indefinitely. To manage undeliverable email addresses,
use your Amazon SES email configuration with an account-level suppression list, as described in
the next section.

When you use the default email configuration, you can use either of the following email
addresses as the FROM address:

- The default email address, *no-reply@verificationemail.com*.
- A custom email address. Before you can use your own email address, you must verify
  it with Amazon SES and grant Amazon Cognito permission to use this address.

## Amazon SES email configuration

Your application might require a higher delivery volume than what is available with
the default option. To increase the possible delivery volume, use your Amazon SES resources
with your user pool to email your users. You can also [monitor your email
sending activity](../../../ses/latest/DeveloperGuide/monitor-sending-activity.md "../../../ses/latest/DeveloperGuide/monitor-sending-activity.md") when you send email messages with your own Amazon SES
configuration.

Before you can use your Amazon SES configuration, you must verify one or more email
addresses, or a domain, with Amazon SES. Use a verified email address, or an address from a
verified domain, as the FROM email address that you assign to your user pool. When Amazon Cognito
sends email to a user, it calls Amazon SES for you and uses your email address.

When you use your Amazon SES configuration, the following conditions apply:

- The email delivery limits for your user pool are the same limits that apply to
  your Amazon SES verified email address in your AWS account.
- You can manage your messages to undeliverable email addresses with an
  account-level suppression list in Amazon SES that overrides the [global suppression list](../../../ses/latest/dg/send-email-concepts-deliverability.md#send-email-concepts-deliverability-suppression-list "../../../ses/latest/dg/send-email-concepts-deliverability.md#send-email-concepts-deliverability-suppression-list"). When you use an
  account-level suppression list, email message bounces affect the reputation of
  your account as a sender. For more information, see [Using the Amazon SES account-level suppression list](../../../ses/latest/dg/sending-email-suppression-list.md "../../../ses/latest/dg/sending-email-suppression-list.md") in the Amazon Simple Email Service
  Developer Guide.

### Amazon SES email configuration

Regions

The AWS Region where you create a user pool will have one of three requirements
for the configuration of email messages with Amazon SES. You might send email messages
from Amazon SES in the same Region as your user pool, several Regions including the same
Region, or one or more remote Regions. For best performance, send email messages
with a Amazon SES verified identity in the same Region as your user pool when you have
the option.

###### Categories of Region requirements for Amazon SES verified identities

**In-Region only**

Your user pools can send email messages with verified identities in
the same AWS Region as the user pool. In the default email
configuration without a custom `FROM` email address, Amazon Cognito
uses a `no-reply@verificationemail.com` verified identity in
the same Region.

**Backwards compatible**

Your user pools can send email messages with verified identities in
the same AWS Region or in one of the following alternate
Regions:

- US East (N. Virginia)
- US West (Oregon)
- Europe (Ireland)

This feature supports continuity for user pool resources that you
might have created to match Amazon Cognito requirements when the service
launched. User pools from that period could only send email messages
with verified identities in a limited number of AWS Regions. In the
default email configuration without a custom `FROM` email
address, Amazon Cognito uses a `no-reply@verificationemail.com`
verified identity in the same Region.

**Alternate Region**

Your user pools can send email messages with verified identities in an
alternate AWS Region that is outside of the user pool Region. This
configuration occurs when Amazon SES isn't available in a Region where Amazon Cognito
is available.

The Amazon SES sending authorization policy for your verified identity in
the alternate Region must trust the Amazon Cognito service principal of the
originating Region. For more information, see [To grant permissions
to use the default email configuration](#user-pool-email-permissions-default "#user-pool-email-permissions-default").

In some of these Regions, Amazon Cognito splits email messages between two
alternate Regions for the default email configuration of
`COGNITO_DEFAULT`. In these cases, to use a custom
`FROM` email address, the Amazon SES sending authorization
policy for your verified identity in each alternate Region must trust
the Amazon Cognito service principal of the originating Region. For more
information, see [To grant permissions
to use the default email configuration](#user-pool-email-permissions-default "#user-pool-email-permissions-default"). With the Amazon SES
email configuration of `DEVELOPER` in these Regions, you must
use a verified identity in the _first_
listed Region and configure it to trust the Amazon Cognito service principal in
the user pool Region. For example, in a user pool in
Middle East (UAE), configure a verified identity in
Europe (Frankfurt) to trust
`cognito-idp.me-central-1.amazonaws.com`. In the default
email configuration without a custom `FROM` email address,
Amazon Cognito uses a `no-reply@verificationemail.com` verified
identity in each Region.

###### Note

Under the following combination of conditions, you must specify the
`SourceArn` parameter of [EmailConfiguration](../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md#CognitoUserPools-CreateUserPool-request-EmailConfiguration "../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md#CognitoUserPools-CreateUserPool-request-EmailConfiguration") with a wildcard in the Region element, in the
format
`arn:`${Partition}`:ses:*:`${Account}`:identity/`${IdentityName}``.
This permits your user pool to send email messages with identical verified
identities in your AWS account in both AWS Regions.

- Your EmailSendingAccount is `COGNITO_DEFAULT`.
- You want to use a custom `FROM` address.
- Your user pool sends emails in an **Alternate
  Region**.
- Your user pool has a _second_[1](#cognito-email-alternate-regions-note "#cognito-email-alternate-regions-note")
  **Alternate Region** specified in the table of
  **Amazon SES supported Regions** that follows.

If you create a user pool programmatically–with an AWS SDK, the Amazon Cognito API
or CLI, the AWS CDK, or AWS CloudFormation–your user pool sends
email messages with the Amazon SES identity that the `SourceArn` parameter of
[EmailConfiguration](../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md#CognitoUserPools-CreateUserPool-request-EmailConfiguration "../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md#CognitoUserPools-CreateUserPool-request-EmailConfiguration") specifies for your user pool. The Amazon SES identity
must occupy a supported AWS Region. If your `EmailSendingAccount` is
`COGNITO_DEFAULT` and you don't specify a `SourceArn`
parameter, Amazon Cognito sends email messages from
`no-reply@verificationemail.com` using resources in the Region where
you created your user pool.

The following table shows the AWS Regions where you can use Amazon SES identities
with Amazon Cognito.

| User pool Region          | Region option        | Amazon SES supported Regions                                                                                                         |
| ------------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| US East (N. Virginia)     | Backwards compatible | US East (N. Virginia), US West (Oregon),<br>Europe (Ireland)                                                                         |
| US East (Ohio)            | Backwards compatible | US East (Ohio), US East (N. Virginia), US West (Oregon),<br>Europe (Ireland)                                                         |
| US West (N. California)   | In-Region only       | US West (N. California)                                                                                                              |
| US West (Oregon)          | Backwards compatible | US East (N. Virginia), US West (Oregon),<br>Europe (Ireland)                                                                         |
| Canada (Central)          | Backwards compatible | Canada (Central), US East (N. Virginia), US West (Oregon),<br>Europe (Ireland)                                                       |
| Canada West (Calgary)     | Alternate Region     | Canada (Central), US West (N. California)[1](#cognito-email-alternate-regions-note "#cognito-email-alternate-regions-note")          |
| Mexico (Central)          | Alternate Region     | US East (N. Virginia), US West (Oregon)[1](#cognito-email-alternate-regions-note "#cognito-email-alternate-regions-note")            |
| Asia Pacific (Tokyo)      | Backwards compatible | Asia Pacific (Tokyo), US East (N. Virginia),<br>US West (Oregon), Europe (Ireland)                                                   |
| Asia Pacific (Hong Kong)  | Alternate Region     | Asia Pacific (Singapore),<br>Asia Pacific (Tokyo)[1](#cognito-email-alternate-regions-note "#cognito-email-alternate-regions-note")  |
| Asia Pacific (Seoul)      | Backwards compatible | Asia Pacific (Seoul), US East (N. Virginia),<br>US West (Oregon), Europe (Ireland)                                                   |
| Asia Pacific (Malaysia)   | Alternate Region     | Asia Pacific (Sydney),<br>Asia Pacific (Singapore)[1](#cognito-email-alternate-regions-note "#cognito-email-alternate-regions-note") |
| Asia Pacific (Thailand)   | Alternate Region     | Asia Pacific (Singapore), Asia Pacific (Mumbai)[1](#cognito-email-alternate-regions-note "#cognito-email-alternate-regions-note")    |
| Asia Pacific (Mumbai)     | Backwards compatible | Asia Pacific (Mumbai), US East (N. Virginia), US West (Oregon),<br>Europe (Ireland)                                                  |
| Asia Pacific (Hyderabad)  | Alternate Region     | Asia Pacific (Mumbai), Asia Pacific (Singapore)[1](#cognito-email-alternate-regions-note "#cognito-email-alternate-regions-note")    |
| Asia Pacific (Singapore)  | Backwards compatible | Asia Pacific (Singapore), US East (N. Virginia),<br>US West (Oregon), Europe (Ireland)                                               |
| Asia Pacific (Sydney)     | Backwards compatible | Asia Pacific (Sydney), US East (N. Virginia),<br>US West (Oregon), Europe (Ireland)                                                  |
| Asia Pacific (Osaka)      | In-Region only       | Asia Pacific (Osaka)                                                                                                                 |
| Asia Pacific (Jakarta)    | In-Region only       | Asia Pacific (Jakarta)                                                                                                               |
| Asia Pacific (Melbourne)  | Alternate Region     | Asia Pacific (Sydney),<br>Asia Pacific (Singapore)[1](#cognito-email-alternate-regions-note "#cognito-email-alternate-regions-note") |
| Europe (Ireland)          | Backwards compatible | US East (N. Virginia), US West (Oregon),<br>Europe (Ireland)                                                                         |
| Europe (London)           | Backwards compatible | Europe (London), US East (N. Virginia), US West (Oregon),<br>Europe (Ireland)                                                        |
| Europe (Paris)            | In-Region only       | Europe (Paris)                                                                                                                       |
| Europe (Frankfurt)        | Backwards compatible | Europe (Frankfurt), US East (N. Virginia), US West (Oregon),<br>Europe (Ireland)                                                     |
| Europe (Zurich)           | Alternate Region     | Europe (Frankfurt), Europe (London)[1](#cognito-email-alternate-regions-note "#cognito-email-alternate-regions-note")                |
| Europe (Stockholm)        | In-Region only       | Europe (Stockholm)                                                                                                                   |
| Europe (Milan)            | In-Region only       | Europe (Milan)                                                                                                                       |
| Europe (Spain)            | Alternate Region     | Europe (Paris), Europe (Stockholm)[1](#cognito-email-alternate-regions-note "#cognito-email-alternate-regions-note")                 |
| Middle East (Bahrain)     | In-Region only       | Middle East (Bahrain)                                                                                                                |
| Middle East (UAE)         | Alternate Region     | Europe (Frankfurt), Europe (London)[1](#cognito-email-alternate-regions-note "#cognito-email-alternate-regions-note")                |
| South America (São Paulo) | In-Region only       | South America (São Paulo)                                                                                                            |
| Israel (Tel Aviv)         | In-Region only       | Israel (Tel Aviv)                                                                                                                    |
| Africa (Cape Town)        | In-Region only       | Africa (Cape Town)                                                                                                                   |

1 Used in user pools with the default email
configuration. Amazon Cognito distributes email messages among verified identities with the
same email address in each Region. To use a custom `FROM` address,
configure `EmailConfiguration` with a `SourceArn` parameter in
the format
`arn:`${Partition}`:ses:*:`${Account}`:identity/`${IdentityName}``.

## Configuring email for your user pool

Complete the following steps to configure the email settings for your user pool.
Depending on the settings that you use, you might need IAM permissions in Amazon SES,
AWS Identity and Access Management (IAM), and Amazon Cognito.

###### Note

You can't share the resources that you create in these steps across
AWS accounts. For example, you can't configure a user pool in one account, and
then use it with an Amazon SES email address in a different account. If you use Amazon Cognito in
multiple accounts, repeat these steps for each account.

### Step 1: Verify your email

address or domain with Amazon SES

Before you configure your user pool, you must verify one or more domains or email
addresses with Amazon SES if you want to do either of the following:

- Use your own email address as the FROM address
- Use your Amazon SES configuration to handle email delivery

By verifying your email address or domain, you confirm that you own it, which
helps prevent unauthorized use.

For information on verifying an email address with Amazon SES, see [Verifying an Email
Address](../../../ses/latest/DeveloperGuide/verify-email-addresses-procedure.md "../../../ses/latest/DeveloperGuide/verify-email-addresses-procedure.md") in the _Amazon Simple Email Service Developer Guide_. For
information on verifying a domain with Amazon SES, see [Verifying
domains](../../../ses/latest/DeveloperGuide/verify-domains.md "../../../ses/latest/DeveloperGuide/verify-domains.md").

### Step 2: Move your account out of

the Amazon SES sandbox

Omit this step if you are using the default Amazon Cognito email configuration.

When you first use Amazon SES in any AWS Region, it places your AWS account in the
Amazon SES sandbox for that Region. Amazon SES uses the sandbox to prevent fraud and abuse. If
you use your Amazon SES configuration to handle email delivery, you must move your
AWS account out of the sandbox before Amazon Cognito can email your users.

In the sandbox, Amazon SES imposes restrictions on how many emails you can send and
where you can send them. You can send emails only to addresses and domains that you
have verified with Amazon SES, or you can send them to Amazon SES mailbox simulator addresses.
While your AWS account remains in the sandbox, don't use your Amazon SES configuration
for applications that are in production. In this situation, Amazon Cognito can't send
messages to your users' email addresses.

To remove your AWS account from the sandbox, see [Moving out of the Amazon SES
sandbox](../../../ses/latest/DeveloperGuide/request-production-access.md "../../../ses/latest/DeveloperGuide/request-production-access.md") in the _Amazon Simple Email Service Developer Guide._

### Step 3: Grant email permissions to

Amazon Cognito

You might need to grant specific permissions to Amazon Cognito before it can email your
users. The permissions that you grant, and the process that you use to grant them,
depend on whether you are using the default email configuration, or your Amazon SES
configuration.

Complete this step only if you configure your user pool to **Send
email with Cognito** or set `EmailSendingAccount` to
`COGNITO_DEFAULT`.

With the default email configuration, your user pool can send email
messages with either of the following addresses.

- The default address
  `no-reply@verificationemail.com`.
- A custom FROM address from your verified email addresses or
  domains in Amazon SES.
  If you use a custom address, Amazon Cognito needs additional permissions to email
  users from that address. These permissions are granted by a [sending authorization policy](../../../ses/latest/dg/sending-authorization.md "../../../ses/latest/dg/sending-authorization.md") for the address or domain in
  Amazon SES. If you use the Amazon Cognito console to add a custom address to your user
  pool, the policy is automatically attached to the Amazon SES verified email
  address. However, if you configure your user pool outside of the console,
  such as using the AWS CLI or the Amazon Cognito API, you must attach the policy using
  the [Amazon SES console](https://console.aws.amazon.com/ses/ "https://console.aws.amazon.com/ses/") or the
  [PutIdentityPolicy](../../../ses/latest/APIReference/API_PutIdentityPolicy.md "../../../ses/latest/APIReference/API_PutIdentityPolicy.md") API.

###### Note

You can only configure a FROM address in a verified domain using the
AWS CLI or the Amazon Cognito API.

A sending authorization policy allows or denies access based on the
account resources that are using Amazon Cognito to invoke Amazon SES. For more information
about resource-based policies, see the [IAM
User Guide](../../../IAM/latest/UserGuide/access_policies.md#policies_resource-based "../../../IAM/latest/UserGuide/access_policies.md#policies_resource-based"). You can also find example resource-based policies in
the [Amazon SES Developer Guide](../../../ses/latest/DeveloperGuide/sending-authorization-policy-examples.md "../../../ses/latest/DeveloperGuide/sending-authorization-policy-examples.md").

###### Example Sending authorization policy

The following example sending authorization policy grants Amazon Cognito a
limited ability to use an Amazon SES verified identity. Amazon Cognito can only send
email messages when it does so on behalf of both the user pool in the
`aws:SourceArn` condition and the
account in the `aws:SourceAccount`
condition.

Regions with Amazon SES
Your sending authorization policy in the user pool Region
or alternate Region must permit the Amazon Cognito service principal
to send email messages. Refer to the [Regions table](#ses-regions-table "#ses-regions-table") for
more information. If your **User pool
Region** matches at least one value in
**Amazon SES Region**, configure your
sending authorization policy with the global service
principal in the following example.

JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "stmnt1234567891234",
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "email.cognito-idp.amazonaws.com"
 ]
 },
 "Action": [
 "SES:SendEmail",
 "SES:SendRawEmail"
 ],
 "Resource": "`arn:`aws`:ses:`us-east-1`:`111122223333`:identity/`support@example.com``",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`111122223333`"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:`aws`:cognito-idp:`us-east-1`:`111122223333`:userpool/`us-east-1_EXAMPLE`"
 }
 }
 }
 ]
}`

```

Opt-in Regions without Amazon SES
Amazon SES isn't available in all opt-in AWS Regions where
Amazon Cognito is available. Middle East (UAE) is an example, and
can only send emails with verified identities in
Europe (Frankfurt) (`eu-central-1`). In user
pools with the default email configuration, Amazon Cognito also sends
email messages with a verified identity in each of two
Regions. In the case of Middle East (UAE), the
additional Region is Europe (London). You must update the
sending authorization policy in both Regions.

Your sending authorization policy in each of the alternate
Regions must permit the Amazon Cognito service principal in the user
pool opt-in Region to send email messages. Refer to the
[Regions table](#ses-regions-table "#ses-regions-table")
for more information. If your Region is marked as
**Alternate Region**, configure your
sending authorization policies with the Regional service
principal as in the following example. Replace the example
Region identifier `me-central-1`
with the required Region ID as needed.

JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "cognito-idp.`me-central-1`.amazonaws.com"
 ]
 },
 "Action": [
 "SES:SendEmail",
 "SES:SendRawEmail"
 ],
 "Resource": "`arn:`aws`:ses:`us-east-1`:`111122223333`:identity/`support@example.com``",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`111122223333`"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:`aws`:cognito-idp:`us-east-1`:`111122223333`:userpool/`us-east-1_EXAMPLE`"
 }
 }
 }
 ]
}`

```

For more information about policy syntax, see [Amazon SES
sending authorization policies](../../../ses/latest/DeveloperGuide/sending-authorization-policies.md "../../../ses/latest/DeveloperGuide/sending-authorization-policies.md") in the
_Amazon Simple Email Service Developer Guide_.

For more examples, see [Amazon
SES sending authorization policy examples](../../../ses/latest/DeveloperGuide/sending-authorization-policy-examples.md "../../../ses/latest/DeveloperGuide/sending-authorization-policy-examples.md") in the
_Amazon Simple Email Service Developer Guide_.

If you configure your user pool to use your Amazon SES configuration, Amazon Cognito
needs additional permissions to call Amazon SES on your behalf when it emails
your users. This authorization is granted with the IAM service.

When you configure your user pool with this option, Amazon Cognito creates a
_service-linked role_, which is a type
of IAM role, in your AWS account. This role contains the permissions
that allow Amazon Cognito to access Amazon SES and send email with your address.

Amazon Cognito creates your service-linked role with the AWS credentials of the
user session that sets the configuration. The IAM permissions of this
session must include the `iam:CreateServiceLinkedRole` action.
For more information about permissions in IAM, see [Access management for AWS resources](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") in the _IAM User Guide_.

For more information about the service-linked role that Amazon Cognito creates, see
[Using service-linked roles for
Amazon Cognito](using-service-linked-roles.md "using-service-linked-roles.md").

### Step 4: Configure your user

pool

Complete the following steps if you want to configure your user pool with any of the
following:

- A custom FROM address that appears as the email sender
- A custom REPLY-TO address that receives the messages that your users send to
  your FROM address
- Your Amazon SES configuration

###### Note

If your verified identity is an email address, Amazon Cognito sets that email address as
the FROM and REPLY-TO email address by default. But, if your verified identity is a
domain, you must provide a value for the FROM email address.

Omit this procedure if you want to use the default Amazon Cognito email configuration and
address.

###### To configure your user pool to use a custom email address

1. Go to the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home").
   If prompted, enter your AWS credentials.
2. Choose **User Pools**.
3. Choose an existing user pool from the list.
4. Choose the **Authentication methods** menu, locate
   **Email configuration**, choose
   **Edit**.
5. On the **Edit email configuration** page, select
   **Send email from Amazon SES** or **Send email with
   Amazon Cognito**. You can customize the **SES Region**,
   **Configuration Set**, and **FROM sender
   name** only when you choose **Send email from
   Amazon SES**.
6. To use a custom FROM address, complete the following steps:
   1. Under **SES Region**, choose the Region that contains
      your verified email address.
   2. Under **FROM email address**, choose your email
      address. Use an email address that you have verified with Amazon SES.
   3. (Optional) Under **Configuration set**, choose a
      configuration set for Amazon SES to use. Making and saving this change
      creates a service-linked role.
   4. (Optional) Under **FROM sender address**, enter an
      email address. You can provide only an email address, or an email
      address and a friendly name in the format `Jane Doe
<janedoe@example.com>`.
   5. (Optional) Under **REPLY-TO email address**, enter
      the email address where you want to receive messages that your users
      send to your FROM address.

7. Choose **Save changes**.

**Related Topics**

- [Customizing email verification messages](cognito-user-pool-settings-message-customizations.md#cognito-user-pool-settings-email-verification-message-customization "cognito-user-pool-settings-message-customizations.md#cognito-user-pool-settings-email-verification-message-customization")
- [Customizing
  user invitation messages](cognito-user-pool-settings-message-customizations.md#cognito-user-pool-settings-user-invitation-message-customization "cognito-user-pool-settings-message-customizations.md#cognito-user-pool-settings-user-invitation-message-customization")
