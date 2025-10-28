# View pipeline details and history (CLI)

You can run the following commands to view details about your pipelines and pipeline
executions:

- **list-pipelines** command to view a summary of all of the
  pipelines associated with your AWS account.
- **get-pipeline** command to review details of a single
  pipeline.
- **list-pipeline-executions** to view summaries of the most
  recent executions for a pipeline.
- **get-pipeline-execution** to view information about an
  execution of a pipeline, including details about artifacts, the pipeline
  execution ID, and the name, version, and status of the pipeline.
- **get-pipeline-state** command to view pipeline, stage, and
  action status.
- **list-action-executions** to view action execution details for
  a pipeline.

###### Topics

1. Open a terminal (Linux, macOS, or Unix) or command prompt (Windows) and use the AWS CLI to
   run the **[list-pipelines](../../../cli/latest/reference/codepipeline/list-pipelines.md "../../../cli/latest/reference/codepipeline/list-pipelines.md")** command:

```
aws codepipeline list-pipelines
```

This command returns a list of all of the pipelines associated with your AWS
account. 2. To view details about a pipeline, run the
**[get-pipeline](../../../cli/latest/reference/codepipeline/get-pipeline.md "../../../cli/latest/reference/codepipeline/get-pipeline.md")** command, specifying the unique
name of the pipeline. For example, to view details about a pipeline named
`MyFirstPipeline`, enter the
following:

```
aws codepipeline get-pipeline --name `MyFirstPipeline`
```

This command returns the structure of the pipeline.
