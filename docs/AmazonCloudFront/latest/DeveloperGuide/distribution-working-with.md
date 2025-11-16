# Configure distributions

You create an Amazon CloudFront distribution to tell CloudFront from where you want content to be delivered,
and the details about how to track and manage content delivery.

When you create your CloudFront distribution, CloudFront automatically configures most distribution settings for you, based on your content origin type. For more details about the preconfigured settings, see [Preconfigured distribution settings reference](template-preconfigured-origin-settings.md "template-preconfigured-origin-settings.md"). Optionally, you can choose to manually edit your distribution settings. For more information, see [All distribution settings reference](distribution-web-values-specify.md "distribution-web-values-specify.md").

The following settings can be configured:

- **Your content origin**—The Amazon S3 bucket, AWS Elemental MediaPackage
  channel, AWS Elemental MediaStore container, Elastic Load Balancing load balancer, or HTTP server from which
  CloudFront gets the files to distribute. You can specify any combination of up to 25
  origins for a single distribution.
- **Access**—Whether you want access to the files to be
  available to everyone or restricted to some users.
- **Security**—Whether you want to enable AWS WAF
  protection and require users to use HTTPS to access your content. For multi-tenant distributions, only AWS WAF V2 web access control lists (ACLs) are supported.
- **Cache key**—Which values, if any, you want to
  include in the _cache key_. The cache key
  uniquely identifies each file in the cache for a given distribution.
- **Origin request settings**—Whether you want CloudFront to
  include HTTP headers, cookies, or query strings in requests that it sends to
  your origin.
- **Geographic restrictions**—Whether you want CloudFront to
  prevent users in selected countries from accessing your content.
- **Logs**—Whether you want CloudFront to create standard logs
  or real-time logs that show viewer activity.
  For more information, see [All distribution settings reference](distribution-web-values-specify.md "distribution-web-values-specify.md").

For the current maximum number of distributions that you can create for each AWS account,
see [General quotas on distributions](cloudfront-limits.md#limits-web-distributions "cloudfront-limits.md#limits-web-distributions").
There is no maximum number of files that you can serve per distribution.

You can use distributions to serve the following content over HTTP or HTTPS:

- Static and dynamic download content, such as HTML, CSS, JavaScript, and image files, using
  HTTP or HTTPS.
- Video on demand in different formats, such as Apple HTTP Live
  Streaming (HLS) and Microsoft Smooth Streaming. (For multi-tenant distributions, Smooth Streaming is not supported.) For more information, see
  [Deliver video on demand with CloudFront](on-demand-video.md "on-demand-video.md").
- A live event, such as a meeting, conference, or concert, in real time. For live
  streaming, you can create the distribution automatically by using an AWS CloudFormation stack. For more
  information, see [Deliver video streaming with CloudFront and AWS Media
  Services](live-streaming.md "live-streaming.md").
  The following topics provide more details about CloudFront distributions and how to configure them to meet your business needs. For more information about creating a distribution, see
  [Create a distribution](distribution-web-creating-console.md "distribution-web-creating-console.md").

###### Topics

- [Understand how multi-tenant distributions work](distribution-config-options.md "distribution-config-options.md")
- [Create a distribution](distribution-web-creating-console.md "distribution-web-creating-console.md")
- [Preconfigured distribution settings reference](template-preconfigured-origin-settings.md "template-preconfigured-origin-settings.md")
- [All distribution settings reference](distribution-web-values-specify.md "distribution-web-values-specify.md")
- [Test a distribution](distribution-web-testing.md "distribution-web-testing.md")
- [Update a distribution](HowToUpdateDistribution.md "HowToUpdateDistribution.md")
- [Tag a distribution](tagging.md "tagging.md")
- [Delete a distribution](HowToDeleteDistribution.md "HowToDeleteDistribution.md")
- [Use various origins with CloudFront
  distributions](DownloadDistS3AndCustomOrigins.md "DownloadDistS3AndCustomOrigins.md")
- [Enable IPv6 for CloudFront distributions](cloudfront-enable-ipv6.md "cloudfront-enable-ipv6.md")
- [Use CloudFront continuous deployment to safely test CDN
  configuration changes](continuous-deployment.md "continuous-deployment.md")
- [Use custom URLs by adding alternate domain names (CNAMEs)](CNAMEs.md "CNAMEs.md")
- [Use WebSockets with CloudFront
  distributions](distribution-working-with.md "distribution-working-with.md")
- [Request Anycast static IPs to use for
  allowlisting](request-static-ips.md "request-static-ips.md")
- [Using gRPC with CloudFront distributions](distribution-using-grpc.md "distribution-using-grpc.md")
