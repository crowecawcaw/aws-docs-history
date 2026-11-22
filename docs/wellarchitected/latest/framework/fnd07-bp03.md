

# FND07-BP03 Establish centralized DNS management

 Centralized DNS management provides reliable name resolution across your organization through a single, governed infrastructure. Because DNS sits beneath almost every distributed system, inconsistent ownership, fragmented hosted zones, and informal changes cause disruptions and security gaps with outsized impact scope. Consolidating DNS under consistent controls, automated processes, and clear ownership keeps name resolution reliable, observable, and secure while supporting operational efficiency. 

 **Desired outcome:** 
+  Your organization has a reliable, secure, and efficient domain name infrastructure with centralized management and consistent policies. 
+  Your infrastructure provides high uptime with rapid automatic failover and consistent global performance. 
+  You maintain protected DNS infrastructure with clear governance and detailed monitoring that supports cost optimization and auditability. 

 **Common anti-patterns:** 
+  Spreading DNS management across multiple environments and failing to implement proper access controls. 
+  Implementing complex DNS configurations without proper testing environments. 
+  Creating unnecessary hosted zones, neglecting to set up DNS delegation, or failing to implement naming conventions, causing resolution issues and management complexity. 
+  Failing to account for time-to-live (TTL) when verifying that a DNS change has propagated, leading to premature rollbacks or cut-overs although resolvers still serve the old answer from cache. 
+  Setting uniformly short TTLs (under 300 seconds) on all records regardless of how often they change, which increases query load and cost without operational benefit. 
+  Neglecting to set up alerts for domain expiration or to enable auto-renewal for registered domains. 
+  Neglecting IPv6 support by only creating A records. 

 **Benefits of establishing this best practice:** 
+  Centralized DNS management provides reliable resolution across the organization while simplifying operations and reducing complexity. 
+  Health checks, automatic failover, and global distribution keep services resolvable during component and Region failures. 
+  Consistent access controls, DNS Security Extensions (DNSSEC), and DNS-layer filtering reduce the likelihood of tampering, spoofing, and exfiltration. 
+  Infrastructure-as-code deployments and automated change management reduce duplication and human error. 
+  Removing redundant hosted zones and tiering TTL values balance query costs against propagation speed. 
+  Centralized monitoring and logging expose DNS usage patterns, support troubleshooting, and help teams manage domain renewals and infrastructure health before problems surface. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 DNS issues tend to have an outsized scope of impact. With [Amazon Route 53](https://aws.amazon.com/route53/), you can manage DNS as a programmable, highly available service with version control, automated testing, and monitoring. Centralize DNS management in a dedicated network or shared services account. This approach concentrates operational ownership, keeps policy consistent, and simplifies certificate issuance. Certificate authorities can verify domain ownership through a single account's DNS records. 

 Public zones serve external clients and require DNS delegation from the parent domain to the Route 53 name servers. Private zones resolve inside your VPCs. Associate them with multiple VPCs, or with many accounts through [Route 53 Profiles](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/profiles.html), so teams do not duplicate zones per account. When the same domain name must resolve differently for internal and external clients (split-horizon DNS), use both public and private hosted zones with identical domain names. The private zone takes precedence for queries from associated VPCs, whereas external clients receive responses from the public zone. 

 For hybrid environments, [Route 53 Resolver endpoints](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver.html) bridge AWS and on-premises DNS. Inbound endpoints let on-premises DNS servers forward queries for AWS-hosted domains. Outbound endpoints let VPCs resolve on-premises domain names. Deploy these endpoints across multiple Availability Zones for resilience, and factor query charges into your hybrid DNS design. 

 [Route 53 health checks](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html) and failover routing policies keep services resolvable during component failures, whereas [Amazon Application Recovery Controller](https://aws.amazon.com/application-recovery-controller/) adds structured control for coordinated multi-Region failover. On the security side, [Route 53 Resolver DNS Firewall](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall.html) filters unwanted queries before they leave the VPC. You can enable DNSSEC on public hosted zones to prevent answer tampering. DNSSEC adds operational complexity around key management, signing operations, and chain-of-trust maintenance. Test it in non-production first, establish key rotation procedures, and monitor for signing failures, which can make domains unresolvable if not caught quickly. [IAM](https://aws.amazon.com/iam/) policies restrict who can modify zones. 

 Tier TTLs by how often records change. Use longer values (an hour or more) for stable infrastructure records, and moderate values (5 to 15 minutes) for application endpoints that shift during deployments. Reserve short values for records being cut over during a migration or failover. When a change must propagate quickly, lower the TTL ahead of time, wait out the old TTL, make the change, then restore the longer value. Create AAAA records alongside A records to support IPv6-capable clients. Use alias records on apex domains to point to AWS resources. Alias records preserve the root-level name and incur no query charges for the alias lookup. 

**Note**  
 Domain registration and DNS hosting are distinct services and can be split between providers. Keeping both services in Route 53 simplifies billing, access control, and monitoring. 

 DNS changes deserve the same discipline you apply to other infrastructure changes. Manage DNS through infrastructure as code using [AWS CloudFormation](https://aws.amazon.com/cloudformation/), [AWS CDK](https://aws.amazon.com/cdk/), or Terraform, and run changes through a CI/CD pipeline with review and staged deployment. This reduces the chance that a single bad change causes a broad disruption. Query logging, metrics, and alerts on health check status make DNS behavior visible, so you can detect problems early. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Set up a centralized services environment for DNS:** Create or use a dedicated networking or shared services account for DNS management so ownership and governance live in one place. Use [Amazon Route 53 Profiles](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/profiles.html) to apply and manage DNS-related Route 53 configurations across many VPCs and accounts without duplicating zones, and [share Route 53 Profiles through AWS RAM](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/sharing-profiles.html) to simplify cross-account distribution. 

1.  **Configure Route 53 hosted zones:** Create [public and private hosted zones](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/AboutHZWorkingWith.html) in the centralized account according to your domain plan. For public hosted zones, set up [DNS delegation](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/MigratingDNS.html) from the parent domain to the Route 53 name servers. Associate private hosted zones with multiple VPCs and use Route 53 Profiles to distribute them across accounts that need resolution. Apply a consistent naming convention and use [hosted zone tags](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/tagging-resources.html) for environment, cost center, and ownership so auditability and chargeback work without extra discovery effort. 

1.  **Establish DNS propagation handling:** Verify DNS changes using tools like dig or nslookup from multiple global vantage points so you can see propagation as clients see it. Automate propagation checks in your deployment pipeline after changes and use them as a gate before declaring a critical change complete. 

1.  **Implement health checks and failover:** Create [Route 53 health checks](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html) for critical endpoints and configure [failover routing policies](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-failover.html) that use them. For complex multi-Region failover scenarios, use [Amazon Application Recovery Controller](https://aws.amazon.com/application-recovery-controller/) to coordinate recovery across services. 

1.  **Configure Route 53 Resolver endpoints for hybrid connectivity:** For hybrid cloud architectures, deploy [Route 53 Resolver inbound endpoints](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-getting-started.html) to let on-premises DNS servers forward queries to AWS, and outbound endpoints to let VPCs resolve on-premises domain names. Deploy endpoints across multiple Availability Zones for high availability, and configure security group rules to control access. If you don't have hybrid DNS requirements, skip this step. 

1.  **Enforce least privilege access with AWS IAM:** Create [IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) with least-privilege permissions for hosted zone management so only authorized principals can change DNS. Use [AWS Organizations](https://aws.amazon.com/organizations/) and [IAM Identity Center](https://aws.amazon.com/iam/identity-center/) to share these roles with the appropriate member accounts, and apply consistent naming conventions and tags to hosted zones for ownership and auditability. 

1.  **Manage DNS records and TTLs:** Create AAAA records alongside A records to support IPv6 clients, and use [alias records](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-choosing-alias-non-alias.html) for apex domains pointing to AWS resources. Alias records also avoid query charges on the alias lookup itself. Tier TTLs to how often each record actually changes: longer values (an hour or more) for stable infrastructure, moderate values (5 to 15 minutes) for endpoints that shift during deployments, and short values only for records you are actively cutting over. For planned changes, lower the TTL in advance, wait for the old TTL to expire, make the change, verify propagation, and then restore the longer value. 

1.  **Implement DNS-layer security controls:** Deploy [Amazon Route 53 Resolver DNS Firewall](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall.html) with rule groups that return NXDOMAIN or NODATA for suspicious or disallowed domains. Enable [DNSSEC signing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-configuring-dnssec.html) for public hosted zones where required and associate appropriate rule groups with each VPC. 

1.  **Automate domain registration management:** Enable auto-renew for all registered domains in [Route 53 domain registration](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar.html), set up billing alerts for domain renewal charges, and review domain registration information annually. 

1.  **Manage DNS changes through infrastructure as code:** Manage DNS through infrastructure as code using [AWS CloudFormation](https://aws.amazon.com/cloudformation/), [AWS CDK](https://aws.amazon.com/cdk/), or Terraform, and run changes through a CI/CD pipeline with appropriate approvals and staged rollout. 

1.  **Enable monitoring and logging:** Enable [Route 53 query logging](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/query-logs.html) for public hosted zones and [Resolver query logging](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-query-logs.html) for VPC queries. Use [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) metrics for query volumes, latency, and [health check status](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/monitoring-health-checks.html), and create CloudWatch alarms for critical DNS events such as health check failures or unusual query patterns. Build a dashboard that gives DNS operations visibility in one place. Query logging incurs CloudWatch Logs ingestion and storage charges, so use sampling, filtering, or shorter retention periods in high-traffic environments to balance observability with cost. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [FND07-BP01 Define your network and connectivity strategy and centralized resources](fnd07-bp01.md) 
+  [FND07-BP02 Implement centralized network protection controls](fnd07-bp02.md) 
+  [FND04-BP07 Establish cross-Region replication and failover capabilities](fnd04-bp07.md) 

 **Related documents:** 
+  [Network account in the Infrastructure OU](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/foundational-ous.html) 
+  [Using Amazon Route 53 Profiles for scalable multi-account AWS environments](https://aws.amazon.com/blogs/networking-and-content-delivery/using-amazon-route-53-profiles-for-scalable-multi-account-aws-environments/) 
+  [DNS best practices for Amazon Route 53](https://aws.amazon.com/blogs/networking-and-content-delivery/dns-best-practices-for-amazon-route-53/) 
+  [SSL and TLS Deployment Best Practices](https://github.com/ssllabs/research/wiki/ssl-and-tls-deployment-best-practices) 
+  [Migrating your multi-account DNS environment to Amazon Route 53 Profiles](https://aws.amazon.com/blogs/networking-and-content-delivery/migrating-your-multi-account-dns-environment-to-amazon-route-53-profiles/) 
+  [Best practices for Amazon Route 53 DNS](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/best-practices-dns.html) 
+  [Construct DNS set up for applications](https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/construct-dns-set-up-applications.html) 
+  [How to achieve DNS high availability with Route 53 Resolver endpoints](https://aws.amazon.com/blogs/networking-and-content-delivery/how-to-achieve-dns-high-availability-with-route-53-resolver-endpoints/) 
+  [DNS domain name format](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DomainNameFormat.html) 
+  [What are Amazon Route 53 Profiles?](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/profiles.html) 
+  [Resolving DNS queries between VPCs and your network](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver.html) 
+  [Considerations when working with DNSSEC signing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-configuring-dnssec.html#dns-configuring-dnssec-considerations) 