# Viewing Instance and Session Performance

Metrics Using the Console

You can monitor Amazon WorkSpaces Applications fleet instances and session performance using the WorkSpaces Applications
console or the CloudWatch console.

Performance metrics are collected at a 5-minute interval. After a new session is
provisioned, the first metric data point will show up in 5 minutes. Subsequent metric
data points will be available at every 5-minute interval.

###### Note

Performance metrics are currently available only for multi-session fleets

###### To view instance and session in the WorkSpaces Applications console

1. Open the WorkSpaces Applications console at
   [https://console.aws.amazon.com/appstream2](https://console.aws.amazon.com/appstream2 "https://console.aws.amazon.com/appstream2").
2. In the left pane, choose **Fleets**.
3. Select a fleet and choose **View Details** and **View
   Sessions**.
4. Select a session to view the metrics.
5. By default, the graph displays the following metrics:
   - Instance metrics
     - CpuUtilizationInstance
     - MemoryUtilizationInstance
     - PagingFileUtilizationInstance
     - DiskUtilizationInstance

   - Session metrics
     - CpuUtilizationSession
     - MemoryUtilizationSession

###### To view instance and session performance in the CloudWatch console

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the left pane, choose **Metrics**.
3. Choose the **AppStream** namespace and then choose
   **Fleet Instance Metrics** or **Fleet Session
   Metrics**.
4. Select the metrics to graph.
