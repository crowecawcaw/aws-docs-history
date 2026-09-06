

# Actions, resources, and condition keys for AWS Elemental MediaPackage V2
<a name="list_mediapackagev2"></a>

AWS Elemental MediaPackage V2 (service prefix: `mediapackagev2`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/mediapackage/latest/userguide/what-is.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/mediapackage/latest/APIReference/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/mediapackage/latest/userguide/setting-up-iam-permissions.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/mediapackagev2/mediapackagev2.json) for this service.

**Topics**
+ [API operations defined by AWS Elemental MediaPackage V2](#list_mediapackagev2-operations)
+ [Actions defined by AWS Elemental MediaPackage V2](#list_mediapackagev2-actions-as-permissions)
+ [Resource types defined by AWS Elemental MediaPackage V2](#list_mediapackagev2-resources-for-iam-policies)
+ [Condition keys for AWS Elemental MediaPackage V2](#list_mediapackagev2-policy-keys)

## API operations defined by AWS Elemental MediaPackage V2
<a name="list_mediapackagev2-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_mediapackagev2-actions-as-permissions).




- **   CancelHarvestJob  **
  - **IAM action:**  [mediapackagev2:CancelHarvestJob](#list_mediapackagev2-action-CancelHarvestJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateChannel  **
  - **IAM action:**  [mediapackagev2:CreateChannel](#list_mediapackagev2-action-CreateChannel)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mediapackagev2:TagResource](#list_mediapackagev2-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateChannelGroup  **
  - **IAM action:**  [mediapackagev2:CreateChannelGroup](#list_mediapackagev2-action-CreateChannelGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mediapackagev2:TagResource](#list_mediapackagev2-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateHarvestJob  **
  - **IAM action:**  [mediapackagev2:CreateHarvestJob](#list_mediapackagev2-action-CreateHarvestJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mediapackagev2:TagResource](#list_mediapackagev2-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateOriginEndpoint  **
  - **IAM action:**  [mediapackagev2:CreateOriginEndpoint](#list_mediapackagev2-action-CreateOriginEndpoint)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mediapackagev2:TagResource](#list_mediapackagev2-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** mediapackagev2.amazonaws.com / **Access level:** Write

- **   DeleteChannel  **
  - **IAM action:**  [mediapackagev2:DeleteChannel](#list_mediapackagev2-action-DeleteChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteChannelGroup  **
  - **IAM action:**  [mediapackagev2:DeleteChannelGroup](#list_mediapackagev2-action-DeleteChannelGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteChannelPolicy  **
  - **IAM action:**  [mediapackagev2:DeleteChannelPolicy](#list_mediapackagev2-action-DeleteChannelPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteOriginEndpoint  **
  - **IAM action:**  [mediapackagev2:DeleteOriginEndpoint](#list_mediapackagev2-action-DeleteOriginEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteOriginEndpointPolicy  **
  - **IAM action:**  [mediapackagev2:DeleteOriginEndpointPolicy](#list_mediapackagev2-action-DeleteOriginEndpointPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetChannel  **
  - **IAM action:**  [mediapackagev2:GetChannel](#list_mediapackagev2-action-GetChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetChannelGroup  **
  - **IAM action:**  [mediapackagev2:GetChannelGroup](#list_mediapackagev2-action-GetChannelGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetChannelPolicy  **
  - **IAM action:**  [mediapackagev2:GetChannelPolicy](#list_mediapackagev2-action-GetChannelPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetHarvestJob  **
  - **IAM action:**  [mediapackagev2:GetHarvestJob](#list_mediapackagev2-action-GetHarvestJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetOriginEndpoint  **
  - **IAM action:**  [mediapackagev2:GetOriginEndpoint](#list_mediapackagev2-action-GetOriginEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetOriginEndpointPolicy  **
  - **IAM action:**  [mediapackagev2:GetOriginEndpointPolicy](#list_mediapackagev2-action-GetOriginEndpointPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListChannelGroups  **
  - **IAM action:**  [mediapackagev2:ListChannelGroups](#list_mediapackagev2-action-ListChannelGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListChannels  **
  - **IAM action:**  [mediapackagev2:ListChannels](#list_mediapackagev2-action-ListChannels) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListHarvestJobs  **
  - **IAM action:**  [mediapackagev2:ListHarvestJobs](#list_mediapackagev2-action-ListHarvestJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListOriginEndpoints  **
  - **IAM action:**  [mediapackagev2:ListOriginEndpoints](#list_mediapackagev2-action-ListOriginEndpoints) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [mediapackagev2:ListTagsForResource](#list_mediapackagev2-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PutChannelPolicy  **
  - **IAM action:**  [mediapackagev2:PutChannelPolicy](#list_mediapackagev2-action-PutChannelPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutOriginEndpointPolicy  **
  - **IAM action:**  [mediapackagev2:PutOriginEndpointPolicy](#list_mediapackagev2-action-PutOriginEndpointPolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** mediapackagev2.amazonaws.com / **Access level:** Write

- **   ResetChannelState  **
  - **IAM action:**  [mediapackagev2:ResetChannelState](#list_mediapackagev2-action-ResetChannelState) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ResetOriginEndpointState  **
  - **IAM action:**  [mediapackagev2:ResetOriginEndpointState](#list_mediapackagev2-action-ResetOriginEndpointState) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [mediapackagev2:TagResource](#list_mediapackagev2-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [mediapackagev2:UntagResource](#list_mediapackagev2-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateChannel  **
  - **IAM action:**  [mediapackagev2:UpdateChannel](#list_mediapackagev2-action-UpdateChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateChannelGroup  **
  - **IAM action:**  [mediapackagev2:UpdateChannelGroup](#list_mediapackagev2-action-UpdateChannelGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateOriginEndpoint  **
  - **IAM action:**  [mediapackagev2:UpdateOriginEndpoint](#list_mediapackagev2-action-UpdateOriginEndpoint)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** mediapackagev2.amazonaws.com / **Access level:** Write



## Actions defined by AWS Elemental MediaPackage V2
<a name="list_mediapackagev2-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CancelHarvestJob](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_CancelHarvestJob.html)  **
  - **Description:** Grants permission to cancel a harvest job
  - **Resource types (\*required):** [Channel\*](#list_mediapackagev2-resource-Channel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ChannelGroup\*](#list_mediapackagev2-resource-ChannelGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [HarvestJob\*](#list_mediapackagev2-resource-HarvestJob) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [OriginEndpoint\*](#list_mediapackagev2-resource-OriginEndpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateChannel](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_CreateChannel.html)  **
  - **Description:** Grants permission to create a channel in a channel group
  - **Resource types (\*required):** [Channel\*](#list_mediapackagev2-resource-Channel) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediapackagev2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediapackagev2-aws_TagKeys)
  - **Resource types (\*required):** [ChannelGroup\*](#list_mediapackagev2-resource-ChannelGroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediapackagev2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediapackagev2-aws_TagKeys)
  - **Access level:** Write

- **   [CreateChannelGroup](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_CreateChannelGroup.html)  **
  - **Description:** Grants permission to create a channel group
  - **Resource types (\*required):** [ChannelGroup\*](#list_mediapackagev2-resource-ChannelGroup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediapackagev2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediapackagev2-aws_TagKeys)
  - **Access level:** Write

- **   [CreateHarvestJob](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_CreateHarvestJob.html)  **
  - **Description:** Grants permission to create a harvest job
  - **Resource types (\*required):** [Channel\*](#list_mediapackagev2-resource-Channel) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediapackagev2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediapackagev2-aws_TagKeys)
  - **Resource types (\*required):** [ChannelGroup\*](#list_mediapackagev2-resource-ChannelGroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediapackagev2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediapackagev2-aws_TagKeys)
  - **Resource types (\*required):** [HarvestJob\*](#list_mediapackagev2-resource-HarvestJob) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediapackagev2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediapackagev2-aws_TagKeys)
  - **Resource types (\*required):** [OriginEndpoint\*](#list_mediapackagev2-resource-OriginEndpoint) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediapackagev2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediapackagev2-aws_TagKeys)
  - **Access level:** Write

- **   [CreateOriginEndpoint](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_CreateOriginEndpoint.html)  **
  - **Description:** Grants permission to create an origin endpoint for a channel
  - **Resource types (\*required):** [Channel\*](#list_mediapackagev2-resource-Channel) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediapackagev2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediapackagev2-aws_TagKeys)
  - **Resource types (\*required):** [ChannelGroup\*](#list_mediapackagev2-resource-ChannelGroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediapackagev2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediapackagev2-aws_TagKeys)
  - **Resource types (\*required):** [OriginEndpoint\*](#list_mediapackagev2-resource-OriginEndpoint) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediapackagev2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediapackagev2-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteChannel](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_DeleteChannel.html)  **
  - **Description:** Grants permission to delete a channel in a channel group
  - **Resource types (\*required):** [Channel\*](#list_mediapackagev2-resource-Channel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ChannelGroup\*](#list_mediapackagev2-resource-ChannelGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteChannelGroup](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_DeleteChannelGroup.html)  **
  - **Description:** Grants permission to delete a channel group
  - **Resource types (\*required):** [ChannelGroup\*](#list_mediapackagev2-resource-ChannelGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteChannelPolicy](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_DeleteChannelPolicy.html)  **
  - **Description:** Grants permission to delete a resource policy from a channel
  - **Resource types (\*required):** [Channel\*](#list_mediapackagev2-resource-Channel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ChannelGroup\*](#list_mediapackagev2-resource-ChannelGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ChannelPolicy\*](#list_mediapackagev2-resource-ChannelPolicy) / **Condition keys:**  
  - **Access level:** Write

- **   [DeleteOriginEndpoint](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_DeleteOriginEndpoint.html)  **
  - **Description:** Grants permission to delete an origin endpoint of a channel
  - **Resource types (\*required):** [Channel\*](#list_mediapackagev2-resource-Channel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ChannelGroup\*](#list_mediapackagev2-resource-ChannelGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [OriginEndpoint\*](#list_mediapackagev2-resource-OriginEndpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteOriginEndpointPolicy](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_DeleteOriginEndpointPolicy.html)  **
  - **Description:** Grants permission to delete a resource policy from an origin endpoint
  - **Resource types (\*required):** [Channel\*](#list_mediapackagev2-resource-Channel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ChannelGroup\*](#list_mediapackagev2-resource-ChannelGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [OriginEndpoint\*](#list_mediapackagev2-resource-OriginEndpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [OriginEndpointPolicy\*](#list_mediapackagev2-resource-OriginEndpointPolicy) / **Condition keys:**  
  - **Access level:** Write

- **   [GetChannel](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_GetChannel.html)  **
  - **Description:** Grants permission to retrieve details of a channel in a channel group
  - **Resource types (\*required):** [Channel\*](#list_mediapackagev2-resource-Channel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ChannelGroup\*](#list_mediapackagev2-resource-ChannelGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetChannelGroup](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_GetChannelGroup.html)  **
  - **Description:** Grants permission to retrieve details of a channel group
  - **Resource types (\*required):** [ChannelGroup\*](#list_mediapackagev2-resource-ChannelGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetChannelPolicy](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_GetChannelPolicy.html)  **
  - **Description:** Grants permission to retrieve a resource policy for a channel
  - **Resource types (\*required):** [Channel\*](#list_mediapackagev2-resource-Channel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ChannelGroup\*](#list_mediapackagev2-resource-ChannelGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ChannelPolicy\*](#list_mediapackagev2-resource-ChannelPolicy) / **Condition keys:**  
  - **Access level:** Read

- **   [GetHarvestJob](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_GetHarvestJob.html)  **
  - **Description:** Grants permission to retrieve details of an harvest job
  - **Resource types (\*required):** [Channel\*](#list_mediapackagev2-resource-Channel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ChannelGroup\*](#list_mediapackagev2-resource-ChannelGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [HarvestJob\*](#list_mediapackagev2-resource-HarvestJob) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [OriginEndpoint\*](#list_mediapackagev2-resource-OriginEndpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetHeadObject](https://docs.aws.amazon.com/mediapackage/latest/userguide/dataplane-apis.html)  **
  - **Description:** Grants permission to make GetHeadObject requests to MediaPackage
  - **Resource types (\*required):** [OriginEndpoint\*](#list_mediapackagev2-resource-OriginEndpoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetObject](https://docs.aws.amazon.com/mediapackage/latest/userguide/dataplane-apis.html)  **
  - **Description:** Grants permission to make GetObject requests to MediaPackage
  - **Resource types (\*required):** [OriginEndpoint\*](#list_mediapackagev2-resource-OriginEndpoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetOriginEndpoint](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_GetOriginEndpoint.html)  **
  - **Description:** Grants permission to retrieve details of an origin endpoint
  - **Resource types (\*required):** [Channel\*](#list_mediapackagev2-resource-Channel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ChannelGroup\*](#list_mediapackagev2-resource-ChannelGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [OriginEndpoint\*](#list_mediapackagev2-resource-OriginEndpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetOriginEndpointPolicy](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_GetOriginEndpointPolicy.html)  **
  - **Description:** Grants permission to retrieve details of a resource policy for an origin endpoint
  - **Resource types (\*required):** [Channel\*](#list_mediapackagev2-resource-Channel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ChannelGroup\*](#list_mediapackagev2-resource-ChannelGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [OriginEndpoint\*](#list_mediapackagev2-resource-OriginEndpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [OriginEndpointPolicy\*](#list_mediapackagev2-resource-OriginEndpointPolicy) / **Condition keys:**  
  - **Access level:** Read

- **   [HarvestObject](https://docs.aws.amazon.com/mediapackage/latest/userguide/dataplane-apis.html)  **
  - **Description:** Grants permission to make HarvestObject requests to MediaPackage
  - **Resource types (\*required):** [OriginEndpoint\*](#list_mediapackagev2-resource-OriginEndpoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListChannelGroups](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_ListChannelGroups.html)  **
  - **Description:** Grants permission to list all channel groups for an aws account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListChannels](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_ListChannels.html)  **
  - **Description:** Grants permission to list all channels in a channel group
  - **Resource types (\*required):** [ChannelGroup\*](#list_mediapackagev2-resource-ChannelGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListHarvestJobs](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_ListHarvestJobs.html)  **
  - **Description:** Grants permission to list all harvest jobs in a channel group, channel, origin endpoint
  - **Resource types (\*required):** [ChannelGroup\*](#list_mediapackagev2-resource-ChannelGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListOriginEndpoints](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_ListOriginEndpoints.html)  **
  - **Description:** Grants permission to list all origin endpoints of a channel
  - **Resource types (\*required):** [Channel\*](#list_mediapackagev2-resource-Channel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ChannelGroup\*](#list_mediapackagev2-resource-ChannelGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for the specified resource
  - **Resource types (\*required):** [Channel](#list_mediapackagev2-resource-Channel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ChannelGroup](#list_mediapackagev2-resource-ChannelGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [HarvestJob](#list_mediapackagev2-resource-HarvestJob) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [OriginEndpoint](#list_mediapackagev2-resource-OriginEndpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PutChannelPolicy](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_PutChannelPolicy.html)  **
  - **Description:** Grants permission to attach a resource policy for a channel
  - **Resource types (\*required):** [Channel\*](#list_mediapackagev2-resource-Channel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ChannelGroup\*](#list_mediapackagev2-resource-ChannelGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ChannelPolicy\*](#list_mediapackagev2-resource-ChannelPolicy) / **Condition keys:**  
  - **Access level:** Write

- **   [PutObject](https://docs.aws.amazon.com/mediapackage/latest/userguide/dataplane-apis.html)  **
  - **Description:** Grants permission to make PutObject requests to MediaPackage
  - **Resource types (\*required):** [Channel\*](#list_mediapackagev2-resource-Channel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutOriginEndpointPolicy](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_PutOriginEndpointPolicy.html)  **
  - **Description:** Grants permission to attach a resource policy to an origin endpoint
  - **Resource types (\*required):** [Channel\*](#list_mediapackagev2-resource-Channel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ChannelGroup\*](#list_mediapackagev2-resource-ChannelGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [OriginEndpoint\*](#list_mediapackagev2-resource-OriginEndpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [OriginEndpointPolicy\*](#list_mediapackagev2-resource-OriginEndpointPolicy) / **Condition keys:**  
  - **Access level:** Write

- **   [ResetChannelState](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_ResetChannelState.html)  **
  - **Description:** Grants permission to reset a channel
  - **Resource types (\*required):** [Channel\*](#list_mediapackagev2-resource-Channel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ChannelGroup\*](#list_mediapackagev2-resource-ChannelGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ResetOriginEndpointState](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_ResetOriginEndpointState.html)  **
  - **Description:** Grants permission to reset an origin endpoint
  - **Resource types (\*required):** [Channel\*](#list_mediapackagev2-resource-Channel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ChannelGroup\*](#list_mediapackagev2-resource-ChannelGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [OriginEndpoint\*](#list_mediapackagev2-resource-OriginEndpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add specified tags to the specified resource
  - **Resource types (\*required):** [Channel](#list_mediapackagev2-resource-Channel) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediapackagev2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediapackagev2-aws_TagKeys)
  - **Resource types (\*required):** [ChannelGroup](#list_mediapackagev2-resource-ChannelGroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediapackagev2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediapackagev2-aws_TagKeys)
  - **Resource types (\*required):** [HarvestJob](#list_mediapackagev2-resource-HarvestJob) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediapackagev2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediapackagev2-aws_TagKeys)
  - **Resource types (\*required):** [OriginEndpoint](#list_mediapackagev2-resource-OriginEndpoint) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediapackagev2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediapackagev2-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove the specified tags from the specified resource
  - **Resource types (\*required):** [Channel](#list_mediapackagev2-resource-Channel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediapackagev2-aws_TagKeys)
  - **Resource types (\*required):** [ChannelGroup](#list_mediapackagev2-resource-ChannelGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediapackagev2-aws_TagKeys)
  - **Resource types (\*required):** [HarvestJob](#list_mediapackagev2-resource-HarvestJob) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediapackagev2-aws_TagKeys)
  - **Resource types (\*required):** [OriginEndpoint](#list_mediapackagev2-resource-OriginEndpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediapackagev2-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateChannel](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_UpdateChannel.html)  **
  - **Description:** Grants permission to update a channel in a channel group
  - **Resource types (\*required):** [Channel\*](#list_mediapackagev2-resource-Channel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ChannelGroup\*](#list_mediapackagev2-resource-ChannelGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateChannelGroup](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_UpdateChannelGroup.html)  **
  - **Description:** Grants permission to update a channel group
  - **Resource types (\*required):** [ChannelGroup\*](#list_mediapackagev2-resource-ChannelGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateOriginEndpoint](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_UpdateOriginEndpoint.html)  **
  - **Description:** Grants permission to update an origin endpoint of a channel
  - **Resource types (\*required):** [Channel\*](#list_mediapackagev2-resource-Channel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ChannelGroup\*](#list_mediapackagev2-resource-ChannelGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [OriginEndpoint\*](#list_mediapackagev2-resource-OriginEndpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS Elemental MediaPackage V2
<a name="list_mediapackagev2-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [Channel](https://docs.aws.amazon.com/mediapackage/latest/userguide/channels.html)  | arn:${Partition}:mediapackagev2:${Region}:${Account}:channelGroup/${ChannelGroupName}/channel/${ChannelName} | [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_) | 
|  [ChannelGroup](https://docs.aws.amazon.com/mediapackage/latest/userguide/channel-groups.html)  | arn:${Partition}:mediapackagev2:${Region}:${Account}:channelGroup/${ChannelGroupName} | [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_) | 
|  [ChannelPolicy](https://docs.aws.amazon.com/mediapackage/latest/userguide/API_GetChannelPolicy.html)  | arn:${Partition}:mediapackagev2:${Region}:${Account}:channelGroup/${ChannelGroupName}/channel/${ChannelName} |   | 
|  [HarvestJob](https://docs.aws.amazon.com/mediapackage/latest/userguide/API_HarvestJobListConfiguration.html)  | arn:${Partition}:mediapackagev2:${Region}:${Account}:channelGroup/${ChannelGroupName}/channel/${ChannelName}/originEndpoint/${OriginEndpointName}/harvestJob/${HarvestJobName} | [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_) | 
|  [OriginEndpoint](https://docs.aws.amazon.com/mediapackage/latest/userguide/endpoints.html)  | arn:${Partition}:mediapackagev2:${Region}:${Account}:channelGroup/${ChannelGroupName}/channel/${ChannelName}/originEndpoint/${OriginEndpointName} | [aws:ResourceTag/${TagKey}](#list_mediapackagev2-aws_ResourceTag___TagKey_) | 
|  [OriginEndpointPolicy](https://docs.aws.amazon.com/mediapackage/latest/userguide/API_GetOriginEndpointPolicy.html)  | arn:${Partition}:mediapackagev2:${Region}:${Account}:channelGroup/${ChannelGroupName}/channel/${ChannelName}/originEndpoint/${OriginEndpointName} |   | 

## Condition keys for AWS Elemental MediaPackage V2
<a name="list_mediapackagev2-policy-keys"></a>

AWS Elemental MediaPackage V2 defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by tag keys that are passed in the request | ArrayOfString | 