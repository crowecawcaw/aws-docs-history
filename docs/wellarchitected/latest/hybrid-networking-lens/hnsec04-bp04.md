# HNSEC04-BP04 Implement DNS security controls

DNS security control protects against DNS threats such as data
exfiltration. You can create blocklists and allowlists to manage
which domains your resources can query through DNS.

**Desired outcome:** Prevent data
exfiltration and block malicious domains at the DNS layer in hybrid
networks.

**Level of risk exposed if this best practice
is not established:** Medium

**Benefits of establishing this best
practice:**

- Blocks DNS-based attacks and data exfiltration
- Provides centralized control over DNS traffic
- Enables logging and reporting for compliance

## Implementation guidance

- Define DNS firewall rule groups for blocklists and allowlists.
- Associate DNS firewall rules with relevant networks.
- Monitor DNS queries and refine rules based on findings.

## Resources

- [How
  Resolver DNS Firewall works](../../../Route%C2%A053/latest/DeveloperGuide/resolver-dns-firewall-overview.md "../../../Route%C2%A053/latest/DeveloperGuide/resolver-dns-firewall-overview.md")
