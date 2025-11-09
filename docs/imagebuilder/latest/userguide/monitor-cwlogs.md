# Monitor Image Builder logs with Amazon CloudWatch Logs

CloudWatch Logs support is turned on by default. Image Builder retains build logs on the instance during
the build process, then streams the logs to CloudWatch Logs when the build is complete. Before it
creates the final build image, Image Builder removes local logs from the instance.

**Image build logs**

Image build logs contain the detailed logs for an individual image build. Image Builder
writes image build logs to the following Image Builder CloudWatch Logs group and stream:

**LogGroup:**
`/aws/imagebuilder/`ImageName``

**LogStream (x.x.x/x):**
`ImageVersion/ImageBuildVersion`

**Pipeline execution logs**

Image Builder writes pipeline execution logs when an image pipeline runs or when a pipeline skips
a regularly scheduled run, along with details about why that happened. For example,
when dependency updates are configured for a scheduled pipeline, the following scenarios
will have associated messaging:

- Image Builder writes a log entry when it skips pipeline execution because there were no
  dependency updates.
- When there is a dependency update, Image Builder logs the ARN of the resource that changed.

Image Builder writes pipeline execution logs to the following Image Builder CloudWatch Logs group and stream:

**LogGroup:**
`/aws/imagebuilder/pipeline/`pipeline-name``

**LogStream:**
`2025/09/01` (the pipeline execution date
in YYYY/MM/DD format)

Each pipeline log is appended to the stream for that day.

**Custom log groups**

If you've specified custom log groups for image or pipeline logging, Image Builder
writes the logs to the LogGroup that you've specified in your pipeline, or in
one of the create image commands if you ran the build manually. For more information
about how this works in Image Builder, see [Configure pipeline logging](schedule-pipeline.md#configure-pipeline-logging "schedule-pipeline.md#configure-pipeline-logging").

 

###### Opt out

You can opt out of CloudWatch Logs streaming by removing the following permissions associated
with the custom role that applies for your use case.

- logs:CreateLogGroup
- logs:CreateLogStream
- logs:PutLogEvents

| Log type           | Custom role           |
| ------------------ | --------------------- |
| Image build        | Execution role        |
| Pipeline execution | Execution role        |
| Component logs     | Instance profile role |

For advanced troubleshooting, you can run predefined commands and scripts using [AWS Systems Manager Run
Command](../../../systems-manager/latest/userguide/run-command.md "../../../systems-manager/latest/userguide/run-command.md"). For more information, see [Troubleshoot Image Builder issues](troubleshooting.md "troubleshooting.md").
