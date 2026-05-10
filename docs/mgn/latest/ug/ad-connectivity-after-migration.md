NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Target instance cannot connect to Active Directory after migration

When you migrate domain-joined Windows servers, the target instance may fail to
authenticate with Active Directory. This prevents login with domain credentials or access to
domain resources.

**Causes:**

- **Network connectivity** – No network path between
  the target VPC and your AD domain controllers. This requires an
  [AWS Site-to-Site
  VPN](../../../vpn/latest/s2svpn/VPC_VPN.md "../../../vpn/latest/s2svpn/VPC_VPN.md") or
  [AWS
  Direct Connect](../../../directconnect/latest/UserGuide/Welcome.md "../../../directconnect/latest/UserGuide/Welcome.md"), and security groups/ACLs must allow AD ports (TCP/UDP 389, 636, 88,
  53, 445, 135, 3268, 3269).
- **DNS resolution** – Application Migration Service resets network settings to
  DHCP during conversion. The VPC's default AmazonProvidedDNS cannot resolve on-premises AD
  domain names, so the instance cannot locate domain controllers.
  **Resolution:**

1.  **Ensure network connectivity** – Verify a network
    path exists between the target VPC and your AD domain controllers. Confirm that
    [security
    groups](../../../vpc/latest/userguide/vpc-security-groups.md "../../../vpc/latest/userguide/vpc-security-groups.md"),
    [network
    ACLs](../../../vpc/latest/userguide/vpc-network-acls.md "../../../vpc/latest/userguide/vpc-network-acls.md"), and on-premises firewalls allow AD traffic.
2.  **Configure DNS resolution** – Use one of these
    approaches:

        * *Recommended:* Create a
         [Route 53
         Resolver](../../../Route53/latest/DeveloperGuide/resolver.md "../../../Route53/latest/DeveloperGuide/resolver.md") outbound endpoint with a forwarding rule for your AD domain. This
         preserves AWS service endpoint resolution. See
         [Integrating
         DNS with Route 53 Resolvers](../../../directoryservice/latest/admin-guide/ms_ad_dns_forwarders.md "../../../directoryservice/latest/admin-guide/ms_ad_dns_forwarders.md").
        * *Alternative:* Create a
         [custom
         DHCP options set](../../../vpc/latest/userguide/VPC_DHCP_Options.md "../../../vpc/latest/userguide/VPC_DHCP_Options.md") with your AD DNS servers. Note: this may break AWS service
         endpoint resolution unless your DNS servers also forward AWS domain queries.

    Test by launching a test instance in the target VPC before performing a cutover
    migration.
