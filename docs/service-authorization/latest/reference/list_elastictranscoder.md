# Actions, resources, and condition keys for Amazon Elastic Transcoder

Amazon Elastic Transcoder (service prefix: `elastictranscoder`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../elastictranscoder/latest/developerguide.md "../../../elastictranscoder/latest/developerguide.md").
- View a list of the [API operations available for
  this service](../../../elastictranscoder/latest/developerguide/api-reference.md "../../../elastictranscoder/latest/developerguide/api-reference.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../elastictranscoder/latest/developerguide/access-control.md "../../../elastictranscoder/latest/developerguide/access-control.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/elastictranscoder/elastictranscoder.json "https://servicereference.us-east-1.amazonaws.com/v1/elastictranscoder/elastictranscoder.json") for this service.

###### Topics

- [Actions defined by Amazon Elastic Transcoder](#list_elastictranscoder-actions-as-permissions "#list_elastictranscoder-actions-as-permissions")
- [Resource types defined by Amazon Elastic Transcoder](#list_elastictranscoder-resources-for-iam-policies "#list_elastictranscoder-resources-for-iam-policies")
- [Condition keys for Amazon Elastic Transcoder](#list_elastictranscoder-policy-keys "#list_elastictranscoder-policy-keys")

## Actions defined by Amazon Elastic Transcoder

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS. When
you use an action in a policy, you usually allow or deny access to the API operation or CLI
command with the same name. However, in some cases, a single action controls access to more
than one operation. Alternatively, some operations require several different actions.

| Actions                                                                                                                                                                                              | Description                                                                                                           | Resource types (\*required)                                                                         | Condition keys | Access level |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | -------------- | ------------ |
| [CancelJob](../../../elastictranscoder/latest/developerguide/cancel-job.md "../../../elastictranscoder/latest/developerguide/cancel-job.md")                                                         | Cancel a job that Elastic Transcoder has not begun to process                                                         | [job\*](#list_elastictranscoder-resource-job "#list_elastictranscoder-resource-job")                |                | Write        |
| [CreateJob](../../../elastictranscoder/latest/developerguide/create-job.md "../../../elastictranscoder/latest/developerguide/create-job.md")                                                         | Create a job                                                                                                          | [pipeline\*](#list_elastictranscoder-resource-pipeline "#list_elastictranscoder-resource-pipeline") |                | Write        |
| [preset\*](#list_elastictranscoder-resource-preset "#list_elastictranscoder-resource-preset")                                                                                                        |                                                                                                                       |
| [CreatePipeline](../../../elastictranscoder/latest/developerguide/create-pipeline.md "../../../elastictranscoder/latest/developerguide/create-pipeline.md")                                          | Create a pipeline                                                                                                     |                                                                                                     |                | Write        |
| [CreatePreset](../../../elastictranscoder/latest/developerguide/create-preset.md "../../../elastictranscoder/latest/developerguide/create-preset.md")                                                | Create a preset                                                                                                       |                                                                                                     |                | Write        |
| [DeletePipeline](../../../elastictranscoder/latest/developerguide/delete-pipeline.md "../../../elastictranscoder/latest/developerguide/delete-pipeline.md")                                          | Delete a pipeline                                                                                                     | [pipeline\*](#list_elastictranscoder-resource-pipeline "#list_elastictranscoder-resource-pipeline") |                | Write        |
| [DeletePreset](../../../elastictranscoder/latest/developerguide/delete-preset.md "../../../elastictranscoder/latest/developerguide/delete-preset.md")                                                | Delete a preset                                                                                                       | [preset\*](#list_elastictranscoder-resource-preset "#list_elastictranscoder-resource-preset")       |                | Write        |
| [ListJobsByPipeline](../../../elastictranscoder/latest/developerguide/list-jobs-by-pipeline.md "../../../elastictranscoder/latest/developerguide/list-jobs-by-pipeline.md")                          | Get a list of the jobs that you assigned to a pipeline                                                                | [pipeline\*](#list_elastictranscoder-resource-pipeline "#list_elastictranscoder-resource-pipeline") |                | List         |
| [ListJobsByStatus](../../../elastictranscoder/latest/developerguide/list-jobs-by-status.md "../../../elastictranscoder/latest/developerguide/list-jobs-by-status.md")                                | Get information about all of the jobs associated with the current AWS account that have a specified status            |                                                                                                     |                | List         |
| [ListPipelines](../../../elastictranscoder/latest/developerguide/list-pipelines.md "../../../elastictranscoder/latest/developerguide/list-pipelines.md")                                             | Get a list of the pipelines associated with the current AWS account                                                   |                                                                                                     |                | List         |
| [ListPresets](../../../elastictranscoder/latest/developerguide/list-presets.md "../../../elastictranscoder/latest/developerguide/list-presets.md")                                                   | Get a list of all presets associated with the current AWS account                                                     |                                                                                                     |                | List         |
| [ReadJob](../../../elastictranscoder/latest/developerguide/get-job.md "../../../elastictranscoder/latest/developerguide/get-job.md")                                                                 | Get detailed information about a job                                                                                  | [job\*](#list_elastictranscoder-resource-job "#list_elastictranscoder-resource-job")                |                | Read         |
| [ReadPipeline](../../../elastictranscoder/latest/developerguide/get-pipeline.md "../../../elastictranscoder/latest/developerguide/get-pipeline.md")                                                  | Get detailed information about a pipeline                                                                             | [pipeline\*](#list_elastictranscoder-resource-pipeline "#list_elastictranscoder-resource-pipeline") |                | Read         |
| [ReadPreset](../../../elastictranscoder/latest/developerguide/get-preset.md "../../../elastictranscoder/latest/developerguide/get-preset.md")                                                        | Get detailed information about a preset                                                                               | [preset\*](#list_elastictranscoder-resource-preset "#list_elastictranscoder-resource-preset")       |                | Read         |
| [TestRole](../../../elastictranscoder/latest/developerguide/test-pipeline-role.md "../../../elastictranscoder/latest/developerguide/test-pipeline-role.md")                                          | Test the settings for a pipeline to ensure that Elastic Transcoder can create and process jobs                        |                                                                                                     |                | Write        |
| [UpdatePipeline](../../../elastictranscoder/latest/developerguide/update-pipeline.md "../../../elastictranscoder/latest/developerguide/update-pipeline.md")                                          | Update settings for a pipeline                                                                                        | [pipeline\*](#list_elastictranscoder-resource-pipeline "#list_elastictranscoder-resource-pipeline") |                | Write        |
| [UpdatePipelineNotifications](../../../elastictranscoder/latest/developerguide/update-pipeline-notifications.md "../../../elastictranscoder/latest/developerguide/update-pipeline-notifications.md") | Update only Amazon Simple Notification Service (Amazon SNS) notifications for a pipeline                              | [pipeline\*](#list_elastictranscoder-resource-pipeline "#list_elastictranscoder-resource-pipeline") |                | Write        |
| [UpdatePipelineStatus](../../../elastictranscoder/latest/developerguide/update-pipeline-status.md "../../../elastictranscoder/latest/developerguide/update-pipeline-status.md")                      | Pause or reactivate a pipeline, so the pipeline stops or restarts processing jobs, update the status for the pipeline | [pipeline\*](#list_elastictranscoder-resource-pipeline "#list_elastictranscoder-resource-pipeline") |                | Write        |

## Resource types defined by Amazon Elastic Transcoder

The following resource types are defined by this service and can be used in the
`Resource` element of IAM permission policy statements.

| Resource types                                                                                                                                                  | ARN                                                                            | Condition keys |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | -------------- |
| [job](../../../elastictranscoder/latest/developerguide/operations-jobs.md "../../../elastictranscoder/latest/developerguide/operations-jobs.md")                | arn:${Partition}:elastictranscoder:${Region}:${Account}:job/${JobId}           |                |
| [pipeline](../../../elastictranscoder/latest/developerguide/operations-pipelines.md "../../../elastictranscoder/latest/developerguide/operations-pipelines.md") | arn:${Partition}:elastictranscoder:${Region}:${Account}:pipeline/${PipelineId} |                |
| [preset](../../../elastictranscoder/latest/developerguide/operations-presets.md "../../../elastictranscoder/latest/developerguide/operations-presets.md")       | arn:${Partition}:elastictranscoder:${Region}:${Account}:preset/${PresetId}     |                |

## Condition keys for Amazon Elastic Transcoder

Amazon Elastic Transcoder has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
