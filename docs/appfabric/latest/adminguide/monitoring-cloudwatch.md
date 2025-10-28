# Monitoring AWS AppFabric with Amazon CloudWatch

You can monitor AWS AppFabric using CloudWatch, which collects raw data and processes it into
readable, near real-time metrics. These statistics are kept for 15 months, so that you can
access historical information and gain a better perspective on how your web application or
service is performing. You can also set alarms that watch for certain thresholds, and send
notifications or take actions when those thresholds are met. For more information, see the
[Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").

The AppFabric service reports the following metrics in the `AWS/AppFabric`
namespace.

| Metric                             | Description                                                                                                                                                                                                                    |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------- |
| AppFabric App Authorization Status | The status of the app authorization (`1` for connected; `0` for any other).                                                                                                                                                    |
| AppFabric Data Delivery Latency    | The time taken (in seconds) by AppFabric to collect audit logs from the SaaS application and deliver them to the configured destination (Amazon S3 or Amazon Data Firehose).                                                   |
| Ingestion Destination Status       | The status of the ingestion destination (`1` for active; `0` for any other).                                                                                                                                                   |
| Overall Data Delay                 | The time difference (in seconds) between when the events happened on the SaaS application and when the corresponding audit logs were delivered to the configured destination (Amazon S3 or Amazon Data Firehose) by AppFabric. |
| Volume of Ingested Data            | The size of data that is delivered to Amazon Simple Storage Service (Amazon S3) or Amazon Data Firehose.                                                                                                                       | The following dimension is supported for AppFabric metrics. |
| Dimension                          | Description                                                                                                                                                                                                                    |
| ---                                | ---                                                                                                                                                                                                                            |
| Ingestion Destination Arn          | The Amazon Resource Name (ARN) of the ingestion destination.                                                                                                                                                                   |
