# Creating and

running Feature Store Feature Processor pipelines

The Feature Processor SDK provides APIs to promote your Feature Processor Definitions into
a fully managed SageMaker AI Pipeline. For more information on Pipelines, see [Pipelines overview](pipelines-overview.md "pipelines-overview.md"). To convert your Feature
Processor Definitions in to a SageMaker AI Pipeline, use the `to_pipeline` API with your
Feature Processor definition. You can schedule executions of your Feature Processor
Definition can be scheduled, operationally monitor them with CloudWatch metrics, and integrate
them with EventBridge to act as event sources or subscribers. For more information about monitoring
pipelines created with Pipelines, see [Monitor Amazon SageMaker Feature Store Feature
Processor pipelines](feature-store-feature-processor-monitor-pipeline.md "feature-store-feature-processor-monitor-pipeline.md").

To view your Feature Processor pipelines, see [View
pipeline executions from the console](feature-store-use-with-studio.md#feature-store-view-feature-processor-pipeline-executions-studio "feature-store-use-with-studio.md#feature-store-view-feature-processor-pipeline-executions-studio").

If your function is also decorated with the `@remote` decorator, then its
configurations is carried over to the Feature Processor pipeline. You can specify advanced
configurations such as compute instance type and count, runtime dependencies, network and
security configurations using the `@remote` decorator.

The following example uses the `to_pipeline` and `execute`
APIs.

```
from sagemaker.feature_store.feature_processor import (
    execute, to_pipeline, describe, TransformationCode
)

pipeline_name="feature-processor-pipeline"
pipeline_arn = to_pipeline(
    pipeline_name=pipeline_name,
    step=transform,
    transformation_code=TransformationCode(s3_uri="s3://bucket/prefix"),
)

pipeline_execution_arn = execute(
    pipeline_name=pipeline_name
)
```

The `to_pipeline` API is semantically an upsert operation. It updates the
pipeline if it already exists; otherwise, it creates a pipeline.

The `to_pipeline` API optionally accepts an Amazon S3 URI that
references a file containing the Feature Processor definition to associate it with the
Feature Processor pipeline to track the transformation function and its versions in its SageMaker AI
machine learning lineage.

To retrieve a list of every Feature Processor pipeline in your account, you can use the
`list_pipelines` API. A subsequent request to the `describe` API
returns details related to the Feature Processor pipeline including, but not limited to,
Pipelines and schedule details.

The following example uses the `list_pipelines` and `describe`
APIs.

```
from sagemaker.feature_store.feature_processor import list_pipelines, describe

feature_processor_pipelines = list_pipelines()

pipeline_description = describe(
    pipeline_name = feature_processor_pipelines[0]
)
```
