# Use a monitor in Internet Monitor

There are several ways to use an Internet Monitor monitor after you create it: for example, you can view information in the CloudWatch dashboard,
get information by using the AWS Command Line Interface, and set health alerts.

Your monitor provides information about your application and configuration preferences so that Internet Monitor can
customize measurements and metrics to publish in events for you. Internet Monitor collects measurements from the global infrastructure footprint
for AWS. These measurements are a tremendous amount of network performance and availability information, from all
over the world. By using information from the resources that you add for your application, Internet Monitor publishes performance
and availability measurements for you that is scoped to the city-networks (that is, client locations and ASNs, typically internet
service providers or ISPs) where your application is active. So, the measurements and metrics in the Internet Monitor dashboard and in CloudWatch Logs
—about availability, performance, monitored bytes transferred, and round-trip time—are specific to your client
locations and ASNs.

Internet Monitor also determines when there are anomalies in performance and availability. By default, Internet Monitor overlays your traffic with the
availability and performance measurements that AWS has collected for each source-destination pair in your client locations, to determine
when there are notable drops in performance or availability. When there's significant degradation for your application's locations
and scope, Internet Monitor generates a _health event_, and publishes information about the issue to your monitor.

After you create a monitor, you can use it to access or be alerted to the information that Internet Monitor provides,
in the following ways:

- **Use the CloudWatch dashboard** to view and explore performance, availability, and health events;
  explore your application's historical data; and get insights into new ways to configure your application for better performance.
  To learn more, see the following:
  - [Track real-time performance and availability in Internet Monitor (Overview page)](CloudWatch-IM-overview.md "CloudWatch-IM-overview.md")
  - [Analyze historical data in Internet Monitor (Analyze page)](CloudWatch-IM-historical-explorer.md "CloudWatch-IM-historical-explorer.md")
  - [Get suggestions to optimize application performance in Internet Monitor (Optimize page)](CloudWatch-IM-insights.md "CloudWatch-IM-insights.md")

- **Configure health event thresholds** to change what triggers Internet Monitor to create a health
  event for your application. You can configure overall thresholds and local (city-network) thresholds. To learn more,
  see [Change health event thresholds](CloudWatch-IM-get-started.md#IMUpdateThresholdFromOverview "CloudWatch-IM-get-started.md#IMUpdateThresholdFromOverview").
- **Use AWS CLI commands** with Internet Monitor API actions to view traffic
  profile information, view measurements, list health events, and so on. To learn more, see [Examples of using the CLI with Internet Monitor](CloudWatch-IM-get-started-CLI.md "CloudWatch-IM-get-started-CLI.md").
- **Use standard CloudWatch tools,** such as CloudWatch Contributor Insights, CloudWatch Metrics explorer, and
  CloudWatch Logs Insights to visualize the data in CloudWatch. To learn more, see [Exploring your data with CloudWatch tools and the Internet Monitor query interface](CloudWatch-IM-view-cw-tools.md "CloudWatch-IM-view-cw-tools.md").
- **Use Athena with S3 logs** to access and analyze Internet Monitor internet measurements for your application,
  if you turned on publishing measurements to S3.
- **Create Amazon EventBridge notifications** to alert you when Internet Monitor determines there is a health event. To learn
  more, see [Using Internet Monitor with Amazon EventBridge](CloudWatch-IM-EventBridge-integration.md "CloudWatch-IM-EventBridge-integration.md").
- **Receive an AWS Health Dashboard notification** automatically, when Internet Monitor determines that an issue is caused by the AWS
  network. The notification includes the steps that AWS is taking to mitigate the problem.
