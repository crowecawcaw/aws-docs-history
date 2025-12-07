# Configuration settings for

Route 53 Profile

When you edit a Route 53 Profile configuration, you specify the following values:

**DNSSEC configuration**

Choose one of the following values:

- **Use local VPC DNSSEC configuration -
  default**

Choose this option to have all the VPCs associated to this
Profile keep their local DNSSEC validation
configuration.

- **Enable DNSSEC validation**

Choose this option to enable DNSSEC validation in all the
VPCs associated to this Profile.

- **Disable DNSSEC validation**

Choose this option to disable DNSSEC validation in all
VPCs that are associated to this Profile.

**Resolver reverse DNS lookup configuration**

Choose one of the following values:

- **Enable**

Choose this option to create auto defined rules for
reverse DNS look up in all the associated VPCs.

- **Not enabled**

Choose this option to not create auto defined rules for
reverse DNS look up in all the associated VPCs.

- **Use local auto defined rules -
  default**

Choose this option to use the local VPC settings for
reverse DNS lookup for the associated VPCs.

**DNS Firewall failure mode configuration**

Choose one of the following values:

- **Disable**

Choose this option to close the DNS Firewall failure mode
for the associated VPCs. With this option, DNS Firewall will
block all queries it can't properly evaluate.

- **Enabled**

Choose this option to keep the DNS Firewall failure mode
open for all the associated VPCs. With this option, DNS
Firewall will allow queries to proceed if it's unable to
properly evaluate them.

- **Use local failure mode settings -
  default**

Choose this option to use the local VPC DNS Firewall
failure mode settings.

For more information about the configurations, see

- [Enabling DNSSEC validation in
  Amazon Route 53](resolver-dnssec-validation.md "resolver-dnssec-validation.md")
- [Forwarding rules for
  reverse DNS queries in VPC Resolver](resolver-rules-managing.md#resolver-automatic-forwarding-rules-reverse-dns "resolver-rules-managing.md#resolver-automatic-forwarding-rules-reverse-dns")
- [DNS Firewall VPC
  configuration](resolver-dns-firewall-vpc-configuration.md "resolver-dns-firewall-vpc-configuration.md")
