# Monitor an AWS Site-to-Site VPN connection

Monitoring is an important part of maintaining the reliability, availability, and
performance of your AWS Site-to-Site VPN connection. You should collect monitoring data from all of
the parts of your solution so that you can more easily debug a multi-point failure if
one occurs. Before you start monitoring your Site-to-Site VPN connection; however, you should create a
monitoring plan that includes answers to the following questions:

- What are your monitoring goals?
- What resources will you monitor?
- How often will you monitor these resources?
- What monitoring tools will you use?
- Who will perform the monitoring tasks?
- Who should be notified when something goes wrong?
  The next step is to establish a baseline for normal VPN
  performance in your environment, by measuring performance at various times and under
  different load conditions. As you monitor your VPN, store
  historical monitoring data so that you can compare it with current performance data,
  identify normal performance patterns and performance anomalies, and devise methods to
  address issues.

To establish a baseline, you should monitor the following items:

- The state of your VPN tunnels
- Data into the tunnel
- Data out of the tunnel

###### Topics

- [Monitoring tools](#monitoring-automated-manual "#monitoring-automated-manual")
- [Site-to-Site VPN logs](monitoring-logs.md "monitoring-logs.md")
- [Monitor Site-to-Site VPN tunnels using CloudWatch](monitoring-cloudwatch-vpn.md "monitoring-cloudwatch-vpn.md")
- [AWS Health and Site-to-Site VPN events](monitoring-vpn-health-events.md "monitoring-vpn-health-events.md")

## Monitoring tools

AWS provides various tools that you can use to monitor a Site-to-Site VPN connection. You
can configure some of these tools to do the monitoring for you, while some of the tools
require manual intervention. We recommend that you automate monitoring tasks as much as
possible.

### Automated monitoring tools

You can use the following automated monitoring tools to watch
a Site-to-Site VPN connection and report when something is wrong:

- **Amazon CloudWatch Alarms** — Watch a single metric over a
  time period that you specify, and perform one or more actions based on the
  value of the metric relative to a given threshold over a number of time
  periods. The action is a notification sent to an Amazon SNS topic. CloudWatch alarms do
  not invoke actions simply because they are in a particular state; the state
  must have changed and been maintained for a specified number of periods. For
  more information, see [Monitor AWS Site-to-Site VPN tunnels using Amazon CloudWatch](monitoring-cloudwatch-vpn.md "monitoring-cloudwatch-vpn.md").
- **AWS CloudTrail Log Monitoring** — Share log files between accounts,
  monitor CloudTrail log files in real time by sending them to CloudWatch Logs, write log
  processing applications in Java, and validate that your log files have not
  changed after delivery by CloudTrail. For more information, see [Log API calls using
  AWS CloudTrail](../../../AWSEC2/latest/UserGuide/monitor-with-cloudtrail.md "../../../AWSEC2/latest/UserGuide/monitor-with-cloudtrail.md") in the _Amazon EC2 API Reference_ and [Working with
  CloudTrail log files](../../../awscloudtrail/latest/userguide/cloudtrail-working-with-log-files.md "../../../awscloudtrail/latest/userguide/cloudtrail-working-with-log-files.md") in the
  _AWS CloudTrail User Guide_.
- **AWS Health events** — Receive
  alerts and notifications related to changes in the health of your Site-to-Site VPN
  tunnels, best practice configuration recommendations, or when approaching
  scaling limits. Use events on the [Personal Health Dashboard](../../../health/latest/ug/what-is-aws-health.md "../../../health/latest/ug/what-is-aws-health.md") to
  trigger automated failovers, reduce troubleshooting time, or optimize
  connections for high availability. For more information, see [AWS Health and AWS Site-to-Site VPN events](monitoring-vpn-health-events.md "monitoring-vpn-health-events.md").

### Manual monitoring tools

Another important part of monitoring a Site-to-Site VPN connection involves manually
monitoring those items that the CloudWatch alarms don't cover. The Amazon VPC and CloudWatch console
dashboards provide an at-a-glance view of the state of your AWS environment.

###### Note

In the Amazon VPC console, Site-to-Site VPN tunnel state parameters such as "Status" and "Last status change", may not reflect transient state changes or momentary tunnel flaps. It is recommended to use CloudWatch metrics and logs for granular tunnel state change updates.

- The Amazon VPC dashboard shows:
  - Service health by Region
  - Site-to-Site VPN connections
  - VPN tunnel status (In the navigation pane, choose **Site-to-Site VPN
    Connections**, select a Site-to-Site VPN connection, and then choose
    **Tunnel Details**)

- The CloudWatch home page shows:

      + Current alarms and status
      + Graphs of alarms and resources
      + Service health status

  In addition, you can use CloudWatch to do the following:

      + Create [customized dashboards](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md") to monitor the services you
       care about
      + Graph metric data to troubleshoot issues and discover
       trends
      + Search and browse all your AWS resource metrics
      + Create and edit alarms to be notified of problems
