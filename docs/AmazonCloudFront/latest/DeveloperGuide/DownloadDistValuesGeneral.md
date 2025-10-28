# Distribution settings

The following values apply to the entire distribution.

###### Topics

- [Price class](#DownloadDistValuesPriceClass "#DownloadDistValuesPriceClass")
- [AWS WAF web ACL](#DownloadDistValuesWAFWebACL "#DownloadDistValuesWAFWebACL")
- [Alternate domain names
  (CNAMEs)](#DownloadDistValuesCNAME "#DownloadDistValuesCNAME")
- [SSL certificate](#DownloadDistValuesSSLCertificate "#DownloadDistValuesSSLCertificate")
- [Custom SSL client
  support](#DownloadDistValuesClientsSupported "#DownloadDistValuesClientsSupported")
- [Security policy (minimum
  SSL/TLS version)](#DownloadDistValues-security-policy "#DownloadDistValues-security-policy")
- [Supported HTTP
  versions](#DownloadDistValuesSupportedHTTPVersions "#DownloadDistValuesSupportedHTTPVersions")
- [Default root
  object](#DownloadDistValuesDefaultRootObject "#DownloadDistValuesDefaultRootObject")
- [Standard logging](#DownloadDistValuesLoggingOnOff "#DownloadDistValuesLoggingOnOff")
- [Log prefix](#DownloadDistValuesLogPrefix "#DownloadDistValuesLogPrefix")
- [Cookie logging](#DownloadDistValuesCookieLogging "#DownloadDistValuesCookieLogging")
- [Enable IPv6 (viewer requests)](#DownloadDistValuesEnableIPv6 "#DownloadDistValuesEnableIPv6")
- [Enable IPv6 for custom origins (origin requests)](#DownloadDistValuesEnableIPv6-origin "#DownloadDistValuesEnableIPv6-origin")
- [Comment](#DownloadDistValuesComment "#DownloadDistValuesComment")
- [Distribution state](#DownloadDistValuesEnabled "#DownloadDistValuesEnabled")

## Price class

Choose the price class that corresponds with the maximum price that you want
to pay for CloudFront service. By default, CloudFront serves your objects from edge
locations in all CloudFront Regions.

For more information about price classes and about how your choice of price
class affects CloudFront performance for your distribution, see [CloudFront pricing](https://aws.amazon.com/cloudfront/pricing/ "https://aws.amazon.com/cloudfront/pricing/").

## AWS WAF web ACL

You can protect your CloudFront distribution with [AWS WAF](../../../waf/latest/developerguide/what-is-aws-waf.md "../../../waf/latest/developerguide/what-is-aws-waf.md"), a web
application firewall that allows you to secure your web applications and APIs to
block requests before they reach your servers. You can [Enable AWS WAF for distributions](WAF-one-click.md "WAF-one-click.md") when creating or
editing a CloudFront distribution.

Optionally, you can later configure additional security protections for other
threats specific to your application in the AWS WAF console at
[https://console.aws.amazon.com/wafv2/](https://console.aws.amazon.com/wafv2/ "https://console.aws.amazon.com/wafv2/").

For more information about AWS WAF, see the [AWS WAF Developer Guide](../../../waf/latest/developerguide.md "../../../waf/latest/developerguide.md").

## Alternate domain names

(CNAMEs)

Optional. Specify one or more domain names that you want to use for URLs for
your objects instead of the domain name that CloudFront assigns when you create your
distribution. You must own the domain name, or have authorization to use it,
which you verify by adding an SSL/TLS certificate.

For example, if you want the URL for the object:

`/images/image.jpg`

To look like this:

`https://www.example.com/images/image.jpg`

Instead of like this:

`https://d111111abcdef8.cloudfront.net/images/image.jpg`

Add a CNAME for `www.example.com`.

###### Important

If you add a CNAME for `www.example.com` to your distribution,
you also must do the following:

- Create (or update) a CNAME record with your DNS service to route
  queries for `www.example.com` to
  `d111111abcdef8.cloudfront.net`.
- Add a certificate to CloudFront from a trusted certificate authority
  (CA) that covers the domain name (CNAME) that you add to your
  distribution, to validate your authorization to use the domain
  name.
  You must have permission to create a CNAME record with the DNS service
  provider for the domain. Typically, this means that you own the domain, or
  that you're developing an application for the domain owner.

For the current maximum number of alternate domain names that you can add to a
distribution, or to request a higher quota (formerly known as limit), see [General quotas on distributions](cloudfront-limits.md#limits-web-distributions "cloudfront-limits.md#limits-web-distributions").

For more information about alternate domain names, see [Use custom URLs by adding alternate domain names (CNAMEs)](CNAMEs.md "CNAMEs.md"). For more information about CloudFront URLs, see [Customize the URL format for files in CloudFront](LinkFormat.md "LinkFormat.md").

## SSL certificate

If you specified an alternate domain name to use with your distribution,
choose **Custom SSL Certificate**, and then, to validate your
authorization to use the alternate domain name, choose a certificate that covers
it. If you want viewers to use HTTPS to access your objects, choose the settings
that support that.

- **Default CloudFront Certificate
  (\*.cloudfront.net)** – Choose this option if you
  want to use the CloudFront domain name in the URLs for your objects, such as
  `https://d111111abcdef8.cloudfront.net/image1.jpg`.
- **Custom SSL Certificate** –
  Choose this option if you want to use your own domain name in the URLs
  for your objects as an alternate domain name, such as
  `https://example.com/image1.jpg`. Then choose a
  certificate to use that covers the alternate domain name. The list of
  certificates can include any of the following:

      + Certificates provided by AWS Certificate Manager
      + Certificates that you purchased from a third-party certificate
       authority and uploaded to ACM
      + Certificates that you purchased from a third-party certificate
       authority and uploaded to the IAM certificate store

  If you choose this setting, we recommend that you use only an
  alternate domain name in your object URLs
  (https://example.com/logo.jpg). If you use your CloudFront distribution domain
  name (https://d111111abcdef8.cloudfront.net/logo.jpg) and a client uses
  an older viewer that doesn't support SNI, how the viewer responds
  depends on the value that you choose for **Clients
  Supported**:

      + **All Clients**: The viewer
       displays a warning because the CloudFront domain name doesn't match
       the domain name in your SSL/TLS certificate.
      + **Only Clients that Support Server Name
       Indication (SNI)**: CloudFront drops the connection with
       the viewer without returning the object.

## Custom SSL client

support

Applies only when you choose **Custom SSL Certificate
(example.com)** for **SSL Certificate**. If you
specified one or more alternate domain names and a custom SSL certificate for
the distribution, choose how you want CloudFront to serve HTTPS requests:

- **Clients that Support Server Name Indication (SNI) -
  (Recommended)** – With this setting, virtually all modern
  web browsers and clients can connect to the distribution, because they
  support SNI. However, some viewers might use older web browsers or
  clients that don’t support SNI, which means they can’t connect to the
  distribution.

To apply this setting using the CloudFront API, specify
`sni-only` in the `SSLSupportMethod` field. In
AWS CloudFormation, the field is named `SslSupportMethod` (note the
different capitalization).

- **Legacy Clients Support** – With this setting, older
  web browsers and clients that don’t support SNI can connect to the
  distribution. However, this setting incurs additional monthly charges.
  For the exact price, go to the [Amazon CloudFront Pricing](https://aws.amazon.com/cloudfront/pricing/ "https://aws.amazon.com/cloudfront/pricing/")
  page, and search the page for **Dedicated IP custom
  SSL**.

To apply this setting using the CloudFront API, specify `vip` in
the `SSLSupportMethod` field. In AWS CloudFormation, the field is named
`SslSupportMethod` (note the different
capitalization).

For more information, see [Choose how CloudFront serves HTTPS
requests](cnames-https-dedicated-ip-or-sni.md "cnames-https-dedicated-ip-or-sni.md").

## Security policy (minimum

SSL/TLS version)

Specify the security policy that you want CloudFront to use for HTTPS connections
with viewers (clients). A security policy determines two settings:

- The minimum SSL/TLS protocol that CloudFront uses to communicate with
  viewers.
- The ciphers that CloudFront can use to encrypt the content that it returns
  to viewers.

For more information about the security policies, including the protocols and
ciphers that each one includes, see [Supported
protocols and ciphers between viewers and CloudFront](secure-connections-supported-viewer-protocols-ciphers.md "secure-connections-supported-viewer-protocols-ciphers.md").

The security policies that are available depend on the values that you specify
for **SSL Certificate** and **Custom SSL Client
Support** (known as `CloudFrontDefaultCertificate` and
`SSLSupportMethod` in the CloudFront API):

- When **SSL Certificate** is **Default
  CloudFront Certificate (\*.cloudfront.net)** (when
  `CloudFrontDefaultCertificate` is `true` in
  the API), CloudFront automatically sets the security policy to TLSv1.
- When **SSL Certificate** is **Custom SSL
  Certificate (example.com)**
  _and_
  **Custom SSL Client Support** is **Clients that
  Support Server Name Indication (SNI) - (Recommended)**
  (when `CloudFrontDefaultCertificate` is `false`
  _and_
  `SSLSupportMethod` is `sni-only` in the API), you
  can choose from the following security policies:

      + TLSv1.3\_2025
      + TLSv1.2\_2025
      + TLSv1.2\_2021
      + TLSv1.2\_2019
      + TLSv1.2\_2018
      + TLSv1.1\_2016
      + TLSv1\_2016
      + TLSv1

- When **SSL Certificate** is **Custom SSL
  Certificate (example.com)**
  _and_
  **Custom SSL Client Support** is **Legacy
  Clients Support** (when
  `CloudFrontDefaultCertificate` is `false`
  _and_
  `SSLSupportMethod` is `vip` in the API), you can
  choose from the following security policies:

      + TLSv1
      + SSLv3

  In this configuration, the TLSv1.3_2025, TLSv1.2_2025, TLSv1.2_2021, TLSv1.2_2019,
  TLSv1.2_2018, TLSv1.1_2016, and TLSv1_2016 security policies aren’t available in
  the CloudFront console or API. If you want to use one of these security policies, you
  have the following options:

      + Evaluate whether your distribution needs Legacy Clients
       Support with dedicated IP addresses. If your viewers support
       [server name indication (SNI)](https://en.wikipedia.org/wiki/Server_Name_Indication "https://en.wikipedia.org/wiki/Server_Name_Indication"), we recommend that you
       update your distribution’s **Custom SSL Client
       Support** setting to **Clients that Support
       Server Name Indication (SNI)** (set
       `SSLSupportMethod` to `sni-only` in
       the API). This enables you to use any of the available TLS
       security policies, and it can also reduce your CloudFront
       charges.
      + If you must keep Legacy Clients Support with dedicated IP addresses, you can request
       one of the other TLS security policies (TLSv1.3\_2025, TLSv1.2\_2025,
       TLSv1.2\_2021, TLSv1.2\_2019, TLSv1.2\_2018, TLSv1.1\_2016, or TLSv1\_2016)
       by creating a case in the [AWS
       Support Center](https://console.aws.amazon.com/support/home "https://console.aws.amazon.com/support/home").


      ###### Note

      Before you contact AWS Support to request this change,
       consider the following:



      	- When you add one of these security policies (TLSv1.3\_2025, TLSv1.2\_2025,
      	 TLSv1.2\_2021, TLSv1.2\_2019, TLSv1.2\_2018, TLSv1.1\_2016, or
      	 TLSv1\_2016) to a Legacy Clients Support distribution, the
      	 security policy is applied to *all* non-SNI viewer requests for *all* Legacy Clients Support
      	 distributions in your AWS account. However, when viewers
      	 send SNI requests to a distribution with Legacy Clients
      	 Support, the security policy of that distribution applies.
      	 To make sure that your desired security policy is applied to
      	 *all* viewer requests
      	 sent to *all* Legacy
      	 Clients Support distributions in your AWS account, add the
      	 desired security policy to each distribution
      	 individually.
      	- By definition, the new security policy doesn’t
      	 support the same ciphers and protocols as the old
      	 one. For example, if you chose to upgrade a
      	 distribution’s security policy from TLSv1 to
      	 TLSv1.1\_2016, that distribution will no longer
      	 support the DES-CBC3-SHA cipher. For more
      	 information about the ciphers and protocols that
      	 each security policy supports, see [Supported
      	 protocols and ciphers between viewers and CloudFront](secure-connections-supported-viewer-protocols-ciphers.md "secure-connections-supported-viewer-protocols-ciphers.md").

## Supported HTTP

versions

Choose the HTTP versions that you want your distribution to support when
viewers communicate with CloudFront.

For viewers and CloudFront to use HTTP/2, viewers must support TLSv1.2 or later, and Server Name
Indication (SNI).

For viewers and CloudFront to use HTTP/3, viewers must support TLSv1.3 and Server
Name Indication (SNI). CloudFront supports HTTP/3 connection migration to allow the
viewer to switch networks without losing connection. For more information about
connection migration, see [Connection Migration](https://www.rfc-editor.org/rfc/rfc9000.html#name-connection-migration "https://www.rfc-editor.org/rfc/rfc9000.html#name-connection-migration") at RFC 9000.

###### Note

For more information about supported TLSv1.3 ciphers, see [Supported
protocols and ciphers between viewers and CloudFront](secure-connections-supported-viewer-protocols-ciphers.md "secure-connections-supported-viewer-protocols-ciphers.md").

###### Note

If you use Amazon Route 53, you can use HTTPS records to allow protocol negotiation as part of the DNS lookup if the client supports it. For more information, see [Create alias resource record set](CreatingCNAME.md#alternate-domain-https "CreatingCNAME.md#alternate-domain-https").

## Default root

object

Optional. The object that you want CloudFront to request from your origin (for
example, `index.html`) when a viewer requests the root URL of your
distribution (`https://www.example.com/`) instead of an object in
your distribution
(`https://www.example.com/product-description.html`). Specifying a
default root object avoids exposing the contents of your distribution.

The maximum length of the name is 255 characters. The name can contain any of
the following characters:

- A-Z, a-z
- 0-9
- \_ - . \* $ / ~ " '
- &, passed and returned as `&amp;`

When you specify the default root object, enter only the object name, for
example, `index.html`. Do not add a `/` before the
object name.

For more information, see [Specify a default root object](DefaultRootObject.md "DefaultRootObject.md").

## Standard logging

Specify if you want CloudFront to log information about each request for an object
and store the log files. You can enable or disable logging at any time. There is
no extra charge if you enable logging, but you may accrue charges for storing
and accessing the files. You can delete the logs at any time.

CloudFront supports the following standard logging options:

- [Standard logging (v2)](standard-logging.md "standard-logging.md") –
  You can send logs to delivery destinations, including Amazon CloudWatch Logs,
  Amazon Data Firehose, and Amazon Simple Storage Service (Amazon S3).
- [Standard logging (legacy)](AccessLogs.md "AccessLogs.md") – You can only send
  logs to an Amazon S3 bucket.

## Log prefix

(Optional) If you enable standard logging (legacy), specify the string, if any, that you want CloudFront to
prefix to the access log file names for this distribution, for example,
`exampleprefix/`. The trailing slash ( / ) is optional but
recommended to simplify browsing your log files. For more information, see [Configure standard logging (legacy)](standard-logging-legacy-s3.md "standard-logging-legacy-s3.md").

## Cookie logging

If you want CloudFront to include cookies in access logs, choose
**On**. If you choose to include cookies in logs, CloudFront logs
all cookies regardless of how you configure the cache behaviors for this
distribution: forward all cookies, forward no cookies, or forward a specified
list of cookies to the origin.

Amazon S3 doesn't process cookies, so unless your distribution also includes an
Amazon EC2 or other custom origin, we recommend that you choose
**Off** for the value of **Cookie
Logging**.

For more information about cookies, see [Cache content based on cookies](Cookies.md "Cookies.md").

## Enable IPv6 (viewer requests)

If
you want CloudFront to respond to viewer requests from IPv4 and IPv6 IP addresses,
select **Enable IPv6**. For more information, see [Enable IPv6 for CloudFront distributions](cloudfront-enable-ipv6.md "cloudfront-enable-ipv6.md").

## Enable IPv6 for custom origins (origin requests)

When you use a custom origin (excluding Amazon S3 and VPC origins), you can customize origin settings for your distribution to choose how CloudFront connects to your origin using IPv4 or IPv6 addresses. For more information, see [Enable IPv6 for CloudFront distributions](cloudfront-enable-ipv6.md "cloudfront-enable-ipv6.md").

## Comment

Optional. When you create a distribution, you can include a comment of up to
128 characters. You can update the comment at any time.

## Distribution state

Indicates whether you want the distribution to be enabled or disabled once
it's deployed:

- _Enabled_ means that as soon as the distribution is
  fully deployed you can deploy links that use the distribution's domain
  name and users can retrieve content. Whenever a distribution is enabled,
  CloudFront accepts and handles any end-user requests for content that use the
  domain name associated with that distribution.

When you create, modify, or delete a CloudFront distribution, it takes time
for your changes to propagate to the CloudFront database. An immediate request
for information about a distribution might not show the change.
Propagation usually completes within minutes, but a high system load or
network partition might increase this time.

- _Disabled_ means that even though the distribution
  might be deployed and ready to use, users can't use it. Whenever a
  distribution is disabled, CloudFront doesn't accept any end-user requests that
  use the domain name associated with that distribution. Until you switch
  the distribution from disabled to enabled (by updating the
  distribution's configuration), no one can use it.

You can toggle a distribution between disabled and enabled as often as you
want. Follow the process for updating a distribution's configuration. For more
information, see [Update a distribution](HowToUpdateDistribution.md "HowToUpdateDistribution.md").
