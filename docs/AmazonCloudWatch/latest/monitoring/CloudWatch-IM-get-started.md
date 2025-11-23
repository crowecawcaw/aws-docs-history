# Add

an Internet Monitor monitor with CloudFront

On the metrics dashboard for a distribution in Amazon CloudFront console, you can set up additional monitoring
for a distribution in Internet Monitor. You can add the distribution to an existing monitor, or you can create a new monitor
for the distribution.

By using Internet Monitor with your CloudFront distribution, you can view and evaluate measurements and metrics about availability, performance,
monitored bytes transferred, and round-trip times that are specific to your application's client locations and ASNs (typically internet
service providers). Internet Monitor also determines when there are anomalies in performance and availability and creates health events in
your monitor, which you can choose to be notified about. To learn more about how you can use a monitor to manage and improve your clients'
experience with your application, see [Use a monitor in Internet Monitor](IMWhyCreateMonitor.md "IMWhyCreateMonitor.md").

###### Important

To create a monitor, or add a distribution to an existing monitor, you must have the correct permissions in place.
For more information, see [Identity and Access Management for Internet Monitor](security-iam.md "security-iam.md").

##

Add a distribution to an existing monitor

You can choose to have Internet Monitor add a distribution to an existing monitor directly from the CloudFront metrics
dashboard in the AWS Management Console. After you add the distribution, wait a few minutes, and then metrics for the
distribution will start being shown on the Internet Monitor console.

You can edit the monitor at any time, to remove the distribution or add another distribution or other resources.
You can also change the percentage of traffic that you're monitoring, or make other changes. If you choose to
remove the distribution from the monitor, traffic from clients to that distribution is no longer monitored by Internet Monitor.

To learn more about updating a monitor, see
[Edit a monitor in Internet Monitor](CloudWatch-IM-get-started.md "CloudWatch-IM-get-started.md").

##

Create a monitor for a distribution

If you opt to create a monitor for a distribution, the **Create monitor** wizard walks you through the steps.
You add the distribution as a monitored resource when you create the monitor. If you like, you can also choose a
percentage of client traffic that you want to monitor for your application (the default is 100%).

You can learn more by reviewing the information in
[Step 1: Create a monitor](CloudWatch-IM-get-started.md#CloudWatch-IM-get-started.create "CloudWatch-IM-get-started.md#CloudWatch-IM-get-started.create").

##

Pricing

With Internet Monitor, you pay only for what you use. Pricing for Internet Monitor has two components: a per monitored resource fee and a per
city-network fee. A city-network is the location that clients access your application resources from and the network (an ASN,
such as an internet service provider or ISP) that clients access the resources through.

For more information, including pricing examples, see
[Pricing for Internet Monitor](CloudWatch-InternetMonitor.md "CloudWatch-InternetMonitor.md").

##

Stop monitoring a distribution

If you'd like to stop monitoring your distribution resource with Internet Monitor, do the following in the Internet Monitor console:

###### To remove a resource from a monitor

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the left navigation pane, under **Network Monitoring**, choose **Internet monitors**.
3. Choose your monitor, and then choose the **Action** menu.
4. Choose **Update monitor**.
5. Under **Added resources**, choose **Remove resources**.
6. Choose the distribution to remove, and then choose **Remove**.
7. Choose **Update**.
