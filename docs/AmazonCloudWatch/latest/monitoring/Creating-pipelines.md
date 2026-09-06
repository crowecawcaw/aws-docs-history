

# Creating pipelines
<a name="Creating-pipelines"></a>

CloudWatch pipelines supports creating pipelines for both logs and metrics data. The following sections describe how to create each type of pipeline.

## Creating a logs pipeline
<a name="creating-logs-pipeline"></a>

The pipeline configuration wizard guides you through creating your logs data pipeline.

1. Under **General settings**, provide the data source details including source name and type. You can also specify pipeline tags and the name of your pipeline.

1. Under **Destination**, specify the destination details. For logs pipelines, CloudWatch Logs is the only supported destination. For metrics pipelines, CloudWatch Metrics is the only supported destination.

1. Under **Processor**, add the desired processors and parsers. A parser is a required first step for certain data types. You can perform custom parsing using processors like Grok or CSV. You can use the lookup processor to enrich log events with data from an Amazon CloudWatch Logs lookup table. Processors that are not supported by the data type are disabled.

   To configure processors using natural language, enable the **AI-assisted** toggle. Enter a description of the log transformations you need, and CloudWatch pipelines generates the processor configuration automatically. For AWS vended logs, a sample log event is also generated so you can verify the output before deploying. You can review and edit the generated configuration before creating the pipeline.
**Important**  
To use AI-assisted processor configuration, you must have the `logs:GeneratePipeline` IAM permission. For more information, see [AI-assisted processor configuration permissions](pipeline-iam-reference.md#ai-assisted-permissions).

   You can also add conditional processing rules to supported processors using the `when` parameter. Conditional processing lets you control which log entries a processor acts on. For the expression syntax and supported processors, see [Expression syntax for conditional processing](conditional-processing.md).

   To preserve unmodified copies of your log data for audit or compliance purposes, enable the **Keep original log** toggle. When enabled, CloudWatch pipelines automatically stores a copy of each raw log event before any transformation takes place in the `@original_message` system field of the event. This ensures that original data is always available for audits or investigations, even after processors modify the log events. The **Keep original log** toggle is only available for pipelines with a CloudWatch vended log source.

1. Under **Review and create**, review the pipeline configuration. If you're satisfied with the configuration, choose **Create pipeline** to start deployment and creation of pipeline resources. Pipeline creation completion takes up to 5 minutes depending on the source type. Upon completion, you'll be taken to the Pipelines tab in the Ingestion Console.

**Important**  
Pipeline processor configurations are logged in AWS CloudTrail events for auditing and compliance purposes. To protect sensitive information, do not include passwords, API keys, or other sensitive information in processor configurations.

## Creating a metrics pipeline
<a name="creating-metrics-pipeline"></a>

You can create a metrics pipeline by using the CloudWatch console or the AWS CLI. With a metrics pipeline, you can process CloudWatch metrics data, apply transformations, and forward the processed metrics to CloudWatch.

### To create a metrics pipeline (console)
<a name="creating-metrics-pipeline-console"></a>

Use the following procedure to create a metrics pipeline in the CloudWatch console.

1. Open the CloudWatch console and in the navigation pane, choose **Ingestion**, **Pipelines**.

1. Choose **Create pipeline**.

1. For the source type, select **CloudWatch Metrics (OTel)**.

1. Configure the selection criteria to specify which metrics the pipeline processes. Selection criteria use OTel attribute paths such as `resource.attributes`, `metric.name`, and `datapoint.attributes`. All criteria use AND semantics (all must match).

1. Under **Processor**, add up to 20 processors to transform your metrics data.

1. Under **Review and create**, review the pipeline configuration and choose **Create pipeline**.

### To create a metrics pipeline (AWS CLI)
<a name="creating-metrics-pipeline-cli"></a>

Use the `create-telemetry-pipeline` command to create a metrics pipeline from the AWS CLI.

```
aws observabilityadmin create-telemetry-pipeline \
    --pipeline-configuration-body file://config.yaml
```

The following example shows a YAML configuration file that defines a metrics pipeline with a source, processor, and sink.

```
pipeline:
  source:
    cloudwatch_metrics:
      format: otlp
      selection_criteria:
        - match_all:
            - 'resource.attributes["service.name"] == "payment-service"'
            - 'metric.name == "http.server.request.duration"'
  processor:
    - add_attributes:
        attributes:
          - key: resource.attributes["team"]
            value: "platform-engineering"
  sink:
    - cloudwatch_metrics: {}
```

When the pipeline is created, it returns an ARN in the following format:

```
arn:aws:observabilityadmin:{{region}}:{{accountId}}:telemetry-pipeline/{{pipelineID}}
```

**Note**  
CloudWatch Metrics is the only supported destination for metrics pipelines.

### Supported API operations
<a name="metrics-pipeline-api-operations"></a>

The following table lists the API operations that you can use to manage metrics pipelines.


| Operation | Description | 
| --- | --- | 
| CreateTelemetryPipeline | Creates a new metrics pipeline. | 
| GetTelemetryPipeline | Retrieves details about a specific metrics pipeline. | 
| ListTelemetryPipelines | Lists all metrics pipelines in your account. | 
| DeleteTelemetryPipeline | Deletes a metrics pipeline. | 
| ValidateTelemetryPipelineConfiguration | Validates a pipeline configuration before creation. | 
| UpdateTelemetryPipeline | Updates an existing metrics pipeline configuration. | 