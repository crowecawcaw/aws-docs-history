

# Actions, resources, and condition keys for Amazon Lookout for Vision
<a name="list_lookoutvision"></a>

Amazon Lookout for Vision (service prefix: `lookoutvision`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/lookout-for-vision/latest/developer-guide/what-is.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/lookout-for-vision/latest/APIReference/API_Operations.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/lookout-for-vision/latest/developer-guide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/lookoutvision/lookoutvision.json) for this service.

**Topics**
+ [Actions defined by Amazon Lookout for Vision](#list_lookoutvision-actions-as-permissions)
+ [Permission-only actions for Amazon Lookout for Vision](#list_lookoutvision-permission-only-actions)
+ [Resource types defined by Amazon Lookout for Vision](#list_lookoutvision-resources-for-iam-policies)
+ [Condition keys for Amazon Lookout for Vision](#list_lookoutvision-policy-keys)

## Actions defined by Amazon Lookout for Vision
<a name="list_lookoutvision-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateDataset](https://docs.aws.amazon.com/lookout-for-vision/latest/APIReference/API_CreateDataset.html)  **
  - **Description:** Grants permission to create a dataset manifest
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateModel](https://docs.aws.amazon.com/lookout-for-vision/latest/APIReference/API_CreateModel.html)  **
  - **Description:** Grants permission to create a new anomaly detection model
  - **Resource types (\*required):** [model\*](#list_lookoutvision-resource-model)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_lookoutvision-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_lookoutvision-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lookoutvision-aws_TagKeys)
  - **Access level:** Write

- **   [CreateProject](https://docs.aws.amazon.com/lookout-for-vision/latest/APIReference/API_CreateProject.html)  **
  - **Description:** Grants permission to create a new project
  - **Resource types (\*required):** [project\*](#list_lookoutvision-resource-project)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteDataset](https://docs.aws.amazon.com/lookout-for-vision/latest/APIReference/API_DeleteDataset.html)  **
  - **Description:** Grants permission to delete a dataset
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteModel](https://docs.aws.amazon.com/lookout-for-vision/latest/APIReference/API_DeleteModel.html)  **
  - **Description:** Grants permission to delete a model and all associated assets
  - **Resource types (\*required):** [model\*](#list_lookoutvision-resource-model)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutvision-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteProject](https://docs.aws.amazon.com/lookout-for-vision/latest/APIReference/API_DeleteProject.html)  **
  - **Description:** Grants permission to permanently remove a project
  - **Resource types (\*required):** [project\*](#list_lookoutvision-resource-project)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DescribeDataset](https://docs.aws.amazon.com/lookout-for-vision/latest/APIReference/API_DescribeDataset.html)  **
  - **Description:** Grants permission to show detailed information about dataset manifest
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeModel](https://docs.aws.amazon.com/lookout-for-vision/latest/APIReference/API_DescribeModel.html)  **
  - **Description:** Grants permission to show detailed information about a model
  - **Resource types (\*required):** [model\*](#list_lookoutvision-resource-model)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutvision-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeModelPackagingJob](https://docs.aws.amazon.com/lookout-for-vision/latest/APIReference/API_DescribeModelPackagingJob.html)  **
  - **Description:** Grants permission to show detailed information about a model packaging job
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeProject](https://docs.aws.amazon.com/lookout-for-vision/latest/APIReference/API_DescribeProject.html)  **
  - **Description:** Grants permission to show detailed information about a project
  - **Resource types (\*required):** [project\*](#list_lookoutvision-resource-project)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DetectAnomalies](https://docs.aws.amazon.com/lookout-for-vision/latest/APIReference/API_DetectAnomalies.html)  **
  - **Description:** Grants permission to invoke detection of anomalies
  - **Resource types (\*required):** [model\*](#list_lookoutvision-resource-model)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutvision-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ListDatasetEntries](https://docs.aws.amazon.com/lookout-for-vision/latest/APIReference/API_ListDatasetEntries.html)  **
  - **Description:** Grants permission to list the contents of dataset manifest
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListModelPackagingJobs](https://docs.aws.amazon.com/lookout-for-vision/latest/APIReference/API_ListModelPackagingJobs.html)  **
  - **Description:** Grants permission to list all model packaging jobs associated with a project
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListModels](https://docs.aws.amazon.com/lookout-for-vision/latest/APIReference/API_ListModels.html)  **
  - **Description:** Grants permission to list all models associated with a project
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListProjects](https://docs.aws.amazon.com/lookout-for-vision/latest/APIReference/API_ListProjects.html)  **
  - **Description:** Grants permission to list all projects
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/lookout-for-vision/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a resource
  - **Resource types (\*required):** [model](#list_lookoutvision-resource-model)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutvision-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [StartModel](https://docs.aws.amazon.com/lookout-for-vision/latest/APIReference/API_StartModel.html)  **
  - **Description:** Grants permission to start anomaly detection model
  - **Resource types (\*required):** [model\*](#list_lookoutvision-resource-model)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutvision-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartModelPackagingJob](https://docs.aws.amazon.com/lookout-for-vision/latest/APIReference/API_StartModelPackagingJob.html)  **
  - **Description:** Grants permission to start a model packaging job
  - **Resource types (\*required):** [model\*](#list_lookoutvision-resource-model)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutvision-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopModel](https://docs.aws.amazon.com/lookout-for-vision/latest/APIReference/API_StopModel.html)  **
  - **Description:** Grants permission to stop anomaly detection model
  - **Resource types (\*required):** [model\*](#list_lookoutvision-resource-model)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutvision-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/lookout-for-vision/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag a resource with given key value pairs
  - **Resource types (\*required):** [model](#list_lookoutvision-resource-model)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_lookoutvision-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_lookoutvision-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lookoutvision-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/lookout-for-vision/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove the tag with the given key from a resource
  - **Resource types (\*required):** [model](#list_lookoutvision-resource-model)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutvision-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lookoutvision-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateDatasetEntries](https://docs.aws.amazon.com/lookout-for-vision/latest/APIReference/API_UpdateDatasetEntries.html)  **
  - **Description:** Grants permission to update a training or test dataset manifest
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write



## Permission-only actions for Amazon Lookout for Vision
<a name="list_lookoutvision-permission-only-actions"></a>

The following actions are defined by Amazon Lookout for Vision but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [DescribeTrialDetection](https://docs.aws.amazon.com/lookout-for-vision/latest/developer-guide/trial-detection.html)  | Grants permission to provides state information about a running anomaly detection job |  |   | Read | 
|   [ListTrialDetections](https://docs.aws.amazon.com/lookout-for-vision/latest/developer-guide/trial-detection.html)  | Grants permission to list all anomaly detection jobs |  |   | List | 
|   [StartTrialDetection](https://docs.aws.amazon.com/lookout-for-vision/latest/developer-guide/trial-detection.html)  | Grants permission to start bulk detection of anomalies for a set of images stored in an S3 bucket |  |   | Write | 

## Resource types defined by Amazon Lookout for Vision
<a name="list_lookoutvision-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [model](https://docs.aws.amazon.com/lookout-for-vision/latest/developer-guide/model-create-project.html)  | arn:${Partition}:lookoutvision:${Region}:${Account}:model/${ProjectName}/${ModelVersion} | [aws:ResourceTag/${TagKey}](#list_lookoutvision-aws_ResourceTag___TagKey_) | 
|  [project](https://docs.aws.amazon.com/lookout-for-vision/latest/developer-guide/model-create-project.html)  | arn:${Partition}:lookoutvision:${Region}:${Account}:project/${ProjectName} |   | 

## Condition keys for Amazon Lookout for Vision
<a name="list_lookoutvision-policy-keys"></a>

Amazon Lookout for Vision defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 