# Best practices for Amazon Route 53

This section provides best practices for various components of Amazon Route 53, including:

1. **DNS best practices:**
   - Understand the trade-offs between time to live (TTL) values and responsiveness versus reliability.
   - Use alias records instead of CNAME records when possible for improved performance and cost savings.
   - Configure default routing policies to ensure all clients receive a response.
   - Leverage latency-based routing for minimizing application latency and geolocation/geoproximity routing for stability and predictability.
   - Verify change propagation using the `GetChange` API for automated workflows.
   - Delegate subdomains from the parent zone for consistent routing.
   - Avoid large single responses by using multivalue answer routing.

2. **Resolver best practices:**
   - Prevent routing loops by avoiding associating the same VPC with both a Resolver rule and its inbound endpoint.
   - Implement security group rules to reduce connection tracking overhead and maximize query throughput.
   - Configure inbound endpoints with IP addresses in multiple Availability Zones for redundancy.
   - Be aware of potential DNS zone walking attacks and contact AWS Support if your endpoints experience throttling.

3. **Health checks best practices:**
   - Follow recommendations for optimizing Amazon Route 53 health checks to ensure reliable monitoring of your resources
     By adhering to these best practices, you can optimize the performance, reliability, and security of your DNS infrastructure,
     ensuring efficient and effective routing of traffic to your applications and services

###### Topics

- [Best practices for Amazon Route 53 DNS](best-practices-dns.md "best-practices-dns.md")
- [Best practices for Resolver](best-practices-resolver.md "best-practices-resolver.md")
- [Best practices for Amazon Route 53 health checks](best-practices-healthchecks.md "best-practices-healthchecks.md")
