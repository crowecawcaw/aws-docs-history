# Evaluate

network flows with workload insights

Network Flow Monitor provides workload insights about the network flows
in the scope that you enable monitoring for. By surfacing top contributor network
flows for each metric type, you can see which flows are potentially experiencing issues.
You can view these top contributor metrics in the console on the **Workload
insights** tab. In Network Flow Monitor, top contributors are network
flows that have the highest values for each network performance metric.

**Top contributors**
On the **Workload insights** page in the Network Flow Monitor console, Network Flow Monitor displays the top
contributor network performance statistics for the network flows between all the resources
in your monitoring scope where you've deployed agents.

To compile lists of top contributors, Network Flow Monitor determines the network flows
in your scope that have the highest values
for retransmissions, retransmission timeouts, and data transferred. These network flows
are the _top contributors_ for each metric type.

For workload insights, the top contributors are determined for all the network flows that you're
receiving performance information for; that is, network flows for all of the
resources in your scope with Network Flow Monitor agents installed.

**Network flow classifications**
Network Flow Monitor classifies metrics into designated local-remote categories.
Metrics are grouped into two types of flows:

- **Network Health Indicator (NHI) Flows:** Flows which contribute to Network Health Indicator (NHI) calculations:
  - Between AZs (`INTER_AZ`). Always within the same VPC.
  - Within AZs (`INTRA_AZ`). Always within the same VPC.
  - Between VPCs (`INTER_VPC`). Crosses the boundary between VPCs.
  - Between Regions (`INTER_REGION`). This means performance for network flows between resources in your Region and the edge of another Region.
  - Toward Amazon S3 buckets (`AMAZON_S3`)
  - Toward Amazon DynamoDB (`AMAZON_DYNAMODB`)

- **Non Network Health Indicator (NHI) Flows:** Flows which do not contribute to Network Health Indicator (NHI) calcuations:
  - Toward the Internet (`INTERNET`). Flows that traverse an Internet Gateway and end on the public Internet.
  - Towards AWS Services (`AWS_SERVICE`). Flows that end at an AWS service that is not fully monitored (like CloudFront or API Gateway).
  - Towards a Transit Gateway (`TRANSIT_GATEWAY`). Flows in this classification are flows that arrive at a Transit Gateway, but the final destination of the flow is unknown.
  - Towards a local zone (`LOCAL_ZONE`). Flows that start or end in a local zone
  - Any other flow that cannot be otherwise classified (`UNCLASSIFIED`).

**Performance metrics**
Performance metrics on **Workload insights** are shown in separate tables for
the following metric type: Retransmissions, retransmission
timeouts, and data transferred. The data provided is for the top contributors for each type.
Note that after you first install Network Flow Monitor agents, there is a
waiting period (about 20 minutes) before you can view performance metrics, while agents gather
and send data to the Network Flow Monitor backend.

**Monitor specific network flows**

As you review performance metrics, when you see specific resources or network flows that you want to
explore more details for, you can create a monitor that includes just those flows.

With a monitor, you can track specific groups of network flows over a period of time,
to gain insights into one aspect of your workload. You can also get helpful troubleshooting
information, such as checking the network health
indicator (NHI) to see if issues you see are caused by AWS impairments.

For more information, see [Create and work with monitors in Network Flow Monitor](CloudWatch-NetworkFlowMonitor-configure-monitors.md "CloudWatch-NetworkFlowMonitor-configure-monitors.md")

**Multi-account coverage**

To work with multiple accounts in Network Flow Monitor, you must configure AWS Organizations
integration with CloudWatch. By configuring Organizations, you can add accounts to the scope for your Network Flow Monitor coverage.
Then, if you have multiple accounts in your scope that each have resources that you want to
monitor network flows between, you can specify a scope that includes all of the accounts,
and then view performance metrics gathered by the Network Flow Monitor agents that you've installed on your
resources. For more information, see [Initialize Network Flow Monitor for multi-account monitoring](CloudWatch-NetworkFlowMonitor-multi-account.md "CloudWatch-NetworkFlowMonitor-multi-account.md").
