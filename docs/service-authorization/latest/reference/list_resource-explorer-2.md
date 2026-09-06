

# Actions, resources, and condition keys for AWS Resource Explorer
<a name="list_resource-explorer-2"></a>

AWS Resource Explorer (service prefix: `resource-explorer-2`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/resource-explorer/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/resource-explorer/latest/apireference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/resource-explorer/latest/userguide/security_iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/resource-explorer-2/resource-explorer-2.json) for this service.

**Topics**
+ [API operations defined by AWS Resource Explorer](#list_resource-explorer-2-operations)
+ [Actions defined by AWS Resource Explorer](#list_resource-explorer-2-actions-as-permissions)
+ [Permission-only actions for AWS Resource Explorer](#list_resource-explorer-2-permission-only-actions)
+ [Resource types defined by AWS Resource Explorer](#list_resource-explorer-2-resources-for-iam-policies)
+ [Condition keys for AWS Resource Explorer](#list_resource-explorer-2-policy-keys)

## API operations defined by AWS Resource Explorer
<a name="list_resource-explorer-2-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_resource-explorer-2-actions-as-permissions).




- **   AssociateDefaultView  **
  - **IAM action:**  [resource-explorer-2:AssociateDefaultView](#list_resource-explorer-2-action-AssociateDefaultView) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchGetView  **
  - **IAM action:**  [resource-explorer-2:BatchGetView](#list_resource-explorer-2-action-BatchGetView)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [resource-explorer-2:GetView](#list_resource-explorer-2-action-GetView)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   CreateIndex  **
  - **IAM action:**  [resource-explorer-2:CreateIndex](#list_resource-explorer-2-action-CreateIndex)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [resource-explorer-2:TagResource](#list_resource-explorer-2-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateResourceExplorerSetup  **
  - **IAM action:**  [resource-explorer-2:CreateResourceExplorerSetup](#list_resource-explorer-2-action-CreateResourceExplorerSetup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateView  **
  - **IAM action:**  [resource-explorer-2:CreateView](#list_resource-explorer-2-action-CreateView)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [resource-explorer-2:TagResource](#list_resource-explorer-2-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteIndex  **
  - **IAM action:**  [resource-explorer-2:DeleteIndex](#list_resource-explorer-2-action-DeleteIndex) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteResourceExplorerSetup  **
  - **IAM action:**  [resource-explorer-2:DeleteResourceExplorerSetup](#list_resource-explorer-2-action-DeleteResourceExplorerSetup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteView  **
  - **IAM action:**  [resource-explorer-2:DeleteView](#list_resource-explorer-2-action-DeleteView) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateDefaultView  **
  - **IAM action:**  [resource-explorer-2:DisassociateDefaultView](#list_resource-explorer-2-action-DisassociateDefaultView) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAccountLevelServiceConfiguration  **
  - **IAM action:**  [resource-explorer-2:GetAccountLevelServiceConfiguration](#list_resource-explorer-2-action-GetAccountLevelServiceConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDefaultView  **
  - **IAM action:**  [resource-explorer-2:GetDefaultView](#list_resource-explorer-2-action-GetDefaultView) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetIndex  **
  - **IAM action:**  [resource-explorer-2:GetIndex](#list_resource-explorer-2-action-GetIndex) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetManagedView  **
  - **IAM action:**  [resource-explorer-2:GetManagedView](#list_resource-explorer-2-action-GetManagedView) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResourceExplorerSetup  **
  - **IAM action:**  [resource-explorer-2:GetResourceExplorerSetup](#list_resource-explorer-2-action-GetResourceExplorerSetup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetServiceIndex  **
  - **IAM action:**  [resource-explorer-2:GetServiceIndex](#list_resource-explorer-2-action-GetServiceIndex) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetServiceView  **
  - **IAM action:**  [resource-explorer-2:GetServiceView](#list_resource-explorer-2-action-GetServiceView) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetView  **
  - **IAM action:**  [resource-explorer-2:GetView](#list_resource-explorer-2-action-GetView) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListIndexes  **
  - **IAM action:**  [resource-explorer-2:ListIndexes](#list_resource-explorer-2-action-ListIndexes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListIndexesForMembers  **
  - **IAM action:**  [resource-explorer-2:ListIndexesForMembers](#list_resource-explorer-2-action-ListIndexesForMembers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListManagedViews  **
  - **IAM action:**  [resource-explorer-2:ListManagedViews](#list_resource-explorer-2-action-ListManagedViews) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListResources  **
  - **IAM action:**  [resource-explorer-2:Search](#list_resource-explorer-2-action-Search) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListServiceIndexes  **
  - **IAM action:**  [resource-explorer-2:ListServiceIndexes](#list_resource-explorer-2-action-ListServiceIndexes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListServiceViews  **
  - **IAM action:**  [resource-explorer-2:ListServiceViews](#list_resource-explorer-2-action-ListServiceViews) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListStreamingAccessForServices  **
  - **IAM action:**  [resource-explorer-2:ListStreamingAccessForServices](#list_resource-explorer-2-action-ListStreamingAccessForServices) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSupportedResourceTypes  **
  - **IAM action:**  [resource-explorer-2:ListSupportedResourceTypes](#list_resource-explorer-2-action-ListSupportedResourceTypes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [resource-explorer-2:ListTagsForResource](#list_resource-explorer-2-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListViews  **
  - **IAM action:**  [resource-explorer-2:ListViews](#list_resource-explorer-2-action-ListViews) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   Search  **
  - **IAM action:**  [resource-explorer-2:Search](#list_resource-explorer-2-action-Search) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   TagResource  **
  - **IAM action:**  [resource-explorer-2:TagResource](#list_resource-explorer-2-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [resource-explorer-2:UntagResource](#list_resource-explorer-2-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateIndexType  **
  - **IAM action:**  [resource-explorer-2:UpdateIndexType](#list_resource-explorer-2-action-UpdateIndexType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateView  **
  - **IAM action:**  [resource-explorer-2:UpdateView](#list_resource-explorer-2-action-UpdateView) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Resource Explorer
<a name="list_resource-explorer-2-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AssociateDefaultView](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_AssociateDefaultView.html)  **
  - **Description:** Grants permission to set the specified view as the default for this AWS Region in this AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [BatchGetView](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_BatchGetView.html)  **
  - **Description:** Grants permission to retrieve details about views that you specify by a list of ARNs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [CreateIndex](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_CreateIndex.html)  **
  - **Description:** Grants permission to turn on Resource Explorer in the AWS Region in which you called this operation by creating an index
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_resource-explorer-2-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_resource-explorer-2-aws_TagKeys)
  - **Access level:** Write

- **   [CreateResourceExplorerSetup](API_CreateResourceExplorerSetup.html)  **
  - **Description:** Grants permission to create resource explorer setup
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateView](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_CreateView.html)  **
  - **Description:** Grants permission to create a view that users can query
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_resource-explorer-2-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_resource-explorer-2-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteIndex](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_DeleteIndex.html)  **
  - **Description:** Grants permission to turn off Resource Explorer in the specified AWS Region by deleting the index
  - **Resource types (\*required):** [index\*](#list_resource-explorer-2-resource-index)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resource-explorer-2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteResourceExplorerSetup](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_DeleteResourceExplorerSetup.html)  **
  - **Description:** Grants permission to delete resource explorer setup
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteView](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_DeleteView.html)  **
  - **Description:** Grants permission to delete a view
  - **Resource types (\*required):** [view\*](#list_resource-explorer-2-resource-view)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resource-explorer-2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateDefaultView](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_DisassociateDefaultView.html)  **
  - **Description:** Grants permission to remove the default view for the AWS Region in which you call this operation
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [GetAccountLevelServiceConfiguration](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_GetAccountLevelServiceConfiguration.html)  **
  - **Description:** Grants permission to Resource Explorer to access account level data within your AWS Organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetDefaultView](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_GetDefaultView.html)  **
  - **Description:** Grants permission to retrieve the Amazon resource name (ARN) of the view that is the default for the AWS Region in which you call this operation
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetIndex](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_GetIndex.html)  **
  - **Description:** Grants permission to retrieve information about the index in the AWS Region in which you call this operation
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetManagedView](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_GetManagedView.html)  **
  - **Description:** Grants permission to get managed view
  - **Resource types (\*required):** [managed-view\*](#list_resource-explorer-2-resource-managed-view)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetResourceExplorerSetup](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_GetResourceExplorerSetup.html)  **
  - **Description:** Grants permission to get resource explorer setup
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetServiceIndex](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_GetServiceIndex.html)  **
  - **Description:** Grants permission to get service index
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetServiceView](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_GetServiceView.html)  **
  - **Description:** Grants permission to get service view
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetView](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_GetView.html)  **
  - **Description:** Grants permission to retrieve information about the specified view
  - **Resource types (\*required):** [view\*](#list_resource-explorer-2-resource-view)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resource-explorer-2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListIndexes](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_ListIndexes.html)  **
  - **Description:** Grants permission to list the indexes in all AWS Regions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListIndexesForMembers](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_ListIndexesForMembers.html)  **
  - **Description:** Grants permission to list the organization member account's indexes in all AWS Regions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListManagedViews](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_ListManagedViews.html)  **
  - **Description:** Grants permission to list managed views
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListServiceIndexes](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_ListServiceIndexes.html)  **
  - **Description:** Grants permission to list service indexes in all AWS Regions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListServiceViews](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_ListServiceViews.html)  **
  - **Description:** Grants permission to list service views in all AWS Regions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListStreamingAccessForServices](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_ListStreamingAccessForServices.html)  **
  - **Description:** Grants permission to list streaming access for services
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSupportedResourceTypes](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_ListSupportedResourceTypes.html)  **
  - **Description:** Grants permission to retrieve a list of all resource types currently supported by Resource Explorer
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list the tags that are attached to the specified resource
  - **Resource types (\*required):** [index](#list_resource-explorer-2-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resource-explorer-2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [view](#list_resource-explorer-2-resource-view) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resource-explorer-2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListViews](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_ListViews.html)  **
  - **Description:** Grants permission to list the Amazon resource names (ARNs) of all of the views available in the AWS Region in which you call this operation
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [Search](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_Search.html)  **
  - **Description:** Grants permission to search for resources and display details about all resources that match the specified criteria
  - **Resource types (\*required):** [view\*](#list_resource-explorer-2-resource-view)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resource-explorer-2-aws_ResourceTag___TagKey_)<br />[resource-explorer-2:Operation](#list_resource-explorer-2-resource-explorer-2_Operation)
  - **Access level:** Read

- **   [TagResource](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_TagResource.html)  **
  - **Description:** Grants permission to add one or more tag key and value pairs to the specified resource
  - **Resource types (\*required):** [index](#list_resource-explorer-2-resource-index) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_resource-explorer-2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_resource-explorer-2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_resource-explorer-2-aws_TagKeys)
  - **Resource types (\*required):** [view](#list_resource-explorer-2-resource-view) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_resource-explorer-2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_resource-explorer-2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_resource-explorer-2-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove one or more tag key and value pairs from the specified resource
  - **Resource types (\*required):** [index](#list_resource-explorer-2-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resource-explorer-2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_resource-explorer-2-aws_TagKeys)
  - **Resource types (\*required):** [view](#list_resource-explorer-2-resource-view) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resource-explorer-2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_resource-explorer-2-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateIndexType](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_UpdateIndexType.html)  **
  - **Description:** Grants permission to change the type of the index from LOCAL to AGGREGATOR or back 
  - **Resource types (\*required):** [index\*](#list_resource-explorer-2-resource-index)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resource-explorer-2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateView](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_UpdateView.html)  **
  - **Description:** Grants permission to modify some of the details of a view
  - **Resource types (\*required):** [view\*](#list_resource-explorer-2-resource-view)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resource-explorer-2-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for AWS Resource Explorer
<a name="list_resource-explorer-2-permission-only-actions"></a>

The following actions are defined by AWS Resource Explorer but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [CreateManagedView](https://docs.aws.amazon.com/resource-explorer/latest/userguide/API_ManagedView.html)  **
  - **Description:** Grants permission to create managed view
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateStreamingAccessForService](API_CreateStreamingAccessForService.html)  **
  - **Description:** Grants permission to create resource explorer streaming access
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteResourcePolicy](https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-views-share.html)  **
  - **Description:** Grants permission to delete the specified view's resource policy
  - **Resource types (\*required):** [view\*](#list_resource-explorer-2-resource-view)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resource-explorer-2-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   DeleteStreamingAccessForService  **
  - **Description:** Grants permission to delete resource explorer streaming access
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [GetResourcePolicy](https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-views-share.html)  **
  - **Description:** Grants permission to retrieve information about the specified view's resource policy
  - **Resource types (\*required):** [view\*](#list_resource-explorer-2-resource-view)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resource-explorer-2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PutResourcePolicy](https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-views-share.html)  **
  - **Description:** Grants permission to update the specified view's resource policy
  - **Resource types (\*required):** [view\*](#list_resource-explorer-2-resource-view)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resource-explorer-2-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write



## Resource types defined by AWS Resource Explorer
<a name="list_resource-explorer-2-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [index](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_Index.html)  | arn:${Partition}:resource-explorer-2:${Region}:${Account}:index/${IndexUuid} | [aws:ResourceTag/${TagKey}](#list_resource-explorer-2-aws_ResourceTag___TagKey_) | 
|  [managed-view](https://docs.aws.amazon.com/resource-explorer/latest/userguide/API_ManagedView.html)  | arn:${Partition}:resource-explorer-2:${Region}:${Account}:managed-view/${ManagedViewName}/${ManagedViewUuid} |   | 
|  [view](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_View.html)  | arn:${Partition}:resource-explorer-2:${Region}:${Account}:view/${ViewName}/${ViewUuid} | [aws:ResourceTag/${TagKey}](#list_resource-explorer-2-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Resource Explorer
<a name="list_resource-explorer-2-policy-keys"></a>

AWS Resource Explorer defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tag keys that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tag keyss attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 
|   [resource-explorer-2:Operation](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsresourceexplorer.html)  | Filters access by the actual operation that is being invoked, available values: Search, ListResources | String | 