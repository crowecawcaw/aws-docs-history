# Workflows

To use Amazon MWAA Serverless for orchestration, first create a workflow as a YAML definition file. If you already have a Python DAG file, convert it to YAML with the
[DAG converter](https://pypi.org/project/python-to-yaml-dag-converter-mwaa-serverless/ "https://pypi.org/project/python-to-yaml-dag-converter-mwaa-serverless/") tool. For instructions, refer to
[Convert Python DAG to YAML definition](workflows-migrate.md "workflows-migrate.md").

###### Important

Each workflow needs an IAM role. This role defines what AWS resources the workflow can access during execution.

Amazon MWAA Serverless workflows can be run on-demand or scheduled. Amazon MWAA Serverless workflows can be one of the following three types:

- **Scheduled**: Your workflow is run on the schedule you define in the workflow definition. You can still run your workflow on-demand outside of this schedule.
  This is similar to an `unpaused` DAG in Apache Airflow.
- **Disabled**: A disabled workflow can not be run on schedule or on-demand. This is like a `paused` DAG in Apache Airflow.
- **Manual only**: Your workflow ignores any defined schedules and can be only run on-demand. This option is best for testing or temporarily disabling automatic runs.

###### Note

Unlike Apache Airflow, Amazon MWAA Serverless doesn't automatically stop executing workflow runs when a workflow is set to
**Manual only** or **Disabled**. Amazon MWAA Serverless uses a separate API [`StopWorkflowRun`](../../../MWAA-serverless/APIReference/API_StopWorkflowRun.md "../../../MWAA-serverless/APIReference/API_StopWorkflowRun.md")
call to stop all workflow runs.

###### Topics

- [Manage your Amazon MWAA Serverless workflows](#workflows-manage "#workflows-manage")
- [Workflow states](#workflows-states "#workflows-states")
- [Convert Python DAG to YAML definition](workflows-migrate.md "workflows-migrate.md")
- [Tag a workflow](workflows-tags.md "workflows-tags.md")

## Manage your Amazon MWAA Serverless workflows

An Amazon MWAA Serverless workflow can be created using CLI or APIs. After uploading the workflow definition YAML in an Amazon S3 bucket, create the workflow. If you already have a
Python workflow (DAG file), you can migrate it to Amazon MWAA Serverless by converting it into a YAML file. For more information, refer to
[Convert Python DAG to YAML definition](workflows-migrate.md "workflows-migrate.md").

To create your workflow using CLI, use `create-workflow`

CLI

```

aws mwaa-serverless create-workflow --name `my-workflow-name` --definition-s3-location'{"Bucket": "`my-bucket-name`", "ObjectKey": "`my-yaml-file`"}'

```

To run your workflow, use [`start-workflow-run`](../../../MWAA-serverless/APIReference/API_StartWorkflowRun.md "../../../MWAA-serverless/APIReference/API_StartWorkflowRun.md") and provide the `workflow-arn`.
This command starts a new workflow execution.

CLI

```

aws mwaa-serverless get-workflow --workflow-arn arn:aws:airflow-serverless:`us-east-1`:`111122223333`:workflow/`workflow-name`

```

The following table contains all the actions you can perform on an Amazon MWAA Serverless workflow:

| Action                                                                                     | API                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Create workflow (the YAML file must already be in your Amazon S3 bucket).                  | [`CreateWorkflow`](../../../mwaa-serverless/latest/APIReference/API_CreateWorkflow.md "../../../mwaa-serverless/latest/APIReference/API_CreateWorkflow.md")                   |
| Delete a workflow and all its versions. You must stop a workflow before you can delete it. | [`DeleteWorkflow`](../../../mwaa-serverless/latest/APIReference/API_DeleteWorkflow.md "../../../mwaa-serverless/latest/APIReference/API_DeleteWorkflow.md").                  |
| Retrieve detailed information about a workflow.                                            | [`GetWorkflow`](../../../mwaa-serverless/latest/APIReference/API_GetWorkflow.md "../../../mwaa-serverless/latest/APIReference/API_GetWorkflow.md")                            |
| List all workflows.                                                                        | [`ListWorkflows`](../../../mwaa-serverless/latest/APIReference/API_ListWorkflows.md "../../../mwaa-serverless/latest/APIReference/API_ListWorkflows.md")                      |
| List all the verisions of a specified workflow.                                            | [`ListWorkflowVersions`](../../../mwaa-serverless/latest/APIReference/API_ListWorkflowVersions.md "../../../mwaa-serverless/latest/APIReference/API_ListWorkflowVersions.md") |
| Start a workflow run.                                                                      | [`StartWorkflowRun`](../../../mwaa-serverless/latest/APIReference/API_StartWorkflowRun.md "../../../mwaa-serverless/latest/APIReference/API_StartWorkflowRun.md")             |
| Stop a workflow run.                                                                       | [`StopWorkflowRun`](../../../mwaa-serverless/latest/APIReference/API_StopWorkflowRun.md "../../../mwaa-serverless/latest/APIReference/API_StopWorkflowRun.md")                |
| Edit the configuration settings of a workflow.                                             | [`UpdateWorkflow`](../../../mwaa-serverless/latest/APIReference/API_UpdateWorkflow.md "../../../mwaa-serverless/latest/APIReference/API_UpdateWorkflow.md")                   |
| List tags for a workflow.                                                                  | [`ListTagsForResource`](../../../mwaa-serverless/latest/APIReference/API_ListTagsForResource.md "../../../mwaa-serverless/latest/APIReference/API_ListTagsForResource.md")    |
| Tag a workflow.                                                                            | [`TagResource`](../../../mwaa-serverless/latest/APIReference/API_TagResource.md "../../../mwaa-serverless/latest/APIReference/API_TagResource.md")                            |
| Untag a workflow.                                                                          | [`UntagResource`](../../../mwaa-serverless/latest/APIReference/API_UntagResource.md "../../../mwaa-serverless/latest/APIReference/API_UntagResource.md")                      |

## Workflow states

When you create a workflow with Amazon MWAA Serverless, it can have a `READY` or a `DELETING` state. When you run a workflow, it can adopt the following states.

| State      | Description                                           |
| ---------- | ----------------------------------------------------- |
| `STARTING` | The workflow is ready to run.                         |
| `QUEUED`   | The workflow is waiting in the queue to run.          |
| `RUNNING`  | The workflow is in progress.                          |
| `SUCCESS`  | The workflow completed successfully.                  |
| `FAILED`   | The workflow failed.                                  |
| `TIMEOUT`  | The workflow timed out before it completed.           |
| `STOPPING` | The workflow run is being stopped.                    |
| `STOPPED`  | The workflow is stopped and no resources are running. |
