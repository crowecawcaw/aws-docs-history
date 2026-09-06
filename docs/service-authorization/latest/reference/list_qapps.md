

# Actions, resources, and condition keys for Amazon Q Business Q Apps
<a name="list_qapps"></a>

Amazon Q Business Q Apps (service prefix: `qapps`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/amazonq/latest/api-reference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/qapps/qapps.json) for this service.

**Topics**
+ [API operations defined by Amazon Q Business Q Apps](#list_qapps-operations)
+ [Actions defined by Amazon Q Business Q Apps](#list_qapps-actions-as-permissions)
+ [Permission-only actions for Amazon Q Business Q Apps](#list_qapps-permission-only-actions)
+ [Resource types defined by Amazon Q Business Q Apps](#list_qapps-resources-for-iam-policies)
+ [Condition keys for Amazon Q Business Q Apps](#list_qapps-policy-keys)

## API operations defined by Amazon Q Business Q Apps
<a name="list_qapps-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_qapps-actions-as-permissions).




- **   AssociateLibraryItemReview  **
  - **IAM action:**  [qapps:AssociateLibraryItemReview](#list_qapps-action-AssociateLibraryItemReview) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateQAppWithUser  **
  - **IAM action:**  [qapps:AssociateQAppWithUser](#list_qapps-action-AssociateQAppWithUser) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchCreateCategory  **
  - **IAM action:**  [qapps:BatchCreateCategory](#list_qapps-action-BatchCreateCategory) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchDeleteCategory  **
  - **IAM action:**  [qapps:BatchDeleteCategory](#list_qapps-action-BatchDeleteCategory) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchUpdateCategory  **
  - **IAM action:**  [qapps:BatchUpdateCategory](#list_qapps-action-BatchUpdateCategory) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateLibraryItem  **
  - **IAM action:**  [qapps:CreateLibraryItem](#list_qapps-action-CreateLibraryItem) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreatePresignedUrl  **
  - **IAM action:**  [qapps:ImportDocument](#list_qapps-action-ImportDocument) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateQApp  **
  - **IAM action:**  [qapps:CreateQApp](#list_qapps-action-CreateQApp) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteLibraryItem  **
  - **IAM action:**  [qapps:DeleteLibraryItem](#list_qapps-action-DeleteLibraryItem) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteQApp  **
  - **IAM action:**  [qapps:DeleteQApp](#list_qapps-action-DeleteQApp) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeQAppPermissions  **
  - **IAM action:**  [qapps:DescribeQAppPermissions](#list_qapps-action-DescribeQAppPermissions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DisassociateLibraryItemReview  **
  - **IAM action:**  [qapps:DisassociateLibraryItemReview](#list_qapps-action-DisassociateLibraryItemReview) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateQAppFromUser  **
  - **IAM action:**  [qapps:DisassociateQAppFromUser](#list_qapps-action-DisassociateQAppFromUser) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ExportQAppSessionData  **
  - **IAM action:**  [qapps:ExportQAppSessionData](#list_qapps-action-ExportQAppSessionData) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetLibraryItem  **
  - **IAM action:**  [qapps:GetLibraryItem](#list_qapps-action-GetLibraryItem) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetQApp  **
  - **IAM action:**  [qapps:GetQApp](#list_qapps-action-GetQApp) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetQAppSession  **
  - **IAM action:**  [qapps:GetQAppSession](#list_qapps-action-GetQAppSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetQAppSessionMetadata  **
  - **IAM action:**  [qapps:GetQAppSessionMetadata](#list_qapps-action-GetQAppSessionMetadata) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ImportDocument  **
  - **IAM action:**  [qapps:ImportDocument](#list_qapps-action-ImportDocument) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ListCategories  **
  - **IAM action:**  [qapps:ListCategories](#list_qapps-action-ListCategories) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListLibraryItems  **
  - **IAM action:**  [qapps:ListLibraryItems](#list_qapps-action-ListLibraryItems) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListQAppSessionData  **
  - **IAM action:**  [qapps:ListQAppSessionData](#list_qapps-action-ListQAppSessionData) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListQApps  **
  - **IAM action:**  [qapps:ListQApps](#list_qapps-action-ListQApps) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [qapps:ListTagsForResource](#list_qapps-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   StartQAppSession  **
  - **IAM action:**  [qapps:StartQAppSession](#list_qapps-action-StartQAppSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopQAppSession  **
  - **IAM action:**  [qapps:StopQAppSession](#list_qapps-action-StopQAppSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [qapps:TagResource](#list_qapps-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [qapps:UntagResource](#list_qapps-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateLibraryItem  **
  - **IAM action:**  [qapps:UpdateLibraryItem](#list_qapps-action-UpdateLibraryItem) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateLibraryItemMetadata  **
  - **IAM action:**  [qapps:UpdateLibraryItemMetadata](#list_qapps-action-UpdateLibraryItemMetadata) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateQApp  **
  - **IAM action:**  [qapps:UpdateQApp](#list_qapps-action-UpdateQApp) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateQAppPermissions  **
  - **IAM action:**  [qapps:UpdateQAppPermissions](#list_qapps-action-UpdateQAppPermissions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateQAppSession  **
  - **IAM action:**  [qapps:UpdateQAppSession](#list_qapps-action-UpdateQAppSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateQAppSessionMetadata  **
  - **IAM action:**  [qapps:UpdateQAppSessionMetadata](#list_qapps-action-UpdateQAppSessionMetadata) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon Q Business Q Apps
<a name="list_qapps-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AssociateLibraryItemReview](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_AssociateLibraryItemReview.html)  **
  - **Description:** Grants permission to associate a library item review in the Q Business application environment
  - **Resource types (\*required):** [qapp\*](#list_qapps-resource-qapp)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qapps-aws_ResourceTag___TagKey_)<br />[qapps:AppIsPublished](#list_qapps-qapps_AppIsPublished)<br />[qapps:UserIsAppOwner](#list_qapps-qapps_UserIsAppOwner)
  - **Access level:** Write

- **   [AssociateQAppWithUser](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_AssociateQAppWithUser.html)  **
  - **Description:** Grants permission to associate Q App with a user in the Q Business application environment
  - **Resource types (\*required):** [application](#list_qapps-resource-application) / **Condition keys:** [qapps:AppIsPublished](#list_qapps-qapps_AppIsPublished)<br />[qapps:UserIsAppOwner](#list_qapps-qapps_UserIsAppOwner)
  - **Resource types (\*required):** [qapp](#list_qapps-resource-qapp) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qapps-aws_ResourceTag___TagKey_)<br />[qapps:AppIsPublished](#list_qapps-qapps_AppIsPublished)<br />[qapps:UserIsAppOwner](#list_qapps-qapps_UserIsAppOwner)
  - **Access level:** Write

- **   [BatchCreateCategory](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_BatchCreateCategory.html)  **
  - **Description:** Grants permission to create the categories of a library in the Q Business application environment
  - **Resource types (\*required):** [application\*](#list_qapps-resource-application)
  - **Condition keys:**  
  - **Access level:** Write

- **   [BatchDeleteCategory](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_BatchDeleteCategory.html)  **
  - **Description:** Grants permission to delete the categories of a library in the Q Business application environment
  - **Resource types (\*required):** [application\*](#list_qapps-resource-application)
  - **Condition keys:**  
  - **Access level:** Write

- **   [BatchUpdateCategory](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_BatchUpdateCategory.html)  **
  - **Description:** Grants permission to update the categories of a library in the Q Business application environment
  - **Resource types (\*required):** [application\*](#list_qapps-resource-application)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateLibraryItem](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_CreateLibraryItem.html)  **
  - **Description:** Grants permission to create a library item in the Q Business application environment
  - **Resource types (\*required):** [application](#list_qapps-resource-application) / **Condition keys:** [qapps:AppIsPublished](#list_qapps-qapps_AppIsPublished)<br />[qapps:UserIsAppOwner](#list_qapps-qapps_UserIsAppOwner)
  - **Resource types (\*required):** [qapp](#list_qapps-resource-qapp) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qapps-aws_ResourceTag___TagKey_)<br />[qapps:AppIsPublished](#list_qapps-qapps_AppIsPublished)<br />[qapps:UserIsAppOwner](#list_qapps-qapps_UserIsAppOwner)
  - **Access level:** Write

- **   [CreateQApp](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_CreateQApp.html)  **
  - **Description:** Grants permission to create Q App in the Q Business application environment
  - **Resource types (\*required):** [application\*](#list_qapps-resource-application)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_qapps-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_qapps-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteLibraryItem](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_DeleteLibraryItem.html)  **
  - **Description:** Grants permission to delete a library item in the Q Business application environment
  - **Resource types (\*required):** [application](#list_qapps-resource-application) / **Condition keys:** [qapps:AppIsPublished](#list_qapps-qapps_AppIsPublished)<br />[qapps:UserIsAppOwner](#list_qapps-qapps_UserIsAppOwner)
  - **Resource types (\*required):** [qapp](#list_qapps-resource-qapp) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qapps-aws_ResourceTag___TagKey_)<br />[qapps:AppIsPublished](#list_qapps-qapps_AppIsPublished)<br />[qapps:UserIsAppOwner](#list_qapps-qapps_UserIsAppOwner)
  - **Access level:** Write

- **   [DeleteQApp](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_DeleteQApp.html)  **
  - **Description:** Grants permission to delete Q App in the Q Business application environment
  - **Resource types (\*required):** [application](#list_qapps-resource-application) / **Condition keys:** [qapps:AppIsPublished](#list_qapps-qapps_AppIsPublished)<br />[qapps:UserIsAppOwner](#list_qapps-qapps_UserIsAppOwner)
  - **Resource types (\*required):** [qapp](#list_qapps-resource-qapp) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qapps-aws_ResourceTag___TagKey_)<br />[qapps:AppIsPublished](#list_qapps-qapps_AppIsPublished)<br />[qapps:UserIsAppOwner](#list_qapps-qapps_UserIsAppOwner)
  - **Access level:** Write

- **   [DescribeQAppPermissions](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_DescribeQAppPermissions.html)  **
  - **Description:** Grants permission to get Q App sharing permissions in the Q Business application environment
  - **Resource types (\*required):** [application](#list_qapps-resource-application) / **Condition keys:** [qapps:AppIsPublished](#list_qapps-qapps_AppIsPublished)<br />[qapps:UserIsAppOwner](#list_qapps-qapps_UserIsAppOwner)
  - **Resource types (\*required):** [qapp](#list_qapps-resource-qapp) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qapps-aws_ResourceTag___TagKey_)<br />[qapps:AppIsPublished](#list_qapps-qapps_AppIsPublished)<br />[qapps:UserIsAppOwner](#list_qapps-qapps_UserIsAppOwner)
  - **Access level:** Read

- **   [DisassociateLibraryItemReview](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_DisassociateLibraryItemReview.html)  **
  - **Description:** Grants permission to disassociate a library item review in the Q Business application environment
  - **Resource types (\*required):** [qapp\*](#list_qapps-resource-qapp)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qapps-aws_ResourceTag___TagKey_)<br />[qapps:AppIsPublished](#list_qapps-qapps_AppIsPublished)<br />[qapps:UserIsAppOwner](#list_qapps-qapps_UserIsAppOwner)
  - **Access level:** Write

- **   [DisassociateQAppFromUser](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_DisassociateQAppFromUser.html)  **
  - **Description:** Grants permission to disassociate Q App with a user in the Q Business application environment
  - **Resource types (\*required):** [application](#list_qapps-resource-application) / **Condition keys:** [qapps:AppIsPublished](#list_qapps-qapps_AppIsPublished)<br />[qapps:UserIsAppOwner](#list_qapps-qapps_UserIsAppOwner)
  - **Resource types (\*required):** [qapp](#list_qapps-resource-qapp) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qapps-aws_ResourceTag___TagKey_)<br />[qapps:AppIsPublished](#list_qapps-qapps_AppIsPublished)<br />[qapps:UserIsAppOwner](#list_qapps-qapps_UserIsAppOwner)
  - **Access level:** Write

- **   [ExportQAppSessionData](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/purpose-built-qapps.html)  **
  - **Description:** Grants permission to export Q App session data in the Q Business application environment
  - **Resource types (\*required):** [qapp-session\*](#list_qapps-resource-qapp-session)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qapps-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetLibraryItem](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_GetLibraryItem.html)  **
  - **Description:** Grants permission to get a library item in the Q Business application environment
  - **Resource types (\*required):** [application](#list_qapps-resource-application) / **Condition keys:** [qapps:AppIsPublished](#list_qapps-qapps_AppIsPublished)<br />[qapps:UserIsAppOwner](#list_qapps-qapps_UserIsAppOwner)
  - **Resource types (\*required):** [qapp](#list_qapps-resource-qapp) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qapps-aws_ResourceTag___TagKey_)<br />[qapps:AppIsPublished](#list_qapps-qapps_AppIsPublished)<br />[qapps:UserIsAppOwner](#list_qapps-qapps_UserIsAppOwner)
  - **Access level:** Read

- **   [GetQApp](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_GetQApp.html)  **
  - **Description:** Grants permission to get Q App in the Q Business application environment
  - **Resource types (\*required):** [application](#list_qapps-resource-application) / **Condition keys:** [qapps:AppIsPublished](#list_qapps-qapps_AppIsPublished)<br />[qapps:UserIsAppOwner](#list_qapps-qapps_UserIsAppOwner)
  - **Resource types (\*required):** [qapp](#list_qapps-resource-qapp) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qapps-aws_ResourceTag___TagKey_)<br />[qapps:AppIsPublished](#list_qapps-qapps_AppIsPublished)<br />[qapps:UserIsAppOwner](#list_qapps-qapps_UserIsAppOwner)
  - **Access level:** Read

- **   [GetQAppSession](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_GetQAppSession.html)  **
  - **Description:** Grants permission to get Q App session in the Q Business application environment
  - **Resource types (\*required):** [qapp-session\*](#list_qapps-resource-qapp-session)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qapps-aws_ResourceTag___TagKey_)<br />[qapps:AppIsPublished](#list_qapps-qapps_AppIsPublished)<br />[qapps:SessionIsShared](#list_qapps-qapps_SessionIsShared)<br />[qapps:UserIsAppOwner](#list_qapps-qapps_UserIsAppOwner)<br />[qapps:UserIsSessionModerator](#list_qapps-qapps_UserIsSessionModerator)
  - **Access level:** Read

- **   [GetQAppSessionMetadata](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/purpose-built-qapps.html)  **
  - **Description:** Grants permission to get Q App session metadata in the Q Business application environment
  - **Resource types (\*required):** [qapp-session\*](#list_qapps-resource-qapp-session)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qapps-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ImportDocument](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_ImportDocument.html)  **
  - **Description:** Grants permission to import a document to Q App or Q App Session in the Q Business application environment
  - **Resource types (\*required):** [qapp](#list_qapps-resource-qapp) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qapps-aws_ResourceTag___TagKey_)<br />[qapps:AppIsPublished](#list_qapps-qapps_AppIsPublished)<br />[qapps:SessionIsShared](#list_qapps-qapps_SessionIsShared)<br />[qapps:UserIsAppOwner](#list_qapps-qapps_UserIsAppOwner)<br />[qapps:UserIsSessionModerator](#list_qapps-qapps_UserIsSessionModerator)
  - **Resource types (\*required):** [qapp-session](#list_qapps-resource-qapp-session) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qapps-aws_ResourceTag___TagKey_)<br />[qapps:AppIsPublished](#list_qapps-qapps_AppIsPublished)<br />[qapps:SessionIsShared](#list_qapps-qapps_SessionIsShared)<br />[qapps:UserIsAppOwner](#list_qapps-qapps_UserIsAppOwner)<br />[qapps:UserIsSessionModerator](#list_qapps-qapps_UserIsSessionModerator)
  - **Access level:** Write

- **   [ListCategories](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_ListCategories.html)  **
  - **Description:** Grants permission to list categories in the Q Business application environment
  - **Resource types (\*required):** [application\*](#list_qapps-resource-application)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListLibraryItems](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_ListLibraryItems.html)  **
  - **Description:** Grants permission to list library items in the Q Business application environment
  - **Resource types (\*required):** [application\*](#list_qapps-resource-application)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListQAppSessionData](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/purpose-built-qapps.html)  **
  - **Description:** Grants permission to get Q App session data in the Q Business application environment
  - **Resource types (\*required):** [qapp-session\*](#list_qapps-resource-qapp-session)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qapps-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListQApps](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_ListQApps.html)  **
  - **Description:** Grants permission to list Q Apps in the Q Business application environment
  - **Resource types (\*required):** [application\*](#list_qapps-resource-application)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a resource
  - **Resource types (\*required):** [qapp](#list_qapps-resource-qapp) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qapps-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [qapp-session](#list_qapps-resource-qapp-session) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qapps-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PredictQApp](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_PredictQApp.html)  **
  - **Description:** Grants permission to predict Q App from conversation log or problem statement in the Q Business application environment
  - **Resource types (\*required):** [application\*](#list_qapps-resource-application)
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartQAppSession](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_StartQAppSession.html)  **
  - **Description:** Grants permission to start Q App session in the Q Business application environment
  - **Resource types (\*required):** [application](#list_qapps-resource-application) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_qapps-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_qapps-aws_TagKeys)<br />[qapps:AppIsPublished](#list_qapps-qapps_AppIsPublished)<br />[qapps:UserIsAppOwner](#list_qapps-qapps_UserIsAppOwner)
  - **Resource types (\*required):** [qapp](#list_qapps-resource-qapp) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_qapps-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_qapps-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_qapps-aws_TagKeys)<br />[qapps:AppIsPublished](#list_qapps-qapps_AppIsPublished)<br />[qapps:UserIsAppOwner](#list_qapps-qapps_UserIsAppOwner)
  - **Access level:** Write

- **   [StopQAppSession](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_StopQAppSession.html)  **
  - **Description:** Grants permission to stop Q App session in the Q Business application environment
  - **Resource types (\*required):** [application](#list_qapps-resource-application) / **Condition keys:** [qapps:AppIsPublished](#list_qapps-qapps_AppIsPublished)<br />[qapps:SessionIsShared](#list_qapps-qapps_SessionIsShared)<br />[qapps:UserIsAppOwner](#list_qapps-qapps_UserIsAppOwner)<br />[qapps:UserIsSessionModerator](#list_qapps-qapps_UserIsSessionModerator)
  - **Resource types (\*required):** [qapp-session](#list_qapps-resource-qapp-session) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qapps-aws_ResourceTag___TagKey_)<br />[qapps:AppIsPublished](#list_qapps-qapps_AppIsPublished)<br />[qapps:SessionIsShared](#list_qapps-qapps_SessionIsShared)<br />[qapps:UserIsAppOwner](#list_qapps-qapps_UserIsAppOwner)<br />[qapps:UserIsSessionModerator](#list_qapps-qapps_UserIsSessionModerator)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_TagResource.html)  **
  - **Description:** Grants permission to tag a resource with given key value pairs
  - **Resource types (\*required):** [qapp](#list_qapps-resource-qapp) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_qapps-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_qapps-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_qapps-aws_TagKeys)
  - **Resource types (\*required):** [qapp-session](#list_qapps-resource-qapp-session) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_qapps-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_qapps-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_qapps-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove the tag with the given key from a resource
  - **Resource types (\*required):** [qapp](#list_qapps-resource-qapp) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qapps-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_qapps-aws_TagKeys)
  - **Resource types (\*required):** [qapp-session](#list_qapps-resource-qapp-session) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qapps-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_qapps-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateLibraryItem](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_UpdateLibraryItem.html)  **
  - **Description:** Grants permission to update a library item in the Q Business application environment
  - **Resource types (\*required):** [application](#list_qapps-resource-application) / **Condition keys:** [qapps:AppIsPublished](#list_qapps-qapps_AppIsPublished)<br />[qapps:UserIsAppOwner](#list_qapps-qapps_UserIsAppOwner)
  - **Resource types (\*required):** [qapp](#list_qapps-resource-qapp) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qapps-aws_ResourceTag___TagKey_)<br />[qapps:AppIsPublished](#list_qapps-qapps_AppIsPublished)<br />[qapps:UserIsAppOwner](#list_qapps-qapps_UserIsAppOwner)
  - **Access level:** Write

- **   [UpdateLibraryItemMetadata](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_UpdateLibraryItemMetadata.html)  **
  - **Description:** Grants permission to update the metadata of a library item in the Q Business application environment
  - **Resource types (\*required):** [qapp\*](#list_qapps-resource-qapp)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qapps-aws_ResourceTag___TagKey_)<br />[qapps:AppIsPublished](#list_qapps-qapps_AppIsPublished)
  - **Access level:** Write

- **   [UpdateQApp](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_UpdateQApp.html)  **
  - **Description:** Grants permission to update Q App in the Q Business application environment
  - **Resource types (\*required):** [application](#list_qapps-resource-application) / **Condition keys:** [qapps:AppIsPublished](#list_qapps-qapps_AppIsPublished)<br />[qapps:UserIsAppOwner](#list_qapps-qapps_UserIsAppOwner)
  - **Resource types (\*required):** [qapp](#list_qapps-resource-qapp) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qapps-aws_ResourceTag___TagKey_)<br />[qapps:AppIsPublished](#list_qapps-qapps_AppIsPublished)<br />[qapps:UserIsAppOwner](#list_qapps-qapps_UserIsAppOwner)
  - **Access level:** Write

- **   [UpdateQAppPermissions](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_UpdateQAppPermissions.html)  **
  - **Description:** Grants permission to update Q App sharing permissions in the Q Business application environment
  - **Resource types (\*required):** [application](#list_qapps-resource-application) / **Condition keys:** [qapps:AppIsPublished](#list_qapps-qapps_AppIsPublished)<br />[qapps:UserIsAppOwner](#list_qapps-qapps_UserIsAppOwner)
  - **Resource types (\*required):** [qapp](#list_qapps-resource-qapp) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qapps-aws_ResourceTag___TagKey_)<br />[qapps:AppIsPublished](#list_qapps-qapps_AppIsPublished)<br />[qapps:UserIsAppOwner](#list_qapps-qapps_UserIsAppOwner)
  - **Access level:** Write

- **   [UpdateQAppSession](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_UpdateQAppSession.html)  **
  - **Description:** Grants permission to update Q App session in the Q Business application environment
  - **Resource types (\*required):** [qapp-session\*](#list_qapps-resource-qapp-session)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qapps-aws_ResourceTag___TagKey_)<br />[qapps:AppIsPublished](#list_qapps-qapps_AppIsPublished)<br />[qapps:SessionIsShared](#list_qapps-qapps_SessionIsShared)<br />[qapps:UserIsAppOwner](#list_qapps-qapps_UserIsAppOwner)<br />[qapps:UserIsSessionModerator](#list_qapps-qapps_UserIsSessionModerator)
  - **Access level:** Write

- **   [UpdateQAppSessionMetadata](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/purpose-built-qapps.html)  **
  - **Description:** Grants permission to update Q App session metadata in the Q Business application environment
  - **Resource types (\*required):** [qapp-session\*](#list_qapps-resource-qapp-session)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qapps-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for Amazon Q Business Q Apps
<a name="list_qapps-permission-only-actions"></a>

The following actions are defined by Amazon Q Business Q Apps but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [CopyQApp](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/purpose-built-qapps.html)  **
  - **Description:** Grants permission to copy Q App in the Q Business application environment
  - **Resource types (\*required):** [application](#list_qapps-resource-application) / **Condition keys:** [qapps:AppIsPublished](#list_qapps-qapps_AppIsPublished)<br />[qapps:UserIsAppOwner](#list_qapps-qapps_UserIsAppOwner)
  - **Resource types (\*required):** [qapp](#list_qapps-resource-qapp) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qapps-aws_ResourceTag___TagKey_)<br />[qapps:AppIsPublished](#list_qapps-qapps_AppIsPublished)<br />[qapps:UserIsAppOwner](#list_qapps-qapps_UserIsAppOwner)
  - **Access level:** Write

- **   [CreateLibraryItemReview](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/purpose-built-qapps.html)  **
  - **Description:** Grants permission to create a library item review in the Q Business application environment
  - **Resource types (\*required):** [application](#list_qapps-resource-application) / **Condition keys:** [qapps:AppIsPublished](#list_qapps-qapps_AppIsPublished)<br />[qapps:UserIsAppOwner](#list_qapps-qapps_UserIsAppOwner)
  - **Resource types (\*required):** [qapp](#list_qapps-resource-qapp) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qapps-aws_ResourceTag___TagKey_)<br />[qapps:AppIsPublished](#list_qapps-qapps_AppIsPublished)<br />[qapps:UserIsAppOwner](#list_qapps-qapps_UserIsAppOwner)
  - **Access level:** Write

- **   [CreateSubscriptionToken](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/purpose-built-qapps.html)  **
  - **Description:** Grants permission to subscribe to a Q App event bus topic in the Q Business application environment
  - **Resource types (\*required):** [application\*](#list_qapps-resource-application)
  - **Condition keys:**  
  - **Access level:** Write

- **   [PredictProblemStatementFromConversation](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/purpose-built-qapps.html)  **
  - **Description:** Grants permission to predict problem statement from conversation log in the Q Business application environment
  - **Resource types (\*required):** [application\*](#list_qapps-resource-application)
  - **Condition keys:**  
  - **Access level:** Write

- **   [PredictQAppFromProblemStatement](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/purpose-built-qapps.html)  **
  - **Description:** Grants permission to predict Q App metadata from problem statement in the Q Business application environment
  - **Resource types (\*required):** [application\*](#list_qapps-resource-application)
  - **Condition keys:**  
  - **Access level:** Write



## Resource types defined by Amazon Q Business Q Apps
<a name="list_qapps-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [application](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-app.html)  | arn:${Partition}:qbusiness:${Region}:${Account}:application/${ApplicationId} |   | 
|  [qapp](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/purpose-built-qapps.html)  | arn:${Partition}:qapps:${Region}:${Account}:application/${ApplicationId}/qapp/${AppId} | [aws:ResourceTag/${TagKey}](#list_qapps-aws_ResourceTag___TagKey_) | 
|  [qapp-session](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/purpose-built-qapps.html)  | arn:${Partition}:qapps:${Region}:${Account}:application/${ApplicationId}/qapp/${AppId}/session/${SessionId} | [aws:ResourceTag/${TagKey}](#list_qapps-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon Q Business Q Apps
<a name="list_qapps-policy-keys"></a>

Amazon Q Business Q Apps defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 
|   [qapps:AppIsPublished](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/security-iam.html)  | Filters access by whether Q App is published | String | 
|   [qapps:SessionIsShared](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/security-iam.html)  | Filters access by whether Q App Session is shared | String | 
|   [qapps:UserIsAppOwner](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/security-iam.html)  | Filters access by whether requester is Q App owner | String | 
|   [qapps:UserIsSessionModerator](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/security-iam.html)  | Filters access by whether requester is Q App Session moderator | String | 