# Container Contract

Inputs

The Amazon SageMaker Model Monitor platform invokes your container code according to a specified
schedule. If you choose to write your own container code, the following
environment variables are available. In this context, you can analyze the
current dataset or evaluate the constraints if you choose and emit metrics,
if applicable.

The available environment variables are the same for real-time endpoints
and batch transform jobs, except for the `dataset_format`
variable. If you are using a real-time endpoint, the
`dataset_format` variable supports the following
options:

```
{\"sagemakerCaptureJson\": {\"captureIndexNames\": [\"endpointInput\",\"endpointOutput\"]}}
```

If you are using a batch transform job, the `dataset_format`
supports the following options:

```
{\"csv\": {\"header\": [\"true\",\"false\"]}}
```

```
{\"json\": {\"line\": [\"true\",\"false\"]}}
```

```
{\"parquet\": {}}
```

The following code sample shows the complete set of environment variables
available for your container code (and uses the `dataset_format`
format for a real-time endpoint).

```
"Environment": {
 "dataset_format": "{\"sagemakerCaptureJson\": {\"captureIndexNames\": [\"endpointInput\",\"endpointOutput\"]}}",
 "dataset_source": "/opt/ml/processing/endpointdata",
 "end_time": "2019-12-01T16: 20: 00Z",
 "output_path": "/opt/ml/processing/resultdata",
 "publish_cloudwatch_metrics": "Disabled",
 "sagemaker_endpoint_name": "endpoint-name",
 "sagemaker_monitoring_schedule_name": "schedule-name",
 "start_time": "2019-12-01T15: 20: 00Z"
}
```

Parameters

| Parameter Name                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `dataset_format`                          | For a job started from a<br>`MonitoringSchedule` backed by an<br>`Endpoint`, this is<br>`sageMakerCaptureJson` with the capture<br>indices `endpointInput`,or<br>`endpointOutput`, or both. For a batch<br>transform job, this specifies the data format, whether<br>CSV, JSON, or Parquet.                                                                                                                                         |
| `dataset_source`                          | If you are using a real-time endpoint, the local path<br>in which the data corresponding to the monitoring<br>period, as specified by `start_time` and<br>`end_time`, are available. At this path,<br>the data is available in`/{endpoint-name}/{variant-name}/yyyy/mm/dd/hh`.<br>We sometimes download more than what is specified by<br>the start and end times. It is up to the container code<br>to parse the data as required. |
| `output_path`                             | The local path to write output reports and other<br>files. You specify this parameter in the<br>`CreateMonitoringSchedule` request as<br>`MonitoringOutputConfig.MonitoringOutput[0].LocalPath`.<br>It is uploaded to the `S3Uri` path specified<br>in<br>`MonitoringOutputConfig.MonitoringOutput[0].S3Uri`.                                                                                                                       |
| `publish_cloudwatch_metrics`              | For a job launched by<br>`CreateMonitoringSchedule`, this<br>parameter is set to `Enabled`. The container<br>can choose to write the Amazon CloudWatch output file at<br>`[filepath]`.                                                                                                                                                                                                                                              |
| `sagemaker_endpoint_name`                 | If you are using a real-time endpoint, the name of the<br>`Endpoint` that this scheduled job was<br>launched for.                                                                                                                                                                                                                                                                                                                   |
| `sagemaker_monitoring_schedule_name`      | The name of the `MonitoringSchedule` that<br>launched this job.                                                                                                                                                                                                                                                                                                                                                                     |
| `*sagemaker_endpoint_datacapture_prefix*` | If you are using a real-time endpoint, the prefix<br>specified in the `DataCaptureConfig`<br>parameter of the `Endpoint`. The container<br>can use this if it needs to directly access more data<br>than already downloaded by SageMaker AI at the<br>`dataset_source` path.                                                                                                                                                        |
| `start_time, end_time`                    | The time window for this analysis run. For example,<br>for a job scheduled to run at 05:00 UTC and a job that<br>runs on 20/02/2020, `start_time`: is<br>2020-02-19T06:00:00Z and `end_time`: is<br>2020-02-20T05:00:00Z                                                                                                                                                                                                            |
| `baseline_constraints:`                   | The local path of the baseline constraint file<br>specified in`BaselineConfig.ConstraintResource.S3Uri`. This<br>is available only if this parameter was specified in the<br>`CreateMonitoringSchedule`<br>request.                                                                                                                                                                                                                 |
| `baseline_statistics`                     | The local path to the baseline statistics file<br>specified in<br>`BaselineConfig.StatisticsResource.S3Uri`.<br>This is available only if this parameter was specified<br>in the `CreateMonitoringSchedule` request.:                                                                                                                                                                                                               |
