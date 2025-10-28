# Routing traffic to an Amazon CloudFront

distribution by using your domain name

This topic provides comprehensive procedures for routing DNS traffic to any Amazon CloudFront
distribution. If you're setting up a static website with Amazon CloudFront and Amazon Simple Storage Service, see
[Use an Amazon CloudFront distribution to serve
a static website](getting-started-cloudfront-overview.md "getting-started-cloudfront-overview.md") for a complete
tutorial.

You can use Amazon CloudFront, the AWS content delivery network (CDN), as one way to speed up
delivery of your web content. CloudFront can deliver your entire website—including
dynamic, static, streaming, and interactive content—by using a global network of
edge locations. Users who request your content are automatically routed to the edge
location that gives them the lowest latency.

###### Note

You can route traffic to a CloudFront distribution only for public hosted zones.

To use CloudFront to distribute your website content, create a distribution and specify
settings for it. For example, specify the Amazon S3 bucket or HTTP server that you want CloudFront
to get your content from, whether you want only selected users to have access to your
content, and whether you want users to use HTTPS.

When you create a distribution, CloudFront assigns a domain name to the distribution, such
as d111111abcdef8.cloudfront.net. You can use this domain name in the
URLs for your content, for example:

`http://d111111abcdef8.cloudfront.net/logo.jpg`

Alternatively, you can use your own domain name in URLs, for example:

`http://example.com/logo.jpg`

Follow the steps in the Amazon CloudFront Developer Guide to use your own domain name in your
files' URLs in a CloudFront distribution, instead of the domain name that CloudFront assigns to your
distribution. For more information, about using your own domain name with a CloudFront
distribution, see [Using custom URLs by
adding alternate domain names (CNAMEs)](../../../AmazonCloudFront/latest/DeveloperGuide/CNAMEs.md "../../../AmazonCloudFront/latest/DeveloperGuide/CNAMEs.md").

When you use a Route 53 domain name with a CloudFront distribution, use Amazon Route 53 to create an
[alias
record](resource-record-sets-choosing-alias-non-alias.md "resource-record-sets-choosing-alias-non-alias.md") that points to your CloudFront distribution. An alias record is a Route 53
extension to DNS. It's similar to a CNAME record, but you can create an alias record
both for the root domain, such as example.com, and for subdomains, such as
www.example.com. (You can create CNAME records only for subdomains.) When Route 53 receives
a DNS query that matches the name and type of an alias record, Route 53 responds with the
domain name that is associated with your distribution.

###### Note

Route 53 doesn't charge for alias queries to CloudFront distributions or other AWS
resources.

## Prerequisites

To get started, you need the following:

1. A registered domain name. You can use Amazon Route 53 as your domain registrar
   or you can use a different registrar.
2. Route 53 as the DNS service for the domain. If you register your domain name
   by using Route 53, we automatically configure Route 53 as the DNS service for the
   domain.

For information about using Route 53 as the DNS service provider for your
domain, see [Making Amazon Route 53 the DNS service for an existing domain](MigratingDNS.md "MigratingDNS.md"). 3. A CloudFront distribution or a CloudFront distribution tenant. The distribution must
include an alternate domain name that matches the domain name that you want
to use for your URLs instead of the domain name that CloudFront assigned to your
distribution. For a CloudFront distribution tenant, it must contain the domain
name that you want to use for your URLs.

For example, if you want the URLs for your content to contain the domain
name **example.com**, the **Alternate Domain
Name** field for the distribution must include
**example.com**.

For more information, see the following documentation in the
_Amazon CloudFront Developer Guide_:

    * [Task list
     for creating a distribution](../../../AmazonCloudFront/latest/DeveloperGuide/distribution-web-creating.md "../../../AmazonCloudFront/latest/DeveloperGuide/distribution-web-creating.md")
    * [Creating or updating a distribution using the CloudFront
     console](../../../AmazonCloudFront/latest/DeveloperGuide/distribution-web-creating-console.md "../../../AmazonCloudFront/latest/DeveloperGuide/distribution-web-creating-console.md")

###### Note

If you're creating a static website, see [Get started with a secure static website](../../../AmazonCloudFront/latest/DeveloperGuide/getting-started-secure-static-website-cloudformation-template.md "../../../AmazonCloudFront/latest/DeveloperGuide/getting-started-secure-static-website-cloudformation-template.md") in the
_Amazon CloudFront Developer Guide_ for complete setup
instructions. 4. (Optional) Request a public certificate so that Amazon CloudFront distributions
require HTTPS. For more information, see [DNS validation in the
AWS Certificate Manager](../../../acm/latest/userguide/dns-validation.md "../../../acm/latest/userguide/dns-validation.md") in the _AWS Certificate Manager User
Guide._

## Configuring Amazon Route 53 to

route traffic to a CloudFront distribution

To configure Amazon Route 53 to route traffic to a CloudFront distribution, follow these
steps. For more information about using your own domain name with a CloudFront
distribution, see [Using custom URLs by adding
alternate domain names (CNAMEs)](../../../AmazonCloudFront/latest/DeveloperGuide/CNAMEs.md "../../../AmazonCloudFront/latest/DeveloperGuide/CNAMEs.md") in the Amazon CloudFront Developer Guide.

###### Note

Changes generally propagate to all Route 53 servers within 60 seconds. When the
changes propagate, you'll be able to route traffic to your CloudFront distribution by
using the name of the alias record that you create in this procedure.

###### To route traffic to a

CloudFront distribution

1. Get the domain name that CloudFront assigned to your distribution and determine
   whether IPv6 is enabled:
   1. Sign in to the AWS Management Console and open the CloudFront console at
      [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
   2. in the **ID** column, select the linked name of
      the distribution that you want to route traffic to (not the check
      box).
   3. On the **General** tab, get the value of the
      **Distribution domain name** field.
   4. On the **General** tab, in the
      **Settings** section, choose edit and scroll to
      check the **IPv6** field to see whether IPv6 is
      enabled for the distribution. If IPv6 is enabled, you'll need to
      create two alias records for the distribution, one to route IPv4
      traffic to the distribution, and one to route IPv6 traffic. Choose
      **Cancel**.

   For more information, see [Enable IPv6](../../../AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.md#DownloadDistValuesEnableIPv6 "../../../AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.md#DownloadDistValuesEnableIPv6") in the topic [Values
   that you specify when you create or update a
   distribution](../../../AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.md "../../../AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.md") in the
   _Amazon CloudFront Developer Guide_.

2. For a CloudFront distribution tenant,
   1. Choose **SaaS** in the left nav, then
      **Distribution tenants**, and choose the
      distribution tenant with the domain name that you want to route
      traffic to
   2. in the **General details** section, copy the
      value of the **Endpoint**.

3. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
4. In the navigation pane, choose **Hosted zones**.
5. Choose the linked name of the hosted zone for the domain that you want to
   use to route traffic to your CloudFront distribution.
6. Choose **Create record**.
7. Specify the following values:

**Record name**

Enter the domain name that you want to use to route traffic to
your CloudFront distribution. The default value is the name of the
hosted zone.

For example, if the name of the hosted zone is example.com and
you want to use **acme.example.com** to route
traffic to your distribution, enter
**acme**.

**Record type**

Choose **A – IPv4 address**.

If IPv6 is enabled for the distribution and you're creating a
second record, choose **AAAA – IPv6
address**.

**Alias**

Turn on **Alias**.

###### Important

You must create an Alias record for the CloudFront distribution
to work.

**Route traffic to**

Choose **Alias to CloudFront distribution**. Choose
the domain name that CloudFront assigned to the distribution when you
created it. This is the value that you got in step 1.

For a CloudFront distribution tenant, choose the endpoint from step 2.

**Evaluate target health**

Accept the default value of **No**.

**Routing policy**

Choose the applicable routing policy. For more information,
see [Choosing a routing policy](routing-policy.md "routing-policy.md"). 8. Choose **Create records**. 9. If IPv6 is enabled for the distribution, repeat steps 5 through 7. Specify
the same settings except for the **Record type** field, as
explained in step 6.
