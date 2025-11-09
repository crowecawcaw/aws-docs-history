# Monitor Amazon GameLift Streams with Amazon CloudWatch

You can monitor Amazon GameLift Streams using CloudWatch, which collects raw data and processes it into readable, near real-time metrics. These statistics are
kept for 15 months, so that you can access historical information and gain a better perspective on how your web application or service is
performing. You can also set alarms that watch for certain thresholds, and send notifications or take actions when those thresholds are
met. For more information, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").

Amazon GameLift Streams provides metrics to help customers monitor the following:

- Stream group capacity and usage.
- Stream performance and resource usage.
- Stream status to resolve issues and support users.
- Customer engagement across content offerings.
- Data channel usage.
  The following tables list the dimensions and metrics for Amazon GameLift Streams.

## Stream group capacity and usage

Use these metrics to help scale resources to meet demand. These metrics are published every minute.

###### Important

**For stream groups created before September 5, 2025**

Due to an issue with CloudWatch's data retention policy, accurate capacity metrics are only available for the last 15 days. For
capacity metrics that are older than 15 days, no data will be visible when the period is 1 minute, and the data shown will be
inaccurate when the period is 5 minutes or more.

As a workaround, you can add `SUM(METRICS())/`5`` math (for example, when using a 5-minute
period) to a sum-type statistic in your CloudWatch graph as a workaround to see accurate capacity counts beyond the 15 day, 1-minute
metrics retention limitation.

To pick up the fix for this issue, recreate your stream groups.

| Metric             | Description                                                                                                                                                                                              | Dimension                 | Unit  |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- | ----- |
| **ActiveCapacity** | The number of compute resources that are provisioned and ready to stream. It includes resources that are<br>currently streaming and resources that are idle and ready to respond to new stream requests. | (StreamGroupId, Location) | Count |
| **IdleCapacity**   | The numerical portion of active capacity that is not currently streaming. It represents the availability of<br>compute resources to respond to new stream requests.                                      | (StreamGroupId, Location) | Count |

## Stream group performance and resource utilization

These metrics are published every minute.

| Metric                | Description                                                    | Dimension                                               | Unit       |
| --------------------- | -------------------------------------------------------------- | ------------------------------------------------------- | ---------- |
| **MemoryUtilization** | % of available memory used by the stream.                      | (StreamGroupId, Location), (ApplicationId, StreamClass) | Percentage |
| **CPUUtilization**    | % of available CPU used by the stream.                         | (StreamGroupId, Location), (ApplicationId, StreamClass) | Percentage |
| **FrameCaptureRate**  | Rate at which frames are captured from the application.        | (StreamGroupId, Location), (ApplicationId, StreamClass) | None       |
| **AudioCaptureRate**  | Rate at which audio samples are captured from the application. | (StreamGroupId, Location), (ApplicationId, StreamClass) | None       |
| RoundTripTime         | Round trip time between client and server.                     | (StreamGroupId, Location), (ApplicationId, StreamClass) | ms         |

## Stream status

These metrics are published at the end of a stream session.

| Metric                       | Description                                    | Dimension                                               | Unit  |
| ---------------------------- | ---------------------------------------------- | ------------------------------------------------------- | ----- |
| **TerminatedStreamSessions** | Number of sessions ended in state `TERMINATED` | (StreamGroupId, Location), (ApplicationId, StreamClass) | Count |
| **ErroredStreamSessions**    | Number of sessions ended in state `ERROR`      | (StreamGroupId, Location), (ApplicationId, StreamClass) | Count |

## Customer engagement

These metrics are published at the end of a stream session..

| Metric             | Description             | Dimension                                               | Unit    |
| ------------------ | ----------------------- | ------------------------------------------------------- | ------- |
| **Session Length** | Stream session duration | (StreamGroupId, Location), (ApplicationId, StreamClass) | Seconds |

## Data channels

These metrics are published at the end of a stream session.

| Metric                                  | Description                                                                                                         | Dimension                                               | Unit  |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- | ----- |
| **DataChannel-ApplicationConnected**    | Number of times your application connects to the data channel port. This number is at most 1 per stream<br>session. | (StreamGroupId, Location), (ApplicationId, StreamClass) | Count |
| **DataChannel-ApplicationMessage**      | Number of messages your application has sent to your client.                                                        | (StreamGroupId, Location), (ApplicationId, StreamClass) | Count |
| **DataChannel-ApplicationMessageBytes** | Total bytes of messages your application has sent to your client.                                                   | (StreamGroupId, Location), (ApplicationId, StreamClass) | Bytes |
| **DataChannel-ClientMessage**           | Number of messages your client has sent to your application.                                                        | (StreamGroupId, Location), (ApplicationId, StreamClass) | Count |
| **DataChannel-ClientMessageBytes**      | Total bytes of messages your client has sent to your application.                                                   | (StreamGroupId, Location), (ApplicationId, StreamClass) | Bytes |
