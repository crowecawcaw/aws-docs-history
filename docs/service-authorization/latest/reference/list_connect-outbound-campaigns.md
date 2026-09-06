

# Actions, resources, and condition keys for Amazon Connect Outbound Campaigns
<a name="list_connect-outbound-campaigns"></a>

Amazon Connect Outbound Campaigns (service prefix: `connect-campaigns`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/connect/latest/adminguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/connect/latest/adminguide/enable-outbound-campaigns.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/connect/latest/adminguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/connect-campaigns/connect-campaigns.json) for this service.

**Topics**
+ [API operations defined by Amazon Connect Outbound Campaigns](#list_connect-outbound-campaigns-operations)
+ [Actions defined by Amazon Connect Outbound Campaigns](#list_connect-outbound-campaigns-actions-as-permissions)
+ [Resource types defined by Amazon Connect Outbound Campaigns](#list_connect-outbound-campaigns-resources-for-iam-policies)
+ [Condition keys for Amazon Connect Outbound Campaigns](#list_connect-outbound-campaigns-policy-keys)

## API operations defined by Amazon Connect Outbound Campaigns
<a name="list_connect-outbound-campaigns-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_connect-outbound-campaigns-actions-as-permissions).




- **   CreateCampaign  **
  - **SDK client:** connectcampaigns
  - **IAM action:**  [connect-campaigns:CreateCampaign](#list_connect-outbound-campaigns-action-CreateCampaign)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [connect-campaigns:TagResource](#list_connect-outbound-campaigns-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteCampaign  **
  - **SDK client:** connectcampaigns
  - **IAM action:**  [connect-campaigns:DeleteCampaign](#list_connect-outbound-campaigns-action-DeleteCampaign) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteConnectInstanceConfig  **
  - **SDK client:** connectcampaigns
  - **IAM action:**  [connect-campaigns:DeleteConnectInstanceConfig](#list_connect-outbound-campaigns-action-DeleteConnectInstanceConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteInstanceOnboardingJob  **
  - **SDK client:** connectcampaigns
  - **IAM action:**  [connect-campaigns:DeleteInstanceOnboardingJob](#list_connect-outbound-campaigns-action-DeleteInstanceOnboardingJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeCampaign  **
  - **SDK client:** connectcampaigns
  - **IAM action:**  [connect-campaigns:DescribeCampaign](#list_connect-outbound-campaigns-action-DescribeCampaign) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCampaignState  **
  - **SDK client:** connectcampaigns
  - **IAM action:**  [connect-campaigns:GetCampaignState](#list_connect-outbound-campaigns-action-GetCampaignState) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCampaignStateBatch  **
  - **SDK client:** connectcampaigns
  - **IAM action:**  [connect-campaigns:GetCampaignStateBatch](#list_connect-outbound-campaigns-action-GetCampaignStateBatch) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetConnectInstanceConfig  **
  - **SDK client:** connectcampaigns
  - **IAM action:**  [connect-campaigns:GetConnectInstanceConfig](#list_connect-outbound-campaigns-action-GetConnectInstanceConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetInstanceOnboardingJobStatus  **
  - **SDK client:** connectcampaigns
  - **IAM action:**  [connect-campaigns:GetInstanceOnboardingJobStatus](#list_connect-outbound-campaigns-action-GetInstanceOnboardingJobStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListCampaigns  **
  - **SDK client:** connectcampaigns
  - **IAM action:**  [connect-campaigns:ListCampaigns](#list_connect-outbound-campaigns-action-ListCampaigns) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **SDK client:** connectcampaigns
  - **IAM action:**  [connect-campaigns:ListTagsForResource](#list_connect-outbound-campaigns-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PauseCampaign  **
  - **SDK client:** connectcampaigns
  - **IAM action:**  [connect-campaigns:PauseCampaign](#list_connect-outbound-campaigns-action-PauseCampaign) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutDialRequestBatch  **
  - **SDK client:** connectcampaigns
  - **IAM action:**  [connect-campaigns:PutDialRequestBatch](#list_connect-outbound-campaigns-action-PutDialRequestBatch) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ResumeCampaign  **
  - **SDK client:** connectcampaigns
  - **IAM action:**  [connect-campaigns:ResumeCampaign](#list_connect-outbound-campaigns-action-ResumeCampaign) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartCampaign  **
  - **SDK client:** connectcampaigns
  - **IAM action:**  [connect-campaigns:StartCampaign](#list_connect-outbound-campaigns-action-StartCampaign) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartInstanceOnboardingJob  **
  - **SDK client:** connectcampaigns
  - **IAM action:**  [connect-campaigns:StartInstanceOnboardingJob](#list_connect-outbound-campaigns-action-StartInstanceOnboardingJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopCampaign  **
  - **SDK client:** connectcampaigns
  - **IAM action:**  [connect-campaigns:StopCampaign](#list_connect-outbound-campaigns-action-StopCampaign) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **SDK client:** connectcampaigns
  - **IAM action:**  [connect-campaigns:TagResource](#list_connect-outbound-campaigns-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **SDK client:** connectcampaigns
  - **IAM action:**  [connect-campaigns:UntagResource](#list_connect-outbound-campaigns-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateCampaignDialerConfig  **
  - **SDK client:** connectcampaigns
  - **IAM action:**  [connect-campaigns:UpdateCampaignDialerConfig](#list_connect-outbound-campaigns-action-UpdateCampaignDialerConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateCampaignName  **
  - **SDK client:** connectcampaigns
  - **IAM action:**  [connect-campaigns:UpdateCampaignName](#list_connect-outbound-campaigns-action-UpdateCampaignName) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateCampaignOutboundCallConfig  **
  - **SDK client:** connectcampaigns
  - **IAM action:**  [connect-campaigns:UpdateCampaignOutboundCallConfig](#list_connect-outbound-campaigns-action-UpdateCampaignOutboundCallConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateCampaign  **
  - **SDK client:** connectcampaignsv2
  - **IAM action:**  [connect-campaigns:CreateCampaign](#list_connect-outbound-campaigns-action-CreateCampaign)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [connect-campaigns:TagResource](#list_connect-outbound-campaigns-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteCampaign  **
  - **SDK client:** connectcampaignsv2
  - **IAM action:**  [connect-campaigns:DeleteCampaign](#list_connect-outbound-campaigns-action-DeleteCampaign) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCampaignChannelSubtypeConfig  **
  - **SDK client:** connectcampaignsv2
  - **IAM action:**  [connect-campaigns:DeleteCampaignChannelSubtypeConfig](#list_connect-outbound-campaigns-action-DeleteCampaignChannelSubtypeConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCampaignCommunicationLimits  **
  - **SDK client:** connectcampaignsv2
  - **IAM action:**  [connect-campaigns:DeleteCampaignCommunicationLimits](#list_connect-outbound-campaigns-action-DeleteCampaignCommunicationLimits) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCampaignCommunicationTime  **
  - **SDK client:** connectcampaignsv2
  - **IAM action:**  [connect-campaigns:DeleteCampaignCommunicationTime](#list_connect-outbound-campaigns-action-DeleteCampaignCommunicationTime) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCampaignEntryLimits  **
  - **SDK client:** connectcampaignsv2
  - **IAM action:**  [connect-campaigns:DeleteCampaignEntryLimits](#list_connect-outbound-campaigns-action-DeleteCampaignEntryLimits) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteConnectInstanceConfig  **
  - **SDK client:** connectcampaignsv2
  - **IAM action:**  [connect-campaigns:DeleteConnectInstanceConfig](#list_connect-outbound-campaigns-action-DeleteConnectInstanceConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteConnectInstanceIntegration  **
  - **SDK client:** connectcampaignsv2
  - **IAM action:**  [connect-campaigns:DeleteConnectInstanceIntegration](#list_connect-outbound-campaigns-action-DeleteConnectInstanceIntegration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteInstanceOnboardingJob  **
  - **SDK client:** connectcampaignsv2
  - **IAM action:**  [connect-campaigns:DeleteInstanceOnboardingJob](#list_connect-outbound-campaigns-action-DeleteInstanceOnboardingJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeCampaign  **
  - **SDK client:** connectcampaignsv2
  - **IAM action:**  [connect-campaigns:DescribeCampaign](#list_connect-outbound-campaigns-action-DescribeCampaign) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCampaignState  **
  - **SDK client:** connectcampaignsv2
  - **IAM action:**  [connect-campaigns:GetCampaignState](#list_connect-outbound-campaigns-action-GetCampaignState) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCampaignStateBatch  **
  - **SDK client:** connectcampaignsv2
  - **IAM action:**  [connect-campaigns:GetCampaignStateBatch](#list_connect-outbound-campaigns-action-GetCampaignStateBatch) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetConnectInstanceConfig  **
  - **SDK client:** connectcampaignsv2
  - **IAM action:**  [connect-campaigns:GetConnectInstanceConfig](#list_connect-outbound-campaigns-action-GetConnectInstanceConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetInstanceCommunicationLimits  **
  - **SDK client:** connectcampaignsv2
  - **IAM action:**  [connect-campaigns:GetInstanceCommunicationLimits](#list_connect-outbound-campaigns-action-GetInstanceCommunicationLimits) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetInstanceOnboardingJobStatus  **
  - **SDK client:** connectcampaignsv2
  - **IAM action:**  [connect-campaigns:GetInstanceOnboardingJobStatus](#list_connect-outbound-campaigns-action-GetInstanceOnboardingJobStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListCampaigns  **
  - **SDK client:** connectcampaignsv2
  - **IAM action:**  [connect-campaigns:ListCampaigns](#list_connect-outbound-campaigns-action-ListCampaigns) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListConnectInstanceIntegrations  **
  - **SDK client:** connectcampaignsv2
  - **IAM action:**  [connect-campaigns:ListConnectInstanceIntegrations](#list_connect-outbound-campaigns-action-ListConnectInstanceIntegrations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **SDK client:** connectcampaignsv2
  - **IAM action:**  [connect-campaigns:ListTagsForResource](#list_connect-outbound-campaigns-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PauseCampaign  **
  - **SDK client:** connectcampaignsv2
  - **IAM action:**  [connect-campaigns:PauseCampaign](#list_connect-outbound-campaigns-action-PauseCampaign) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutConnectInstanceIntegration  **
  - **SDK client:** connectcampaignsv2
  - **IAM action:**  [connect-campaigns:PutConnectInstanceIntegration](#list_connect-outbound-campaigns-action-PutConnectInstanceIntegration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutInstanceCommunicationLimits  **
  - **SDK client:** connectcampaignsv2
  - **IAM action:**  [connect-campaigns:PutInstanceCommunicationLimits](#list_connect-outbound-campaigns-action-PutInstanceCommunicationLimits) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutOutboundRequestBatch  **
  - **SDK client:** connectcampaignsv2
  - **IAM action:**  [connect-campaigns:PutOutboundRequestBatch](#list_connect-outbound-campaigns-action-PutOutboundRequestBatch) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutProfileOutboundRequestBatch  **
  - **SDK client:** connectcampaignsv2
  - **IAM action:**  [connect-campaigns:PutProfileOutboundRequestBatch](#list_connect-outbound-campaigns-action-PutProfileOutboundRequestBatch) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ResumeCampaign  **
  - **SDK client:** connectcampaignsv2
  - **IAM action:**  [connect-campaigns:ResumeCampaign](#list_connect-outbound-campaigns-action-ResumeCampaign) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartCampaign  **
  - **SDK client:** connectcampaignsv2
  - **IAM action:**  [connect-campaigns:StartCampaign](#list_connect-outbound-campaigns-action-StartCampaign) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartInstanceOnboardingJob  **
  - **SDK client:** connectcampaignsv2
  - **IAM action:**  [connect-campaigns:StartInstanceOnboardingJob](#list_connect-outbound-campaigns-action-StartInstanceOnboardingJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopCampaign  **
  - **SDK client:** connectcampaignsv2
  - **IAM action:**  [connect-campaigns:StopCampaign](#list_connect-outbound-campaigns-action-StopCampaign) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **SDK client:** connectcampaignsv2
  - **IAM action:**  [connect-campaigns:TagResource](#list_connect-outbound-campaigns-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **SDK client:** connectcampaignsv2
  - **IAM action:**  [connect-campaigns:UntagResource](#list_connect-outbound-campaigns-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateCampaignChannelSubtypeConfig  **
  - **SDK client:** connectcampaignsv2
  - **IAM action:**  [connect-campaigns:UpdateCampaignChannelSubtypeConfig](#list_connect-outbound-campaigns-action-UpdateCampaignChannelSubtypeConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateCampaignCommunicationLimits  **
  - **SDK client:** connectcampaignsv2
  - **IAM action:**  [connect-campaigns:UpdateCampaignCommunicationLimits](#list_connect-outbound-campaigns-action-UpdateCampaignCommunicationLimits) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateCampaignCommunicationTime  **
  - **SDK client:** connectcampaignsv2
  - **IAM action:**  [connect-campaigns:UpdateCampaignCommunicationTime](#list_connect-outbound-campaigns-action-UpdateCampaignCommunicationTime) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateCampaignEntryLimits  **
  - **SDK client:** connectcampaignsv2
  - **IAM action:**  [connect-campaigns:UpdateCampaignEntryLimits](#list_connect-outbound-campaigns-action-UpdateCampaignEntryLimits) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateCampaignFlowAssociation  **
  - **SDK client:** connectcampaignsv2
  - **IAM action:**  [connect-campaigns:UpdateCampaignFlowAssociation](#list_connect-outbound-campaigns-action-UpdateCampaignFlowAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateCampaignName  **
  - **SDK client:** connectcampaignsv2
  - **IAM action:**  [connect-campaigns:UpdateCampaignName](#list_connect-outbound-campaigns-action-UpdateCampaignName) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateCampaignSchedule  **
  - **SDK client:** connectcampaignsv2
  - **IAM action:**  [connect-campaigns:UpdateCampaignSchedule](#list_connect-outbound-campaigns-action-UpdateCampaignSchedule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateCampaignSource  **
  - **SDK client:** connectcampaignsv2
  - **IAM action:**  [connect-campaigns:UpdateCampaignSource](#list_connect-outbound-campaigns-action-UpdateCampaignSource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon Connect Outbound Campaigns
<a name="list_connect-outbound-campaigns-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateCampaign](https://docs.aws.amazon.com/connect/latest/adminguide/enable-outbound-campaigns.html)  **
  - **Description:** Grants permission to create a campaign
  - **Resource types (\*required):** [campaign\*](#list_connect-outbound-campaigns-resource-campaign)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_connect-outbound-campaigns-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_connect-outbound-campaigns-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_connect-outbound-campaigns-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteCampaign](https://docs.aws.amazon.com/connect/latest/adminguide/enable-outbound-campaigns.html)  **
  - **Description:** Grants permission to delete a campaign
  - **Resource types (\*required):** [campaign\*](#list_connect-outbound-campaigns-resource-campaign)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connect-outbound-campaigns-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCampaignChannelSubtypeConfig](https://docs.aws.amazon.com/connect/latest/adminguide/enable-outbound-campaigns.html)  **
  - **Description:** Grants permission to delete the channel subtype configuration of a campaign
  - **Resource types (\*required):** [campaign\*](#list_connect-outbound-campaigns-resource-campaign)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connect-outbound-campaigns-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCampaignCommunicationLimits](https://docs.aws.amazon.com/connect/latest/adminguide/enable-outbound-campaigns.html)  **
  - **Description:** Grants permission to delete the communication limits configuration of a campaign
  - **Resource types (\*required):** [campaign\*](#list_connect-outbound-campaigns-resource-campaign)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connect-outbound-campaigns-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCampaignCommunicationTime](https://docs.aws.amazon.com/connect/latest/adminguide/enable-outbound-campaigns.html)  **
  - **Description:** Grants permission to delete the communication time configuration of a campaign
  - **Resource types (\*required):** [campaign\*](#list_connect-outbound-campaigns-resource-campaign)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connect-outbound-campaigns-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCampaignEntryLimits](https://docs.aws.amazon.com/connect/latest/adminguide/enable-outbound-campaigns.html)  **
  - **Description:** Grants permission to delete the entry limits configuration of a campaign
  - **Resource types (\*required):** [campaign\*](#list_connect-outbound-campaigns-resource-campaign)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connect-outbound-campaigns-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteConnectInstanceConfig](https://docs.aws.amazon.com/connect/latest/adminguide/enable-outbound-campaigns.html)  **
  - **Description:** Grants permission to remove configuration information for an Amazon Connect instance
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteConnectInstanceIntegration](https://docs.aws.amazon.com/connect/latest/adminguide/enable-outbound-campaigns.html)  **
  - **Description:** Grants permission to remove integration information for an Amazon Connect instance
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteInstanceOnboardingJob](https://docs.aws.amazon.com/connect/latest/adminguide/enable-outbound-campaigns.html)  **
  - **Description:** Grants permission to remove onboarding job for an Amazon Connect instance
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DescribeCampaign](https://docs.aws.amazon.com/connect/latest/adminguide/enable-outbound-campaigns.html)  **
  - **Description:** Grants permission to describe a specific campaign
  - **Resource types (\*required):** [campaign\*](#list_connect-outbound-campaigns-resource-campaign)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_connect-outbound-campaigns-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_connect-outbound-campaigns-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCampaignState](https://docs.aws.amazon.com/connect/latest/adminguide/enable-outbound-campaigns.html)  **
  - **Description:** Grants permission to get state of a campaign
  - **Resource types (\*required):** [campaign\*](#list_connect-outbound-campaigns-resource-campaign)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_connect-outbound-campaigns-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_connect-outbound-campaigns-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCampaignStateBatch](https://docs.aws.amazon.com/connect/latest/adminguide/enable-outbound-campaigns.html)  **
  - **Description:** Grants permission to get state of campaigns
  - **Resource types (\*required):** [campaign\*](#list_connect-outbound-campaigns-resource-campaign)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_connect-outbound-campaigns-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_connect-outbound-campaigns-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetConnectInstanceConfig](https://docs.aws.amazon.com/connect/latest/adminguide/enable-outbound-campaigns.html)  **
  - **Description:** Grants permission to get configuration information for an Amazon Connect instance
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetInstanceCommunicationLimits](https://docs.aws.amazon.com/connect/latest/adminguide/enable-outbound-campaigns.html)  **
  - **Description:** Grants permission to get the communication limits configuration of an Amazon Connect instance
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetInstanceOnboardingJobStatus](https://docs.aws.amazon.com/connect/latest/adminguide/enable-outbound-campaigns.html)  **
  - **Description:** Grants permission to get onboarding job status for an Amazon Connect instance
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListCampaigns](https://docs.aws.amazon.com/connect/latest/adminguide/enable-outbound-campaigns.html)  **
  - **Description:** Grants permission to provide summary of all campaigns
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_connect-outbound-campaigns-aws_RequestTag___TagKey_)
  - **Access level:** List

- **   [ListConnectInstanceIntegrations](https://docs.aws.amazon.com/connect/latest/adminguide/enable-outbound-campaigns.html)  **
  - **Description:** Grants permission to provide summary of all integrations with an Amazon Connect instance
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/connect/latest/adminguide/enable-outbound-campaigns.html)  **
  - **Description:** Grants permission to list tags for a resource
  - **Resource types (\*required):** [campaign](#list_connect-outbound-campaigns-resource-campaign)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connect-outbound-campaigns-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PauseCampaign](https://docs.aws.amazon.com/connect/latest/adminguide/enable-outbound-campaigns.html)  **
  - **Description:** Grants permission to pause a campaign
  - **Resource types (\*required):** [campaign\*](#list_connect-outbound-campaigns-resource-campaign)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connect-outbound-campaigns-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutConnectInstanceIntegration](https://docs.aws.amazon.com/connect/latest/adminguide/enable-outbound-campaigns.html)  **
  - **Description:** Grants permission to put an integration configuration with an Amazon Connect instance
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutDialRequestBatch](https://docs.aws.amazon.com/connect/latest/adminguide/enable-outbound-campaigns.html)  **
  - **Description:** Grants permission to create dial requests for the specified campaign
  - **Resource types (\*required):** [campaign\*](#list_connect-outbound-campaigns-resource-campaign)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connect-outbound-campaigns-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutInstanceCommunicationLimits](https://docs.aws.amazon.com/connect/latest/adminguide/enable-outbound-campaigns.html)  **
  - **Description:** Grants permission to put the communication limits configuration of an Amazon Connect instance
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutOutboundRequestBatch](https://docs.aws.amazon.com/connect/latest/adminguide/enable-outbound-campaigns.html)  **
  - **Description:** Grants permission to create dial requests for the specified campaign
  - **Resource types (\*required):** [campaign\*](#list_connect-outbound-campaigns-resource-campaign)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connect-outbound-campaigns-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutProfileOutboundRequestBatch](https://docs.aws.amazon.com/connect/latest/adminguide/enable-outbound-campaigns.html)  **
  - **Description:** Grants permission to create profile outbound requests for the specified campaign
  - **Resource types (\*required):** [campaign\*](#list_connect-outbound-campaigns-resource-campaign)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connect-outbound-campaigns-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ResumeCampaign](https://docs.aws.amazon.com/connect/latest/adminguide/enable-outbound-campaigns.html)  **
  - **Description:** Grants permission to resume a campaign
  - **Resource types (\*required):** [campaign\*](#list_connect-outbound-campaigns-resource-campaign)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connect-outbound-campaigns-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartCampaign](https://docs.aws.amazon.com/connect/latest/adminguide/enable-outbound-campaigns.html)  **
  - **Description:** Grants permission to start a campaign
  - **Resource types (\*required):** [campaign\*](#list_connect-outbound-campaigns-resource-campaign)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connect-outbound-campaigns-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartInstanceOnboardingJob](https://docs.aws.amazon.com/connect/latest/adminguide/enable-outbound-campaigns.html)  **
  - **Description:** Grants permission to start onboarding job for an Amazon Connect instance
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StopCampaign](https://docs.aws.amazon.com/connect/latest/adminguide/enable-outbound-campaigns.html)  **
  - **Description:** Grants permission to stop a campaign
  - **Resource types (\*required):** [campaign\*](#list_connect-outbound-campaigns-resource-campaign)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connect-outbound-campaigns-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/connect/latest/adminguide/enable-outbound-campaigns.html)  **
  - **Description:** Grants permission to tag a resource
  - **Resource types (\*required):** [campaign\*](#list_connect-outbound-campaigns-resource-campaign)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_connect-outbound-campaigns-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_connect-outbound-campaigns-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_connect-outbound-campaigns-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/connect/latest/adminguide/enable-outbound-campaigns.html)  **
  - **Description:** Grants permission to untag a resource
  - **Resource types (\*required):** [campaign\*](#list_connect-outbound-campaigns-resource-campaign)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connect-outbound-campaigns-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_connect-outbound-campaigns-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateCampaignChannelSubtypeConfig](https://docs.aws.amazon.com/connect/latest/adminguide/enable-outbound-campaigns.html)  **
  - **Description:** Grants permission to update the channel subtype configuration of a campaign
  - **Resource types (\*required):** [campaign\*](#list_connect-outbound-campaigns-resource-campaign)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connect-outbound-campaigns-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateCampaignCommunicationLimits](https://docs.aws.amazon.com/connect/latest/adminguide/enable-outbound-campaigns.html)  **
  - **Description:** Grants permission to update the communication limits configuration of a campaign
  - **Resource types (\*required):** [campaign\*](#list_connect-outbound-campaigns-resource-campaign)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connect-outbound-campaigns-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateCampaignCommunicationTime](https://docs.aws.amazon.com/connect/latest/adminguide/enable-outbound-campaigns.html)  **
  - **Description:** Grants permission to update the communication time configuration of a campaign
  - **Resource types (\*required):** [campaign\*](#list_connect-outbound-campaigns-resource-campaign)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connect-outbound-campaigns-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateCampaignDialerConfig](https://docs.aws.amazon.com/connect/latest/adminguide/enable-outbound-campaigns.html)  **
  - **Description:** Grants permission to update the dialer configuration of a campaign
  - **Resource types (\*required):** [campaign\*](#list_connect-outbound-campaigns-resource-campaign)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connect-outbound-campaigns-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateCampaignEntryLimits](https://docs.aws.amazon.com/connect/latest/adminguide/enable-outbound-campaigns.html)  **
  - **Description:** Grants permission to update the entry limits configuration of a campaign
  - **Resource types (\*required):** [campaign\*](#list_connect-outbound-campaigns-resource-campaign)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connect-outbound-campaigns-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateCampaignFlowAssociation](https://docs.aws.amazon.com/connect/latest/adminguide/enable-outbound-campaigns.html)  **
  - **Description:** Grants permission to update the flow association of a campaign
  - **Resource types (\*required):** [campaign\*](#list_connect-outbound-campaigns-resource-campaign)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connect-outbound-campaigns-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateCampaignName](https://docs.aws.amazon.com/connect/latest/adminguide/enable-outbound-campaigns.html)  **
  - **Description:** Grants permission to update the name of a campaign
  - **Resource types (\*required):** [campaign\*](#list_connect-outbound-campaigns-resource-campaign)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connect-outbound-campaigns-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateCampaignOutboundCallConfig](https://docs.aws.amazon.com/connect/latest/adminguide/enable-outbound-campaigns.html)  **
  - **Description:** Grants permission to update the outbound call configuration of a campaign
  - **Resource types (\*required):** [campaign\*](#list_connect-outbound-campaigns-resource-campaign)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connect-outbound-campaigns-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateCampaignSchedule](https://docs.aws.amazon.com/connect/latest/adminguide/enable-outbound-campaigns.html)  **
  - **Description:** Grants permission to update the schedule of a campaign
  - **Resource types (\*required):** [campaign\*](#list_connect-outbound-campaigns-resource-campaign)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connect-outbound-campaigns-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateCampaignSource](https://docs.aws.amazon.com/connect/latest/adminguide/enable-outbound-campaigns.html)  **
  - **Description:** Grants permission to update the source of a campaign
  - **Resource types (\*required):** [campaign\*](#list_connect-outbound-campaigns-resource-campaign)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connect-outbound-campaigns-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon Connect Outbound Campaigns
<a name="list_connect-outbound-campaigns-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [campaign](https://docs.aws.amazon.com/connect/latest/adminguide/enable-outbound-campaigns.html)  | arn:${Partition}:connect-campaigns:${Region}:${Account}:campaign/${CampaignId} | [aws:ResourceTag/${TagKey}](#list_connect-outbound-campaigns-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon Connect Outbound Campaigns
<a name="list_connect-outbound-campaigns-policy-keys"></a>

Amazon Connect Outbound Campaigns defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by actions based on the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by actions based on tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by actions based on the presence of tag keys in the request | ArrayOfString | 