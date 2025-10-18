# Set up rate limiting

Rate limiting is one of the recommendations you may receive when configuring security
 protections. 

 CloudFront always enables rate limiting in monitor mode. When monitor mode is enabled, CloudFront
 captures metrics that tell you if the rate you configured in the **Rate
 limiting** field has been exceeded, how often, and by how much.

After you save the distribution, CloudFront starts to collect data based on the number in the
 **Rate limiting** field. 

You can enable or manage the rate limiting settings in the **Security - Web
 Application Firewall (WAF)** section on the **Security** tab of any
 CloudFront distribution.

###### Note

The **Rate limiting** option only appears in the CloudFront console if you
 specified a non-S3 custom origin for your distribution. Otherwise, you will only see the
 **Core protections** enabled for the distribution. For more information about
 origin types, see [Use various origins with CloudFront
 distributions](DownloadDistS3AndCustomOrigins.md "DownloadDistS3AndCustomOrigins.md").

###### To set up rate limiting

1. Open the CloudFront console at [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. In the navigation pane, choose **Distributions**, and then choose the
 distribution that you want to change.
3. Choose the **Security** tab.
4. In the **Security – Web Application Firewall (WAF)** section,
 choose **Edit**.
5. Under **Additional protections**, select **Rate
 limiting**. You can optionally change the rate limit. When you have fine-tuned the
 rate, choose **Save changes**.
6. In the **Security – Web Application Firewall (WAF)** section, next
 to **Rate limiting**, you can choose **Monitor mode** and
 then choose **Enable blocking** to deactivate monitor mode. CloudFront will start to
 block requests that exceed the specified rate limit.
For more information about enabling AWS WAF and rate limiting, see the  [Introducing CloudFront Security Dashboard, a Unified CDN and Security
 Experience](https://aws.amazon.com/blogs/networking-and-content-delivery/introducing-cloudfront-security-dashboard-a-unified-cdn-and-security-experience/ "https://aws.amazon.com/blogs/networking-and-content-delivery/introducing-cloudfront-security-dashboard-a-unified-cdn-and-security-experience/") blog post.
