# Using Network Flow Monitor

Network Flow Monitor gives you near real-time visibility into network performance for
traffic between compute resources (Amazon EC2 and Amazon Elastic Kubernetes Service), traffic to other AWS
services (Amazon S3 and Amazon DynamoDB), and traffic to the edge of another AWS Region.
Network Flow Monitor collects data from lightweight software agents that you install on
your instances. These agents gather performance statistics from TCP connections and send
this data to the Network Flow Monitor backend service, which calculates the top contributors
for each metric type.

Network Flow Monitor also determines if AWS is the cause of a detected network issue, and reports
that information for network flows that you choose to monitor details for.

You can view network performance information for network flows for resources in a single
account, or you can configure Network Flow Monitor with AWS Organizations to view performance information for multiple accounts
in an organization, by signing in with a management or delegated administrator account.

Network Flow Monitor is intended for network operators and application developers who want near real-time
insights into network performance. In the Network Flow Monitor console in CloudWatch, you can see performance
data for your resources' network traffic that has been aggregated from agents and grouped into
different categories. For example, you can see data for flows between Availability Zones or
between VPCs. Then, you can create monitors for specific flows that you want to see more details for
or track more closely over time.

Using a monitor, you can quickly visualize packet loss and latency of your network
connections over a time frame that you specify. For each monitor, Network Flow Monitor also generates
a network health indicator (NHI). The NHI value informs you whether there were AWS network
issues for the network flows tracked by your monitor during the time period that you're evaluating.
Using the NHI information, you can quickly decide whether to focus troubleshooting efforts on an AWS network
issue or network problems originating with your workloads.

To see an example of configuring and using Network Flow Monitor, see the following blog post:
[Visualizing network performance of your AWS Cloud workloads with Network Flow Monitor](https://aws.amazon.com/blogs/networking-and-content-delivery/visualizing-network-performance-of-your-aws-cloud-workloads-with-network-flow-monitor/ "https://aws.amazon.com/blogs/networking-and-content-delivery/visualizing-network-performance-of-your-aws-cloud-workloads-with-network-flow-monitor/").
