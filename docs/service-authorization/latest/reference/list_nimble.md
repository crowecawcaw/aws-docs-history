

# Actions, resources, and condition keys for Amazon Nimble Studio
<a name="list_nimble"></a>

Amazon Nimble Studio (service prefix: `nimble`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/nimble-studio/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/nimble-studio/latest/userguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/nimble/nimble.json) for this service.

**Topics**
+ [Actions defined by Amazon Nimble Studio](#list_nimble-actions-as-permissions)
+ [Permission-only actions for Amazon Nimble Studio](#list_nimble-permission-only-actions)
+ [Resource types defined by Amazon Nimble Studio](#list_nimble-resources-for-iam-policies)
+ [Condition keys for Amazon Nimble Studio](#list_nimble-policy-keys)

## Actions defined by Amazon Nimble Studio
<a name="list_nimble-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AcceptEulas](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_AcceptEulas.html)  **
  - **Description:** Grants permission to accept EULAs
  - **Resource types (\*required):** [eula\*](#list_nimble-resource-eula)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateLaunchProfile](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_CreateLaunchProfile.html)  **
  - **Description:** Grants permission to create a launch profile
  - **Resource types (\*required):** [studio\*](#list_nimble-resource-studio)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:studioId](#list_nimble-nimble_studioId)
  - **Access level:** Write

- **   [CreateStreamingImage](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_CreateStreamingImage.html)  **
  - **Description:** Grants permission to create a streaming image
  - **Resource types (\*required):** [studio\*](#list_nimble-resource-studio)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:studioId](#list_nimble-nimble_studioId)
  - **Access level:** Write

- **   [CreateStreamingSession](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_CreateStreamingSession.html)  **
  - **Description:** Grants permission to create a streaming session
  - **Resource types (\*required):** [launch-profile\*](#list_nimble-resource-launch-profile)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:studioId](#list_nimble-nimble_studioId)
  - **Access level:** Write

- **   [CreateStreamingSessionStream](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_CreateStreamingSessionStream.html)  **
  - **Description:** Grants permission to create a StreamingSessionStream
  - **Resource types (\*required):** [streaming-session\*](#list_nimble-resource-streaming-session)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:createdBy](#list_nimble-nimble_createdBy)<br />[nimble:ownedBy](#list_nimble-nimble_ownedBy)<br />[nimble:requesterPrincipalId](#list_nimble-nimble_requesterPrincipalId)
  - **Access level:** Write

- **   [CreateStudio](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_CreateStudio.html)  **
  - **Description:** Grants permission to create a studio
  - **Resource types (\*required):** [studio\*](#list_nimble-resource-studio)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:studioId](#list_nimble-nimble_studioId)
  - **Access level:** Write

- **   [CreateStudioComponent](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_CreateStudioComponent.html)  **
  - **Description:** Grants permission to create a studio component. A studio component designates a network resource to which a launch profile will provide access
  - **Resource types (\*required):** [studio\*](#list_nimble-resource-studio)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:studioId](#list_nimble-nimble_studioId)
  - **Access level:** Write

- **   [DeleteLaunchProfile](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_DeleteLaunchProfile.html)  **
  - **Description:** Grants permission to delete a launch profile
  - **Resource types (\*required):** [launch-profile\*](#list_nimble-resource-launch-profile)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:studioId](#list_nimble-nimble_studioId)
  - **Access level:** Write

- **   [DeleteLaunchProfileMember](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_DeleteLaunchProfileMember.html)  **
  - **Description:** Grants permission to delete a launch profile member
  - **Resource types (\*required):** [launch-profile\*](#list_nimble-resource-launch-profile)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:studioId](#list_nimble-nimble_studioId)
  - **Access level:** Write

- **   [DeleteStreamingImage](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_DeleteStreamingImage.html)  **
  - **Description:** Grants permission to delete a streaming image
  - **Resource types (\*required):** [streaming-image\*](#list_nimble-resource-streaming-image)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:studioId](#list_nimble-nimble_studioId)
  - **Access level:** Write

- **   [DeleteStreamingSession](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_DeleteStreamingSession.html)  **
  - **Description:** Grants permission to delete a streaming session
  - **Resource types (\*required):** [streaming-session\*](#list_nimble-resource-streaming-session)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:createdBy](#list_nimble-nimble_createdBy)<br />[nimble:ownedBy](#list_nimble-nimble_ownedBy)<br />[nimble:requesterPrincipalId](#list_nimble-nimble_requesterPrincipalId)
  - **Access level:** Write

- **   [DeleteStudio](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_DeleteStudio.html)  **
  - **Description:** Grants permission to delete a studio
  - **Resource types (\*required):** [studio\*](#list_nimble-resource-studio)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:studioId](#list_nimble-nimble_studioId)
  - **Access level:** Write

- **   [DeleteStudioComponent](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_DeleteStudioComponent.html)  **
  - **Description:** Grants permission to delete a studio component
  - **Resource types (\*required):** [studio-component\*](#list_nimble-resource-studio-component)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:studioId](#list_nimble-nimble_studioId)
  - **Access level:** Write

- **   [DeleteStudioMember](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_DeleteStudioMember.html)  **
  - **Description:** Grants permission to delete a studio member
  - **Resource types (\*required):** [studio\*](#list_nimble-resource-studio)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:studioId](#list_nimble-nimble_studioId)
  - **Access level:** Write

- **   [GetEula](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_GetEula.html)  **
  - **Description:** Grants permission to get a EULA
  - **Resource types (\*required):** [eula\*](#list_nimble-resource-eula)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetLaunchProfile](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_GetLaunchProfile.html)  **
  - **Description:** Grants permission to get a launch profile
  - **Resource types (\*required):** [launch-profile\*](#list_nimble-resource-launch-profile)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:studioId](#list_nimble-nimble_studioId)
  - **Access level:** Read

- **   [GetLaunchProfileDetails](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_GetLaunchProfileDetails.html)  **
  - **Description:** Grants permission to get a launch profile's details, which includes the summary of studio components and streaming images used by the launch profile
  - **Resource types (\*required):** [launch-profile\*](#list_nimble-resource-launch-profile)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:studioId](#list_nimble-nimble_studioId)
  - **Access level:** Read

- **   [GetLaunchProfileInitialization](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_GetLaunchProfileInitialization.html)  **
  - **Description:** Grants permission to get a launch profile initialization. A launch profile initialization is a dereferenced version of a launch profile, including attached studio component connection information
  - **Resource types (\*required):** [launch-profile\*](#list_nimble-resource-launch-profile)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:studioId](#list_nimble-nimble_studioId)
  - **Access level:** Read

- **   [GetLaunchProfileMember](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_GetLaunchProfileMember.html)  **
  - **Description:** Grants permission to get a launch profile member
  - **Resource types (\*required):** [launch-profile\*](#list_nimble-resource-launch-profile)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:studioId](#list_nimble-nimble_studioId)
  - **Access level:** Read

- **   [GetStreamingImage](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_GetStreamingImage.html)  **
  - **Description:** Grants permission to get a streaming image
  - **Resource types (\*required):** [streaming-image\*](#list_nimble-resource-streaming-image)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:studioId](#list_nimble-nimble_studioId)
  - **Access level:** Read

- **   [GetStreamingSession](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_GetStreamingSession.html)  **
  - **Description:** Grants permission to get a streaming session
  - **Resource types (\*required):** [streaming-session\*](#list_nimble-resource-streaming-session)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:createdBy](#list_nimble-nimble_createdBy)<br />[nimble:ownedBy](#list_nimble-nimble_ownedBy)<br />[nimble:requesterPrincipalId](#list_nimble-nimble_requesterPrincipalId)
  - **Access level:** Read

- **   [GetStreamingSessionBackup](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_GetStreamingSessionBackup.html)  **
  - **Description:** Grants permission to get a streaming session backup
  - **Resource types (\*required):** [streaming-session-backup\*](#list_nimble-resource-streaming-session-backup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:ownedBy](#list_nimble-nimble_ownedBy)<br />[nimble:requesterPrincipalId](#list_nimble-nimble_requesterPrincipalId)
  - **Access level:** Read

- **   [GetStreamingSessionStream](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_GetStreamingSessionStream.html)  **
  - **Description:** Grants permission to get a streaming session stream
  - **Resource types (\*required):** [streaming-session\*](#list_nimble-resource-streaming-session)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:createdBy](#list_nimble-nimble_createdBy)<br />[nimble:ownedBy](#list_nimble-nimble_ownedBy)<br />[nimble:requesterPrincipalId](#list_nimble-nimble_requesterPrincipalId)
  - **Access level:** Read

- **   [GetStudio](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_GetStudio.html)  **
  - **Description:** Grants permission to get a studio
  - **Resource types (\*required):** [studio\*](#list_nimble-resource-studio)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:studioId](#list_nimble-nimble_studioId)
  - **Access level:** Read

- **   [GetStudioComponent](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_GetStudioComponent.html)  **
  - **Description:** Grants permission to get a studio component
  - **Resource types (\*required):** [studio-component\*](#list_nimble-resource-studio-component)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:studioId](#list_nimble-nimble_studioId)
  - **Access level:** Read

- **   [GetStudioMember](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_GetStudioMember.html)  **
  - **Description:** Grants permission to get a studio member
  - **Resource types (\*required):** [studio\*](#list_nimble-resource-studio)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:studioId](#list_nimble-nimble_studioId)
  - **Access level:** Read

- **   [ListEulaAcceptances](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_ListEulaAcceptances.html)  **
  - **Description:** Grants permission to list EULA acceptances
  - **Resource types (\*required):** [eula-acceptance\*](#list_nimble-resource-eula-acceptance)
  - **Condition keys:** [nimble:studioId](#list_nimble-nimble_studioId)
  - **Access level:** Read

- **   [ListEulas](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_ListEulas.html)  **
  - **Description:** Grants permission to list EULAs
  - **Resource types (\*required):** [eula\*](#list_nimble-resource-eula)
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListLaunchProfileMembers](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_ListLaunchProfileMembers.html)  **
  - **Description:** Grants permission to list launch profile members
  - **Resource types (\*required):** [launch-profile\*](#list_nimble-resource-launch-profile)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:studioId](#list_nimble-nimble_studioId)
  - **Access level:** Read

- **   [ListLaunchProfiles](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_ListLaunchProfiles.html)  **
  - **Description:** Grants permission to list launch profiles
  - **Resource types (\*required):** [studio\*](#list_nimble-resource-studio)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:principalId](#list_nimble-nimble_principalId)<br />[nimble:requesterPrincipalId](#list_nimble-nimble_requesterPrincipalId)<br />[nimble:studioId](#list_nimble-nimble_studioId)
  - **Access level:** Read

- **   [ListStreamingImages](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_ListStreamingImages.html)  **
  - **Description:** Grants permission to list streaming images
  - **Resource types (\*required):** [studio\*](#list_nimble-resource-studio)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:studioId](#list_nimble-nimble_studioId)
  - **Access level:** Read

- **   [ListStreamingSessionBackups](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_ListStreamingSessionBackups.html)  **
  - **Description:** Grants permission to list streaming session backups
  - **Resource types (\*required):** [studio\*](#list_nimble-resource-studio)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:requesterPrincipalId](#list_nimble-nimble_requesterPrincipalId)<br />[nimble:studioId](#list_nimble-nimble_studioId)
  - **Access level:** Read

- **   [ListStreamingSessions](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_ListStreamingSessions.html)  **
  - **Description:** Grants permission to list streaming sessions
  - **Resource types (\*required):** [studio\*](#list_nimble-resource-studio)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:createdBy](#list_nimble-nimble_createdBy)<br />[nimble:ownedBy](#list_nimble-nimble_ownedBy)<br />[nimble:requesterPrincipalId](#list_nimble-nimble_requesterPrincipalId)<br />[nimble:studioId](#list_nimble-nimble_studioId)
  - **Access level:** Read

- **   [ListStudioComponents](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_ListStudioComponents.html)  **
  - **Description:** Grants permission to list studio components
  - **Resource types (\*required):** [studio\*](#list_nimble-resource-studio)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:studioId](#list_nimble-nimble_studioId)
  - **Access level:** Read

- **   [ListStudioMembers](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_ListStudioMembers.html)  **
  - **Description:** Grants permission to list studio members
  - **Resource types (\*required):** [studio\*](#list_nimble-resource-studio)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:studioId](#list_nimble-nimble_studioId)
  - **Access level:** Read

- **   [ListStudios](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_ListStudios.html)  **
  - **Description:** Grants permission to list all studios
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListTagsForResource](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list all tags on a Nimble Studio resource
  - **Resource types (\*required):** [launch-profile](#list_nimble-resource-launch-profile) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:studioId](#list_nimble-nimble_studioId)
  - **Resource types (\*required):** [streaming-image](#list_nimble-resource-streaming-image) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:studioId](#list_nimble-nimble_studioId)
  - **Resource types (\*required):** [streaming-session](#list_nimble-resource-streaming-session) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:createdBy](#list_nimble-nimble_createdBy)<br />[nimble:ownedBy](#list_nimble-nimble_ownedBy)
  - **Resource types (\*required):** [streaming-session-backup](#list_nimble-resource-streaming-session-backup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:ownedBy](#list_nimble-nimble_ownedBy)
  - **Resource types (\*required):** [studio](#list_nimble-resource-studio) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:studioId](#list_nimble-nimble_studioId)
  - **Resource types (\*required):** [studio-component](#list_nimble-resource-studio-component) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:studioId](#list_nimble-nimble_studioId)
  - **Access level:** Read

- **   [PutLaunchProfileMembers](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_PutLaunchProfileMembers.html)  **
  - **Description:** Grants permission to add/update launch profile members
  - **Resource types (\*required):** [launch-profile\*](#list_nimble-resource-launch-profile)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:studioId](#list_nimble-nimble_studioId)
  - **Access level:** Write

- **   [PutStudioMembers](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_PutStudioMembers.html)  **
  - **Description:** Grants permission to add/update studio members
  - **Resource types (\*required):** [studio\*](#list_nimble-resource-studio)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:studioId](#list_nimble-nimble_studioId)
  - **Access level:** Write

- **   [StartStreamingSession](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_StartStreamingSession.html)  **
  - **Description:** Grants permission to start a streaming session
  - **Resource types (\*required):** [streaming-session\*](#list_nimble-resource-streaming-session) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:createdBy](#list_nimble-nimble_createdBy)<br />[nimble:ownedBy](#list_nimble-nimble_ownedBy)<br />[nimble:requesterPrincipalId](#list_nimble-nimble_requesterPrincipalId)
  - **Resource types (\*required):** [streaming-session-backup](#list_nimble-resource-streaming-session-backup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:ownedBy](#list_nimble-nimble_ownedBy)<br />[nimble:requesterPrincipalId](#list_nimble-nimble_requesterPrincipalId)
  - **Access level:** Write

- **   [StartStudioSSOConfigurationRepair](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_StartStudioSSOConfigurationRepair.html)  **
  - **Description:** Grants permission to repair the studio's AWS IAM Identity Center configuration
  - **Resource types (\*required):** [studio\*](#list_nimble-resource-studio)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:studioId](#list_nimble-nimble_studioId)
  - **Access level:** Write

- **   [StopStreamingSession](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_StopStreamingSession.html)  **
  - **Description:** Grants permission to stop a streaming session
  - **Resource types (\*required):** [streaming-session\*](#list_nimble-resource-streaming-session)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:createdBy](#list_nimble-nimble_createdBy)<br />[nimble:ownedBy](#list_nimble-nimble_ownedBy)<br />[nimble:requesterPrincipalId](#list_nimble-nimble_requesterPrincipalId)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add or overwrite one or more tags for the specified Nimble Studio resource
  - **Resource types (\*required):** [launch-profile](#list_nimble-resource-launch-profile) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:studioId](#list_nimble-nimble_studioId)
  - **Resource types (\*required):** [streaming-image](#list_nimble-resource-streaming-image) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:studioId](#list_nimble-nimble_studioId)
  - **Resource types (\*required):** [streaming-session](#list_nimble-resource-streaming-session) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:createdBy](#list_nimble-nimble_createdBy)<br />[nimble:ownedBy](#list_nimble-nimble_ownedBy)
  - **Resource types (\*required):** [streaming-session-backup](#list_nimble-resource-streaming-session-backup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:ownedBy](#list_nimble-nimble_ownedBy)
  - **Resource types (\*required):** [studio](#list_nimble-resource-studio) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:studioId](#list_nimble-nimble_studioId)
  - **Resource types (\*required):** [studio-component](#list_nimble-resource-studio-component) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:studioId](#list_nimble-nimble_studioId)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to disassociate one or more tags from the specified Nimble Studio resource
  - **Resource types (\*required):** [launch-profile](#list_nimble-resource-launch-profile) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:studioId](#list_nimble-nimble_studioId)
  - **Resource types (\*required):** [streaming-image](#list_nimble-resource-streaming-image) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:studioId](#list_nimble-nimble_studioId)
  - **Resource types (\*required):** [streaming-session](#list_nimble-resource-streaming-session) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:createdBy](#list_nimble-nimble_createdBy)<br />[nimble:ownedBy](#list_nimble-nimble_ownedBy)
  - **Resource types (\*required):** [streaming-session-backup](#list_nimble-resource-streaming-session-backup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:ownedBy](#list_nimble-nimble_ownedBy)
  - **Resource types (\*required):** [studio](#list_nimble-resource-studio) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:studioId](#list_nimble-nimble_studioId)
  - **Resource types (\*required):** [studio-component](#list_nimble-resource-studio-component) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:studioId](#list_nimble-nimble_studioId)
  - **Access level:** Tagging, Write

- **   [UpdateLaunchProfile](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_UpdateLaunchProfile.html)  **
  - **Description:** Grants permission to update a launch profile
  - **Resource types (\*required):** [launch-profile\*](#list_nimble-resource-launch-profile)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:studioId](#list_nimble-nimble_studioId)
  - **Access level:** Write

- **   [UpdateLaunchProfileMember](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_UpdateLaunchProfileMember.html)  **
  - **Description:** Grants permission to update a launch profile member
  - **Resource types (\*required):** [launch-profile\*](#list_nimble-resource-launch-profile)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:studioId](#list_nimble-nimble_studioId)
  - **Access level:** Write

- **   [UpdateStreamingImage](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_UpdateStreamingImage.html)  **
  - **Description:** Grants permission to update a streaming image
  - **Resource types (\*required):** [streaming-image\*](#list_nimble-resource-streaming-image)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:studioId](#list_nimble-nimble_studioId)
  - **Access level:** Write

- **   [UpdateStudio](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_UpdateStudio.html)  **
  - **Description:** Grants permission to update a studio
  - **Resource types (\*required):** [studio\*](#list_nimble-resource-studio)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:studioId](#list_nimble-nimble_studioId)
  - **Access level:** Write

- **   [UpdateStudioComponent](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_UpdateStudioComponent.html)  **
  - **Description:** Grants permission to update a studio component
  - **Resource types (\*required):** [studio-component\*](#list_nimble-resource-studio-component)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:studioId](#list_nimble-nimble_studioId)
  - **Access level:** Write



## Permission-only actions for Amazon Nimble Studio
<a name="list_nimble-permission-only-actions"></a>

The following actions are defined by Amazon Nimble Studio but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [GetFeatureMap](https://docs.aws.amazon.com/nimble-studio/latest/userguide/security-iam-service-with-iam.html)  **
  - **Description:** Grants permission to allow Nimble Studio portal to show the appropriate features for this account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [PutStudioLogEvents](https://docs.aws.amazon.com/nimble-studio/latest/userguide/security-iam-service-with-iam.html)  **
  - **Description:** Grants permission to report metrics and logs for the Nimble Studio portal to monitor application health
  - **Resource types (\*required):** [studio\*](#list_nimble-resource-studio)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:studioId](#list_nimble-nimble_studioId)
  - **Access level:** Write



## Resource types defined by Amazon Nimble Studio
<a name="list_nimble-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [eula](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_Eula.html)  | arn:${Partition}:nimble:${Region}:${Account}:eula/${EulaId} |   | 
|  [eula-acceptance](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_EulaAcceptance.html)  | arn:${Partition}:nimble:${Region}:${Account}:eula-acceptance/${EulaAcceptanceId} | [nimble:studioId](#list_nimble-nimble_studioId) | 
|  [launch-profile](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_LaunchProfile.html)  | arn:${Partition}:nimble:${Region}:${Account}:launch-profile/${LaunchProfileId} | [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:studioId](#list_nimble-nimble_studioId) | 
|  [streaming-image](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_StreamingImage.html)  | arn:${Partition}:nimble:${Region}:${Account}:streaming-image/${StreamingImageId} | [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:studioId](#list_nimble-nimble_studioId) | 
|  [streaming-session](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_StreamingSession.html)  | arn:${Partition}:nimble:${Region}:${Account}:streaming-session/${StreamingSessionId} | [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:createdBy](#list_nimble-nimble_createdBy)<br />[nimble:ownedBy](#list_nimble-nimble_ownedBy) | 
|  [streaming-session-backup](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_StreamingSessionBackup.html)  | arn:${Partition}:nimble:${Region}:${Account}:streaming-session-backup/${StreamingSessionBackupId} | [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:ownedBy](#list_nimble-nimble_ownedBy) | 
|  [studio](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_Studio.html)  | arn:${Partition}:nimble:${Region}:${Account}:studio/${StudioId} | [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:studioId](#list_nimble-nimble_studioId) | 
|  [studio-component](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_StudioComponent.html)  | arn:${Partition}:nimble:${Region}:${Account}:studio-component/${StudioComponentId} | [aws:RequestTag/${TagKey}](#list_nimble-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_nimble-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_nimble-aws_TagKeys)<br />[nimble:studioId](#list_nimble-nimble_studioId) | 

## Condition keys for Amazon Nimble Studio
<a name="list_nimble-policy-keys"></a>

Amazon Nimble Studio defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by a tag key and value pair that is allowed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by a tag key and value pair of a resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by a list of tag keys that are allowed in the request | ArrayOfString | 
|   [nimble:createdBy](https://docs.aws.amazon.com/nimble-studio/latest/userguide/security-iam-service-with-iam.html)  | Filters access by the createdBy request parameter or the ID of the creator of the resource | String | 
|   [nimble:ownedBy](https://docs.aws.amazon.com/nimble-studio/latest/userguide/security-iam-service-with-iam.html)  | Filters access by the ownedBy request parameter or the ID of the owner of the resource | String | 
|   [nimble:principalId](https://docs.aws.amazon.com/nimble-studio/latest/userguide/security-iam-service-with-iam.html)  | Filters access by the principalId request parameter | String | 
|   [nimble:requesterPrincipalId](https://docs.aws.amazon.com/nimble-studio/latest/userguide/security-iam-service-with-iam.html)  | Filters access by the ID of the logged in user | String | 
|   [nimble:studioId](https://docs.aws.amazon.com/nimble-studio/latest/userguide/security-iam-service-with-iam.html)  | Filters access by a specific studio | ARN | 