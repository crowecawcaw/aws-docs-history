

# Actions, resources, and condition keys for AWS Elemental MediaStore
<a name="list_mediastore"></a>

AWS Elemental MediaStore (service prefix: `mediastore`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/mediastore/latest/ug/what-is.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/mediastore/latest/apireference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/mediastore/latest/ug/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/mediastore/mediastore.json) for this service.

**Topics**
+ [API operations defined by AWS Elemental MediaStore](#list_mediastore-operations)
+ [Actions defined by AWS Elemental MediaStore](#list_mediastore-actions-as-permissions)
+ [Resource types defined by AWS Elemental MediaStore](#list_mediastore-resources-for-iam-policies)
+ [Condition keys for AWS Elemental MediaStore](#list_mediastore-policy-keys)

## API operations defined by AWS Elemental MediaStore
<a name="list_mediastore-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_mediastore-actions-as-permissions).




- **   CreateContainer  **
  - **SDK client:** mediastore
  - **IAM action:**  [mediastore:CreateContainer](#list_mediastore-action-CreateContainer)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mediastore:TagResource](#list_mediastore-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteContainer  **
  - **SDK client:** mediastore
  - **IAM action:**  [mediastore:DeleteContainer](#list_mediastore-action-DeleteContainer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteContainerPolicy  **
  - **SDK client:** mediastore
  - **IAM action:**  [mediastore:DeleteContainerPolicy](#list_mediastore-action-DeleteContainerPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DeleteCorsPolicy  **
  - **SDK client:** mediastore
  - **IAM action:**  [mediastore:DeleteCorsPolicy](#list_mediastore-action-DeleteCorsPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteLifecyclePolicy  **
  - **SDK client:** mediastore
  - **IAM action:**  [mediastore:DeleteLifecyclePolicy](#list_mediastore-action-DeleteLifecyclePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteMetricPolicy  **
  - **SDK client:** mediastore
  - **IAM action:**  [mediastore:DeleteMetricPolicy](#list_mediastore-action-DeleteMetricPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeContainer  **
  - **SDK client:** mediastore
  - **IAM action:**  [mediastore:DescribeContainer](#list_mediastore-action-DescribeContainer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetContainerPolicy  **
  - **SDK client:** mediastore
  - **IAM action:**  [mediastore:GetContainerPolicy](#list_mediastore-action-GetContainerPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCorsPolicy  **
  - **SDK client:** mediastore
  - **IAM action:**  [mediastore:GetCorsPolicy](#list_mediastore-action-GetCorsPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetLifecyclePolicy  **
  - **SDK client:** mediastore
  - **IAM action:**  [mediastore:GetLifecyclePolicy](#list_mediastore-action-GetLifecyclePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMetricPolicy  **
  - **SDK client:** mediastore
  - **IAM action:**  [mediastore:GetMetricPolicy](#list_mediastore-action-GetMetricPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListContainers  **
  - **SDK client:** mediastore
  - **IAM action:**  [mediastore:ListContainers](#list_mediastore-action-ListContainers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **SDK client:** mediastore
  - **IAM action:**  [mediastore:ListTagsForResource](#list_mediastore-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PutContainerPolicy  **
  - **SDK client:** mediastore
  - **IAM action:**  [mediastore:PutContainerPolicy](#list_mediastore-action-PutContainerPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   PutCorsPolicy  **
  - **SDK client:** mediastore
  - **IAM action:**  [mediastore:PutCorsPolicy](#list_mediastore-action-PutCorsPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutLifecyclePolicy  **
  - **SDK client:** mediastore
  - **IAM action:**  [mediastore:PutLifecyclePolicy](#list_mediastore-action-PutLifecyclePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutMetricPolicy  **
  - **SDK client:** mediastore
  - **IAM action:**  [mediastore:PutMetricPolicy](#list_mediastore-action-PutMetricPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartAccessLogging  **
  - **SDK client:** mediastore
  - **IAM action:**  [mediastore:StartAccessLogging](#list_mediastore-action-StartAccessLogging)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** mediastore.amazonaws.com / **Access level:** Write

- **   StopAccessLogging  **
  - **SDK client:** mediastore
  - **IAM action:**  [mediastore:StopAccessLogging](#list_mediastore-action-StopAccessLogging) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **SDK client:** mediastore
  - **IAM action:**  [mediastore:TagResource](#list_mediastore-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **SDK client:** mediastore
  - **IAM action:**  [mediastore:UntagResource](#list_mediastore-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   DeleteObject  **
  - **SDK client:** mediastore-data
  - **IAM action:**  [mediastore:DeleteObject](#list_mediastore-action-DeleteObject) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeObject  **
  - **SDK client:** mediastore-data
  - **IAM action:**  [mediastore:DescribeObject](#list_mediastore-action-DescribeObject) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetObject  **
  - **SDK client:** mediastore-data
  - **IAM action:**  [mediastore:GetObject](#list_mediastore-action-GetObject) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListItems  **
  - **SDK client:** mediastore-data
  - **IAM action:**  [mediastore:ListItems](#list_mediastore-action-ListItems) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PutObject  **
  - **SDK client:** mediastore-data
  - **IAM action:**  [mediastore:PutObject](#list_mediastore-action-PutObject) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Elemental MediaStore
<a name="list_mediastore-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateContainer](https://docs.aws.amazon.com/mediastore/latest/apireference/API_CreateContainer.html)  **
  - **Description:** Grants permission to create a container
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediastore-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_mediastore-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteContainer](https://docs.aws.amazon.com/mediastore/latest/apireference/API_DeleteContainer.html)  **
  - **Description:** Grants permission to delete a container
  - **Resource types (\*required):** [container\*](#list_mediastore-resource-container)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediastore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteContainerPolicy](https://docs.aws.amazon.com/mediastore/latest/apireference/API_DeleteContainerPolicy.html)  **
  - **Description:** Grants permission to delete the access policy of a container
  - **Resource types (\*required):** [container\*](#list_mediastore-resource-container)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediastore-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [DeleteCorsPolicy](https://docs.aws.amazon.com/mediastore/latest/apireference/API_DeleteCorsPolicy.html)  **
  - **Description:** Grants permission to delete the CORS policy from a container
  - **Resource types (\*required):** [container\*](#list_mediastore-resource-container)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediastore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteLifecyclePolicy](https://docs.aws.amazon.com/mediastore/latest/apireference/API_DeleteLifecyclePolicy.html)  **
  - **Description:** Grants permission to delete the lifecycle policy from a container
  - **Resource types (\*required):** [container\*](#list_mediastore-resource-container)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediastore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteMetricPolicy](https://docs.aws.amazon.com/mediastore/latest/apireference/API_DeleteMetricPolicy.html)  **
  - **Description:** Grants permission to delete the metric policy from a container
  - **Resource types (\*required):** [container\*](#list_mediastore-resource-container)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediastore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteObject](https://docs.aws.amazon.com/mediastore/latest/apireference/API_objstore_DeleteObject.html)  **
  - **Description:** Grants permission to delete an object
  - **Resource types (\*required):** [object\*](#list_mediastore-resource-object)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DescribeContainer](https://docs.aws.amazon.com/mediastore/latest/apireference/API_DescribeContainer.html)  **
  - **Description:** Grants permission to retrieve details on a container
  - **Resource types (\*required):** [container\*](#list_mediastore-resource-container)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediastore-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [DescribeObject](https://docs.aws.amazon.com/mediastore/latest/apireference/API_objstore_DescribeObject.html)  **
  - **Description:** Grants permission to retrieve metadata for an object
  - **Resource types (\*required):** [object\*](#list_mediastore-resource-object)
  - **Condition keys:**  
  - **Access level:** List

- **   [GetContainerPolicy](https://docs.aws.amazon.com/mediastore/latest/apireference/API_GetContainerPolicy.html)  **
  - **Description:** Grants permission to retrieve the access policy of a container
  - **Resource types (\*required):** [container\*](#list_mediastore-resource-container)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediastore-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCorsPolicy](https://docs.aws.amazon.com/mediastore/latest/apireference/API_GetCorsPolicy.html)  **
  - **Description:** Grants permission to retrieve the CORS policy of a container
  - **Resource types (\*required):** [container\*](#list_mediastore-resource-container)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediastore-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetLifecyclePolicy](https://docs.aws.amazon.com/mediastore/latest/apireference/API_GetLifecyclePolicy.html)  **
  - **Description:** Grants permission to retrieve the lifecycle policy that is assigned to a container
  - **Resource types (\*required):** [container\*](#list_mediastore-resource-container)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediastore-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetMetricPolicy](https://docs.aws.amazon.com/mediastore/latest/apireference/API_GetMetricPolicy.html)  **
  - **Description:** Grants permission to retrieve the metric policy that is assigned to a container
  - **Resource types (\*required):** [container\*](#list_mediastore-resource-container)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediastore-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetObject](https://docs.aws.amazon.com/mediastore/latest/apireference/API_objstore_GetObject.html)  **
  - **Description:** Grants permission to retrieve an object
  - **Resource types (\*required):** [object\*](#list_mediastore-resource-object)
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListContainers](https://docs.aws.amazon.com/mediastore/latest/apireference/API_ListContainers.html)  **
  - **Description:** Grants permission to retrieve a list of containers in the current account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListItems](https://docs.aws.amazon.com/mediastore/latest/apireference/API_objstore_ListItems.html)  **
  - **Description:** Grants permission to retrieve a list of objects and subfolders that are stored in a folder
  - **Resource types (\*required):** [folder](#list_mediastore-resource-folder)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/mediastore/latest/apireference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags on a container
  - **Resource types (\*required):** [container](#list_mediastore-resource-container)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediastore-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PutContainerPolicy](https://docs.aws.amazon.com/mediastore/latest/apireference/API_PutContainerPolicy.html)  **
  - **Description:** Grants permission to create or replace the access policy of a container
  - **Resource types (\*required):** [container\*](#list_mediastore-resource-container)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediastore-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [PutCorsPolicy](https://docs.aws.amazon.com/mediastore/latest/apireference/API_PutCorsPolicy.html)  **
  - **Description:** Grants permission to add or modify the CORS policy of a container
  - **Resource types (\*required):** [container\*](#list_mediastore-resource-container)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediastore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutLifecyclePolicy](https://docs.aws.amazon.com/mediastore/latest/apireference/API_PutLifecyclePolicy.html)  **
  - **Description:** Grants permission to add or modify the lifecycle policy that is assigned to a container
  - **Resource types (\*required):** [container\*](#list_mediastore-resource-container)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediastore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutMetricPolicy](https://docs.aws.amazon.com/mediastore/latest/apireference/API_PutMetricPolicy.html)  **
  - **Description:** Grants permission to add or modify the metric policy that is assigned to a container
  - **Resource types (\*required):** [container\*](#list_mediastore-resource-container)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediastore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutObject](https://docs.aws.amazon.com/mediastore/latest/apireference/API_objstore_PutObject.html)  **
  - **Description:** Grants permission to upload an object
  - **Resource types (\*required):** [object\*](#list_mediastore-resource-object)
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartAccessLogging](https://docs.aws.amazon.com/mediastore/latest/apireference/API_StartAccessLogging.html)  **
  - **Description:** Grants permission to start access logging on a container
  - **Resource types (\*required):** [container\*](#list_mediastore-resource-container)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediastore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopAccessLogging](https://docs.aws.amazon.com/mediastore/latest/apireference/API_StopAccessLogging.html)  **
  - **Description:** Grants permission to stop access logging on a container
  - **Resource types (\*required):** [container\*](#list_mediastore-resource-container)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediastore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/mediastore/latest/apireference/API_TagResource.html)  **
  - **Description:** Grants permission to add tags to a container
  - **Resource types (\*required):** [container](#list_mediastore-resource-container)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediastore-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mediastore-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediastore-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/mediastore/latest/apireference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from a container
  - **Resource types (\*required):** [container](#list_mediastore-resource-container)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediastore-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediastore-aws_TagKeys)
  - **Access level:** Tagging, Write



## Resource types defined by AWS Elemental MediaStore
<a name="list_mediastore-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [container](https://docs.aws.amazon.com/mediastore/latest/ug/containers.html)  | arn:${Partition}:mediastore:${Region}:${Account}:container/${ContainerName} | [aws:ResourceTag/${TagKey}](#list_mediastore-aws_ResourceTag___TagKey_) | 
|  [folder](https://docs.aws.amazon.com/mediastore/latest/ug/folders.html)  | arn:${Partition}:mediastore:${Region}:${Account}:container/${ContainerName}/${FolderPath} |   | 
|  [object](https://docs.aws.amazon.com/mediastore/latest/ug/objects.html)  | arn:${Partition}:mediastore:${Region}:${Account}:container/${ContainerName}/${ObjectPath} |   | 

## Condition keys for AWS Elemental MediaStore
<a name="list_mediastore-policy-keys"></a>

AWS Elemental MediaStore defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 