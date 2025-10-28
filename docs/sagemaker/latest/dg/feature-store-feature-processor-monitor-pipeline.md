# Monitor Amazon SageMaker Feature Store Feature

Processor pipelines

AWS provides monitoring tools to watch your Amazon SageMaker AI resources and applications in real
time, report when something goes wrong, and take automatic actions when appropriate. Feature Store
Feature Processor pipelines are Pipelines, so the standard monitoring mechanisms and integrations
are available. Operational metrics such as execution failures can be monitored via Amazon CloudWatch
metrics and Amazon EventBridge events.

For more information on how to monitor and operationalize Feature Store Feature Processor, see the
following resources:

- [Monitoring AWS resources in Amazon SageMaker AI](monitoring-overview.md "monitoring-overview.md") - General
  guidance on monitoring and auditing activity for SageMaker AI resources.
- [SageMaker pipelines metrics](monitoring-cloudwatch.md#cloudwatch-metrics-pipelines "monitoring-cloudwatch.md#cloudwatch-metrics-pipelines") - CloudWatch Metrics emitted by Pipelines.
- [SageMaker pipeline execution state change](automating-sagemaker-with-eventbridge.md#eventbridge-pipeline "automating-sagemaker-with-eventbridge.md#eventbridge-pipeline") - EventBridge
  events emitted for Pipelines and executions.
- [Troubleshooting Amazon SageMaker Pipelines](pipelines-troubleshooting.md "pipelines-troubleshooting.md") -
  General debugging and troubleshooting tips for Pipelines.
  Feature Store Feature Processor execution logs can be found in Amazon CloudWatch Logs under the
  `/aws/sagemaker/TrainingJobs` log group, where you can find the execution log
  streams using lookup conventions. For executions created by directly invoking the
  `@feature_processor` decorated function, you can find logs in your local execution
  environment’s console. For `@remote` decorated executions, the CloudWatch Logs stream name
  contains the name of the function and the execution timestamp. For Feature Processor pipeline
  executions, the CloudWatch Logs stream for the step contains the `feature-processor` string and
  the pipeline execution ID.

Feature Store Feature Processor pipelines and recent execution statuses can be found in
Amazon SageMaker Studio Classic for a given feature group in the Feature Store UI. Feature groups related to the Feature
Processor pipelines as either inputs or outputs are displayed in the UI. In addition, the
lineage view can provide context into upstream executions, such as data producing Feature
Processor pipelines and data sources, for further debugging. For more information on using the
lineage view using Studio Classic, see [View lineage
from the console](feature-store-use-with-studio.md#feature-store-view-feature-processor-pipeline-lineage-studio "feature-store-use-with-studio.md#feature-store-view-feature-processor-pipeline-lineage-studio").
