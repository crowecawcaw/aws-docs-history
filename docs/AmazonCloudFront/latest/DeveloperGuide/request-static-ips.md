# Request Anycast static IPs to use for

allowlisting

You can request Anycast static IPs from CloudFront to use with your distributions. Anycast
static IP lists can contain only IPv4 IP addresses or both IPv4 and IPv6 IP addresses.
These IP addresses are dedicated to your AWS account and spread across geographic
regions.

You can request 21 Anycast static IP addresses to allowlist with network providers so
that you can waive data charges for viewers who access your application. Alternatively,
you can use these static IPs within outbound security firewalls to control traffic
exchange with approved applications. Anycast static IP lists can be used with one or
more distributions.

If you want to enable routing of apex domains (such as example.com) directly to your
CloudFront distributions, you can request 3 Anycast static IP addresses for this use case.
Then, add A records in your DNS to point the apex domain to CloudFront.

Anycast static IPs work with [Server Name Indication
(SNI)](https://en.wikipedia.org/wiki/Server_Name_Indication "https://en.wikipedia.org/wiki/Server_Name_Indication"). For more information, see [Use SNI to serve HTTPS requests (works for most
clients)](cnames-https-dedicated-ip-or-sni.md#cnames-https-sni "cnames-https-dedicated-ip-or-sni.md#cnames-https-sni").

## Prerequisites

To use Anycast static IP lists with your CloudFront distribution, you must select
**Use all edge locations** for the price class for the
distribution. For more information about pricing, see [CloudFront pricing](https://aws.amazon.com/cloudfront/pricing/ "https://aws.amazon.com/cloudfront/pricing/").

## Request an Anycast static IP list

Request an Anycast static IP list to use with your CloudFront distribution.

###### To request an Anycast static IP list

1. Sign in to the AWS Management Console and open the CloudFront console at
   [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. In the left navigation pane, choose **Static
   IPs**.
3. For **Request**, choose the link to contact CloudFront support
   engineering.
4. Provide your workload information (request bytes per second and requests
   per second).
5. CloudFront support engineering reviews your request. The review process might
   take up to two days.

After your request is approved, you can create an Anycast static IP list and
associate it with one or more distributions.

## Create an Anycast static IP list

Before you begin, request an Anycast static IP list as explained in the preceding
section.

###### To create an Anycast static IP list

1. Sign in to the AWS Management Console and open the CloudFront console at
   [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. In the left navigation pane, choose **Static
   IPs**.
3. Choose **Create Anycast IP list**.
4. For **Name**, enter a name.
5. For **Static IP use cases**, select the appropriate use
   case.
6. For **IP address type**, specify one of the following
   options:
   - **IPv4** – Allocate a list of only IPv4
     addresses
   - **Dualstack** – Allocate a list of both
     IPv4 and IPv6 addresses

7. Review the service terms and pricing, and choose
   **Submit**.

After your static IP list is created, you can view the allocated IP addresses on
your static IP list detail page. You can also associate distributions with the
static IP list.

## Associate an Anycast static IP

list with an existing distribution

Before you begin, request and create an Anycast static IP list as explained in the
preceding sections.

Verify that the following distribution settings are compatible with your Anycast
static IP list:

- [Price class](DownloadDistValuesGeneral.md#DownloadDistValuesPriceClass "DownloadDistValuesGeneral.md#DownloadDistValuesPriceClass") has the **Use all edge
  locations (best performance)** setting.
- If [IPv6](cloudfront-enable-ipv6.md "cloudfront-enable-ipv6.md") is enabled, you can
  associate a dualstack Anycast static IP list. An Anycast static IP list that
  only has IPv4 addresses can't be associated to distributions with IPv6
  enabled.

###### To associate an Anycast static IP list with an existing distribution

- Do one of the following:
  - Associate the static IP list from the static IP list detail
    page:
    1. Sign in to the AWS Management Console and open the CloudFront console at
       [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
    2. Choose **Static IPs** in the left
       navigation pane.
    3. Choose the name of your static IP list.
    4. Choose **Associate
       distributions**.
    5. Select one or more distributions and choose
       **Associate distributions**.

  - Associate the static IP list from the distribution detail
    page:
    1. Sign in to the AWS Management Console and open the CloudFront console at
       [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
    2. Choose **Distributions** in the left
       navigation pane.
    3. Choose the name of your distribution.
    4. On the **General** tab, under
       **Settings**, choose
       **Edit**.
    5. For **Anycast IP list**, select the
       Anycast static IP list to use with this distribution.
    6. Choose **Save changes**.

## Associate an Anycast static IP list

with a new distribution

Before you begin, request and create an Anycast static IP list as explained in the
preceding sections.

###### To associate an Anycast static IP list with a new distribution

- Create a new distribution. For more information, see [Create a CloudFront distribution in the console](distribution-web-creating-console.md#create-console-distribution "distribution-web-creating-console.md#create-console-distribution"). For
  **Settings**, you must make the following selections to
  use your Anycast static IP list:
  - For **Anycast IP list**, select your Anycast
    static IP list from the dropdown list.
  - For **Price class**, select **Use all
    edge locations (best performance)**.
  - **Note:** If your Anycast static IP
    is only using IPv4 and not dualstack, for **IPv6**,
    select **Off**.

Finish creating your distribution. You can choose any other settings and
configurations that are not required for Anycast static IP lists based on your
needs.

For more information about quotas related to Anycast static IP lists, see [Amazon CloudFront endpoints and quotas](../../../general/latest/gr/cf_region.md#limits_cloudfront "../../../general/latest/gr/cf_region.md#limits_cloudfront") in the
_AWS General Reference_.

## Update an Anycast static IP list

After you have created your Anycast static IP address and associated it to a
distribution, you can change the IP address type of your Anycast static IP
list..

###### To update an Anycast static IP list

1. Sign in to the AWS Management Console and open the CloudFront console at
   [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. In the left navigation pane, choose **Static
   IPs**.
3. Choose the name of your static IP list.
4. Choose **Edit**.
5. For **IP address type**, specify one of the following
   options:
   - **IPv4** – Allocate a list of only IPv4
     addresses
   - **Dualstack** – Allocate a list of both
     IPv4 and IPv6 addresses

###### Note

You can't choose **IPv4** if your associated
distribution has already enabled IPv6. To do so, disable IPv6 before you
can update the IP address type for your Anycast static IP. For more
information, see [Enable IPv6 for CloudFront distributions](cloudfront-enable-ipv6.md "cloudfront-enable-ipv6.md"). 6. Choose **Submit** to save your changes and update the
Anycast static IP list.
