# Firewall components in AWS Network Firewall

The AWS Network Firewall firewall runs stateless and stateful traffic inspection rules engines.
The engines use rules and other settings that you configure inside a firewall policy.

You install the firewall endpoints on a per-Availability Zone basis in your VPC. For each Availability
Zone where you want to use the firewall, you choose a subnet to host the primary firewall endpoint.
As needed, you can create VPC endpoint associations to provide additional subnets as firewall endpoints.

A firewall endpoint can protect any subnet in your VPC except for the one in which it's located.

You manage Network Firewall firewalls with the following central components.

- **Rule group** – Holds a reusable collection of
  criteria for inspecting traffic and for handling packets and traffic flows that
  match the inspection criteria. For example, you can choose to drop or pass a
  packet or all packets in a traffic flow based on the inspection criteria. Some
  rule groups fully define the behavior and some use lower-level rules that
  provide more detail. Rule groups are either stateless or stateful.
  For
  more information about rule groups and rules, see [Managing your rule groups](rule-groups.md "rule-groups.md").
- **Firewall policy** – Defines a reusable
  set of stateless and stateful rule groups, along with some policy-level behavior
  settings. The firewall policy provides the network traffic filtering behavior for
  a firewall. You can use a single firewall policy in multiple firewalls.
  For more information about firewall policies, see [Firewall policies](firewall-policies.md "firewall-policies.md").
- **Firewall** – Connects the inspection
  rules in the firewall policy to the primary VPC that the
  rules protect. Each firewall requires one firewall policy. The firewall additionally
  defines settings like how to log information about your network traffic and
  the firewall's stateful traffic filtering. For more information about
  firewalls, see [Firewalls and firewall endpoints](firewalls.md "firewalls.md").
- **VPC endpoint association** – Implements a
  firewall's protections in additional firewall endpoints.
  For more information, see [Firewalls and firewall endpoints](firewalls.md "firewalls.md").
