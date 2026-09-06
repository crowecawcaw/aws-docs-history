

# Actions, resources, and condition keys for Amazon Elastic Transcoder
<a name="list_elastictranscoder"></a>

Amazon Elastic Transcoder (service prefix: `elastictranscoder`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/elastictranscoder/latest/developerguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/elastictranscoder/latest/developerguide/api-reference.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/elastictranscoder/latest/developerguide/access-control.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/elastictranscoder/elastictranscoder.json) for this service.

**Topics**
+ [Actions defined by Amazon Elastic Transcoder](#list_elastictranscoder-actions-as-permissions)
+ [Resource types defined by Amazon Elastic Transcoder](#list_elastictranscoder-resources-for-iam-policies)
+ [Condition keys for Amazon Elastic Transcoder](#list_elastictranscoder-policy-keys)

## Actions defined by Amazon Elastic Transcoder
<a name="list_elastictranscoder-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CancelJob](https://docs.aws.amazon.com/elastictranscoder/latest/developerguide/cancel-job.html)  **
  - **Description:** Cancel a job that Elastic Transcoder has not begun to process
  - **Resource types (\*required):** [job\*](#list_elastictranscoder-resource-job)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateJob](https://docs.aws.amazon.com/elastictranscoder/latest/developerguide/create-job.html)  **
  - **Description:** Create a job
  - **Resource types (\*required):** [pipeline\*](#list_elastictranscoder-resource-pipeline) / **Condition keys:**  
  - **Resource types (\*required):** [preset\*](#list_elastictranscoder-resource-preset) / **Condition keys:**  
  - **Access level:** Write

- **   [CreatePipeline](https://docs.aws.amazon.com/elastictranscoder/latest/developerguide/create-pipeline.html)  **
  - **Description:** Create a pipeline
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreatePreset](https://docs.aws.amazon.com/elastictranscoder/latest/developerguide/create-preset.html)  **
  - **Description:** Create a preset
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeletePipeline](https://docs.aws.amazon.com/elastictranscoder/latest/developerguide/delete-pipeline.html)  **
  - **Description:** Delete a pipeline
  - **Resource types (\*required):** [pipeline\*](#list_elastictranscoder-resource-pipeline)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeletePreset](https://docs.aws.amazon.com/elastictranscoder/latest/developerguide/delete-preset.html)  **
  - **Description:** Delete a preset
  - **Resource types (\*required):** [preset\*](#list_elastictranscoder-resource-preset)
  - **Condition keys:**  
  - **Access level:** Write

- **   [ListJobsByPipeline](https://docs.aws.amazon.com/elastictranscoder/latest/developerguide/list-jobs-by-pipeline.html)  **
  - **Description:** Get a list of the jobs that you assigned to a pipeline
  - **Resource types (\*required):** [pipeline\*](#list_elastictranscoder-resource-pipeline)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListJobsByStatus](https://docs.aws.amazon.com/elastictranscoder/latest/developerguide/list-jobs-by-status.html)  **
  - **Description:** Get information about all of the jobs associated with the current AWS account that have a specified status
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPipelines](https://docs.aws.amazon.com/elastictranscoder/latest/developerguide/list-pipelines.html)  **
  - **Description:** Get a list of the pipelines associated with the current AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPresets](https://docs.aws.amazon.com/elastictranscoder/latest/developerguide/list-presets.html)  **
  - **Description:** Get a list of all presets associated with the current AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ReadJob](https://docs.aws.amazon.com/elastictranscoder/latest/developerguide/get-job.html)  **
  - **Description:** Get detailed information about a job
  - **Resource types (\*required):** [job\*](#list_elastictranscoder-resource-job)
  - **Condition keys:**  
  - **Access level:** Read

- **   [ReadPipeline](https://docs.aws.amazon.com/elastictranscoder/latest/developerguide/get-pipeline.html)  **
  - **Description:** Get detailed information about a pipeline
  - **Resource types (\*required):** [pipeline\*](#list_elastictranscoder-resource-pipeline)
  - **Condition keys:**  
  - **Access level:** Read

- **   [ReadPreset](https://docs.aws.amazon.com/elastictranscoder/latest/developerguide/get-preset.html)  **
  - **Description:** Get detailed information about a preset
  - **Resource types (\*required):** [preset\*](#list_elastictranscoder-resource-preset)
  - **Condition keys:**  
  - **Access level:** Read

- **   [TestRole](https://docs.aws.amazon.com/elastictranscoder/latest/developerguide/test-pipeline-role.html)  **
  - **Description:** Test the settings for a pipeline to ensure that Elastic Transcoder can create and process jobs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdatePipeline](https://docs.aws.amazon.com/elastictranscoder/latest/developerguide/update-pipeline.html)  **
  - **Description:** Update settings for a pipeline
  - **Resource types (\*required):** [pipeline\*](#list_elastictranscoder-resource-pipeline)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdatePipelineNotifications](https://docs.aws.amazon.com/elastictranscoder/latest/developerguide/update-pipeline-notifications.html)  **
  - **Description:** Update only Amazon Simple Notification Service (Amazon SNS) notifications for a pipeline
  - **Resource types (\*required):** [pipeline\*](#list_elastictranscoder-resource-pipeline)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdatePipelineStatus](https://docs.aws.amazon.com/elastictranscoder/latest/developerguide/update-pipeline-status.html)  **
  - **Description:** Pause or reactivate a pipeline, so the pipeline stops or restarts processing jobs, update the status for the pipeline
  - **Resource types (\*required):** [pipeline\*](#list_elastictranscoder-resource-pipeline)
  - **Condition keys:**  
  - **Access level:** Write



## Resource types defined by Amazon Elastic Transcoder
<a name="list_elastictranscoder-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [job](https://docs.aws.amazon.com/elastictranscoder/latest/developerguide/operations-jobs.html)  | arn:${Partition}:elastictranscoder:${Region}:${Account}:job/${JobId} |   | 
|  [pipeline](https://docs.aws.amazon.com/elastictranscoder/latest/developerguide/operations-pipelines.html)  | arn:${Partition}:elastictranscoder:${Region}:${Account}:pipeline/${PipelineId} |   | 
|  [preset](https://docs.aws.amazon.com/elastictranscoder/latest/developerguide/operations-presets.html)  | arn:${Partition}:elastictranscoder:${Region}:${Account}:preset/${PresetId} |   | 

## Condition keys for Amazon Elastic Transcoder
<a name="list_elastictranscoder-policy-keys"></a>

Amazon Elastic Transcoder has no service-specific condition keys that can be used in the `Condition` element of policy statements.