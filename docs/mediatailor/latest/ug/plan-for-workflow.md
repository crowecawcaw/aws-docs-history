

# Customize planning for CDN and MediaTailor integrations
<a name="plan-for-workflow"></a>

Different AWS Elemental MediaTailor workflows have unique requirements that affect content delivery network (CDN) planning. For workflow-specific guidance, see [Working with configurations](https://docs.aws.amazon.com/mediatailor/latest/ug/configurations.html).

Adjust your capacity plan based on your specific MediaTailor workflow:

## For MediaTailor ad insertion workflows
<a name="plan-ad-insertion"></a>

1. Configure your CDN to handle personalized manifests with zero caching. This ensures each viewer receives unique, targeted ads. The ads are based on their profile and viewing context.

1. Size your ad decision server (ADS) to handle peak request volumes. For guidance on ADS configuration, see [Ad insertion with MediaTailor](https://docs.aws.amazon.com/mediatailor/latest/ug/ad-insertion.html). Consider:
   + Response time requirements for your use case
   + Expected concurrent viewer capacity
   + Redundancy and failover requirements
   + Geographic distribution needs

1. Implement request collapsing at the CDN level to handle synchronized ad break requests. Request collapsing combines multiple identical requests into a single origin request. This is crucial during:
   + Live sports events when many viewers hit ad breaks simultaneously
   + Popular TV show premieres with synchronized commercial breaks
   + Breaking news events that attract sudden viewer spikes

   For implementation details, see [Origin failover](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/high_availability_origin_failover.html) to configure request handling during peak loads.

## For MediaTailor channel assembly workflows
<a name="plan-channel-assembly"></a>

1. Calculate capacity requirements based on the number of channels and their bitrates. For guidance on channel assembly capacity planning, see [Channel assembly in MediaTailor](https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly.html). Consider:
   + Total number of channels
   + Bitrate requirements per channel
   + Expected concurrent viewer load
   + Geographic distribution needs

1. Configure your CDN to handle predictable traffic patterns based on published schedules. Channel assembly typically has more predictable patterns than ad insertion because:
   + Programming schedules are known in advance
   + Viewer behavior follows established patterns
   + Content doesn't change dynamically per viewer

1. Ensure your origin has sufficient bandwidth to maintain consistent channel output. Implement:
   + Redundant origin servers for high-availability channels
   + Automated failover between primary and backup origins
   + Monitoring to detect origin performance issues

   For implementation guidance, see [Setting up origin redundancy](https://docs.aws.amazon.com/mediapackage/latest/ug/cloudfront-origin-failover.html) to create a resilient origin infrastructure.

## For combined MediaTailor workflows
<a name="plan-combined-workflow"></a>

1. Size your infrastructure to handle the combined traffic patterns of both services. For guidance on combined workflows, see [Using AWS Elemental MediaTailor to insert ads](configurations.md). Consider:
   + Channel assembly baseline requirements
   + Ad insertion overhead requirements
   + Peak traffic patterns
   + Redundancy needs

1. Configure separate CDN behaviors for linear content delivery and dynamic ad insertion. This separation allows you to:
   + Optimize caching policies for each content type independently
   + Route requests to appropriate origins based on content type
   + Monitor performance metrics separately for each workflow

1. Set up proper routing between edge and origin CDNs to maintain optimal performance. Consider using:
   + Different origin paths for content segments (/content/\*) and ad segments (/ads/\*)
   + Separate cache behaviors for manifests and segments
   + Geographic routing to optimize latency for different regions

   For implementation details, see [Configuring cache behaviors](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesCacheBehavior) to set up path-based routing and caching rules.