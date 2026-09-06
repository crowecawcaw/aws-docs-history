

# What is Internet Monitor?
<a name="CloudWatch-InternetMonitor.what-is-cwim"></a>

With Internet Monitor, you can monitor your application's internet performance and availability, so that you can visualize data and get insights and suggestions about your AWS application's internet traffic. You can also get suggestions for ways to reduce latency for your application, by using different Regions or AWS services, like Amazon CloudFront.

**Key features of Internet Monitor**
+ Internet Monitor suggests insights and recommendations that can help you improve your end users' experience. You can explore, in near real-time, how to improve the projected latency of your application by switching to use other services, or by rerouting traffic to your workload through different AWS Regions.
+ Internet Monitor stores internet measurements for pairs of your client locations and ASNs, or *city-networks*. Internet Monitor also creates aggregated CloudWatch metrics for traffic to your application, and to each AWS Region and edge location. With the Internet Monitor dashboard, you can quickly identify what's impacting your application's performance and availability, so that you can track down and address issues.
+ Internet Monitor also publishes internet measurements to CloudWatch Logs and CloudWatch Metrics, to support using CloudWatch tools to explore data for city-networks that are specific to your monitored application traffic. Optionally, you can also publish internet measurements to Amazon S3.
+ Internet Monitor sends health events to Amazon EventBridge so that you can set up notifications. Both overall (global) health events and local health events are published to EventBridge. If an issue is caused by the AWS network, you also automatically receive an AWS Health Dashboard notification with the steps that AWS is taking to mitigate the problem.

**How to use Internet Monitor**

To use Internet Monitor, you create a *monitor* and associate your application's resources with it—VPCs, Network Load Balancers, CloudFront distributions, or WorkSpaces directories—to enable Internet Monitor to know where your application's internet-facing traffic is. Internet Monitor then publishes internet measurements from AWS that are specific to the *city-networks*, that is, the client locations and ASNs (typically internet service providers or ISPs), where clients access your application. For more information, see [How Internet Monitor works](CloudWatch-IM-inside-internet-monitor.md). To begin working with Internet Monitor, see [Getting started with Internet Monitor using the console](CloudWatch-IM-get-started.md).

**Topics**
+ [Supported Regions](CloudWatch-InternetMonitor.Regions.md)
+ [Components](CloudWatch-IM-components.md)
+ [How it works](CloudWatch-IM-inside-internet-monitor.md)
+ [Use cases](CloudWatch-IM-use-cases.md)
+ [Internet weather map](CloudWatch-InternetMonitor.outage-map.md)
+ [Cross-account observability](cwim-cross-account.md)
+ [Pricing](CloudWatch-InternetMonitor.pricing.md)