End of support notice: On October 31, 2025, AWS
will discontinue support for Amazon Lookout for Vision. After October 31, 2025, you will
no longer be able to access the Lookout for Vision console or Lookout for Vision resources.
For more information, visit this [blog post](https://aws.amazon.com/blogs/machine-learning/exploring-alternatives-and-seamlessly-migrating-data-from-amazon-lookout-for-vision "https://aws.amazon.com/blogs/machine-learning/exploring-alternatives-and-seamlessly-migrating-data-from-amazon-lookout-for-vision").

# Monitoring Lookout for Vision with Amazon CloudWatch

You can monitor Lookout for Vision using CloudWatch, which collects raw data and processes it
into readable, near real-time metrics. These statistics are kept for 15 months, so that you can access historical
information and gain a better perspective on how your web application or service is performing. You can also set
alarms that watch for certain thresholds, and send notifications or take actions when those thresholds are met. For
more information, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").

The Lookout for Vision service reports the following metrics
in the `AWS/LookoutVision` namespace.

| Metric                    | Description                                                                                                                                                                                                                    |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `DetectedAnomalyCount`    | The number of anomalies detected in a project<br>Valid Statistics: `Sum,Average`<br>Unit: Count                                                                                                                                |
| `ProcessedImageCount`     | The total number of images run through anomaly detection<br>Valid Statistics: `Sum,Average`<br>Unit: Count                                                                                                                     |
| `InvalidImageCount`       | The number of images that were invalid and could not return a result<br>Valid Statistics: `Sum,Average`<br>Unit: Count                                                                                                         |
| `SuccessfulRequestCount`  | The number of successful API calls<br>Valid Statistics: `Sum,Average`<br>Unit: Count                                                                                                                                           |
| `ErrorCount`              | The number of API errors<br>Valid Statistics: `Sum,Average`<br>Unit: Count                                                                                                                                                     |
| `ThrottledCount`          | The number of API errors that were due to throttling<br>Valid Statistics: `Sum,Average`<br>Unit: Count                                                                                                                         |
| `Time`                    | The time in milliseconds for Lookout for Vision to compute the anomaly detection<br>Valid Statistics: `Data Samples,Average`<br>Units: Milliseconds for `Average` statistics and Count for `Data Samples` statistics           |
| `MinInferenceUnits`       | The minimum number of inference units specified during the<br>`StartModel` request.<br>Valid statistics: `Average`<br>Unit: Count                                                                                              |
| `MaxInferenceUnits`       | The maximum number of inference units specified during the<br>`StartModel`request.<br>Valid statistics: `Average`<br>Unit: Count                                                                                               |
| `DesiredInferenceUnits`   | The number of inference units to which Lookout for Vision is scaling up or<br>down.<br>Valid statistics: `Average`<br>Unit: Count                                                                                              |
| `InServiceInferenceUnits` | The number of inference units that the model is using.<br>Valid statistics: `Average`<br>It is recommended that you use the Average statistic to obtain<br>the 1 minute average of how many instances are used.<br>Unit: Count |

The following dimensions are supported for the Lookout for Vision metrics.

| Dimension      | Description                                                                                           |
| -------------- | ----------------------------------------------------------------------------------------------------- |
| `ProjectName`  | You can split metrics by project to see which projects are having problems or need to be updated.     |
| `ModelVersion` | You can split metrics by model version to see which models are having problems or need to be updated. |
