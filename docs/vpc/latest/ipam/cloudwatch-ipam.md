# Monitor IPAM with Amazon CloudWatch

IPAM automatically stores metrics related to IP address usage (such as the IP address
space available in your IPAM pools and the number of resource CIDRs that comply with
allocation rules) and resource utilization in the `AWS/IPAM`
[Amazon CloudWatch namespace](../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md#Namespace "../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md#Namespace") in the home Region of your IPAM.

Integrating IPAM with CloudWatch enhances your ability to monitor, analyze, and optimize your IP address management within AWS.

Use cases include:

- **Tracking IP address utilization trends**: CloudWatch can monitor CIDR
  pool usage, scope allocation, and other IPAM metrics, helping you proactively
  identify potential IP address exhaustion risks.
- **Setting utilization-based alerts**: You can configure CloudWatch
  alarms to notify you when CIDR utilization reaches predetermined thresholds,
  enabling timely intervention and optimization.
- **Monitoring IPAM events**: CloudWatch can capture and analyze
  IPAM-related events, such as CIDR allocations, deallocations, and scope
  modifications, providing visibility into IP address management activities.
- **Generating custom dashboards**: By combining IPAM data with
  other AWS metrics, you can create comprehensive dashboards to visualize and
  analyze your IP address landscape alongside related infrastructure and performance
  indicators.

###### Contents

- [Manage alarms from IPAM console](cloudwatch-ipam-manage-alarms.md "cloudwatch-ipam-manage-alarms.md")
- [IPAM metrics](cloudwatch-ipam-ip-address-usage.md "cloudwatch-ipam-ip-address-usage.md")
- [IPAM resource utilization metrics](cloudwatch-ipam-res-util.md "cloudwatch-ipam-res-util.md")
