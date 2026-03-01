# Understand how multi-tenant distributions work

You can create CloudFront multi-tenant distributions with settings that can be reused across multiple distribution tenants.
With a multi-tenant distribution, you can have CloudFront configure your distribution settings for you, based on
your content origin type. For more details about the preconfigured settings, see [Preconfigured distribution settings reference](template-preconfigured-origin-settings.md "template-preconfigured-origin-settings.md").

Benefits of using a multi-tenant distribution instead of a standard distribution include:

- Reducing operational burden.
- Reusable configurations for web admins and software providers to manage CloudFront distribution for multiple web applications that deliver content to end users.
- Enhanced integrations with other AWS services to deliver automated certificate management, unified security controls, and hassle-free configuration control at scale.
- Maintaining consistent resource patterns across your implementations. Define
  settings that must be shared and then specify customizations for settings to
  override.
- Customizable origin and security settings to meet specific needs at the distribution tenant level.
- Organize your distribution tenants into different tiers. For example, if some distribution tenants
  require Origin Shield and some do not, you can group
  distribution tenants into different multi-tenant distributions.
- Sharing a common DNS configuration across multiple domains.
  Unlike a standard distribution, a multi-tenant distribution cannot be accessed directly because it has no CloudFront
  routing endpoint. Therefore, it must be used in conjunction with a connection group and one or more
  distribution tenants. While standard distributions have their own CloudFront endpoint and can be directly accessed by end
  users, they cannot be used as a template for other distributions.

For information about multi-tenant distribution quotas, see [Quotas on multi-tenant distributions](cloudfront-limits.md#limits-template "cloudfront-limits.md#limits-template").

###### Topics

- [How it works](#how-template-distribution-works "#how-template-distribution-works")
- [Terms](#template-distributions-concepts "#template-distributions-concepts")
- [Unsupported features](#unsupported-saas "#unsupported-saas")
- [Distribution tenant customizations](tenant-customization.md "tenant-customization.md")
- [Request certificates for your CloudFront distribution tenant](managed-cloudfront-certificates.md "managed-cloudfront-certificates.md")
- [Create custom connection group (optional)](custom-connection-group.md "custom-connection-group.md")
- [Migrate to a multi-tenant distribution](template-migrate-distribution.md "template-migrate-distribution.md")

## How it works

In a _standard distribution_, the distribution contains all the settings that
you want to enable for your website or application, such as the origin configurations,
cache behaviors, and security settings. If you wanted to create a separate website and
use many of the same settings, you would need to create a new distribution each
time.

CloudFront multi-tenant distributions are different in that you can create an initial multi-tenant distribution. For each
new website, you create a distribution tenant that automatically inherits the defined values of its
source distribution. Then, you customize specific settings for your distribution tenant.

###### Overview

1. To get started, you first create a multi-tenant distribution. CloudFront configures your
   distribution settings for you, based on your content origin type. You can customize settings for all origins except VPC origins. VPC origins settings are customized on the VPC origin resource itself. For more
   information about the multi-tenant distribution settings that you can customize, see [Preconfigured distribution settings reference](template-preconfigured-origin-settings.md "template-preconfigured-origin-settings.md").
   - The TLS certificate that you use for the multi-tenant distribution can be inherited
     by your distribution tenants. The multi-tenant distribution itself is not routable, so it will not
     have a domain name associated with it.

2. By default, CloudFront creates a connection group for you. The connection group controls how viewer
   requests for content connect to CloudFront. You can customize some routing settings in
   the connection group.

You can change this by manually creating your own connection group. For more information, see [Create custom connection group (optional)](custom-connection-group.md "custom-connection-group.md"). 3. Then, you create one or more distribution tenants. The distribution tenant is the "front door" for
viewers to access your content. Each distribution tenant references the multi-tenant distribution and is automatically associated with the
connection group that CloudFront created for you. The distribution tenant supports an individual domain or subdomain. 4. You can then customize some distribution tenant settings, such as vanity domains and
origin paths. For more information, see [Distribution tenant customizations](tenant-customization.md "tenant-customization.md"). 5. Finally, you must update the DNS record in your DNS host to route traffic to
the distribution tenant. To do this, get the CloudFront endpoint value from your connection group
and create a CNAME record that points to the CloudFront endpoint.

###### Example

The following graphic demonstrates how a multi-tenant distribution,distribution tenants, and connection
groups work together to deliver content for your viewers for multiple
domains.

1. The multi-tenant distribution defines the inherited settings for each distribution tenant. You use
   the multi-tenant distribution as a template.
2. Each distribution tenant created from the multi-tenant distribution has its own domain.
3. The distribution tenants are automatically added to the connection group that CloudFront created for you when you created the multi-tenant distribution. Connection groups control how viewer
   requests are connected to the CloudFront network.

![How multi-tenant distributions work with distribution tenants.](images/template_distribution.png)

For detailed multi-tenant distribution creation instructions, see [Create a CloudFront distribution in the console](distribution-web-creating-console.md#create-console-distribution "distribution-web-creating-console.md#create-console-distribution").

## Terms

The following concepts describe components of multi-tenant distributions:

**Multi-tenant distribution**

A blueprint, multi-tenant distribution that specifies all shared
configuration settings for any distribution tenants, including cache behavior, security
protections, and origins. Multi-tenant distributions cannot serve traffic directly. They
must be used in conjunction with connection groups and distribution tenants.

**Standard distribution**

A distribution that does not have multi-tenant functionality. These distributions are best for supporting single websites or apps.

**Distribution tenant**

A distribution tenant inherits the multi-tenant distribution configuration. Some configuration settings can be
customized at the distribution tenant level. The distribution tenant must have a valid TLS
certificate, which can be inherited from the multi-tenant distribution as long as it covers
the distribution tenant domain or subdomain.

The distribution tenant must be associated with a connection group. CloudFront creates a connection group for you when you create a distribution tenant, and automatically assigns any distribution tenants to that connection group.

**Multi-tenancy**

You can use the multi-tenant distribution to serve content across multiple domains, while
sharing configuration and infrastructure. This approach allows different
domains (called tenants) to share common settings from the multi-tenant distribution, while
maintaining their own customizations.

**Connection group**

Provides the CloudFront routing endpoint that serves content to viewers. You must
associate each distribution tenant to a connection group to get the corresponding CloudFront
routing endpoint for the CNAME record that you create for your distribution tenant domain or
subdomain. Connection groups can be shared across multiple distribution tenants.
Connection groups manage routing settings for distribution tenants, such as IPv6 and Anycast IP list settings.

**Parameters**

A list of key-value pairs for placeholder values, such as origin paths and domain names. You can define parameters in your multi-tenant distribution and provide values for those parameters at the distribution tenant level. You choose whether the parameter values are required to be entered for the distribution tenant.

If you do not provide a value for an optional parameter in a distribution tenant,
then the default value from the multi-tenant distribution is
used as the value.

**CloudFront routing endpoint**

Canonical DNS for the connection group, such as
`d123.cloudfront.net`. Used in the CNAME record for your
distribution tenant domain or subdomain.

**Customizations**

You can customize your distribution tenants so that they use
_different_ settings from the multi-tenant distribution. For each
distribution tenant, you can specify a different AWS WAF web access control list
(ACL), TLS certificates, and geographic restrictions.

## Unsupported features

The following features can't be used with a multi-tenant distribution. If you want to create a new
multi-tenant distribution using the same settings as your standard distribution, note that some settings aren't
available.

###### Notes

- Currently, AWS Firewall Manager policies only apply to your standard distributions. Firewall Manager
  will add support for multi-tenant distributions in a future release.
- Unlike standard distributions, you specify your domain name (alias) at the
  _distribution tenant_ level. For more information, see [Request certificates for your CloudFront distribution tenant](managed-cloudfront-certificates.md "managed-cloudfront-certificates.md") and the [CreateDistributionTenant](../../../cloudfront/latest/APIReference/API_CreateDistributionTenant.md "../../../cloudfront/latest/APIReference/API_CreateDistributionTenant.md") API operation.

- [Continuous deployment](continuous-deployment.md "continuous-deployment.md")
- [Origin access
  identity (OAI)](private-content-restricting-access-to-s3.md#private-content-restricting-access-to-s3-oai "private-content-restricting-access-to-s3.md#private-content-restricting-access-to-s3-oai") – Use [origin access control
  (OAC)](private-content-restricting-access-to-origin.md "private-content-restricting-access-to-origin.md") instead.
- [Dedicated IP custom SSL support](DownloadDistValuesGeneral.md#DownloadDistValuesClientsSupported "DownloadDistValuesGeneral.md#DownloadDistValuesClientsSupported") –
  Only the `sni-only` method is supported.
- [AWS WAF Classic (V1) web ACL](DownloadDistValuesGeneral.md#DownloadDistValuesWAFWebACL "DownloadDistValuesGeneral.md#DownloadDistValuesWAFWebACL")
  – Only AWS WAF V2 web ACLs are supported.
- [Standard logging (legacy)](standard-logging-legacy-s3.md "standard-logging-legacy-s3.md")
- [Minimum TTL](DownloadDistValuesCacheBehavior.md#DownloadDistValuesMinTTL "DownloadDistValuesCacheBehavior.md#DownloadDistValuesMinTTL")
- [Default TTL](DownloadDistValuesCacheBehavior.md#DownloadDistValuesDefaultTTL "DownloadDistValuesCacheBehavior.md#DownloadDistValuesDefaultTTL")
- [Maximum TTL](DownloadDistValuesCacheBehavior.md#DownloadDistValuesMaxTTL "DownloadDistValuesCacheBehavior.md#DownloadDistValuesMaxTTL")
- [ForwardedValues](../../../cloudfront/latest/APIReference/API_ForwardedValues.md "../../../cloudfront/latest/APIReference/API_ForwardedValues.md")
- [PriceClass](../../../cloudfront/latest/APIReference/API_DistributionConfig.md "../../../cloudfront/latest/APIReference/API_DistributionConfig.md")
- [Trusted Signers](DownloadDistValuesCacheBehavior.md#DownloadDistValuesTrustedSigners "DownloadDistValuesCacheBehavior.md#DownloadDistValuesTrustedSigners")
- [Smooth streaming](DownloadDistValuesCacheBehavior.md#DownloadDistValuesSmoothStreaming "DownloadDistValuesCacheBehavior.md#DownloadDistValuesSmoothStreaming")
- [AWS Identity and Access Management (IAM)
  server certificates](../../../IAM/latest/UserGuide/id_credentials_server-certs.md "../../../IAM/latest/UserGuide/id_credentials_server-certs.md")
- [Dedicated IP addresses](cnames-https-dedicated-ip-or-sni.md#cnames-https-dedicated-ip "cnames-https-dedicated-ip-or-sni.md#cnames-https-dedicated-ip")
- [Minimum Protocol Version
  SSLv3](DownloadDistValuesGeneral.md#DownloadDistValues-security-policy "DownloadDistValuesGeneral.md#DownloadDistValues-security-policy")

The following settings can't be configured in a multi-tenant distribution or distribution tenant. Instead, set the
values that you want in a connection group. All distribution tenants associated in the connection group
will use these settings. For more information, see [Create custom connection group (optional)](custom-connection-group.md "custom-connection-group.md").

- [Enable IPv6 (viewer requests)](DownloadDistValuesGeneral.md#DownloadDistValuesEnableIPv6 "DownloadDistValuesGeneral.md#DownloadDistValuesEnableIPv6")
- [Anycast static IP list](request-static-ips.md "request-static-ips.md")
