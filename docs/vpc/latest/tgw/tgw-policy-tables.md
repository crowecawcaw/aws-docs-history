# Transit gateway policy tables in AWS Transit Gateway

Policy-Based Routing (PBR) for AWS Transit Gateway gives network administrators rule-based control
over how traffic is forwarded across a transit gateway. With PBR, forwarding decisions can
be based on a combination of packet attributes including source and destination IP
addresses, source and destination ports, and protocol rather than destination IP address
alone. This enables you to apply different forwarding behaviors to different traffic flows
even when those flows share the same destination.

With PBR, you can:

- Steer traffic selectively to security appliances or inspection services based on
  source, port, or protocol.
- Route traffic from different applications or user populations over different
  network paths.
- Isolate network traffic into separate routing domains for security
  segmentation.
  PBR is configured through policy tables, which are ordered lists of rules that classify
  traffic and direct matching packets to a specified transit gateway route table. You associate a policy
  table with a transit gateway attachment. A policy table replaces the standard route table on an
  attachment. An attachment can be associated with either a policy table or a route table, but
  not both.

PBR is available in all AWS Regions where transit gateway is available at no additional charge
beyond standard transit gateway fees.

###### Tasks

- [Policy table concepts](tgw-policy-tables-concepts.md "tgw-policy-tables-concepts.md")
- [Prerequisites](tgw-policy-tables-prerequisites.md "tgw-policy-tables-prerequisites.md")
- [Create a transit gateway policy table](tgw-policy-tables-create.md "tgw-policy-tables-create.md")
- [View transit gateway policy tables](tgw-policy-tables-view.md "tgw-policy-tables-view.md")
- [Create a policy table entry](tgw-policy-tables-entry-create.md "tgw-policy-tables-entry-create.md")
- [Modify a policy table entry](tgw-policy-tables-entry-modify.md "tgw-policy-tables-entry-modify.md")
- [Delete a policy table entry](tgw-policy-tables-entry-delete.md "tgw-policy-tables-entry-delete.md")
- [Associate a transit gateway policy table](tgw-policy-tables-associate.md "tgw-policy-tables-associate.md")
- [Disassociate a transit gateway policy table](tgw-policy-tables-disassociate.md "tgw-policy-tables-disassociate.md")
- [Delete a transit gateway policy table](tgw-policy-tables-disable.md "tgw-policy-tables-disable.md")
- [Example: Steering traffic to a security appliance](tgw-policy-tables-example.md "tgw-policy-tables-example.md")
- [Limitations](tgw-policy-tables-limitations.md "tgw-policy-tables-limitations.md")
- [Troubleshooting](tgw-policy-tables-troubleshooting.md "tgw-policy-tables-troubleshooting.md")
- [Related resources](tgw-policy-tables-related.md "tgw-policy-tables-related.md")
