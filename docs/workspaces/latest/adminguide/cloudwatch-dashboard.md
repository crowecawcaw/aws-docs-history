# Monitor your WorkSpaces health using the CloudWatch

automatic dashboard

You can monitor WorkSpaces using CloudWatch automatic dashboard, which collects raw data
and processes it into readable, near real-time metrics. The metrics are kept for 15
months to access historical information and to monitor the performance of your web
application or service. You can also set alarms that watch for certain thresholds, and
send notifications or take actions when those thresholds are met. For more information,
see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").

The CloudWatch dashboard is automatically created when you use your AWS account to
configure your WorkSpaces. The dashboard allows you to monitor your WorkSpaces metrics, such as
their health and performance, across Regions. You can also use the dashboard for the
following purposes:

- Identify unhealthy WorkSpace instances.
- Identify running modes, protocols, and operating systems that have unhealthy
  WorkSpace instances.
- View critical resource utilization over time.
- Identify anomalies to help with troubleshooting.
  WorkSpaces CloudWatch automatic dashboards are available in all AWS commercial Regions.

###### To use the WorkSpaces CloudWatch automatic dashboard

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Dashboards**.
3. Choose the **Automatic dashboards** tab.
4. Choose **WorkSpaces**.

## Understanding your WorkSpaces CloudWatch

automatic dashboard

The CloudWatch automatic dashboard allows you to gain insight into the performance of
your WorkSpaces resources and helps you identify performance issues.

![WorkSpaces client sign in screen](images/cw_dashboard_withcallouts.png)

###### The dashboard consists of the following features:

1. View historical data using time and date range controls.
2. Add customized dashboard view to the CloudWatch custom dashboards.
3. Monitor the overall health and utilization status of your WorkSpaces by doing
   the following:
   1. View the total number of provisioned WorkSpaces, number of users
      connected, number of unhealthy and healthy WorkSpace
      instances.
   2. View unhealthy WorkSpaces and their different variables, such as
      protocol and compute mode.
   3. Hover over the line chart to view the number of healthy or
      unhealthy WorkSpace instances for a specific protocol and running
      mode over a period of time.
   4. Choose the ellipsis menu, then choose **View in
      metrics** to view the metrics on a time scale
      chart.

4. View your connection metrics and their different variables, such as number
   of connection attempts, successful connections, and failed connections in
   your WorkSpaces environment at any given time.
5. View InSession latencies that impact your user's experience, such as round
   trip time (RTT), to determine connection health and packet loss to monitor
   network health.
6. View host performance and resource utilization to identify and
   troubleshoot potential performance issues.
