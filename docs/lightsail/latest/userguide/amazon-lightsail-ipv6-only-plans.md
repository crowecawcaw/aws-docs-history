

# Configure IPv6-only networking for Lightsail instances
<a name="amazon-lightsail-ipv6-only-plans"></a>

Lightsail instances support two types of networking—*dual-stack networking* (IPv4 and IPv6) and *IPv6-only networking*. With dual-stack networking, your instance is assigned a public IPv4 and a public IPv6 address. For instances with dual-stack networking, you can enable or disable IPv6 as needed.

With IPv6-only networking, your instance is assigned a public IPv6 address and doesn't support public IPv4 traffic. Not all Lightsail blueprints are compatible with IPv6. To learn which blueprints support IPv6-only, see [IPv6 compatible blueprints](ipv6-only-blueprints.md).

Use IPv6-only networking if you don’t require a public IPv4 address. But first, make sure that your local network, computer, devices, and end-users can communicate using IPv6. For more information, see IPv6 reachability in [Verify IPv6 reachability for Lightsail instances](amazon-lightsail-ipv6-reachability.md).

For existing instances with supported blueprints, you can change the networking type between dual-stack networking and IPv6-only networking. To review the considerations of IPv6-only networking and make changes to existing instances, see [Switch instance networking type to IPv6 or dual-stack in Lightsail](migrate-to-ipv6-only-plan.md).

**Topics**
+ [Switch instance networking type to IPv6 or dual-stack in Lightsail](migrate-to-ipv6-only-plan.md)
+ [IPv6 compatible blueprints](ipv6-only-blueprints.md)