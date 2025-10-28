# Managing your firewall state table using flow operations in AWS Network Firewall

This section describes how to use flow operations to perform actions in your firewall's state table.

Flow operations are asynchronous actions that you execute within a firewall that you own.
To track and manage traffic that's logged within the firewall's state table. You can run flow capture operations or flow flush operations.
Flow capture operations collect information about active flows, and flow flush operations remove specified flows from the firewall.

Before you start using flow operations, review the following key definitions.

- **Flows** – Network traffic that is monitored by
  a firewall, either by stateful or stateless rules. For traffic to be considered part of a flow, it must
  share Destination, DestinationPort, Direction, Protocol, Source, and SourcePort with other traffic. Flows that are processed by
  the firewall are tracked in the firewall state table and are visible in flow logs.
- **Firewall state table** – Table where Network Firewall tracks and maintains information about network traffic flows.
  The firewall state table only tracks flows that are processed by stateful rules.
  When traffic matches the criteria in a stateful rule, the firewall creates a flow entry in the firewall state table.
  These entries persist until they are either removed using a flow flush operation, naturally terminate, or time out due to inactivity.
  You can manage the firewall state table using specific operations. This is also known as the firewall table or state table.

For information, see Flow operations in your firewall.

- **Flow filter** – Parameters that you use when defining the scope of a flow operation. You can use up to 20 filters in a single operation.

###### Topics

- [Caveats and considerations for flow operations](#flow-operations-caveats "#flow-operations-caveats")
- [Capturing traffic in your firewall's state table](flow-operations-capture.md "flow-operations-capture.md")
- [Using flow flush operations in Network Firewall](flow-operations-flush.md "flow-operations-flush.md")
- [Viewing flow operations in Network Firewall](flow-operations-view.md "flow-operations-view.md")

###### Note

This section and others that describe Suricata-based concepts are not intended to replace or duplicate information from the Suricata documentation.
For more Suricata-specific information, see the [Suricata documentation](https://docs.suricata.io/en/suricata-7.0.8/ "https://docs.suricata.io/en/suricata-7.0.8/").

## Caveats and considerations for flow operations

Before using flow operations, consider the following:

- When you initiate a flow flush operation, the firewall treats impacted flows according to your stream exception policy configuration. Review your stream exception policy settings before performing a flush operation. For information, see [Stream exception policy options](stream-exception-policy.md "stream-exception-policy.md").
- If you execute flow capture operations using broad filter criteria (like wide IP ranges), you might encounter operation limits.
  To stay within these limits, use more specific flow filters, such as narrower IP ranges or additional criteria like ports and protocols.
- When you flush flows, subsequent matching traffic is considered a new flow and evaluated against current firewall rule configurations.
- Only firewall owners can perform flow operations. VPC endpoint association owners who do not also own the main firewall cannot perform flow operations on that firewall.
  For more information, see [Firewalls and firewall endpoints in AWS Network Firewall](firewalls.md "firewalls.md").
- Flow operations execute asynchronously across your firewall infrastructure. In the context of flow flush operations,
  this means flows might be marked for removal at slightly different times as the operation propagates.
- Each flow operation (capture or flush) runs on one individual firewall at a time.
  If you need to perform flow operations across multiple firewalls in your network configuration,
  you must run separate operations for each firewall.

###### Note

We throttle flush and capture operations to one concurrent request per firewall per Availability Zone (AZ).
For example, if a firewall is deployed to two Availability Zones in the same Region,
you can issue two concurrent flow or capture requests for that firewall (one request per Availability Zone).
This throttling helps maintain optimal performance and prevents overloading the system.

For information on how Network Firewall propagates changes you make, see [Managing a firewall and firewall endpoints in AWS Network Firewall](firewall-managing.md "firewall-managing.md").
