# Best practices for VPC Resolver

This section provides best practices for optimizing Amazon Route 53 VPC Resolver, covering the following topics:

1.  **Avoiding Loop Configurations with Resolver Endpoints:**

        * Prevent routing loops by ensuring that the same VPC is not associated with both a Resolver rule and its inbound endpoint.
        * Utilize AWS RAM to share VPCs across accounts while maintaining proper routing configurations.

    For more information, see [Avoid loop configurations with
    Resolver endpoints](best-practices-resolver-endpoints.md "best-practices-resolver-endpoints.md")

2.  **Scaling Resolver endpoints:**

        * Implement security group rules that permit traffic based on connection state to reduce connection tracking overhead
        * Follow recommended security group rules for inbound and outbound Resolver endpoints to maximize query throughput.
        * Monitor unique IP address and port combinations generating DNS traffic to avoid capacity limitations.

    For more information, see [Resolver endpoint
    scaling](best-practices-resolver-endpoint-scaling.md "best-practices-resolver-endpoint-scaling.md")

3.  **High availability for Resolver endpoints:**

        * Create inbound endpoints with IP addresses in at least two Availability Zones for redundancy.
        * Provision additional network interfaces to ensure availability during maintenance or traffic surges

    For more information, see [High
    availability for Resolver endpoints](best-practices-resolver-endpoint-high-availability.md "best-practices-resolver-endpoint-high-availability.md")

4.  **Preventing DNS zone walking attacks:**

        * Be aware of potential DNS zone walking attacks, where attackers attempt to retrieve all content from DNSSEC-signed DNS zones.
        * If your endpoints experience throttling due to suspected zone walking, contact AWS Support for assistance.

    For more information, see [DNS zone walking](best-practices-resolver-zone-walking.md "best-practices-resolver-zone-walking.md")
    By following these best practices, you can optimize the performance, scalability, and security of your VPC Resolver deployments, ensuring reliable
    and efficient DNS resolution for your applications and resources.
