# ADVSEC01-BP03 Restrict DSP outbound traffic to authorized SSPs only

Address the risk of DSP unintentional data disclosure to SSPs that
were not approved.

## Implementation guidance

Consider using an
[Amazon Virtual Private Cloud (Amazon VPC)](https://aws.amazon.com/vpc/ "https://aws.amazon.com/vpc/") to restrict outgoing traffic from
instances to the authorized DSP endpoints. VPCs can to define
access to verify that all ports, protocols, and destination IP
addresses meet your organizations security needs. Use VPC
security groups to permit access from trusted sources or
specific IP ranges. Use a protocol with encryption when
transmitting data to maintain data confidentiality and mitigate
the risk of unauthorized access to the data.

Additionally, implement
[AWS Network Firewall](https://aws.amazon.com/network-firewall/ "https://aws.amazon.com/network-firewall/") to provide control over outbound traffic from
your VPCs to approved destinations only. Network Firewall allows
you to define and enforce rules to inspect and filter outgoing
traffic against malware or unauthorized data exfiltration. Using
Network Firewall rule groups, you can prevent data loss, meet
compliance requirements, or block any known malware
communications.
