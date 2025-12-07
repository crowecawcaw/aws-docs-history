# Configure settings for DNS views in

Route 53 Global Resolver

Route 53 Global Resolver allows you to configure different DNS policies and access controls for different
groups of client devices based on their security requirements and access needs. Set up DNS
policies and access controls in Route 53 Global Resolver for different groups of client devices based on their
security requirements and access needs.

## Configuring DNS settings for client groups

Each DNS view has several settings that control how DNS queries are processed and resolved
for different client device groups.

### DNSSEC validation

DNSSEC validation helps ensure that DNS responses for public domains are authentic and
haven't been tampered with. When you enable DNSSEC validation, Route 53 Global Resolver checks DNSSEC
signatures and returns SERVFAIL for domains with invalid signatures.

**Consider enabling DNSSEC validation if:**

- Your organization needs cryptographic verification of DNS responses
- You want protection against DNS spoofing and cache poisoning attacks
- You have compliance requirements that require DNSSEC validation

###### Note

DNSSEC validation only applies to public domains. Private hosted zones use their own
authentication mechanisms.

### EDNS Client Subnet (ECS)

EDNS Client Subnet includes information about the client's network location in DNS queries
sent to authoritative servers. This allows content delivery networks and geographically
distributed services to provide location-appropriate responses.

**ECS can help you:**

- Get better performance from geographically distributed services
- Improve content delivery network routing accuracy
- Better comply with regional content restrictions

**Privacy considerations:**

- ECS reveals partial client IP information to authoritative servers (maximum /24 for IPv4
  and /48 for IPv6)
- Consider your organization's privacy requirements before enabling

### Firewall fail open

The firewall fail open setting determines what happens when DNS firewall rules cannot be
evaluated due to service impairment or configuration issues.

Disabled (default)

DNS queries are blocked when firewall rules can't be evaluated. This gives you maximum
security but might affect availability during service issues.

Enabled

DNS queries are allowed when firewall rules can't be evaluated. This prioritizes
availability over security during service issues.

## Best practices for organizing client device

groups

Follow these best practices when designing DNS views for different client device
groups:

### View organization strategies

- **Separate by security requirements** - Create different
  views for client devices with different security clearances or access levels
- **Organize by location** - Use separate views for different
  geographic locations or network segments
- **Group by device type** - Create dedicated views for
  servers, workstations, mobile devices, or IoT devices
- **Use descriptive names** - Choose names that clearly
  indicate the view's purpose and target client devices

### Security considerations

- **Principle of least privilege** - Configure each view with
  the minimum access required for its client devices
- **Default deny** - Start with restrictive firewall rules
  and add exceptions as needed
- **Regular review** - Periodically review and update DNS
  view configurations
- **Monitor usage** - Use DNS query logs to monitor and
  analyze DNS view usage patterns
