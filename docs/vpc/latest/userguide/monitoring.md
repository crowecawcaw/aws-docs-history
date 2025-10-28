# Monitoring your VPC

You can use the following tools to monitor traffic or network access in your virtual private cloud (VPC).

**VPC Flow Logs**

You can use VPC Flow Logs to capture detailed information about the traffic going to and from
network interfaces in your VPCs.

**Amazon CloudWatch Internet Monitor**

You can use Internet Monitor for visibility into how internet issues impact the performance and availability
between your applications hosted on AWS and your end users. You can also explore, in near real-time, how to improve the
projected latency of your application by switching to use other services, or by rerouting traffic to your
workload through different AWS Regions. For more
information, see [Using Amazon CloudWatch Internet Monitor](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-InternetMonitor.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-InternetMonitor.md").

**Amazon VPC IP Address Manager (IPAM)**

You can use IPAM to plan, track, and monitor IP addresses for your workloads. For more
information, see [IP Address Manager](../ipam.md "../ipam.md").

**Traffic Mirroring**

You can use this feature to copy network traffic from a network interface of an Amazon EC2 instance
and send it to out-of-band security and monitoring appliances for deep packet inspection. You can
detect network and security anomalies, gain operational insights, implement compliance and security
controls, and troubleshoot issues. For more information, see [Traffic Mirroring](../mirroring.md "../mirroring.md").

**Reachability Analyzer**

You can use this tool to analyze and debug network reachability between two resources in your VPC.
After you specify the source and destination resources, Reachability Analyzer produces hop-by-hop details of the
virtual path between them when they are reachable, and identifies the blocking component when they
are unreachable. For more information, see [Reachability Analyzer](../reachability.md "../reachability.md").

**Network Access Analyzer**

You can use Network Access Analyzer to understand network access to your resources. This helps
you identify improvements to your network security posture and demonstrate that your network meets
specific compliance requirements. For more information, see [Network Access Analyzer](../network-access-analyzer.md "../network-access-analyzer.md").

**CloudTrail logs**

AWS CloudTrail logs API calls for Amazon VPC, such as:

- Which API calls were made (such as actions like creating or modifying VPC resources)
- The source IP address of the call
- Who made the call
- When the call was made

Separate logs are created for `CreateVpc`, `DeleteVpc` and `CreateDefaultVpc` actions. These logs also include the default resources (like any default internet gateways or default security groups) created and associated with the VPC.

For more information,
see [Log Amazon EC2 API calls using AWS CloudTrail](../../../AWSEC2/latest/UserGuide/monitor-with-cloudtrail.md "../../../AWSEC2/latest/UserGuide/monitor-with-cloudtrail.md")
in the _Amazon EC2 User Guide_.
