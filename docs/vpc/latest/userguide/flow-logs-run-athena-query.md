# Run a predefined query

The generated CloudFormation template provides a set of predefined queries that
you can run to quickly get meaningful insights about the traffic in your AWS
network. After you create the stack and verify that all resources were created
correctly, you can run one of the predefined queries.

###### To run a predefined query using the console

1. Open the Athena console.
2. In the left nav, choose **Query editor**. Under **Workgroup**, select
   the workgroup created by the CloudFormation template.
3. Select **Saved queries**, select a query, modify the
   parameters as needed, and run the query. For a list of available predefined
   queries, see [Predefined
   queries](#predefined-queries "#predefined-queries").
4. Under **Query results**, view the query results.

## Predefined queries

The following is the complete list of Athena named queries. The predefined queries that
are provided when you generate the template depend on the fields that are part of the
log record format for the flow log. Therefore, the template might not contain all of
these predefined queries.

- **VpcFlowLogsAcceptedTraffic** – The TCP connections that were allowed
  based on your security groups and network ACLs.
- **VpcFlowLogsAdminPortTraffic** – The top 10 IP addresses with the
  most traffic, as recorded by applications serving requests on
  administrative ports.
- **VpcFlowLogsIPv4Traffic** – The total bytes of IPv4 traffic
  recorded.
- **VpcFlowLogsIPv6Traffic** – The total bytes of IPv6 traffic
  recorded.
- **VpcFlowLogsRejectedTCPTraffic** – The TCP connections that were
  rejected based on your security groups or network ACLs.
- **VpcFlowLogsRejectedTraffic** – The traffic that was rejected based
  on your security groups or network ACLs.
- **VpcFlowLogsSshRdpTraffic** –
  The SSH and RDP traffic.
- **VpcFlowLogsTopTalkers** – The 50 IP addresses with the most traffic
  recorded.
- **VpcFlowLogsTopTalkersPacketLevel** – The 50 packet-level IP
  addresses with the most traffic recorded.
- **VpcFlowLogsTopTalkingInstances** – The IDs of the 50 instances with
  the most traffic recorded.
- **VpcFlowLogsTopTalkingSubnets** – The IDs of the 50 subnets with the
  most traffic recorded.
- **VpcFlowLogsTopTCPTraffic** – All TCP traffic recorded for a source
  IP address.
- **VpcFlowLogsTotalBytesTransferred** – The 50 pairs of source and
  destination IP addresses with the most bytes recorded.
- **VpcFlowLogsTotalBytesTransferredPacketLevel** – The 50 pairs of
  packet-level source and destination IP addresses with the most bytes
  recorded.
- **VpcFlowLogsTrafficFrmSrcAddr** – The traffic recorded for a specific
  source IP address.
- **VpcFlowLogsTrafficToDstAddr** – The traffic recorded for a specific
  destination IP address.
