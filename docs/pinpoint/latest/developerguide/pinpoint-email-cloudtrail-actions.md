

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Supported Amazon Pinpoint email API actions in CloudTrail log files
<a name="pinpoint-email-cloudtrail-actions"></a>

The Amazon Pinpoint Email API supports logging the following actions as events in CloudTrail log files:
+ [CreateConfigurationSet](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_CreateConfigurationSet.html)
+ [CreateConfigurationSetEventDestination](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_CreateConfigurationSetEventDestination.html)
+ [CreateDedicatedIpPool](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_CreateDedicatedIpPool.html)
+ [CreateEmailIdentity](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_CreateEmailIdentity.html)
+ [DeleteConfigurationSet](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_DeleteConfigurationSet.html)
+ [DeleteConfigurationSetEventDestination](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_DeleteConfigurationSetEventDestination.html)
+ [DeleteDedicatedIpPool](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_DeleteDedicatedIpPool.html)
+ [DeleteEmailIdentity](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_DeleteEmailIdentity.html)
+ [GetAccount](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_GetAccount.html)
+ [GetConfigurationSet](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_GetConfigurationSet.html)
+ [GetConfigurationSetEventDestinations](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_GetConfigurationSetEventDestinations.html)
+ [GetDedicatedIp](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_GetDedicatedIp.html)
+ [GetDedicatedIps](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_GetDedicatedIps.html)
+ [GetEmailIdentity](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_GetEmailIdentity.html)
+ [ListConfigurationSets](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_ListConfigurationSets.html)
+ [ListDedicatedIpPools](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_ListDedicatedIpPools.html)
+ [ListEmailIdentities](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_ListEmailIdentities.html)
+ [PutAccountDedicatedIpWarmupAttributes](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_PutAccountDedicatedIpWarmupAttributes.html)
+ [PutAccountSendingAttributes](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_PutAccountSendingAttributes.html)
+ [PutConfigurationSetDeliveryOptions](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_PutConfigurationSetDeliveryOptions.html)
+ [PutConfigurationSetReputationOptions](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_PutConfigurationSetReputationOptions.html)
+ [PutConfigurationSetSendingOptions](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_PutConfigurationSetSendingOptions.html)
+ [PutConfigurationSetTrackingOptions](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_PutConfigurationSetTrackingOptions.html)
+ [PutDedicatedIpInPool](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_PutDedicatedIpInPool.html)
+ [PutDedicatedIpWarmupAttributes](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_PutDedicatedIpWarmupAttributes.html)
+ [PutEmailIdentityDkimAttributes](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_PutEmailIdentityDkimAttributes.html)
+ [PutEmailIdentityFeedbackAttributes](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_PutEmailIdentityFeedbackAttributes.html)
+ [PutEmailIdentityMailFromAttributes](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_PutEmailIdentityMailFromAttributes.html)
+ [UpdateConfigurationSetEventDestination](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_UpdateConfigurationSetEventDestination.html)

The following Amazon Pinpoint Email API action **isn't** logged in CloudTrail:
+ SendEmail