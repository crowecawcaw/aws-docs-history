

# Actions, resources, and condition keys for AWS IoT TwinMaker
<a name="list_iottwinmaker"></a>

AWS IoT TwinMaker (service prefix: `iottwinmaker`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/iottwinmaker/iottwinmaker.json) for this service.

**Topics**
+ [API operations defined by AWS IoT TwinMaker](#list_iottwinmaker-operations)
+ [Actions defined by AWS IoT TwinMaker](#list_iottwinmaker-actions-as-permissions)
+ [Resource types defined by AWS IoT TwinMaker](#list_iottwinmaker-resources-for-iam-policies)
+ [Condition keys for AWS IoT TwinMaker](#list_iottwinmaker-policy-keys)

## API operations defined by AWS IoT TwinMaker
<a name="list_iottwinmaker-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_iottwinmaker-actions-as-permissions).




- **   BatchPutPropertyValues  **
  - **IAM action:**  [iottwinmaker:BatchPutPropertyValues](#list_iottwinmaker-action-BatchPutPropertyValues) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelMetadataTransferJob  **
  - **IAM action:**  [iottwinmaker:CancelMetadataTransferJob](#list_iottwinmaker-action-CancelMetadataTransferJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateComponentType  **
  - **IAM action:**  [iottwinmaker:CreateComponentType](#list_iottwinmaker-action-CreateComponentType)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iottwinmaker:TagResource](#list_iottwinmaker-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateEntity  **
  - **IAM action:**  [iottwinmaker:CreateEntity](#list_iottwinmaker-action-CreateEntity)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iottwinmaker:TagResource](#list_iottwinmaker-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateMetadataTransferJob  **
  - **IAM action:**  [iottwinmaker:CreateMetadataTransferJob](#list_iottwinmaker-action-CreateMetadataTransferJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateScene  **
  - **IAM action:**  [iottwinmaker:CreateScene](#list_iottwinmaker-action-CreateScene)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iottwinmaker:TagResource](#list_iottwinmaker-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateSyncJob  **
  - **IAM action:**  [iottwinmaker:CreateSyncJob](#list_iottwinmaker-action-CreateSyncJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iottwinmaker:TagResource](#list_iottwinmaker-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** iottwinmaker.amazonaws.com / **Access level:** Write

- **   CreateWorkspace  **
  - **IAM action:**  [iottwinmaker:CreateWorkspace](#list_iottwinmaker-action-CreateWorkspace)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iottwinmaker:TagResource](#list_iottwinmaker-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** iottwinmaker.amazonaws.com / **Access level:** Write

- **   DeleteComponentType  **
  - **IAM action:**  [iottwinmaker:DeleteComponentType](#list_iottwinmaker-action-DeleteComponentType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEntity  **
  - **IAM action:**  [iottwinmaker:DeleteEntity](#list_iottwinmaker-action-DeleteEntity) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteScene  **
  - **IAM action:**  [iottwinmaker:DeleteScene](#list_iottwinmaker-action-DeleteScene) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSyncJob  **
  - **IAM action:**  [iottwinmaker:DeleteSyncJob](#list_iottwinmaker-action-DeleteSyncJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteWorkspace  **
  - **IAM action:**  [iottwinmaker:DeleteWorkspace](#list_iottwinmaker-action-DeleteWorkspace) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ExecuteQuery  **
  - **IAM action:**  [iottwinmaker:ExecuteQuery](#list_iottwinmaker-action-ExecuteQuery) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetComponentType  **
  - **IAM action:**  [iottwinmaker:GetComponentType](#list_iottwinmaker-action-GetComponentType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEntity  **
  - **IAM action:**  [iottwinmaker:GetEntity](#list_iottwinmaker-action-GetEntity) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMetadataTransferJob  **
  - **IAM action:**  [iottwinmaker:GetMetadataTransferJob](#list_iottwinmaker-action-GetMetadataTransferJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPricingPlan  **
  - **IAM action:**  [iottwinmaker:GetPricingPlan](#list_iottwinmaker-action-GetPricingPlan) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPropertyValue  **
  - **IAM action:**  [iottwinmaker:GetPropertyValue](#list_iottwinmaker-action-GetPropertyValue) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPropertyValueHistory  **
  - **IAM action:**  [iottwinmaker:GetPropertyValueHistory](#list_iottwinmaker-action-GetPropertyValueHistory) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetScene  **
  - **IAM action:**  [iottwinmaker:GetScene](#list_iottwinmaker-action-GetScene) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSyncJob  **
  - **IAM action:**  [iottwinmaker:GetSyncJob](#list_iottwinmaker-action-GetSyncJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetWorkspace  **
  - **IAM action:**  [iottwinmaker:GetWorkspace](#list_iottwinmaker-action-GetWorkspace) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListComponentTypes  **
  - **IAM action:**  [iottwinmaker:ListComponentTypes](#list_iottwinmaker-action-ListComponentTypes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListComponents  **
  - **IAM action:**  [iottwinmaker:ListComponents](#list_iottwinmaker-action-ListComponents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEntities  **
  - **IAM action:**  [iottwinmaker:ListEntities](#list_iottwinmaker-action-ListEntities) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMetadataTransferJobs  **
  - **IAM action:**  [iottwinmaker:ListMetadataTransferJobs](#list_iottwinmaker-action-ListMetadataTransferJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListProperties  **
  - **IAM action:**  [iottwinmaker:ListProperties](#list_iottwinmaker-action-ListProperties) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListScenes  **
  - **IAM action:**  [iottwinmaker:ListScenes](#list_iottwinmaker-action-ListScenes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSyncJobs  **
  - **IAM action:**  [iottwinmaker:ListSyncJobs](#list_iottwinmaker-action-ListSyncJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSyncResources  **
  - **IAM action:**  [iottwinmaker:ListSyncResources](#list_iottwinmaker-action-ListSyncResources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [iottwinmaker:ListTagsForResource](#list_iottwinmaker-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListWorkspaces  **
  - **IAM action:**  [iottwinmaker:ListWorkspaces](#list_iottwinmaker-action-ListWorkspaces) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   TagResource  **
  - **IAM action:**  [iottwinmaker:TagResource](#list_iottwinmaker-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [iottwinmaker:UntagResource](#list_iottwinmaker-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateComponentType  **
  - **IAM action:**  [iottwinmaker:UpdateComponentType](#list_iottwinmaker-action-UpdateComponentType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateEntity  **
  - **IAM action:**  [iottwinmaker:UpdateEntity](#list_iottwinmaker-action-UpdateEntity) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdatePricingPlan  **
  - **IAM action:**  [iottwinmaker:UpdatePricingPlan](#list_iottwinmaker-action-UpdatePricingPlan) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateScene  **
  - **IAM action:**  [iottwinmaker:UpdateScene](#list_iottwinmaker-action-UpdateScene) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateWorkspace  **
  - **IAM action:**  [iottwinmaker:UpdateWorkspace](#list_iottwinmaker-action-UpdateWorkspace)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** iottwinmaker.amazonaws.com / **Access level:** Write



## Actions defined by AWS IoT TwinMaker
<a name="list_iottwinmaker-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [BatchPutPropertyValues](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_BatchPutPropertyValues.html)  **
  - **Description:** Grants permission to set values for multiple time series properties
  - **Resource types (\*required):** [entity](#list_iottwinmaker-resource-entity) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workspace\*](#list_iottwinmaker-resource-workspace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CancelMetadataTransferJob](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_CancelMetadataTransferJob.html)  **
  - **Description:** Grants permission to cancel a metadata transfer job
  - **Resource types (\*required):** [metadataTransferJob\*](#list_iottwinmaker-resource-metadataTransferJob)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateComponentType](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_CreateComponentType.html)  **
  - **Description:** Grants permission to create a componentType
  - **Resource types (\*required):** [workspace\*](#list_iottwinmaker-resource-workspace)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iottwinmaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iottwinmaker-aws_TagKeys)
  - **Access level:** Write

- **   [CreateEntity](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_CreateEntity.html)  **
  - **Description:** Grants permission to create an entity
  - **Resource types (\*required):** [workspace\*](#list_iottwinmaker-resource-workspace)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iottwinmaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iottwinmaker-aws_TagKeys)
  - **Access level:** Write

- **   [CreateMetadataTransferJob](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_CreateMetadataTransferJob.html)  **
  - **Description:** Grants permission to create a metadata transfer job
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateScene](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_CreateScene.html)  **
  - **Description:** Grants permission to create a scene
  - **Resource types (\*required):** [workspace\*](#list_iottwinmaker-resource-workspace)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iottwinmaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iottwinmaker-aws_TagKeys)
  - **Access level:** Write

- **   [CreateSyncJob](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_CreateSyncJob.html)  **
  - **Description:** Grants permission to create a sync job
  - **Resource types (\*required):** [workspace\*](#list_iottwinmaker-resource-workspace)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iottwinmaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iottwinmaker-aws_TagKeys)
  - **Access level:** Write

- **   [CreateWorkspace](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_CreateWorkspace.html)  **
  - **Description:** Grants permission to create a workspace
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iottwinmaker-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iottwinmaker-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteComponentType](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_DeleteComponentType.html)  **
  - **Description:** Grants permission to delete a componentType
  - **Resource types (\*required):** [componentType\*](#list_iottwinmaker-resource-componentType) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workspace\*](#list_iottwinmaker-resource-workspace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteEntity](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_DeleteEntity.html)  **
  - **Description:** Grants permission to delete an entity
  - **Resource types (\*required):** [entity\*](#list_iottwinmaker-resource-entity) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workspace\*](#list_iottwinmaker-resource-workspace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteScene](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_DeleteScene.html)  **
  - **Description:** Grants permission to delete a scene
  - **Resource types (\*required):** [scene\*](#list_iottwinmaker-resource-scene) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workspace\*](#list_iottwinmaker-resource-workspace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSyncJob](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_DeleteSyncJob.html)  **
  - **Description:** Grants permission to delete a sync job
  - **Resource types (\*required):** [syncJob\*](#list_iottwinmaker-resource-syncJob) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workspace\*](#list_iottwinmaker-resource-workspace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteWorkspace](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_DeleteWorkspace.html)  **
  - **Description:** Grants permission to delete a workspace
  - **Resource types (\*required):** [workspace\*](#list_iottwinmaker-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ExecuteQuery](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_ExecuteQuery.html)  **
  - **Description:** Grants permission to execute query
  - **Resource types (\*required):** [workspace\*](#list_iottwinmaker-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetComponentType](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_GetComponentType.html)  **
  - **Description:** Grants permission to get a componentType
  - **Resource types (\*required):** [componentType\*](#list_iottwinmaker-resource-componentType) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workspace\*](#list_iottwinmaker-resource-workspace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetEntity](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_GetEntity.html)  **
  - **Description:** Grants permission to get an entity
  - **Resource types (\*required):** [entity\*](#list_iottwinmaker-resource-entity) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workspace\*](#list_iottwinmaker-resource-workspace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetMetadataTransferJob](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_GetMetadataTransferJob.html)  **
  - **Description:** Grants permission to get a metadata transfer job
  - **Resource types (\*required):** [metadataTransferJob\*](#list_iottwinmaker-resource-metadataTransferJob)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetPricingPlan](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_GetPricingPlan.html)  **
  - **Description:** Grants permission to get pricing plan
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetPropertyValue](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_GetPropertyValue.html)  **
  - **Description:** Grants permission to retrieve the property values
  - **Resource types (\*required):** [componentType](#list_iottwinmaker-resource-componentType) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [entity](#list_iottwinmaker-resource-entity) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workspace\*](#list_iottwinmaker-resource-workspace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPropertyValueHistory](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_GetPropertyValueHistory.html)  **
  - **Description:** Grants permission to retrieve the time series value history
  - **Resource types (\*required):** [componentType](#list_iottwinmaker-resource-componentType) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [entity](#list_iottwinmaker-resource-entity) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workspace\*](#list_iottwinmaker-resource-workspace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetScene](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_GetScene.html)  **
  - **Description:** Grants permission to get a scene
  - **Resource types (\*required):** [scene\*](#list_iottwinmaker-resource-scene) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workspace\*](#list_iottwinmaker-resource-workspace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSyncJob](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_GetSyncJob.html)  **
  - **Description:** Grants permission to get a sync job
  - **Resource types (\*required):** [syncJob\*](#list_iottwinmaker-resource-syncJob) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workspace\*](#list_iottwinmaker-resource-workspace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetWorkspace](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_GetWorkspace.html)  **
  - **Description:** Grants permission to get a workspace
  - **Resource types (\*required):** [workspace\*](#list_iottwinmaker-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListComponentTypes](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_ListComponentTypes.html)  **
  - **Description:** Grants permission to list all componentTypes in a workspace
  - **Resource types (\*required):** [workspace\*](#list_iottwinmaker-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListComponents](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_ListComponents.html)  **
  - **Description:** Grants permission to list components attached to an entity
  - **Resource types (\*required):** [entity\*](#list_iottwinmaker-resource-entity) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workspace\*](#list_iottwinmaker-resource-workspace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListEntities](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_ListEntities.html)  **
  - **Description:** Grants permission to list all entities in a workspace
  - **Resource types (\*required):** [workspace\*](#list_iottwinmaker-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListMetadataTransferJobs](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_ListMetadataTransferJobs.html)  **
  - **Description:** Grants permission to list all metadata transfer jobs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListProperties](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_ListProperties.html)  **
  - **Description:** Grants permission to list properties of an entity component
  - **Resource types (\*required):** [entity\*](#list_iottwinmaker-resource-entity) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workspace\*](#list_iottwinmaker-resource-workspace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListScenes](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_ListScenes.html)  **
  - **Description:** Grants permission to list all scenes in a workspace
  - **Resource types (\*required):** [workspace\*](#list_iottwinmaker-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListSyncJobs](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_ListSyncJobs.html)  **
  - **Description:** Grants permission to list all sync jobs in a workspace
  - **Resource types (\*required):** [workspace\*](#list_iottwinmaker-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListSyncResources](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_ListSyncResources.html)  **
  - **Description:** Grants permission to list all sync resources for a sync job
  - **Resource types (\*required):** [syncJob\*](#list_iottwinmaker-resource-syncJob) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workspace\*](#list_iottwinmaker-resource-workspace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list all tags for a resource
  - **Resource types (\*required):** [componentType](#list_iottwinmaker-resource-componentType) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [entity](#list_iottwinmaker-resource-entity) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [scene](#list_iottwinmaker-resource-scene) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [syncJob](#list_iottwinmaker-resource-syncJob) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workspace](#list_iottwinmaker-resource-workspace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListWorkspaces](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_ListWorkspaces.html)  **
  - **Description:** Grants permission to list all workspaces
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [TagResource](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_TagResource.html)  **
  - **Description:** Grants permission to tag a resource
  - **Resource types (\*required):** [componentType](#list_iottwinmaker-resource-componentType) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iottwinmaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iottwinmaker-aws_TagKeys)
  - **Resource types (\*required):** [entity](#list_iottwinmaker-resource-entity) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iottwinmaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iottwinmaker-aws_TagKeys)
  - **Resource types (\*required):** [scene](#list_iottwinmaker-resource-scene) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iottwinmaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iottwinmaker-aws_TagKeys)
  - **Resource types (\*required):** [syncJob](#list_iottwinmaker-resource-syncJob) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iottwinmaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iottwinmaker-aws_TagKeys)
  - **Resource types (\*required):** [workspace](#list_iottwinmaker-resource-workspace) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iottwinmaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iottwinmaker-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_UntagResource.html)  **
  - **Description:** Grants permission to untag a resource
  - **Resource types (\*required):** [componentType](#list_iottwinmaker-resource-componentType) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iottwinmaker-aws_TagKeys)
  - **Resource types (\*required):** [entity](#list_iottwinmaker-resource-entity) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iottwinmaker-aws_TagKeys)
  - **Resource types (\*required):** [scene](#list_iottwinmaker-resource-scene) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iottwinmaker-aws_TagKeys)
  - **Resource types (\*required):** [syncJob](#list_iottwinmaker-resource-syncJob) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iottwinmaker-aws_TagKeys)
  - **Resource types (\*required):** [workspace](#list_iottwinmaker-resource-workspace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iottwinmaker-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateComponentType](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_UpdateComponentType.html)  **
  - **Description:** Grants permission to update a componentType
  - **Resource types (\*required):** [componentType\*](#list_iottwinmaker-resource-componentType) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workspace\*](#list_iottwinmaker-resource-workspace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateEntity](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_UpdateEntity.html)  **
  - **Description:** Grants permission to update an entity
  - **Resource types (\*required):** [entity\*](#list_iottwinmaker-resource-entity) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workspace\*](#list_iottwinmaker-resource-workspace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdatePricingPlan](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_UpdatePricingPlan.html)  **
  - **Description:** Grants permission to update pricing plan
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateScene](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_UpdateScene.html)  **
  - **Description:** Grants permission to update a scene
  - **Resource types (\*required):** [scene\*](#list_iottwinmaker-resource-scene) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workspace\*](#list_iottwinmaker-resource-workspace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateWorkspace](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_UpdateWorkspace.html)  **
  - **Description:** Grants permission to update a workspace
  - **Resource types (\*required):** [workspace\*](#list_iottwinmaker-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS IoT TwinMaker
<a name="list_iottwinmaker-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [componentType](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_CreateComponentType.html)  | arn:${Partition}:iottwinmaker:${Region}:${Account}:workspace/${WorkspaceId}/component-type/${ComponentTypeId} | [aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_) | 
|  [entity](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_CreateEntity.html)  | arn:${Partition}:iottwinmaker:${Region}:${Account}:workspace/${WorkspaceId}/entity/${EntityId} | [aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_) | 
|  [metadataTransferJob](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_CreateMetadataTransferJob.html)  | arn:${Partition}:iottwinmaker:${Region}:${Account}:metadata-transfer-job/${MetadataTransferJobId} |   | 
|  [scene](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_CreateScene.html)  | arn:${Partition}:iottwinmaker:${Region}:${Account}:workspace/${WorkspaceId}/scene/${SceneId} | [aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_) | 
|  [syncJob](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_CreateSyncJob.html)  | arn:${Partition}:iottwinmaker:${Region}:${Account}:workspace/${WorkspaceId}/sync-job/${SyncJobId} | [aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_) | 
|  [workspace](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_CreateWorkspace.html)  | arn:${Partition}:iottwinmaker:${Region}:${Account}:workspace/${WorkspaceId} | [aws:ResourceTag/${TagKey}](#list_iottwinmaker-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS IoT TwinMaker
<a name="list_iottwinmaker-policy-keys"></a>

AWS IoT TwinMaker defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys in the request | ArrayOfString | 
|   [iottwinmaker:destinationType](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiottwinmaker.html#awsiottwinmaker-policy-keys)  | Filters access by destination type of metadata transfer job | String | 
|   [iottwinmaker:linkedServices](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiottwinmaker.html#awsiottwinmaker-policy-keys)  | Filters access by workspace linked to services | ArrayOfString | 
|   [iottwinmaker:sourceType](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiottwinmaker.html#awsiottwinmaker-policy-keys)  | Filters access by source type of metadata transfer job | String | 