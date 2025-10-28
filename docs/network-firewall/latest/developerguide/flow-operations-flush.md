# Using flow flush operations in Network Firewall

Flow flush operations give you greater control over how your firewall rules are applied to network traffic.
While Network Firewall automatically applies changes to stateful rules for new traffic flows, existing flows continue
to be processed according to the rules that were in place when those flows began.

By flushing specific flows from your firewall's state table,
you can force the firewall to treat subsequent matching traffic as new flows, ensuring they are evaluated against your current rule configurations.
This is useful when you update rule groups or firewall policies and want these changes to take effect for existing network traffic. For example, if you modify a rule group to drop specific types of traffic,
you can use a flow flush operation to ensure that all matching traffic—both new and existing—is evaluated against your updated rules.

The flow flush operation consists of two phases:

1. Initial flow identification phase - Marks specified flows for timeout in the state table
2. Flow pruning phase - Removes marked flows according to the firewall's built-in pruning mechanism

## Flushing traffic from your firewall's state table

###### Important

Flush operations cannot be cancelled once started.
If you haven't already reviewed the stream exception policy in your firewall, go do that now.
When you flush flows from the firewall state table, the rules engine will treat traffic according to the firewall's stream exception policy.
For information, see [Stream exception policy options](stream-exception-policy.md "stream-exception-policy.md").

###### Tip

If your firewall is shared with other AWS accounts through VPC endpoint associations, take care to notify VPC endpoint association owners before you flush flows from the primary firewall.

###### To flush traffic flows from a firewall state table

1. Sign in to the AWS Management Console and open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **Network Firewall**, choose **Firewalls**.
3. Choose the name of the firewall where you want to perform the flow operation.
4. In the **Firewall operations** section, choose **Configure flow flush**.
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
8. Choose **Start flush**, then confirm that you want to begin the operation.
9. Return to the firewall **Details** page to monitor the operation status.

For information on viewing the status and history of your operations, see [Viewing flow operations in Network Firewall](flow-operations-view.md "flow-operations-view.md").
