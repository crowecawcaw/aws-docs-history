

# Plan your CDN integration for AWS Elemental MediaTailor
<a name="planning-cdn-integration"></a>

You can improve the viewer experience and reduce latency with a CDN integration for AWS Elemental MediaTailor. When you implement a content delivery network (CDN), you can deliver content from locations that are closer to your viewers. This ensures faster load times, better scalability, and consistent ad delivery across different geographic regions.

You need proper planning before implementing a CDN with AWS Elemental MediaTailor. This section guides you through the key planning areas. You address these areas before beginning the actual configuration. These steps help you create an optimal viewing experience for your audience.

After you complete your planning, see [Integrating a CDN with MediaTailor](https://docs.aws.amazon.com/mediatailor/latest/ug/cdn-integration.html) for step-by-step implementation instructions.

For information about MediaTailor quotas that may affect your CDN planning, see [Quotas in AWS Elemental MediaTailor](quotas.md). For information about CloudFront quotas, see [Quotas](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html) in the CloudFront Developer Guide.

Before you start planning, understand how MediaTailor interacts with a CDN:

1. The viewers request content through your CDN instead of directly from MediaTailor

1. The CDN forwards manifest requests to MediaTailor for personalization.

1. The CDN caches and serves content segments and ad segments from edge locations.

This architecture reduces load on MediaTailor while you ensure viewers receive personalized ads with minimal latency.

Understanding the manifest terminology helps you configure your CDN correctly. Different streaming protocols use specific manifest structures that affect how you set up the caching and routing:
+ *HLS manifests* - When you work with HLS streams, you handle:
  + *Multivariant playlist*: Configure your CDN to route these top-level manifests to MediaTailor for personalization.
  + *Media playlist*: Set appropriate caching rules for these manifests that contain links to content segments.
+ *DASH manifests* - When you work with DASH streams, you handle:
  + *MPD (Media Presentation Description)*: Configure your CDN to handle these manifests according to your personalization requirements.

The CDN planning process involves these key steps, each focused on a specific task:
+ [Estimate traffic requirements for CDN and MediaTailor integrations](estimate-traffic.md): Calculate your expected viewer concurrency and the bandwidth requirements.
+ [Configure optimization strategies for CDN and MediaTailor integrations](optimize-cdn-config.md): Configure your CDN for optimal content delivery and ad personalization.
+ [Customize planning for CDN and MediaTailor integrations](plan-for-workflow.md): Adjust your CDN strategy based on your specific MediaTailor workflow.
+ [Set up monitoring and scaling for CDN and MediaTailor integrations](setup-monitoring.md): Implement monitoring and scaling strategies for reliable performance.
+ [Optimize costs for CDN and MediaTailor integrations](optimize-costs.md): Balance the performance with the cost efficiency.
+ [Test your implementation for CDN and MediaTailor integrations](test-implementation.md): Thoroughly test your CDN integration before production deployment.