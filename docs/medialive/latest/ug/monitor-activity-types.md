# Types of activity that can be monitored

The following table summarizes the type of MediaLive activity you can monitor, and the service
you can use. In the table, read down the first column to find the type of activity you want
to monitor, then read across to find the service to use.

| Activity                       | Specific<br>activity                                                                               | MediaLive console | An AWS SDK or API | CloudWatch events | CloudWatch metrics           | CloudWatch logs | CloudTrail events |
| ------------------------------ | -------------------------------------------------------------------------------------------------- | ----------------- | ----------------- | ----------------- | ---------------------------- | --------------- | ----------------- |
| State of channel               | Report state of a channel                                                                          | Yes               | Yes               | Yes               |                              | Yes             |                   |
| State of multiplex             | Report state of a multiplex                                                                        | Yes               | Yes               | Yes               |                              | Yes             |                   |
| Alerts                         | Generate alerts when a<br>channel<br>or multiplex is running                                       | Yes               | Yes               | Yes               | Yes (count of active alerts) | Yes             |                   |
| Alerts                         | Generate alerts about the state of the cluster, when deploying<br>AWS Elemental MediaLive Anywhere | Yes               | Yes               | Yes               | Yes (count of active alerts) | Yes             |                   |
| Metrics                        | Generate metrics                                                                                   |                   |                   |                   | Yes                          |                 |                   |
| Logs for channel and multiplex | Log activity when a channel or multiplex is running                                                |                   |                   |                   |                              | Yes             |                   |
| Logs for schedule              | Log active schedule actions                                                                        |                   |                   |                   |                              | Yes             |                   |
| Logs for API calls             | Log API calls, including those performed from the console                                          |                   |                   |                   |                              | Yes             | Yes               |

The following sections provide details about some of these types of activities.

###### Topics

- [States for channels and
  multiplexes](monitor-activity-types-channel.md "monitor-activity-types-channel.md")
- [Alerts that MediaLive
  generates](monitor-activity-alerts.md "monitor-activity-alerts.md")
- [Metrics that MediaLive generates](monitor-activity-types-metrics.md "monitor-activity-types-metrics.md")
- [Logs that MediaLive generates](monitor-activity-types-logs.md "monitor-activity-types-logs.md")
