# Create custom connection group (optional)

By default, CloudFront creates a connection group for you when you create a multi-tenant distribution. The connection group controls how viewer
requests for content connect to CloudFront.

We recommend that you use the default connection group. However, if you need to isolate enterprise applications or manage groups of distribution tenants separately, you can choose to create a custom connection group. For example, you might need to move a distribution tenant to a separate connection group if it experiences a DDoS attack. This way, you can protect other distribution tenants from impact.

## Create custom connection group (optional)

Optionally, you can choose to create a custom connection group for your distribution tenants.

###### To create a custom connection group (optional)

1. Sign in to the AWS Management Console and open the CloudFront console at
   [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. In the navigation pane, choose **Settings**.
3. Turn on the **Connection group** settings.
4. In the navigation pane, choose **Connection groups**, and then
   choose **Create connection group**.
5. For **Connection group name**, enter a name for the connection
   group. You can't update this name after you create the connection group.
6. For **IPv6**, specify if you want to enable this IP protocol. For
   more information, see [Enable IPv6 (viewer requests)](DownloadDistValuesGeneral.md#DownloadDistValuesEnableIPv6 "DownloadDistValuesGeneral.md#DownloadDistValuesEnableIPv6").
7. For **Anycast static IP list**, specify if you want to deliver
   traffic to your distribution tenants from a set of IP addresses. For more information, see
   [Anycast static IP list](request-static-ips.md "request-static-ips.md").
8. (Optional) Add tags to your connection group.
9. Choose **Create connection group**.

When your connection group
is created, you can find the settings that you specified, and also the ARN and
endpoint.

- The ARN looks like the following example:
  `arn:aws:cloudfront::123456789012:connection-group/cg_2uVbA9KeWaADTbKzhj9lcKDoM25`
- The endpoint looks like the following example: d111111abcdef8.cloudfront.net

You can edit or delete your custom connection group after you create it. Before you can delete a connection group, you must first delete all associated distribution tenants from it. You can't delete the default connection group that CloudFront created for you when you created your multi-tenant distribution.

###### Important

If you change the connection group for a distribution tenant, CloudFront will continue to carry traffic
for the distribution tenant, but with increased latency. We recommend that you update the DNS
record for the distribution tenant to use the CloudFront routing endpoint from the new connection group.

Until you update the DNS record, CloudFront will route based on settings defined for the routing endpoint that the website is currently pointing to with DNS. For example, assume that your default connection group does not use Anycast static IPs but your new, custom connection group does. You must update the DNS record before CloudFront will use Anycast static IPs for the distribution tenants in your custom connection group.
