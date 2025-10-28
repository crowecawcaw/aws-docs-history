# Monitor and optimize with the Internet Monitor dashboard

Using the Internet Monitor dashboard in the AWS Management Console, you can visualize data and get insights and suggestions about your AWS
application's internet traffic, and configure options for your monitor.

After you create a monitor to monitor your application's internet performance and availability,
Internet Monitor stores internet measurements for pairs of your client locations and ASNs, or _city-networks_.
Internet Monitor also creates aggregated CloudWatch metrics for traffic to your application, and to each AWS Region and edge location.
You can filter, explore, and get action-oriented suggestions from your monitor's information in several different ways.
The Internet Monitor dashboard guides you through viewing and getting insights about the data for your monitored traffic.

To get started, on the CloudWatch console, under **Network Monitoring**, choose **Internet monitors**.
Then, select a monitor to work with.

###### Note

This section primarily describes how to filter and view Internet Monitor metrics using the AWS Management Console. Alternatively, you can
use Internet Monitor API operations with the AWS CLI or an SDK to work directly with Internet Monitor events stored in CloudWatch Logs files. For more information,
see [Using your monitor and measurements information](IMWhyCreateMonitor.md#IMAccessIMInformation "IMWhyCreateMonitor.md#IMAccessIMInformation"). For more information
about using API operations, see [Examples of using the CLI with Internet Monitor](CloudWatch-IM-get-started-CLI.md "CloudWatch-IM-get-started-CLI.md")
and the [Internet Monitor API Reference](../../../internet-monitor/latest/api/Welcome.md "../../../internet-monitor/latest/api/Welcome.md").

There are five pages (tabs) in the Internet Monitor dashboard:

- On the **Overview** page, you can get an overall view of your monitored traffic, including
  current performance and availability information, a summary of recent and current health events, and the top
  suggestion for potentially improving performance for your clients.
- On the **Health events** page, you can see current and historical health events that currently
  impact, or previously impacted, locations where clients access your application.
- On the **Analyze** page, you can view information about top monitored traffic in client
  locations (by traffic volume), summarized in several customizable ways. You can also see historical trends for health scores
  and metrics. You can filter by location, ASN, date, and so on, and visualize metrics for your internet traffic over time.
- On the **Optimize** page, Internet Monitor predicts your application's performance improvement for top
  AWS Regions (or Amazon CloudFront), based on your traffic patterns and past performance. For each top configuration, associated
  tables provide a breakdown of reduced latency by client location. On a second page, you can select multiple Regions (and,
  if you like, include CloudFront configurations) to compare latency reductions. For each configuration (Region) that you selected,
  the page displays an associated table of latency details, listed by city location.
- On the **Configure** page, you can see monitor details and configure options, such as the percentage
  of traffic to monitor.
  In addition to these dashboard options, you can use tools for deeper dives into details of the metrics that Internet Monitor
  collects with your monitor. Internet Monitor generates and publishes log files with the measurements about your traffic, so you can
  use other CloudWatch tools in the console to further visualize the data published by Internet Monitor, including CloudWatch Contributor Insights, CloudWatch
  Metrics, and CloudWatch Logs Insights. For more information, see [Exploring your data with CloudWatch tools and the Internet Monitor query interface](CloudWatch-IM-view-cw-tools.md "CloudWatch-IM-view-cw-tools.md").

Learn about using Internet Monitor to explore your performance and availability measurements in the following sections.

###### Topics

- [Track real-time performance and availability in Internet Monitor (Overview page)](CloudWatch-IM-overview.md "CloudWatch-IM-overview.md")
- [View health events and metrics in Internet Monitor (Health events page)](CloudWatch-IM-Health-events.md "CloudWatch-IM-Health-events.md")
- [Analyze historical data in Internet Monitor (Analyze page)](CloudWatch-IM-historical-explorer.md "CloudWatch-IM-historical-explorer.md")
- [Get suggestions to optimize application performance in Internet Monitor (Optimize page)](CloudWatch-IM-insights.md "CloudWatch-IM-insights.md")
- [Monitoring details in Internet Monitor (Configure page)](CloudWatch-IM-configure.md "CloudWatch-IM-configure.md")
