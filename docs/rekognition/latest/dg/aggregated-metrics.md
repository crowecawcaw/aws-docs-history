# Exercise 4: See aggregated metrics

(console)

The Amazon Rekognition metrics pane shows activity graphs for an aggregate of individual Rekognition
metrics over a specified period of time. For example, the
`SuccessfulRequestCount` aggregated metric shows the total number of
successful requests to all Rekognition API operations over the last seven days.

The following table lists the graphs displayed in the Rekognition metrics pane and the
corresponding Rekognition metric. For more information, see [CloudWatch
metrics for Rekognition](rekognition-monitoring.md#cloudwatch-metricsdim "rekognition-monitoring.md#cloudwatch-metricsdim").

| Graph            | Aggregated Metric      |
| ---------------- | ---------------------- |
| Successful calls | SuccessfulRequestCount |
| Client errors    | UserErrorCount         |
| Server errors    | ServerErrorCount       |
| Throttled        | ThrottledCount         |
| Detected labels  | DetectedLabelCount     |
| Detected faces   | DetectedFaceCount      |

Each graph shows aggregated metric data collected over a specified period of
time. A total count of aggregated metric data for the time period is
also displayed. To see metrics for individual API calls, choose the link beneath each
graph.

To allow users access to the Rekognition metrics pane, ensure that the user has appropriate CloudWatch
and Rekognition permissions. For example, a user with
`AmazonRekognitionReadOnlyAccess` and
`CloudWatchReadOnlyAccess` managed policy permissions can see the metrics
pane. If a user does not have the required permissions, when the user opens the metrics
pane, no graphs appear. For more
information, see [Identity and access management for Amazon Rekognition](security-iam.md "security-iam.md").

For more information about monitoring Rekognition with CloudWatch see
[Monitoring Rekognition with Amazon CloudWatch](rekognition-monitoring.md "rekognition-monitoring.md").

###### To see aggregated metrics (console)

1. Open the Amazon Rekognition console at
   [https://console.aws.amazon.com/rekognition/](https://console.aws.amazon.com/rekognition/ "https://console.aws.amazon.com/rekognition/").
2. In the navigation pane, choose **Metrics**.
3. In the dropdown, select the period of time you want metrics for.
4. To update the graphs, choose the **Refresh** button.
5. To see detailed CloudWatch metrics for a specific aggregated metric, choose **See details on
   CloudWatch** beneath the metric graph.
