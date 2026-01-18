# Operational excellence pillar

The operational excellence pillar includes the ability to run and
monitor systems to deliver business value, and to continually
improve supporting processes and procedures. It provides an
overview of design principles, best practices, and questions

## Best practices

There are three best practice areas for operational excellence
in the cloud:

- Preparation
- Operation
- Evolution

To drive operational excellence in hybrid networking
architectures, operations teams need to understand their
business and customer needs so that they can effectively and
efficiently support business outcomes. Operations creates and
uses procedures to respond to operational events and validates
their effectiveness to support business needs. Operations
collects metrics that are used to measure the achievement of
desired business outcomes. Everything continues to change—your
business context, business priorities, customer needs, and etc.
It’s important to design operations to support evolution over
time in response to change and to incorporate lessons learned
through their performance.

### Preparation

Preparation is essential to drive operational excellence in
your hybrid networking environment. Many operational issues
can be avoided by following best practices when designing the
workload, and fixes are less expensive to implement in design
phases rather than in production. It is important to assess
the current state of your on-premises network and understand
solutions for establishing your hybrid networking
capabilities.

| HN_OPS1: How do you ensure efficient IP address allocation across your VPCs<br>and on-premises networks? |
| -------------------------------------------------------------------------------------------------------- |
|                                                                                                          |

To prepare for operational excellence, you have to understand
your hybrid workloads and their requirements. One key aspect
is IP addressing. A well defined IP address allocation scheme
has the following benefits:

- Enables efficient routing structure where you can summarize routes based on a
  network boundary. For example, if you were hosting workloads in VPCs in
  `us-east-1`, you can allocate CIDR ranges to these VPCs from a defined
  block like 10.1.1.0/22. You can then configure the Transit Gateway association a
  Direct Connect gateway to advertise this block over transit virtual interface instead
  of advertising individual prefixes associated with individual VPCs. Well summarized
  CIDR ranges can also help with security and firewall configuration when defining
  security groups and NACLs.
- Reduces the risk of over-lapping CIDR ranges between VPC
  and on-premises networks. You should avoid re-using the
  same CIDR range between your on-premises and Amazon VPC
  network, since overlapping CIDR ranges will make host to
  host communication very difficult.

We recommend that you keep track of the IP prefixes you currently have and allocate
CIDR ranges for your deployment in a systematic manner. You can utilize one of many [IPAM
solutions](https://aws.amazon.com/marketplace/search/results?searchTerms=IPAM "https://aws.amazon.com/marketplace/search/results?searchTerms=IPAM") available from the AWS marketplace. When provisioning VPCs, you need
to ensure that you allocate right-sized CIDR ranges. If you overprovision your VPC CIDR
ranges you will later face IP exhaustion as you grow the number of VPCs. If you under
provision the VPC CIDR range, you can associate secondary IPv4 CIDR blocks to your VPC,
but with [restrictions](../../../vpc/latest/userguide/VPC_Subnets.md "../../../vpc/latest/userguide/VPC_Subnets.md"). It’s important to understand your workload requirements such as
their scalability patterns (and how scalability impacts IP usage), their reliability
requirements (how many AZs the workload gets deployed in and how many IPs per AZ is
utilized), and factor this information in when allocating IP ranges to the VPCs running
these workloads. Its better to start with a conservative approach than overprovision the
size of CIDR range allocation. In addition, ensure that VPC ranges don’t overlap with
on-premises IP ranges.

### Operation

It’s important to define standards, procedures, and monitoring
capabilities for your on-premises network environment that can
provide you with real-time metrics important for your specific
business needs. Aggregate these metrics, visualize them in a
dashboard, and set automated alerts that can notify the
operations team. In addition, develop a runbook that provides
procedures for different alerts and alarms.

| HN_OPS2: How do you understand the health of your<br>hybrid network? |
| -------------------------------------------------------------------- |
|                                                                      |

| HN_OPS3: How do you manage operational events? |
| ---------------------------------------------- |
|                                                |

**AWS Direct Connect:** Enables
you to monitor physical AWS Direct Connect connections using
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/") to collect and process raw data from AWS Direct Connect into readable, near real-time metrics. You can
consolidate these metrics in CloudWatch, and build dashboards
and alerts to notify your operations team based on the defined
conditions.

AWS Direct Connect schedules planned maintenance and notifies
you. To help you manage these events, you can leverage
[AWS Health Dashboard](https://aws.amazon.com/premiumsupport/phd/ "https://aws.amazon.com/premiumsupport/phd/") to display
relevant information and provide proactive notifications so
that you can plan for scheduled activities. We recommend using
the Health Dashboard to receive notifications for
scheduled maintenance or events that will affect Direct
Connect.

Your operations team should be prepared for unplanned outages
with networking while connecting from on-premises to AWS. For
example, to be prepared for an unplanned outage like an AWS Direct Connect connection failure, you should establish a
second Direct Connect connection. Traffic will fail over to
the second link automatically if the BGP prefixes advertised
are same over both connections. We recommend enabling
Bidirectional Forwarding Detection (BFD) when configuring your
connections to ensure fast detection and failover. Ensure that
you test your high-availability design and configuration
periodically using
[AWS Direct Connect Resiliency toolkit failover testing](https://aws.amazon.com/blogs/networking-and-content-delivery/testing-aws-direct-connect-resiliency-with-resiliency-toolkit-failover-testing/ "https://aws.amazon.com/blogs/networking-and-content-delivery/testing-aws-direct-connect-resiliency-with-resiliency-toolkit-failover-testing/").
Additionally, you can configure a back-up IPsec VPN
connection, in which case all VPC traffic will fail over to
the VPN connection automatically when direct connect
connections fails. Traffic to and from public resources, such
as Amazon Simple Storage Service (Amazon S3), can be routed
over the internet if they were previously being routed over
Direct Connect public virtual interface.

**AWS site-to-site VPN:**
Enables you to
[monitor
VPN tunnels](../../../vpn/latest/s2svpn/monitoring-cloudwatch-vpn.md "../../../vpn/latest/s2svpn/monitoring-cloudwatch-vpn.md") using CloudWatch, leveraging near real-time
metrics. You can monitor the state of your VPN tunnels and the
data retrieved in/out of the tunnels. These metrics are
recorded for 15 months, so you can access historical
information and gain a better perspective on how your hybrid
setup performed. VPN metric data is automatically sent to
CloudWatch as it becomes available.

To ensure operational stability in case of failures, Site-to-Site VPN
has built in high-availability. AWS Site-to-Site VPN
connection has two tunnels, with each tunnel using a unique
virtual private gateway public IP address. It is important to
configure both tunnels for redundancy, if one tunnel becomes
unavailable (for example, if it is down for maintenance),
network traffic is automatically routed to the available
tunnel for that specific Site-to-Site VPN connection. However,
to protect against a loss of connectivity if your customer
gateway becomes unavailable, you can set up a second
Site-to-Site VPN connection to your VPC and virtual private
gateway by using a second customer gateway. By using redundant
Site-to-Site VPN connections and customer gateways, you can
perform maintenance on one of your customer gateways while
traffic continues to flow over the second customer gateway
Site-to-Site VPN connection.

**AWS Transit Gateway:**
Leveraging a transit gateway as a central hub enables access
between your VPC resources and on-premises using AWS Direct
connect or Site-to-Site VPN. AWS Transit Gateway provides statistics
and logs that can be used by services such as Amazon CloudWatch and
[Amazon VPC Flow Logs](../../../vpc/latest/userguide/flow-logs.md "../../../vpc/latest/userguide/flow-logs.md"). You can start by tracking health data
and manage operations by building dashboards/alarms off
[transit
gateway attachment level CloudWatch metrics](../../../vpc/latest/tgw/transit-gateway-cloudwatch-metrics.md "../../../vpc/latest/tgw/transit-gateway-cloudwatch-metrics.md"). You can
use Amazon CloudWatch to retrieve bandwidth usage between
Amazon VPCs and a VPN connection, packet flow count, and
packet drop count. Additionally, you can enable Amazon VPC
Flow Logs on AWS Transit Gateway to capture information on the
IP traffic routed through the AWS Transit Gateway.

**AWS Transit Gateway Network
Manager:** Provides a single global view of your
private network including hybrid connectivity. It enables you
to see network activity in many locations from one single
dashboard. It also includes the following data to help you
monitor and troubleshoot the quality of your global network.

- **Events:** Describes
  changes in your global network. Transit Gateway Network
  Manager sends the following type of events to CloudWatch Events:
  - Topology changes: For example, an AWS Direct Connect
    gateway was attached to a transit gateway
  - Routing updates: For example, a VPN attachment's route
    table association changed
  - Status updates: For example, a VPN tunnel's BGP
    session went up (after being down)

For more information on tracking and getting notified of
events relevant to your use case, refer to
[Transit
Gateways User Guide](../../../vpc/latest/tgw/monitoring-events.md "../../../vpc/latest/tgw/monitoring-events.md").

- **Metrics:** Enables you to
  view CloudWatch metrics in your global network for your
  registered transited gateways, your associated
  Site-to-Site VPN connections, and your on-premises
  resources. You can view metrics per transit gateway and
  per transit gateway attachment, per global network. For
  more information, refer to
  [Monitoring
  CloudWatch metrics](../../../vpc/latest/tgw/monitoring-cloudwatch-metrics.md "../../../vpc/latest/tgw/monitoring-cloudwatch-metrics.md").

- **Route Analyzer:** Enables
  you to perform an analysis of the routes in your transit
  gateway route tables in your global network. The Route
  Analyzer analyzes the routing path between a specified
  source and destination, and returns information about the
  connectivity between components. You can use the Route
  Analyzer to do the following:

- Verify that the transit gateway route table configuration
  will work as expected before you start sending traffic.
- Validate your existing route configuration.
- Diagnose route-related issues that are causing traffic
  disruption in your global network.

When building a hybrid network leveraging Transit Gateway,
we recommend using Route Analyzer to
[verify
and resolve network connectivity issues](https://aws.amazon.com/blogs/networking-and-content-delivery/diagnosing-traffic-disruption-using-aws-transit-gateway-network-manager-route-analyzer/ "https://aws.amazon.com/blogs/networking-and-content-delivery/diagnosing-traffic-disruption-using-aws-transit-gateway-network-manager-route-analyzer/").

### Evolution

There are no operational practices unique to Hybrid lens for the **evolve** practice area, you can review the corresponding section in
the [AWS
Well-Architected Framework whitepaper](../framework/welcome.md "../framework/welcome.md").

## Resources

Refer to the following resources to learn more about AWS best
practices for operational excellence.

### Documents

- [Amazon CloudWatch metrics for AWS Direct Connect](../../../directconnect/latest/UserGuide/monitoring-cloudwatch.md "../../../directconnect/latest/UserGuide/monitoring-cloudwatch.md")
- [Amazon CloudWatch metrics for AWS Site-to-site VPN](../../../vpn/latest/s2svpn/monitoring-cloudwatch-vpn.md "../../../vpn/latest/s2svpn/monitoring-cloudwatch-vpn.md")

### AWS Support

- [How
  can I get notifications for AWS Direct Connect Scheduled
  maintenance or events?](https://aws.amazon.com/premiumsupport/knowledge-center/get-direct-connect-notifications/ "https://aws.amazon.com/premiumsupport/knowledge-center/get-direct-connect-notifications/")
- [How
  do I monitor Site-to-Site VPN tunnels using Amazon CloudWatch
  alarms?](https://aws.amazon.com/premiumsupport/knowledge-center/monitor-vpn-with-cloudwatch-alarms/ "https://aws.amazon.com/premiumsupport/knowledge-center/monitor-vpn-with-cloudwatch-alarms/")
- [How
  do I check the current status of my VPN tunnel?](https://aws.amazon.com/premiumsupport/knowledge-center/check-vpn-tunnel-status/ "https://aws.amazon.com/premiumsupport/knowledge-center/check-vpn-tunnel-status/")
- [How
  can I get notifications for AWS Direct Connect scheduled
  maintenance or events?](https://aws.amazon.com/premiumsupport/knowledge-center/get-direct-connect-notifications/ "https://aws.amazon.com/premiumsupport/knowledge-center/get-direct-connect-notifications/")
- [How
  should I prepare for maintenance on my Direct Connect
  connection?](https://aws.amazon.com/premiumsupport/knowledge-center/prepare-direct-connect-maintenance/ "https://aws.amazon.com/premiumsupport/knowledge-center/prepare-direct-connect-maintenance/")
