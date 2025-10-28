# Capturing traffic in your firewall's state table

With flow capture operations in Network Firewall, you can view information about active traffic flows that are tracked in your firewall's state table.
These operations provide a time-boxed view of network traffic, showing both new and established flows that match your specified criteria.
Captured data makes it easier to analyze current network traffic patterns, verify the effectiveness of your firewall rules,
identify unexpected traffic flows, and troubleshoot network connectivity issues.

You can the progress and history of flow captures in your firewall's **Details** page.

###### Tip

When using flow capture operations with broad filter criteria (like wide IP ranges), you might encounter operation limits. To stay within these limits, use more specific flow filters, such as narrower IP ranges or additional criteria like ports and protocols.

###### To capture traffic flows from a firewall state table

1. Sign in to the AWS Management Console and open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **Network Firewall**, choose **Firewalls**.
3. Choose the name of the firewall where you want to perform the flow operation.
4. In the **Firewall operations** section, choose **Configure flow capture**.
5. Configure the scope of the flow operation, depending on your firewall configuration:
   - To perform the operation in the primary firewall endpoint only, define the VpcEndpointId.
   - To perform the operation in a VPC endpoint association only, define the VPC endpoint association ARN.
   - To perform the operation in the primary firewall endpoint and all associated VPC endpoints, define the Availability Zone of the primary firewall endpoint.

6. Optionally, configure additional flow filters to further customize the scope of the operation:
   - **Minimum age** - To exclude recently established flows, set this value to filter out flows that are newer than the specified age, in seconds
   - **Source** - A single IP address, a range of IPs (CIDR), or port
   - **Destination** - A single IP address, a range of IPs (CIDR), or port
   - **Protocol number** - The assigned internet protocol number (IANA) for each supported protocol.
     If left empty, the operation captures flows with any supported protocol (TCP, UDP, ICMP, ICMPv6, SCTP).

7. Review your configured filters in the **Filters** section.
8. Choose **Start capture**, then confirm that you want to begin the operation.
9. Return to the **Details** page to monitor the operation status.
   For information on viewing the status and history of your operations, see [Viewing flow operations in Network Firewall](flow-operations-view.md "flow-operations-view.md").
