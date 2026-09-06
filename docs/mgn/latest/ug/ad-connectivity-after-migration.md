

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Target instance cannot connect to Active Directory after migration
<a name="ad-connectivity-after-migration"></a>

When you migrate domain-joined Windows servers, the target instance may fail to authenticate with Active Directory. This prevents login with domain credentials or access to domain resources.

**Causes:**
+ **Network connectivity** – No network path between the target VPC and your AD domain controllers. This requires an [AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html) or [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html), and security groups/ACLs must allow AD ports (TCP/UDP 389, 636, 88, 53, 445, 135, 3268, 3269).
+ **DNS resolution** – MGN resets network settings to DHCP during conversion. The VPC's default AmazonProvidedDNS cannot resolve on-premises AD domain names, so the instance cannot locate domain controllers.

**Resolution:**

1. **Ensure network connectivity** – Verify a network path exists between the target VPC and your AD domain controllers. Confirm that [security groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html), [network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html), and on-premises firewalls allow AD traffic.

1. **Configure DNS resolution** – Use one of these approaches:
   + *Recommended:* Create a [Route 53 Resolver](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver.html) outbound endpoint with a forwarding rule for your AD domain. This preserves AWS service endpoint resolution. See [Integrating DNS with Route 53 Resolvers](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_dns_forwarders.html).
   + *Alternative:* Create a [custom DHCP options set](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_DHCP_Options.html) with your AD DNS servers. Note: this may break AWS service endpoint resolution unless your DNS servers also forward AWS domain queries.

Test by launching a test instance in the target VPC before performing a cutover migration.