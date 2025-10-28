# Advanced CDN features for MediaTailor

After implementing basic content delivery network (CDN) configuration, explore
these advanced features to further enhance your AWS Elemental MediaTailor streaming platform's
performance and reliability.

Media Quality-Aware Routing (MQAR)

MQAR is an Amazon CloudFront feature that automatically selects the highest
quality content source based on real-time network performance metrics.
Instead of using a fixed origin server, MQAR dynamically routes requests
to the best-performing origin based on factors like latency and
throughput. This helps ensure viewers receive the highest possible
quality stream even during network fluctuations.

If you use Amazon CloudFront, implement MQAR to automatically select the
highest quality content source based on real-time metrics. For details,
see [CloudFront
integration](cloudfront-specific-recommendations.md "cloudfront-specific-recommendations.md") in the
CloudFront integration section.

Manifest filtering

Manifest filtering allows you to customize which renditions (different
quality versions of the same content) are included in the manifests that
MediaTailor delivers to viewers. Filtering helps optimize bandwidth usage by
removing renditions that aren't appropriate for certain devices or
network conditions. For example, you might remove 4K renditions for
mobile devices or low-bandwidth connections.

For detailed information about implementing manifest filtering with
AWS Elemental MediaPackage, see [MediaPackage CDN integration](mediapackage-integration.md "mediapackage-integration.md").

Multi-CDN strategy

A multi-CDN strategy uses multiple CDN providers simultaneously to
improve reliability and performance. If one CDN experiences issues,
traffic can automatically shift to another provider. This approach is
particularly valuable for high-profile live events where reliability is
critical.

For information about implementing a multi-CDN strategy with MediaTailor,
see [Plan CDN integration](planning-cdn-integration.md "planning-cdn-integration.md").
