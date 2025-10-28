**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Supported Amazon Pinpoint email API actions in CloudTrail log files

The Amazon Pinpoint Email API supports logging the following actions as events in CloudTrail log
files:

- [CreateConfigurationSet](../../../pinpoint-email/latest/APIReference/API_CreateConfigurationSet.md "../../../pinpoint-email/latest/APIReference/API_CreateConfigurationSet.md")
- [CreateConfigurationSetEventDestination](../../../pinpoint-email/latest/APIReference/API_CreateConfigurationSetEventDestination.md "../../../pinpoint-email/latest/APIReference/API_CreateConfigurationSetEventDestination.md")
- [CreateDedicatedIpPool](../../../pinpoint-email/latest/APIReference/API_CreateDedicatedIpPool.md "../../../pinpoint-email/latest/APIReference/API_CreateDedicatedIpPool.md")
- [CreateEmailIdentity](../../../pinpoint-email/latest/APIReference/API_CreateEmailIdentity.md "../../../pinpoint-email/latest/APIReference/API_CreateEmailIdentity.md")
- [DeleteConfigurationSet](../../../pinpoint-email/latest/APIReference/API_DeleteConfigurationSet.md "../../../pinpoint-email/latest/APIReference/API_DeleteConfigurationSet.md")
- [DeleteConfigurationSetEventDestination](../../../pinpoint-email/latest/APIReference/API_DeleteConfigurationSetEventDestination.md "../../../pinpoint-email/latest/APIReference/API_DeleteConfigurationSetEventDestination.md")
- [DeleteDedicatedIpPool](../../../pinpoint-email/latest/APIReference/API_DeleteDedicatedIpPool.md "../../../pinpoint-email/latest/APIReference/API_DeleteDedicatedIpPool.md")
- [DeleteEmailIdentity](../../../pinpoint-email/latest/APIReference/API_DeleteEmailIdentity.md "../../../pinpoint-email/latest/APIReference/API_DeleteEmailIdentity.md")
- [GetAccount](../../../pinpoint-email/latest/APIReference/API_GetAccount.md "../../../pinpoint-email/latest/APIReference/API_GetAccount.md")
- [GetConfigurationSet](../../../pinpoint-email/latest/APIReference/API_GetConfigurationSet.md "../../../pinpoint-email/latest/APIReference/API_GetConfigurationSet.md")
- [GetConfigurationSetEventDestinations](../../../pinpoint-email/latest/APIReference/API_GetConfigurationSetEventDestinations.md "../../../pinpoint-email/latest/APIReference/API_GetConfigurationSetEventDestinations.md")
- [GetDedicatedIp](../../../pinpoint-email/latest/APIReference/API_GetDedicatedIp.md "../../../pinpoint-email/latest/APIReference/API_GetDedicatedIp.md")
- [GetDedicatedIps](../../../pinpoint-email/latest/APIReference/API_GetDedicatedIps.md "../../../pinpoint-email/latest/APIReference/API_GetDedicatedIps.md")
- [GetEmailIdentity](../../../pinpoint-email/latest/APIReference/API_GetEmailIdentity.md "../../../pinpoint-email/latest/APIReference/API_GetEmailIdentity.md")
- [ListConfigurationSets](../../../pinpoint-email/latest/APIReference/API_ListConfigurationSets.md "../../../pinpoint-email/latest/APIReference/API_ListConfigurationSets.md")
- [ListDedicatedIpPools](../../../pinpoint-email/latest/APIReference/API_ListDedicatedIpPools.md "../../../pinpoint-email/latest/APIReference/API_ListDedicatedIpPools.md")
- [ListEmailIdentities](../../../pinpoint-email/latest/APIReference/API_ListEmailIdentities.md "../../../pinpoint-email/latest/APIReference/API_ListEmailIdentities.md")
- [PutAccountDedicatedIpWarmupAttributes](../../../pinpoint-email/latest/APIReference/API_PutAccountDedicatedIpWarmupAttributes.md "../../../pinpoint-email/latest/APIReference/API_PutAccountDedicatedIpWarmupAttributes.md")
- [PutAccountSendingAttributes](../../../pinpoint-email/latest/APIReference/API_PutAccountSendingAttributes.md "../../../pinpoint-email/latest/APIReference/API_PutAccountSendingAttributes.md")
- [PutConfigurationSetDeliveryOptions](../../../pinpoint-email/latest/APIReference/API_PutConfigurationSetDeliveryOptions.md "../../../pinpoint-email/latest/APIReference/API_PutConfigurationSetDeliveryOptions.md")
- [PutConfigurationSetReputationOptions](../../../pinpoint-email/latest/APIReference/API_PutConfigurationSetReputationOptions.md "../../../pinpoint-email/latest/APIReference/API_PutConfigurationSetReputationOptions.md")
- [PutConfigurationSetSendingOptions](../../../pinpoint-email/latest/APIReference/API_PutConfigurationSetSendingOptions.md "../../../pinpoint-email/latest/APIReference/API_PutConfigurationSetSendingOptions.md")
- [PutConfigurationSetTrackingOptions](../../../pinpoint-email/latest/APIReference/API_PutConfigurationSetTrackingOptions.md "../../../pinpoint-email/latest/APIReference/API_PutConfigurationSetTrackingOptions.md")
- [PutDedicatedIpInPool](../../../pinpoint-email/latest/APIReference/API_PutDedicatedIpInPool.md "../../../pinpoint-email/latest/APIReference/API_PutDedicatedIpInPool.md")
- [PutDedicatedIpWarmupAttributes](../../../pinpoint-email/latest/APIReference/API_PutDedicatedIpWarmupAttributes.md "../../../pinpoint-email/latest/APIReference/API_PutDedicatedIpWarmupAttributes.md")
- [PutEmailIdentityDkimAttributes](../../../pinpoint-email/latest/APIReference/API_PutEmailIdentityDkimAttributes.md "../../../pinpoint-email/latest/APIReference/API_PutEmailIdentityDkimAttributes.md")
- [PutEmailIdentityFeedbackAttributes](../../../pinpoint-email/latest/APIReference/API_PutEmailIdentityFeedbackAttributes.md "../../../pinpoint-email/latest/APIReference/API_PutEmailIdentityFeedbackAttributes.md")
- [PutEmailIdentityMailFromAttributes](../../../pinpoint-email/latest/APIReference/API_PutEmailIdentityMailFromAttributes.md "../../../pinpoint-email/latest/APIReference/API_PutEmailIdentityMailFromAttributes.md")
- [UpdateConfigurationSetEventDestination](../../../pinpoint-email/latest/APIReference/API_UpdateConfigurationSetEventDestination.md "../../../pinpoint-email/latest/APIReference/API_UpdateConfigurationSetEventDestination.md")
  The following Amazon Pinpoint Email API action **isn't** logged in
  CloudTrail:

- SendEmail
