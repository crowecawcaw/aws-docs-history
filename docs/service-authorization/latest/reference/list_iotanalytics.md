

# Actions, resources, and condition keys for AWS IoT Analytics
<a name="list_iotanalytics"></a>

AWS IoT Analytics (service prefix: `iotanalytics`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/iotanalytics/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/iotanalytics/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/iotanalytics/latest/userguide/getting-started.html#aws-iot-analytics-step-create-role) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/iotanalytics/iotanalytics.json) for this service.

**Topics**
+ [Actions defined by AWS IoT Analytics](#list_iotanalytics-actions-as-permissions)
+ [Resource types defined by AWS IoT Analytics](#list_iotanalytics-resources-for-iam-policies)
+ [Condition keys for AWS IoT Analytics](#list_iotanalytics-policy-keys)

## Actions defined by AWS IoT Analytics
<a name="list_iotanalytics-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [BatchPutMessage](https://docs.aws.amazon.com/iotanalytics/latest/APIReference/API_BatchPutMessage.html)  **
  - **Description:** Puts a batch of messages into the specified channel
  - **Resource types (\*required):** [channel\*](#list_iotanalytics-resource-channel)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotanalytics-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iotanalytics-aws_TagKeys)<br />[iotanalytics:ResourceTag/${TagKey}](#list_iotanalytics-iotanalytics_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CancelPipelineReprocessing](https://docs.aws.amazon.com/iotanalytics/latest/APIReference/API_CancelPipelineReprocessing.html)  **
  - **Description:** Cancels reprocessing for the specified pipeline
  - **Resource types (\*required):** [pipeline\*](#list_iotanalytics-resource-pipeline)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotanalytics-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iotanalytics-aws_TagKeys)<br />[iotanalytics:ResourceTag/${TagKey}](#list_iotanalytics-iotanalytics_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateChannel](https://docs.aws.amazon.com/iotanalytics/latest/APIReference/API_CreateChannel.html)  **
  - **Description:** Creates a channel
  - **Resource types (\*required):** [channel\*](#list_iotanalytics-resource-channel)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotanalytics-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iotanalytics-aws_TagKeys)<br />[iotanalytics:ResourceTag/${TagKey}](#list_iotanalytics-iotanalytics_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateDataset](https://docs.aws.amazon.com/iotanalytics/latest/APIReference/API_CreateDataset.html)  **
  - **Description:** Creates a dataset
  - **Resource types (\*required):** [dataset\*](#list_iotanalytics-resource-dataset)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotanalytics-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iotanalytics-aws_TagKeys)<br />[iotanalytics:ResourceTag/${TagKey}](#list_iotanalytics-iotanalytics_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateDatasetContent](https://docs.aws.amazon.com/iotanalytics/latest/APIReference/API_CreateDatasetContent.html)  **
  - **Description:** Generates content from the specified dataset (by executing the dataset actions)
  - **Resource types (\*required):** [dataset\*](#list_iotanalytics-resource-dataset)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotanalytics-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iotanalytics-aws_TagKeys)<br />[iotanalytics:ResourceTag/${TagKey}](#list_iotanalytics-iotanalytics_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateDatastore](https://docs.aws.amazon.com/iotanalytics/latest/APIReference/API_CreateDatastore.html)  **
  - **Description:** Creates a datastore
  - **Resource types (\*required):** [datastore\*](#list_iotanalytics-resource-datastore)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotanalytics-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iotanalytics-aws_TagKeys)<br />[iotanalytics:ResourceTag/${TagKey}](#list_iotanalytics-iotanalytics_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreatePipeline](https://docs.aws.amazon.com/iotanalytics/latest/APIReference/API_CreatePipeline.html)  **
  - **Description:** Creates a pipeline
  - **Resource types (\*required):** [pipeline\*](#list_iotanalytics-resource-pipeline)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotanalytics-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iotanalytics-aws_TagKeys)<br />[iotanalytics:ResourceTag/${TagKey}](#list_iotanalytics-iotanalytics_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteChannel](https://docs.aws.amazon.com/iotanalytics/latest/APIReference/API_DeleteChannel.html)  **
  - **Description:** Deletes the specified channel
  - **Resource types (\*required):** [channel\*](#list_iotanalytics-resource-channel)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotanalytics-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iotanalytics-aws_TagKeys)<br />[iotanalytics:ResourceTag/${TagKey}](#list_iotanalytics-iotanalytics_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDataset](https://docs.aws.amazon.com/iotanalytics/latest/APIReference/API_DeleteDataset.html)  **
  - **Description:** Deletes the specified dataset
  - **Resource types (\*required):** [dataset\*](#list_iotanalytics-resource-dataset)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotanalytics-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iotanalytics-aws_TagKeys)<br />[iotanalytics:ResourceTag/${TagKey}](#list_iotanalytics-iotanalytics_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDatasetContent](https://docs.aws.amazon.com/iotanalytics/latest/APIReference/API_DeleteDatasetContent.html)  **
  - **Description:** Deletes the content of the specified dataset
  - **Resource types (\*required):** [dataset\*](#list_iotanalytics-resource-dataset)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotanalytics-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iotanalytics-aws_TagKeys)<br />[iotanalytics:ResourceTag/${TagKey}](#list_iotanalytics-iotanalytics_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDatastore](https://docs.aws.amazon.com/iotanalytics/latest/APIReference/API_DeleteDatastore.html)  **
  - **Description:** Deletes the specified datastore
  - **Resource types (\*required):** [datastore\*](#list_iotanalytics-resource-datastore)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotanalytics-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iotanalytics-aws_TagKeys)<br />[iotanalytics:ResourceTag/${TagKey}](#list_iotanalytics-iotanalytics_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePipeline](https://docs.aws.amazon.com/iotanalytics/latest/APIReference/API_DeletePipeline.html)  **
  - **Description:** Deletes the specified pipeline
  - **Resource types (\*required):** [pipeline\*](#list_iotanalytics-resource-pipeline)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotanalytics-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iotanalytics-aws_TagKeys)<br />[iotanalytics:ResourceTag/${TagKey}](#list_iotanalytics-iotanalytics_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeChannel](https://docs.aws.amazon.com/iotanalytics/latest/APIReference/API_DescribeChannel.html)  **
  - **Description:** Describes the specified channel
  - **Resource types (\*required):** [channel\*](#list_iotanalytics-resource-channel)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotanalytics-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iotanalytics-aws_TagKeys)<br />[iotanalytics:ResourceTag/${TagKey}](#list_iotanalytics-iotanalytics_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeDataset](https://docs.aws.amazon.com/iotanalytics/latest/APIReference/API_DescribeDataset.html)  **
  - **Description:** Describes the specified dataset
  - **Resource types (\*required):** [dataset\*](#list_iotanalytics-resource-dataset)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotanalytics-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iotanalytics-aws_TagKeys)<br />[iotanalytics:ResourceTag/${TagKey}](#list_iotanalytics-iotanalytics_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeDatastore](https://docs.aws.amazon.com/iotanalytics/latest/APIReference/API_DescribeDatastore.html)  **
  - **Description:** Describes the specified datastore
  - **Resource types (\*required):** [datastore\*](#list_iotanalytics-resource-datastore)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotanalytics-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iotanalytics-aws_TagKeys)<br />[iotanalytics:ResourceTag/${TagKey}](#list_iotanalytics-iotanalytics_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeLoggingOptions](https://docs.aws.amazon.com/iotanalytics/latest/APIReference/API_DescribeLoggingOptions.html)  **
  - **Description:** Describes logging options for the the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribePipeline](https://docs.aws.amazon.com/iotanalytics/latest/APIReference/API_DescribePipeline.html)  **
  - **Description:** Describes the specified pipeline
  - **Resource types (\*required):** [pipeline\*](#list_iotanalytics-resource-pipeline)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotanalytics-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iotanalytics-aws_TagKeys)<br />[iotanalytics:ResourceTag/${TagKey}](#list_iotanalytics-iotanalytics_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDatasetContent](https://docs.aws.amazon.com/iotanalytics/latest/APIReference/API_GetDatasetContent.html)  **
  - **Description:** Gets the content of the specified dataset
  - **Resource types (\*required):** [dataset\*](#list_iotanalytics-resource-dataset)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotanalytics-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iotanalytics-aws_TagKeys)<br />[iotanalytics:ResourceTag/${TagKey}](#list_iotanalytics-iotanalytics_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListChannels](https://docs.aws.amazon.com/iotanalytics/latest/APIReference/API_ListChannels.html)  **
  - **Description:** Lists the channels for the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDatasetContents](https://docs.aws.amazon.com/iotanalytics/latest/APIReference/API_ListDatasetContents.html)  **
  - **Description:** Lists information about dataset contents that have been created
  - **Resource types (\*required):** [dataset\*](#list_iotanalytics-resource-dataset)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotanalytics-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iotanalytics-aws_TagKeys)<br />[iotanalytics:ResourceTag/${TagKey}](#list_iotanalytics-iotanalytics_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDatasets](https://docs.aws.amazon.com/iotanalytics/latest/APIReference/API_ListDatasets.html)  **
  - **Description:** Lists the datasets for the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDatastores](https://docs.aws.amazon.com/iotanalytics/latest/APIReference/API_ListDatastores.html)  **
  - **Description:** Lists the datastores for the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPipelines](https://docs.aws.amazon.com/iotanalytics/latest/APIReference/API_ListPipelines.html)  **
  - **Description:** Lists the pipelines for the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/iotanalytics/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Lists the tags (metadata) which you have assigned to the resource
  - **Resource types (\*required):** [channel](#list_iotanalytics-resource-channel) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotanalytics-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iotanalytics-aws_TagKeys)<br />[iotanalytics:ResourceTag/${TagKey}](#list_iotanalytics-iotanalytics_ResourceTag___TagKey_)
  - **Resource types (\*required):** [dataset](#list_iotanalytics-resource-dataset) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotanalytics-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iotanalytics-aws_TagKeys)<br />[iotanalytics:ResourceTag/${TagKey}](#list_iotanalytics-iotanalytics_ResourceTag___TagKey_)
  - **Resource types (\*required):** [datastore](#list_iotanalytics-resource-datastore) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotanalytics-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iotanalytics-aws_TagKeys)<br />[iotanalytics:ResourceTag/${TagKey}](#list_iotanalytics-iotanalytics_ResourceTag___TagKey_)
  - **Resource types (\*required):** [pipeline](#list_iotanalytics-resource-pipeline) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotanalytics-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iotanalytics-aws_TagKeys)<br />[iotanalytics:ResourceTag/${TagKey}](#list_iotanalytics-iotanalytics_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PutLoggingOptions](https://docs.aws.amazon.com/iotanalytics/latest/APIReference/API_PutLoggingOptions.html)  **
  - **Description:** Puts logging options for the the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [RunPipelineActivity](https://docs.aws.amazon.com/iotanalytics/latest/APIReference/API_RunPipelineActivity.html)  **
  - **Description:** Runs the specified pipeline activity
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [SampleChannelData](https://docs.aws.amazon.com/iotanalytics/latest/APIReference/API_SampleChannelData.html)  **
  - **Description:** Samples the specified channel's data
  - **Resource types (\*required):** [channel\*](#list_iotanalytics-resource-channel)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotanalytics-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iotanalytics-aws_TagKeys)<br />[iotanalytics:ResourceTag/${TagKey}](#list_iotanalytics-iotanalytics_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [StartPipelineReprocessing](https://docs.aws.amazon.com/iotanalytics/latest/APIReference/API_StartPipelineReprocessing.html)  **
  - **Description:** Starts reprocessing for the specified pipeline
  - **Resource types (\*required):** [pipeline\*](#list_iotanalytics-resource-pipeline)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotanalytics-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iotanalytics-aws_TagKeys)<br />[iotanalytics:ResourceTag/${TagKey}](#list_iotanalytics-iotanalytics_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/iotanalytics/latest/APIReference/API_TagResource.html)  **
  - **Description:** Adds to or modifies the tags of the given resource. Tags are metadata which can be used to manage a resource
  - **Resource types (\*required):** [channel](#list_iotanalytics-resource-channel) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotanalytics-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iotanalytics-aws_TagKeys)<br />[iotanalytics:ResourceTag/${TagKey}](#list_iotanalytics-iotanalytics_ResourceTag___TagKey_)
  - **Resource types (\*required):** [dataset](#list_iotanalytics-resource-dataset) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotanalytics-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iotanalytics-aws_TagKeys)<br />[iotanalytics:ResourceTag/${TagKey}](#list_iotanalytics-iotanalytics_ResourceTag___TagKey_)
  - **Resource types (\*required):** [datastore](#list_iotanalytics-resource-datastore) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotanalytics-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iotanalytics-aws_TagKeys)<br />[iotanalytics:ResourceTag/${TagKey}](#list_iotanalytics-iotanalytics_ResourceTag___TagKey_)
  - **Resource types (\*required):** [pipeline](#list_iotanalytics-resource-pipeline) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotanalytics-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iotanalytics-aws_TagKeys)<br />[iotanalytics:ResourceTag/${TagKey}](#list_iotanalytics-iotanalytics_ResourceTag___TagKey_)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/iotanalytics/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Removes the given tags (metadata) from the resource
  - **Resource types (\*required):** [channel](#list_iotanalytics-resource-channel) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotanalytics-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iotanalytics-aws_TagKeys)<br />[iotanalytics:ResourceTag/${TagKey}](#list_iotanalytics-iotanalytics_ResourceTag___TagKey_)
  - **Resource types (\*required):** [dataset](#list_iotanalytics-resource-dataset) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotanalytics-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iotanalytics-aws_TagKeys)<br />[iotanalytics:ResourceTag/${TagKey}](#list_iotanalytics-iotanalytics_ResourceTag___TagKey_)
  - **Resource types (\*required):** [datastore](#list_iotanalytics-resource-datastore) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotanalytics-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iotanalytics-aws_TagKeys)<br />[iotanalytics:ResourceTag/${TagKey}](#list_iotanalytics-iotanalytics_ResourceTag___TagKey_)
  - **Resource types (\*required):** [pipeline](#list_iotanalytics-resource-pipeline) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotanalytics-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iotanalytics-aws_TagKeys)<br />[iotanalytics:ResourceTag/${TagKey}](#list_iotanalytics-iotanalytics_ResourceTag___TagKey_)
  - **Access level:** Tagging, Write

- **   [UpdateChannel](https://docs.aws.amazon.com/iotanalytics/latest/APIReference/API_UpdateChannel.html)  **
  - **Description:** Updates the specified channel
  - **Resource types (\*required):** [channel\*](#list_iotanalytics-resource-channel)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotanalytics-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iotanalytics-aws_TagKeys)<br />[iotanalytics:ResourceTag/${TagKey}](#list_iotanalytics-iotanalytics_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDataset](https://docs.aws.amazon.com/iotanalytics/latest/APIReference/API_UpdateDataset.html)  **
  - **Description:** Updates the specified dataset
  - **Resource types (\*required):** [dataset\*](#list_iotanalytics-resource-dataset)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotanalytics-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iotanalytics-aws_TagKeys)<br />[iotanalytics:ResourceTag/${TagKey}](#list_iotanalytics-iotanalytics_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDatastore](https://docs.aws.amazon.com/iotanalytics/latest/APIReference/API_UpdateDatastore.html)  **
  - **Description:** Updates the specified datastore
  - **Resource types (\*required):** [datastore\*](#list_iotanalytics-resource-datastore)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotanalytics-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iotanalytics-aws_TagKeys)<br />[iotanalytics:ResourceTag/${TagKey}](#list_iotanalytics-iotanalytics_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdatePipeline](https://docs.aws.amazon.com/iotanalytics/latest/APIReference/API_UpdatePipeline.html)  **
  - **Description:** Updates the specified pipeline
  - **Resource types (\*required):** [pipeline\*](#list_iotanalytics-resource-pipeline)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotanalytics-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iotanalytics-aws_TagKeys)<br />[iotanalytics:ResourceTag/${TagKey}](#list_iotanalytics-iotanalytics_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS IoT Analytics
<a name="list_iotanalytics-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [channel](https://docs.aws.amazon.com/iotanalytics/latest/userguide/welcome.html#aws-iot-analytics-how)  | arn:${Partition}:iotanalytics:${Region}:${Account}:channel/${ChannelName} | [aws:RequestTag/${TagKey}](#list_iotanalytics-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iotanalytics-aws_TagKeys)<br />[iotanalytics:ResourceTag/${TagKey}](#list_iotanalytics-iotanalytics_ResourceTag___TagKey_) | 
|  [dataset](https://docs.aws.amazon.com/iotanalytics/latest/userguide/welcome.html#aws-iot-analytics-how)  | arn:${Partition}:iotanalytics:${Region}:${Account}:dataset/${DatasetName} | [aws:RequestTag/${TagKey}](#list_iotanalytics-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iotanalytics-aws_TagKeys)<br />[iotanalytics:ResourceTag/${TagKey}](#list_iotanalytics-iotanalytics_ResourceTag___TagKey_) | 
|  [datastore](https://docs.aws.amazon.com/iotanalytics/latest/userguide/welcome.html#aws-iot-analytics-how)  | arn:${Partition}:iotanalytics:${Region}:${Account}:datastore/${DatastoreName} | [aws:RequestTag/${TagKey}](#list_iotanalytics-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iotanalytics-aws_TagKeys)<br />[iotanalytics:ResourceTag/${TagKey}](#list_iotanalytics-iotanalytics_ResourceTag___TagKey_) | 
|  [pipeline](https://docs.aws.amazon.com/iotanalytics/latest/userguide/welcome.html#aws-iot-analytics-how)  | arn:${Partition}:iotanalytics:${Region}:${Account}:pipeline/${PipelineName} | [aws:RequestTag/${TagKey}](#list_iotanalytics-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iotanalytics-aws_TagKeys)<br />[iotanalytics:ResourceTag/${TagKey}](#list_iotanalytics-iotanalytics_ResourceTag___TagKey_) | 

## Condition keys for AWS IoT Analytics
<a name="list_iotanalytics-policy-keys"></a>

AWS IoT Analytics defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access based on the tags that are passed in the request | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access based on the presence of tag keys in the request | ArrayOfString | 
|   [iotanalytics:ResourceTag/${TagKey}](https://docs.aws.amazon.com/iotanalytics/latest/userguide/tagging.html#tagging-iam)  | Filters access by the tag key-value pairs attached to the resource | String | 