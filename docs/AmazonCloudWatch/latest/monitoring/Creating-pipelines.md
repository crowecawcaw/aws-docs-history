# Creating pipelines

The pipeline configuration wizard guides you through creating your data
pipeline.

1. Under **General settings**, provide the data source details
   including source name and type. You can also specify pipeline tags and the name
   of your pipeline.
2. Under **Destination**, specify the destination details. CloudWatch Logs
   is the default destination.
3. Under **Processor**, add the desired processors and parsers.
   A parser is a required first step for certain data types. You can perform custom
   parsing using processors like Grok or CSV. Processors that are not supported by the
   data type are disabled.

To configure processors using natural language, enable the
**AI-assisted** toggle. Enter a description of the log
transformations you need, and CloudWatch pipelines generates the processor configuration
automatically. For AWS vended logs, a sample log event is also generated so
you can verify the output before deploying. You can review and edit the generated
configuration before creating the pipeline.

###### Important

To use AI-assisted processor configuration, you must have the
`logs:GeneratePipeline` IAM permission. For more information, see
[AI-assisted processor configuration permissions](pipeline-iam-reference.md#ai-assisted-permissions "pipeline-iam-reference.md#ai-assisted-permissions").

You can also add conditional processing rules to supported processors using
the `when` parameter. Conditional processing lets you
control which log entries a processor acts on. For the expression syntax and
supported processors, see
[Expression syntax for conditional processing](conditional-processing.md "conditional-processing.md").

To preserve unmodified copies of your log data for audit or compliance
purposes, enable the **Keep original log** toggle. When
enabled, CloudWatch pipelines automatically stores a copy of each raw log event before any
transformation takes place in the `@original_message` system field
of the event. This ensures that original data is always
available for audits or investigations, even after processors modify the log
events. The **Keep original log** toggle is only available
for pipelines with a CloudWatch vended log source. 4. Under **Review and create**, review the pipeline
configuration. If you're satisfied with the configuration, choose
**Create pipeline** to start deployment and creation of
pipeline resources. Pipeline creation completion takes up to 5 minutes depending
on the source type. Upon completion, you'll be taken to the Pipelines tab in the
Ingestion Console.

###### Important

Pipeline processor configurations are logged in AWS CloudTrail events for
auditing and compliance purposes. To protect sensitive information, do not include
passwords, API keys, or other sensitive information in processor
configurations.
