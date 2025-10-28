# Scheduled and event

based executions for Feature Processor pipelines

Amazon SageMaker Feature Store Feature Processing pipeline executions can be configured to start automatically
and asynchronously based on a preconfigured schedule or as a result of another AWS service
event. For example, you can schedule Feature Processing pipelines to execute on the first of
every month or chain two pipelines together so that a target pipeline is executed
automatically after a source pipeline execution completes.

###### Topics

- [Schedule based executions](#feature-store-feature-processor-schedule-pipeline-schedule-based "#feature-store-feature-processor-schedule-pipeline-schedule-based")
- [Event
  based executions](#feature-store-feature-processor-schedule-pipeline-event-based "#feature-store-feature-processor-schedule-pipeline-event-based")

##

Schedule based executions

The Feature Processor SDK provides a [`schedule`](https://sagemaker.readthedocs.io/en/stable/api/prep_data/feature_store.html#sagemaker.feature_store.feature_processor.schedule "https://sagemaker.readthedocs.io/en/stable/api/prep_data/feature_store.html#sagemaker.feature_store.feature_processor.schedule") API to run Feature Processor pipelines on a
recurring basis with Amazon EventBridge Scheduler integration. The schedule can be specified with an
`at`, `rate`, or `cron` expression using the [`ScheduleExpression`](../../../scheduler/latest/APIReference/API_CreateSchedule.md#scheduler-CreateSchedule-request-ScheduleExpression "../../../scheduler/latest/APIReference/API_CreateSchedule.md#scheduler-CreateSchedule-request-ScheduleExpression") parameter with the same expressions
supported by Amazon EventBridge. The schedule API is semantically an upsert operation in that it
updates the schedule if it already exists; otherwise, it creates it. For more
information on the EventBridge expressions and examples, see [Schedule types on EventBridge Scheduler](../../../scheduler/latest/UserGuide/schedule-types.md "../../../scheduler/latest/UserGuide/schedule-types.md")
in the EventBridge Scheduler User Guide.

The following examples use the Feature Processor [`schedule`](https://sagemaker.readthedocs.io/en/stable/api/prep_data/feature_store.html#sagemaker.feature_store.feature_processor.schedule "https://sagemaker.readthedocs.io/en/stable/api/prep_data/feature_store.html#sagemaker.feature_store.feature_processor.schedule") API, using the `at`,
`rate`, and `cron` expressions.

```
from sagemaker.feature_store.feature_processor import schedule
pipeline_name='feature-processor-pipeline'

event_bridge_schedule_arn = schedule(
    pipeline_name=pipeline_name,
    schedule_expression="at(2020-11-30T00:00:00)"
)

event_bridge_schedule_arn = schedule(
    pipeline_name=pipeline_name,
    schedule_expression="rate(24 hours)"
)

event_bridge_schedule_arn = schedule(
    pipeline_name=pipeline_name,
    schedule_expression="cron(0 0-23/1 ? * * 2023-2024)"
)
```

The default timezone for date and time inputs in the `schedule` API are in
UTC. For more information about EventBridge Scheduler schedule expressions, see [`ScheduleExpression`](../../../scheduler/latest/APIReference/API_CreateSchedule.md#scheduler-CreateSchedule-request-ScheduleExpression "../../../scheduler/latest/APIReference/API_CreateSchedule.md#scheduler-CreateSchedule-request-ScheduleExpression") in the EventBridge Scheduler API Reference
documentation.

Scheduled Feature Processor pipeline executions provide your transformation function
with the scheduled execution time, to be used as an idempotency token or a fixed
reference point for date range–based inputs. To disable (i.e., pause) or re-enable a
schedule, use the `state` parameter of the [`schedule`](https://sagemaker.readthedocs.io/en/stable/api/prep_data/feature_store.html#sagemaker.feature_store.feature_processor.schedule "https://sagemaker.readthedocs.io/en/stable/api/prep_data/feature_store.html#sagemaker.feature_store.feature_processor.schedule") API with `‘DISABLED’` or
`‘ENABLED’`, respectively.

For information about Feature Processor, see [Feature Processor SDK data
sources](feature-store-feature-processor-data-sources-sdk.md "feature-store-feature-processor-data-sources-sdk.md").

## Event

based executions

A Feature Processing pipeline can be configured to automatically execute when an AWS
event occurs. The Feature Processing SDK provides a [`put_trigger`](https://sagemaker.readthedocs.io/en/stable/api/prep_data/feature_store.html#sagemaker.feature_store.feature_processor.put_trigger "https://sagemaker.readthedocs.io/en/stable/api/prep_data/feature_store.html#sagemaker.feature_store.feature_processor.put_trigger") function that accepts a list of source events
and a target pipeline. The source events must be instances of [`FeatureProcessorPipelineEvent`](https://sagemaker.readthedocs.io/en/stable/api/prep_data/feature_store.html#sagemaker.feature_store.feature_processor.FeatureProcessorPipelineEvent "https://sagemaker.readthedocs.io/en/stable/api/prep_data/feature_store.html#sagemaker.feature_store.feature_processor.FeatureProcessorPipelineEvent"), that specifies a pipeline
and [execution status](../APIReference/API_DescribePipelineExecution.md#sagemaker-DescribePipelineExecution-response-PipelineExecutionStatus "../APIReference/API_DescribePipelineExecution.md#sagemaker-DescribePipelineExecution-response-PipelineExecutionStatus") events.

The `put_trigger` function configures an Amazon EventBridge rule and target to route
events and allows you to specify an EventBridge event pattern to respond to any AWS event.
For information on these concepts, see Amazon EventBridge [rules](../../../eventbridge/latest/userguide/eb-rules.md "../../../eventbridge/latest/userguide/eb-rules.md"), [targets](../../../eventbridge/latest/userguide/eb-targets.md "../../../eventbridge/latest/userguide/eb-targets.md"), and [event
patterns](../../../eventbridge/latest/userguide/eb-event-patterns.md "../../../eventbridge/latest/userguide/eb-event-patterns.md").

Triggers can be enabled or disabled. EventBridge will start a target pipeline execution using
the role provided in the `role_arn` parameter of the `put_trigger`
API. The execution role is used by default if the SDK is used in a Amazon SageMaker Studio Classic or
Notebook environment. For information on how to get your execution role, see [Get your execution role](sagemaker-roles.md#sagemaker-roles-get-execution-role "sagemaker-roles.md#sagemaker-roles-get-execution-role").

The following example sets up:

- A SageMaker AI Pipeline using the `to_pipeline` API, that takes in your
  target pipeline name (`target-pipeline`) and your transformation
  function (`transform`). For information on your Feature Processor and
  transform function, see [Feature Processor SDK data
  sources](feature-store-feature-processor-data-sources-sdk.md "feature-store-feature-processor-data-sources-sdk.md").
- A trigger using the `put_trigger` API, that takes in
  `FeatureProcessorPipelineEvent` for the event and your target
  pipeline name (`target-pipeline`).

The `FeatureProcessorPipelineEvent` defines the trigger for when
the status of your source pipeline (`source-pipeline`) becomes
`Succeeded`. For information on the Feature Processor Pipeline
event function, see [`FeatureProcessorPipelineEvent`](https://sagemaker.readthedocs.io/en/stable/api/prep_data/feature_store.html#sagemaker.feature_store.feature_processor.FeatureProcessorPipelineEvent "https://sagemaker.readthedocs.io/en/stable/api/prep_data/feature_store.html#sagemaker.feature_store.feature_processor.FeatureProcessorPipelineEvent") in the Feature Store Read the
Docs.

```
from sagemaker.feature_store.feature_processor import put_trigger, to_pipeline, FeatureProcessorPipelineEvent

to_pipeline(pipeline_name="target-pipeline", step=transform)

put_trigger(
    source_pipeline_events=[
        FeatureProcessorPipelineEvent(
            pipeline_name="source-pipeline",
            status=["Succeeded"]
        )
    ],
    target_pipeline="target-pipeline"
)
```

For an example of using event based triggers to create continuous executions and
automatic retries for your Feature Processor pipeline, see [Continuous executions and automatic retries using event based triggers](feature-store-feature-processor-examples.md#feature-store-feature-processor-examples-continuous-execution-automatic-retries "feature-store-feature-processor-examples.md#feature-store-feature-processor-examples-continuous-execution-automatic-retries").

For an example of using event based triggers to create continuous _streaming_ and automatic retries using event based triggers,
see [Streaming custom data source examples](feature-store-feature-processor-data-sources-custom-examples.md#feature-store-feature-processor-data-sources-custom-examples-streaming "feature-store-feature-processor-data-sources-custom-examples.md#feature-store-feature-processor-data-sources-custom-examples-streaming").
