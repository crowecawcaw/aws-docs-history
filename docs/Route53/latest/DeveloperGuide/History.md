# Document history

The following entries describe important changes in each release of the Route 53 documentation.
For notification about updates to this documentation, you can subscribe to an RSS feed.

###### Topics

- [2025 releases](#doc-history-2025 "#doc-history-2025")
- [2024 releases](#doc-history-2024 "#doc-history-2024")
- [2023 releases](#doc-history-2023 "#doc-history-2023")
- [2022 releases](#doc-history-2022 "#doc-history-2022")
- [2021 releases](#doc-history-2021 "#doc-history-2021")
- [2020 releases](#doc-history-2020 "#doc-history-2020")
- [2018 releases](#doc-history-2018 "#doc-history-2018")
- [2017 releases](#doc-history-2017 "#doc-history-2017")
- [2016 releases](#doc-history-2016 "#doc-history-2016")
- [2015 releases](#doc-history-2015 "#doc-history-2015")
- [2014 releases](#doc-history-2014 "#doc-history-2014")
- [2013 releases](#doc-history-2013 "#doc-history-2013")
- [2012 release](#doc-history-2012 "#doc-history-2012")
- [2011 releases](#doc-history-2011 "#doc-history-2011")
- [2010 release](#doc-history-2010 "#doc-history-2010")

## 2025 releases

**June 26, 2025**
Added `ResolverEndpointCapacityStatus` to the `AWS/Route53Resolver` namespace.
For more information, see [Metrics for Resolver endpoints](monitoring-resolver-with-cloudwatch.md#cloudwatch-metrics-resolver-endpoint "monitoring-resolver-with-cloudwatch.md#cloudwatch-metrics-resolver-endpoint").

**June 25, 2025**
Amazon Route 53 now supports alias records for VPC Lattice service
custom domain endpoints. For more information,
see [Routing traffic to Amazon VPC Lattice service domain endpoint](routing-to-vpc-lattice-service.md "routing-to-vpc-lattice-service.md").

**June 24, 2025**
You can now use inbound and outbound delegation with VPC Resolver.
For more information, see [How DNS resolvers on your network
forward DNS queries to Resolver endpoints](resolver-overview-forward-network-to-vpc.md "resolver-overview-forward-network-to-vpc.md").

**June 01, 2025**
Added permissions for `cloudwatch:GetMetricData` ,`tag:GetResources`, `es:ListDomainNames`,
`es:DescribeDomains`, `cloudfront:GetDistributionTenantByDomain`, `cloudfront:GetConnectionGroup` and `lightsail:GetContainerServices`. These permissions enable you to
fetch up to 500 CloudWatch health check metrics, up to 100 names of health checks, get the domain configuration for the specified Amazon OpenSearch Service domains, and
list the names of all Amazon OpenSearch Service domains owned by the current user in the active Region, fetch the CloudFront multi-tenant distributions and get the Lightsail container services.
For more information, see [AWS managed policy:
AmazonRoute53FullAccess](security-iam-awsmanpol-route53.md#security-iam-awsmanpol-AmazonRoute53FullAccess "security-iam-awsmanpol-route53.md#security-iam-awsmanpol-AmazonRoute53FullAccess").

**April 28, 2025**
You can now associate interface VPC endpoints to Route 53 Profiles.
For more information, see [Associate interface VPC endpoints
to a Route 53 Profile](profile-associate-vpc-endpoints.md "profile-associate-vpc-endpoints.md").

**April 28, 2025**
You can now add an alias record to a CloudFront distribution tenant.
For more information, see [Routing traffic to an Amazon CloudFront
distribution by using your domain name](routing-to-cloudfront-distribution.md "routing-to-cloudfront-distribution.md").

**February 27, 2025**
Updated the Route 53 guide with the new console experience for Traffic Flow.
For more information, see [Creating and managing traffic policies](traffic-policies.md "traffic-policies.md") and [Creating and managing policy records](traffic-policy-records.md "traffic-policy-records.md").

**January 14, 2025**
Amazon Route 53 now supports alias records for OpenSearch Service custom domain endpoints. For more information,
see [Routing traffic to Amazon OpenSearch Service domain endpoint](routing-to-open-search-service.md "routing-to-open-search-service.md").

**January 13, 2025**
Added Resolver DNS Firewall findings to the Security Hub CSPM. For more information, see [Sending findings from Resolver DNS Firewall to Security Hub CSPM](securityhub-integration.md "securityhub-integration.md").

## 2024 releases

**November 15, 2024**
Added Resolver DNS Firewall Advanced, a new set of features on Resolver DNS Firewall that allows you to identify and block DNS traffic associated with advanced DNS threats,
such as DNS tunneling, Domain Generation Algorithm (DGA), and Dictionary DGA based threats.
For more information, see [Resolver DNS Firewall Advanced](firewall-advanced.md "firewall-advanced.md").

**October 29, 2024**
Added support for HTTPS, SSHFP, SVCB, and TLSA DNS record types.
For more information, see [Supported DNS record types](ResourceRecordTypes.md "ResourceRecordTypes.md").

**October 3, 2024**
Added support for Service Name Indication (SNI) for DoH outbound Resolver endpoints.
For more information, see [Values that you specify when you create or edit rules](resolver-forwarding-outbound-queries-rule-values.md "resolver-forwarding-outbound-queries-rule-values.md").

**September 3, 2024**
You can now use `route53:VPCs` policy condition to grant fine-grained access to managing
hosted zone associations to VPCs. For more information, see [Using IAM policy conditions for
fine-grained access control](specifying-conditions-route53.md "specifying-conditions-route53.md").

**August 27, 2024**
`AmazonRoute53ProfilesFullAccess` added permissions for
`GetProfilePolicy` and `PutProfilePolicy`. These are permission-only IAM actions. If an IAM principal doesn't have these permissions granted,
an error will occur when attempting to share the Profile using the AWS RAM service. For more information, see [AWS managed policy: AmazonRoute53ProfilesFullAccess](security-iam-awsmanpol-route53.md#security-iam-awsmanpol-AmazonRoute53ProfilesFullAccess "security-iam-awsmanpol-route53.md#security-iam-awsmanpol-AmazonRoute53ProfilesFullAccess").

**August 27, 2024**
`AmazonRoute53ProfilesReadOnlyAccess` added permission for
`GetProfilePolicy`. This is a permission-only IAM action. If an IAM principal doesn't have this permission
granted, an error will occur when attempting to access the Profile's policy using the AWS RAM service. For more information, see [AWS managed policy: AmazonRoute53ProfilesReadOnlyAccess](security-iam-awsmanpol-route53.md#security-iam-awsmanpol-AmazonRoute53ProfilesReadOnlyAccess "security-iam-awsmanpol-route53.md#security-iam-awsmanpol-AmazonRoute53ProfilesReadOnlyAccess").

**August 5, 2024**
Added a statement id (Sid) to uniquely identity the managed policy `AmazonRoute53ResolverFullAccess`. For more information, see [AWS managed policy: AmazonRoute53ResolverFullAccess](security-iam-awsmanpol-route53.md#security-iam-awsmanpol-AmazonRoute53ResolverFullAccess "security-iam-awsmanpol-route53.md#security-iam-awsmanpol-AmazonRoute53ResolverFullAccess").

**August 5, 2024**
Added a statement id (Sid) to uniquely identity the managed policy `AmazonRoute53ResolverReadOnlyAccess`. For more information, see [AWS managed policy: AmazonRoute53ResolverReadOnlyAccess](security-iam-awsmanpol-route53.md#security-iam-awsmanpol-AmazonRoute53ResolverReadOnlyAccess "security-iam-awsmanpol-route53.md#security-iam-awsmanpol-AmazonRoute53ResolverReadOnlyAccess").

**July 18, 2024**
Updated the entire Route 53 guide with the new console experience for health checks.
For more information, see [Creating, updating, and deleting
health checks](health-checks-creating-deleting.md "health-checks-creating-deleting.md").

**April 30, 2024**
You can now decide if a DNS Firewall rule will either inspect (default), or trust the DNS redirection chain. For more information, see
[Resolver DNS Firewall components and
settings](resolver-dns-firewall-overview.md#resolver-dns-firewall-components "resolver-dns-firewall-overview.md#resolver-dns-firewall-components") and [Rule settings in
DNS Firewall](resolver-dns-firewall-rule-settings.md "resolver-dns-firewall-rule-settings.md").

**April 22, 2024**
You can now use Route 53 Profiles to share DNS-specific configurations with many VPCs and with AWS acounts. For more information, see
[What are Amazon Route 53 Profiles?](profiles.md "profiles.md").

**April 22, 2024**
Added the managed policies `AmazonRoute53ProfilesReadOnlyAccess` and
`AmazonRoute53ProfilesFullAccess` to grant read-only and full
access to Amazon Route 53 Profiles. For more information, see [AWS managed policies for Amazon Route 53](security-iam-awsmanpol-route53.md "security-iam-awsmanpol-route53.md").

**February 5, 2024**
You can now use Amazon EventBridge for real time alerts with DNS Firewall. For more information, see
[Managing Resolver DNS Firewall events using Amazon EventBridge](dns-firewall-eventbridge-integration.md "dns-firewall-eventbridge-integration.md").

**January 9, 2024**
You can now use the DNS query type as an optional value for DNS Firewall rule to differentiate the
rule's response for a specific DNS query type. For more information, see
[Resolver DNS Firewall components and
settings](resolver-dns-firewall-overview.md#resolver-dns-firewall-components "resolver-dns-firewall-overview.md#resolver-dns-firewall-components") and [Rule settings in
DNS Firewall](resolver-dns-firewall-rule-settings.md "resolver-dns-firewall-rule-settings.md").

**January 9, 2024**
You can now use the Quick create record or the Create record wizard to create geoproximity routing records. For more information, see
[Geoproximity routing](routing-policy-geoproximity.md "routing-policy-geoproximity.md"), [Values specific for geoproximity
records](resource-record-sets-values-geoprox.md "resource-record-sets-values-geoprox.md"), and [Values specific for geoproximity
alias records](resource-record-sets-values-geoprox-alias.md "resource-record-sets-values-geoprox-alias.md").

## 2023 releases

**December 20, 2023**
You can now use DNS over HTTPS with Resolver endpoints.
For more information, see [Choosing protocols for the endpoints](resolver-choose-vpc.md#resolver-endpoint-protocol-considerations "resolver-choose-vpc.md#resolver-endpoint-protocol-considerations").

**July 20, 2023**
Amazon Route 53 on Outposts is now available on AWS Outposts racks. It includes a VPC Resolver that caches all DNS queries that originate from the AWS Outposts.
You can also set up hybrid connectivity between an Outpost and an on-premises DNS resolver when you deploy
inbound and outbound endpoints.
For more information, see [What is Amazon Route 53 on Outposts?](outpost-resolver.md "outpost-resolver.md").

**July 19, 2023**
You can now use Local Zones with geoproximity routing (traffic flow only) after you enable them.
For more information, see [Geoproximity routing](routing-policy-geoproximity.md "routing-policy-geoproximity.md") and
[Traffic Policy Document Format](../APIReference/api-policies-traffic-policy-document-format.md "../APIReference/api-policies-traffic-policy-document-format.md").

**March 22, 2023**
Updated the entire Route 53 guide with the new console experience for domains. You can also
use the new console experience to transfer a domain from one AWS account to another AWS account.
For more information, see [Registering a new domain](domain-register.md "domain-register.md") and [Transferring domains](domain-transfer.md "domain-transfer.md").

**March 10, 2023**
You can now connect to your resources by using IPv4, IPv6, or dual-stack endpoints with
Route 53 VPC Resolver. For more information, see [Values that you specify when you create or edit inbound endpoints](resolver-forwarding-inbound-queries-values.md "resolver-forwarding-inbound-queries-values.md") and [Values that you specify when you create or edit
outbound endpoints](resolver-forwarding-outbound-queries-endpoint-values.md "resolver-forwarding-outbound-queries-endpoint-values.md").

## 2022 releases

**September 21, 2022**
You can now use policy conditions for giving users fine-grained access to updating resource
record sets in Amazon Route 53. For more information, see [Using IAM policy conditions for
fine-grained access control](specifying-conditions-route53.md "specifying-conditions-route53.md").

**August 30, 2022**
Amazon Route 53 now supports alias records for AWS App Runner services that are created after
August 1, 2022. For more information, see [Routing traffic to an AWS App Runner service](routing-to-app-runner.md "routing-to-app-runner.md").

**June 1, 2022**
IP-based routing option is now available in Amazon Route 53. For more information, see [IP-based routing](routing-policy-ipbased.md "routing-policy-ipbased.md").

**March 16, 2022**
Geolocation and latency-based routing options are now supported for private hosted zones in Amazon Route 53.
For more information, see [Considerations when working with a private hosted zone](hosted-zone-private-considerations.md "hosted-zone-private-considerations.md").

**January 25, 2022**
The process for changing ownership for .com.au and .net.au TLDs has been simplified to include
responding to two emails (by both old and new registrants) and doesn't
include filling in forms. For more information, see [.com.au (Australia)](com.md "com.md") and [.net.au (Australia)](net.md "net.md").

## 2021 releases

**October 26, 2021**
Added support for disabling default reverse DNS rules with Amazon Route 53. You can now disable the
creation of these rules and instead forward queries for reverse DNS
namespaces to external servers if desired. For more information, see [Forwarding rules for
reverse DNS queries in VPC Resolver](resolver-rules-managing.md#resolver-automatic-forwarding-rules-reverse-dns "resolver-rules-managing.md#resolver-automatic-forwarding-rules-reverse-dns").

**September 1, 2021**
Added a new getting started topic that walks you through creating Amazon CloudFront distributions for
a static website. For more information, see [Use an Amazon CloudFront distribution to serve
a static website](getting-started-cloudfront-overview.md "getting-started-cloudfront-overview.md").

**July 14, 2021**
Started tracking AWS managed policies for Amazon Route 53.
For more information, see [AWS managed policies for Amazon Route 53](security-iam-awsmanpol-route53.md "security-iam-awsmanpol-route53.md").

**March 31, 2021**
Added Resolver DNS Firewall. With DNS Firewall you can provide protection for outbound DNS requests from your VPCs.
For more information, see [Using DNS Firewall to filter outbound DNS traffic](resolver-dns-firewall.md "resolver-dns-firewall.md").

## 2020 releases

**December 17, 2020**
Added support for DNSSEC signing for Route 53 VPC Resolver. For more information, see [Configuring DNSSEC signing in Amazon Route 53](dns-configuring-dnssec.md "dns-configuring-dnssec.md").

Added support for DNSSEC validation for Route 53 VPC Resolver. For more information, see [Enabling DNSSEC validation in
Amazon Route 53](resolver-dnssec-validation.md "resolver-dnssec-validation.md").

**September 23, 2020**
Updated the entire Route 53 guide with the new console experience. For more information, see [What is Amazon Route 53?](Welcome.md "Welcome.md").

**September 1, 2020**
Added support for Resolver query logs. For more information, see [Resolver query logging](resolver-query-logs.md "resolver-query-logs.md").

## 2018 releases

**December 20, 2018**
You can create Route 53 alias records that route traffic to API Gateway APIs or to Amazon VPC interface endpoints.
For more information, see [Value/route traffic to](resource-record-sets-values-alias.md#rrsets-values-alias-alias-target "resource-record-sets-values-alias.md#rrsets-values-alias-alias-target").

**November 28, 2018**
Route 53 Auto Naming (also known as Service Discovery) is now a separate service, AWS Cloud Map. For more information, see the
[AWS Cloud Map Developer Guide](../../../cloud-map/latest/dg.md "../../../cloud-map/latest/dg.md").

**November 19, 2018**
You can use Route 53 Resolver to configure DNS resolution between your VPC and your network over a Direct Connect or VPN connection.
(Resolver is the new name for the recursive DNS service that is provided to all customers by default in Amazon Virtual Private Cloud (Amazon VPC).)
This lets you forward DNS queries from resolvers on your network to Route 53 Resolver. Resolver also lets you forward queries for
selected domain names (example.com) and subdomain names (api.example.com) from a VPC to resolvers on your network. For more information, see
[What is Route 53 VPC Resolver?](resolver.md "resolver.md").

**November 7, 2018**
When you're using Route 53 traffic flow and geoproximity routing, you can use an interactive map to visualize how your end users
will be routed to your endpoints around the world. For more information, see
[Viewing a map that shows the effect of geoproximity settings](traffic-policies.md#traffic-flow-geoproximity-map "traffic-policies.md#traffic-flow-geoproximity-map").

**October 18, 2018**
You can use the Route 53 console and API to temporarily disable a Route 53 health check. This gives you an easy way
to pause monitoring of an endpoint, such a web server, so that you can perform maintenance on it without triggering alarms or
generating unnecessary logs or status messages. For more information, see "Disabled" in
[Values that you specify when you
create or update health checks](health-checks-creating-values.md "health-checks-creating-values.md").
The feature is available for all three types of Route 53 health checks: health checks that monitor an endpoint, health checks
that monitor other health checks, and health checks that monitor a CloudWatch alarm.

**March 13, 2018**
If you're using auto naming, you can now use a third-party health checker to evaluate the health of your resources.
This is useful when a resource isn't available over the internet, for example, because the instance is in an Amazon VPC.
For more information, see [HealthCheckCustomConfig](../../../cloud-map/latest/api/API_HealthCheckCustomConfig.md "../../../cloud-map/latest/api/API_HealthCheckCustomConfig.md") in the
_Amazon Route 53 API Reference_.

**March 9, 2018**
IAM now includes managed policies for auto naming. For more information, see
[AWS managed policies for Amazon Route 53](security-iam-awsmanpol-route53.md "security-iam-awsmanpol-route53.md").

**February 6, 2018**
You can now configure auto naming to create alias records that route traffic to ELB load balancers or to create
CNAME records. For more information, see
[Attributes](../../../cloud-map/latest/api/API_RegisterInstance.md#cloudmap-RegisterInstance-request-Attributes "../../../cloud-map/latest/api/API_RegisterInstance.md#cloudmap-RegisterInstance-request-Attributes")
in the documentation for the [RegisterInstance](../APIReference/API_autonaming_RegisterInstance.md "../APIReference/API_autonaming_RegisterInstance.md") API in the
_Amazon Route 53 API Reference_.

## 2017 releases

**December 5, 2017**
You can now use the Route 53 autonaming API to provision instances for microservices.
Autonaming lets you automatically create DNS records and, optionally, health checks based on a template that you define.
For more information, see [What is AWS Cloud Map?](../../../cloud-map/latest/dg.md "../../../cloud-map/latest/dg.md") in the
_AWS Cloud Map Developer Guide_.

**November 16, 2017**
You can now programmatically get both the current quotas on Route 53 resources such as hosted zones and health checks,
and the number of each resource that you're currently using. For more information, see
[GetAccountLimit](../APIReference/API_GetAccountLimit.md "../APIReference/API_GetAccountLimit.md"),
[GetHostedZoneLimit](../APIReference/API_GetHostedZoneLimit.md "../APIReference/API_GetHostedZoneLimit.md"), and
[GetReusableDelegationSetLimit](../APIReference/API_GetReusableDelegationSetLimit.md "../APIReference/API_GetReusableDelegationSetLimit.md")
in the _Amazon Route 53 API Reference_.

**October 3, 2017**
Route 53 is now a HIPAA eligible service. For more information, see
[Compliance validation for Amazon Route 53](route-53-compliance.md "route-53-compliance.md").

**September 29, 2017**
You can now programmatically check whether a domain can be transferred to Route 53. For more information, see
[CheckDomainTransferability](../APIReference/API_domains_CheckDomainTransferability.md "../APIReference/API_domains_CheckDomainTransferability.md") in the
_Amazon Route 53 API Reference_.

**September 11, 2017**
You can now create Route 53 alias records that route internet traffic to ELB Network Load Balancers.
For more information about alias records, see
[Choosing between alias and non-alias records](resource-record-sets-choosing-alias-non-alias.md "resource-record-sets-choosing-alias-non-alias.md").

**September 7, 2017**
If you're using Route 53 as your public, authoritative DNS service, you can now log DNS queries that Route 53 receives.
For more information, see [Public DNS query logging](query-logs.md "query-logs.md").

**September 1, 2017**
If you're using Route 53 traffic flow, you can now use geoproximity routing, which lets you route traffic
based on the physical distance between your users and your resources. You can also route more or less traffic to
each resource by specifying a positive or negative bias. For more information, see
[Geoproximity routing](routing-policy-geoproximity.md "routing-policy-geoproximity.md").

**August 21, 2017**
You can now use Route 53 to create Certification Authority Authorization (CAA) records, which let you
specify the certificate authorities that can issue certificates for your domains and subdomains. For more information,
see [CAA record type](ResourceRecordTypes.md#CAAFormat "ResourceRecordTypes.md#CAAFormat").

**August 18, 2017**
You can now transfer large numbers of domains to Route 53 using the Route 53 console. For more information, see
[Transferring registration for a domain to
Amazon Route 53](domain-transfer-to-route-53.md "domain-transfer-to-route-53.md").

**August 4, 2017**
When you register a domain, the registries for some top-level domains (TLDs) require you to verify that you
specified a valid email address for the registrant contact. You can now send the verification email and get confirmation
that you successfully verified the email address during the domain registration process. For more information, see
[Registering a new domain](domain-register.md "domain-register.md").

**June 21, 2017**
If you want to route traffic approximately randomly to multiple resources, such as web servers, you can now
create one multivalue answer record for each resource and, optionally, associate a Route 53 health check with each record.
Route 53 responds to DNS queries with up to eight healthy records in response to each DNS query, and gives different answers
to different DNS resolvers. For more information, see
[Multivalue answer routing](routing-policy-multivalue.md "routing-policy-multivalue.md").

**April 10, 2017**
When you use the Route 53 console to transfer a domain registration to Route 53, you can now choose
one of the following options for associating the name servers for the DNS service for the domain with the
transferred domain registration:

- Use the name servers for a Route 53 hosted zone that you choose
- Use the name servers for the current DNS service for the domain
- Use name servers that you specify

Route 53 automatically associates these name servers with the transferred domain registration.

## 2016 releases

**November 21, 2016**

You can now create health checks that use IPv6 addresses to check the health of endpoints. For more information, see
[Creating and updating health checks](health-checks-creating.md "health-checks-creating.md").

**November 15, 2016**

You can now use a Route 53 API action to associate an Amazon VPC that you created with one account with a private hosted zone
that you created with another account. For more information, see
[Associating an Amazon VPC and a private hosted zone
that you created with different AWS accounts](hosted-zone-private-associate-vpcs-different-accounts.md "hosted-zone-private-associate-vpcs-different-accounts.md").

**August 30, 2016**

With this release, Route 53 adds the following new features:

- **Name Authority Pointer (NAPTR) records** –
  You can now create NAPTR records, which are used by Dynamic Delegation Discovery System (DDDS) applications
  to convert one value to another or to replace one value with another. For example, one common use is to convert phone numbers
  into SIP URIs. For more information, see [NAPTR record type](ResourceRecordTypes.md#NAPTRFormat "ResourceRecordTypes.md#NAPTRFormat").
- **DNS query test tool** –
  You can now simulate DNS queries for a record and see the value that Route 53 returns. For geolocation and
  latency records, you can also simulate requests from a particular DNS resolver and/or client IP address
  to find out what response Route 53 would return to a client with that resolver and/or IP address. For more information, see
  [Checking DNS responses from Route 53](dns-test.md "dns-test.md").

**August 11, 2016**

With this release, you can create alias records that route traffic to ELB Application Load Balancers.
The process is the same as for Classic Load Balancers. For more information, see
[Value/route traffic to](resource-record-sets-values-alias.md#rrsets-values-alias-alias-target "resource-record-sets-values-alias.md#rrsets-values-alias-alias-target").

**August 9, 2016**

With this release, Route 53 adds support for DNSSEC for domain registration. DNSSEC lets you protect your domain from
DNS spoofing attacks, which are also known as man-in-the-middle attacks. For more information, see
[Configuring DNSSEC for a domain](domain-configure-dnssec.md "domain-configure-dnssec.md").

**July 7, 2016**

You can now manually extend the registration for a domain and register a domain with an initial registration period
longer than the minimum registration period specified by the registry. For more information, see
[Extending the registration period for a domain](domain-extend.md "domain-extend.md").

**July 6, 2016**

If you're an AISPL customer with a contact address in India, you can now use Route 53 to register domains. For more information, see
[Managing an Account in India](../../../awsaccountbilling/latest/aboutv2/manage-account-payment-aispl.md "../../../awsaccountbilling/latest/aboutv2/manage-account-payment-aispl.md").

**May 26, 2016**

With this release, Route 53 adds the following new features:

- **Domain billing report** – You can now download a report that lists
  all domain registration charges, by domain, for a specified time period. The report includes all domain registration operations
  for which there is a fee, including registering domains, transferring domains to Route 53, renewing domain registration, and
  (for some TLDs), changing the owner of a domain. For more information, see the following documentation:
  - **Route 53 console** – See
    [Downloading a domain billing report](domain-billing-report.md "domain-billing-report.md")
  - **Route 53 API** – See
    [ViewBilling](../APIReference/API_ViewBilling.md "../APIReference/API_ViewBilling.md") in the _Amazon Route 53 API Reference_.

- **New TLDs** – You can now register domains that have the following TLDs:
  .college, .consulting, .host, .name, .online, .republican, .rocks, .sucks, .trade, .website, and .uk. For more information,
  see [Domains that you can register with Amazon Route 53](registrar-tld-list.md "registrar-tld-list.md").
- **New APIs for domain registration** – For operations that require confirmation
  that the email address for the registrant contact is valid, such as registering a new domain, you can now programmatically
  determine whether the registrant contact has clicked the link in the confirmation email and, if not, whether the link is
  still valid. You can also programmatically request that we send another confirmation email. For more information,
  see the following documentation in the _Amazon Route 53 API Reference_:
  - [GetContactReachabilityStatus](../APIReference/API_GetContactReachabilityStatus.md "../APIReference/API_GetContactReachabilityStatus.md")
  - [ResendContactReachabilityEmail](../APIReference/API_ResendContactReachabilityEmail.md "../APIReference/API_ResendContactReachabilityEmail.md")

**April 5, 2016**

With this release, Route 53 adds the following new features:

- **Health checks based on CloudWatch metrics** – You can now create
  health checks that are based on the alarm state of any CloudWatch metric. This is useful for checking the health of endpoints
  that can't be reached by a standard Route 53 health check, such as instances within an Amazon Virtual Private Cloud (VPC) that have only
  private IP addresses. For more information, see the following documentation:
  - **Route 53 console** – See
    [Monitoring a CloudWatch
    alarm](health-checks-creating-values.md#health-checks-creating-values-cloudwatch "health-checks-creating-values.md#health-checks-creating-values-cloudwatch")
    in the "Values that You Specify When You Create or Update Health Checks" topic.
  - **Route 53 API** – See
    [CreateHealthCheck](../APIReference/API_CreateHealthCheck.md "../APIReference/API_CreateHealthCheck.md") and
    [UpdateHealthCheck](../APIReference/API_UpdateHealthCheck.md "../APIReference/API_UpdateHealthCheck.md") in the
    _Amazon Route 53 API Reference_.

- **Configurable health check locations** – You can now choose the Route 53
  health checking regions that check the health of your resources, which reduces the load on the endpoint from
  health checks. This is useful if your customers are concentrated in one or a few geographic regions.
  For more information, see the following documentation:
  - **Route 53 console** – See
    [Advanced configuration
    ("Monitor an Endpoint" only)](health-checks-creating-values.md#health-checks-creating-values-advanced "health-checks-creating-values.md#health-checks-creating-values-advanced")
    in the "Values that You Specify When You Create or Update Health Checks" topic.
  - **Route 53 API** – See the `Regions` element for
    [CreateHealthCheck](../APIReference/API_CreateHealthCheck.md "../APIReference/API_CreateHealthCheck.md") and
    [UpdateHealthCheck](../APIReference/API_UpdateHealthCheck.md "../APIReference/API_UpdateHealthCheck.md") in the
    _Amazon Route 53 API Reference_.

- **Failover in private hosted zones** – You can now create failover and
  failover alias records in a private hosted zone. When you combine this feature with metric-based health checks,
  you can configure DNS failover even for endpoints that have only private IP addresses and can't be reached by using
  standard Route 53 health checks. For more information, see the following documentation:
  - **Route 53 console** – See
    [Configuring failover in a private hosted zone](dns-failover-private-hosted-zones.md "dns-failover-private-hosted-zones.md").
  - **Route 53 API** – See
    [ChangeResourceRecordSets](../APIReference/API_ChangeResourceRecordSets.md "../APIReference/API_ChangeResourceRecordSets.md")
    in the _Amazon Route 53 API Reference_.

- **Alias records in private hosted zones** – In the past,
  you could create alias records that route DNS queries only to other Route 53 records in the same
  hosted zone. With this release, you can also create alias records that route DNS queries to Elastic Beanstalk environments
  that have regionalized subdomains, ELB load balancers, and Amazon S3 buckets. (You still can't create alias records
  that route DNS queries to a CloudFront distribution.) For more information, see the following documentation:
  - **Route 53 console** – See
    [Choosing between alias and non-alias records](resource-record-sets-choosing-alias-non-alias.md "resource-record-sets-choosing-alias-non-alias.md").
  - **Route 53 API** – See
    [ChangeResourceRecordSets](../APIReference/API_ChangeResourceRecordSets.md "../APIReference/API_ChangeResourceRecordSets.md")
    in the _Amazon Route 53 API Reference_.

**February 23, 2016**

When you create or update HTTPS health checks, you can now configure Route 53 to send the host name to the endpoint
during TLS negotiation. This allows the endpoint to respond to the HTTPS request with the applicable SSL/TLS certificate.
For more information, see the description for the SNI in [Advanced configuration
("Monitor an Endpoint" only)](health-checks-creating-values.md#health-checks-creating-values-advanced "health-checks-creating-values.md#health-checks-creating-values-advanced")
field in the "Values that You Specify When You Create or Update Health Checks" topic. For information about how to enable SNI
when you use the API to create or update a health check, see
[CreateHealthCheck](../APIReference/API_CreateHealthCheck.md "../APIReference/API_CreateHealthCheck.md") and
[UpdateHealthCheck](../APIReference/API_UpdateHealthCheck.md "../APIReference/API_UpdateHealthCheck.md") in the _Amazon Route 53 API Reference_.

**January 27, 2016**

You can now register domains for over 100 additional top-level domains (TLDs) such as .accountants, .band, and .city.
For a complete list of supported TLDs, see [Domains that you can register with Amazon Route 53](registrar-tld-list.md "registrar-tld-list.md").

**January 19, 2016**

You can now create alias records that route traffic to Elastic Beanstalk environments. For information about
creating records by using the Route 53 console, see
[Creating records by using the Amazon Route 53 console](resource-record-sets-creating.md "resource-record-sets-creating.md").
For information about using the API to create records, see
[ChangeResourceRecordSets](../APIReference/API_ChangeResourceRecordSets.md "../APIReference/API_ChangeResourceRecordSets.md")
in the _Amazon Route 53 API Reference_.

## 2015 releases

**December 3, 2015**

The Route 53 console now includes a visual editor that lets you quickly create complex routing configurations that use a
combination of Route 53 weighted, latency, failover, and geolocation routing policies. You can then associate the configuration
with one or more domain names (such as example.com) or subdomain names (such as www.example.com), in the same hosted zone or in
multiple hosted zones. In addition, you can roll back the updates if the new configuration isn't performing as you expected
it to. The same functionality is available by using the Route 53 API, AWS SDKs, the AWS CLI, and AWS Tools for Windows PowerShell.
For information about using the visual editor, see [Using Traffic Flow to route DNS traffic](traffic-flow.md "traffic-flow.md"). For information
about using the API to create traffic flow configurations, see the [Amazon Route 53 API Reference](../APIReference.md "../APIReference.md").

**October 19, 2015**

With this release, Route 53 adds the following new features:

- **Domain registration for .com and .net domains by Amazon Registrar, Inc.** –
  Amazon is now an ICANN-accredited registrar for the .com and .net top-level domains (TLDs) through Amazon Registrar, Inc.
  When you use Route 53 to register a .com or .net domain, Amazon Registrar will be the registrar of record and will be listed as the
  "Sponsoring Registrar" in your Whois query results. For information about using Route 53 to register domains, see
  [Registering and managing domains using Amazon Route 53](registrar.md "registrar.md").
- **Privacy protection for .com and .net domains** – When you register a .com or .net
  domain with Route 53, all of your personal information, including first and last name, is now hidden. First and last name are not hidden
  for other domains that you register with Route 53. For more information about privacy protection, see
  [Enabling or disabling privacy protection for
  contact information for a domain](domain-privacy-protection.md "domain-privacy-protection.md").

**September 15, 2015**

With this release, Route 53 adds the following new features:

- **Calculated health checks** – You can now create health checks
  whose status is determined by the health status of other health checks. For more information, see
  [Creating and updating health checks](health-checks-creating.md "health-checks-creating.md"). In addition, see
  [CreateHealthCheck](../APIReference/API_CreateHealthCheck.md "../APIReference/API_CreateHealthCheck.md") in the
  _Amazon Route 53 API Reference_.
- **Latency measurements for health checks** – You can now configure
  Route 53 to measure the latency between health checkers and your endpoint. Latency data appears in Amazon CloudWatch graphs in the
  Route 53 console. To enable latency measurements for new health checks, see the **Latency measurements**
  setting under [Advanced configuration
  ("Monitor an Endpoint" only)](health-checks-creating-values.md#health-checks-creating-values-advanced "health-checks-creating-values.md#health-checks-creating-values-advanced")
  in the topic [Values that you specify when you
  create or update health checks](health-checks-creating-values.md "health-checks-creating-values.md").
  (You can't enable latency measurements for existing health checks.) In addition, see **MeasureLatency**
  in the topic [CreateHealthCheck](../APIReference/API_CreateHealthCheck.md "../APIReference/API_CreateHealthCheck.md") in the
  _Amazon Route 53 API Reference_.
- **Updates to the health checks dashboard in the Route 53 console** –
  The dashboard for monitoring health checks has been improved in a variety of ways, including CloudWatch graphs for monitoring latency
  between Route 53 health checkers and your endpoints. For more information, see
  [Monitoring health check status and getting notifications](health-checks-monitor-view-status.md "health-checks-monitor-view-status.md").

**March 3, 2015**

The _Amazon Route 53 Developer Guide_ now explains how to configure white-label name servers for Route 53 hosted zones.
For more information, see [Configuring white-label name servers](white-label-name-servers.md "white-label-name-servers.md").

**February 26, 2015**

You can now use the Route 53 API to list the hosted zones that are associated with an AWS account in alphabetical order by name.
You can also get a count of the hosted zones that are associated with an account. For more information, see
[ListHostedZonesByName](../APIReference/API_ListHostedZonesByName.md "../APIReference/API_ListHostedZonesByName.md") and
[GetHostedZoneCount](../APIReference/API_GetHostedZoneCount.md "../APIReference/API_GetHostedZoneCount.md")
in the _Amazon Route 53 API Reference_.

**February 11, 2015**

With this release, Route 53 adds the following new features:

- **Health Check Status** – The health checks page in the Route 53 console
  now includes a **Status** column that lets you view the overall status of all of your health checks.
  For more information, see [Viewing health check status and the reason for health check failures](health-checks-view-status.md "health-checks-view-status.md").
- **Integration with AWS CloudTrail** – Route 53 now works with CloudTrail to capture information
  about every request that your AWS account sends to the Route 53 API. Integrating Route 53 and CloudTrail
  lets you determine which requests were made to the Route 53 API, the source IP address from which each request was made,
  who made the request, when it was made, and more. For more information, see
  [Logging Amazon Route 53 API calls with AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md").
- **Quick Alarms for Health Checks** – When you create a health check by using the Route 53 console,
  you can now simultaneously create an Amazon CloudWatch alarm for the health check and specify who to notify when Route 53 considers
  the endpoint unhealthy for one minute. For more information, see
  [Creating and updating health checks](health-checks-creating.md "health-checks-creating.md").
- **Tagging for Hosted Zones and Domains** – You can now assign tags,
  which are commonly used for cost allocation, to Route 53 hosted zones and domains. For more information, see
  [Tagging Amazon Route 53 resources](tagging-resources.md "tagging-resources.md").

**February 5, 2015**

You can now use the Route 53 console to update contact information for a domain. For more information, see
[Values that you specify when you register or transfer a domain](domain-register-values-specify.md "domain-register-values-specify.md").

**January 22, 2015**

You can now specify internationalized domain names when you're registering a new domain name with Route 53.
(Route 53 already supported internationalized domain names for hosted zones and records.) For more information,
see [DNS domain name format](DomainNameFormat.md "DomainNameFormat.md").

## 2014 releases

**November 25, 2014**

With this release, you can now edit the comment that you specified for a hosted zone when you created it.
In the console, you just click the pencil icon next to the **Comment** field and enter a new value.
For more information about changing the comment by using the Route 53 API, see
[UpdateHostedZoneComment](../APIReference/API_UpdateHostedZoneComment.md "../APIReference/API_UpdateHostedZoneComment.md")
in the _Amazon Route 53 API Reference_.

**November 5, 2014**

With this release, Route 53 adds the following new features:

- **Private DNS for VPCs created using the Amazon Virtual Private Cloud service** – You can now
  use Route 53 to manage your internal domain names for VPCs without exposing DNS data to the public internet.
  For more information, see [Working with private hosted zones](hosted-zones-private.md "hosted-zones-private.md").
- **Health check failure reasons** – You can now see the current status
  of a selected health check, as well as details on why the health check last failed, as reported by each of the
  Route 53 health checkers. The status includes the HTTP status code, and failure reasons include information about
  numerous types of failures, such as string matching failures and response timeouts. For more information, see
  [Viewing health check status and the reason for health check failures](health-checks-view-status.md "health-checks-view-status.md").
- **Reusable delegation sets** – You can now apply the same set of
  four authoritative name servers, known collectively as a delegation set, to multiple hosted zones that correspond with
  different domain names. This greatly simplifies the process of migrating DNS service to Route 53 and managing
  large numbers of hosted zones. Using reusable delegation sets currently requires that you use the Route 53 API or an
  AWS SDK. For more information, see the [Amazon Route 53 API Reference](../APIReference.md "../APIReference.md").
- **Improved geolocation routing** – We further improved the
  accuracy of geolocation routing by adding support for the edns-client-subnet extension of EDNS0. For more information,
  see [Geolocation routing](routing-policy-geo.md "routing-policy-geo.md").
- **Support for Signature v4** – You can now sign all Route 53 API requests
  using Signature version 4. For more information, see
  [Signing Route 53 API Requests](../APIReference/requests-authentication.md "../APIReference/requests-authentication.md")
  in the _Amazon Route 53 API Reference_.

**July 31, 2014**

With this release, you can now do the following:

- Register domain names using Route 53. For more information, see
  [Registering and managing domains using Amazon Route 53](registrar.md "registrar.md").
- Configure Route 53 to respond to DNS queries based on the geographic location that the queries originate from.
  For more information, see [Geolocation routing](routing-policy-geo.md "routing-policy-geo.md").

**July 2, 2014**

With this release, you can now do the following:

- Edit most values in health checks. For more information, see
  [Creating, updating, and deleting
  health checks](health-checks-creating-deleting.md "health-checks-creating-deleting.md").
- Use the Route 53 API to get a list of the IP ranges that Route 53 health checkers use to check the
  health of your resources. You can use these IP addresses to configure your router and firewall rules to
  allow health checkers to check the health of your resources. For more information, see
  [GetCheckerIpRanges](../APIReference/API_GetCheckerIpRanges.md "../APIReference/API_GetCheckerIpRanges.md")
  in the _Amazon Route 53 API Reference_.
- Assign cost allocation tags to health checks, which also lets you assign a name to health checks.
  For more information, see [Naming and tagging health checks](health-checks-tagging.md "health-checks-tagging.md").
- Use the Route 53 API to get the number of health checks that are associated with your AWS account.
  For more information, see [GetHealthCheckCount](../APIReference/API_GetHealthCheckCount.md "../APIReference/API_GetHealthCheckCount.md") in the
  _Amazon Route 53 API Reference_.

**April 30, 2014**

With this release, you can now create health checks and use a domain name instead of an IP address to specify the endpoint.
This is helpful when an endpoint's IP address either is not fixed or is served by multiple IPs, such as Amazon EC2 or Amazon RDS instances.
For more information, see [Creating and updating health checks](health-checks-creating.md "health-checks-creating.md").

In addition, some information about using the Route 53 API that formerly appeared in the _Amazon Route 53 Developer Guide_
has been moved. Now all API documentation appears in the _Amazon Route 53 API Reference_.

**April 18, 2014**

With this release, Route 53 passes a different value in the `Host` header when the health check
**Port** value is **443** and the **Protocol** value is
**HTTPS**. During a health check, Route 53 now passes to the endpoint a `Host` header
that contains the value of the **Host Name** field. If you created the health check by using
the `CreateHealthCheck` API action, this is the value of the `FullyQualifiedDomainName` element.

For more information, see [Creating, updating, and deleting
health checks](health-checks-creating-deleting.md "health-checks-creating-deleting.md").

**April 9, 2014**

With this release, you can now view what percentage of Route 53 health checkers are currently
reporting that an endpoint is healthy.

In addition, behavior of the Health Check Status metric in Amazon CloudWatch now shows only zero (if your
endpoint was unhealthy during a given time period) or one (if the endpoint was healthy for that time period).
The metric no longer shows values between 0 and 1 reflecting the portion of Route 53 health checks that are
reporting the endpoint as healthy.

For more information, see [Monitoring health checks using CloudWatch](monitoring-health-checks.md "monitoring-health-checks.md").

**February 18, 2014**

With this release, Route 53 adds the following features:

- **Health check failover threshold:** You can now specify how many consecutive health checks an endpoint
  must fail before Route 53 considers the endpoint unhealthy, between 1 and 10 consecutive checks. An unhealthy endpoint must pass the same
  number of checks to be considered healthy. For more information, see
  [How Amazon Route 53 determines
  whether a health check is healthy](dns-failover-determining-health-of-endpoints.md "dns-failover-determining-health-of-endpoints.md").
- **Health check request interval:** You can now specify how frequently Route 53 sends requests
  to an endpoint to determine whether the endpoint is healthy. Valid settings are 10 seconds and 30 seconds.
  For more information, see
  [How Amazon Route 53 determines
  whether a health check is healthy](dns-failover-determining-health-of-endpoints.md "dns-failover-determining-health-of-endpoints.md").

**January 30, 2014**

With this release, Route 53 adds the following features:

- **HTTP and HTTPS string-match health checks:** Route 53 now supports health checks
  that determine the health of an endpoint based on the appearance of a specified string in the response body.
  For more information, see
  [How Amazon Route 53 determines
  whether a health check is healthy](dns-failover-determining-health-of-endpoints.md "dns-failover-determining-health-of-endpoints.md").
- **HTTPS health checks:** Route 53 now supports health checks for secure, SSL-only websites.
  For more information, see
  [How Amazon Route 53 determines
  whether a health check is healthy](dns-failover-determining-health-of-endpoints.md "dns-failover-determining-health-of-endpoints.md").
- **`UPSERT` for the `ChangeResourceRecordSets` API Action:**
  When creating or changing records using the `ChangeResourceRecordSets` API action, you can now use the
  `UPSERT` action either to create a new record if none exists with a given name and type, or to
  update an existing record. For more information, see
  [ChangeResourceRecordSets](../APIReference/API_ChangeResourceRecordSets.md "../APIReference/API_ChangeResourceRecordSets.md") in the
  _Amazon Route 53 API Reference_.

**January 7, 2014**

With this release, Route 53 adds support for health checks that determine the health of an endpoint based on
whether a specified string appears in the response body. For more information, see
[How Amazon Route 53 determines
whether a health check is healthy](dns-failover-determining-health-of-endpoints.md "dns-failover-determining-health-of-endpoints.md").

## 2013 releases

**August 14, 2013**

With this release, Route 53 adds support for creating records by importing a BIND-formatted zone file.
For more information, see [Creating records by importing a zone file](resource-record-sets-creating-import.md "resource-record-sets-creating-import.md").

In addition, CloudWatch metrics for Route 53 health checks have been integrated into the Route 53 console and streamlined.
For more information, see [Monitoring health checks using CloudWatch](monitoring-health-checks.md "monitoring-health-checks.md").

**June 26, 2013**

With this release, Route 53 adds support for integrating health checks with CloudWatch metrics so you can do the following:

- Verify that a health check is properly configured.
- Review the health of a health check endpoint over a specified period of time.
- Configure CloudWatch to send an Amazon Simple Notification Service (Amazon SNS) alert when all Route 53 health checkers consider your
  specified endpoint to be unhealthy.

For more information, see [Monitoring health checks using CloudWatch](monitoring-health-checks.md "monitoring-health-checks.md").

**June 11, 2013**

With this release, Route 53 adds support for creating alias records that route DNS queries to alternate domain names for
Amazon CloudFront distributions. You can use this feature both for alternate domain names at the zone apex (example.com) and
alternate domain names for subdomains (www.example.com). For more information, see
[Routing traffic to an Amazon CloudFront
distribution by using your domain name](routing-to-cloudfront-distribution.md "routing-to-cloudfront-distribution.md").

**May 30, 2013**

With this release, Route 53 adds support for evaluating the health of ELB load balancers and the associated
Amazon EC2 instances. For more information, see [Creating Amazon Route 53 health checks](dns-failover.md "dns-failover.md") .

**March 28, 2013**

The documentation about health checks and failover was rewritten to enhance usability.
For more information, see [Creating Amazon Route 53 health checks](dns-failover.md "dns-failover.md") .

**February 11, 2013**

With this release, Route 53 adds support for failover and health checks. For more information,
see [Creating Amazon Route 53 health checks](dns-failover.md "dns-failover.md") .

## 2012 release

**March 21, 2012**

With this release, Route 53 lets you create latency records. For more information,
see [Latency-based routing](routing-policy-latency.md "routing-policy-latency.md").

## 2011 releases

**December 21, 2011**

With this release, the Route 53 console in the AWS Management Console lets you create an alias record by
choosing an Elastic Load Balancer from a list instead of manually entering the hosted zone ID and the DNS name
of the load balancer. New functionality is documented in the _Amazon Route 53 Developer Guide_.

**November 16, 2011**

With this release, you can use the Route 53 console in the AWS Management Console to create and delete hosted zones, and to
create, change, and delete records. New functionality is documented throughout the
_Amazon Route 53 Developer Guide_, as applicable.

**October 18, 2011**

The _Amazon Route 53 Getting Started Guide_ was merged into the _Amazon Route 53 Developer Guide_,
and the _Developer Guide_ was reorganized to enhance usability.

**May 24, 2011**

This release of Amazon Route 53 introduces alias records, which allow you to create zone apex aliases;
weighted records; a new API (2011-05-05); and a service-level agreement. In addition, after six
months in beta, Route 53 is now generally available. For more information, see the
[Amazon Route 53 product page](https://aws.amazon.com/route53/ "https://aws.amazon.com/route53/") and
[Choosing between alias and non-alias records](resource-record-sets-choosing-alias-non-alias.md "resource-record-sets-choosing-alias-non-alias.md")
in the _Amazon Route 53 Developer Guide_.

## 2010 release

**December 5, 2010**

This is the first release of _Amazon Route 53 Developer Guide_.
