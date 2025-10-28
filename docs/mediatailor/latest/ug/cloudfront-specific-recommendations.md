# Integrating AWS Elemental MediaTailor with

Amazon CloudFront

AWS Elemental MediaTailor integrates with Amazon CloudFront to improve content delivery performance and reliability. CloudFront is a content delivery network (CDN) that distributes your content through a
worldwide network of data centers called edge locations. When viewers request your content
from MediaTailor, CloudFront routes requests to the nearest edge location. This approach reduces
latency and improves performance for your viewers.

Integrating MediaTailor with CloudFront provides several key benefits:

- Reduced latency for viewers accessing personalized content
- Improved scalability for handling large audience sizes
- Enhanced reliability through redundant delivery paths
- Cost optimization through efficient caching strategies
- Advanced features like multi-Region failover with Media Quality-Aware Resiliency
  (MQAR)
  For comprehensive information about CloudFront features, see the [CloudFront Developer Guide](../../../AmazonCloudFront/latest/DeveloperGuide/Introduction.md "../../../AmazonCloudFront/latest/DeveloperGuide/Introduction.md"). For information about CloudFront pricing, see [CloudFront Pricing](https://aws.amazon.com/cloudfront/pricing/ "https://aws.amazon.com/cloudfront/pricing/").

For brevity, we sometimes use "manifests" to refer collectively to multivariant playlists,
media playlists, and MPDs.

###### Topics

- [Basic CloudFront setup](cloudfront-basic-setup.md "cloudfront-basic-setup.md")
- [Performance
  optimization](cloudfront-performance-optimization.md "cloudfront-performance-optimization.md")
- [Multi-Region resilience](media-quality-resiliency.md "media-quality-resiliency.md")
- [Monitoring and
  troubleshooting](monitoring-and-troubleshooting.md "monitoring-and-troubleshooting.md")
