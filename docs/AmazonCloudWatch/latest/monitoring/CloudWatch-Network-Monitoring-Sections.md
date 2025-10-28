# Network Monitoring

The topics in this section describe CloudWatch network and internet monitoring capabilities provided by Network Flow Monitor, Internet Monitor
and Network Synthetic Monitor. These services help you to gain operational visibility into the network and internet performance
and availability of your applications hosted on AWS.

- Network Flow Monitor provides near real-time visibility into network performance, such
  as packet loss and latency, for traffic between Amazon EC2 instances, as well as traffic
  toward other AWS services, such as Amazon S3 and Amazon DynamoDB. Network Flow Monitor works by using data from
  lightweight software agents that you install to run on your instances. These fully-managed agents gather
  performance statistics from TCP connections and send them to the Network Flow Monitor backend. By creating
  monitors for specific agents and then using Network Flow Monitor dashboards, you can quickly
  visualize packet loss and latency of your network connections, and use attribution
  information to determine where to
  focus your troubleshooting efforts to improve your end users’ experience.
- Internet Monitor uses the connectivity data that AWS captures from its global networking footprint to
  calculate a baseline of performance and availability for internet-facing traffic. You can see a global view
  of traffic patterns and health events, and easily drill down into information about events. You can also
  get alerts for internet health events that affect your application clients. In addition, you can use insights
  that Internet Monitor provides to explore potential improvements to your client experience, by using Amazon CloudFront or routing
  through different AWS Regions.
- Network Synthetic Monitor uses fully-managed agents to enable you to track and visualize latency
  and packet loss for hybrid network connections. To gather measurements and enable Network Synthetic Monitor to create health
  event alerts for your application, you create probes that are sent from your resources hosted on AWS to
  on-premises destination IP addresses. You don't need to install additional agents to monitor your network
  performance. As with Internet Monitor, you can set alerts and thresholds, get information to help you quickly troubleshoot
  issues, and then take action to improve your end user experience.

###### Topics

- [Using Network Flow Monitor](CloudWatch-NetworkFlowMonitor.md "CloudWatch-NetworkFlowMonitor.md")
- [Using Internet Monitor](CloudWatch-InternetMonitor.md "CloudWatch-InternetMonitor.md")
- [Using Network Synthetic Monitor](what-is-network-monitor.md "what-is-network-monitor.md")
