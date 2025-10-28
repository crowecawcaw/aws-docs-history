# Network Firewall stateless and stateful rules engines

AWS Network Firewall uses two rules engines to inspect packets. The engines inspect packets
according to the rules that you provide in your firewall policy.

The following figure shows the processing flow for packets coming through the firewall.
First the stateless engine inspects the packet against the configured stateless
rules. Depending on the packet settings, the stateless inspection criteria, and the
firewall policy settings, the stateless engine might drop a packet, pass it through
to its destination, or forward it to the stateful rules engine. The stateful engine
inspects packets in the context of their traffic flow, using the configured stateful
rules. The stateful engine either drops packets or passes them to their destination.
Stateful engine activities are recorded in the firewall's logs, if
logging is configured. The stateful engine sends alerts for dropped packets and can
optionally send them for passed packets.

![The figure shows a firewall stateless engine, which inspects packets against stateless rules, and a firewall stateful engine, which inspects traffic flows against stateful rules. The stateless engine sits above and to the left of the stateful engine. One vertical grey arrow points down to the stateless engine from above. The stateless engine and the stateful engine each have a vertical green arrow labeled "pass" that comes from the bottom of the engine, joins the green arrow from the other engine and points down to the bottom of the figure. From the right side of the stateless engine, a grey arrow labeled "forward to stateful" points out and down to the stateful engine. Each engine also has a horizontal red arrow labeled "drop" that points right from the right side of the engine to a large red X. The stateful engine also has arrows indicating an alert that's sent with drop and an optional alert that's sent with pass.](images/firewall-stateless-stateful.png)
The stateless and stateful rules inspection engines operate in different ways:

- **Stateless rules engine** – Inspects each packet in
  isolation, without regard to factors such as the direction of traffic, or
  whether the packet is part of an existing, approved connection. This engine
  prioritizes the speed of evaluation. It takes rules with standard network connection attributes. The engine processes your rules in the order that you prioritize them and stops processing when it finds a match.

Network Firewall stateless rules are similar in behavior and use to Amazon VPC network
access control lists (ACLs).

- **Stateful rules engine** – Inspects packets in the
  context of their traffic flow, allows you to use more complex rules, and
  allows you to log network traffic and to log Network Firewall firewall alerts
  on traffic. Stateful rules consider traffic direction. The stateful rules
  engine might delay packet delivery in order to group packets for inspection.
  By default, the stateful rules engine processes your rules in the order of
  their action setting, with pass rules processed first, then drop, then
  alert. The engine stops processing when it finds a match.

The stateful engine takes rules that are compatible with Suricata, an open
source intrusion prevention system (IPS). Suricata provides a standard
rule-based language for stateful network traffic inspection. For more
information about Suricata, see [Working with stateful rule groups in
AWS Network Firewall](stateful-rule-groups-ips.md "stateful-rule-groups-ips.md") and the [Suricata website](https://suricata.io/ "https://suricata.io/").

Network Firewall stateful rules are similar in behavior and use to Amazon VPC security groups. By
default, the stateful rules engine allows traffic to pass, while the
security groups default is to deny traffic.
Whether you use only one of these engines or a combination depends on your specific
use case.
