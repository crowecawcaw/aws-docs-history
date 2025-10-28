# MediaTailor configuration aliases

overview

AWS Elemental MediaTailor configuration aliases enable dynamic variable replacement in URL domains and
other supported fields. Use this feature to use multiple domains and dynamically configure
URLs during session initialization.

## Use cases

Configuration aliases enable sophisticated multi-configuration architectures for the
following scenarios:

- **Geographic routing:** Route requests to
  different origins or ad servers based on viewer location using region-specific
  aliases. For implementation guidance, see [CloudFront Origin Failover](../../../AmazonCloudFront/latest/DeveloperGuide/high_availability_origin_failover.md "../../../AmazonCloudFront/latest/DeveloperGuide/high_availability_origin_failover.md").
- **Content-based routing:** Direct different
  content types to specialized origins or processing pipelines. For routing
  behavior configuration, see [Set up CDN routing behaviors for MediaTailor](cdn-routing-behaviors.md "cdn-routing-behaviors.md").
- **Failover scenarios:** Implement backup origins
  and ad servers with automatic failover using alias switching. For detailed
  implementation, see [Implement multi-Region resilience for MediaTailor with
  MQAR](media-quality-resiliency.md "media-quality-resiliency.md") and [Plan your CDN integration for AWS Elemental MediaTailor](planning-cdn-integration.md "planning-cdn-integration.md").
- **A/B testing:** Test different ad servers,
  origins, or configurations by routing traffic based on player parameters. For
  load testing guidance, see [Prepare and run performance tests for Amazon CloudFront with real user
  monitoring](https://aws.amazon.com/blogs/networking-and-content-delivery/prepare-and-run-performance-tests-for-amazon-cloudfront-with-real-user-monitoring/ "https://aws.amazon.com/blogs/networking-and-content-delivery/prepare-and-run-performance-tests-for-amazon-cloudfront-with-real-user-monitoring/").
- **Device-specific optimization:** Optimize
  content delivery and ad serving for different device types or capabilities. For
  comprehensive guidance, see [Set up manifest filtering with MediaTailor, MediaPackage,
  and CDN](cdn-emp-manifest-filtering.md "cdn-emp-manifest-filtering.md").
- **Load balancing:** Distribute load across
  multiple origins or ad servers using dynamic routing. For implementation
  guidance, see [Implement multi-Region resilience for MediaTailor with
  MQAR](media-quality-resiliency.md "media-quality-resiliency.md") and [Plan your CDN integration for AWS Elemental MediaTailor](planning-cdn-integration.md "planning-cdn-integration.md").

## Supported fields

You can use dynamic variables in the following configuration fields:

- `VideoContentSourceUrl`
- `AdDecisionServerUrl`
- `LivePreroll.AdDecisionServerUrl`
- `AdSegmentUrlPrefix`
- `ContentSegmentUrlPrefix`
- `TranscodeProfileName`
- `SlateAdUrl`
- `StartUrl`
- `EndUrl`
  The following sections describe how to use configuration aliases.

###### Topics

- [Creating and using](creating-configuration-aliases.md "creating-configuration-aliases.md")
- [Example flow](configuration-aliases-examples.md "configuration-aliases-examples.md")
