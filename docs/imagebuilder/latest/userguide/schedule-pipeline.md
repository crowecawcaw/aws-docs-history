# Configure pipeline execution settings for image pipelines

You can choose from the following options to schedule pipeline execution:

Schedule Builder

Use the Schedule Builder to configure automatic, recurring
pipeline execution. You define when and how often your pipeline should
run (day, time, and frequency). The default schedule is every week based on the
day and time that the schedule is created (UTC).

Cron expression

Automatically run the pipeline with a cron expression that specifies
the schedule. For more information about the cron syntax that Image Builder uses,
see [Use cron expressions in Image Builder](cron-expressions.md "cron-expressions.md").

Manual

The pipeline does not run on a schedule. In the console, choose
**Run pipeline** from the **Actions**
menu to run the pipeline. From the AWS CLI, you can run
`start-image-pipeline-execution`.

###### Dependency settings

For scheduled builds, you can choose whether to always run on the schedule
or to skip pipeline execution unless there are dependency updates, such as a
change to the base image or to a component that's used in the recipe.

## Automatically disable a failing pipeline

For image pipelines that run on a schedule, you can configure the maximum
number of consecutive failures to allow (up to`10`) before Image Builder
automatically disables the pipeline.

###### Auto-disable settings

Image Builder tracks the number of consecutive failures for scheduled pipeline
executions and takes one of the following actions each time it runs on a
schedule:

- If the pipeline execution is successful, the number of consecutive
  failures resets to zero.
- If the pipeline execution fails, Image Builder increments the number of
  consecutive failures. If the failure count exceeds the limit defined in the
  `AutoDisablePolicy`, Image Builder disables the pipeline.

The consecutive failure count is also reset to zero under the following
conditions:

- The pipeline runs manually and succeeds.
- The pipeline configuration is updated.

If the pipeline runs manually and fails, the count remains the same. The next
scheduled run continues to increment where it left off before.

## Configure pipeline logging

When you create or update an image pipeline, you can configure custom CloudWatch Logs
groups for image build and pipeline logs. Make sure that your custom pipeline
execution role has the following permissions to create and access the log group
resources.

- logs:CreateLogGroup
- logs:CreateLogStream
- logs:PutLogEvents

###### Custom log groups

To use custom log groups for image build or pipeline execution, first
create the log group in CloudWatch Logs. For more information, see [Create a log group](../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md#Create-Log-Group "../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md#Create-Log-Group") in the _Amazon CloudWatch Logs User Guide_. For
additional guidance on log group naming requirements, see [CreateLogGroup](../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLogGroup.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLogGroup.md") in the _Amazon CloudWatch Logs API Reference_.

Console
Specify the **Image log group** or
**Pipeline log group** for your pipeline in the
**Logging configuration** section under
**Advanced settings**.

CLI
Specify the following fields within the `logging-configuration` object
if you use a JSON object for configuration:

- `imageLogGroupName`
- `pipelineLogGroupName`

To specify all parameters directly in the command line, see
[create-image-pipeline](../../../cli/latest/reference/imagebuilder/create-image-pipeline.md "../../../cli/latest/reference/imagebuilder/create-image-pipeline.md") in the _AWS CLI Command Reference_.

Image Builder uses the following default log groups if you don't specify a custom
log group:

Image build logs

Image Builder writes build logs to the following Image Builder CloudWatch Logs group and stream:

**LogGroup:**
`/aws/imagebuilder/`ImageName``

**LogStream (x.x.x/x):**
`ImageVersion/ImageBuildVersion`

Pipeline execution logs

Image Builder writes pipeline execution logs to the following Image Builder CloudWatch Logs group and stream:

**LogGroup:**
`/aws/imagebuilder/pipeline/`pipeline-name``

**LogStream:**
`2025/09/01` (the pipeline execution date in YYYY/MM/DD format)

Each pipeline log is appended to the stream for that day.
