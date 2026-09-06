

# Actions, resources, and condition keys for AWS Data Exchange
<a name="list_dataexchange"></a>

AWS Data Exchange (service prefix: `dataexchange`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/data-exchange/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/data-exchange/latest/apireference/welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/data-exchange/latest/userguide/auth-access.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/dataexchange/dataexchange.json) for this service.

**Topics**
+ [API operations defined by AWS Data Exchange](#list_dataexchange-operations)
+ [Actions defined by AWS Data Exchange](#list_dataexchange-actions-as-permissions)
+ [Permission-only actions for AWS Data Exchange](#list_dataexchange-permission-only-actions)
+ [Resource types defined by AWS Data Exchange](#list_dataexchange-resources-for-iam-policies)
+ [Condition keys for AWS Data Exchange](#list_dataexchange-policy-keys)

## API operations defined by AWS Data Exchange
<a name="list_dataexchange-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_dataexchange-actions-as-permissions).




- **   AcceptDataGrant  **
  - **IAM action:**  [dataexchange:AcceptDataGrant](#list_dataexchange-action-AcceptDataGrant)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [aws-marketplace:Subscribe](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-iam-users-groups-policies.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CancelJob  **
  - **IAM action:**  [dataexchange:CancelJob](#list_dataexchange-action-CancelJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateDataGrant  **
  - **IAM action:**  [dataexchange:CreateDataGrant](#list_dataexchange-action-CreateDataGrant)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dataexchange:CreateJob](#list_dataexchange-action-CreateJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dataexchange:PublishDataSet](#list_dataexchange-action-PublishDataSet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dataexchange:PublishToDataGrant](#list_dataexchange-action-PublishToDataGrant)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dataexchange:StartJob](#list_dataexchange-action-StartJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dataexchange:TagResource](#list_dataexchange-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateDataSet  **
  - **IAM action:**  [dataexchange:CreateDataSet](#list_dataexchange-action-CreateDataSet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dataexchange:TagResource](#list_dataexchange-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateEventAction  **
  - **IAM action:**  [dataexchange:CreateEventAction](#list_dataexchange-action-CreateEventAction)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dataexchange:TagResource](#list_dataexchange-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateJob  **
  - **IAM action:**  [dataexchange:CreateJob](#list_dataexchange-action-CreateJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** dataexchange.amazonaws.com / **Access level:** Write

- **   CreateRevision  **
  - **IAM action:**  [dataexchange:CreateRevision](#list_dataexchange-action-CreateRevision)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dataexchange:TagResource](#list_dataexchange-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteAsset  **
  - **IAM action:**  [dataexchange:DeleteAsset](#list_dataexchange-action-DeleteAsset) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDataGrant  **
  - **IAM action:**  [dataexchange:CreateJob](#list_dataexchange-action-CreateJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dataexchange:DeleteDataGrant](#list_dataexchange-action-DeleteDataGrant)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dataexchange:DeleteDataSet](#list_dataexchange-action-DeleteDataSet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dataexchange:StartJob](#list_dataexchange-action-StartJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteDataSet  **
  - **IAM action:**  [dataexchange:DeleteDataSet](#list_dataexchange-action-DeleteDataSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEventAction  **
  - **IAM action:**  [dataexchange:DeleteEventAction](#list_dataexchange-action-DeleteEventAction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRevision  **
  - **IAM action:**  [dataexchange:DeleteRevision](#list_dataexchange-action-DeleteRevision) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAsset  **
  - **IAM action:**  [dataexchange:GetAsset](#list_dataexchange-action-GetAsset) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDataGrant  **
  - **IAM action:**  [dataexchange:GetDataGrant](#list_dataexchange-action-GetDataGrant)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [dataexchange:GetDataSet](#list_dataexchange-action-GetDataSet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetDataSet  **
  - **IAM action:**  [dataexchange:GetDataSet](#list_dataexchange-action-GetDataSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEventAction  **
  - **IAM action:**  [dataexchange:GetEventAction](#list_dataexchange-action-GetEventAction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetJob  **
  - **IAM action:**  [dataexchange:GetJob](#list_dataexchange-action-GetJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetReceivedDataGrant  **
  - **IAM action:**  [dataexchange:GetDataSet](#list_dataexchange-action-GetDataSet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [dataexchange:GetReceivedDataGrant](#list_dataexchange-action-GetReceivedDataGrant)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetRevision  **
  - **IAM action:**  [dataexchange:GetRevision](#list_dataexchange-action-GetRevision) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListDataGrants  **
  - **IAM action:**  [dataexchange:ListDataGrants](#list_dataexchange-action-ListDataGrants)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [dataexchange:ListDataSets](#list_dataexchange-action-ListDataSets)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ListDataSetRevisions  **
  - **IAM action:**  [dataexchange:ListDataSetRevisions](#list_dataexchange-action-ListDataSetRevisions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDataSets  **
  - **IAM action:**  [dataexchange:ListDataSets](#list_dataexchange-action-ListDataSets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEventActions  **
  - **IAM action:**  [dataexchange:ListEventActions](#list_dataexchange-action-ListEventActions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListJobs  **
  - **IAM action:**  [dataexchange:ListJobs](#list_dataexchange-action-ListJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListReceivedDataGrants  **
  - **IAM action:**  [dataexchange:ListDataSets](#list_dataexchange-action-ListDataSets)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [dataexchange:ListReceivedDataGrants](#list_dataexchange-action-ListReceivedDataGrants)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ListRevisionAssets  **
  - **IAM action:**  [dataexchange:ListRevisionAssets](#list_dataexchange-action-ListRevisionAssets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [dataexchange:ListTagsForResource](#list_dataexchange-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   RevokeRevision  **
  - **IAM action:**  [dataexchange:RevokeRevision](#list_dataexchange-action-RevokeRevision) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SendApiAsset  **
  - **IAM action:**  [dataexchange:SendApiAsset](#list_dataexchange-action-SendApiAsset) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SendDataSetNotification  **
  - **IAM action:**  [dataexchange:SendDataSetNotification](#list_dataexchange-action-SendDataSetNotification) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartJob  **
  - **IAM action:**  [dataexchange:CreateAsset](#list_dataexchange-action-CreateAsset)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dataexchange:StartJob](#list_dataexchange-action-StartJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dataexchange:TagResource](#list_dataexchange-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   TagResource  **
  - **IAM action:**  [dataexchange:TagResource](#list_dataexchange-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [dataexchange:UntagResource](#list_dataexchange-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateAsset  **
  - **IAM action:**  [dataexchange:UpdateAsset](#list_dataexchange-action-UpdateAsset) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDataSet  **
  - **IAM action:**  [dataexchange:UpdateDataSet](#list_dataexchange-action-UpdateDataSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateEventAction  **
  - **IAM action:**  [dataexchange:UpdateEventAction](#list_dataexchange-action-UpdateEventAction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRevision  **
  - **IAM action:**  [dataexchange:PublishDataSet](#list_dataexchange-action-PublishDataSet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dataexchange:PublishToDataGrant](#list_dataexchange-action-PublishToDataGrant)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dataexchange:UpdateRevision](#list_dataexchange-action-UpdateRevision)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write



## Actions defined by AWS Data Exchange
<a name="list_dataexchange-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AcceptDataGrant](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_AcceptDataGrant.html)  **
  - **Description:** Grants permission to accept a data grant
  - **Resource types (\*required):** [data-grants\*](#list_dataexchange-resource-data-grants)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dataexchange-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CancelJob](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_CancelJob.html)  **
  - **Description:** Grants permission to cancel a job
  - **Resource types (\*required):** [jobs\*](#list_dataexchange-resource-jobs)
  - **Condition keys:** [dataexchange:JobType](#list_dataexchange-dataexchange_JobType)
  - **Access level:** Write

- **   [CreateDataGrant](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_CreateDataGrant.html)  **
  - **Description:** Grants permission to create a data grant
  - **Resource types (\*required):** [data-grants\*](#list_dataexchange-resource-data-grants)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_dataexchange-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_dataexchange-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dataexchange-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDataSet](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_CreateDataSet.html)  **
  - **Description:** Grants permission to create a data set
  - **Resource types (\*required):** [data-sets\*](#list_dataexchange-resource-data-sets)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_dataexchange-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_dataexchange-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dataexchange-aws_TagKeys)
  - **Access level:** Write

- **   [CreateEventAction](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_CreateEventAction.html)  **
  - **Description:** Grants permission to create an event action
  - **Resource types (\*required):** [event-actions\*](#list_dataexchange-resource-event-actions)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_dataexchange-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_dataexchange-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dataexchange-aws_TagKeys)
  - **Access level:** Write

- **   [CreateJob](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_CreateJob.html)  **
  - **Description:** Grants permission to create a job to import or export assets
  - **Resource types (\*required):** [jobs\*](#list_dataexchange-resource-jobs)
  - **Condition keys:** [dataexchange:JobType](#list_dataexchange-dataexchange_JobType)
  - **Access level:** Write

- **   [CreateRevision](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_CreateRevision.html)  **
  - **Description:** Grants permission to create a revision
  - **Resource types (\*required):** [data-sets\*](#list_dataexchange-resource-data-sets)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_dataexchange-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_dataexchange-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dataexchange-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteAsset](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_DeleteAsset.html)  **
  - **Description:** Grants permission to delete an asset
  - **Resource types (\*required):** [assets\*](#list_dataexchange-resource-assets)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dataexchange-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDataGrant](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_DeleteDataGrant.html)  **
  - **Description:** Grants permission to delete a data grant
  - **Resource types (\*required):** [data-grants\*](#list_dataexchange-resource-data-grants)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dataexchange-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDataSet](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_DeleteDataSet.html)  **
  - **Description:** Grants permission to delete a data set
  - **Resource types (\*required):** [data-sets\*](#list_dataexchange-resource-data-sets) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dataexchange-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [entitled-data-sets\*](#list_dataexchange-resource-entitled-data-sets) / **Condition keys:**  
  - **Access level:** Write

- **   [DeleteEventAction](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_DeleteEventAction.html)  **
  - **Description:** Grants permission to delete an event action
  - **Resource types (\*required):** [event-actions\*](#list_dataexchange-resource-event-actions)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dataexchange-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRevision](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_DeleteRevision.html)  **
  - **Description:** Grants permission to delete a revision
  - **Resource types (\*required):** [revisions\*](#list_dataexchange-resource-revisions)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dataexchange-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetAsset](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_GetAsset.html)  **
  - **Description:** Grants permission to get information about an asset and to export it (for example, in a Job)
  - **Resource types (\*required):** [assets\*](#list_dataexchange-resource-assets) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dataexchange-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [entitled-assets\*](#list_dataexchange-resource-entitled-assets) / **Condition keys:**  
  - **Access level:** Read

- **   [GetDataGrant](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_GetDataGrant.html)  **
  - **Description:** Grants permission to get a data grant
  - **Resource types (\*required):** [data-grants\*](#list_dataexchange-resource-data-grants)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dataexchange-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDataSet](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_GetDataSet.html)  **
  - **Description:** Grants permission to get information about a data set
  - **Resource types (\*required):** [data-sets\*](#list_dataexchange-resource-data-sets) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dataexchange-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [entitled-data-sets\*](#list_dataexchange-resource-entitled-data-sets) / **Condition keys:**  
  - **Access level:** Read

- **   [GetEventAction](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_GetEventAction.html)  **
  - **Description:** Grants permission to get an event action
  - **Resource types (\*required):** [event-actions\*](#list_dataexchange-resource-event-actions)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dataexchange-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetJob](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_GetJob.html)  **
  - **Description:** Grants permission to get information about a job
  - **Resource types (\*required):** [jobs\*](#list_dataexchange-resource-jobs)
  - **Condition keys:** [dataexchange:JobType](#list_dataexchange-dataexchange_JobType)
  - **Access level:** Read

- **   [GetReceivedDataGrant](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_GetReceivedDataGrant.html)  **
  - **Description:** Grants permission to get a received data grant
  - **Resource types (\*required):** [data-grants\*](#list_dataexchange-resource-data-grants)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dataexchange-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRevision](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_GetRevision.html)  **
  - **Description:** Grants permission to get information about a revision
  - **Resource types (\*required):** [entitled-revisions\*](#list_dataexchange-resource-entitled-revisions) / **Condition keys:**  
  - **Resource types (\*required):** [revisions\*](#list_dataexchange-resource-revisions) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dataexchange-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListDataGrants](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_ListDataGrants.html)  **
  - **Description:** Grants permission to list data grants for the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDataSetRevisions](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_ListDataSetRevisions.html)  **
  - **Description:** Grants permission to list the revisions of a data set
  - **Resource types (\*required):** [data-sets\*](#list_dataexchange-resource-data-sets) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dataexchange-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [entitled-data-sets\*](#list_dataexchange-resource-entitled-data-sets) / **Condition keys:**  
  - **Access level:** List

- **   [ListDataSets](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_ListDataSets.html)  **
  - **Description:** Grants permission to list data sets for the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListEventActions](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_ListEventActions.html)  **
  - **Description:** Grants permission to list event actions for the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListJobs](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_ListJobs.html)  **
  - **Description:** Grants permission to list jobs for the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListReceivedDataGrants](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_ListReceivedDataGrants.html)  **
  - **Description:** Grants permission to list received data grants for the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRevisionAssets](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_ListRevisionAssets.html)  **
  - **Description:** Grants permission to get list the assets of a revision
  - **Resource types (\*required):** [entitled-revisions\*](#list_dataexchange-resource-entitled-revisions) / **Condition keys:**  
  - **Resource types (\*required):** [revisions\*](#list_dataexchange-resource-revisions) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dataexchange-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list the tags that you associated with the specified resource
  - **Resource types (\*required):** [assets](#list_dataexchange-resource-assets) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dataexchange-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [data-grants](#list_dataexchange-resource-data-grants) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dataexchange-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [data-sets](#list_dataexchange-resource-data-sets) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dataexchange-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [event-actions](#list_dataexchange-resource-event-actions) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dataexchange-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [revisions](#list_dataexchange-resource-revisions) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dataexchange-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [RevokeRevision](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_RevokeRevision.html)  **
  - **Description:** Grants permission to revoke subscriber access to a revision
  - **Resource types (\*required):** [revisions\*](#list_dataexchange-resource-revisions)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dataexchange-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SendApiAsset](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_SendApiAsset.html)  **
  - **Description:** Grants permission to send a request to an API asset
  - **Resource types (\*required):** [assets\*](#list_dataexchange-resource-assets) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dataexchange-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [entitled-assets\*](#list_dataexchange-resource-entitled-assets) / **Condition keys:**  
  - **Access level:** Write

- **   [SendDataSetNotification](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_SendDataSetNotification.html)  **
  - **Description:** Grants permission to send a notification to subscribers of a data set
  - **Resource types (\*required):** [data-sets\*](#list_dataexchange-resource-data-sets)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dataexchange-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartJob](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_StartJob.html)  **
  - **Description:** Grants permission to start a job
  - **Resource types (\*required):** [jobs\*](#list_dataexchange-resource-jobs)
  - **Condition keys:** [dataexchange:JobType](#list_dataexchange-dataexchange_JobType)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_TagResource.html)  **
  - **Description:** Grants permission to add one or more tags to a specified resource
  - **Resource types (\*required):** [assets](#list_dataexchange-resource-assets) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_dataexchange-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_dataexchange-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dataexchange-aws_TagKeys)
  - **Resource types (\*required):** [data-grants](#list_dataexchange-resource-data-grants) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_dataexchange-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_dataexchange-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dataexchange-aws_TagKeys)
  - **Resource types (\*required):** [data-sets](#list_dataexchange-resource-data-sets) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_dataexchange-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_dataexchange-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dataexchange-aws_TagKeys)
  - **Resource types (\*required):** [event-actions](#list_dataexchange-resource-event-actions) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_dataexchange-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_dataexchange-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dataexchange-aws_TagKeys)
  - **Resource types (\*required):** [revisions](#list_dataexchange-resource-revisions) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_dataexchange-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_dataexchange-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dataexchange-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove one or more tags from a specified resource
  - **Resource types (\*required):** [assets](#list_dataexchange-resource-assets) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dataexchange-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dataexchange-aws_TagKeys)
  - **Resource types (\*required):** [data-grants](#list_dataexchange-resource-data-grants) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dataexchange-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dataexchange-aws_TagKeys)
  - **Resource types (\*required):** [data-sets](#list_dataexchange-resource-data-sets) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dataexchange-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dataexchange-aws_TagKeys)
  - **Resource types (\*required):** [event-actions](#list_dataexchange-resource-event-actions) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dataexchange-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dataexchange-aws_TagKeys)
  - **Resource types (\*required):** [revisions](#list_dataexchange-resource-revisions) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dataexchange-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dataexchange-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateAsset](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_UpdateAsset.html)  **
  - **Description:** Grants permission to get update information about an asset
  - **Resource types (\*required):** [assets\*](#list_dataexchange-resource-assets)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dataexchange-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDataSet](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_UpdateDataSet.html)  **
  - **Description:** Grants permission to update information about a data set
  - **Resource types (\*required):** [data-sets\*](#list_dataexchange-resource-data-sets)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dataexchange-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateEventAction](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_UpdateEventAction.html)  **
  - **Description:** Grants permission to update information for an event action
  - **Resource types (\*required):** [event-actions\*](#list_dataexchange-resource-event-actions)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dataexchange-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateRevision](https://docs.aws.amazon.com/data-exchange/latest/apireference/API_UpdateRevision.html)  **
  - **Description:** Grants permission to update information about a revision
  - **Resource types (\*required):** [revisions\*](#list_dataexchange-resource-revisions)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dataexchange-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for AWS Data Exchange
<a name="list_dataexchange-permission-only-actions"></a>

The following actions are defined by AWS Data Exchange but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [CreateAsset](https://docs.aws.amazon.com/data-exchange/latest/userguide/api-permissions-ref.html)  **
  - **Description:** Grants permission to create an asset (for example, in a Job)
  - **Resource types (\*required):** [revisions\*](#list_dataexchange-resource-revisions)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_dataexchange-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_dataexchange-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dataexchange-aws_TagKeys)
  - **Access level:** Write

- **   [PublishDataSet](https://docs.aws.amazon.com/data-exchange/latest/userguide/api-permissions-ref.html)  **
  - **Description:** Grants permission to publish a data set to a product
  - **Resource types (\*required):** [data-sets\*](#list_dataexchange-resource-data-sets)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dataexchange-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PublishToDataGrant](https://docs.aws.amazon.com/data-exchange/latest/userguide/api-permissions-ref.html)  **
  - **Description:** Grants permission to publish a data set to a data grant
  - **Resource types (\*required):** [data-sets\*](#list_dataexchange-resource-data-sets)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_dataexchange-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_dataexchange-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dataexchange-aws_TagKeys)
  - **Access level:** Write



## Resource types defined by AWS Data Exchange
<a name="list_dataexchange-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [assets](https://docs.aws.amazon.com/data-exchange/latest/userguide/data-sets.html#assets)  | arn:${Partition}:dataexchange:${Region}:${Account}:data-sets/${DataSetId}/revisions/${RevisionId}/assets/${AssetId} | [aws:ResourceTag/${TagKey}](#list_dataexchange-aws_ResourceTag___TagKey_) | 
|  [data-grants](https://docs.aws.amazon.com/data-exchange/latest/userguide/data-sets.html)  | arn:${Partition}:dataexchange:${Region}:${Account}:data-grants/${DataGrantId} | [aws:ResourceTag/${TagKey}](#list_dataexchange-aws_ResourceTag___TagKey_) | 
|  [data-sets](https://docs.aws.amazon.com/data-exchange/latest/userguide/data-sets.html)  | arn:${Partition}:dataexchange:${Region}:${Account}:data-sets/${DataSetId} | [aws:ResourceTag/${TagKey}](#list_dataexchange-aws_ResourceTag___TagKey_) | 
|  [entitled-assets](https://docs.aws.amazon.com/data-exchange/latest/userguide/data-sets.html#assets)  | arn:${Partition}:dataexchange:${Region}::data-sets/${DataSetId}/revisions/${RevisionId}/assets/${AssetId} |   | 
|  [entitled-data-sets](https://docs.aws.amazon.com/data-exchange/latest/userguide/data-sets.html)  | arn:${Partition}:dataexchange:${Region}::data-sets/${DataSetId} |   | 
|  [entitled-revisions](https://docs.aws.amazon.com/data-exchange/latest/userguide/data-sets.html#revisions)  | arn:${Partition}:dataexchange:${Region}::data-sets/${DataSetId}/revisions/${RevisionId} |   | 
|  [event-actions](https://docs.aws.amazon.com/data-exchange/latest/userguide/data-sets.html)  | arn:${Partition}:dataexchange:${Region}:${Account}:event-actions/${EventActionId} | [aws:ResourceTag/${TagKey}](#list_dataexchange-aws_ResourceTag___TagKey_) | 
|  [jobs](https://docs.aws.amazon.com/data-exchange/latest/userguide/jobs.html)  | arn:${Partition}:dataexchange:${Region}:${Account}:jobs/${JobId} | [dataexchange:JobType](#list_dataexchange-dataexchange_JobType) | 
|  [revisions](https://docs.aws.amazon.com/data-exchange/latest/userguide/data-sets.html#revisions)  | arn:${Partition}:dataexchange:${Region}:${Account}:data-sets/${DataSetId}/revisions/${RevisionId} | [aws:ResourceTag/${TagKey}](#list_dataexchange-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Data Exchange
<a name="list_dataexchange-policy-keys"></a>

AWS Data Exchange defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-globally-available)  | Filters access by the allowed set of values for each of the mandatory tags in the create request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-globally-available)  | Filters access by the tag value associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-globally-available)  | Filters access by the presence of mandatory tags in the create request | ArrayOfString | 
|   [dataexchange:JobType](https://docs.aws.amazon.com/data-exchange/latest/userguide/access-control.html)  | Filters access by the specified job type | String | 