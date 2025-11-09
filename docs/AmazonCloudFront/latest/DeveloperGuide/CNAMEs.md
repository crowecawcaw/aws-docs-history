# Use custom URLs by adding alternate domain names (CNAMEs)

When you create a distribution, CloudFront provides a domain name for it, such as
d111111abcdef8.cloudfront.net. Instead of using this provided domain name, you can use an
alternate domain name (also known as a CNAME).

To learn how to use your own domain name, such as www.example.com, see the following topics:

###### Topics

- [Requirements for using alternate domain
  names](#alternate-domain-names-requirements "#alternate-domain-names-requirements")
- [Restrictions on using
  alternate domain names](#alternate-domain-names-restrictions "#alternate-domain-names-restrictions")
- [Add an alternate domain name](CreatingCNAME.md "CreatingCNAME.md")
- [Move an alternate domain name](alternate-domain-names-move.md "alternate-domain-names-move.md")
- [Remove an alternate domain name](alternate-domain-names-remove-domain.md "alternate-domain-names-remove-domain.md")
- [Use wildcards in alternate domain names](alternate-domain-names-wildcard.md "alternate-domain-names-wildcard.md")

## Requirements for using alternate domain

names

When you add an alternate domain name, such as www.example.com, to a CloudFront distribution, the
following are requirements:

**Alternate domain names must be lowercase**

All alternate domain names (CNAMEs) must be lowercase.

**Alternate domain names must be covered by a valid TLS certificate**

To add an alternate domain name (CNAME) to a CloudFront distribution, you must attach to your
distribution a trusted, valid TLS certificate that covers the
alternate domain name. This ensures that only people with access to your
domain’s certificate can associate with CloudFront a CNAME related to your
domain.

A trusted certificate is one that is issued by AWS Certificate Manager (ACM) or by another valid certificate authority (CA). You can use a self-signed certificate to
validate an existing CNAME, but _not_ for a new
CNAME. CloudFront supports the same certificate authorities as Mozilla. For
the current list, see [Mozilla
Included CA Certificate List](https://wiki.mozilla.org/CA/Included_Certificates "https://wiki.mozilla.org/CA/Included_Certificates"). For information about intermediate certificates when using a third-party CA, see [Intermediate
certificates](cnames-and-https-requirements.md#https-requirements-intermediate-certificates "cnames-and-https-requirements.md#https-requirements-intermediate-certificates").

To verify an alternate domain name by using the certificate that you attach, including
alternate domain names that include wildcards, CloudFront checks the subject
alternative name (SAN) on the certificate. The alternate domain name
that you’re adding must be covered by the SAN.

###### Note

Only one certificate can be attached to a CloudFront distribution at a time.

You prove that you are authorized to add a specific alternate domain name to your distribution by doing
one of the following:

- Attaching a certificate that includes the alternate domain name, like
  product-name.example.com.
- Attaching a certificate that includes a \* wildcard at the beginning of a domain name,
  to cover multiple subdomains with one certificate. When you specify a wildcard, you can add multiple
  subdomains as alternate domain names in CloudFront.

The following examples illustrate how using wildcards in domain names in a certificate work to authorize you
to add specific alternate domain names in CloudFront.

- You want to add marketing.example.com as an alternate domain name. You list in your
  certificate the following domain name: \*.example.com. When you
  attach this certificate to CloudFront, you can add any alternate
  domain name for your distribution that replaces the wildcard at
  that level, including marketing.example.com. You can also, for
  example, add the following alternate domain names:

      + product.example.com
      + api.example.com

  However, you can’t add alternate domain names that are at levels higher or lower than
  the wildcard. For example, you can’t add the alternate domain
  names example.com or marketing.product.example.com.

- You want to add example.com as an alternate domain name. To do this, you must list the domain
  name example.com itself on the certificate that you attach to
  your distribution.
- You want to add marketing.product.example.com as an alternate domain name. To do this, you can
  list \*.product.example.com on the certificate, or you can list
  marketing.product.example.com itself on the certificate.

**Permission to change DNS configuration**

When you add alternate domain names, you must create CNAME records to route DNS queries
for the alternate domain names to your CloudFront distribution. To do this,
you must have permission to create CNAME records with the DNS service
provider for the alternate domain names that you’re using. Typically,
this means that you own the domains, but you might be developing an
application for the domain owner.

**Alternate domain names and HTTPS**

If you want viewers to use HTTPS with an alternate domain name, you must complete some
additional configuration. For more information, see [Use alternate domain names and
HTTPS](using-https-alternate-domain-names.md "using-https-alternate-domain-names.md").

## Restrictions on using

alternate domain names

Note the following restrictions on using alternate domain names:

**Maximum number of alternate domain names**

For the current maximum number of alternate domain names that you can
add to a distribution, or to request a higher quota (formerly known as
limit), see [General quotas on distributions](cloudfront-limits.md#limits-web-distributions "cloudfront-limits.md#limits-web-distributions").

**Duplicate and overlapping alternate domain names**

You cannot add an alternate domain name to a CloudFront distribution if the
same alternate domain name already exists in another CloudFront distribution,
even if your AWS account owns the other distribution.

However, you can add a wildcard alternate domain name, such as
\*.example.com, that includes (that overlaps with) a non-wildcard
alternate domain name, such as www.example.com. If you have overlapping
alternate domain names in two distributions, CloudFront sends the request to
the distribution with the more specific name match, regardless of the
distribution that the DNS record points to. For example,
marketing.domain.com is more specific than \*.domain.com.

If you have an existing wildcard DNS entry that points to a CloudFront
distribution and you receive an incorrectly configured DNS error when
trying to add a new CNAME with a more specific name, see [CloudFront returns
an incorrectly configured DNS record error when I try to add a new CNAME](troubleshooting-distributions.md#troubleshoot-incorrectly-configured-DNS-record-error "troubleshooting-distributions.md#troubleshoot-incorrectly-configured-DNS-record-error").

**Domain fronting**

CloudFront has protection against domain fronting occurring across different
AWS account. This is a scenario when a non-standard client creates a
TLS/SSL connection to a domain name in one AWS account, and then makes
an HTTPS request for an unrelated domain name in another
AWS account.

For example, the TLS connection might connect to www.example.com, and
then issue a request for www.example.org.

To determine whether a request is being domain fronted, CloudFront performs
the following checks:

- The SNI extension is equal to the HTTP request
  `Host` header
- The certificate belongs to the same AWS account as the
  distribution for the request
- The HTTP request `Host` is covered by the
  certificate that is served during the TLS handshake

If none of these conditions are met, CloudFront determines the request is
domain fronting. CloudFront will reject the request with a 421 HTTP error
response.

###### Note

If the client doesn't provide the SNI extension and gets a default
\*.cloudfront.net certificate instead, CloudFront will accept the incoming
requests.

**How CloudFront identifies the distribution for a request**

CloudFront identifies a distribution for a HTTP request based on the
`Host` header. CloudFront doesn't depend on the CloudFront IP address
that you're connecting to or what SNI handshake was provided during TLS
handshake.

When CloudFront receives a request, it will use the value of the
`Host` header to match the request to the specific
distribution.

For example, say that you have two distributions and you've updated
your DNS configuration so that the alternate domain names route to the
following endpoints:

- primary.example.com points to d111111primary.cloudfront.net
- secondary.example.com points to
  d222222secondary.cloudfront.net

If you make a request to https://primary.example.com but specify the
`Host` header as secondary.example.com, such as
`curl https://primary.example.com -H "Host:
 secondary.example.com"`, the request will route to the
secondary distribution instead.

**Adding an alternate domain name at the top node (zone apex) for a
domain**

When you add an alternate domain name to a distribution, you typically
create a CNAME record in your DNS configuration to route DNS queries for
the domain name to your CloudFront distribution. However, you can’t create a
CNAME record for the top node of a DNS namespace, also known as the zone
apex; the DNS protocol doesn’t allow it. For example, if you register
the DNS name example.com, the zone apex is example.com. You can’t create
a CNAME record for example.com, but you can create CNAME records for
www.example.com, newproduct.example.com, and so on.

If you’re using Route 53 as your DNS service, you can create an alias
resource record set, which has the following advantages over CNAME
records:

- You can create an alias resource record set for a domain name
  at the top node (example.com).
- You can create an HTTPS record for an alternate domain name to
  allow protocol negotiation as part of the DNS lookup if the
  client supports it. For more information, see [Create alias resource record set](CreatingCNAME.md#alternate-domain-https "CreatingCNAME.md#alternate-domain-https").
- You don’t pay for Route 53 queries when you use an alias resource
  record set.

###### Note

If you enable IPv6, you must create two alias resource record
sets: one to route IPv4 traffic (an A record) and one to route IPv6
traffic (an AAAA record). For more information, see [Enable IPv6 (viewer requests)](DownloadDistValuesGeneral.md#DownloadDistValuesEnableIPv6 "DownloadDistValuesGeneral.md#DownloadDistValuesEnableIPv6") in the topic
[All distribution settings reference](distribution-web-values-specify.md "distribution-web-values-specify.md").

For more information, see [Routing traffic to an Amazon CloudFront web distribution
by using your domain name](../../../Route53/latest/DeveloperGuide/routing-to-cloudfront-distribution.md "../../../Route53/latest/DeveloperGuide/routing-to-cloudfront-distribution.md") in the
_Amazon Route 53 Developer Guide_.

If you're not using Route 53 for your DNS, you can request Anycast static
IP addresses to route apex domains like example.com to CloudFront. For more
information, see [Request Anycast static IPs to use for
allowlisting](request-static-ips.md "request-static-ips.md").
