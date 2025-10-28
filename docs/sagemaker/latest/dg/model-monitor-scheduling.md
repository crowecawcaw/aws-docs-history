# Schedule monitoring jobs

Amazon SageMaker Model Monitor provides you the ability to monitor the data collected from your real-time
endpoints. You can monitor your data on a recurring schedule, or you can monitor it one
time, immediately. You can create a monitoring schedule with the [`CreateMonitoringSchedule`](../APIReference/API_CreateMonitoringSchedule.md "../APIReference/API_CreateMonitoringSchedule.md") API.

With a monitoring schedule, SageMaker AI can start processing jobs to analyze the data collected
during a given period. In the processing job, SageMaker AI compares the dataset for the current
analysis with the baseline statistics and constraints that you provide. Then, SageMaker AI generate
a violations report. In addition, CloudWatch metrics are emitted for each feature under
analysis.

SageMaker AI provides a prebuilt container for performing analysis on tabular datasets.
Alternatively, you could choose to bring your own container as outlined in the [Support for Your Own Containers
With Amazon SageMaker Model Monitor](model-monitor-byoc-containers.md "model-monitor-byoc-containers.md")
topic.

You can create a model monitoring schedule for your real-time endpoint or batch transform
job. Use the baseline resources (constraints and statistics) to compare against the
real-time traffic or batch job inputs.

###### Example baseline assignments

In the following example, the training dataset used to train the model was uploaded to
Amazon S3. If you already have it in Amazon S3, you can point to it directly.

```
# copy over the training dataset to Amazon S3 (if you already have it in Amazon S3, you could reuse it)
baseline_prefix = prefix + '/baselining'
baseline_data_prefix = baseline_prefix + '/data'
baseline_results_prefix = baseline_prefix + '/results'

baseline_data_uri = 's3://{}/{}'.format(bucket,baseline_data_prefix)
baseline_results_uri = 's3://{}/{}'.format(bucket, baseline_results_prefix)
print('Baseline data uri: {}'.format(baseline_data_uri))
print('Baseline results uri: {}'.format(baseline_results_uri))
```

```
training_data_file = open("test_data/training-dataset-with-header.csv", 'rb')
s3_key = os.path.join(baseline_prefix, 'data', 'training-dataset-with-header.csv')
boto3.Session().resource('s3').Bucket(bucket).Object(s3_key).upload_fileobj(training_data_file)
```

###### Example schedule for recurring analysis

If you are scheduling a model monitor for a real-time endpoint, use the baseline
constraints and statistics to compare against real-time traffic. The following code
snippet shows the general format you use to schedule a model monitor for a real-time
endpoint. This example schedules the model monitor to run hourly.

```
from sagemaker.model_monitor import CronExpressionGenerator
from time import gmtime, strftime

mon_schedule_name = 'my-model-monitor-schedule-' + strftime("%Y-%m-%d-%H-%M-%S", gmtime())
my_default_monitor.create_monitoring_schedule(
    monitor_schedule_name=mon_schedule_name,
    endpoint_input=EndpointInput(
        endpoint_name=endpoint_name,
        destination="/opt/ml/processing/input/endpoint"
    ),
    post_analytics_processor_script=s3_code_postprocessor_uri,
    output_s3_uri=s3_report_path,
    statistics=my_default_monitor.baseline_statistics(),
    constraints=my_default_monitor.suggested_constraints(),
    schedule_cron_expression=CronExpressionGenerator.hourly(),
    enable_cloudwatch_metrics=True,
)
```

###### Example schedule for one-time analysis

You can also schedule the analysis to run once without recurring by passing arguments
like the following to the `create_monitoring_schedule` method:

```
    schedule_cron_expression=CronExpressionGenerator.now(),
    data_analysis_start_time="-PT1H",
    data_analysis_end_time="-PT0H",
```

In these arguments, the `schedule_cron_expression` parameter schedules the
analysis to run once, immediately, with the value
`CronExpressionGenerator.now()`. For any schedule with this setting, the
`data_analysis_start_time` and `data_analysis_end_time`
parameters are required. These parameters set the start time and end time of an analysis
window. Define these times as offsets that are relative to the current time, and use ISO
8601 duration format. In this example, the times `-PT1H` and
`-PT0H` define a window between one hour in the past and the current
time. With this schedule, the analysis evaluates only the data that was collected during
the specified window.

###### Example schedule for a batch transform job

The following code snippet shows the general format you use to schedule a model
monitor for a batch transform job.

```
from sagemaker.model_monitor import (
    CronExpressionGenerator,
    BatchTransformInput,
    MonitoringDatasetFormat,
)
from time import gmtime, strftime

mon_schedule_name = 'my-model-monitor-schedule-' + strftime("%Y-%m-%d-%H-%M-%S", gmtime())
my_default_monitor.create_monitoring_schedule(
    monitor_schedule_name=mon_schedule_name,
    batch_transform_input=BatchTransformInput(
        destination="opt/ml/processing/input",
        data_captured_destination_s3_uri=s3_capture_upload_path,
        dataset_format=MonitoringDatasetFormat.csv(header=False),
    ),
    post_analytics_processor_script=s3_code_postprocessor_uri,
    output_s3_uri=s3_report_path,
    statistics=my_default_monitor.baseline_statistics(),
    constraints=my_default_monitor.suggested_constraints(),
    schedule_cron_expression=CronExpressionGenerator.hourly(),
    enable_cloudwatch_metrics=True,
)
```

```
desc_schedule_result = my_default_monitor.describe_schedule()
print('Schedule status: {}'.format(desc_schedule_result['MonitoringScheduleStatus']))
```
