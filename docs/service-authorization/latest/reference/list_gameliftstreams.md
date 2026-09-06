

# Actions, resources, and condition keys for Amazon GameLift Streams
<a name="list_gameliftstreams"></a>

Amazon GameLift Streams (service prefix: `gameliftstreams`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/security_iam_service-with-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/gameliftstreams/gameliftstreams.json) for this service.

**Topics**
+ [API operations defined by Amazon GameLift Streams](#list_gameliftstreams-operations)
+ [Actions defined by Amazon GameLift Streams](#list_gameliftstreams-actions-as-permissions)
+ [Resource types defined by Amazon GameLift Streams](#list_gameliftstreams-resources-for-iam-policies)
+ [Condition keys for Amazon GameLift Streams](#list_gameliftstreams-policy-keys)

## API operations defined by Amazon GameLift Streams
<a name="list_gameliftstreams-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_gameliftstreams-actions-as-permissions).




- **   AddStreamGroupLocations  **
  - **IAM action:**  [gameliftstreams:AddStreamGroupLocations](#list_gameliftstreams-action-AddStreamGroupLocations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateApplications  **
  - **IAM action:**  [gameliftstreams:AssociateApplications](#list_gameliftstreams-action-AssociateApplications) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateApplication  **
  - **IAM action:**  [gameliftstreams:CreateApplication](#list_gameliftstreams-action-CreateApplication)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [gameliftstreams:TagResource](#list_gameliftstreams-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateStreamGroup  **
  - **IAM action:**  [gameliftstreams:AssociateApplications](#list_gameliftstreams-action-AssociateApplications)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [gameliftstreams:CreateStreamGroup](#list_gameliftstreams-action-CreateStreamGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [gameliftstreams:TagResource](#list_gameliftstreams-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateStreamSessionAdminShell  **
  - **IAM action:**  [gameliftstreams:CreateStreamSessionAdminShell](#list_gameliftstreams-action-CreateStreamSessionAdminShell) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateStreamSessionConnection  **
  - **IAM action:**  [gameliftstreams:CreateStreamSessionConnection](#list_gameliftstreams-action-CreateStreamSessionConnection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteApplication  **
  - **IAM action:**  [gameliftstreams:DeleteApplication](#list_gameliftstreams-action-DeleteApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteStreamGroup  **
  - **IAM action:**  [gameliftstreams:DeleteStreamGroup](#list_gameliftstreams-action-DeleteStreamGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateApplications  **
  - **IAM action:**  [gameliftstreams:DisassociateApplications](#list_gameliftstreams-action-DisassociateApplications) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ExportStreamSessionFiles  **
  - **IAM action:**  [gameliftstreams:ExportStreamSessionFiles](#list_gameliftstreams-action-ExportStreamSessionFiles) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetApplication  **
  - **IAM action:**  [gameliftstreams:GetApplication](#list_gameliftstreams-action-GetApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetStreamGroup  **
  - **IAM action:**  [gameliftstreams:GetStreamGroup](#list_gameliftstreams-action-GetStreamGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetStreamSession  **
  - **IAM action:**  [gameliftstreams:GetStreamSession](#list_gameliftstreams-action-GetStreamSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetStreamUrl  **
  - **IAM action:**  [gameliftstreams:GetStreamUrl](#list_gameliftstreams-action-GetStreamUrl) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListApplicationShaderCaches  **
  - **IAM action:**  [gameliftstreams:ListApplicationShaderCaches](#list_gameliftstreams-action-ListApplicationShaderCaches) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListApplications  **
  - **IAM action:**  [gameliftstreams:ListApplications](#list_gameliftstreams-action-ListApplications) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListStreamGroups  **
  - **IAM action:**  [gameliftstreams:ListStreamGroups](#list_gameliftstreams-action-ListStreamGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListStreamSessions  **
  - **IAM action:**  [gameliftstreams:ListStreamSessions](#list_gameliftstreams-action-ListStreamSessions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListStreamSessionsByAccount  **
  - **IAM action:**  [gameliftstreams:ListStreamSessionsByAccount](#list_gameliftstreams-action-ListStreamSessionsByAccount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListStreamUrls  **
  - **IAM action:**  [gameliftstreams:ListStreamUrls](#list_gameliftstreams-action-ListStreamUrls) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [gameliftstreams:ListTagsForResource](#list_gameliftstreams-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   RemoveStreamGroupLocations  **
  - **IAM action:**  [gameliftstreams:RemoveStreamGroupLocations](#list_gameliftstreams-action-RemoveStreamGroupLocations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RevokeStreamUrl  **
  - **IAM action:**  [gameliftstreams:RevokeStreamUrl](#list_gameliftstreams-action-RevokeStreamUrl) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartStreamSession  **
  - **IAM action:**  [gameliftstreams:StartStreamSession](#list_gameliftstreams-action-StartStreamSession)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** gameliftstreams.amazonaws.com / **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [gameliftstreams:TagResource](#list_gameliftstreams-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   TerminateStreamSession  **
  - **IAM action:**  [gameliftstreams:TerminateStreamSession](#list_gameliftstreams-action-TerminateStreamSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UntagResource  **
  - **IAM action:**  [gameliftstreams:UntagResource](#list_gameliftstreams-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateApplication  **
  - **IAM action:**  [gameliftstreams:UpdateApplication](#list_gameliftstreams-action-UpdateApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateStreamGroup  **
  - **IAM action:**  [gameliftstreams:UpdateStreamGroup](#list_gameliftstreams-action-UpdateStreamGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon GameLift Streams
<a name="list_gameliftstreams-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AddStreamGroupLocations](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_AddStreamGroupLocations.html)  **
  - **Description:** Grants permission to attach a StreamGroup remote location
  - **Resource types (\*required):** [stream group\*](#list_gameliftstreams-resource-streamgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gameliftstreams-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AssociateApplications](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_AssociateApplications.html)  **
  - **Description:** Grants permission to associate Applications to a StreamGroup
  - **Resource types (\*required):** [application\*](#list_gameliftstreams-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gameliftstreams-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [stream group\*](#list_gameliftstreams-resource-streamgroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gameliftstreams-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateApplication](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_CreateApplication.html)  **
  - **Description:** Grants permission to create application
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_gameliftstreams-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_gameliftstreams-aws_TagKeys)
  - **Access level:** Write

- **   [CreateStreamGroup](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_CreateStreamGroup.html)  **
  - **Description:** Grants permission to create a StreamGroup
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_gameliftstreams-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_gameliftstreams-aws_TagKeys)
  - **Access level:** Write

- **   [CreateStreamSessionAdminShell](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_CreateStreamSessionAdminShell.html)  **
  - **Description:** Grants permission to establish an administrative terminal connection to a stream session
  - **Resource types (\*required):** [stream group\*](#list_gameliftstreams-resource-streamgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gameliftstreams-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateStreamSessionConnection](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_CreateStreamSessionConnection.html)  **
  - **Description:** Grants permission to create a stream session connection
  - **Resource types (\*required):** [stream group\*](#list_gameliftstreams-resource-streamgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gameliftstreams-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateStreamUrl](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_CreateStreamUrl.html)  **
  - **Description:** Grants permission to create a stream URL
  - **Resource types (\*required):** [application\*](#list_gameliftstreams-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gameliftstreams-aws_ResourceTag___TagKey_)<br />[gameliftstreams:RoleArn](#list_gameliftstreams-gameliftstreams_RoleArn)
  - **Resource types (\*required):** [stream group\*](#list_gameliftstreams-resource-streamgroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gameliftstreams-aws_ResourceTag___TagKey_)<br />[gameliftstreams:RoleArn](#list_gameliftstreams-gameliftstreams_RoleArn)
  - **Access level:** Write

- **   [DeleteApplication](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_DeleteApplication.html)  **
  - **Description:** Grants permission to delete an application
  - **Resource types (\*required):** [application\*](#list_gameliftstreams-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gameliftstreams-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteStreamGroup](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_DeleteStreamGroup.html)  **
  - **Description:** Grants permission to delete a StreamGroup
  - **Resource types (\*required):** [stream group\*](#list_gameliftstreams-resource-streamgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gameliftstreams-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateApplications](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_DisassociateApplications.html)  **
  - **Description:** Grants permission to disassociate Applications from a StreamGroup
  - **Resource types (\*required):** [application\*](#list_gameliftstreams-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gameliftstreams-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [stream group\*](#list_gameliftstreams-resource-streamgroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gameliftstreams-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ExportStreamSessionFiles](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ExportStreamSessionFiles.html)  **
  - **Description:** Grants permission to export stream session files that your application generates
  - **Resource types (\*required):** [stream group\*](#list_gameliftstreams-resource-streamgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gameliftstreams-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetApplication](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_GetApplication.html)  **
  - **Description:** Grants permission to get an application
  - **Resource types (\*required):** [application\*](#list_gameliftstreams-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gameliftstreams-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetStreamGroup](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_GetStreamGroup.html)  **
  - **Description:** Grants `permission` to get a StreamGroup
  - **Resource types (\*required):** [stream group\*](#list_gameliftstreams-resource-streamgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gameliftstreams-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetStreamSession](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_GetStreamSession.html)  **
  - **Description:** Grants permission to get a stream session
  - **Resource types (\*required):** [stream group\*](#list_gameliftstreams-resource-streamgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gameliftstreams-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetStreamUrl](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_GetStreamUrl.html)  **
  - **Description:** Grants permission to get a stream URL
  - **Resource types (\*required):** [stream group\*](#list_gameliftstreams-resource-streamgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gameliftstreams-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListApplicationShaderCaches](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ListApplicationShaderCaches.html)  **
  - **Description:** Grants permission to list application shader caches
  - **Resource types (\*required):** [application\*](#list_gameliftstreams-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gameliftstreams-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListApplications](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ListApplications.html)  **
  - **Description:** Grants permission to list applications
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListStreamGroups](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ListStreamGroups.html)  **
  - **Description:** Grants permission to list StreamGroups
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListStreamSessions](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ListStreamSessions.html)  **
  - **Description:** Grants permission to list stream sessions
  - **Resource types (\*required):** [stream group\*](#list_gameliftstreams-resource-streamgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gameliftstreams-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListStreamSessionsByAccount](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ListStreamSessionsByAccount.html)  **
  - **Description:** Grants permission to list stream sessions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListStreamUrls](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ListStreamUrls.html)  **
  - **Description:** Grants permission to list stream URLs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a resource
  - **Resource types (\*required):** [application](#list_gameliftstreams-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gameliftstreams-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [stream group](#list_gameliftstreams-resource-streamgroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gameliftstreams-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [RemoveStreamGroupLocations](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_RemoveStreamGroupLocations.html)  **
  - **Description:** Grants permission to detach a StreamGroup remote location
  - **Resource types (\*required):** [stream group\*](#list_gameliftstreams-resource-streamgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gameliftstreams-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RevokeStreamUrl](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_RevokeStreamUrl.html)  **
  - **Description:** Grants permission to revoke a stream URL
  - **Resource types (\*required):** [stream group\*](#list_gameliftstreams-resource-streamgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gameliftstreams-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartStreamSession](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_StartStreamSession.html)  **
  - **Description:** Grants permission to create a stream session
  - **Resource types (\*required):** [stream group\*](#list_gameliftstreams-resource-streamgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gameliftstreams-aws_ResourceTag___TagKey_)<br />[gameliftstreams:RoleArn](#list_gameliftstreams-gameliftstreams_RoleArn)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_TagResource.html)  **
  - **Description:** Grants permission to tag a resource
  - **Resource types (\*required):** [application](#list_gameliftstreams-resource-application) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_gameliftstreams-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_gameliftstreams-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_gameliftstreams-aws_TagKeys)
  - **Resource types (\*required):** [stream group](#list_gameliftstreams-resource-streamgroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_gameliftstreams-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_gameliftstreams-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_gameliftstreams-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [TerminateStreamSession](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_TerminateStreamSession.html)  **
  - **Description:** Grants permission to terminate a stream session
  - **Resource types (\*required):** [stream group\*](#list_gameliftstreams-resource-streamgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gameliftstreams-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UntagResource](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_UntagResource.html)  **
  - **Description:** Grants permission to untag a resource
  - **Resource types (\*required):** [application](#list_gameliftstreams-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gameliftstreams-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_gameliftstreams-aws_TagKeys)
  - **Resource types (\*required):** [stream group](#list_gameliftstreams-resource-streamgroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gameliftstreams-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_gameliftstreams-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateApplication](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_UpdateApplication.html)  **
  - **Description:** Grants permission to update an application
  - **Resource types (\*required):** [application\*](#list_gameliftstreams-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gameliftstreams-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateStreamGroup](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_UpdateStreamGroup.html)  **
  - **Description:** Grants permission to update a StreamGroup
  - **Resource types (\*required):** [stream group\*](#list_gameliftstreams-resource-streamgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_gameliftstreams-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon GameLift Streams
<a name="list_gameliftstreams-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [application](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/applications.html)  | arn:${Partition}:gameliftstreams:${Region}:${Account}:application/${ApplicationId} | [aws:ResourceTag/${TagKey}](#list_gameliftstreams-aws_ResourceTag___TagKey_) | 
|  [stream group](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/stream-groups.html)  | arn:${Partition}:gameliftstreams:${Region}:${Account}:streamgroup/${StreamGroupId} | [aws:ResourceTag/${TagKey}](#list_gameliftstreams-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon GameLift Streams
<a name="list_gameliftstreams-policy-keys"></a>

Amazon GameLift Streams defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by a list of tag keys that are allowed in the request | ArrayOfString | 
|   [gameliftstreams:RoleArn](https://docs.aws.amazon.com/service-authorization/latest/reference/list_gameliftstreams.html#list_gameliftstreams-policy-keys)  | Filters access by the ARN of the IAM role passed to Amazon GameLift Streams to assume for the stream session | ARN | 