# Feature Processing

Amazon SageMaker Feature Store Feature Processing is a capability with which you can transform raw data into
machine learning (ML) features. It provides you with a Feature Processor SDK with which you
can transform and ingest data from batch data sources into your feature groups. With this
capability, Feature Store takes care of the underlying infrastructure including provisioning the
compute environments and creating and maintaining Pipelines to load and ingest data. This way
you can focus on your feature processor definitions that includes a transformation function
(for example, count of product views, mean of transaction value), sources (where to apply
this transformation on), and sinks (where to write the computed feature values to).

Feature Processor pipeline is a Pipelines pipeline. As a Pipelines, you can also track scheduled
Feature Processor pipelines with SageMaker AI lineage in the console. For more information on SageMaker AI
Lineage, see [Amazon SageMaker ML Lineage Tracking](lineage-tracking.md "lineage-tracking.md") This
includes tracking scheduled executions, visualizing lineage to trace features back to their
data sources, and viewing shared feature processors in a single environment. For information
on using Feature Store with the console, see [View
pipeline executions from the console](feature-store-use-with-studio.md#feature-store-view-feature-processor-pipeline-executions-studio "feature-store-use-with-studio.md#feature-store-view-feature-processor-pipeline-executions-studio").

###### Topics

- [Feature Store Feature Processor SDK](feature-store-feature-processor-sdk.md "feature-store-feature-processor-sdk.md")
- [Running Feature Store Feature
  Processor remotely](feature-store-feature-processor-execute-remotely.md "feature-store-feature-processor-execute-remotely.md")
- [Creating and
  running Feature Store Feature Processor pipelines](feature-store-feature-processor-create-execute-pipeline.md "feature-store-feature-processor-create-execute-pipeline.md")
- [Scheduled and event
  based executions for Feature Processor pipelines](feature-store-feature-processor-schedule-pipeline.md "feature-store-feature-processor-schedule-pipeline.md")
- [Monitor Amazon SageMaker Feature Store Feature
  Processor pipelines](feature-store-feature-processor-monitor-pipeline.md "feature-store-feature-processor-monitor-pipeline.md")
- [IAM permissions and
  execution roles](feature-store-feature-processor-iam-permissions.md "feature-store-feature-processor-iam-permissions.md")
- [Feature Processor restrictions, limits,
  and quotas](feature-store-feature-processor-quotas.md "feature-store-feature-processor-quotas.md")
- [Data sources](feature-store-feature-processor-data-sources.md "feature-store-feature-processor-data-sources.md")
- [Example Feature Processing code
  for common use cases](feature-store-feature-processor-examples.md "feature-store-feature-processor-examples.md")
