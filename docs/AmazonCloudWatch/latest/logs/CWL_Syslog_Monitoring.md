# Monitoring syslog ingestion

The syslog ingestion service publishes metrics to CloudWatch in the `AWS/Logs`
namespace. These metrics give you visibility into your syslog ingestion pipeline –
what was received, what was dropped, and why.

To view these metrics in the CloudWatch console, navigate to
**Metrics** > **All metrics** >
**AWS/Logs** and filter by the metric names listed below.

## Syslog metrics

| Metric                         | Dimensions               | Description                                                                                                                                                         |
| ------------------------------ | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `SyslogMessagesReceived`       | `LogGroupName`           | The number of syslog messages successfully ingested into your log group.                                                                                            |
| `SyslogMessagesDropped`        | `LogGroupName`, `Reason` | The number of syslog messages that could not be delivered. See [Drop reasons](#CWL_Syslog_Monitoring_DropReasons "#CWL_Syslog_Monitoring_DropReasons") for details. |
| `SyslogConnectionsRejected`    | `Reason`                 | The number of TCP connections that were rejected.                                                                                                                   |
| `SyslogConnectionsEstablished` | —                        | The number of TCP connections successfully accepted.                                                                                                                |
| `SyslogConnectionsClosed`      | —                        | The number of TCP connections closed.                                                                                                                               |

## Drop reasons

The `SyslogMessagesDropped` metric includes a `Reason`
dimension that indicates why messages were dropped.

| Reason                     | Description                                                                                                                   |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `MessageRateLimitExceeded` | Your account's `PutLogEvents` quota was exceeded. Consider requesting a quota increase.                                       |
| `MessageSizeExceeded`      | A UDP datagram exceeded the maximum message size.                                                                             |
| `ServiceUnavailable`       | Internal capacity or rate limit exceeded. This is typically transient.                                                        |
| `ResourceNotFound`         | The target log group does not exist. Verify that the log group has not been deleted.                                          |
| `AccessDenied`             | The resource policy on the log group does not grant access to the syslog service. Verify that the resource policy is correct. |
| `VpcePolicyDenied`         | The VPC endpoint policy denied the request. Review your VPC endpoint policy.                                                  |
| `InternalError`            | An unexpected internal error occurred. If this persists, contact AWS Support.                                                 |

## Connection rejection reasons

The `SyslogConnectionsRejected` metric includes a `Reason`
dimension.

| Reason               | Description                                    |
| -------------------- | ---------------------------------------------- |
| `VpcePolicyDenied`   | The VPC endpoint policy denied the connection. |
| `ServiceUnavailable` | Connection dropped due to an internal error.   |

## Recommended alarms

We recommend creating CloudWatch alarms on the following conditions to detect issues
early:

| Alarm                  | Condition                                                       | Suggested action                                                                                   |
| ---------------------- | --------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| Messages being dropped | `SyslogMessagesDropped` > 0 for 5 minutes                       | Investigate the `Reason` dimension to determine the cause.                                         |
| Access denied          | `SyslogMessagesDropped` with `Reason=AccessDenied`              | Verify that the resource policy on the log group is correctly configured.                          |
| Log group missing      | `SyslogMessagesDropped` with `Reason=ResourceNotFound`          | Verify that the log group exists and has not been deleted.                                         |
| No messages received   | `SyslogMessagesReceived` = 0 for 15 minutes (when normally > 0) | Verify that devices are still sending and that network connectivity to the VPC endpoint is intact. |

For information about creating CloudWatch alarms, see [Creating CloudWatch alarms](../monitoring/AlarmThatSendsEmail.md "../monitoring/AlarmThatSendsEmail.md")
in the _CloudWatch User Guide_.

## Viewing syslog metrics on the automatic dashboard

CloudWatch provides an automatic dashboard for CloudWatch Logs that includes a
**Syslog Ingestion** section. This dashboard appears
automatically when your account publishes syslog metrics – no manual setup is
required. The dashboard includes one chart for each metric described in
[Syslog metrics](#CWL_Syslog_Monitoring_Metrics "#CWL_Syslog_Monitoring_Metrics"). Each chart displays the metric
rate broken down by the relevant dimensions, such as log group or reason.

### Accessing the dashboard

To view the syslog automatic dashboard:

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Dashboards**,
   then choose **Automatic dashboards**.
3. Choose the **CloudWatch Logs** dashboard.
4. Scroll to the **Syslog Ingestion**
   section.
