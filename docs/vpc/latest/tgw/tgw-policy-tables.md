# Transit gateway policy tables in AWS Transit Gateway

Transit gateway dynamic routing uses policy tables to route network traffic for
AWS Cloud WAN. The table contains policy rules for matching network traffic by policy
attributes, and then maps the traffic that matches the rule to a target route table.

You can use dynamic routing for transit gateways to automatically exchange routing and
reachability information with peered transit gateway types. Unlike with a static route, traffic
can be routed along a different path based on network conditions, such as path failures
or congestion. Dynamic routing also adds an extra layer of security in that it's easier
to re-route traffic in the event of a network breach or incursion.

###### Note

Transit gateway policy tables are currently only supported in Cloud WAN when
creating a transit gateway peering connection. When creating a peering connection, you can
associate that table with the connection. The association then populates the table
automatically with the policy rules.

For more information about peering connections in Cloud WAN, see [Peerings](../../../network-manager/latest/cloudwan/cloudwan-peerings.md "../../../network-manager/latest/cloudwan/cloudwan-peerings.md") in the _AWS Cloud WAN User Guide_.

###### Tasks

- [Create a transit gateway policy table](tgw-policy-tables-create.md "tgw-policy-tables-create.md")
- [Delete a transit gateway policy table](tgw-policy-tables-disable.md "tgw-policy-tables-disable.md")
