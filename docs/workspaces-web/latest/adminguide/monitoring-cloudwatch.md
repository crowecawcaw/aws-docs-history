# Monitoring Amazon WorkSpaces Secure Browser with Amazon CloudWatch

You can monitor Amazon WorkSpaces Secure Browser using CloudWatch, which collects raw data and processes it
into readable, near real-time metrics. These statistics are kept for 15 months, so that you can access historical
information and gain a better perspective on how your web application or service is performing. You can also set
alarms that watch for certain thresholds, and send notifications or take actions when those thresholds are met. For
more information, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").

The `AWS/WorkSpacesWeb` namespace includes the following metrics.

| CloudWatch metrics for Amazon WorkSpaces Secure Browser | Metric                                                                                                                          | Description                               | Dimensions                        | Statistics  | Units |
| ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------- | --------------------------------- | ----------- | ----- |
| `SessionAttempt`                                        | The number of Amazon WorkSpaces Secure Browser session attempts.                                                                | `[PortalId]`                              | Average, Sum, Maximum, Minimum    | Count       |
| `SessionSuccess`                                        | The number of successful Amazon WorkSpaces Secure Browser session starts.                                                       | `[PortalId]`                              | Average, Sum, Maximum, Minimum    | Count       |
| `SessionFailure`                                        | The number of failed Amazon WorkSpaces Secure Browser session starts.                                                           | `[PortalId]`                              | Average, Sum, Maximum, Minimum    | Count       |
| `SessionIdleDisconnect`                                 | The number of connections that were closed due to user inactivity.                                                              | `[PortalId]`                              | Average                           | Count       |
| `ActiveSession`                                         | The number of active sessions on a portal.                                                                                      | `[PortalId]`                              | Average                           | Count       |
| `GlobalCpuPercent`                                      | The CPU usage of the Amazon WorkSpaces Secure Browser session<br>instance.                                                      | `[PortalId]`<br>`[PortalId,<br>UserName]` | Average, Sum, Maximum,<br>Minimum | Percent     |
| `GlobalMemoryPercent`                                   | The memory (RAM) usage of the Amazon WorkSpaces Secure Browser session<br>instance.                                             | `[PortalId]`<br>`[PortalId,<br>UserName]` | Average, Sum, Maximum,<br>Minimum | Percent     |
| `DisplayLatency`                                        | The average time in milliseconds between frame capture and presentation.                                                        | `[PortalId]`<br>`[PortalId, UserName]`    | Average, Maximum, Minimum         | Miliseconds |
| `InputLatency`                                          | The input latency between client and server. For example, the latency between the<br>client mouse click and server mouse click. | `[PortalId]`<br>`[PortalId, UserName]`    | Average, Maximum, Minimum         | Miliseconds |
| `SessionLoggerEventDelivered`                           | The number of events each delivered Session Logger file has.                                                                    | `[PortalId]`                              | Average, Sum, Maximum, Minimum    | Count       |
| `SessionLoggerTargetNotFoundError`                      | The number of log file deliveries that resulted in bucket not found.                                                            | `[PortalId]`                              | Average, Sum, Maximum, Minimum    | Count       |
| `SessionLoggerAccessDeniedError`                        | The number of log file deliveries that resulted in permissions denied.                                                          | `[PortalId]`                              | Average, Sum, Maximum, Minimum    | Count       |

###### Note

The metric data points are collected by each session once per minute and published to
CloudWatch once every 5 minutes. Session Logger metrics are emitted immediately, for each Log File
delivery.

| Dimensions for Amazon WorkSpaces Secure Browser metrics | Dimension                                                                                     | Description |
| ------------------------------------------------------- | --------------------------------------------------------------------------------------------- | ----------- |
| PortalId                                                | Filters the metric data for Amazon WorkSpaces Secure Browser for a specified portal.          |
| UserName                                                | Filters the metric data for Amazon WorkSpaces Secure Browser for a specified portal and user. |

You can use the **SessionLoggerEventDelivered** metric to monitor the
aggregate number of events from your portal, or see the number of log files that were
delivered by counting the number of data points rather than summing values. We recommend
configuring alarms on the **SessionLoggerTargetNotFoundError** and
SessionLoggerAccessDeniedError metrics to detect accidental resource or
permissions deletion.
