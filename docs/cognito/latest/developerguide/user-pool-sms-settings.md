# SMS message settings for Amazon Cognito user pools

Some Amazon Cognito events for your user pool might cause Amazon Cognito to send SMS text messages to
your users. For example, if you configure your user pool to require phone verification,
Amazon Cognito sends an SMS text message when a user signs up for a new account in your app or resets
their password. Depending on the action that initiates the SMS text message, the message
contains a verification code, a temporary password, or a welcome message.

Amazon Cognito can send SMS messages with one of the following configurations:

- **Amazon Simple Notification Service (Amazon SNS)** – Amazon Cognito calls
  Amazon SNS, which routes SMS messages to AWS End User Messaging SMS.
- **AWS End User Messaging SMS direct** –
  Amazon Cognito calls AWS End User Messaging SMS directly, without Amazon SNS as an intermediary. You can use this
  option in most AWS Regions where Amazon Cognito is available. For exceptions, see
  [AWS End User Messaging SMS direct path Region configuration](#sms-choose-a-region-eums "#sms-choose-a-region-eums").
  A user pool uses one SMS configuration at a time. The Amazon SNS and AWS End User Messaging SMS direct
  configurations are mutually exclusive. When you set one configuration, Amazon Cognito clears the
  other. This applies to [CreateUserPool](../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md "../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md"), [UpdateUserPool](../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserPool.md "../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserPool.md"), and [SetUserPoolMfaConfig](../../../cognito-user-identity-pools/latest/APIReference/API_SetUserPoolMfaConfig.md "../../../cognito-user-identity-pools/latest/APIReference/API_SetUserPoolMfaConfig.md") operations.

Amazon SNS SMS is available in the AWS Regions listed in [Amazon SNS path Region configuration](#sms-choose-a-region-sns "#sms-choose-a-region-sns"). To send
SMS messages from a user pool in any other AWS Region, use AWS End User Messaging SMS directly.

If you send a text message through Amazon Cognito for the first time, AWS End User Messaging SMS places you
in a [sandbox environment](../../../sms-voice/latest/userguide/sandbox.md "../../../sms-voice/latest/userguide/sandbox.md"). In the
sandbox environment, you can test your applications for SMS text messages. In the sandbox,
you can send messages to a limited number of verified destination phone numbers if you have
an origination identity, or simulate sending messages if you don't.

###### Note

In November 2024, AWS replaced Amazon SNS SMS messaging with AWS End User Messaging SMS. When you use the
Amazon SNS configuration path, user pools initiate SMS messages with the Amazon SNS
[Publish](../../../sns/latest/api/API_Publish.md "../../../sns/latest/api/API_Publish.md")
operation, which is a pass-through to AWS End User Messaging SMS. For this path, you must configure
permissions for `sns:Publish`. When you use the direct AWS End User Messaging SMS
configuration path, Amazon Cognito calls the AWS End User Messaging SMS `SendTextMessage` operation and
you must configure permissions for `sms-voice:SendTextMessage`.

AWS End User Messaging SMS charges for SMS text messages. For more information, see [AWS End User Messaging SMS pricing](https://aws.amazon.com/end-user-messaging/pricing/ "https://aws.amazon.com/end-user-messaging/pricing/").

Amazon Cognito sends SMS messages to your users with a code that they can enter. The following
table shows the events that can generate an SMS message.

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
configuration](user-pool-email.md#user-pool-email-developer "user-pool-email.md#user-pool-email-developer").

² For SMS and email messages.

³ You can only customize the MFA message template when MFA is required or optional in
your user pool. When MFA is inactive, Amazon Cognito sends one-time passwords with the default
template.

AWS End User Messaging SMS charges for SMS messages. For more information, see [AWS End User Messaging SMS pricing](https://aws.amazon.com/end-user-messaging/pricing/ "https://aws.amazon.com/end-user-messaging/pricing/").

To learn more about MFA, see [SMS and email message MFA](user-pool-settings-mfa-sms-email-message.md "user-pool-settings-mfa-sms-email-message.md").

Amazon Cognito might prevent delivery of additional email or SMS messages to a single destination
in a short time period. If you believe your user pool is affected, configure and review
[logs for message delivery
errors](exporting-quotas-and-usage.md#exporting-quotas-and-usage-messages "exporting-quotas-and-usage.md#exporting-quotas-and-usage-messages") and then contact your account team.

## Choosing between Amazon SNS and AWS End User Messaging SMS

Amazon Cognito user pools can send SMS messages through two paths: Amazon SNS or AWS End User Messaging SMS
directly. For new user pools, use the AWS End User Messaging SMS direct path. Amazon SNS SMS is available
only in a fixed set of AWS Regions. The direct AWS End User Messaging SMS path supports additional
Regions and exposes features that the Amazon SNS path does not. Both paths deliver messages
through AWS End User Messaging SMS.

The following table compares the two SMS configuration paths.

| Capability                 | Amazon SNS path                                                                                              | AWS End User Messaging SMS direct path                                                                                                                                                                                                                   |
| -------------------------- | ------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Region availability        | Available in the AWS Regions listed in the Amazon SNS path Region table                                      | Available in most AWS Regions where Amazon Cognito is available. Regions where only the Amazon SNS path is available are listed in [AWS End User Messaging SMS direct path Region configuration](#sms-choose-a-region-eums "#sms-choose-a-region-eums"). |
| Integration                | Amazon Cognito calls the Amazon SNS Publish operation, which passes<br>through to AWS End User Messaging SMS | Amazon Cognito calls the AWS End User Messaging SMS SendTextMessage operation<br>directly                                                                                                                                                                |
| IAM permission             | `sns:Publish`                                                                                                | `sms-voice:SendTextMessage`                                                                                                                                                                                                                              |
| Configuration sets         | Not configurable through Amazon Cognito                                                                      | Set the `ConfigurationSetName` field for event<br>logging and destinations                                                                                                                                                                               |
| Origination identity       | Not configurable through Amazon Cognito                                                                      | Set the `OriginationIdentity` field                                                                                                                                                                                                                      |
| Cross-Region sending       | Set the `SnsRegion` field                                                                                    | Not supported                                                                                                                                                                                                                                            |
| India DLT registration     | Not configurable through Amazon Cognito                                                                      | Set the `InEntityId` and<br>`InTemplateId` fields                                                                                                                                                                                                        |
| Fraud protection (Protect) | Account-default protect configuration applies                                                                | Account-default applies. You can also apply a protect<br>configuration to a specific use case through a configuration<br>set.                                                                                                                            |

###### Note

A default AWS End User Messaging SMS Protect configuration applies to all messages, including
those from Amazon Cognito. To apply a protect configuration to a specific use case,
link it to a configuration set and use the direct AWS End User Messaging SMS path. For more
information, see [Fraud Protection in
AWS End User Messaging SMS](../../../sms-voice/latest/userguide/protect.md "../../../sms-voice/latest/userguide/protect.md").

## SMS configuration in the Amazon Cognito user pools API

The [SmsConfigurationType](../../../cognito-user-identity-pools/latest/APIReference/API_SmsConfigurationType.md "../../../cognito-user-identity-pools/latest/APIReference/API_SmsConfigurationType.md") object in the Amazon Cognito user pools API contains the SMS
configuration for your user pool. This object has the following configuration
paths:

Amazon SNS path

Set `SnsCallerArn` to the ARN of an IAM role that grants
Amazon Cognito permission to call `sns:Publish`. Optionally set
`SnsRegion` and `ExternalId`. The
`SnsCallerArn` parameter is optional when you use the
AWS End User Messaging SMS direct path.

AWS End User Messaging SMS direct path

Set the `EumsSms` object of type
`EumsSmsConfigurationType`. This object has the following
members:

- `CallerArn` (Required) – The ARN of an
  IAM role that grants Amazon Cognito permission to call
  `sms-voice:SendTextMessage`.
- `ExternalId` (Optional) – The external ID
  for the IAM role trust policy. This value provides confused-deputy
  prevention.
- `OriginationIdentity` (Optional) – The phone
  number, pool, or sender ID to use for sending.
- `ConfigurationSetName` (Optional) – The
  AWS End User Messaging SMS configuration set to use.
- `InEntityId` (Optional) – The entity
  registration ID from India DLT registration. Required for sending
  to recipients in India.
- `InTemplateId` (Optional) – The template
  registration ID from India DLT registration. Required for sending
  to recipients in India.
- `Region` (Optional) – The AWS Region of
  your AWS End User Messaging SMS resources. For more information, see [Choose the AWS Region for SMS messages](#sms-choose-a-region "#sms-choose-a-region").

For more information, see [SmsConfigurationType](../../../cognito-user-identity-pools/latest/APIReference/API_SmsConfigurationType.md "../../../cognito-user-identity-pools/latest/APIReference/API_SmsConfigurationType.md") in the _Amazon Cognito User Pools
API Reference_.

## Best practices

Because of the volume of unsolicited SMS traffic worldwide, some governments impose
barriers between the senders and recipients of SMS messages. When you use SMS messages
for MFA and user updates, you must take additional steps to ensure that your messages
are delivered. You must also monitor SMS-message-related regulations in countries where
your users might live and keep your SMS message configuration current. For more
information, see [SMS and
MMS country capabilities and limitations](../../../sms-voice/latest/userguide/phone-numbers-sms-support-by-country.md "../../../sms-voice/latest/userguide/phone-numbers-sms-support-by-country.md") in the _AWS End User Messaging SMS User Guide_.

The use of SMS messages to authenticate and verify users isn't a security best
practice. Phone numbers can change owners, and might not reliably represent a _something you have_ factor of MFA for your users. Instead,
implement TOTP MFA in your app or with your third-party IdP. You can also create
additional custom authentication factors with [Custom authentication challenge Lambda triggers](user-pool-lambda-challenge.md "user-pool-lambda-challenge.md").

Review the following links for information about securing your SMS message delivery
architecture.

- [Reduce risks of user sign-up fraud and SMS pumping with
  Amazon Cognito user pools](https://aws.amazon.com/blogs/security/reduce-risks-of-user-sign-up-fraud-and-sms-pumping-with-amazon-cognito-user-pools/ "https://aws.amazon.com/blogs/security/reduce-risks-of-user-sign-up-fraud-and-sms-pumping-with-amazon-cognito-user-pools/")
- [Defending Against SMS Pumping: New AWS Features to Help Combat
  Artificially Inflated Traffic](https://aws.amazon.com/blogs/messaging-and-targeting/defending-against-sms-pumping-new-aws-features-to-help-combat-artificially-inflated-traffic/ "https://aws.amazon.com/blogs/messaging-and-targeting/defending-against-sms-pumping-new-aws-features-to-help-combat-artificially-inflated-traffic/")

## Setting up SMS messaging for the first time in Amazon Cognito user pools

Amazon Cognito uses either Amazon SNS (and indirectly AWS End User Messaging SMS) or AWS End User Messaging SMS directly to send SMS
messages from your user pools. You can also use a [Custom SMS sender Lambda trigger](user-pool-lambda-custom-sms-sender.md "user-pool-lambda-custom-sms-sender.md") to use your own resources to
send SMS messages. The first time that you set up SMS text messages in a particular
AWS Region, AWS End User Messaging SMS places your AWS account in the SMS sandbox for that Region.
AWS End User Messaging SMS uses the sandbox to prevent fraud and abuse and to meet compliance
requirements. When your AWS account is in the sandbox, AWS End User Messaging SMS imposes some [restrictions](../../../sms-voice/latest/userguide/sandbox.md#sandbox-sms "../../../sms-voice/latest/userguide/sandbox.md#sandbox-sms"). For example, you can send text messages to a maximum of 10
verified destination numbers if you have an origination identity, or you can simulate
sending messages without an origination identity. While your AWS account remains in
the sandbox, do not send SMS messages in production. When you're in the sandbox, Amazon Cognito
can't send messages to your users' phone numbers.

###### Topics

- [Prepare an IAM role that Amazon Cognito can use to send SMS messages with AWS End User Messaging SMS](#sms-create-a-role "#sms-create-a-role")
- [To set up AWS End User Messaging SMS direct SMS for a user pool](#sms-setup-eums "#sms-setup-eums")
- [Choose the AWS Region for SMS messages](#sms-choose-a-region "#sms-choose-a-region")
- [Obtain an origination identity to send SMS messages to US phone numbers](#user-pool-sms-settings-first-time-origination "#user-pool-sms-settings-first-time-origination")
- [Confirm that you are in the SMS sandbox](#user-pool-sms-settings-first-time-confirm-sandbox "#user-pool-sms-settings-first-time-confirm-sandbox")
- [Move your account out of the sandbox](#user-pool-sms-settings-first-time-out-sandbox "#user-pool-sms-settings-first-time-out-sandbox")
- [Use simulator numbers or verified phone numbers with AWS End User Messaging SMS](#user-pool-sms-settings-first-time-verify-numbers "#user-pool-sms-settings-first-time-verify-numbers")
- [Complete user pool setup in Amazon Cognito](#user-pool-sms-settings-first-time-finish-user-pool "#user-pool-sms-settings-first-time-finish-user-pool")

### Prepare an IAM role that Amazon Cognito can use to send SMS messages with AWS End User Messaging SMS

When you send an SMS message from your user pool, Amazon Cognito assumes an IAM role in
your account. The permissions that the role requires depend on the SMS configuration
path you choose:

- **Amazon SNS path** – The role must
  grant the `sns:Publish` permission. Amazon Cognito uses this permission
  to send SMS messages through Amazon SNS.
- **AWS End User Messaging SMS direct path** – The
  role must grant the `sms-voice:SendTextMessage` permission.
  Amazon Cognito uses this permission to call AWS End User Messaging SMS directly.

In the Amazon Cognito console, you can set an **IAM role selection**
from the **Authentication methods** menu of your user pool, under
**SMS** or make this selection during the user pool creation
wizard.

The following example IAM role trust policy grants Amazon Cognito user pools a limited ability to
assume the role. Amazon Cognito can only assume the role when it meets the following
conditions:

- The assume-role operation is on behalf of the user pool in the
  `aws:SourceArn` condition.
- The assume-role operation is on behalf of a user pool in the AWS account
  set by the `aws:SourceAccount` condition.
- The assume-role operation includes the external ID in the
  `sts:externalId` condition.

These trust policy conditions apply to both the Amazon SNS path and the AWS End User Messaging SMS
direct path.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "",
 "Effect": "Allow",
 "Principal": {
 "Service": "cognito-idp.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "sts:ExternalId": "`a1b2c3d4-5678-90ab-cdef-EXAMPLE22222`",
 "aws:SourceAccount": "`111122223333`"
 },
 "ArnLike": {
 "aws:SourceArn": "`arn:aws:cognito-idp:us-west-2:111122223333:userpool/us-west-2_EXAMPLE`"
 }
 }
 }
 ]
}`

```

You can specify an exact [user pool ARN](../../../service-authorization/latest/reference/list_amazoncognitouserpools.md#amazoncognitouserpools-resources-for-iam-policies "../../../service-authorization/latest/reference/list_amazoncognitouserpools.md#amazoncognitouserpools-resources-for-iam-policies") or a wildcard ARN in the value of the
`aws:SourceArn` condition. Look up the ARNs of
your user pools in the AWS Management Console or with a [DescribeUserPool](../../../cognito-user-identity-pools/latest/APIReference/API_DescribeUserPool.md "../../../cognito-user-identity-pools/latest/APIReference/API_DescribeUserPool.md") API request.

To send SMS messages for [multi-factor authentication](user-pool-settings-mfa-sms-email-message.md "user-pool-settings-mfa-sms-email-message.md"), your IAM role trust policy must have an
`sts:ExternalId` condition. The value of this condition must match
the `ExternalId` property of the [SmsConfiguration](../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md#CognitoUserPools-CreateUserPool-request-SmsConfiguration "../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md#CognitoUserPools-CreateUserPool-request-SmsConfiguration") of your user pool. When you create an IAM role
during the process of user pool creation in the Amazon Cognito console, Amazon Cognito configures the
external ID for you in the role and in the user pool settings. This isn't true when
you use an existing IAM role.

You must update the user pool `ExternalId` parameter in an [UpdateUserPool](../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserPool.md "../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserPool.md") API request and update the IAM role trust policy with an
`sts:externalId` condition with the same value. To learn how to use
the API to update a user pool in a way that preserves the original configuration,
see [Updating user pool and app client configuration](cognito-user-pool-updating.md "cognito-user-pool-updating.md").

For more information about IAM roles and trust policies, see [Roles terms and concepts](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md") in the _AWS Identity and Access Management User
Guide_.

### To set up AWS End User Messaging SMS direct SMS for a user pool

Use the following procedure to configure your user pool to send SMS messages
directly through AWS End User Messaging SMS. This configuration uses the `EumsSms`
object in [SmsConfigurationType](../../../cognito-user-identity-pools/latest/APIReference/API_SmsConfigurationType.md "../../../cognito-user-identity-pools/latest/APIReference/API_SmsConfigurationType.md").

###### To set up AWS End User Messaging SMS direct SMS messaging

1. Create or identify an AWS End User Messaging SMS origination identity in the AWS Region
   that you want to send from. An origination identity can be a phone number,
   sender ID, or pool. You can also create an AWS End User Messaging SMS configuration set to
   apply sending rules. For instructions on requesting a phone number, see
   [Request a
   phone number](../../../sms-voice/latest/userguide/phone-numbers-request.md "../../../sms-voice/latest/userguide/phone-numbers-request.md") in the _AWS End User Messaging SMS User
   Guide_.
2. Create an IAM role that Amazon Cognito can assume to call AWS End User Messaging SMS. The trust
   policy for this role is the same as the Amazon SNS path: it must include
   `aws:SourceArn`,
   `aws:SourceAccount`, and
   `sts:ExternalId` conditions. For trust policy details, see
   [Prepare an IAM role that Amazon Cognito can use to send SMS messages with AWS End User Messaging SMS](#sms-create-a-role "#sms-create-a-role").
3. Attach the following identity (permissions) policy to the role. This
   policy grants Amazon Cognito permission to call
   `sms-voice:SendTextMessage` on the origination identity that your
   user pool sends from. Scope the `Resource` element to the ARN of
   your phone number, phone pool, or sender ID as a least-privilege practice.
   Replace the example ARN with the ARN of your origination identity.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "sms-voice:SendTextMessage"
            ],
            "Resource": "arn:aws:sms-voice:us-east-1:123456789012:phone-number/phone-a1b2c3d4e5f6EXAMPLE"
        }
    ]
}
```

The origination identity ARN uses one of the following formats, depending
on the identity type:

    * Phone number –
     `arn:`partition`:sms-voice:`region`:`account`:phone-number/`phoneNumberId``
    * Phone pool –
     `arn:`partition`:sms-voice:`region`:`account`:pool/`poolId``
    * Sender ID –
     `arn:`partition`:sms-voice:`region`:`account`:sender-id/`senderId`/`isoCountryCode``

###### Important

When your policy scopes the `Resource` element to an
origination identity ARN, set the `OriginationIdentity` field
to that same ARN—for example,
`arn:aws:sms-voice:us-east-1:123456789012:phone-number/phone-a1b2c3d4e5f6EXAMPLE`.
A phone number in E.164 format (such as `+12065550100`)
doesn't match the scoped policy, so the request isn't authorized and
Amazon Cognito can't send SMS messages. 4. If you send SMS messages to recipients in India, register a DLT entity
ID and template ID with a Distributed Ledger Technology (DLT) portal.
Supply the entity ID as `InEntityId` and the template ID as
`InTemplateId` in the `EumsSms` configuration. For
more information about India DLT registration, see [Special requirements for sending SMS messages to recipients in
India](../../../sms-voice/latest/userguide/india-sms-best-practices.md "../../../sms-voice/latest/userguide/india-sms-best-practices.md") in the _AWS End User Messaging SMS User
Guide_. 5. Test your configuration by calling the AWS End User Messaging SMS [SendTextMessage](../../../pinpoint/latest/apireference_smsvoicev2/API_SendTextMessage.md "../../../pinpoint/latest/apireference_smsvoicev2/API_SendTextMessage.md") API operation directly with the origination
identity and IAM role that you configured. Confirm that your test
message is delivered before you assign the configuration to your user
pool. 6. Set the `EumsSms` object on your user pool. You can set this
configuration in a [CreateUserPool](../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md "../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md"), [UpdateUserPool](../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserPool.md "../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserPool.md"), or [SetUserPoolMfaConfig](../../../cognito-user-identity-pools/latest/APIReference/API_SetUserPoolMfaConfig.md "../../../cognito-user-identity-pools/latest/APIReference/API_SetUserPoolMfaConfig.md") request. The `CallerArn`
parameter is required. The following example shows the minimum
`EumsSms` configuration:

```
"EumsSms": {
    "CallerArn": "arn:aws:iam::123456789012:role/service-role/CognitoEumsSmsRole",
    "ExternalId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
}
```

To send from a specific origination identity or use a configuration
set, include the `OriginationIdentity` and
`ConfigurationSetName` parameters.

#### IAM permissions for AWS End User Messaging SMS direct SMS

The IAM role in `CallerArn` requires a trust policy that
permits the `cognito-idp.amazonaws.com` service principal to
assume it. Use the same trust policy structure as the Amazon SNS path (see [Prepare an IAM role that Amazon Cognito can use to send SMS messages with AWS End User Messaging SMS](#sms-create-a-role "#sms-create-a-role")). The role
also requires a permissions policy that grants
`sms-voice:SendTextMessage` scoped to your origination identity ARN
(see the setup procedure in [To set up AWS End User Messaging SMS direct SMS for a user pool](#sms-setup-eums "#sms-setup-eums")).

### Choose the AWS Region for SMS messages

###### Note

SMS messages in AWS are now managed in [AWS End User Messaging SMS](https://console.aws.amazon.com/sms-voice/home "https://console.aws.amazon.com/sms-voice/home").

#### Amazon SNS path Region configuration

In some AWS Regions, you can choose the Region that contains
the Amazon SNS resources that you want to use for Amazon Cognito SMS messages. In any
AWS Region where Amazon Cognito is available, except for Asia Pacific (Seoul), you
can use Amazon SNS resources in the AWS Region where you created your user pool. To
make your SMS messaging faster and more reliable when you have a choice of
Regions, use Amazon SNS resources in the same Region
as your user pool.

Choose a Region for SMS resources in the **Configure
message delivery** step of the new user pool wizard. You can also
choose **Edit** under **SMS** in the
**Authentication methods** menu of an existing user
pool.

At launch, for some AWS Regions, Amazon Cognito sent SMS messages with Amazon SNS
resources in an alternate Region. To set your preferred
Region, use the `SnsRegion` parameter of the [SmsConfigurationType](../../../cognito-user-identity-pools/latest/APIReference/API_SmsConfigurationType.md "../../../cognito-user-identity-pools/latest/APIReference/API_SmsConfigurationType.md") object for your user pool. When you
programmatically create an Amazon Cognito user pools resource in an **Amazon Cognito
Region** from the following table and you do not provide an
`SnsRegion` parameter, your user pool can send SMS messages with
Amazon SNS resources in a legacy **Amazon SNS Region**.

Amazon Cognito user pools in the Asia Pacific (Seoul) AWS Region must use your Amazon SNS
configuration in the Asia Pacific (Tokyo) Region.

Amazon SNS (through AWS End User Messaging SMS) sets the spending quota for all new accounts at $1.00
(USD) per month. You might have increased your spend limit in an AWS Region
that you use with Amazon Cognito. Before you change the AWS Region for Amazon SNS SMS
messages, open a quota increase case in the AWS Support Center to increase
your limit in the new Region. For more information, see [Moving from the AWS End User Messaging SMS MMS and Voice sandbox to
production](../../../sms-voice/latest/userguide/sandbox.md#sandbox-sms-move-to-production "../../../sms-voice/latest/userguide/sandbox.md#sandbox-sms-move-to-production") in the _AWS End User Messaging SMS User
Guide_.

You can send SMS messages for any **Amazon Cognito Region** in the
following table with AWS End User Messaging SMS resources in the corresponding **SMS
message Region**.

| Amazon Cognito Region     | SMS message Region                              |
| ------------------------- | ----------------------------------------------- |
| US East (Ohio)            | US East (Ohio), US East (N. Virginia)           |
| US East (N. Virginia)     | US East (N. Virginia)                           |
| US West (N. California)   | US West (N. California)                         |
| US West (Oregon)          | US West (Oregon)                                |
| Canada (Central)          | Canada (Central), US East (N. Virginia)         |
| Canada West (Calgary)     | Canada West (Calgary)                           |
| Mexico (Central)          | Mexico (Central)                                |
| Europe (Frankfurt)        | Europe (Frankfurt), Europe (Ireland)            |
| Europe (London)           | Europe (London), Europe (Ireland)               |
| Europe (Ireland)          | Europe (Ireland)                                |
| Europe (Paris)            | Europe (Paris)                                  |
| Europe (Stockholm)        | Europe (Stockholm)                              |
| Europe (Milan)            | Europe (Milan)                                  |
| Europe (Spain)            | Europe (Spain)                                  |
| Europe (Zurich)           | Europe (Zurich)                                 |
| Asia Pacific (Malaysia)   | Asia Pacific (Singapore)                        |
| Asia Pacific (Thailand)   | Asia Pacific (Mumbai)                           |
| Asia Pacific (Mumbai)     | Asia Pacific (Mumbai), Asia Pacific (Singapore) |
| Asia Pacific (Hyderabad)  | Asia Pacific (Hyderabad)                        |
| Asia Pacific (Hong Kong)  | Asia Pacific (Singapore)                        |
| Asia Pacific (Seoul)      | Asia Pacific (Tokyo)                            |
| Asia Pacific (Singapore)  | Asia Pacific (Singapore)                        |
| Asia Pacific (Sydney)     | Asia Pacific (Sydney)                           |
| Asia Pacific (Tokyo)      | Asia Pacific (Tokyo)                            |
| Asia Pacific (Jakarta)    | Asia Pacific (Jakarta)                          |
| Asia Pacific (Osaka)      | Asia Pacific (Osaka)                            |
| Asia Pacific (Melbourne)  | Asia Pacific (Melbourne)                        |
| Middle East (Bahrain)     | Middle East (Bahrain)                           |
| Middle East (UAE)         | Middle East (UAE)                               |
| South America (São Paulo) | South America (São Paulo)                       |
| Israel (Tel Aviv)         | Israel (Tel Aviv)                               |
| Africa (Cape Town)        | Africa (Cape Town)                              |

#### AWS End User Messaging SMS direct path Region configuration

AWS End User Messaging SMS is available in its own set of AWS Regions, which can differ
from the Regions where Amazon SNS or Amazon Cognito user pools are available. For the
current list, see [Supported Regions and
countries](../../../sms-voice/latest/userguide/regions.md "../../../sms-voice/latest/userguide/regions.md") in the _AWS End User Messaging SMS User
Guide_.

The `Region` field of the `EumsSms` object in
[SmsConfigurationType](../../../cognito-user-identity-pools/latest/APIReference/API_SmsConfigurationType.md "../../../cognito-user-identity-pools/latest/APIReference/API_SmsConfigurationType.md") sets the AWS Region where Amazon Cognito calls
AWS End User Messaging SMS. AWS End User Messaging SMS must be available in your user pool's Region. Omit
`Region` and Amazon Cognito uses AWS End User Messaging SMS in your user pool's Region, or
set `Region` to your user pool's Region explicitly. Amazon Cognito rejects
any other value.

###### Note

If you set `Region` to an unsupported value, the
`CreateUserPool`, `UpdateUserPool`, and
`SetUserPoolMfaConfig` requests fail with an
`InvalidParameterException`.

###### Note

The AWS End User Messaging SMS direct path is not available in the
Asia Pacific (Thailand), Asia Pacific (Hong Kong), and
Asia Pacific (Malaysia) AWS Regions. To send SMS
messages from a user pool in one of these Regions, use the Amazon SNS path
instead. For more information, see [Amazon SNS path Region configuration](#sms-choose-a-region-sns "#sms-choose-a-region-sns").

### Obtain an origination identity to send SMS messages to US phone numbers

If you plan to send SMS text messages to US phone numbers, you must obtain an
origination identity, regardless of whether you build an SMS sandbox testing
environment, or a production environment.

US carriers require an origination identity to send messages to US phone numbers.
If you don't already have an origination identity, you must get one. To learn how to
obtain an origination identity, see [Request a phone
number](../../../sms-voice/latest/userguide/phone-numbers-request.md "../../../sms-voice/latest/userguide/phone-numbers-request.md") in the _AWS End User Messaging SMS User
Guide_.

When you have more than one origination identity in the same AWS Region,
AWS End User Messaging SMS chooses an origination identity type in the following order of priority:
short code, 10DLC, toll-free number. You can't change this priority. For more
information, see [AWS End User Messaging SMS
FAQs](https://aws.amazon.com/end-user-messaging/faqs/ "https://aws.amazon.com/end-user-messaging/faqs/").

### Confirm that you are in the SMS sandbox

Use the following procedure to confirm that you are in the SMS sandbox. Repeat for
each AWS Region where you have production Amazon Cognito user pools.

###### To confirm that you are in the SMS sandbox

1. Go to the [Amazon Cognito
   console](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home"). If prompted, enter your AWS
   credentials.
2. Choose **User Pools**.
3. Choose an existing user pool from the list.
4. Choose the **Authentication methods**
   menu.
5. In the **SMS configuration** section, expand
   **Move to Amazon SNS production environment**.
   If your account is in the SMS sandbox, you will see the following
   message:

**Configure AWS service dependencies to complete your
SMS message setup**

If you don't see this message, then someone has set up SMS
messages in your account already. Skip to [Complete user pool setup in Amazon Cognito](#user-pool-sms-settings-first-time-finish-user-pool "#user-pool-sms-settings-first-time-finish-user-pool"). 6. Choose the [Amazon SNS](https://console.aws.amazon.com/sns/home "https://console.aws.amazon.com/sns/home") link
under **Move to Amazon SNS production
environment**. This opens the Amazon SNS console in a new
tab. 7. Verify that you are in the sandbox environment. The console
message indicates your sandbox status and AWS Region, as
follows:

`This account is in the SMS sandbox in
 US East (N. Virginia).`

### Move your account out of the sandbox

To use your app in production, move your account out of the SMS sandbox and into
production. After you have configured an origination identity in the AWS Region
that contains the AWS End User Messaging SMS resources that you want Amazon Cognito to use, you can verify
US phone numbers while your AWS account remains in the SMS sandbox. When your
environment is in production, you don't need to verify user phone numbers before you
send SMS messages to them.

You can create a request to exit the sandbox from either the AWS End User Messaging SMS console or
the Amazon SNS console. For detailed instructions, see [Moving from the SMS Sandbox](../../../sms-voice/latest/userguide/sandbox.md#sandbox-sms-move-to-production "../../../sms-voice/latest/userguide/sandbox.md#sandbox-sms-move-to-production") in the _AWS End User Messaging SMS
User Guide_.

### Use simulator numbers or verified phone numbers with AWS End User Messaging SMS

If you have moved your account out of the SMS sandbox, skip this step.

If you're in the sandbox but you have set up an origination number, you can send
messages to verified destination numbers. To set up verified destinations, see
[Add a
verified destination phone number](../../../sms-voice/latest/userguide/verify-destination-phone-number.md "../../../sms-voice/latest/userguide/verify-destination-phone-number.md") in the _AWS End User Messaging SMS User Guide_.

You can also send messages with simulated senders and destinations. Simulator
messages produce logs but don't get sent out over the carrier network. From the
[Shortcuts menu](https://console.aws.amazon.com/sms-voice/home?#/shortcuts "https://console.aws.amazon.com/sms-voice/home?#/shortcuts"),
select **Test SMS sending with SMS simulator**. For more
information, see [Simulator phone
numbers](../../../sms-voice/latest/userguide/test-phone-numbers.md "../../../sms-voice/latest/userguide/test-phone-numbers.md") in the _AWS End User Messaging SMS User
Guide_.

### Complete user pool setup in Amazon Cognito

Return to the browser tab where you were creating or [editing](signing-up-users-in-your-app.md#verification-configure "signing-up-users-in-your-app.md#verification-configure") your user pool. Complete the
procedure. When you have successfully added SMS configuration to your user pool,
Amazon Cognito sends a test message to an internal phone number to verify that your
configuration works. AWS End User Messaging SMS charges for each test SMS message.
