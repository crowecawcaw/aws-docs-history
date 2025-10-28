# Enable IPv6 for CloudFront distributions

Amazon CloudFront supports both IPv4 and IPv6 from clients to AWS edge locations. CloudFront also supports IPv6 and dual-stack (IPv4 and IPv6) connectivity towards origins. This helps you achieve end-to-end IPv6 delivery.

IPv6 is the next-generation internet protocol designed to replace IPv4. While IPv4 uses 32-bit addresses (such as 192.0.2.44), IPv6 uses 128-bit addresses (such as 2001:0db8:85a3::8a2e:0370:7334). IPv6 provides an expanded address space to accommodate more internet-connected devices.

###### Topics

- [IPv6 viewer requests](#ipv6-viewer-requests "#ipv6-viewer-requests")
- [IPv6 origin requests](#ipv6-origin-requests "#ipv6-origin-requests")

## IPv6 viewer requests

In general, you should enable IPv6 if you have users on IPv6 networks who want
to access your content. However, if you're using signed URLs or signed cookies
to restrict access to your content, and if you're using a custom policy that
includes the `IpAddress` parameter to restrict the IP addresses that
can access your content, do not enable IPv6. If you want to restrict access to
some content by IP address and not restrict access to other content (or restrict
access but not by IP address), you can create two distributions. For information
about creating signed URLs by using a custom policy, see [Create a signed URL using
a custom policy](private-content-creating-signed-url-custom-policy.md "private-content-creating-signed-url-custom-policy.md"). For
information about creating signed cookies by using a custom policy, see [Set signed
cookies using a custom policy](private-content-setting-signed-cookie-custom-policy.md "private-content-setting-signed-cookie-custom-policy.md").

If you're using a Route 53 alias resource record set to route traffic to your
CloudFront distribution, you need to create a second alias resource record set when
both of the following are true:

- You enable IPv6 for the distribution
- You're using alternate domain names in the URLs for your
  objects

For more information, see [Routing traffic to an Amazon CloudFront distribution by using your domain
name](../../../Route53/latest/DeveloperGuide/routing-to-cloudfront-distribution.md "../../../Route53/latest/DeveloperGuide/routing-to-cloudfront-distribution.md") in the _Amazon Route 53 Developer Guide_.

If you created a CNAME resource record set, either with Route 53 or with another
DNS service, you don't need to make any changes. A CNAME record routes traffic
to your distribution regardless of the IP address format of the viewer
request.

If you enable IPv6 and CloudFront access logs, the `c-ip` column includes values in
IPv4 and IPv6 format. For more information, see [Log file fields](standard-logs-reference.md#BasicDistributionFileFormat "standard-logs-reference.md#BasicDistributionFileFormat").

###### Note

To maintain high customer availability, CloudFront responds to viewer requests
by using IPv4 if our data suggests that IPv4 will provide a better user
experience. To find out what percentage of requests CloudFront is serving over
IPv6, enable CloudFront logging for your distribution and parse the
`c-ip` column, which contains the IP address of the viewer
that made the request. This percentage should grow over time, but it will
remain a minority of traffic as IPv6 is not yet supported by all viewer
networks globally. Some viewer networks have excellent IPv6 support, but
others don't support IPv6 at all. (A viewer network is analogous to your
home internet or wireless carrier.)

For more information about our support for IPv6, see the [CloudFront FAQ](https://aws.amazon.com/cloudfront/faqs/ "https://aws.amazon.com/cloudfront/faqs/"). For information
about enabling access logs, see the [Standard logging](DownloadDistValuesGeneral.md#DownloadDistValuesLoggingOnOff "DownloadDistValuesGeneral.md#DownloadDistValuesLoggingOnOff") and [Log prefix](DownloadDistValuesGeneral.md#DownloadDistValuesLogPrefix "DownloadDistValuesGeneral.md#DownloadDistValuesLogPrefix") fields.

## IPv6 origin requests

When you use a custom origin (excluding Amazon S3 and VPC origins), you can customize origin settings for your distribution to choose how CloudFront connects to your origin using IPv4 or IPv6 addresses. For custom origins (excluding Amazon S3 and VPC origins), you have the following connectivity options:

- IPv4 only (default) – This is the default configuration that CloudFront uses to connect to origins over IPv4.
- IPv6 only – Requires your origin domain to resolve to an IPv6 address. CloudFront will exclusively use IPv6 addresses for origin connections.
- Dual-stack – Enables connections over IPv4 and IPv6. CloudFront automatically chooses IPv4 or IPv6 origin connectivity to prioritize performance and availability so that you can use CloudFront as an IPv6 and IPv4 dual-stack internet gateway for your web applications.

Choose the option that aligns with your origin's network configuration and connectivity requirements. For more information, see [Designing DNS for IPv6](../../../whitepapers/latest/ipv6-on-aws/designing-dns-for-ipv6.md "../../../whitepapers/latest/ipv6-on-aws/designing-dns-for-ipv6.md") and [IPv6 security and monitoring considerations](../../../whitepapers/latest/ipv6-on-aws/ipv6-security-and-monitoring-considerations.md "../../../whitepapers/latest/ipv6-on-aws/ipv6-security-and-monitoring-considerations.md").
