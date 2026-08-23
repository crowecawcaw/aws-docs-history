# Viewing instance and session metrics using the console

You can monitor Amazon WorkSpaces Applications fleet instance and session metrics using the
WorkSpaces Applications console or the CloudWatch console.

These metrics are collected at a 5-minute interval. After a new session is
provisioned, the first metric data point appears within 5 minutes. Subsequent metric
data points are available at every 5-minute interval.

###### To view instance and session in the WorkSpaces Applications console

1. Open the WorkSpaces Applications console at
   [https://console.aws.amazon.com/appstream2/home](https://console.aws.amazon.com/appstream2/home "https://console.aws.amazon.com/appstream2/home").
2. In the left pane, choose **Fleets**.
3. Select a fleet and choose **View Details**.
4. View fleet utilization information under **Sessions on
   fleet**.
5. View the list of all active sessions under **Instances with
   sessions**.
6. Select a session to view the metrics.
7. You can sort and filter the table to find specific user
   sessions.

###### To view instance and session metrics in the CloudWatch console

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the left pane, choose **Metrics**.
3. Choose the **AppStream** namespace and then choose
   **Fleet Instance Metrics** or **Fleet Session
   Metrics**.
4. Select the metrics to graph.
