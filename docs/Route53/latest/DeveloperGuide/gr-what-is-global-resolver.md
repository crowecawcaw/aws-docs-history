# What is Route 53 Global Resolver?

Route 53 Global Resolver is an internet-reachable DNS resolver that provides easy, secure, and reliable DNS resolution for authorized clients in your organization across remote locations, branch offices, and on-premises environments. You can resolve queries for domains hosted on Amazon Route 53 private hosted zones or public domains on the internet, while maintaining high availability through global anycast architecture. Route 53 Global Resolver helps you protect your clients from DNS-based data exfiltration attacks, by filtering queries to potentially malicious domains.

Route 53 Global Resolver uses anycast IP addresses that automatically route DNS queries to the AWS Region closest to your source query location for optimal latency and availability. You can select the regions where your global resolver should provide DNS resolution from for your authorized clients, configure different views for the clients for the resolution of private and public domains, filter malicious domains, and monitor DNS activity across your organization.

###### Topics

- [Why Route 53 Global Resolver?](#gr-why-global-resolver "#gr-why-global-resolver")
- [Concepts and terminology](gr-concepts-terminology.md "gr-concepts-terminology.md")
- [How it works](gr-how-it-works.md "gr-how-it-works.md")
- [Use cases](gr-cloud-resolver-use-cases.md "gr-cloud-resolver-use-cases.md")
- [Related services](gr-related-services.md "gr-related-services.md")
- [Accessing Global Resolver](gr-accessing-cloud-resolver.md "gr-accessing-cloud-resolver.md")
- [Supported AWS Regions](#regions "#regions")
- [Setting up account access](gr-setting-up.md "gr-setting-up.md")
- [Tutorial: Create your first Route 53 Global Resolver](gr-getting-started.md "gr-getting-started.md")
- [Managing DNS views](gr-manage-dns-views.md "gr-manage-dns-views.md")
- [Managing access controls](gr-managing-access-controls.md "gr-managing-access-controls.md")
- [Securing DNS](gr-securing-dns.md "gr-securing-dns.md")
- [Configuring private hosted associations](gr-configuring-private-hosted-zone-associations.md "gr-configuring-private-hosted-zone-associations.md")
- [Monitoring DNS activity](gr-monitoring.md "gr-monitoring.md")
- [Troubleshooting DNS issues](gr-troubleshooting-dns-issues.md "gr-troubleshooting-dns-issues.md")
- [Quotas](gr-load-balancer-limits.md "gr-load-balancer-limits.md")

## Why Route 53 Global Resolver?

Route 53 Global Resolver provides centralized DNS security and filtering for remote and hybrid clients and
workloads across multiple locations. Regardless of the location of your workloads, applications, or users, Route 53 Global Resolver ensures consistent DNS protection without requiring complex
on-premises infrastructure.

Key benefits for remote and hybrid environments:

- **Simplified management** - Configure private and public domain resolution using a single solution instead of managing multiple on-premises DNS servers
- **Unified DNS security** - Apply consistent filtering policies
  across all remote clients and hybrid workloads
- **Scalable protection** - Automatically scales to handle DNS
  queries from growing remote workforces and cloud workloads
- **Reduced infrastructure** - Minimizes the need for DNS
  security appliances at each remote location

To get started, see:

- [Key concepts and components for Route 53 Global Resolver](gr-concepts-terminology.md "gr-concepts-terminology.md") - Core concepts for DNS security deployment
- [How Route 53 Global Resolver works](gr-how-it-works.md "gr-how-it-works.md") - How Route 53 Global Resolver protects remote and hybrid
  environments
- [Tutorial: Create your first Route 53 Global Resolver](gr-getting-started.md "gr-getting-started.md") - Tutorial for your first DNS filtering setup

## Supported AWS Regions

Route 53 Global Resolver is available in the
following AWS Regions:

- US East (N. Virginia) Region
- US East (Ohio) Region
- US West (N. California) Region
- US West (Oregon) Region
- Europe (Frankfurt) Region
- Europe (Ireland) Region
- Europe (London) Region
- Asia Pacific (Mumbai) Region
- Asia Pacific (Singapore) Region
- Asia Pacific (Tokyo) Region
- Asia Pacific (Sydney) Region
