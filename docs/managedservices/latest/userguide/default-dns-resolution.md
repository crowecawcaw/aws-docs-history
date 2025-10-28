# DNS resolution defaults (MALZ)

AWS Managed Services (AMS) multi-account landing zone: In AWS environments, domain name system (DNS) resolution between Route 53 Resolver and DNS resolvers in a VPC can be integrated
by configuring Resolver forwarding rules. Before these rules can be used for forwarding DNS queries, inbound
and outbound resolver endpoints need to be set up to which these queries can be forwarded.

By default, DNS queries within application account VPCs in multi-account settings in AMS are forwarded to
the conditional forwarders of the AWS Directory Service for Microsoft Active Directory (also known as Managed AD)
domain present in the shared services account. AMS optionally enables you to make use of the AmazonProvidedDNS;
for example, AmazonProvidedDNS to forward DNS queries to. This helps you utilize VPC endpoints that today only
support Amazon-provided DNS through Amazon Route 53. Correspondingly, Resolver Rules are also automatically set
up for common VPC endpoints that are deployed by default in the shared services account. For more information
on these common VPC endpoints, see [AMS VPC endpoints](ams-endpoints.md "ams-endpoints.md").

To configure Dynamic Host Configuration Protocol (DHCP) Option Sets in all of your application account VPCs to use
Amazon-provided DNS for VPC endpoints, and have Route53 Resolver rules pointing to the common VPC endpoints in
your shared services accounts (with an optional Resolver Rule for on-premises domain), create a Management | Other |
Other | Create request for change (RFC) specifying the shared services account, and requesting enablement of
the application account VPC local DNS and Route 53 Resolver rules for VPC endpoints.
