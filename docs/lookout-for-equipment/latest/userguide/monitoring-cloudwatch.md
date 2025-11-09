On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# Monitoring `Service Name` with Amazon CloudWatch

You can monitor `Amazon Lookout for Equipment` using CloudWatch, which collects raw data and processes it
into readable, near real-time metrics. These statistics are kept for 15 months, so that you can access historical
information and gain a better perspective on how your web application or service is performing. You can also set
alarms that watch for certain thresholds, and send notifications or take actions when those thresholds are met. For
more information, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").

The `Amazon Lookout for Equipment` service reports the following metrics
in the `AWS/lookoutequipment` namespace.

| Metric                  | Description                                                                                                                                                                              |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `InferenceSucceeded`    | If the value is `1`, the inference succeeded. If the value is `0`, the inference failed.<br>ModelName: The name of the model.<br>InferenceSchedulerName: Name of the inference scheduler |
| `InferenceFailed`       | If the value is `1`, the inference failed. If the value is `0`, the inference succeeded.<br>ModelName: The name of the model.<br>InferenceSchedulerName: Name of the inference scheduler |
| `InferenceInvalidInput` | If the value is `1`, you've provided an invalid value for the inference.<br>ModelName: The name of the model.<br>InferenceSchedulerName: Name of the inference scheduler                 |

The following dimensions are supported for the `Service Name` metrics.

| ModelName                | The name of the ML model that you've trained to monitor your equipment.              |
| ------------------------ | ------------------------------------------------------------------------------------ |
| `InferenceSchedulerName` | The inference scheduler schedules the times when your model monitors your equipment. |
