# Add

a monitor with a Network Load Balancer

When you create a Network Load Balancer in the AWS Management Console, you can optionally choose to also set up monitoring for traffic to
and from the Network Load Balancer using a monitor in Internet Monitor. You can add the Network Load Balancer to an existing monitor, or you can opt to
create a new monitor for your Network Load Balancer traffic.

By using Internet Monitor with your Network Load Balancer, you can view and evaluate measurements and metrics about availability, performance, monitored
bytes transferred, and round-trip times that are specific to your application's client locations and ASNs (typically, internet
service providers). Internet Monitor also determines when there are anomalies in performance and availability, and then creates health events in
your monitor, which you can choose to be notified about. To learn more about how you can use a monitor to manage and improve your clients'
experience with your application, see [Use a monitor in Internet Monitor](IMWhyCreateMonitor.md "IMWhyCreateMonitor.md").

###### Important

To create a monitor, or add a Network Load Balancer to an existing monitor, you must have the correct permissions in place.
For more information, see [Identity and Access Management for Internet Monitor](security-iam.md "security-iam.md").

##

Add a Network Load Balancer to an existing monitor

When you create the Network Load Balancer in the AWS Management Console, you can choose to have Internet Monitor add the new Network Load Balancer to an existing monitor.
Under **Integrations**, choose Internet Monitor, and then choose **Add monitor**.
Choose **Select an existing monitor**, and then enter a monitor name. Or choose **View
monitors** to go to the Internet Monitor console, and then scroll down to see a list of available monitors.

After you add the Network Load Balancer to a monitor, wait a few minutes, and then metrics for traffic to and from the load
balancer will start being shown on the Internet Monitor console. To learn more about the **Status**
and **Data processing status** values, see
[Monitoring details in Internet Monitor (Configure page)](CloudWatch-IM-configure.md "CloudWatch-IM-configure.md").

You can edit the monitor at any time, to remove the load balancer or add another Network Load Balancer, or other resources.
You can also change the percentage of traffic that you're monitoring, or make other changes.
If you choose to remove the Network Load Balancer from the monitor, traffic from clients to that load balancer is no longer monitored by Internet Monitor.

To learn more about updating a monitor, see
[Edit a monitor in Internet Monitor](CloudWatch-IM-get-started.md "CloudWatch-IM-get-started.md").

##

Create a monitor for a Network Load Balancer

Under **Integrations**, choose Internet Monitor, and then choose **Monitor resource traffic**.
Choose **Create a new monitor**, and then enter a monitor name. Leave the default traffic
percentage to monitor, 100%, or specify a custom percentage, and then choose **Create monitor**.

After you create the monitor, wait a few minutes, and then metrics for traffic to and from the Network Load Balancer will start being shown on
the Internet Monitor console. If you like, you can also choose a
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

Stop monitoring a Network Load Balancer

If you'd like to stop monitoring your Network Load Balancer resource with Internet Monitor, do the following in the Internet Monitor console:

###### To remove a resource from a monitor

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the left navigation pane, under **Network Monitoring**, choose **Internet monitors**.
3. Choose your monitor, and then choose the **Action** menu.
4. Choose **Update monitor**.
5. Under **Added resources**, choose **Remove resources**.
6. Choose the Network Load Balancer to remove, and then choose **Remove**.
7. Choose **Update**.
