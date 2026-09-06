

# Actions, resources, and condition keys for AWS Elemental MediaPackage
<a name="list_mediapackage"></a>

AWS Elemental MediaPackage (service prefix: `mediapackage`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/mediapackage/latest/ug/what-is.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/mediapackage/latest/apireference/welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/mediapackage/latest/ug/setting-up.html#setting-up-create-iam-user) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/mediapackage/mediapackage.json) for this service.

**Topics**
+ [API operations defined by AWS Elemental MediaPackage](#list_mediapackage-operations)
+ [Actions defined by AWS Elemental MediaPackage](#list_mediapackage-actions-as-permissions)
+ [Resource types defined by AWS Elemental MediaPackage](#list_mediapackage-resources-for-iam-policies)
+ [Condition keys for AWS Elemental MediaPackage](#list_mediapackage-policy-keys)

## API operations defined by AWS Elemental MediaPackage
<a name="list_mediapackage-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_mediapackage-actions-as-permissions).




- **   ConfigureLogs  **
  - **IAM action:**  [mediapackage:UpdateChannel](#list_mediapackage-action-UpdateChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateChannel  **
  - **IAM action:**  [mediapackage:CreateChannel](#list_mediapackage-action-CreateChannel)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mediapackage:TagResource](#list_mediapackage-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateHarvestJob  **
  - **IAM action:**  [mediapackage:CreateHarvestJob](#list_mediapackage-action-CreateHarvestJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** mediapackage.amazonaws.com / **Access level:** Write

- **   CreateOriginEndpoint  **
  - **IAM action:**  [mediapackage:CreateOriginEndpoint](#list_mediapackage-action-CreateOriginEndpoint)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mediapackage:TagResource](#list_mediapackage-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** mediapackage.amazonaws.com / **Access level:** Write

- **   DeleteChannel  **
  - **IAM action:**  [mediapackage:DeleteChannel](#list_mediapackage-action-DeleteChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteOriginEndpoint  **
  - **IAM action:**  [mediapackage:DeleteOriginEndpoint](#list_mediapackage-action-DeleteOriginEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeChannel  **
  - **IAM action:**  [mediapackage:DescribeChannel](#list_mediapackage-action-DescribeChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeHarvestJob  **
  - **IAM action:**  [mediapackage:DescribeHarvestJob](#list_mediapackage-action-DescribeHarvestJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeOriginEndpoint  **
  - **IAM action:**  [mediapackage:DescribeOriginEndpoint](#list_mediapackage-action-DescribeOriginEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListChannels  **
  - **IAM action:**  [mediapackage:ListChannels](#list_mediapackage-action-ListChannels) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListHarvestJobs  **
  - **IAM action:**  [mediapackage:ListHarvestJobs](#list_mediapackage-action-ListHarvestJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListOriginEndpoints  **
  - **IAM action:**  [mediapackage:ListOriginEndpoints](#list_mediapackage-action-ListOriginEndpoints) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTagsForResource  **
  - **IAM action:**  [mediapackage:ListTagsForResource](#list_mediapackage-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   RotateChannelCredentials  **
  - **IAM action:**  [mediapackage:RotateChannelCredentials](#list_mediapackage-action-RotateChannelCredentials) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RotateIngestEndpointCredentials  **
  - **IAM action:**  [mediapackage:RotateIngestEndpointCredentials](#list_mediapackage-action-RotateIngestEndpointCredentials) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [mediapackage:TagResource](#list_mediapackage-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [mediapackage:UntagResource](#list_mediapackage-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateChannel  **
  - **IAM action:**  [mediapackage:UpdateChannel](#list_mediapackage-action-UpdateChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateOriginEndpoint  **
  - **IAM action:**  [mediapackage:UpdateOriginEndpoint](#list_mediapackage-action-UpdateOriginEndpoint)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** mediapackage.amazonaws.com / **Access level:** Write



## Actions defined by AWS Elemental MediaPackage
<a name="list_mediapackage-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [ConfigureLogs](https://docs.aws.amazon.com/mediapackage/latest/apireference/channels-id-configure_logs.html#channels-id-configure_logsput)  **
  - **Description:** Grants permission to configure access logs for a Channel
  - **Resource types (\*required):** [channels\*](#list_mediapackage-resource-channels)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackage-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateChannel](https://docs.aws.amazon.com/mediapackage/latest/apireference/channels.html#channelspost)  **
  - **Description:** Grants permission to create a channel in AWS Elemental MediaPackage
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediapackage-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_mediapackage-aws_TagKeys)
  - **Access level:** Write

- **   [CreateHarvestJob](https://docs.aws.amazon.com/mediapackage/latest/apireference/harvest_jobs.html#harvest_jobspost)  **
  - **Description:** Grants permission to create a harvest job in AWS Elemental MediaPackage
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediapackage-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_mediapackage-aws_TagKeys)
  - **Access level:** Write

- **   [CreateOriginEndpoint](https://docs.aws.amazon.com/mediapackage/latest/apireference/origin_endpoints.html#origin_endpointspost)  **
  - **Description:** Grants permission to create an endpoint in AWS Elemental MediaPackage
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediapackage-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_mediapackage-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteChannel](https://docs.aws.amazon.com/mediapackage/latest/apireference/channels-id.html#channels-iddelete)  **
  - **Description:** Grants permission to delete a channel in AWS Elemental MediaPackage
  - **Resource types (\*required):** [channels\*](#list_mediapackage-resource-channels)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackage-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteOriginEndpoint](https://docs.aws.amazon.com/mediapackage/latest/apireference/origin_endpoints-id.html#origin_endpoints-iddelete)  **
  - **Description:** Grants permission to delete an endpoint in AWS Elemental MediaPackage
  - **Resource types (\*required):** [origin\_endpoints\*](#list_mediapackage-resource-origin_endpoints)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackage-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeChannel](https://docs.aws.amazon.com/mediapackage/latest/apireference/channels-id.html#channels-idget)  **
  - **Description:** Grants permission to view the details of a channel in AWS Elemental MediaPackage
  - **Resource types (\*required):** [channels\*](#list_mediapackage-resource-channels)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackage-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeHarvestJob](https://docs.aws.amazon.com/mediapackage/latest/apireference/harvest_jobs-id.html#harvest_jobs-idget)  **
  - **Description:** Grants permission to view the details of a harvest job in AWS Elemental MediaPackage
  - **Resource types (\*required):** [harvest\_jobs\*](#list_mediapackage-resource-harvest_jobs)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackage-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeOriginEndpoint](https://docs.aws.amazon.com/mediapackage/latest/apireference/origin_endpoints-id.html#origin_endpoints-idget)  **
  - **Description:** Grants permission to view the details of an endpoint in AWS Elemental MediaPackage
  - **Resource types (\*required):** [origin\_endpoints\*](#list_mediapackage-resource-origin_endpoints)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackage-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListChannels](https://docs.aws.amazon.com/mediapackage/latest/apireference/channels.html#channelsget)  **
  - **Description:** Grants permission to view a list of channels in AWS Elemental MediaPackage
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListHarvestJobs](https://docs.aws.amazon.com/mediapackage/latest/apireference/harvest_jobs.html#harvest_jobsget)  **
  - **Description:** Grants permission to view a list of harvest jobs in AWS Elemental MediaPackage
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListOriginEndpoints](https://docs.aws.amazon.com/mediapackage/latest/apireference/origin_endpoints.html#origin_endpointsget)  **
  - **Description:** Grants permission to view a list of endpoints in AWS Elemental MediaPackage
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListTagsForResource](https://docs.aws.amazon.com/mediapackage/latest/apireference/tags-resource-arn.html#tags-resource-arnget)  **
  - **Description:** Grants permission to list the tags assigned to a Channel or OriginEndpoint
  - **Resource types (\*required):** [channels](#list_mediapackage-resource-channels) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackage-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [harvest\_jobs](#list_mediapackage-resource-harvest_jobs) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackage-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [origin\_endpoints](#list_mediapackage-resource-origin_endpoints) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackage-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [RotateChannelCredentials](https://docs.aws.amazon.com/mediapackage/latest/apireference/channels-id-credentials.html#channels-id-credentialsput)  **
  - **Description:** Grants permission to rotate credentials for the first IngestEndpoint of a Channel in AWS Elemental MediaPackage
  - **Resource types (\*required):** [channels\*](#list_mediapackage-resource-channels)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackage-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RotateIngestEndpointCredentials](https://docs.aws.amazon.com/mediapackage/latest/apireference/channels-id-ingest_endpoints-ingest_endpoint_id-credentials.html#channels-id-ingest_endpoints-ingest_endpoint_id-credentialsput)  **
  - **Description:** Grants permission to rotate IngestEndpoint credentials for a Channel in AWS Elemental MediaPackage
  - **Resource types (\*required):** [channels\*](#list_mediapackage-resource-channels)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackage-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/mediapackage/latest/apireference/hj-create.html)  **
  - **Description:** Grants permission to tag a MediaPackage resource
  - **Resource types (\*required):** [channels](#list_mediapackage-resource-channels) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediapackage-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mediapackage-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediapackage-aws_TagKeys)
  - **Resource types (\*required):** [harvest\_jobs](#list_mediapackage-resource-harvest_jobs) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediapackage-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mediapackage-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediapackage-aws_TagKeys)
  - **Resource types (\*required):** [origin\_endpoints](#list_mediapackage-resource-origin_endpoints) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediapackage-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mediapackage-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediapackage-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/mediapackage/latest/apireference/tags-resource-arn.html#tags-resource-arndelete)  **
  - **Description:** Grants permission to delete tags to a Channel or OriginEndpoint
  - **Resource types (\*required):** [channels](#list_mediapackage-resource-channels) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackage-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediapackage-aws_TagKeys)
  - **Resource types (\*required):** [harvest\_jobs](#list_mediapackage-resource-harvest_jobs) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackage-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediapackage-aws_TagKeys)
  - **Resource types (\*required):** [origin\_endpoints](#list_mediapackage-resource-origin_endpoints) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackage-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediapackage-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateChannel](https://docs.aws.amazon.com/mediapackage/latest/apireference/channels-id.html#channels-idput)  **
  - **Description:** Grants permission to make changes to a channel in AWS Elemental MediaPackage
  - **Resource types (\*required):** [channels\*](#list_mediapackage-resource-channels)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackage-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateOriginEndpoint](https://docs.aws.amazon.com/mediapackage/latest/apireference/origin_endpoints-id.html#origin_endpoints-idput)  **
  - **Description:** Grants permission to make changes to an endpoint in AWS Elemental MediaPackage
  - **Resource types (\*required):** [origin\_endpoints\*](#list_mediapackage-resource-origin_endpoints)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackage-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS Elemental MediaPackage
<a name="list_mediapackage-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [channels](https://docs.aws.amazon.com/mediapackage/latest/ug/channels.html)  | arn:${Partition}:mediapackage:${Region}:${Account}:channels/${ChannelIdentifier} | [aws:ResourceTag/${TagKey}](#list_mediapackage-aws_ResourceTag___TagKey_) | 
|  [harvest\_jobs](https://docs.aws.amazon.com/mediapackage/latest/ug/harvest-jobs.html)  | arn:${Partition}:mediapackage:${Region}:${Account}:harvest\_jobs/${HarvestJobIdentifier} | [aws:ResourceTag/${TagKey}](#list_mediapackage-aws_ResourceTag___TagKey_) | 
|  [origin\_endpoints](https://docs.aws.amazon.com/mediapackage/latest/ug/endpoints.html)  | arn:${Partition}:mediapackage:${Region}:${Account}:origin\_endpoints/${OriginEndpointIdentifier} | [aws:ResourceTag/${TagKey}](#list_mediapackage-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Elemental MediaPackage
<a name="list_mediapackage-policy-keys"></a>

AWS Elemental MediaPackage defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tag for a MediaPackage request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tag for a MediaPackage resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys for a MediaPackage resource or request | ArrayOfString | 