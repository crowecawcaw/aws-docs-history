

# Actions, resources, and condition keys for Amazon Pinpoint
<a name="list_pinpoint"></a>

Amazon Pinpoint (service prefix: `mobiletargeting`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/pinpoint/latest/developerguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/pinpoint/latest/apireference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/pinpoint/latest/developerguide/permissions-actions.html#permissions-actions-apiactions) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/mobiletargeting/mobiletargeting.json) for this service.

**Topics**
+ [API operations defined by Amazon Pinpoint](#list_pinpoint-operations)
+ [Actions defined by Amazon Pinpoint](#list_pinpoint-actions-as-permissions)
+ [Permission-only actions for Amazon Pinpoint](#list_pinpoint-permission-only-actions)
+ [Resource types defined by Amazon Pinpoint](#list_pinpoint-resources-for-iam-policies)
+ [Condition keys for Amazon Pinpoint](#list_pinpoint-policy-keys)

## API operations defined by Amazon Pinpoint
<a name="list_pinpoint-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_pinpoint-actions-as-permissions).




- **   CreateApp  **
  - **IAM action:**  [mobiletargeting:CreateApp](#list_pinpoint-action-CreateApp)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mobiletargeting:TagResource](#list_pinpoint-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateCampaign  **
  - **IAM action:**  [mobiletargeting:CreateCampaign](#list_pinpoint-action-CreateCampaign)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mobiletargeting:TagResource](#list_pinpoint-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateEmailTemplate  **
  - **IAM action:**  [mobiletargeting:CreateEmailTemplate](#list_pinpoint-action-CreateEmailTemplate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mobiletargeting:TagResource](#list_pinpoint-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateExportJob  **
  - **IAM action:**  [mobiletargeting:CreateExportJob](#list_pinpoint-action-CreateExportJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** mobiletargeting.amazonaws.com / **Access level:** Write

- **   CreateImportJob  **
  - **IAM action:**  [mobiletargeting:CreateImportJob](#list_pinpoint-action-CreateImportJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** mobiletargeting.amazonaws.com / **Access level:** Write

- **   CreateInAppTemplate  **
  - **IAM action:**  [mobiletargeting:CreateInAppTemplate](#list_pinpoint-action-CreateInAppTemplate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mobiletargeting:TagResource](#list_pinpoint-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateJourney  **
  - **IAM action:**  [mobiletargeting:CreateJourney](#list_pinpoint-action-CreateJourney)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mobiletargeting:TagResource](#list_pinpoint-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** mobiletargeting.amazonaws.com / **Access level:** Write

- **   CreatePushTemplate  **
  - **IAM action:**  [mobiletargeting:CreatePushTemplate](#list_pinpoint-action-CreatePushTemplate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mobiletargeting:TagResource](#list_pinpoint-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateRecommenderConfiguration  **
  - **IAM action:**  [mobiletargeting:CreateRecommenderConfiguration](#list_pinpoint-action-CreateRecommenderConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** mobiletargeting.amazonaws.com / **Access level:** Write

- **   CreateSegment  **
  - **IAM action:**  [mobiletargeting:CreateSegment](#list_pinpoint-action-CreateSegment)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mobiletargeting:TagResource](#list_pinpoint-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateSmsTemplate  **
  - **IAM action:**  [mobiletargeting:CreateSmsTemplate](#list_pinpoint-action-CreateSmsTemplate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mobiletargeting:TagResource](#list_pinpoint-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateVoiceTemplate  **
  - **IAM action:**  [mobiletargeting:CreateVoiceTemplate](#list_pinpoint-action-CreateVoiceTemplate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mobiletargeting:TagResource](#list_pinpoint-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteAdmChannel  **
  - **IAM action:**  [mobiletargeting:DeleteAdmChannel](#list_pinpoint-action-DeleteAdmChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteApnsChannel  **
  - **IAM action:**  [mobiletargeting:DeleteApnsChannel](#list_pinpoint-action-DeleteApnsChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteApnsSandboxChannel  **
  - **IAM action:**  [mobiletargeting:DeleteApnsSandboxChannel](#list_pinpoint-action-DeleteApnsSandboxChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteApnsVoipChannel  **
  - **IAM action:**  [mobiletargeting:DeleteApnsVoipChannel](#list_pinpoint-action-DeleteApnsVoipChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteApnsVoipSandboxChannel  **
  - **IAM action:**  [mobiletargeting:DeleteApnsVoipSandboxChannel](#list_pinpoint-action-DeleteApnsVoipSandboxChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteApp  **
  - **IAM action:**  [mobiletargeting:DeleteApp](#list_pinpoint-action-DeleteApp) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteBaiduChannel  **
  - **IAM action:**  [mobiletargeting:DeleteBaiduChannel](#list_pinpoint-action-DeleteBaiduChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCampaign  **
  - **IAM action:**  [mobiletargeting:DeleteCampaign](#list_pinpoint-action-DeleteCampaign) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEmailChannel  **
  - **IAM action:**  [mobiletargeting:DeleteEmailChannel](#list_pinpoint-action-DeleteEmailChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEmailTemplate  **
  - **IAM action:**  [mobiletargeting:DeleteEmailTemplate](#list_pinpoint-action-DeleteEmailTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEndpoint  **
  - **IAM action:**  [mobiletargeting:DeleteEndpoint](#list_pinpoint-action-DeleteEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEventStream  **
  - **IAM action:**  [mobiletargeting:DeleteEventStream](#list_pinpoint-action-DeleteEventStream) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteGcmChannel  **
  - **IAM action:**  [mobiletargeting:DeleteGcmChannel](#list_pinpoint-action-DeleteGcmChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteInAppTemplate  **
  - **IAM action:**  [mobiletargeting:DeleteInAppTemplate](#list_pinpoint-action-DeleteInAppTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteJourney  **
  - **IAM action:**  [mobiletargeting:DeleteJourney](#list_pinpoint-action-DeleteJourney) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePushTemplate  **
  - **IAM action:**  [mobiletargeting:DeletePushTemplate](#list_pinpoint-action-DeletePushTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRecommenderConfiguration  **
  - **IAM action:**  [mobiletargeting:DeleteRecommenderConfiguration](#list_pinpoint-action-DeleteRecommenderConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSegment  **
  - **IAM action:**  [mobiletargeting:DeleteSegment](#list_pinpoint-action-DeleteSegment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSmsChannel  **
  - **IAM action:**  [mobiletargeting:DeleteSmsChannel](#list_pinpoint-action-DeleteSmsChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSmsTemplate  **
  - **IAM action:**  [mobiletargeting:DeleteSmsTemplate](#list_pinpoint-action-DeleteSmsTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteUserEndpoints  **
  - **IAM action:**  [mobiletargeting:DeleteUserEndpoints](#list_pinpoint-action-DeleteUserEndpoints) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteVoiceChannel  **
  - **IAM action:**  [mobiletargeting:DeleteVoiceChannel](#list_pinpoint-action-DeleteVoiceChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteVoiceTemplate  **
  - **IAM action:**  [mobiletargeting:DeleteVoiceTemplate](#list_pinpoint-action-DeleteVoiceTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAdmChannel  **
  - **IAM action:**  [mobiletargeting:GetAdmChannel](#list_pinpoint-action-GetAdmChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetApnsChannel  **
  - **IAM action:**  [mobiletargeting:GetApnsChannel](#list_pinpoint-action-GetApnsChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetApnsSandboxChannel  **
  - **IAM action:**  [mobiletargeting:GetApnsSandboxChannel](#list_pinpoint-action-GetApnsSandboxChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetApnsVoipChannel  **
  - **IAM action:**  [mobiletargeting:GetApnsVoipChannel](#list_pinpoint-action-GetApnsVoipChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetApnsVoipSandboxChannel  **
  - **IAM action:**  [mobiletargeting:GetApnsVoipSandboxChannel](#list_pinpoint-action-GetApnsVoipSandboxChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetApp  **
  - **IAM action:**  [mobiletargeting:GetApp](#list_pinpoint-action-GetApp) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetApplicationDateRangeKpi  **
  - **IAM action:**  [mobiletargeting:GetApplicationDateRangeKpi](#list_pinpoint-action-GetApplicationDateRangeKpi) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetApplicationSettings  **
  - **IAM action:**  [mobiletargeting:GetApplicationSettings](#list_pinpoint-action-GetApplicationSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetApps  **
  - **IAM action:**  [mobiletargeting:GetApps](#list_pinpoint-action-GetApps) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBaiduChannel  **
  - **IAM action:**  [mobiletargeting:GetBaiduChannel](#list_pinpoint-action-GetBaiduChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCampaign  **
  - **IAM action:**  [mobiletargeting:GetCampaign](#list_pinpoint-action-GetCampaign) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCampaignActivities  **
  - **IAM action:**  [mobiletargeting:GetCampaignActivities](#list_pinpoint-action-GetCampaignActivities) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetCampaignDateRangeKpi  **
  - **IAM action:**  [mobiletargeting:GetCampaignDateRangeKpi](#list_pinpoint-action-GetCampaignDateRangeKpi) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCampaignVersion  **
  - **IAM action:**  [mobiletargeting:GetCampaignVersion](#list_pinpoint-action-GetCampaignVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCampaignVersions  **
  - **IAM action:**  [mobiletargeting:GetCampaignVersions](#list_pinpoint-action-GetCampaignVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetCampaigns  **
  - **IAM action:**  [mobiletargeting:GetCampaigns](#list_pinpoint-action-GetCampaigns) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetChannels  **
  - **IAM action:**  [mobiletargeting:GetChannels](#list_pinpoint-action-GetChannels) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetEmailChannel  **
  - **IAM action:**  [mobiletargeting:GetEmailChannel](#list_pinpoint-action-GetEmailChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEmailTemplate  **
  - **IAM action:**  [mobiletargeting:GetEmailTemplate](#list_pinpoint-action-GetEmailTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEndpoint  **
  - **IAM action:**  [mobiletargeting:GetEndpoint](#list_pinpoint-action-GetEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEventStream  **
  - **IAM action:**  [mobiletargeting:GetEventStream](#list_pinpoint-action-GetEventStream) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetExportJob  **
  - **IAM action:**  [mobiletargeting:GetExportJob](#list_pinpoint-action-GetExportJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetExportJobs  **
  - **IAM action:**  [mobiletargeting:GetExportJobs](#list_pinpoint-action-GetExportJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetGcmChannel  **
  - **IAM action:**  [mobiletargeting:GetGcmChannel](#list_pinpoint-action-GetGcmChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetImportJob  **
  - **IAM action:**  [mobiletargeting:GetImportJob](#list_pinpoint-action-GetImportJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetImportJobs  **
  - **IAM action:**  [mobiletargeting:GetImportJobs](#list_pinpoint-action-GetImportJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetInAppMessages  **
  - **IAM action:**  [mobiletargeting:GetInAppMessages](#list_pinpoint-action-GetInAppMessages) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetInAppTemplate  **
  - **IAM action:**  [mobiletargeting:GetInAppTemplate](#list_pinpoint-action-GetInAppTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetJourney  **
  - **IAM action:**  [mobiletargeting:GetJourney](#list_pinpoint-action-GetJourney) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetJourneyDateRangeKpi  **
  - **IAM action:**  [mobiletargeting:GetJourneyDateRangeKpi](#list_pinpoint-action-GetJourneyDateRangeKpi) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetJourneyExecutionActivityMetrics  **
  - **IAM action:**  [mobiletargeting:GetJourneyExecutionActivityMetrics](#list_pinpoint-action-GetJourneyExecutionActivityMetrics) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetJourneyExecutionMetrics  **
  - **IAM action:**  [mobiletargeting:GetJourneyExecutionMetrics](#list_pinpoint-action-GetJourneyExecutionMetrics) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetJourneyRunExecutionActivityMetrics  **
  - **IAM action:**  [mobiletargeting:GetJourneyRunExecutionActivityMetrics](#list_pinpoint-action-GetJourneyRunExecutionActivityMetrics) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetJourneyRunExecutionMetrics  **
  - **IAM action:**  [mobiletargeting:GetJourneyRunExecutionMetrics](#list_pinpoint-action-GetJourneyRunExecutionMetrics) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetJourneyRuns  **
  - **IAM action:**  [mobiletargeting:GetJourneyRuns](#list_pinpoint-action-GetJourneyRuns) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetPushTemplate  **
  - **IAM action:**  [mobiletargeting:GetPushTemplate](#list_pinpoint-action-GetPushTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRecommenderConfiguration  **
  - **IAM action:**  [mobiletargeting:GetRecommenderConfiguration](#list_pinpoint-action-GetRecommenderConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRecommenderConfigurations  **
  - **IAM action:**  [mobiletargeting:GetRecommenderConfigurations](#list_pinpoint-action-GetRecommenderConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetSegment  **
  - **IAM action:**  [mobiletargeting:GetSegment](#list_pinpoint-action-GetSegment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSegmentExportJobs  **
  - **IAM action:**  [mobiletargeting:GetSegmentExportJobs](#list_pinpoint-action-GetSegmentExportJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetSegmentImportJobs  **
  - **IAM action:**  [mobiletargeting:GetSegmentImportJobs](#list_pinpoint-action-GetSegmentImportJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetSegmentVersion  **
  - **IAM action:**  [mobiletargeting:GetSegmentVersion](#list_pinpoint-action-GetSegmentVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSegmentVersions  **
  - **IAM action:**  [mobiletargeting:GetSegmentVersions](#list_pinpoint-action-GetSegmentVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetSegments  **
  - **IAM action:**  [mobiletargeting:GetSegments](#list_pinpoint-action-GetSegments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetSmsChannel  **
  - **IAM action:**  [mobiletargeting:GetSmsChannel](#list_pinpoint-action-GetSmsChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSmsTemplate  **
  - **IAM action:**  [mobiletargeting:GetSmsTemplate](#list_pinpoint-action-GetSmsTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetUserEndpoints  **
  - **IAM action:**  [mobiletargeting:GetUserEndpoints](#list_pinpoint-action-GetUserEndpoints) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetVoiceChannel  **
  - **IAM action:**  [mobiletargeting:GetVoiceChannel](#list_pinpoint-action-GetVoiceChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetVoiceTemplate  **
  - **IAM action:**  [mobiletargeting:GetVoiceTemplate](#list_pinpoint-action-GetVoiceTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListJourneys  **
  - **IAM action:**  [mobiletargeting:ListJourneys](#list_pinpoint-action-ListJourneys) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [mobiletargeting:ListTagsForResource](#list_pinpoint-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTemplateVersions  **
  - **IAM action:**  [mobiletargeting:ListTemplateVersions](#list_pinpoint-action-ListTemplateVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTemplates  **
  - **IAM action:**  [mobiletargeting:ListTemplates](#list_pinpoint-action-ListTemplates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PhoneNumberValidate  **
  - **IAM action:**  [mobiletargeting:PhoneNumberValidate](#list_pinpoint-action-PhoneNumberValidate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PutEventStream  **
  - **IAM action:**  [mobiletargeting:PutEventStream](#list_pinpoint-action-PutEventStream)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** mobiletargeting.amazonaws.com / **Access level:** Write

- **   PutEvents  **
  - **IAM action:**  [mobiletargeting:PutEvents](#list_pinpoint-action-PutEvents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RemoveAttributes  **
  - **IAM action:**  [mobiletargeting:RemoveAttributes](#list_pinpoint-action-RemoveAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SendMessages  **
  - **IAM action:**  [mobiletargeting:SendMessages](#list_pinpoint-action-SendMessages) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SendOTPMessage  **
  - **IAM action:**  [mobiletargeting:SendOTPMessage](#list_pinpoint-action-SendOTPMessage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SendUsersMessages  **
  - **IAM action:**  [mobiletargeting:SendUsersMessages](#list_pinpoint-action-SendUsersMessages) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [mobiletargeting:TagResource](#list_pinpoint-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [mobiletargeting:UntagResource](#list_pinpoint-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateAdmChannel  **
  - **IAM action:**  [mobiletargeting:UpdateAdmChannel](#list_pinpoint-action-UpdateAdmChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateApnsChannel  **
  - **IAM action:**  [mobiletargeting:UpdateApnsChannel](#list_pinpoint-action-UpdateApnsChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateApnsSandboxChannel  **
  - **IAM action:**  [mobiletargeting:UpdateApnsSandboxChannel](#list_pinpoint-action-UpdateApnsSandboxChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateApnsVoipChannel  **
  - **IAM action:**  [mobiletargeting:UpdateApnsVoipChannel](#list_pinpoint-action-UpdateApnsVoipChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateApnsVoipSandboxChannel  **
  - **IAM action:**  [mobiletargeting:UpdateApnsVoipSandboxChannel](#list_pinpoint-action-UpdateApnsVoipSandboxChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateApplicationSettings  **
  - **IAM action:**  [mobiletargeting:UpdateApplicationSettings](#list_pinpoint-action-UpdateApplicationSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateBaiduChannel  **
  - **IAM action:**  [mobiletargeting:UpdateBaiduChannel](#list_pinpoint-action-UpdateBaiduChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateCampaign  **
  - **IAM action:**  [mobiletargeting:UpdateCampaign](#list_pinpoint-action-UpdateCampaign) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateEmailChannel  **
  - **IAM action:**  [mobiletargeting:UpdateEmailChannel](#list_pinpoint-action-UpdateEmailChannel)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** mobiletargeting.amazonaws.com / **Access level:** Write

- **   UpdateEmailTemplate  **
  - **IAM action:**  [mobiletargeting:UpdateEmailTemplate](#list_pinpoint-action-UpdateEmailTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateEndpoint  **
  - **IAM action:**  [mobiletargeting:UpdateEndpoint](#list_pinpoint-action-UpdateEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateEndpointsBatch  **
  - **IAM action:**  [mobiletargeting:UpdateEndpointsBatch](#list_pinpoint-action-UpdateEndpointsBatch) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateGcmChannel  **
  - **IAM action:**  [mobiletargeting:UpdateGcmChannel](#list_pinpoint-action-UpdateGcmChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateInAppTemplate  **
  - **IAM action:**  [mobiletargeting:UpdateInAppTemplate](#list_pinpoint-action-UpdateInAppTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateJourney  **
  - **IAM action:**  [mobiletargeting:UpdateJourney](#list_pinpoint-action-UpdateJourney)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** mobiletargeting.amazonaws.com / **Access level:** Write

- **   UpdateJourneyState  **
  - **IAM action:**  [mobiletargeting:UpdateJourneyState](#list_pinpoint-action-UpdateJourneyState) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdatePushTemplate  **
  - **IAM action:**  [mobiletargeting:UpdatePushTemplate](#list_pinpoint-action-UpdatePushTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRecommenderConfiguration  **
  - **IAM action:**  [mobiletargeting:UpdateRecommenderConfiguration](#list_pinpoint-action-UpdateRecommenderConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** mobiletargeting.amazonaws.com / **Access level:** Write

- **   UpdateSegment  **
  - **IAM action:**  [mobiletargeting:UpdateSegment](#list_pinpoint-action-UpdateSegment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSmsChannel  **
  - **IAM action:**  [mobiletargeting:UpdateSmsChannel](#list_pinpoint-action-UpdateSmsChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSmsTemplate  **
  - **IAM action:**  [mobiletargeting:UpdateSmsTemplate](#list_pinpoint-action-UpdateSmsTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateTemplateActiveVersion  **
  - **IAM action:**  [mobiletargeting:UpdateTemplateActiveVersion](#list_pinpoint-action-UpdateTemplateActiveVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateVoiceChannel  **
  - **IAM action:**  [mobiletargeting:UpdateVoiceChannel](#list_pinpoint-action-UpdateVoiceChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateVoiceTemplate  **
  - **IAM action:**  [mobiletargeting:UpdateVoiceTemplate](#list_pinpoint-action-UpdateVoiceTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   VerifyOTPMessage  **
  - **IAM action:**  [mobiletargeting:VerifyOTPMessage](#list_pinpoint-action-VerifyOTPMessage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon Pinpoint
<a name="list_pinpoint-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateApp](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps.html#CreateApp)  **
  - **Description:** Grants permission to create an app
  - **Resource types (\*required):** [apps\*](#list_pinpoint-resource-apps)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-aws_TagKeys)
  - **Access level:** Write

- **   [CreateCampaign](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-campaigns.html#CreateCampaign)  **
  - **Description:** Grants permission to create a campaign for an app
  - **Resource types (\*required):** [app\*](#list_pinpoint-resource-app)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-aws_TagKeys)
  - **Access level:** Write

- **   [CreateEmailTemplate](https://docs.aws.amazon.com/pinpoint/latest/apireference/templates-template-name-email.html#CreateEmailTemplate)  **
  - **Description:** Grants permission to create an email template
  - **Resource types (\*required):** [template\*](#list_pinpoint-resource-template)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-aws_TagKeys)
  - **Access level:** Write

- **   [CreateExportJob](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-jobs-export.html#CreateExportJob)  **
  - **Description:** Grants permission to create an export job that exports endpoint definitions to Amazon S3
  - **Resource types (\*required):** [app\*](#list_pinpoint-resource-app)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateImportJob](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-jobs-import.html#CreateImportJob)  **
  - **Description:** Grants permission to import endpoint definitions from to create a segment
  - **Resource types (\*required):** [app\*](#list_pinpoint-resource-app)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateInAppTemplate](https://docs.aws.amazon.com/pinpoint/latest/apireference/templates-template-name-inapp.html#CreateInAppTemplate)  **
  - **Description:** Grants permission to create an in-app message template
  - **Resource types (\*required):** [template\*](#list_pinpoint-resource-template)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-aws_TagKeys)
  - **Access level:** Write

- **   [CreateJourney](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-journeys.html#CreateJourney)  **
  - **Description:** Grants permission to create a Journey for an app
  - **Resource types (\*required):** [journeys\*](#list_pinpoint-resource-journeys)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-aws_TagKeys)
  - **Access level:** Write

- **   [CreatePushTemplate](https://docs.aws.amazon.com/pinpoint/latest/apireference/templates-template-name-push.html#CreatePushTemplate)  **
  - **Description:** Grants permission to create a push notification template
  - **Resource types (\*required):** [template\*](#list_pinpoint-resource-template)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-aws_TagKeys)
  - **Access level:** Write

- **   [CreateRecommenderConfiguration](https://docs.aws.amazon.com/pinpoint/latest/apireference/recommenders.html#CreateRecommenderConfiguration)  **
  - **Description:** Grants permission to create an Amazon Pinpoint configuration for a recommender model
  - **Resource types (\*required):** [recommenders\*](#list_pinpoint-resource-recommenders)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateSegment](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-segments.html#CreateSegment)  **
  - **Description:** Grants permission to create a segment that is based on endpoint data reported to Pinpoint by your app. To allow a user to create a segment by importing endpoint data from outside of Pinpoint, allow the mobiletargeting:CreateImportJob action
  - **Resource types (\*required):** [app\*](#list_pinpoint-resource-app)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-aws_TagKeys)
  - **Access level:** Write

- **   [CreateSmsTemplate](https://docs.aws.amazon.com/pinpoint/latest/apireference/templates-template-name-sms.html#CreateSmsTemplate)  **
  - **Description:** Grants permission to create an sms message template
  - **Resource types (\*required):** [template\*](#list_pinpoint-resource-template)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-aws_TagKeys)
  - **Access level:** Write

- **   [CreateVoiceTemplate](https://docs.aws.amazon.com/pinpoint/latest/apireference/templates-template-name-voice.html#CreateVoiceTemplate)  **
  - **Description:** Grants permission to create a voice message template
  - **Resource types (\*required):** [template\*](#list_pinpoint-resource-template)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteAdmChannel](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-channels-adm.html#DeleteAdmChannel)  **
  - **Description:** Grants permission to delete the ADM channel for an app
  - **Resource types (\*required):** [channel\*](#list_pinpoint-resource-channel)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteApnsChannel](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-channels-apns.html#DeleteApnsChannel)  **
  - **Description:** Grants permission to delete the APNs channel for an app
  - **Resource types (\*required):** [channel\*](#list_pinpoint-resource-channel)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteApnsSandboxChannel](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-channels-apns_sandbox.html#DeleteApnsSandboxChannel)  **
  - **Description:** Grants permission to delete the APNs sandbox channel for an app
  - **Resource types (\*required):** [channel\*](#list_pinpoint-resource-channel)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteApnsVoipChannel](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-channels-apns_voip.html#DeleteApnsVoipChannel)  **
  - **Description:** Grants permission to delete the APNs VoIP channel for an app
  - **Resource types (\*required):** [channel\*](#list_pinpoint-resource-channel)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteApnsVoipSandboxChannel](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-channels-apns_voip_sandbox.html#DeleteApnsVoipSandboxChannel)  **
  - **Description:** Grants permission to delete the APNs VoIP sandbox channel for an app
  - **Resource types (\*required):** [channel\*](#list_pinpoint-resource-channel)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteApp](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id.html#DeleteApp)  **
  - **Description:** Grants permission to delete a specific campaign
  - **Resource types (\*required):** [app\*](#list_pinpoint-resource-app)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteBaiduChannel](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-channels-baidu.html#DeleteBaiduChannel)  **
  - **Description:** Grants permission to delete the Baidu channel for an app
  - **Resource types (\*required):** [channel\*](#list_pinpoint-resource-channel)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteCampaign](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-campaigns-campaign-id.html#DeleteCampaign)  **
  - **Description:** Grants permission to delete a specific campaign
  - **Resource types (\*required):** [campaign\*](#list_pinpoint-resource-campaign)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteEmailChannel](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-channels-email.html#DeleteEmailChannel)  **
  - **Description:** Grants permission to delete the email channel for an app
  - **Resource types (\*required):** [channel\*](#list_pinpoint-resource-channel)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteEmailTemplate](https://docs.aws.amazon.com/pinpoint/latest/apireference/templates-template-name-email.html#DeleteEmailTemplate)  **
  - **Description:** Grants permission to delete an email template or an email template version
  - **Resource types (\*required):** [template\*](#list_pinpoint-resource-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteEndpoint](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-endpoints-endpoint-id.html#DeleteEndpoint)  **
  - **Description:** Grants permission to delete an endpoint
  - **Resource types (\*required):** [endpoint\*](#list_pinpoint-resource-endpoint)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteEventStream](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-eventstream.html#DeleteEventStream)  **
  - **Description:** Grants permission to delete the event stream for an app
  - **Resource types (\*required):** [event-stream\*](#list_pinpoint-resource-event-stream)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteGcmChannel](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-channels-gcm.html#DeleteGcmChannel)  **
  - **Description:** Grants permission to delete the GCM channel for an app
  - **Resource types (\*required):** [channel\*](#list_pinpoint-resource-channel)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteInAppTemplate](https://docs.aws.amazon.com/pinpoint/latest/apireference/templates-template-name-inapp.html#DeleteInAppTemplate)  **
  - **Description:** Grants permission to delete an in-app message template or an in-app message template version
  - **Resource types (\*required):** [template\*](#list_pinpoint-resource-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteJourney](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-journeys-journey-id.html#DeleteJourney)  **
  - **Description:** Grants permission to delete a specific journey
  - **Resource types (\*required):** [journey\*](#list_pinpoint-resource-journey)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePushTemplate](https://docs.aws.amazon.com/pinpoint/latest/apireference/templates-template-name-push.html#DeletePushTemplate)  **
  - **Description:** Grants permission to delete a push notification template or a push notification template version
  - **Resource types (\*required):** [template\*](#list_pinpoint-resource-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRecommenderConfiguration](https://docs.aws.amazon.com/pinpoint/latest/apireference/recommenders-recommender-id.html#DeleteRecommenderConfiguration)  **
  - **Description:** Grants permission to delete an Amazon Pinpoint configuration for a recommender model
  - **Resource types (\*required):** [recommender\*](#list_pinpoint-resource-recommender)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteSegment](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-segments-segment-id.html#DeleteSegment)  **
  - **Description:** Grants permission to delete a specific segment
  - **Resource types (\*required):** [segment\*](#list_pinpoint-resource-segment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSmsChannel](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-channels-sms.html#DeleteSmsChannel)  **
  - **Description:** Grants permission to delete the SMS channel for an app
  - **Resource types (\*required):** [channel\*](#list_pinpoint-resource-channel)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteSmsTemplate](https://docs.aws.amazon.com/pinpoint/latest/apireference/templates-template-name-sms.html#DeleteSmsTemplate)  **
  - **Description:** Grants permission to delete an sms message template or an sms message template version
  - **Resource types (\*required):** [template\*](#list_pinpoint-resource-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteUserEndpoints](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-users-user-id.html#DeleteUserEndpoints)  **
  - **Description:** Grants permission to delete all of the endpoints that are associated with a user ID
  - **Resource types (\*required):** [user\*](#list_pinpoint-resource-user)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteVoiceChannel](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-channels-voice.html#DeleteVoiceChannel)  **
  - **Description:** Grants permission to delete the Voice channel for an app
  - **Resource types (\*required):** [channel\*](#list_pinpoint-resource-channel)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteVoiceTemplate](https://docs.aws.amazon.com/pinpoint/latest/apireference/templates-template-name-voice.html#DeleteVoiceTemplate)  **
  - **Description:** Grants permission to delete a voice message template or a voice message template version
  - **Resource types (\*required):** [template\*](#list_pinpoint-resource-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetAdmChannel](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-channels-adm.html#GetAdmChannel)  **
  - **Description:** Grants permission to retrieve information about the Amazon Device Messaging (ADM) channel for an app
  - **Resource types (\*required):** [channel\*](#list_pinpoint-resource-channel)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetApnsChannel](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-channels-apns.html#GetApnsChannel)  **
  - **Description:** Grants permission to retrieve information about the APNs channel for an app
  - **Resource types (\*required):** [channel\*](#list_pinpoint-resource-channel)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetApnsSandboxChannel](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-channels-apns_sandbox.html#GetApnsSandboxChannel)  **
  - **Description:** Grants permission to retrieve information about the APNs sandbox channel for an app
  - **Resource types (\*required):** [channel\*](#list_pinpoint-resource-channel)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetApnsVoipChannel](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-channels-apns_voip.html#GetApnsVoipChannel)  **
  - **Description:** Grants permission to retrieve information about the APNs VoIP channel for an app
  - **Resource types (\*required):** [channel\*](#list_pinpoint-resource-channel)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetApnsVoipSandboxChannel](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-channels-apns_voip_sandbox.html#GetApnsVoipSandboxChannel)  **
  - **Description:** Grants permission to retrieve information about the APNs VoIP sandbox channel for an app
  - **Resource types (\*required):** [channel\*](#list_pinpoint-resource-channel)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetApp](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id.html#GetApp)  **
  - **Description:** Grants permission to retrieve information about a specific app in your Amazon Pinpoint account
  - **Resource types (\*required):** [app\*](#list_pinpoint-resource-app)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetApplicationDateRangeKpi](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-kpis-daterange-kpi-name.html#GetApplicationDateRangeKpi)  **
  - **Description:** Grants permission to retrieve (queries) pre-aggregated data for a standard metric that applies to an application
  - **Resource types (\*required):** [application-metrics\*](#list_pinpoint-resource-application-metrics)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetApplicationSettings](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-settings.html#GetApplicationSettings)  **
  - **Description:** Grants permission to retrieve the default settings for an app
  - **Resource types (\*required):** [app\*](#list_pinpoint-resource-app)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [GetApps](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps.html#GetApps)  **
  - **Description:** Grants permission to retrieve a list of apps in your Amazon Pinpoint account
  - **Resource types (\*required):** [apps\*](#list_pinpoint-resource-apps)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetBaiduChannel](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-channels-baidu.html#GetBaiduChannel)  **
  - **Description:** Grants permission to retrieve information about the Baidu channel for an app
  - **Resource types (\*required):** [channel\*](#list_pinpoint-resource-channel)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetCampaign](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-campaigns-campaign-id.html#GetCampaign)  **
  - **Description:** Grants permission to retrieve information about a specific campaign
  - **Resource types (\*required):** [campaign\*](#list_pinpoint-resource-campaign)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCampaignActivities](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-campaigns-campaign-id-activities.html#GetCampaignActivities)  **
  - **Description:** Grants permission to retrieve information about the activities performed by a campaign
  - **Resource types (\*required):** [campaign\*](#list_pinpoint-resource-campaign)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [GetCampaignDateRangeKpi](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-campaigns-campaign-id-kpis-daterange-kpi-name.html#GetCampaignDateRangeKpi)  **
  - **Description:** Grants permission to retrieve (queries) pre-aggregated data for a standard metric that applies to a campaign
  - **Resource types (\*required):** [campaign-metrics\*](#list_pinpoint-resource-campaign-metrics)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetCampaignVersion](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-campaigns-campaign-id-versions-version.html#GetCampaignVersion)  **
  - **Description:** Grants permission to retrieve information about a specific campaign version
  - **Resource types (\*required):** [campaign\*](#list_pinpoint-resource-campaign)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCampaignVersions](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-campaigns-campaign-id-versions.html#GetCampaignVersions)  **
  - **Description:** Grants permission to retrieve information about the current and prior versions of a campaign
  - **Resource types (\*required):** [campaign\*](#list_pinpoint-resource-campaign)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [GetCampaigns](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-campaigns.html#GetCampaigns)  **
  - **Description:** Grants permission to retrieve information about all campaigns for an app
  - **Resource types (\*required):** [app\*](#list_pinpoint-resource-app)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [GetChannels](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-channels.html#GetChannels)  **
  - **Description:** Grants permission to get all channels information for your app
  - **Resource types (\*required):** [channels\*](#list_pinpoint-resource-channels)
  - **Condition keys:**  
  - **Access level:** List

- **   [GetEmailChannel](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-channels-email.html#GetEmailChannel)  **
  - **Description:** Grants permission to obtain information about the email channel in an app
  - **Resource types (\*required):** [channel\*](#list_pinpoint-resource-channel)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetEmailTemplate](https://docs.aws.amazon.com/pinpoint/latest/apireference/templates-template-name-email.html#GetEmailTemplate)  **
  - **Description:** Grants permission to retrieve information about a specific or the active version of an email template
  - **Resource types (\*required):** [template\*](#list_pinpoint-resource-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetEndpoint](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-endpoints-endpoint-id.html#GetEndpoint)  **
  - **Description:** Grants permission to retrieve information about a specific endpoint
  - **Resource types (\*required):** [endpoint\*](#list_pinpoint-resource-endpoint)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetEventStream](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-eventstream.html#GetEventStream)  **
  - **Description:** Grants permission to retrieve information about the event stream for an app
  - **Resource types (\*required):** [event-stream\*](#list_pinpoint-resource-event-stream)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetExportJob](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-jobs-export-job-id.html#GetExportJob)  **
  - **Description:** Grants permission to obtain information about a specific export job
  - **Resource types (\*required):** [export-job\*](#list_pinpoint-resource-export-job)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetExportJobs](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-jobs-export.html#GetExportJobs)  **
  - **Description:** Grants permission to retrieve a list of all of the export jobs for an app
  - **Resource types (\*required):** [app\*](#list_pinpoint-resource-app)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [GetGcmChannel](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-channels-gcm.html#GetGcmChannel)  **
  - **Description:** Grants permission to retrieve information about the GCM channel for an app
  - **Resource types (\*required):** [channel\*](#list_pinpoint-resource-channel)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetImportJob](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-jobs-import-job-id.html#GetImportJob)  **
  - **Description:** Grants permission to retrieve information about a specific import job
  - **Resource types (\*required):** [import-job\*](#list_pinpoint-resource-import-job)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetImportJobs](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-jobs-import.html#GetImportJobs)  **
  - **Description:** Grants permission to retrieve information about all import jobs for an app
  - **Resource types (\*required):** [app\*](#list_pinpoint-resource-app)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [GetInAppMessages](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-endpoints-endpoint-id-inappmessages.html#GetInAppMessages)  **
  - **Description:** Grants permission to retrive in-app messages for the given endpoint id
  - **Resource types (\*required):** [app\*](#list_pinpoint-resource-app)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetInAppTemplate](https://docs.aws.amazon.com/pinpoint/latest/apireference/templates-template-name-inapp.html#GetInAppTemplate)  **
  - **Description:** Grants permission to retrieve information about a specific or the active version of an in-app message template
  - **Resource types (\*required):** [template\*](#list_pinpoint-resource-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetJourney](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-journeys-journey-id.html#GetJourney)  **
  - **Description:** Grants permission to retrieve information about a specific journey
  - **Resource types (\*required):** [journey\*](#list_pinpoint-resource-journey)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetJourneyDateRangeKpi](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-journeys-journey-id-kpis-daterange-kpi-name.html#GetJourneyDateRangeKpi)  **
  - **Description:** Grants permission to retrieve (queries) pre-aggregated data for a standard engagement metric that applies to a journey
  - **Resource types (\*required):** [journey-metrics\*](#list_pinpoint-resource-journey-metrics)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetJourneyExecutionActivityMetrics](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-journeys-journey-id-activities-journey-activity-id-execution-metrics.html#GetJourneyExecutionActivityMetrics)  **
  - **Description:** Grants permission to retrieve (queries) pre-aggregated data for a standard execution metric that applies to a journey activity
  - **Resource types (\*required):** [journey-execution-activity-metrics\*](#list_pinpoint-resource-journey-execution-activity-metrics)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetJourneyExecutionMetrics](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-journeys-journey-id-execution-metrics.html#GetJourneyExecutionMetrics)  **
  - **Description:** Grants permission to retrieve (queries) pre-aggregated data for a standard execution metric that applies to a journey
  - **Resource types (\*required):** [journey-execution-metrics\*](#list_pinpoint-resource-journey-execution-metrics)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetJourneyRunExecutionActivityMetrics](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-journeys-journey-id-runs-run-id-activities-journey-activity-id-execution-metrics.html#GetJourneyRunExecutionActivityMetrics)  **
  - **Description:** Grants permission to retrieve (queries) pre-aggregated data for a standard execution metric that applies to a journey activity for a single journey run
  - **Resource types (\*required):** [journey\*](#list_pinpoint-resource-journey)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetJourneyRunExecutionMetrics](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-journeys-journey-id-runs-run-id-execution-metrics.html#GetJourneyRunExecutionMetrics)  **
  - **Description:** Grants permission to retrieve (queries) pre-aggregated data for a standard execution metric that applies to a journey for a single journey run
  - **Resource types (\*required):** [journey\*](#list_pinpoint-resource-journey)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetJourneyRuns](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-journeys-journey-id-runs.html)  **
  - **Description:** Grants permission to retrieve information about all journey runs for a journey
  - **Resource types (\*required):** [journey\*](#list_pinpoint-resource-journey)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [GetPushTemplate](https://docs.aws.amazon.com/pinpoint/latest/apireference/templates-template-name-push.html#GetPushTemplate)  **
  - **Description:** Grants permission to retrieve information about a specific or the active version of an push notification template
  - **Resource types (\*required):** [template\*](#list_pinpoint-resource-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRecommenderConfiguration](https://docs.aws.amazon.com/pinpoint/latest/apireference/recommenders-recommender-id.html#GetRecommenderConfiguration)  **
  - **Description:** Grants permission to retrieve information about an Amazon Pinpoint configuration for a recommender model
  - **Resource types (\*required):** [recommender\*](#list_pinpoint-resource-recommender)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetRecommenderConfigurations](https://docs.aws.amazon.com/pinpoint/latest/apireference/recommenders.html#GetRecommenderConfigurations)  **
  - **Description:** Grants permission to retrieve information about all the recommender model configurations that are associated with an Amazon Pinpoint account
  - **Resource types (\*required):** [recommenders\*](#list_pinpoint-resource-recommenders)
  - **Condition keys:**  
  - **Access level:** List

- **   [GetSegment](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-segments-segment-id.html#GetSegment)  **
  - **Description:** Grants permission to retrieve information about a specific segment
  - **Resource types (\*required):** [segment\*](#list_pinpoint-resource-segment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSegmentExportJobs](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-segments-segment-id-jobs-export.html#GetSegmentExportJobs)  **
  - **Description:** Grants permission to retrieve information about jobs that export endpoint definitions from segments to Amazon S3
  - **Resource types (\*required):** [segment\*](#list_pinpoint-resource-segment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [GetSegmentImportJobs](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-segments-segment-id-jobs-import.html#GetSegmentImportJobs)  **
  - **Description:** Grants permission to retrieve information about jobs that create segments by importing endpoint definitions from 
  - **Resource types (\*required):** [segment\*](#list_pinpoint-resource-segment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [GetSegmentVersion](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-segments-segment-id-versions-version.html#GetSegmentVersion)  **
  - **Description:** Grants permission to retrieve information about a specific segment version
  - **Resource types (\*required):** [segment\*](#list_pinpoint-resource-segment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSegmentVersions](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-segments-segment-id-versions.html#GetSegmentVersions)  **
  - **Description:** Grants permission to retrieve information about the current and prior versions of a segment
  - **Resource types (\*required):** [segment\*](#list_pinpoint-resource-segment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [GetSegments](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-segments.html#GetSegments)  **
  - **Description:** Grants permission to retrieve information about the segments for an app
  - **Resource types (\*required):** [app\*](#list_pinpoint-resource-app)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [GetSmsChannel](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-channels-sms.html#GetSmsChannel)  **
  - **Description:** Grants permission to obtain information about the SMS channel in an app
  - **Resource types (\*required):** [channel\*](#list_pinpoint-resource-channel)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSmsTemplate](https://docs.aws.amazon.com/pinpoint/latest/apireference/templates-template-name-sms.html#GetSmsTemplate)  **
  - **Description:** Grants permission to retrieve information about a specific or the active version of an sms message template
  - **Resource types (\*required):** [template\*](#list_pinpoint-resource-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetUserEndpoints](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-users-user-id.html#GetUserEndpoints)  **
  - **Description:** Grants permission to retrieve information about the endpoints that are associated with a user ID
  - **Resource types (\*required):** [user\*](#list_pinpoint-resource-user)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetVoiceChannel](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-channels-voice.html#GetVoiceChannel)  **
  - **Description:** Grants permission to obtain information about the Voice channel in an app
  - **Resource types (\*required):** [channel\*](#list_pinpoint-resource-channel)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetVoiceTemplate](https://docs.aws.amazon.com/pinpoint/latest/apireference/templates-template-name-voice.html#GetVoiceTemplate)  **
  - **Description:** Grants permission to retrieve information about a specific or the active version of a voice message template
  - **Resource types (\*required):** [template\*](#list_pinpoint-resource-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListJourneys](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-journeys.html#ListJourneys)  **
  - **Description:** Grants permission to retrieve information about all journeys for an app
  - **Resource types (\*required):** [app\*](#list_pinpoint-resource-app)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/pinpoint/latest/apireference/tags-resource-arn.html#ListTagsForResource)  **
  - **Description:** Grants permission to list tags for a resource
  - **Resource types (\*required):** [app](#list_pinpoint-resource-app) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [campaign](#list_pinpoint-resource-campaign) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [journey](#list_pinpoint-resource-journey) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [segment](#list_pinpoint-resource-segment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [template](#list_pinpoint-resource-template) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListTemplateVersions](https://docs.aws.amazon.com/pinpoint/latest/apireference/templates-template-name-template-type-versions.html#ListTemplateVersions)  **
  - **Description:** Grants permission to retrieve all versions about a specific template
  - **Resource types (\*required):** [template\*](#list_pinpoint-resource-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTemplates](https://docs.aws.amazon.com/pinpoint/latest/apireference/templates.html#ListTemplates)  **
  - **Description:** Grants permission to retrieve metadata about the queried templates
  - **Resource types (\*required):** [templates\*](#list_pinpoint-resource-templates)
  - **Condition keys:**  
  - **Access level:** List

- **   [PhoneNumberValidate](https://docs.aws.amazon.com/pinpoint/latest/apireference/phone-number-validate.html#PhoneNumberValidate)  **
  - **Description:** Grants permission to obtain metadata for a phone number, such as the number type (mobile, landline, or VoIP), location, and provider
  - **Resource types (\*required):** [phone-number-validate\*](#list_pinpoint-resource-phone-number-validate)
  - **Condition keys:**  
  - **Access level:** Read

- **   [PutEventStream](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-eventstream.html#PutEventStream)  **
  - **Description:** Grants permission to create or update an event stream for an app
  - **Resource types (\*required):** [event-stream\*](#list_pinpoint-resource-event-stream)
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutEvents](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-events.html#PutEvents)  **
  - **Description:** Grants permission to create or update events for an app
  - **Resource types (\*required):** [events\*](#list_pinpoint-resource-events)
  - **Condition keys:**  
  - **Access level:** Write

- **   [RemoveAttributes](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-attributes-attribute-type.html#RemoveAttributes)  **
  - **Description:** Grants permission to remove the attributes for an app
  - **Resource types (\*required):** [attribute\*](#list_pinpoint-resource-attribute)
  - **Condition keys:**  
  - **Access level:** Write

- **   [SendMessages](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-messages.html#SendMessages)  **
  - **Description:** Grants permission to send an SMS message or push notification to specific endpoints
  - **Resource types (\*required):** [messages\*](#list_pinpoint-resource-messages)
  - **Condition keys:**  
  - **Access level:** Write

- **   [SendOTPMessage](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-otp.html#SendOTPMessage)  **
  - **Description:** Grants permission to send an OTP code to a user of your application
  - **Resource types (\*required):** [otp\*](#list_pinpoint-resource-otp)
  - **Condition keys:**  
  - **Access level:** Write

- **   [SendUsersMessages](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-users-messages.html#SendUsersMessages)  **
  - **Description:** Grants permission to send an SMS message or push notification to all endpoints that are associated with a specific user ID
  - **Resource types (\*required):** [messages\*](#list_pinpoint-resource-messages)
  - **Condition keys:**  
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/pinpoint/latest/apireference/tags-resource-arn.html#TagResource)  **
  - **Description:** Grants permission to add tags to a resource
  - **Resource types (\*required):** [app](#list_pinpoint-resource-app) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-aws_TagKeys)
  - **Resource types (\*required):** [campaign](#list_pinpoint-resource-campaign) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-aws_TagKeys)
  - **Resource types (\*required):** [journey](#list_pinpoint-resource-journey) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-aws_TagKeys)
  - **Resource types (\*required):** [segment](#list_pinpoint-resource-segment) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-aws_TagKeys)
  - **Resource types (\*required):** [template](#list_pinpoint-resource-template) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/pinpoint/latest/apireference/tags-resource-arn.html#UntagResource)  **
  - **Description:** Grants permission to remove tags from a resource
  - **Resource types (\*required):** [app](#list_pinpoint-resource-app) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-aws_TagKeys)
  - **Resource types (\*required):** [campaign](#list_pinpoint-resource-campaign) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-aws_TagKeys)
  - **Resource types (\*required):** [journey](#list_pinpoint-resource-journey) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-aws_TagKeys)
  - **Resource types (\*required):** [segment](#list_pinpoint-resource-segment) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-aws_TagKeys)
  - **Resource types (\*required):** [template](#list_pinpoint-resource-template) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateAdmChannel](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-channels-adm.html#UpdateAdmChannel)  **
  - **Description:** Grants permission to update the Amazon Device Messaging (ADM) channel for an app
  - **Resource types (\*required):** [channel\*](#list_pinpoint-resource-channel)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateApnsChannel](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-channels-apns.html#UpdateApnsChannel)  **
  - **Description:** Grants permission to update the Apple Push Notification service (APNs) channel for an app
  - **Resource types (\*required):** [channel\*](#list_pinpoint-resource-channel)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateApnsSandboxChannel](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-channels-apns_sandbox.html#UpdateApnsSandboxChannel)  **
  - **Description:** Grants permission to update the Apple Push Notification service (APNs) sandbox channel for an app
  - **Resource types (\*required):** [channel\*](#list_pinpoint-resource-channel)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateApnsVoipChannel](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-channels-apns_voip.html#UpdateApnsVoipChannel)  **
  - **Description:** Grants permission to update the Apple Push Notification service (APNs) VoIP channel for an app
  - **Resource types (\*required):** [channel\*](#list_pinpoint-resource-channel)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateApnsVoipSandboxChannel](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-channels-apns_voip_sandbox.html#UpdateApnsVoipSandboxChannel)  **
  - **Description:** Grants permission to update the Apple Push Notification service (APNs) VoIP sandbox channel for an app
  - **Resource types (\*required):** [channel\*](#list_pinpoint-resource-channel)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateApplicationSettings](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-settings.html#UpdateApplicationSettings)  **
  - **Description:** Grants permission to update the default settings for an app
  - **Resource types (\*required):** [app\*](#list_pinpoint-resource-app)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateBaiduChannel](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-channels-baidu.html#UpdateBaiduChannel)  **
  - **Description:** Grants permission to update the Baidu channel for an app
  - **Resource types (\*required):** [channel\*](#list_pinpoint-resource-channel)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateCampaign](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-campaigns-campaign-id.html#UpdateCampaign)  **
  - **Description:** Grants permission to update a specific campaign
  - **Resource types (\*required):** [campaign\*](#list_pinpoint-resource-campaign)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-aws_TagKeys)
  - **Access level:** Write

- **   [UpdateEmailChannel](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-channels-email.html#UpdateEmailChannel)  **
  - **Description:** Grants permission to update the email channel for an app
  - **Resource types (\*required):** [channel\*](#list_pinpoint-resource-channel)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateEmailTemplate](https://docs.aws.amazon.com/pinpoint/latest/apireference/templates-template-name-email.html#UpdateEmailTemplate)  **
  - **Description:** Grants permission to update a specific email template under the same version or generate a new version
  - **Resource types (\*required):** [template\*](#list_pinpoint-resource-template)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-aws_TagKeys)
  - **Access level:** Write

- **   [UpdateEndpoint](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-endpoints-endpoint-id.html#UpdateEndpoint)  **
  - **Description:** Grants permission to create an endpoint or update the information for an endpoint
  - **Resource types (\*required):** [endpoint\*](#list_pinpoint-resource-endpoint)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateEndpointsBatch](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-endpoints.html#UpdateEndpointsBatch)  **
  - **Description:** Grants permission to create or update endpoints as a batch operation
  - **Resource types (\*required):** [app\*](#list_pinpoint-resource-app)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateGcmChannel](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-channels-gcm.html#UpdateGcmChannel)  **
  - **Description:** Grants permission to update the Firebase Cloud Messaging (FCM) or Google Cloud Messaging (GCM) API key that allows to send push notifications to your Android app
  - **Resource types (\*required):** [channel\*](#list_pinpoint-resource-channel)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateInAppTemplate](https://docs.aws.amazon.com/pinpoint/latest/apireference/templates-template-name-inapp.html#UpdateInAppTemplate)  **
  - **Description:** Grants permission to update a specific in-app message template under the same version or generate a new version
  - **Resource types (\*required):** [template\*](#list_pinpoint-resource-template)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-aws_TagKeys)
  - **Access level:** Write

- **   [UpdateJourney](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-journeys-journey-id.html#UpdateJourney)  **
  - **Description:** Grants permission to update a specific journey
  - **Resource types (\*required):** [journey\*](#list_pinpoint-resource-journey)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-aws_TagKeys)
  - **Access level:** Write

- **   [UpdateJourneyState](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-journeys-journey-id-state.html#UpdateJourneyState)  **
  - **Description:** Grants permission to update a specific journey state
  - **Resource types (\*required):** [journey\*](#list_pinpoint-resource-journey)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-aws_TagKeys)
  - **Access level:** Write

- **   [UpdatePushTemplate](https://docs.aws.amazon.com/pinpoint/latest/apireference/templates-template-name-push.html#UpdatePushTemplate)  **
  - **Description:** Grants permission to update a specific push notification template under the same version or generate a new version
  - **Resource types (\*required):** [template\*](#list_pinpoint-resource-template)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-aws_TagKeys)
  - **Access level:** Write

- **   [UpdateRecommenderConfiguration](https://docs.aws.amazon.com/pinpoint/latest/apireference/recommenders-recommender-id.html#UpdateRecommenderConfiguration)  **
  - **Description:** Grants permission to update an Amazon Pinpoint configuration for a recommender model
  - **Resource types (\*required):** [recommender\*](#list_pinpoint-resource-recommender)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateSegment](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-segments-segment-id.html#UpdateSegment)  **
  - **Description:** Grants permission to update a specific segment
  - **Resource types (\*required):** [segment\*](#list_pinpoint-resource-segment)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-aws_TagKeys)
  - **Access level:** Write

- **   [UpdateSmsChannel](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-channels-sms.html#UpdateSmsChannel)  **
  - **Description:** Grants permission to update the SMS channel for an app
  - **Resource types (\*required):** [channel\*](#list_pinpoint-resource-channel)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateSmsTemplate](https://docs.aws.amazon.com/pinpoint/latest/apireference/templates-template-name-sms.html#UpdateSmsTemplate)  **
  - **Description:** Grants permission to update a specific sms message template under the same version or generate a new version
  - **Resource types (\*required):** [template\*](#list_pinpoint-resource-template)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-aws_TagKeys)
  - **Access level:** Write

- **   [UpdateTemplateActiveVersion](https://docs.aws.amazon.com/pinpoint/latest/apireference/templates-template-name-template-type-active-version.html#UpdateTemplateActiveVersion)  **
  - **Description:** Grants permission to update the active version parameter of a specific template
  - **Resource types (\*required):** [template\*](#list_pinpoint-resource-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateVoiceChannel](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-channels-voice.html#UpdateVoiceChannel)  **
  - **Description:** Grants permission to update the Voice channel for an app
  - **Resource types (\*required):** [channel\*](#list_pinpoint-resource-channel)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateVoiceTemplate](https://docs.aws.amazon.com/pinpoint/latest/apireference/templates-template-name-voice.html#UpdateVoiceTemplate)  **
  - **Description:** Grants permission to update a specific voice message template under the same version or generate a new version
  - **Resource types (\*required):** [template\*](#list_pinpoint-resource-template)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-aws_TagKeys)
  - **Access level:** Write

- **   [VerifyOTPMessage](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-verify-otp.html#VerifyOTPMessage)  **
  - **Description:** Grants permission to check the validity of One-Time Passwords (OTPs)
  - **Resource types (\*required):** [verify-otp\*](#list_pinpoint-resource-verify-otp)
  - **Condition keys:**  
  - **Access level:** Write



## Permission-only actions for Amazon Pinpoint
<a name="list_pinpoint-permission-only-actions"></a>

The following actions are defined by Amazon Pinpoint but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [GetReports](${UserGuideDocPage}/permissions-actions.html)  **
  - **Description:** Grants permission to mobiletargeting:GetReports
  - **Resource types (\*required):** [reports\*](#list_pinpoint-resource-reports)
  - **Condition keys:**  
  - **Access level:** Read



## Resource types defined by Amazon Pinpoint
<a name="list_pinpoint-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [app](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id.html)  | arn:${Partition}:mobiletargeting:${Region}:${Account}:apps/${AppId} | [aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_) | 
|  [application-metrics](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-kpis-daterange-kpi-name.html)  | arn:${Partition}:mobiletargeting:${Region}:${Account}:apps/${AppId}/kpis/daterange/${KpiName} |   | 
|  [apps](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps.html)  | arn:${Partition}:mobiletargeting:${Region}:${Account}:apps/\* |   | 
|  [attribute](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-attributes-attribute-type.html)  | arn:${Partition}:mobiletargeting:${Region}:${Account}:apps/${AppId}/attributes/${AttributeType} |   | 
|  [campaign](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-campaigns-campaign-id.html)  | arn:${Partition}:mobiletargeting:${Region}:${Account}:apps/${AppId}/campaigns/${CampaignId} | [aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_) | 
|  [campaign-metrics](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-campaigns-campaign-id-kpis-daterange-kpi-name.html)  | arn:${Partition}:mobiletargeting:${Region}:${Account}:apps/${AppId}/campaigns/${CampaignId}/kpis/daterange/${KpiName} |   | 
|  [channel](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-channels.html)  | arn:${Partition}:mobiletargeting:${Region}:${Account}:apps/${AppId}/channels/${ChannelType} |   | 
|  [channels](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-channels.html)  | arn:${Partition}:mobiletargeting:${Region}:${Account}:apps/${AppId}/channels |   | 
|  [endpoint](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-endpoints-endpoint-id.html)  | arn:${Partition}:mobiletargeting:${Region}:${Account}:apps/${AppId}/endpoints/${EndpointId} |   | 
|  [event-stream](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-eventstream.html)  | arn:${Partition}:mobiletargeting:${Region}:${Account}:apps/${AppId}/eventstream |   | 
|  [events](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-events.html)  | arn:${Partition}:mobiletargeting:${Region}:${Account}:apps/${AppId}/events |   | 
|  [export-job](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-jobs-export-job-id.html)  | arn:${Partition}:mobiletargeting:${Region}:${Account}:apps/${AppId}/jobs/export/${JobId} |   | 
|  [import-job](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-jobs-import-job-id.html)  | arn:${Partition}:mobiletargeting:${Region}:${Account}:apps/${AppId}/jobs/import/${JobId} |   | 
|  [journey](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-journeys-journey-id.html)  | arn:${Partition}:mobiletargeting:${Region}:${Account}:apps/${AppId}/journeys/${JourneyId} | [aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_) | 
|  [journey-execution-activity-metrics](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-journeys-journey-id-activities-journey-activity-id-execution-metrics.html)  | arn:${Partition}:mobiletargeting:${Region}:${Account}:apps/${AppId}/journeys/${JourneyId}/activities/${JourneyActivityId}/execution-metrics |   | 
|  [journey-execution-metrics](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-journeys-journey-id-execution-metrics.html)  | arn:${Partition}:mobiletargeting:${Region}:${Account}:apps/${AppId}/journeys/${JourneyId}/execution-metrics |   | 
|  [journey-metrics](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-journeys-journey-id-kpis-daterange-kpi-name.html)  | arn:${Partition}:mobiletargeting:${Region}:${Account}:apps/${AppId}/journeys/${JourneyId}/kpis/daterange/${KpiName} |   | 
|  [journeys](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-journeys.html)  | arn:${Partition}:mobiletargeting:${Region}:${Account}:apps/${AppId}/journeys |   | 
|  [messages](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-messages.html)  | arn:${Partition}:mobiletargeting:${Region}:${Account}:apps/${AppId}/messages |   | 
|  [otp](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-verify-otp.html)  | arn:${Partition}:mobiletargeting:${Region}:${Account}:apps/${AppId}/otp |   | 
|  [phone-number-validate](https://docs.aws.amazon.com/pinpoint/latest/apireference/phone-number-validate.html)  | arn:${Partition}:mobiletargeting:${Region}:${Account}:phone/number/validate |   | 
|  [recommender](https://docs.aws.amazon.com/pinpoint/latest/apireference/recommenders.html)  | arn:${Partition}:mobiletargeting:${Region}:${Account}:recommenders/${RecommenderId} |   | 
|  [recommenders](https://docs.aws.amazon.com/pinpoint/latest/apireference/recommenders.html)  | arn:${Partition}:mobiletargeting:${Region}:${Account}:recommenders/\* |   | 
|  [reports](https://docs.aws.amazon.com/pinpoint/latest/apireference/reports.html)  | arn:${Partition}:mobiletargeting:${Region}:${Account}:reports |   | 
|  [segment](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-segments-segment-id.html)  | arn:${Partition}:mobiletargeting:${Region}:${Account}:apps/${AppId}/segments/${SegmentId} | [aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_) | 
|  [template](https://docs.aws.amazon.com/pinpoint/latest/apireference/templates.html)  | arn:${Partition}:mobiletargeting:${Region}:${Account}:templates/${TemplateName}/${TemplateType} | [aws:ResourceTag/${TagKey}](#list_pinpoint-aws_ResourceTag___TagKey_) | 
|  [templates](https://docs.aws.amazon.com/pinpoint/latest/apireference/templates.html)  | arn:${Partition}:mobiletargeting:${Region}:${Account}:templates |   | 
|  [user](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-users-user-id.html)  | arn:${Partition}:mobiletargeting:${Region}:${Account}:apps/${AppId}/users/${UserId} |   | 
|  [verify-otp](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-verify-otp.html)  | arn:${Partition}:mobiletargeting:${Region}:${Account}:apps/${AppId}/verify-otp |   | 

## Condition keys for Amazon Pinpoint
<a name="list_pinpoint-policy-keys"></a>

Amazon Pinpoint defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-permissions.html#iam-contextkeys)  | Filters access by a key that is present in the request the user makes to the pinpoint service | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-permissions.html#iam-contextkeys)  | Filters access by a tag key and value pair | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-permissions.html#iam-contextkeys)  | Filters access by the list of all the tag key names present in the request the user makes to the pinpoint service | ArrayOfString | 