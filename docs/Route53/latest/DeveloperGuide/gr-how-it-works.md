# How Route 53 Global Resolver works

Route 53 Global Resolver enables split-traffic DNS resolution between public and private domains, provides
high availability through through the two or more AWS Regions you choose, and secures DNS queries
by intercepting requests and applying DNS filtering policies. Understanding this process helps you
troubleshoot issues and optimize your deployment for performance, availability, and
security.

## What happens when clients make DNS queries

When someone at your location tries to query domain, Route 53 Global Resolver processes their DNS request
through multiple security layers.

The DNS query processing involves these sequential steps:

1. **Query reception** - Client devices send DNS queries to
   Route 53 Global Resolver anycast IP addresses. The anycast routing automatically directs queries to the nearest
   AWS Region.
2. **Authentication** - Route 53 Global Resolver authenticates the client using
   configured authentication methods (token-based for DoH/DoT or IP Access Source for all
   protocols).
3. **Policy evaluation** - The service evaluates DNS queries
   against configured security policies and domain lists to determine the appropriate action
   (allow, block, or alert). For queries targeting private hosted zones, Route 53 Global Resolver checks if the
   client is authorized to access the private domain based on the DNS view rule managed by your administrator before proceeding with
   resolution.
4. **Resolution** - For allowed queries, Route 53 Global Resolver performs DNS
   resolution using public DNS resolvers or private hosted zone resolution as appropriate.
5. **Response delivery** - The service returns the DNS response
   to the client and logs the query details for monitoring and analysis.

## Global anycast architecture

Route 53 Global Resolver uses anycast IP addresses to provide global availability and automatic geographic
routing.

Route 53 Global Resolver uses anycast IP addresses to provide:

- **Automatic geographic routing** - DNS queries are
  automatically routed to the closest AWS Region for optimal performance.
- **Built-in redundancy** - If a Region becomes unavailable,
  traffic automatically fails over to the next closest Region.
- **Consistent IP addresses** - Clients use the same anycast IP
  addresses regardless of their location, simplifying configuration.

## DNS filtering and security

Route 53 Global Resolver provides comprehensive DNS filtering and security through multiple layers. The DNS
filtering and security architecture diagram illustrates how queries are processed through
authentication, policy evaluation, and resolution layers.

Route 53 Global Resolver provides comprehensive DNS security through:

- **Domain-based filtering** - Block or allow queries based on
  domain names using custom or AWS managed domain lists.
- **Threat intelligence integration** - Leverage AWS managed
  threat intelligence to automatically block known malicious domains.
- **Advanced threat detection** - Detect and block DNS
  tunneling attempts and Domain Generation Algorithm (DGA) patterns.
- **Real-time monitoring** - Generate alerts and logs for
  security events and policy violations.
