# Customize planning for CDN and MediaTailor integrations

Different AWS Elemental MediaTailor workflows have unique requirements that affect content delivery network (CDN) planning. For
workflow-specific guidance, see [Working
with configurations](configurations.md "configurations.md").

Adjust your capacity plan based on your specific MediaTailor workflow:

## For MediaTailor ad insertion workflows

1.  Configure your CDN to handle personalized manifests with zero caching.
    This ensures each viewer receives unique, targeted ads. The ads are based on
    their profile and viewing context.
2.  Size your ad decision server (ADS) to handle peak request volumes. For
    guidance on ADS configuration, see [Ad insertion with MediaTailor](ad-insertion.md "ad-insertion.md"). Consider:
    - Response time requirements for your use case
    - Expected concurrent viewer capacity
    - Redundancy and failover requirements
    - Geographic distribution needs

3.  Implement request collapsing at the CDN level to handle synchronized ad
    break requests. Request collapsing combines multiple identical requests into
    a single origin request. This is crucial during:

        * Live sports events when many viewers hit ad breaks
         simultaneously
        * Popular TV show premieres with synchronized commercial
         breaks
        * Breaking news events that attract sudden viewer spikes

    For implementation details, see [Origin failover](../../../AmazonCloudFront/latest/DeveloperGuide/high_availability_origin_failover.md "../../../AmazonCloudFront/latest/DeveloperGuide/high_availability_origin_failover.md") to configure request handling during peak
    loads.

## For MediaTailor channel assembly workflows

1.  Calculate capacity requirements based on the number of channels and their
    bitrates. For guidance on channel assembly capacity planning, see [Channel assembly in MediaTailor](channel-assembly.md "channel-assembly.md"). Consider:
    - Total number of channels
    - Bitrate requirements per channel
    - Expected concurrent viewer load
    - Geographic distribution needs

2.  Configure your CDN to handle predictable traffic patterns based on
    published schedules. Channel assembly typically has more predictable
    patterns than ad insertion because:
    - Programming schedules are known in advance
    - Viewer behavior follows established patterns
    - Content doesn't change dynamically per viewer

3.  Ensure your origin has sufficient bandwidth to maintain consistent channel
    output. Implement:

        * Redundant origin servers for high-availability channels
        * Automated failover between primary and backup origins
        * Monitoring to detect origin performance issues

    For implementation guidance, see [Setting up origin redundancy](../../../mediapackage/latest/ug/cloudfront-origin-failover.md "../../../mediapackage/latest/ug/cloudfront-origin-failover.md") to create a resilient origin
    infrastructure.

## For combined MediaTailor workflows

1.  Size your infrastructure to handle the combined traffic patterns of both
    services. For guidance on combined workflows, see [Using AWS Elemental MediaTailor to insert ads](configurations.md "configurations.md").
    Consider:
    - Channel assembly baseline requirements
    - Ad insertion overhead requirements
    - Peak traffic patterns
    - Redundancy needs

2.  Configure separate CDN behaviors for linear content delivery and dynamic
    ad insertion. This separation allows you to:
    - Optimize caching policies for each content type
      independently
    - Route requests to appropriate origins based on content type
    - Monitor performance metrics separately for each workflow

3.  Set up proper routing between edge and origin CDNs to maintain optimal
    performance. Consider using:

        * Different origin paths for content segments (/content/\*) and ad
         segments (/ads/\*)
        * Separate cache behaviors for manifests and segments
        * Geographic routing to optimize latency for different
         regions

    For implementation details, see [Configuring cache behaviors](../../../AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.md#DownloadDistValuesCacheBehavior "../../../AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.md#DownloadDistValuesCacheBehavior") to set up path-based routing and
    caching rules.
