

# Actions, resources, and condition keys for Amazon Q Business
<a name="list_qbusiness"></a>

Amazon Q Business (service prefix: `qbusiness`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/amazonq/latest/api-reference/).
+ Learn how to secure this service and its resources by [using IAM](${UserGuideDocPage}security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/qbusiness/qbusiness.json) for this service.

**Topics**
+ [API operations defined by Amazon Q Business](#list_qbusiness-operations)
+ [Actions defined by Amazon Q Business](#list_qbusiness-actions-as-permissions)
+ [Permission-only actions for Amazon Q Business](#list_qbusiness-permission-only-actions)
+ [Resource types defined by Amazon Q Business](#list_qbusiness-resources-for-iam-policies)
+ [Condition keys for Amazon Q Business](#list_qbusiness-policy-keys)

## API operations defined by Amazon Q Business
<a name="list_qbusiness-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_qbusiness-actions-as-permissions).




- **   AssociatePermission  **
  - **IAM action:**  [qbusiness:AssociatePermission](#list_qbusiness-action-AssociatePermission)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [qbusiness:PutResourcePolicy](#list_qbusiness-action-PutResourcePolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   BatchDeleteDocument  **
  - **IAM action:**  [qbusiness:BatchDeleteDocument](#list_qbusiness-action-BatchDeleteDocument) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchPutDocument  **
  - **IAM action:**  [qbusiness:BatchPutDocument](#list_qbusiness-action-BatchPutDocument)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** qbusiness.amazonaws.com / **Access level:** Write

- **   CancelSubscription  **
  - **IAM action:**  [qbusiness:CancelSubscription](#list_qbusiness-action-CancelSubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   Chat  **
  - **IAM action:**  [qbusiness:Chat](#list_qbusiness-action-Chat) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ChatSync  **
  - **IAM action:**  [qbusiness:ChatSync](#list_qbusiness-action-ChatSync) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   CheckDocumentAccess  **
  - **IAM action:**  [qbusiness:CheckDocumentAccess](#list_qbusiness-action-CheckDocumentAccess) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   CreateAnonymousWebExperienceUrl  **
  - **IAM action:**  [qbusiness:CreateAnonymousWebExperienceUrl](#list_qbusiness-action-CreateAnonymousWebExperienceUrl) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateApplication  **
  - **IAM action:**  [qbusiness:CreateApplication](#list_qbusiness-action-CreateApplication)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [qbusiness:TagResource](#list_qbusiness-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** qbusiness.amazonaws.com / **Access level:** Write

- **   CreateChatResponseConfiguration  **
  - **IAM action:**  [qbusiness:CreateChatResponseConfiguration](#list_qbusiness-action-CreateChatResponseConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [qbusiness:TagResource](#list_qbusiness-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateDataAccessor  **
  - **IAM action:**  [qbusiness:CreateDataAccessor](#list_qbusiness-action-CreateDataAccessor)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [qbusiness:CreateDataAccessorWithTti](#list_qbusiness-action-CreateDataAccessorWithTti)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [qbusiness:TagResource](#list_qbusiness-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateDataSource  **
  - **IAM action:**  [qbusiness:CreateDataSource](#list_qbusiness-action-CreateDataSource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [qbusiness:DisableAclOnDataSource](#list_qbusiness-action-DisableAclOnDataSource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [qbusiness:TagResource](#list_qbusiness-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** qbusiness.amazonaws.com / **Access level:** Write

- **   CreateIndex  **
  - **IAM action:**  [qbusiness:CreateIndex](#list_qbusiness-action-CreateIndex)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [qbusiness:TagResource](#list_qbusiness-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreatePlugin  **
  - **IAM action:**  [qbusiness:CreatePlugin](#list_qbusiness-action-CreatePlugin)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [qbusiness:TagResource](#list_qbusiness-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** qbusiness.amazonaws.com / **Access level:** Write

- **   CreateRetriever  **
  - **IAM action:**  [qbusiness:CreateRetriever](#list_qbusiness-action-CreateRetriever)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [qbusiness:TagResource](#list_qbusiness-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** qbusiness.amazonaws.com / **Access level:** Write

- **   CreateSubscription  **
  - **IAM action:**  [qbusiness:CreateSubscription](#list_qbusiness-action-CreateSubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateUser  **
  - **IAM action:**  [qbusiness:CreateUser](#list_qbusiness-action-CreateUser) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateWebExperience  **
  - **IAM action:**  [qbusiness:CreateWebExperience](#list_qbusiness-action-CreateWebExperience)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [qbusiness:TagResource](#list_qbusiness-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** qbusiness.amazonaws.com / **Access level:** Write

- **   DeleteApplication  **
  - **IAM action:**  [qbusiness:DeleteApplication](#list_qbusiness-action-DeleteApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAttachment  **
  - **IAM action:**  [qbusiness:DeleteAttachment](#list_qbusiness-action-DeleteAttachment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteChatControlsConfiguration  **
  - **IAM action:**  [qbusiness:DeleteChatControlsConfiguration](#list_qbusiness-action-DeleteChatControlsConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteChatResponseConfiguration  **
  - **IAM action:**  [qbusiness:DeleteChatResponseConfiguration](#list_qbusiness-action-DeleteChatResponseConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteConversation  **
  - **IAM action:**  [qbusiness:DeleteConversation](#list_qbusiness-action-DeleteConversation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDataAccessor  **
  - **IAM action:**  [qbusiness:DeleteDataAccessor](#list_qbusiness-action-DeleteDataAccessor) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDataSource  **
  - **IAM action:**  [qbusiness:DeleteDataSource](#list_qbusiness-action-DeleteDataSource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteGroup  **
  - **IAM action:**  [qbusiness:DeleteGroup](#list_qbusiness-action-DeleteGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteIndex  **
  - **IAM action:**  [qbusiness:DeleteIndex](#list_qbusiness-action-DeleteIndex) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePlugin  **
  - **IAM action:**  [qbusiness:DeletePlugin](#list_qbusiness-action-DeletePlugin) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRetriever  **
  - **IAM action:**  [qbusiness:DeleteRetriever](#list_qbusiness-action-DeleteRetriever) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteUser  **
  - **IAM action:**  [qbusiness:DeleteUser](#list_qbusiness-action-DeleteUser) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteWebExperience  **
  - **IAM action:**  [qbusiness:DeleteWebExperience](#list_qbusiness-action-DeleteWebExperience) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociatePermission  **
  - **IAM action:**  [qbusiness:DisassociatePermission](#list_qbusiness-action-DisassociatePermission)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [qbusiness:PutResourcePolicy](#list_qbusiness-action-PutResourcePolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   GetApplication  **
  - **IAM action:**  [qbusiness:GetApplication](#list_qbusiness-action-GetApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetChatControlsConfiguration  **
  - **IAM action:**  [qbusiness:GetChatControlsConfiguration](#list_qbusiness-action-GetChatControlsConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetChatResponseConfiguration  **
  - **IAM action:**  [qbusiness:GetChatResponseConfiguration](#list_qbusiness-action-GetChatResponseConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDataAccessor  **
  - **IAM action:**  [qbusiness:GetDataAccessor](#list_qbusiness-action-GetDataAccessor) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDataSource  **
  - **IAM action:**  [qbusiness:GetDataSource](#list_qbusiness-action-GetDataSource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDocumentContent  **
  - **IAM action:**  [qbusiness:GetDocumentContent](#list_qbusiness-action-GetDocumentContent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetGroup  **
  - **IAM action:**  [qbusiness:GetGroup](#list_qbusiness-action-GetGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetIndex  **
  - **IAM action:**  [qbusiness:GetIndex](#list_qbusiness-action-GetIndex) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMedia  **
  - **IAM action:**  [qbusiness:GetMedia](#list_qbusiness-action-GetMedia) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPlugin  **
  - **IAM action:**  [qbusiness:GetPlugin](#list_qbusiness-action-GetPlugin) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPolicy  **
  - **IAM action:**  [qbusiness:GetPolicy](#list_qbusiness-action-GetPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRetriever  **
  - **IAM action:**  [qbusiness:GetRetriever](#list_qbusiness-action-GetRetriever) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetUser  **
  - **IAM action:**  [qbusiness:GetUser](#list_qbusiness-action-GetUser) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetWebExperience  **
  - **IAM action:**  [qbusiness:GetWebExperience](#list_qbusiness-action-GetWebExperience) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListApplications  **
  - **IAM action:**  [qbusiness:ListApplications](#list_qbusiness-action-ListApplications) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAttachments  **
  - **IAM action:**  [qbusiness:ListAttachments](#list_qbusiness-action-ListAttachments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListChatResponseConfigurations  **
  - **IAM action:**  [qbusiness:ListChatResponseConfigurations](#list_qbusiness-action-ListChatResponseConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListConversations  **
  - **IAM action:**  [qbusiness:ListConversations](#list_qbusiness-action-ListConversations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDataAccessors  **
  - **IAM action:**  [qbusiness:ListDataAccessors](#list_qbusiness-action-ListDataAccessors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDataSourceSyncJobs  **
  - **IAM action:**  [qbusiness:ListDataSourceSyncJobs](#list_qbusiness-action-ListDataSourceSyncJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDataSources  **
  - **IAM action:**  [qbusiness:ListDataSources](#list_qbusiness-action-ListDataSources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDocuments  **
  - **IAM action:**  [qbusiness:ListDocuments](#list_qbusiness-action-ListDocuments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListGroups  **
  - **IAM action:**  [qbusiness:ListGroups](#list_qbusiness-action-ListGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListIndices  **
  - **IAM action:**  [qbusiness:ListIndices](#list_qbusiness-action-ListIndices) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMessages  **
  - **IAM action:**  [qbusiness:ListMessages](#list_qbusiness-action-ListMessages) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPluginActions  **
  - **IAM action:**  [qbusiness:ListPluginActions](#list_qbusiness-action-ListPluginActions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListPluginTypeActions  **
  - **IAM action:**  [qbusiness:ListPluginTypeActions](#list_qbusiness-action-ListPluginTypeActions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListPluginTypeMetadata  **
  - **IAM action:**  [qbusiness:ListPluginTypeMetadata](#list_qbusiness-action-ListPluginTypeMetadata) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListPlugins  **
  - **IAM action:**  [qbusiness:ListPlugins](#list_qbusiness-action-ListPlugins) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRetrievers  **
  - **IAM action:**  [qbusiness:ListRetrievers](#list_qbusiness-action-ListRetrievers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSubscriptions  **
  - **IAM action:**  [qbusiness:ListSubscriptions](#list_qbusiness-action-ListSubscriptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [qbusiness:ListTagsForResource](#list_qbusiness-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListWebExperiences  **
  - **IAM action:**  [qbusiness:ListWebExperiences](#list_qbusiness-action-ListWebExperiences) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PutFeedback  **
  - **IAM action:**  [qbusiness:PutFeedback](#list_qbusiness-action-PutFeedback) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutGroup  **
  - **IAM action:**  [qbusiness:PutGroup](#list_qbusiness-action-PutGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** qbusiness.amazonaws.com / **Access level:** Write

- **   SearchRelevantContent  **
  - **IAM action:**  [qbusiness:SearchRelevantContent](#list_qbusiness-action-SearchRelevantContent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   StartDataSourceSyncJob  **
  - **IAM action:**  [qbusiness:StartDataSourceSyncJob](#list_qbusiness-action-StartDataSourceSyncJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopDataSourceSyncJob  **
  - **IAM action:**  [qbusiness:StopDataSourceSyncJob](#list_qbusiness-action-StopDataSourceSyncJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [qbusiness:TagResource](#list_qbusiness-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [qbusiness:UntagResource](#list_qbusiness-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateApplication  **
  - **IAM action:**  [qbusiness:UpdateApplication](#list_qbusiness-action-UpdateApplication)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** qbusiness.amazonaws.com / **Access level:** Write

- **   UpdateChatControlsConfiguration  **
  - **IAM action:**  [qbusiness:UpdateChatControlsConfiguration](#list_qbusiness-action-UpdateChatControlsConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateChatResponseConfiguration  **
  - **IAM action:**  [qbusiness:UpdateChatResponseConfiguration](#list_qbusiness-action-UpdateChatResponseConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDataAccessor  **
  - **IAM action:**  [qbusiness:UpdateDataAccessor](#list_qbusiness-action-UpdateDataAccessor) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDataSource  **
  - **IAM action:**  [qbusiness:UpdateDataSource](#list_qbusiness-action-UpdateDataSource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** qbusiness.amazonaws.com / **Access level:** Write

- **   UpdateIndex  **
  - **IAM action:**  [qbusiness:UpdateIndex](#list_qbusiness-action-UpdateIndex) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdatePlugin  **
  - **IAM action:**  [qbusiness:UpdatePlugin](#list_qbusiness-action-UpdatePlugin)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** qbusiness.amazonaws.com / **Access level:** Write

- **   UpdateRetriever  **
  - **IAM action:**  [qbusiness:UpdateRetriever](#list_qbusiness-action-UpdateRetriever)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** qbusiness.amazonaws.com / **Access level:** Write

- **   UpdateSubscription  **
  - **IAM action:**  [qbusiness:UpdateSubscription](#list_qbusiness-action-UpdateSubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateUser  **
  - **IAM action:**  [qbusiness:UpdateUser](#list_qbusiness-action-UpdateUser) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateWebExperience  **
  - **IAM action:**  [qbusiness:UpdateWebExperience](#list_qbusiness-action-UpdateWebExperience)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** qbusiness.amazonaws.com / **Access level:** Write



## Actions defined by Amazon Q Business
<a name="list_qbusiness-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AssociatePermission](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_AssociatePermission.html)  **
  - **Description:** Grants permission to associate resource based policy statement to the application
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchDeleteDocument](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_BatchDeleteDocument.html)  **
  - **Description:** Grants permission to batch delete document
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [index\*](#list_qbusiness-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchPutDocument](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_BatchPutDocument.html)  **
  - **Description:** Grants permission to batch put document
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [index\*](#list_qbusiness-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CancelSubscription](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CancelSubscription.html)  **
  - **Description:** Grants permission to cancel a subscription
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [subscription\*](#list_qbusiness-resource-subscription) / **Condition keys:**  
  - **Access level:** Write

- **   [Chat](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_Chat.html)  **
  - **Description:** Grants permission to chat using an application
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ChatSync](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ChatSync.html)  **
  - **Description:** Grants permission to chat synchronously using an application
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [CheckDocumentAccess](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CheckDocumentAccess.html)  **
  - **Description:** Grants permission to check if a user has access to a document
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [index\*](#list_qbusiness-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [CreateAnonymousWebExperienceUrl](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateAnonymousWebExperienceUrl.html)  **
  - **Description:** Grants permission to create a unique URL for anonymous Amazon Q Business web experience
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [web-experience\*](#list_qbusiness-resource-web-experience) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateApplication](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateApplication.html)  **
  - **Description:** Grants permission to create an application
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_qbusiness-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_qbusiness-aws_TagKeys)
  - **Access level:** Write

- **   [CreateChatResponseConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateChatResponseConfiguration.html)  **
  - **Description:** Grants permission to create a chat response configuration to the application
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_qbusiness-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_qbusiness-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDataAccessor](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateDataAccessor.html)  **
  - **Description:** Grants permission to create DataAccessor to the application
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_qbusiness-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_qbusiness-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDataSource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateDataSource.html)  **
  - **Description:** Grants permission to create a data source for a given application and index
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_qbusiness-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_qbusiness-aws_TagKeys)
  - **Resource types (\*required):** [index\*](#list_qbusiness-resource-index) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_qbusiness-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_qbusiness-aws_TagKeys)
  - **Access level:** Write

- **   [CreateIndex](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateIndex.html)  **
  - **Description:** Grants permission to create an index for a given application
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_qbusiness-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_qbusiness-aws_TagKeys)
  - **Access level:** Write

- **   [CreateIntegration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateIntegration.html)  **
  - **Description:** Grants permission to create a new integration for a Q Business application
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_qbusiness-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_qbusiness-aws_TagKeys)
  - **Access level:** Write

- **   [CreatePlugin](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreatePlugin.html)  **
  - **Description:** Grants permission to create a plugin for a given application
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_qbusiness-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_qbusiness-aws_TagKeys)
  - **Access level:** Write

- **   [CreateRetriever](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateRetriever.html)  **
  - **Description:** Grants permission to create a retriever for a given application
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_qbusiness-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_qbusiness-aws_TagKeys)
  - **Access level:** Write

- **   [CreateSubscription](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateSubscription.html)  **
  - **Description:** Grants permission to create a subscription
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)<br />[identitystore:GroupId](#list_qbusiness-identitystore_GroupId)<br />[identitystore:UserId](#list_qbusiness-identitystore_UserId)
  - **Access level:** Write

- **   [CreateUser](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateUser.html)  **
  - **Description:** Grants permission to create a user
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateWebExperience](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateWebExperience.html)  **
  - **Description:** Grants permission to create a web experience for a given application
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_qbusiness-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_qbusiness-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteApplication](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DeleteApplication.html)  **
  - **Description:** Grants permission to delete an application
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAttachment](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DeleteAttachment.html)  **
  - **Description:** Grants permission to delete an attachment in the current chat context
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteChatControlsConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DeleteChatControlsConfiguration.html)  **
  - **Description:** Grants permission to delete chat controls configuration for an application
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteChatResponseConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DeleteChatResponseConfiguration.html)  **
  - **Description:** Grants permission to delete a chat response configuration
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [chat-response-configuration\*](#list_qbusiness-resource-chat-response-configuration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteConversation](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DeleteConversation.html)  **
  - **Description:** Grants permission to delete a conversation
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDataAccessor](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DeleteDataAccessor.html)  **
  - **Description:** Grants permission to delete DataAccessor
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [data-accessor\*](#list_qbusiness-resource-data-accessor) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDataSource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DeleteDataSource.html)  **
  - **Description:** Grants permission to delete a DataSource
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [data-source\*](#list_qbusiness-resource-data-source) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [index\*](#list_qbusiness-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteGroup](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DeleteGroup.html)  **
  - **Description:** Grants permission to delete a group
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [index\*](#list_qbusiness-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteIndex](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DeleteIndex.html)  **
  - **Description:** Grants permission to delete an index
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [index\*](#list_qbusiness-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteIntegration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DeleteIntegration.html)  **
  - **Description:** Grants permission to delete an integration for a Q Business application
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [integration\*](#list_qbusiness-resource-integration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePlugin](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DeletePlugin.html)  **
  - **Description:** Grants permission to delete a plugin
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [plugin\*](#list_qbusiness-resource-plugin) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRetriever](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DeleteRetriever.html)  **
  - **Description:** Grants permission to delete a retriever
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [retriever\*](#list_qbusiness-resource-retriever) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteUser](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DeleteUser.html)  **
  - **Description:** Grants permission to delete a user
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteWebExperience](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DeleteWebExperience.html)  **
  - **Description:** Grants permission to delete a web-experience
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [web-experience\*](#list_qbusiness-resource-web-experience) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociatePermission](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DisassociatePermission.html)  **
  - **Description:** Grants permission to disassociate resource based policy statement to the application
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetApplication](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GetApplication.html)  **
  - **Description:** Grants permission to get an application
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetChatControlsConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GetChatControlsConfiguration.html)  **
  - **Description:** Grants permission to get chat controls configuration for an application
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [GetChatResponseConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GetChatResponseConfiguration.html)  **
  - **Description:** Grants permission to get a chat response configuration
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [chat-response-configuration\*](#list_qbusiness-resource-chat-response-configuration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDataAccessor](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GetDataAccessor.html)  **
  - **Description:** Grants permission to get DataAccessor
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [data-accessor\*](#list_qbusiness-resource-data-accessor) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDataSource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GetDataSource.html)  **
  - **Description:** Grants permission to get a data source
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [data-source\*](#list_qbusiness-resource-data-source) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [index\*](#list_qbusiness-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDocumentContent](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GetDocumentContent.html)  **
  - **Description:** Grants permission to get a document content
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [index\*](#list_qbusiness-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetGroup](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GetGroup.html)  **
  - **Description:** Grants permission to get a group
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [index\*](#list_qbusiness-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetIndex](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GetIndex.html)  **
  - **Description:** Grants permission to get an index
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [index\*](#list_qbusiness-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetIntegration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GetIntegration.html)  **
  - **Description:** Grants permission to get an integration for a Q Business application
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [integration\*](#list_qbusiness-resource-integration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetMedia](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GetMedia.html)  **
  - **Description:** Grants permission to get the media associated to a system message
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPlugin](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GetPlugin.html)  **
  - **Description:** Grants permission to get a plugin
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [plugin\*](#list_qbusiness-resource-plugin) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPolicy](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GetPolicy.html)  **
  - **Description:** Grants permission to get resource based policy of the application
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRetriever](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GetRetriever.html)  **
  - **Description:** Grants permission to get a retriever
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [retriever\*](#list_qbusiness-resource-retriever) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetUser](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GetUser.html)  **
  - **Description:** Grants permission to get a user
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetWebExperience](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GetWebExperience.html)  **
  - **Description:** Grants permission to get a web-experience
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [web-experience\*](#list_qbusiness-resource-web-experience) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListApplications](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListApplications.html)  **
  - **Description:** Grants permission to list the applications
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAttachments](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListAttachments.html)  **
  - **Description:** Grants permission to list attachments in the current chat context
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListChatResponseConfigurations](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListChatResponseConfigurations.html)  **
  - **Description:** Grants permission to list chat response configurations for an application
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListConversations](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListConversations.html)  **
  - **Description:** Grants permission to list all conversations for an application
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDataAccessors](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListDataAccessors.html)  **
  - **Description:** Grants permission to list DataAccessors for the application
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDataSourceSyncJobs](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListDataSourceSyncJobs.html)  **
  - **Description:** Grants permission to get Data Source sync job history
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [data-source\*](#list_qbusiness-resource-data-source) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [index\*](#list_qbusiness-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDataSources](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListDataSources.html)  **
  - **Description:** Grants permission to list the data sources of an application and an index
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [index\*](#list_qbusiness-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDocuments](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListDocuments.html)  **
  - **Description:** Grants permission to list all documents
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [index\*](#list_qbusiness-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListGroups](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListGroups.html)  **
  - **Description:** Grants permission to list groups
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [index\*](#list_qbusiness-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListIndices](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListIndices.html)  **
  - **Description:** Grants permission to list the indices of an application
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListIntegrations](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListIntegrations.html)  **
  - **Description:** Grants permission to list all integrations for a Q Business application
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListMessages](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListMessages.html)  **
  - **Description:** Grants permission to list all messages
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListPluginActions](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListPluginActions.html)  **
  - **Description:** Grants permission to list the plugins actions of a plugin within application
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [plugin\*](#list_qbusiness-resource-plugin) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListPluginTypeActions](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListPluginTypeActions.html)  **
  - **Description:** Grants permission to list all the actions for a plugin type
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListPluginTypeMetadata](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListPluginTypeMetadata.html)  **
  - **Description:** Grants permission to list all the plugin type metadata
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListPlugins](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListPlugins.html)  **
  - **Description:** Grants permission to list the plugins of an application
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListRetrievers](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListRetrievers.html)  **
  - **Description:** Grants permission to list the retrievers of an application
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListSubscriptions](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListSubscriptions.html)  **
  - **Description:** Grants permission to list subscriptions
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a resource
  - **Resource types (\*required):** [application](#list_qbusiness-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [chat-response-configuration](#list_qbusiness-resource-chat-response-configuration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [data-accessor](#list_qbusiness-resource-data-accessor) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [data-source](#list_qbusiness-resource-data-source) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [index](#list_qbusiness-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [integration](#list_qbusiness-resource-integration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [plugin](#list_qbusiness-resource-plugin) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [retriever](#list_qbusiness-resource-retriever) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [web-experience](#list_qbusiness-resource-web-experience) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListWebExperiences](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListWebExperiences.html)  **
  - **Description:** Grants permission to list the web experiences of an application
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [PutFeedback](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_PutFeedback.html)  **
  - **Description:** Grants permission to put feedback about a conversation message
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutGroup](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_PutGroup.html)  **
  - **Description:** Grants permission to put a group of users
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [index\*](#list_qbusiness-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SearchRelevantContent](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_SearchRelevantContent.html)  **
  - **Description:** Grants permission to search relevant content from the Amazon Q Business Application
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [StartDataSourceSyncJob](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_StartDataSourceSyncJob.html)  **
  - **Description:** Grants permission to start Data Source sync job
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [data-source\*](#list_qbusiness-resource-data-source) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [index\*](#list_qbusiness-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartDeployment](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_StartDeployment.html)  **
  - **Description:** Grants permission to start deployment for an integration
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [integration\*](#list_qbusiness-resource-integration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopDataSourceSyncJob](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_StopDataSourceSyncJob.html)  **
  - **Description:** Grants permission to stop Data Source sync job
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [data-source\*](#list_qbusiness-resource-data-source) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [index\*](#list_qbusiness-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_TagResource.html)  **
  - **Description:** Grants permission to tag a resource with given key value pairs
  - **Resource types (\*required):** [application](#list_qbusiness-resource-application) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_qbusiness-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_qbusiness-aws_TagKeys)
  - **Resource types (\*required):** [chat-response-configuration](#list_qbusiness-resource-chat-response-configuration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_qbusiness-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_qbusiness-aws_TagKeys)
  - **Resource types (\*required):** [data-accessor](#list_qbusiness-resource-data-accessor) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_qbusiness-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_qbusiness-aws_TagKeys)
  - **Resource types (\*required):** [data-source](#list_qbusiness-resource-data-source) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_qbusiness-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_qbusiness-aws_TagKeys)
  - **Resource types (\*required):** [index](#list_qbusiness-resource-index) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_qbusiness-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_qbusiness-aws_TagKeys)
  - **Resource types (\*required):** [integration](#list_qbusiness-resource-integration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_qbusiness-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_qbusiness-aws_TagKeys)
  - **Resource types (\*required):** [plugin](#list_qbusiness-resource-plugin) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_qbusiness-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_qbusiness-aws_TagKeys)
  - **Resource types (\*required):** [retriever](#list_qbusiness-resource-retriever) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_qbusiness-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_qbusiness-aws_TagKeys)
  - **Resource types (\*required):** [web-experience](#list_qbusiness-resource-web-experience) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_qbusiness-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_qbusiness-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove the tag with the given key from a resource
  - **Resource types (\*required):** [application](#list_qbusiness-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_qbusiness-aws_TagKeys)
  - **Resource types (\*required):** [chat-response-configuration](#list_qbusiness-resource-chat-response-configuration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_qbusiness-aws_TagKeys)
  - **Resource types (\*required):** [data-accessor](#list_qbusiness-resource-data-accessor) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_qbusiness-aws_TagKeys)
  - **Resource types (\*required):** [data-source](#list_qbusiness-resource-data-source) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_qbusiness-aws_TagKeys)
  - **Resource types (\*required):** [index](#list_qbusiness-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_qbusiness-aws_TagKeys)
  - **Resource types (\*required):** [integration](#list_qbusiness-resource-integration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_qbusiness-aws_TagKeys)
  - **Resource types (\*required):** [plugin](#list_qbusiness-resource-plugin) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_qbusiness-aws_TagKeys)
  - **Resource types (\*required):** [retriever](#list_qbusiness-resource-retriever) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_qbusiness-aws_TagKeys)
  - **Resource types (\*required):** [web-experience](#list_qbusiness-resource-web-experience) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_qbusiness-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateApplication](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UpdateApplication.html)  **
  - **Description:** Grants permission to update an Application
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateChatControlsConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UpdateChatControlsConfiguration.html)  **
  - **Description:** Grants permission to update chat controls configuration for an application
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateChatResponseConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UpdateChatResponseConfiguration.html)  **
  - **Description:** Grants permission to update a chat response configuration
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [chat-response-configuration\*](#list_qbusiness-resource-chat-response-configuration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDataAccessor](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UpdateDataAccessor.html)  **
  - **Description:** Grants permission to update DataAccessor
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [data-accessor\*](#list_qbusiness-resource-data-accessor) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDataSource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UpdateDataSource.html)  **
  - **Description:** Grants permission to update a DataSource
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [data-source\*](#list_qbusiness-resource-data-source) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [index\*](#list_qbusiness-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateIndex](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UpdateIndex.html)  **
  - **Description:** Grants permission to update an index
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [index\*](#list_qbusiness-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateIntegration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UpdateIntegration.html)  **
  - **Description:** Grants permission to update an integration for a Q Business application
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [integration\*](#list_qbusiness-resource-integration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdatePlugin](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UpdatePlugin.html)  **
  - **Description:** Grants permission to update a plugin
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [plugin\*](#list_qbusiness-resource-plugin) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateRetriever](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UpdateRetriever.html)  **
  - **Description:** Grants permission to update a Retriever
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [retriever\*](#list_qbusiness-resource-retriever) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSubscription](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UpdateSubscription.html)  **
  - **Description:** Grants permission to update a subscription
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [subscription\*](#list_qbusiness-resource-subscription) / **Condition keys:**  
  - **Access level:** Write

- **   [UpdateUser](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UpdateUser.html)  **
  - **Description:** Grants permission to update a user
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateWebExperience](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UpdateWebExperience.html)  **
  - **Description:** Grants permission to update a WebExperience
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [web-experience\*](#list_qbusiness-resource-web-experience) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for Amazon Q Business
<a name="list_qbusiness-permission-only-actions"></a>

The following actions are defined by Amazon Q Business but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [AllowVendedLogDeliveryForResource](${UserGuideDocPage}monitoring-overview.html)  **
  - **Description:** Grants permission to configure vended log delivery for Amazon Q Business application resource
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [CreateDataAccessorWithTti](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateDataAccessor.html)  **
  - **Description:** Grants permission to create AWS IAM Identity center Trusted Token Issuer based DataAccessor to the application
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisableAclOnDataSource](${UserGuideDocPage}setting-up.html#DisableAclOnDataSource)  **
  - **Description:** Grants permission to disable the ACL crawl while creating the Amazon Q Business data source resource
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutResourcePolicy](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_AssociatePermission.html)  **
  - **Description:** Grants permission to put resource based policy statement to the application
  - **Resource types (\*required):** [application\*](#list_qbusiness-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon Q Business
<a name="list_qbusiness-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [application](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/create-application.html)  | arn:${Partition}:qbusiness:${Region}:${Account}:application/${ApplicationId} | [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_) | 
|  [chat-response-configuration](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/response-customization.html)  | arn:${Partition}:qbusiness:${Region}:${Account}:application/${ApplicationId}/chat-response-configuration/${ChatResponseConfigurationId} | [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_) | 
|  [data-accessor](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/data-accessors.html)  | arn:${Partition}:qbusiness:${Region}:${Account}:application/${ApplicationId}/data-accessor/${DataAccessorId} | [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_) | 
|  [data-source](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/connect-data.html)  | arn:${Partition}:qbusiness:${Region}:${Account}:application/${ApplicationId}/index/${IndexId}/data-source/${DataSourceId} | [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_) | 
|  [index](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/select-retriever.html)  | arn:${Partition}:qbusiness:${Region}:${Account}:application/${ApplicationId}/index/${IndexId} | [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_) | 
|  [integration](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/create-integration.html)  | arn:${Partition}:qbusiness:${Region}:${Account}:application/${ApplicationId}/integration/${IntegrationId} | [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_) | 
|  [plugin](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/plugins.html)  | arn:${Partition}:qbusiness:${Region}:${Account}:application/${ApplicationId}/plugin/${PluginId} | [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_) | 
|  [retriever](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/select-retriever.html)  | arn:${Partition}:qbusiness:${Region}:${Account}:application/${ApplicationId}/retriever/${RetrieverId} | [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_) | 
|  [subscription](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/subscriptions.html)  | arn:${Partition}:qbusiness:${Region}:${Account}:application/${ApplicationId}/subscription/${SubscriptionId} |   | 
|  [web-experience](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/using-web-experience.html)  | arn:${Partition}:qbusiness:${Region}:${Account}:application/${ApplicationId}/web-experience/${WebExperienceId} | [aws:ResourceTag/${TagKey}](#list_qbusiness-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon Q Business
<a name="list_qbusiness-policy-keys"></a>

Amazon Q Business defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 
|   [identitystore:GroupId](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/security_iam_service-with-iam.html)  | Filters access by IAM Identity Center Group ID | ArrayOfString | 
|   [identitystore:UserId](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/security_iam_service-with-iam.html)  | Filters access by IAM Identity Center User ID | ArrayOfString | 