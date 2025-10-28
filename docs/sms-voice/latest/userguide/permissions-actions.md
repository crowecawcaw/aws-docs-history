# AWS End User Messaging SMS actions for IAM policies

To manage access to AWS End User Messaging SMS resources in your AWS account, you can add AWS End User Messaging SMS
actions to AWS Identity and Access Management (IAM) policies. By using actions in policies, you can control what
users can do on the AWS End User Messaging SMS console. You can also control what users can do programmatically
by using the AWS SDKs, the AWS Command Line Interface (AWS CLI), or the AWS End User Messaging SMS APIs directly.

This topic identifies AWS End User Messaging SMS actions that you can add to IAM policies for your AWS
account. To see examples that demonstrate how you can use actions in policies to manage
access to AWS End User Messaging SMS resources, see [Identity-based policy
examples for AWS End User Messaging SMS](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

###### Topics

- [AWS End User Messaging SMS and Voice v2 API actions](#permissions-actions-sms-voice-apiactions-V2 "#permissions-actions-sms-voice-apiactions-V2")

## AWS End User Messaging SMS and Voice v2 API actions

This section identifies actions for features that are available from the
AWS End User Messaging SMS and Voice v2 API. For the AWS End User Messaging SMS and Voice v2 API is an API that provides
advanced options for using and managing the SMS and voice channels. For a complete list
of actions available in version 2, see the [AWS End User Messaging SMS and Voice API
version 2 API Reference](../../../pinpoint/latest/apireference_smsvoicev2/Welcome.md "../../../pinpoint/latest/apireference_smsvoicev2/Welcome.md").

**`sms-voice:AssociateOriginationIdentity`**

Associate the specified origination identity with a pool.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:pool/`poolId``
- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:phone-number/`phoneNumberId``
- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:sender-id/senderId/`isoCountyCode``

**`sms-voice:AssociateProtectConfiguration`**

Associate the specified protect configuration with a configuration
set.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:configuration-set/`configurationSetName``
- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:protect-configuration/`ProtectConfigurationId``

**`sms-voice:CreateConfigurationSet`**

Create a new configuration set.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:configuration-set/`configurationSetName``

**`sms-voice:CreateEventDestination`**

Create a new event destination in a configuration set.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:configuration-set/`configurationSetName``

**`sms-voice:CreateOptOutList`**

Create a new opt-out list.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:opt-out-list/`optOutListName``

**`sms-voice:CreatePool`**

Create a new pool and associates the specified origination identity to the
pool.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:pool/`poolId``
- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:phone-number/`phoneNumberId``
- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:sender-id/senderId/`isoCountyCode``

**`sms-voice:CreateProtectConfiguration`**

Create a new protect configuration.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:protect-configuration/`ProtectConfigurationId``

**`sms-voice:CreateRegistration`**

Create a registration.

- Resource ARN –`arn:aws:sms-voice:`region`:`accountId`:registration/`registrationId``

**`sms-voice:CreateRegistrationAssociation`**

Associate aregistration with an origination identity.

- Resource ARN –`arn:aws:sms-voice:`region`:`accountId`:registration/`registrationId``
- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:phone-number/`phoneNumberId``

**`sms-voice:CreateRegistrationAttachment`**

Create an attachment for a registration.

- Resource ARN
  –`arn:aws:sms-voice:`region`:`accountId`:registration-attachment/`registrationAttachmentId``

**`sms-voice:CreateRegistrationVersion`**

Create a new version of the registration.

- Resource ARN –`arn:aws:sms-voice:`region`:`accountId`:registration/`registrationId``

**`sms-voice:CreateVerifiedDestinationNumber`**

Create a new verififed destination phone number.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:verified-destination-number/`verifiedDestinationNumberId``

**`sms-voice:DeleteAccountDefaultProtectConfiguration`**

Disassociate the account default protect configuration.

- Resource ARN – Not available. Use `*`.

**`sms-voice:DeleteConfigurationSet`**

Delete an existing configuration set.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:configuration-set/`configurationSetName``

**`sms-voice:DeleteDefaultMessageType`**

Delete an existing default message type on a configuration set.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:configuration-set/`configurationSetName``

**`sms-voice:DeleteDefaultSenderId`**

Delete an existing default sender ID on a configuration set.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:sender-id/`configuration-set/configurationSetName``

**`sms-voice:DeleteEventDestination`**

Delete an existing event destination.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:configuration-set/`configurationSetName``

**`sms-voice:DeleteKeyword`**

Delete an existing keyword from an origination phone number or
pool.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:pool/`poolId``
- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:phone-number/`phoneNumberId``

**`sms-voice:DeleteMediaMessageSpendLimitOverride`**

Delete an account-level monthly spending limit override for sending MMS
messages.

- Resource ARN – Not available. Use `*`.

**`sms-voice:DeleteOptedOutNumber`**

Delete an existing opted out destination phone number from the specified
opt-out list.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:opt-out-list/`optOutListName``

**`sms-voice:DeleteOptOutList`**

Delete an existing opt-out list. All opted out phone numbers in the
opt-out list are deleted.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:opt-out-list/`optOutListName``

**`sms-voice:DeletePool`**

Delete an existing pool.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:pool/`poolId``

**`sms-voice:DeleteProtectConfiguration`**

Delete a protect configuration.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:protect-configuration/`ProtectConfigurationId``

**`sms-voice:DeleteRegistration`**

Delete a new version of the registration.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:registration/`registrationId``

**`sms-voice:DeleteRegistrationAttachment`**

Delete the registration attachment.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:registration-attachment/`registrationAttachmentId``

**`sms-voice:DeleteRegistrationFieldValue`**

Delete the value from a registration field.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:registration/`registrationId``

**`sms-voice:DeleteTextMessageSpendLimitOverride`**

Delete an account-level monthly spending limit override for sending text
messages.

- Resource ARN – Not available. Use `*`.

**`sms-voice:DeleteVerifiedDestinationNumber`**

Delete a verififed destination phone number.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:verified-destination-number/`verifiedDestinationNumberId``

**`sms-voice:DeleteVoiceMessageSpendLimitOverride`**

Delete an account-level monthly spend limit override for sending voice
messages.

- Resource ARN – Not available. Use `*`.

**`sms-voice:DescribeAccountAttributes`**

Describe attributes of your AWS account.

- Resource ARN – Not available. Use `*`.

**`sms-voice:DescribeAccountLimits`**

Describe the current AWS End User Messaging SMS and Voice V2 resource quotas for your
account.

- Resource ARN – Not available. Use `*`.

**`sms-voice:DescribeConfigurationSets`**

Describe the specified configuration sets or all in your account.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:configuration-set/`configurationSetName``

**`sms-voice:DescribeKeywords`**

Describe the specified keywords or all keywords on your origination phone
number or pool.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:pool/`poolId``
- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:phone-number/`phoneNumberId``

**`sms-voice:DescribeOptedOutNumbers`**

Describe the specified opted out destination numbers or all opted out
destination numbers in an opt-out list.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:opt-out-list/`optOutListName``

**`sms-voice:DescribeOptOutLists`**

Describe the specified opt-out list or all opt-out lists in your
account.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:opt-out-list/`optOutListName``

**`sms-voice:DescribePhoneNumbers`**

Describe the specified origination phone number, or all the phone numbers
in your account.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:phone-number/`phoneNumberId``

**`sms-voice:DescribePools`**

Retrieve the specified pools or all pools associated with your AWS
account.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:pool/`poolId``

**`sms-voice:DescribeProtectConfiguration`**

Retrieve the specified protect configurations.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:protect-configuration/`ProtectConfigurationId``

**`sms-voice:DescribeRegistrationAttachments`**

List all registration attachments.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:registration-attachment/`registrationAttachmentId``

**`sms-voice:DescribeRegistrationFieldDefinitions`**

List the field definition for a registration.

- Resource ARN – Not available. Use `*`.

**`sms-voice:DescribeRegistrationFieldValues`**

List the field values for a registration.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:registration/`registrationId``

**`sms-voice:DescribeRegistrations`**

List the registrations in your account.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:registration/`registrationId``

**`sms-voice:DescribeRegistrationSectionDefinitions`**

List the section definition for a registration.

- Resource ARN – Not available. Use `*`.

**`sms-voice:DescribeRegistrationTypeDefinitions`**

List the type definitions for a registration.

- Resource ARN – Not available. Use `*`.

**`sms-voice:DescribeRegistrationVersions`**

List the versions for a registration.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:registration/`registrationId``

**`sms-voice:DescribeSenderIds`**

Describe the specified SenderIds or all SenderIds associated with your AWS
account.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:sender-id/`senderId/isoCountryCode``

**`sms-voice:DescribeSpendLimits`**

Describe the current AWS End User Messaging SMS monthly spend limits for sending
voice and text messages.

- Resource ARN – Not available. Use `*`.

**`sms-voice:DescribeVerifiedDestinationNumbers`**

List the verififed destination phone numbers in your account.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:verified-destination-number/`verifiedDestinationNumberId``

**`sms-voice:DisassociateOriginationIdentity`**

Remove the specified origination identity from an existing pool.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:pool/`poolId``
- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:phone-number/`phoneNumberId``
- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:sender-id/`senderId/isoCountryCode``

**`sms-voice:DisassociateProtectConfiguration`**

Disassociate a configuration set from a protect configuration.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:protect-configuration/`ProtectConfigurationId``
- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:configuration-set/`configurationSetName``

**`sms-voice:DiscardRegistrationVersion`**

Discard the current version of a registration.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:registration/`registrationId``

**`sms-voice:GetProtectConfigurationCountryRuleSet`**

Get the country rule set for a protect configuration.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:protect-configuration/`ProtectConfigurationId``

**`sms-voice:ListPoolOriginationIdentities`**

Show the origination phone numbers in a pool.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:pool/`poolId``

**`sms-voice:ListRegistrationAssociations`**

List all resources associated with the registration.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:registration/`registrationId``

**`sms-voice:ListTagsForResource`**

List the tags associated with a resource.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:configuration-set/`configurationSetName``
- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:opt-out-list/`optOutListName``
- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:phone-number/`phoneNumberId``
- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:pool/`poolId``
- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:sender-id/`senderId/isoCountryCode``

**`sms-voice:ProtectConfiguration`**

A protect configuration controls which destination countries messages can
be sent to.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:protect-configuration/`ProtectConfigurationId``

**`sms-voice:PutKeyword`**

Add or update a keyword on an origination phone number or pool.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:phone-number/`phoneNumberId``
- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:pool/`poolId``

**`sms-voice:PutOptedOutNumber`**

Add a destination phone number to an opt-out list.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:opt-out-list/`optOutListName``

**`sms-voice:PutRegistrationFieldValue`**

Update a field value in the registration.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:registration/`registrationId``

**`sms-voice:ReleasePhoneNumber`**

Remove an origination phone number from your AWS End User Messaging SMS account.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:phone-number/`phoneNumberId``

**`sms-voice:ReleaseSenderId`**

Remove a sender ID from your AWS End User Messaging SMS account.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:sender-id/`senderId/isoCountryCode``

**`sms-voice:RequestPhoneNumber`**

Request to add an origination phone number to your account.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:phone-number/`phoneNumberId``
- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:pool/`poolId``

**`sms-voice:RequestSenderId`**

Request a new sender ID.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:sender-id/`senderId/isoCountryCode``

**`sms-voice:SendDestinationNumberVerificationCode`**

Send an SMS or voice message containg a verification code to the dsetination phone number.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:phone-number/`phoneNumberId``
- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:pool/`poolId``
- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:sender-id/`senderId/isoCountryCode``

**`sms-voice:SendMediaMessage`**

Send an MMS message.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:phone-number/`phoneNumberId``
- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:pool/`poolId``
- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:sender-id/`senderId/isoCountryCode``

**`sms-voice:SendTextMessage`**

Send an SMS message.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:phone-number/`phoneNumberId``
- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:pool/`poolId``
- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:sender-id/`senderId/isoCountryCode``

**`sms-voice:SendVoiceMessage`**

Send a voice message.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:phone-number/`phoneNumberId``
- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:pool/`poolId``

**`sms-voice:SetAccountDefaultProtectConfiguration`**

Set the account protect configuration.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:protect-configuration/`ProtectConfigurationId``

**`sms-voice:SetDefaultMessageType`**

Set the default message type for SMS messages.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:configuration-set/`configurationSetName``

**`sms-voice:SetDefaultSenderId`**

Set the default sender ID value for voice messages.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:configuration-set/`configurationSetName``

**`sms-voice:SetMediaMessageSpendLimitOverride`**

Set a monthly spending limit for MMS messages.

- Resource ARN – Not available. Use `*`.

**`sms-voice:SetTextMessageSpendLimitOverride`**

Set a monthly spending limit for SMS messages.

- Resource ARN – Not available. Use `*`.

**`sms-voice:SetVoiceMessageSpendLimitOverride`**

Set a monthly spending limit for voice messages.

- Resource ARN – Not available. Use `*`.

**`sms-voice:SubmitRegistrationVersion`**

Submit the latest version of a registration.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:registration/`registrationId``

**`sms-voice:TagResource`**

Add a tag to a resource.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:configuration-set/`configurationSetName``
- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:opt-out-list/`optOutListName``
- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:phone-number/`phoneNumberId``
- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:pool/`poolId``
- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:sender-id/`senderId/isoCountryCode``

**`sms-voice:UntagResource`**

Remove tags from a resource.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:configuration-set/`configurationSetName``
- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:opt-out-list/`optOutListName``
- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:phone-number/`phoneNumberId``
- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:pool/`poolId``
- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:sender-id/`senderId/isoCountryCode``

**`sms-voice:UpdateEventDestination`**

Update an existing event destination.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:configuration-set/`configurationSetName``

**`sms-voice:UpdatePhoneNumber`**

Update the configuration of an origination phone number.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:phone-number/`phoneNumberId``

**`sms-voice:UpdateProtectConfiguration`**

Update the protect configuration.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:protect-configuration/`ProtectConfigurationId``

**`sms-voice:UpdateProtectConfigurationCountryRuleSet`**

Update the country rule set of a protect configuration.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:protect-configuration/`ProtectConfigurationId``

**`sms-voice:UpdatePool`**

Update an existing phone number pool.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:pool/`poolId``

**`sms-voice:UpdateSenderId`**

Update a sender ID.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:sender-id/`senderId/isoCountryCode``

**`sms-voice:VerifyDestinationNumber`**

Verify a destination phone number.

- Resource ARN –
  `arn:aws:sms-voice:`region`:`accountId`:verified-destination-number/`verifiedDestinationNumberId``
