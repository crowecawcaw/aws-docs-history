

# Actions, resources, and condition keys for AWS End User Messaging SMS and Voice V2
<a name="list_pinpoint-sms-voice-v2"></a>

AWS End User Messaging SMS and Voice V2 (service prefix: `sms-voice`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/pinpoint/latest/userguide/welcome.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/pinpoint/latest/developerguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/sms-voice/sms-voice.json) for this service.

**Topics**
+ [API operations defined by AWS End User Messaging SMS and Voice V2](#list_pinpoint-sms-voice-v2-operations)
+ [Actions defined by AWS End User Messaging SMS and Voice V2](#list_pinpoint-sms-voice-v2-actions-as-permissions)
+ [Resource types defined by AWS End User Messaging SMS and Voice V2](#list_pinpoint-sms-voice-v2-resources-for-iam-policies)
+ [Condition keys for AWS End User Messaging SMS and Voice V2](#list_pinpoint-sms-voice-v2-policy-keys)

## API operations defined by AWS End User Messaging SMS and Voice V2
<a name="list_pinpoint-sms-voice-v2-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_pinpoint-sms-voice-v2-actions-as-permissions).




- **   AssociateOriginationIdentity  **
  - **IAM action:**  [sms-voice:AssociateOriginationIdentity](#list_pinpoint-sms-voice-v2-action-AssociateOriginationIdentity) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateProtectConfiguration  **
  - **IAM action:**  [sms-voice:AssociateProtectConfiguration](#list_pinpoint-sms-voice-v2-action-AssociateProtectConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CarrierLookup  **
  - **IAM action:**  [sms-voice:CarrierLookup](#list_pinpoint-sms-voice-v2-action-CarrierLookup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   CreateConfigurationSet  **
  - **IAM action:**  [sms-voice:CreateConfigurationSet](#list_pinpoint-sms-voice-v2-action-CreateConfigurationSet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sms-voice:TagResource](#list_pinpoint-sms-voice-v2-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateEventDestination  **
  - **IAM action:**  [sms-voice:CreateEventDestination](#list_pinpoint-sms-voice-v2-action-CreateEventDestination)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sms-voice.amazonaws.com / **Access level:** Write

- **   CreateNotifyConfiguration  **
  - **IAM action:**  [sms-voice:CreateNotifyConfiguration](#list_pinpoint-sms-voice-v2-action-CreateNotifyConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sms-voice:TagResource](#list_pinpoint-sms-voice-v2-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateOptOutList  **
  - **IAM action:**  [sms-voice:CreateOptOutList](#list_pinpoint-sms-voice-v2-action-CreateOptOutList)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sms-voice:TagResource](#list_pinpoint-sms-voice-v2-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreatePool  **
  - **IAM action:**  [sms-voice:CreatePool](#list_pinpoint-sms-voice-v2-action-CreatePool)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sms-voice:TagResource](#list_pinpoint-sms-voice-v2-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateProtectConfiguration  **
  - **IAM action:**  [sms-voice:CreateProtectConfiguration](#list_pinpoint-sms-voice-v2-action-CreateProtectConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sms-voice:TagResource](#list_pinpoint-sms-voice-v2-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateRcsAgent  **
  - **IAM action:**  [sms-voice:CreateRcsAgent](#list_pinpoint-sms-voice-v2-action-CreateRcsAgent)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sms-voice:TagResource](#list_pinpoint-sms-voice-v2-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateRegistration  **
  - **IAM action:**  [sms-voice:CreateRegistration](#list_pinpoint-sms-voice-v2-action-CreateRegistration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sms-voice:TagResource](#list_pinpoint-sms-voice-v2-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateRegistrationAssociation  **
  - **IAM action:**  [sms-voice:CreateRegistrationAssociation](#list_pinpoint-sms-voice-v2-action-CreateRegistrationAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateRegistrationAttachment  **
  - **IAM action:**  [sms-voice:CreateRegistrationAttachment](#list_pinpoint-sms-voice-v2-action-CreateRegistrationAttachment)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sms-voice:TagResource](#list_pinpoint-sms-voice-v2-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateRegistrationVersion  **
  - **IAM action:**  [sms-voice:CreateRegistrationVersion](#list_pinpoint-sms-voice-v2-action-CreateRegistrationVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateVerifiedDestinationNumber  **
  - **IAM action:**  [sms-voice:CreateVerifiedDestinationNumber](#list_pinpoint-sms-voice-v2-action-CreateVerifiedDestinationNumber)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sms-voice:TagResource](#list_pinpoint-sms-voice-v2-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteAccountDefaultProtectConfiguration  **
  - **IAM action:**  [sms-voice:DeleteAccountDefaultProtectConfiguration](#list_pinpoint-sms-voice-v2-action-DeleteAccountDefaultProtectConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteConfigurationSet  **
  - **IAM action:**  [sms-voice:DeleteConfigurationSet](#list_pinpoint-sms-voice-v2-action-DeleteConfigurationSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDefaultMessageType  **
  - **IAM action:**  [sms-voice:DeleteDefaultMessageType](#list_pinpoint-sms-voice-v2-action-DeleteDefaultMessageType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDefaultSenderId  **
  - **IAM action:**  [sms-voice:DeleteDefaultSenderId](#list_pinpoint-sms-voice-v2-action-DeleteDefaultSenderId) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEventDestination  **
  - **IAM action:**  [sms-voice:DeleteEventDestination](#list_pinpoint-sms-voice-v2-action-DeleteEventDestination) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteKeyword  **
  - **IAM action:**  [sms-voice:DeleteKeyword](#list_pinpoint-sms-voice-v2-action-DeleteKeyword) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteMediaMessageSpendLimitOverride  **
  - **IAM action:**  [sms-voice:DeleteMediaMessageSpendLimitOverride](#list_pinpoint-sms-voice-v2-action-DeleteMediaMessageSpendLimitOverride) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteNotifyConfiguration  **
  - **IAM action:**  [sms-voice:DeleteNotifyConfiguration](#list_pinpoint-sms-voice-v2-action-DeleteNotifyConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteNotifyMessageSpendLimitOverride  **
  - **IAM action:**  [sms-voice:DeleteNotifyMessageSpendLimitOverride](#list_pinpoint-sms-voice-v2-action-DeleteNotifyMessageSpendLimitOverride) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteOptOutList  **
  - **IAM action:**  [sms-voice:DeleteOptOutList](#list_pinpoint-sms-voice-v2-action-DeleteOptOutList) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteOptedOutNumber  **
  - **IAM action:**  [sms-voice:DeleteOptedOutNumber](#list_pinpoint-sms-voice-v2-action-DeleteOptedOutNumber) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePool  **
  - **IAM action:**  [sms-voice:DeletePool](#list_pinpoint-sms-voice-v2-action-DeletePool) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteProtectConfiguration  **
  - **IAM action:**  [sms-voice:DeleteProtectConfiguration](#list_pinpoint-sms-voice-v2-action-DeleteProtectConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteProtectConfigurationRuleSetNumberOverride  **
  - **IAM action:**  [sms-voice:DeleteProtectConfigurationRuleSetNumberOverride](#list_pinpoint-sms-voice-v2-action-DeleteProtectConfigurationRuleSetNumberOverride) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRcsAgent  **
  - **IAM action:**  [sms-voice:DeleteRcsAgent](#list_pinpoint-sms-voice-v2-action-DeleteRcsAgent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRcsMessageSpendLimitOverride  **
  - **IAM action:**  [sms-voice:DeleteRcsMessageSpendLimitOverride](#list_pinpoint-sms-voice-v2-action-DeleteRcsMessageSpendLimitOverride) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRegistration  **
  - **IAM action:**  [sms-voice:DeleteRegistration](#list_pinpoint-sms-voice-v2-action-DeleteRegistration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRegistrationAttachment  **
  - **IAM action:**  [sms-voice:DeleteRegistrationAttachment](#list_pinpoint-sms-voice-v2-action-DeleteRegistrationAttachment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRegistrationFieldValue  **
  - **IAM action:**  [sms-voice:DeleteRegistrationFieldValue](#list_pinpoint-sms-voice-v2-action-DeleteRegistrationFieldValue) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteResourcePolicy  **
  - **IAM action:**  [sms-voice:DeleteResourcePolicy](#list_pinpoint-sms-voice-v2-action-DeleteResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DeleteTextMessageSpendLimitOverride  **
  - **IAM action:**  [sms-voice:DeleteTextMessageSpendLimitOverride](#list_pinpoint-sms-voice-v2-action-DeleteTextMessageSpendLimitOverride) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteVerifiedDestinationNumber  **
  - **IAM action:**  [sms-voice:DeleteVerifiedDestinationNumber](#list_pinpoint-sms-voice-v2-action-DeleteVerifiedDestinationNumber) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteVoiceMessageSpendLimitOverride  **
  - **IAM action:**  [sms-voice:DeleteVoiceMessageSpendLimitOverride](#list_pinpoint-sms-voice-v2-action-DeleteVoiceMessageSpendLimitOverride) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeAccountAttributes  **
  - **IAM action:**  [sms-voice:DescribeAccountAttributes](#list_pinpoint-sms-voice-v2-action-DescribeAccountAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAccountLimits  **
  - **IAM action:**  [sms-voice:DescribeAccountLimits](#list_pinpoint-sms-voice-v2-action-DescribeAccountLimits) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeConfigurationSets  **
  - **IAM action:**  [sms-voice:DescribeConfigurationSets](#list_pinpoint-sms-voice-v2-action-DescribeConfigurationSets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeKeywords  **
  - **IAM action:**  [sms-voice:DescribeKeywords](#list_pinpoint-sms-voice-v2-action-DescribeKeywords) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeNotifyConfigurations  **
  - **IAM action:**  [sms-voice:DescribeNotifyConfigurations](#list_pinpoint-sms-voice-v2-action-DescribeNotifyConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeNotifyTemplates  **
  - **IAM action:**  [sms-voice:DescribeNotifyTemplates](#list_pinpoint-sms-voice-v2-action-DescribeNotifyTemplates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeOptOutLists  **
  - **IAM action:**  [sms-voice:DescribeOptOutLists](#list_pinpoint-sms-voice-v2-action-DescribeOptOutLists) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeOptedOutNumbers  **
  - **IAM action:**  [sms-voice:DescribeOptedOutNumbers](#list_pinpoint-sms-voice-v2-action-DescribeOptedOutNumbers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribePhoneNumbers  **
  - **IAM action:**  [sms-voice:DescribePhoneNumbers](#list_pinpoint-sms-voice-v2-action-DescribePhoneNumbers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribePools  **
  - **IAM action:**  [sms-voice:DescribePools](#list_pinpoint-sms-voice-v2-action-DescribePools) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeProtectConfigurations  **
  - **IAM action:**  [sms-voice:DescribeProtectConfigurations](#list_pinpoint-sms-voice-v2-action-DescribeProtectConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeRcsAgentCountryLaunchStatus  **
  - **IAM action:**  [sms-voice:DescribeRcsAgentCountryLaunchStatus](#list_pinpoint-sms-voice-v2-action-DescribeRcsAgentCountryLaunchStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeRcsAgents  **
  - **IAM action:**  [sms-voice:DescribeRcsAgents](#list_pinpoint-sms-voice-v2-action-DescribeRcsAgents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeRegistrationAttachments  **
  - **IAM action:**  [sms-voice:DescribeRegistrationAttachments](#list_pinpoint-sms-voice-v2-action-DescribeRegistrationAttachments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeRegistrationFieldDefinitions  **
  - **IAM action:**  [sms-voice:DescribeRegistrationFieldDefinitions](#list_pinpoint-sms-voice-v2-action-DescribeRegistrationFieldDefinitions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeRegistrationFieldValues  **
  - **IAM action:**  [sms-voice:DescribeRegistrationFieldValues](#list_pinpoint-sms-voice-v2-action-DescribeRegistrationFieldValues) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeRegistrationSectionDefinitions  **
  - **IAM action:**  [sms-voice:DescribeRegistrationSectionDefinitions](#list_pinpoint-sms-voice-v2-action-DescribeRegistrationSectionDefinitions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeRegistrationTypeDefinitions  **
  - **IAM action:**  [sms-voice:DescribeRegistrationTypeDefinitions](#list_pinpoint-sms-voice-v2-action-DescribeRegistrationTypeDefinitions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeRegistrationVersions  **
  - **IAM action:**  [sms-voice:DescribeRegistrationVersions](#list_pinpoint-sms-voice-v2-action-DescribeRegistrationVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeRegistrations  **
  - **IAM action:**  [sms-voice:DescribeRegistrations](#list_pinpoint-sms-voice-v2-action-DescribeRegistrations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeSenderIds  **
  - **IAM action:**  [sms-voice:DescribeSenderIds](#list_pinpoint-sms-voice-v2-action-DescribeSenderIds) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeSpendLimits  **
  - **IAM action:**  [sms-voice:DescribeSpendLimits](#list_pinpoint-sms-voice-v2-action-DescribeSpendLimits) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeVerifiedDestinationNumbers  **
  - **IAM action:**  [sms-voice:DescribeVerifiedDestinationNumbers](#list_pinpoint-sms-voice-v2-action-DescribeVerifiedDestinationNumbers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DisassociateOriginationIdentity  **
  - **IAM action:**  [sms-voice:DisassociateOriginationIdentity](#list_pinpoint-sms-voice-v2-action-DisassociateOriginationIdentity) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateProtectConfiguration  **
  - **IAM action:**  [sms-voice:DisassociateProtectConfiguration](#list_pinpoint-sms-voice-v2-action-DisassociateProtectConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DiscardRegistrationVersion  **
  - **IAM action:**  [sms-voice:DiscardRegistrationVersion](#list_pinpoint-sms-voice-v2-action-DiscardRegistrationVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetProtectConfigurationCountryRuleSet  **
  - **IAM action:**  [sms-voice:GetProtectConfigurationCountryRuleSet](#list_pinpoint-sms-voice-v2-action-GetProtectConfigurationCountryRuleSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResourcePolicy  **
  - **IAM action:**  [sms-voice:GetResourcePolicy](#list_pinpoint-sms-voice-v2-action-GetResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListNotifyCountries  **
  - **IAM action:**  [sms-voice:ListNotifyCountries](#list_pinpoint-sms-voice-v2-action-ListNotifyCountries) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListPoolOriginationIdentities  **
  - **IAM action:**  [sms-voice:ListPoolOriginationIdentities](#list_pinpoint-sms-voice-v2-action-ListPoolOriginationIdentities) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListProtectConfigurationRuleSetNumberOverrides  **
  - **IAM action:**  [sms-voice:ListProtectConfigurationRuleSetNumberOverrides](#list_pinpoint-sms-voice-v2-action-ListProtectConfigurationRuleSetNumberOverrides) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListRegistrationAssociations  **
  - **IAM action:**  [sms-voice:ListRegistrationAssociations](#list_pinpoint-sms-voice-v2-action-ListRegistrationAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTagsForResource  **
  - **IAM action:**  [sms-voice:ListTagsForResource](#list_pinpoint-sms-voice-v2-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PutKeyword  **
  - **IAM action:**  [sms-voice:PutKeyword](#list_pinpoint-sms-voice-v2-action-PutKeyword) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutMessageFeedback  **
  - **IAM action:**  [sms-voice:PutMessageFeedback](#list_pinpoint-sms-voice-v2-action-PutMessageFeedback) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutOptedOutNumber  **
  - **IAM action:**  [sms-voice:PutOptedOutNumber](#list_pinpoint-sms-voice-v2-action-PutOptedOutNumber) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutProtectConfigurationRuleSetNumberOverride  **
  - **IAM action:**  [sms-voice:PutProtectConfigurationRuleSetNumberOverride](#list_pinpoint-sms-voice-v2-action-PutProtectConfigurationRuleSetNumberOverride) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutRegistrationFieldValue  **
  - **IAM action:**  [sms-voice:PutRegistrationFieldValue](#list_pinpoint-sms-voice-v2-action-PutRegistrationFieldValue) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutResourcePolicy  **
  - **IAM action:**  [sms-voice:PutResourcePolicy](#list_pinpoint-sms-voice-v2-action-PutResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   ReleasePhoneNumber  **
  - **IAM action:**  [sms-voice:ReleasePhoneNumber](#list_pinpoint-sms-voice-v2-action-ReleasePhoneNumber) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ReleaseSenderId  **
  - **IAM action:**  [sms-voice:ReleaseSenderId](#list_pinpoint-sms-voice-v2-action-ReleaseSenderId) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RequestPhoneNumber  **
  - **IAM action:**  [sms-voice:AssociateOriginationIdentity](#list_pinpoint-sms-voice-v2-action-AssociateOriginationIdentity)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sms-voice:RequestPhoneNumber](#list_pinpoint-sms-voice-v2-action-RequestPhoneNumber)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sms-voice:TagResource](#list_pinpoint-sms-voice-v2-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   RequestSenderId  **
  - **IAM action:**  [sms-voice:RequestSenderId](#list_pinpoint-sms-voice-v2-action-RequestSenderId)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sms-voice:TagResource](#list_pinpoint-sms-voice-v2-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   SendDestinationNumberVerificationCode  **
  - **IAM action:**  [sms-voice:SendDestinationNumberVerificationCode](#list_pinpoint-sms-voice-v2-action-SendDestinationNumberVerificationCode)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sms-voice:SendTextMessage](#list_pinpoint-sms-voice-v2-action-SendTextMessage)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sms-voice:SendVoiceMessage](#list_pinpoint-sms-voice-v2-action-SendVoiceMessage)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   SendMediaMessage  **
  - **IAM action:**  [sms-voice:SendMediaMessage](#list_pinpoint-sms-voice-v2-action-SendMediaMessage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SendNotifyTextMessage  **
  - **IAM action:**  [sms-voice:SendNotifyTextMessage](#list_pinpoint-sms-voice-v2-action-SendNotifyTextMessage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SendNotifyVoiceMessage  **
  - **IAM action:**  [sms-voice:SendNotifyVoiceMessage](#list_pinpoint-sms-voice-v2-action-SendNotifyVoiceMessage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SendRcsMessage  **
  - **IAM action:**  [sms-voice:SendRcsMessage](#list_pinpoint-sms-voice-v2-action-SendRcsMessage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SendTextMessage  **
  - **IAM action:**  [sms-voice:SendTextMessage](#list_pinpoint-sms-voice-v2-action-SendTextMessage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SendVoiceMessage  **
  - **IAM action:**  [sms-voice:SendVoiceMessage](#list_pinpoint-sms-voice-v2-action-SendVoiceMessage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SetAccountDefaultProtectConfiguration  **
  - **IAM action:**  [sms-voice:SetAccountDefaultProtectConfiguration](#list_pinpoint-sms-voice-v2-action-SetAccountDefaultProtectConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SetDefaultMessageFeedbackEnabled  **
  - **IAM action:**  [sms-voice:SetDefaultMessageFeedbackEnabled](#list_pinpoint-sms-voice-v2-action-SetDefaultMessageFeedbackEnabled) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SetDefaultMessageType  **
  - **IAM action:**  [sms-voice:SetDefaultMessageType](#list_pinpoint-sms-voice-v2-action-SetDefaultMessageType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SetDefaultSenderId  **
  - **IAM action:**  [sms-voice:SetDefaultSenderId](#list_pinpoint-sms-voice-v2-action-SetDefaultSenderId) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SetMediaMessageSpendLimitOverride  **
  - **IAM action:**  [sms-voice:SetMediaMessageSpendLimitOverride](#list_pinpoint-sms-voice-v2-action-SetMediaMessageSpendLimitOverride) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SetNotifyMessageSpendLimitOverride  **
  - **IAM action:**  [sms-voice:SetNotifyMessageSpendLimitOverride](#list_pinpoint-sms-voice-v2-action-SetNotifyMessageSpendLimitOverride) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SetRcsMessageSpendLimitOverride  **
  - **IAM action:**  [sms-voice:SetRcsMessageSpendLimitOverride](#list_pinpoint-sms-voice-v2-action-SetRcsMessageSpendLimitOverride) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SetTextMessageSpendLimitOverride  **
  - **IAM action:**  [sms-voice:SetTextMessageSpendLimitOverride](#list_pinpoint-sms-voice-v2-action-SetTextMessageSpendLimitOverride) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SetVoiceMessageSpendLimitOverride  **
  - **IAM action:**  [sms-voice:SetVoiceMessageSpendLimitOverride](#list_pinpoint-sms-voice-v2-action-SetVoiceMessageSpendLimitOverride) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SubmitRegistrationVersion  **
  - **IAM action:**  [sms-voice:SubmitRegistrationVersion](#list_pinpoint-sms-voice-v2-action-SubmitRegistrationVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [sms-voice:TagResource](#list_pinpoint-sms-voice-v2-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [sms-voice:UntagResource](#list_pinpoint-sms-voice-v2-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateEventDestination  **
  - **IAM action:**  [sms-voice:UpdateEventDestination](#list_pinpoint-sms-voice-v2-action-UpdateEventDestination)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sms-voice.amazonaws.com / **Access level:** Write

- **   UpdateNotifyConfiguration  **
  - **IAM action:**  [sms-voice:UpdateNotifyConfiguration](#list_pinpoint-sms-voice-v2-action-UpdateNotifyConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdatePhoneNumber  **
  - **IAM action:**  [sms-voice:UpdatePhoneNumber](#list_pinpoint-sms-voice-v2-action-UpdatePhoneNumber)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sms-voice.amazonaws.com / **Access level:** Write

- **   UpdatePool  **
  - **IAM action:**  [sms-voice:UpdatePool](#list_pinpoint-sms-voice-v2-action-UpdatePool)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sms-voice.amazonaws.com / **Access level:** Write

- **   UpdateProtectConfiguration  **
  - **IAM action:**  [sms-voice:UpdateProtectConfiguration](#list_pinpoint-sms-voice-v2-action-UpdateProtectConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateProtectConfigurationCountryRuleSet  **
  - **IAM action:**  [sms-voice:UpdateProtectConfigurationCountryRuleSet](#list_pinpoint-sms-voice-v2-action-UpdateProtectConfigurationCountryRuleSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRcsAgent  **
  - **IAM action:**  [sms-voice:UpdateRcsAgent](#list_pinpoint-sms-voice-v2-action-UpdateRcsAgent)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sms-voice.amazonaws.com / **Access level:** Write

- **   UpdateSenderId  **
  - **IAM action:**  [sms-voice:UpdateSenderId](#list_pinpoint-sms-voice-v2-action-UpdateSenderId) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   VerifyDestinationNumber  **
  - **IAM action:**  [sms-voice:VerifyDestinationNumber](#list_pinpoint-sms-voice-v2-action-VerifyDestinationNumber) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS End User Messaging SMS and Voice V2
<a name="list_pinpoint-sms-voice-v2-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AssociateOriginationIdentity](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_AssociateOriginationIdentity.html)  **
  - **Description:** Grants permission to associate an origination phone number or sender ID to a pool
  - **Resource types (\*required):** [PhoneNumber](#list_pinpoint-sms-voice-v2-resource-PhoneNumber) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Pool\*](#list_pinpoint-sms-voice-v2-resource-Pool) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [RcsAgent](#list_pinpoint-sms-voice-v2-resource-RcsAgent) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [SenderId](#list_pinpoint-sms-voice-v2-resource-SenderId) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AssociateProtectConfiguration](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_AssociateProtectConfiguration.html)  **
  - **Description:** Grants permission to associate a protect configuration to a configuration set
  - **Resource types (\*required):** [ConfigurationSet\*](#list_pinpoint-sms-voice-v2-resource-ConfigurationSet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ProtectConfiguration\*](#list_pinpoint-sms-voice-v2-resource-ProtectConfiguration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CarrierLookup](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_CarrierLookup.html)  **
  - **Description:** Grants permission to look up carrier information for a phone number
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [CreateConfigurationSet](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_CreateConfigurationSet.html)  **
  - **Description:** Grants permission to create a configuration set
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-sms-voice-v2-aws_TagKeys)
  - **Access level:** Write

- **   [CreateEventDestination](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_CreateEventDestination.html)  **
  - **Description:** Grants permission to create an event destination within a configuration set
  - **Resource types (\*required):** [ConfigurationSet\*](#list_pinpoint-sms-voice-v2-resource-ConfigurationSet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateNotifyConfiguration](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_CreateNotifyConfiguration.html)  **
  - **Description:** Grants permission to create a notify configuration
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-sms-voice-v2-aws_TagKeys)
  - **Access level:** Write

- **   [CreateOptOutList](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_CreateOptOutList.html)  **
  - **Description:** Grants permission to create an opt-out list
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-sms-voice-v2-aws_TagKeys)
  - **Access level:** Write

- **   [CreatePool](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_CreatePool.html)  **
  - **Description:** Grants permission to create a pool
  - **Resource types (\*required):** [PhoneNumber](#list_pinpoint-sms-voice-v2-resource-PhoneNumber) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-sms-voice-v2-aws_TagKeys)
  - **Resource types (\*required):** [SenderId](#list_pinpoint-sms-voice-v2-resource-SenderId) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-sms-voice-v2-aws_TagKeys)
  - **Access level:** Write

- **   [CreateProtectConfiguration](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_CreateProtectConfiguration.html)  **
  - **Description:** Grants permission to create a protect configuration
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-sms-voice-v2-aws_TagKeys)
  - **Access level:** Write

- **   [CreateRcsAgent](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_CreateRcsAgent.html)  **
  - **Description:** Grants permission to create an RCS agent
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-sms-voice-v2-aws_TagKeys)
  - **Access level:** Write

- **   [CreateRegistration](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_CreateRegistration.html)  **
  - **Description:** Grants permission to create a registration
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-sms-voice-v2-aws_TagKeys)
  - **Access level:** Write

- **   [CreateRegistrationAssociation](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_CreateRegistrationAssociation.html)  **
  - **Description:** Grants permission to associate a registration with a phone number or another registration
  - **Resource types (\*required):** [PhoneNumber](#list_pinpoint-sms-voice-v2-resource-PhoneNumber) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [RcsAgent](#list_pinpoint-sms-voice-v2-resource-RcsAgent) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Registration\*](#list_pinpoint-sms-voice-v2-resource-Registration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateRegistrationAttachment](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_CreateRegistrationAttachment.html)  **
  - **Description:** Grants permission to create a registration attachment
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-sms-voice-v2-aws_TagKeys)
  - **Access level:** Write

- **   [CreateRegistrationVersion](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_CreateRegistrationVersion.html)  **
  - **Description:** Grants permission to create a registration version
  - **Resource types (\*required):** [Registration\*](#list_pinpoint-sms-voice-v2-resource-Registration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateVerifiedDestinationNumber](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_CreateVerifiedDestinationNumber.html)  **
  - **Description:** Grants permission to create a verified destination number
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-sms-voice-v2-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteAccountDefaultProtectConfiguration](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DeleteAccountDefaultProtectConfiguration.html)  **
  - **Description:** Grants permission to delete the account default protect configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteConfigurationSet](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DeleteConfigurationSet.html)  **
  - **Description:** Grants permission to delete a configuration set
  - **Resource types (\*required):** [ConfigurationSet\*](#list_pinpoint-sms-voice-v2-resource-ConfigurationSet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDefaultMessageType](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DeleteDefaultMessageType.html)  **
  - **Description:** Grants permission to delete the default message type for a configuration set
  - **Resource types (\*required):** [ConfigurationSet\*](#list_pinpoint-sms-voice-v2-resource-ConfigurationSet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDefaultSenderId](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DeleteDefaultSenderId.html)  **
  - **Description:** Grants permission to delete the default sender ID for a configuration set
  - **Resource types (\*required):** [ConfigurationSet\*](#list_pinpoint-sms-voice-v2-resource-ConfigurationSet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteEventDestination](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DeleteEventDestination.html)  **
  - **Description:** Grants permission to delete an event destination within a configuration set
  - **Resource types (\*required):** [ConfigurationSet\*](#list_pinpoint-sms-voice-v2-resource-ConfigurationSet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteKeyword](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DeleteKeyword.html)  **
  - **Description:** Grants permission to delete a keyword for a pool or origination phone number
  - **Resource types (\*required):** [PhoneNumber](#list_pinpoint-sms-voice-v2-resource-PhoneNumber) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Pool](#list_pinpoint-sms-voice-v2-resource-Pool) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteMediaMessageSpendLimitOverride](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DeleteMediaMessageSpendLimitOverride.html)  **
  - **Description:** Grants permission to delete an override for your account's media messaging monthly spend limit
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteNotifyConfiguration](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DeleteNotifyConfiguration.html)  **
  - **Description:** Grants permission to delete a notify configuration
  - **Resource types (\*required):** [NotifyConfiguration\*](#list_pinpoint-sms-voice-v2-resource-NotifyConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteNotifyMessageSpendLimitOverride](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DeleteNotifyMessageSpendLimitOverride.html)  **
  - **Description:** Grants permission to delete an override for your account's notify messaging monthly spend limit
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteOptOutList](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DeleteOptOutList.html)  **
  - **Description:** Grants permission to delete an opt-out list
  - **Resource types (\*required):** [OptOutList\*](#list_pinpoint-sms-voice-v2-resource-OptOutList)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteOptedOutNumber](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DeleteOptedOutNumber.html)  **
  - **Description:** Grants permission to delete a destination phone number from an opt-out list
  - **Resource types (\*required):** [OptOutList\*](#list_pinpoint-sms-voice-v2-resource-OptOutList)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePool](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DeletePool.html)  **
  - **Description:** Grants permission to delete a pool
  - **Resource types (\*required):** [Pool\*](#list_pinpoint-sms-voice-v2-resource-Pool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteProtectConfiguration](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DeleteProtectConfiguration.html)  **
  - **Description:** Grants permission to delete a protect configuration
  - **Resource types (\*required):** [ProtectConfiguration\*](#list_pinpoint-sms-voice-v2-resource-ProtectConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteProtectConfigurationRuleSetNumberOverride](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DeleteProtectConfigurationRuleSetNumberOverride.html)  **
  - **Description:** Grants permission to delete a phone number override for a protect configuration
  - **Resource types (\*required):** [ProtectConfiguration\*](#list_pinpoint-sms-voice-v2-resource-ProtectConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRcsAgent](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DeleteRcsAgent.html)  **
  - **Description:** Grants permission to delete an RCS agent
  - **Resource types (\*required):** [RcsAgent\*](#list_pinpoint-sms-voice-v2-resource-RcsAgent)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRcsMessageSpendLimitOverride](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DeleteRcsMessageSpendLimitOverride.html)  **
  - **Description:** Grants permission to delete an override for your account's RCS messaging monthly spend limit
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteRegistration](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DeleteRegistration.html)  **
  - **Description:** Grants permission to delete a registration
  - **Resource types (\*required):** [Registration\*](#list_pinpoint-sms-voice-v2-resource-Registration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRegistrationAttachment](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DeleteRegistrationAttachment.html)  **
  - **Description:** Grants permission to delete a registration attachment
  - **Resource types (\*required):** [RegistrationAttachment\*](#list_pinpoint-sms-voice-v2-resource-RegistrationAttachment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRegistrationFieldValue](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DeleteRegistrationFieldValue.html)  **
  - **Description:** Grants permission to delete an optional registration field value
  - **Resource types (\*required):** [Registration\*](#list_pinpoint-sms-voice-v2-resource-Registration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteResourcePolicy](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DeleteResourcePolicy.html)  **
  - **Description:** Grants permission to delete a resource policy
  - **Resource types (\*required):** [OptOutList](#list_pinpoint-sms-voice-v2-resource-OptOutList) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [PhoneNumber](#list_pinpoint-sms-voice-v2-resource-PhoneNumber) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Pool](#list_pinpoint-sms-voice-v2-resource-Pool) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [SenderId](#list_pinpoint-sms-voice-v2-resource-SenderId) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [DeleteTextMessageSpendLimitOverride](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DeleteTextMessageSpendLimitOverride.html)  **
  - **Description:** Grants permission to delete an override for your account's text messaging monthly spend limit
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteVerifiedDestinationNumber](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DeleteVerifiedDestinationNumber.html)  **
  - **Description:** Grants permission to delete a verified destination number
  - **Resource types (\*required):** [VerifiedDestinationNumber\*](#list_pinpoint-sms-voice-v2-resource-VerifiedDestinationNumber)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteVoiceMessageSpendLimitOverride](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DeleteVoiceMessageSpendLimitOverride.html)  **
  - **Description:** Grants permission to delete an override for your account's voice messaging monthly spend limit
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DescribeAccountAttributes](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DescribeAccountAttributes.html)  **
  - **Description:** Grants permission to describe the attributes of your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeAccountLimits](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DescribeAccountLimits.html)  **
  - **Description:** Grants permission to describe the service quotas for your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeConfigurationSets](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DescribeConfigurationSets.html)  **
  - **Description:** Grants permission to describe the configuration sets in your account
  - **Resource types (\*required):** [ConfigurationSet](#list_pinpoint-sms-voice-v2-resource-ConfigurationSet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeKeywords](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DescribeKeywords.html)  **
  - **Description:** Grants permission to describe the keywords for a pool or origination phone number
  - **Resource types (\*required):** [PhoneNumber](#list_pinpoint-sms-voice-v2-resource-PhoneNumber) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Pool](#list_pinpoint-sms-voice-v2-resource-Pool) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeNotifyConfigurations](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DescribeNotifyConfigurations.html)  **
  - **Description:** Grants permission to describe the notify configurations in your account
  - **Resource types (\*required):** [NotifyConfiguration](#list_pinpoint-sms-voice-v2-resource-NotifyConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeNotifyTemplates](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DescribeNotifyTemplates.html)  **
  - **Description:** Grants permission to describe the notify templates available
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeOptOutLists](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DescribeOptOutLists.html)  **
  - **Description:** Grants permission to describe the opt-out lists in your account
  - **Resource types (\*required):** [OptOutList](#list_pinpoint-sms-voice-v2-resource-OptOutList)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeOptedOutNumbers](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DescribeOptedOutNumbers.html)  **
  - **Description:** Grants permission to describe the destination phone numbers in an opt-out list
  - **Resource types (\*required):** [OptOutList\*](#list_pinpoint-sms-voice-v2-resource-OptOutList)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribePhoneNumbers](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DescribePhoneNumbers.html)  **
  - **Description:** Grants permission to describe the origination phone numbers in your account
  - **Resource types (\*required):** [PhoneNumber](#list_pinpoint-sms-voice-v2-resource-PhoneNumber)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribePools](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DescribePools.html)  **
  - **Description:** Grants permission to describe the pools in your account
  - **Resource types (\*required):** [Pool](#list_pinpoint-sms-voice-v2-resource-Pool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeProtectConfigurations](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DescribeProtectConfigurations.html)  **
  - **Description:** Grants permission to describe the protect configurations in your account
  - **Resource types (\*required):** [ProtectConfiguration](#list_pinpoint-sms-voice-v2-resource-ProtectConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeRcsAgentCountryLaunchStatus](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DescribeRcsAgentCountryLaunchStatus.html)  **
  - **Description:** Grants permission to describe the country launch status for an RCS agent
  - **Resource types (\*required):** [RcsAgent\*](#list_pinpoint-sms-voice-v2-resource-RcsAgent)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeRcsAgents](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DescribeRcsAgents.html)  **
  - **Description:** Grants permission to describe the RCS agents in your account
  - **Resource types (\*required):** [RcsAgent](#list_pinpoint-sms-voice-v2-resource-RcsAgent)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeRegistrationAttachments](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DescribeRegistrationAttachments.html)  **
  - **Description:** Grants permission to describe the registration attachments in your account
  - **Resource types (\*required):** [RegistrationAttachment](#list_pinpoint-sms-voice-v2-resource-RegistrationAttachment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeRegistrationFieldDefinitions](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DescribeRegistrationFieldDefinitions.html)  **
  - **Description:** Grants permission to describe the field definitions for a given registration type
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeRegistrationFieldValues](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DescribeRegistrationFieldValues.html)  **
  - **Description:** Grants permission to describe the field values for a given registration
  - **Resource types (\*required):** [Registration\*](#list_pinpoint-sms-voice-v2-resource-Registration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeRegistrationSectionDefinitions](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DescribeRegistrationSectionDefinitions.html)  **
  - **Description:** Grants permission to describe the section definitions for a given registration type
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeRegistrationTypeDefinitions](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DescribeRegistrationTypeDefinitions.html)  **
  - **Description:** Grants permission to describe the registration types supported by the service
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeRegistrationVersions](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DescribeRegistrationVersions.html)  **
  - **Description:** Grants permission to describe the versions for a given registration
  - **Resource types (\*required):** [Registration\*](#list_pinpoint-sms-voice-v2-resource-Registration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeRegistrations](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DescribeRegistrations.html)  **
  - **Description:** Grants permission to describe the registrations in your account
  - **Resource types (\*required):** [Registration](#list_pinpoint-sms-voice-v2-resource-Registration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeSenderIds](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DescribeSenderIds.html)  **
  - **Description:** Grants permission to describe the sender IDs in your account
  - **Resource types (\*required):** [SenderId](#list_pinpoint-sms-voice-v2-resource-SenderId)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeSpendLimits](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DescribeSpendLimits.html)  **
  - **Description:** Grants permission to describe the monthly spend limits for your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeVerifiedDestinationNumbers](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DescribeVerifiedDestinationNumbers.html)  **
  - **Description:** Grants permission to describe the verified destination numbers in your account
  - **Resource types (\*required):** [VerifiedDestinationNumber](#list_pinpoint-sms-voice-v2-resource-VerifiedDestinationNumber)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DisassociateOriginationIdentity](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DisassociateOriginationIdentity.html)  **
  - **Description:** Grants permission to disassociate an origination phone number or sender ID from a pool
  - **Resource types (\*required):** [PhoneNumber](#list_pinpoint-sms-voice-v2-resource-PhoneNumber) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Pool\*](#list_pinpoint-sms-voice-v2-resource-Pool) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [RcsAgent](#list_pinpoint-sms-voice-v2-resource-RcsAgent) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [SenderId](#list_pinpoint-sms-voice-v2-resource-SenderId) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateProtectConfiguration](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DisassociateProtectConfiguration.html)  **
  - **Description:** Grants permission to disassociate a protect configuration from a configuration set
  - **Resource types (\*required):** [ConfigurationSet\*](#list_pinpoint-sms-voice-v2-resource-ConfigurationSet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ProtectConfiguration\*](#list_pinpoint-sms-voice-v2-resource-ProtectConfiguration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DiscardRegistrationVersion](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DiscardRegistrationVersion.html)  **
  - **Description:** Grants permission to discard the latest version of a given registration
  - **Resource types (\*required):** [Registration\*](#list_pinpoint-sms-voice-v2-resource-Registration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetProtectConfigurationCountryRuleSet](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_GetProtectConfigurationCountryRuleSet.html)  **
  - **Description:** Grants permission to get the country rule set for a protect configuration
  - **Resource types (\*required):** [ProtectConfiguration\*](#list_pinpoint-sms-voice-v2-resource-ProtectConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetResourcePolicy](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_GetResourcePolicy.html)  **
  - **Description:** Grants permission to get a resource policy
  - **Resource types (\*required):** [OptOutList](#list_pinpoint-sms-voice-v2-resource-OptOutList) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [PhoneNumber](#list_pinpoint-sms-voice-v2-resource-PhoneNumber) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Pool](#list_pinpoint-sms-voice-v2-resource-Pool) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [SenderId](#list_pinpoint-sms-voice-v2-resource-SenderId) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListNotifyCountries](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_ListNotifyCountries.html)  **
  - **Description:** Grants permission to list countries that support notify messaging
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListPoolOriginationIdentities](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_ListPoolOriginationIdentities.html)  **
  - **Description:** Grants permission to list all origination phone numbers and sender IDs associated to a pool
  - **Resource types (\*required):** [Pool\*](#list_pinpoint-sms-voice-v2-resource-Pool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListProtectConfigurationRuleSetNumberOverrides](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_ListProtectConfigurationRuleSetNumberOverrides.html)  **
  - **Description:** Grants permission to list all phone number overrides for a protect configuration
  - **Resource types (\*required):** [ProtectConfiguration\*](#list_pinpoint-sms-voice-v2-resource-ProtectConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListRegistrationAssociations](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_ListRegistrationAssociations.html)  **
  - **Description:** Grants permission to list all resources associated to a registration
  - **Resource types (\*required):** [Registration\*](#list_pinpoint-sms-voice-v2-resource-Registration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListTagsForResource](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list the tags for a resource
  - **Resource types (\*required):** [ConfigurationSet](#list_pinpoint-sms-voice-v2-resource-ConfigurationSet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [NotifyConfiguration](#list_pinpoint-sms-voice-v2-resource-NotifyConfiguration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [OptOutList](#list_pinpoint-sms-voice-v2-resource-OptOutList) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [PhoneNumber](#list_pinpoint-sms-voice-v2-resource-PhoneNumber) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Pool](#list_pinpoint-sms-voice-v2-resource-Pool) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ProtectConfiguration](#list_pinpoint-sms-voice-v2-resource-ProtectConfiguration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [RcsAgent](#list_pinpoint-sms-voice-v2-resource-RcsAgent) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Registration](#list_pinpoint-sms-voice-v2-resource-Registration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [RegistrationAttachment](#list_pinpoint-sms-voice-v2-resource-RegistrationAttachment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [SenderId](#list_pinpoint-sms-voice-v2-resource-SenderId) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [VerifiedDestinationNumber](#list_pinpoint-sms-voice-v2-resource-VerifiedDestinationNumber) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PutKeyword](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_PutKeyword.html)  **
  - **Description:** Grants permission to create or update a keyword for a pool or origination phone number
  - **Resource types (\*required):** [PhoneNumber](#list_pinpoint-sms-voice-v2-resource-PhoneNumber) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Pool](#list_pinpoint-sms-voice-v2-resource-Pool) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutMessageFeedback](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_PutMessageFeedback.html)  **
  - **Description:** Grants permission to put feedback for a text, voice, or media message
  - **Resource types (\*required):** [Message\*](#list_pinpoint-sms-voice-v2-resource-Message)
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutOptedOutNumber](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_PutOptedOutNumber.html)  **
  - **Description:** Grants permission to put a destination phone number into an opt-out list
  - **Resource types (\*required):** [OptOutList\*](#list_pinpoint-sms-voice-v2-resource-OptOutList)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutProtectConfigurationRuleSetNumberOverride](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_PutProtectConfigurationRuleSetNumberOverride.html)  **
  - **Description:** Grants permission to put a phone number override for a protect configuration
  - **Resource types (\*required):** [ProtectConfiguration\*](#list_pinpoint-sms-voice-v2-resource-ProtectConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutRegistrationFieldValue](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_PutRegistrationFieldValue.html)  **
  - **Description:** Grants permission to put a registration field value
  - **Resource types (\*required):** [Registration\*](#list_pinpoint-sms-voice-v2-resource-Registration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutResourcePolicy](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_PutResourcePolicy.html)  **
  - **Description:** Grants permission to put a resource policy
  - **Resource types (\*required):** [OptOutList](#list_pinpoint-sms-voice-v2-resource-OptOutList) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [PhoneNumber](#list_pinpoint-sms-voice-v2-resource-PhoneNumber) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Pool](#list_pinpoint-sms-voice-v2-resource-Pool) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [SenderId](#list_pinpoint-sms-voice-v2-resource-SenderId) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [ReleasePhoneNumber](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_ReleasePhoneNumber.html)  **
  - **Description:** Grants permission to release an origination phone number
  - **Resource types (\*required):** [PhoneNumber\*](#list_pinpoint-sms-voice-v2-resource-PhoneNumber)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ReleaseSenderId](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_ReleaseSenderId.html)  **
  - **Description:** Grants permission to release a sender ID
  - **Resource types (\*required):** [SenderId\*](#list_pinpoint-sms-voice-v2-resource-SenderId)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RequestPhoneNumber](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_RequestPhoneNumber.html)  **
  - **Description:** Grants permission to request an origination phone number
  - **Resource types (\*required):** [OptOutList](#list_pinpoint-sms-voice-v2-resource-OptOutList) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-sms-voice-v2-aws_TagKeys)
  - **Resource types (\*required):** [Pool](#list_pinpoint-sms-voice-v2-resource-Pool) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-sms-voice-v2-aws_TagKeys)
  - **Resource types (\*required):** [Registration](#list_pinpoint-sms-voice-v2-resource-Registration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-sms-voice-v2-aws_TagKeys)
  - **Access level:** Write

- **   [RequestSenderId](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_RequestSenderId.html)  **
  - **Description:** Grants permission to request an unregistered sender ID
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-sms-voice-v2-aws_TagKeys)
  - **Access level:** Write

- **   [SendDestinationNumberVerificationCode](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_SendDestinationNumberVerificationCode.html)  **
  - **Description:** Grants permission to send a text or voice message containing a verification code to a destination phone number
  - **Resource types (\*required):** [ConfigurationSet](#list_pinpoint-sms-voice-v2-resource-ConfigurationSet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [PhoneNumber](#list_pinpoint-sms-voice-v2-resource-PhoneNumber) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Pool](#list_pinpoint-sms-voice-v2-resource-Pool) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [SenderId](#list_pinpoint-sms-voice-v2-resource-SenderId) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SendMediaMessage](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_SendMediaMessage.html)  **
  - **Description:** Grants permission to send a media message to a destination phone number
  - **Resource types (\*required):** [ConfigurationSet](#list_pinpoint-sms-voice-v2-resource-ConfigurationSet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [PhoneNumber](#list_pinpoint-sms-voice-v2-resource-PhoneNumber) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Pool](#list_pinpoint-sms-voice-v2-resource-Pool) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ProtectConfiguration](#list_pinpoint-sms-voice-v2-resource-ProtectConfiguration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SendNotifyTextMessage](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_SendNotifyTextMessage.html)  **
  - **Description:** Grants permission to send a notify text message to a destination phone number
  - **Resource types (\*required):** [ConfigurationSet](#list_pinpoint-sms-voice-v2-resource-ConfigurationSet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [NotifyConfiguration\*](#list_pinpoint-sms-voice-v2-resource-NotifyConfiguration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SendNotifyVoiceMessage](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_SendNotifyVoiceMessage.html)  **
  - **Description:** Grants permission to send a notify voice message to a destination phone number
  - **Resource types (\*required):** [ConfigurationSet](#list_pinpoint-sms-voice-v2-resource-ConfigurationSet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [NotifyConfiguration\*](#list_pinpoint-sms-voice-v2-resource-NotifyConfiguration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SendRcsMessage](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_SendRcsMessage.html)  **
  - **Description:** Grants permission to send an RCS message to a destination phone number
  - **Resource types (\*required):** [ConfigurationSet](#list_pinpoint-sms-voice-v2-resource-ConfigurationSet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [PhoneNumber](#list_pinpoint-sms-voice-v2-resource-PhoneNumber) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Pool](#list_pinpoint-sms-voice-v2-resource-Pool) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ProtectConfiguration](#list_pinpoint-sms-voice-v2-resource-ProtectConfiguration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [RcsAgent](#list_pinpoint-sms-voice-v2-resource-RcsAgent) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [SenderId](#list_pinpoint-sms-voice-v2-resource-SenderId) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SendTextMessage](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_SendTextMessage.html)  **
  - **Description:** Grants permission to send a text message to a destination phone number
  - **Resource types (\*required):** [ConfigurationSet](#list_pinpoint-sms-voice-v2-resource-ConfigurationSet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [PhoneNumber](#list_pinpoint-sms-voice-v2-resource-PhoneNumber) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Pool](#list_pinpoint-sms-voice-v2-resource-Pool) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ProtectConfiguration](#list_pinpoint-sms-voice-v2-resource-ProtectConfiguration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [SenderId](#list_pinpoint-sms-voice-v2-resource-SenderId) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SendVoiceMessage](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_SendVoiceMessage.html)  **
  - **Description:** Grants permission to send a voice message to a destination phone number
  - **Resource types (\*required):** [ConfigurationSet](#list_pinpoint-sms-voice-v2-resource-ConfigurationSet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [PhoneNumber](#list_pinpoint-sms-voice-v2-resource-PhoneNumber) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Pool](#list_pinpoint-sms-voice-v2-resource-Pool) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SetAccountDefaultProtectConfiguration](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_SetAccountDefaultProtectConfiguration.html)  **
  - **Description:** Grants permission to set a default protect configuration for the account
  - **Resource types (\*required):** [ProtectConfiguration\*](#list_pinpoint-sms-voice-v2-resource-ProtectConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SetDefaultMessageFeedbackEnabled](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_SetDefaultMessageFeedbackEnabled.html)  **
  - **Description:** Grants permission to set the default message feedback for a configuration set
  - **Resource types (\*required):** [ConfigurationSet\*](#list_pinpoint-sms-voice-v2-resource-ConfigurationSet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SetDefaultMessageType](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_SetDefaultMessageType.html)  **
  - **Description:** Grants permission to set the default message type for a configuration set
  - **Resource types (\*required):** [ConfigurationSet\*](#list_pinpoint-sms-voice-v2-resource-ConfigurationSet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SetDefaultSenderId](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_SetDefaultSenderId.html)  **
  - **Description:** Grants permission to set the default sender ID for a configuration set
  - **Resource types (\*required):** [ConfigurationSet\*](#list_pinpoint-sms-voice-v2-resource-ConfigurationSet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SetMediaMessageSpendLimitOverride](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_SetMediaMessageSpendLimitOverride.html)  **
  - **Description:** Grants permission to set an override for your account's media messaging monthly spend limit
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [SetNotifyMessageSpendLimitOverride](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_SetNotifyMessageSpendLimitOverride.html)  **
  - **Description:** Grants permission to set an override for your account's notify messaging monthly spend limit
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [SetRcsMessageSpendLimitOverride](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_SetRcsMessageSpendLimitOverride.html)  **
  - **Description:** Grants permission to set an override for your account's RCS messaging monthly spend limit
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [SetTextMessageSpendLimitOverride](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_SetTextMessageSpendLimitOverride.html)  **
  - **Description:** Grants permission to set an override for your account's text messaging monthly spend limit
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [SetVoiceMessageSpendLimitOverride](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_SetVoiceMessageSpendLimitOverride.html)  **
  - **Description:** Grants permission to set an override for your account's voice messaging monthly spend limit
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [SubmitRegistrationVersion](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_SubmitRegistrationVersion.html)  **
  - **Description:** Grants permission to submit the latest version of a given registration
  - **Resource types (\*required):** [Registration\*](#list_pinpoint-sms-voice-v2-resource-Registration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_TagResource.html)  **
  - **Description:** Grants permission to add tags to a resource
  - **Resource types (\*required):** [ConfigurationSet](#list_pinpoint-sms-voice-v2-resource-ConfigurationSet) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-sms-voice-v2-aws_TagKeys)
  - **Resource types (\*required):** [NotifyConfiguration](#list_pinpoint-sms-voice-v2-resource-NotifyConfiguration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-sms-voice-v2-aws_TagKeys)
  - **Resource types (\*required):** [OptOutList](#list_pinpoint-sms-voice-v2-resource-OptOutList) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-sms-voice-v2-aws_TagKeys)
  - **Resource types (\*required):** [PhoneNumber](#list_pinpoint-sms-voice-v2-resource-PhoneNumber) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-sms-voice-v2-aws_TagKeys)
  - **Resource types (\*required):** [Pool](#list_pinpoint-sms-voice-v2-resource-Pool) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-sms-voice-v2-aws_TagKeys)
  - **Resource types (\*required):** [ProtectConfiguration](#list_pinpoint-sms-voice-v2-resource-ProtectConfiguration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-sms-voice-v2-aws_TagKeys)
  - **Resource types (\*required):** [RcsAgent](#list_pinpoint-sms-voice-v2-resource-RcsAgent) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-sms-voice-v2-aws_TagKeys)
  - **Resource types (\*required):** [Registration](#list_pinpoint-sms-voice-v2-resource-Registration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-sms-voice-v2-aws_TagKeys)
  - **Resource types (\*required):** [RegistrationAttachment](#list_pinpoint-sms-voice-v2-resource-RegistrationAttachment) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-sms-voice-v2-aws_TagKeys)
  - **Resource types (\*required):** [SenderId](#list_pinpoint-sms-voice-v2-resource-SenderId) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-sms-voice-v2-aws_TagKeys)
  - **Resource types (\*required):** [VerifiedDestinationNumber](#list_pinpoint-sms-voice-v2-resource-VerifiedDestinationNumber) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-sms-voice-v2-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from a resource
  - **Resource types (\*required):** [ConfigurationSet](#list_pinpoint-sms-voice-v2-resource-ConfigurationSet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-sms-voice-v2-aws_TagKeys)
  - **Resource types (\*required):** [NotifyConfiguration](#list_pinpoint-sms-voice-v2-resource-NotifyConfiguration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-sms-voice-v2-aws_TagKeys)
  - **Resource types (\*required):** [OptOutList](#list_pinpoint-sms-voice-v2-resource-OptOutList) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-sms-voice-v2-aws_TagKeys)
  - **Resource types (\*required):** [PhoneNumber](#list_pinpoint-sms-voice-v2-resource-PhoneNumber) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-sms-voice-v2-aws_TagKeys)
  - **Resource types (\*required):** [Pool](#list_pinpoint-sms-voice-v2-resource-Pool) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-sms-voice-v2-aws_TagKeys)
  - **Resource types (\*required):** [ProtectConfiguration](#list_pinpoint-sms-voice-v2-resource-ProtectConfiguration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-sms-voice-v2-aws_TagKeys)
  - **Resource types (\*required):** [RcsAgent](#list_pinpoint-sms-voice-v2-resource-RcsAgent) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-sms-voice-v2-aws_TagKeys)
  - **Resource types (\*required):** [Registration](#list_pinpoint-sms-voice-v2-resource-Registration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-sms-voice-v2-aws_TagKeys)
  - **Resource types (\*required):** [RegistrationAttachment](#list_pinpoint-sms-voice-v2-resource-RegistrationAttachment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-sms-voice-v2-aws_TagKeys)
  - **Resource types (\*required):** [SenderId](#list_pinpoint-sms-voice-v2-resource-SenderId) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-sms-voice-v2-aws_TagKeys)
  - **Resource types (\*required):** [VerifiedDestinationNumber](#list_pinpoint-sms-voice-v2-resource-VerifiedDestinationNumber) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-sms-voice-v2-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateEventDestination](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_UpdateEventDestination.html)  **
  - **Description:** Grants permission to update an event destination within a configuration set
  - **Resource types (\*required):** [ConfigurationSet\*](#list_pinpoint-sms-voice-v2-resource-ConfigurationSet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateNotifyConfiguration](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_UpdateNotifyConfiguration.html)  **
  - **Description:** Grants permission to update a notify configuration
  - **Resource types (\*required):** [NotifyConfiguration\*](#list_pinpoint-sms-voice-v2-resource-NotifyConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdatePhoneNumber](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_UpdatePhoneNumber.html)  **
  - **Description:** Grants permission to update an origination phone number's configuration
  - **Resource types (\*required):** [OptOutList](#list_pinpoint-sms-voice-v2-resource-OptOutList) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [PhoneNumber\*](#list_pinpoint-sms-voice-v2-resource-PhoneNumber) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdatePool](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_UpdatePool.html)  **
  - **Description:** Grants permission to update a pool's configuration
  - **Resource types (\*required):** [OptOutList](#list_pinpoint-sms-voice-v2-resource-OptOutList) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Pool\*](#list_pinpoint-sms-voice-v2-resource-Pool) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateProtectConfiguration](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_UpdateProtectConfiguration.html)  **
  - **Description:** Grants permission to update a protect configuration
  - **Resource types (\*required):** [ProtectConfiguration\*](#list_pinpoint-sms-voice-v2-resource-ProtectConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateProtectConfigurationCountryRuleSet](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_UpdateProtectConfigurationCountryRuleSet.html)  **
  - **Description:** Grants permission to update a country rule set for a protect configuration
  - **Resource types (\*required):** [ProtectConfiguration\*](#list_pinpoint-sms-voice-v2-resource-ProtectConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateRcsAgent](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_UpdateRcsAgent.html)  **
  - **Description:** Grants permission to update an RCS agent's configuration
  - **Resource types (\*required):** [RcsAgent\*](#list_pinpoint-sms-voice-v2-resource-RcsAgent)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSenderId](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_UpdateSenderId.html)  **
  - **Description:** Grants permission to update a sender ID's configuration
  - **Resource types (\*required):** [SenderId\*](#list_pinpoint-sms-voice-v2-resource-SenderId)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [VerifyDestinationNumber](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_VerifyDestinationNumber.html)  **
  - **Description:** Grants permission to verify a destination phone number
  - **Resource types (\*required):** [VerifiedDestinationNumber\*](#list_pinpoint-sms-voice-v2-resource-VerifiedDestinationNumber)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS End User Messaging SMS and Voice V2
<a name="list_pinpoint-sms-voice-v2-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [ConfigurationSet](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_CreateConfigurationSet.html)  | arn:${Partition}:sms-voice:${Region}:${Account}:configuration-set/${ConfigurationSetName} | [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_) | 
|  [Message](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_PutMessageFeedback.html)  | arn:${Partition}:sms-voice:${Region}:${Account}:message/${MessageId} |   | 
|  [NotifyConfiguration](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_CreateNotifyConfiguration.html)  | arn:${Partition}:sms-voice:${Region}:${Account}:notify-configuration/${NotifyConfigurationId} | [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_) | 
|  [OptOutList](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_CreateOptOutList.html)  | arn:${Partition}:sms-voice:${Region}:${Account}:opt-out-list/${OptOutListName} | [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_) | 
|  [PhoneNumber](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_RequestPhoneNumber.html)  | arn:${Partition}:sms-voice:${Region}:${Account}:phone-number/${PhoneNumberId} | [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_) | 
|  [Pool](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_CreatePool.html)  | arn:${Partition}:sms-voice:${Region}:${Account}:pool/${PoolId} | [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_) | 
|  [ProtectConfiguration](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_CreateProtectConfiguration.html)  | arn:${Partition}:sms-voice:${Region}:${Account}:protect-configuration/${ProtectConfigurationId} | [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_) | 
|  [RcsAgent](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_CreateRcsAgent.html)  | arn:${Partition}:sms-voice:${Region}:${Account}:rcs-agent/${RcsAgentId} | [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_) | 
|  [Registration](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DescribeRegistrations.html)  | arn:${Partition}:sms-voice:${Region}:${Account}:registration/${RegistrationId} | [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_) | 
|  [RegistrationAttachment](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DescribeRegistrationAttachments.html)  | arn:${Partition}:sms-voice:${Region}:${Account}:registration-attachment/${RegistrationAttachmentId} | [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_) | 
|  [SenderId](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DescribeSenderIds.html)  | arn:${Partition}:sms-voice:${Region}:${Account}:sender-id/${SenderId}/${IsoCountryCode} | [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_) | 
|  [VerifiedDestinationNumber](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DescribeVerifiedDestinationNumbers.html)  | arn:${Partition}:sms-voice:${Region}:${Account}:verified-destination-number/${VerifiedDestinationNumberId} | [aws:ResourceTag/${TagKey}](#list_pinpoint-sms-voice-v2-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS End User Messaging SMS and Voice V2
<a name="list_pinpoint-sms-voice-v2-policy-keys"></a>

AWS End User Messaging SMS and Voice V2 defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 