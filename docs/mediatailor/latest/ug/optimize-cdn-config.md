# Configure optimization

strategies for CDN and MediaTailor integrations

When you complete your traffic estimation, configure your content delivery network (CDN) to optimize content
delivery and ad personalization with AWS Elemental MediaTailor. These optimizations help ensure smooth playback while
maintaining targeted advertising.

Implement these specific CDN optimizations that follow:

1.  Configure origin shield capabilities in your CDN to reduce load on MediaTailor and
    improve caching efficiency. Origin shield acts as an intermediary caching layer
    that:

        * Consolidate multiple viewer requests into a single origin
         request
        * Reduce the number of redundant requests to MediaTailor
        * Improve the response times for the cached content

    For implementation details on setting up origin shield with CloudFront, see
    [Using Origin Shield](../../../AmazonCloudFront/latest/DeveloperGuide/origin-shield.md "../../../AmazonCloudFront/latest/DeveloperGuide/origin-shield.md") in the CloudFront Developer Guide.

2.  Set appropriate Time To Live (TTL) values for different content types. TTL
    determines how long the CDN caches content. After this time, the CDN requests a
    fresh copy from the origin:

        * Manifests:




        	+ 0 seconds for ad insertion
        	+ 5-10 seconds for channel assembly
        In ad insertion, MediaTailor provides manifests with ads personalized to the
         viewer. If a playlist or MPD is cached and served to the wrong playback
         device, the device could encounter playback or tracking issues.
        * Content segments: 24 or more hours (these rarely change and you can
         cache them aggressively to reduce origin load)
        * Ad segments: 24 or more hours (ad content is typically reused across
         viewers and you can cache it for extended periods)

    For comprehensive TTL recommendations and caching optimization strategies across all MediaTailor workflows, see [Caching optimization for CDN and MediaTailor
    integrations](cdn-optimize-caching.md "cdn-optimize-caching.md").

For detailed instructions on configuring cache behaviors in CloudFront, see
[Cache Behavior Settings](../../../AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.md#DownloadDistValuesCacheBehavior "../../../AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.md#DownloadDistValuesCacheBehavior") in the CloudFront Developer Guide. 3. Deploy CDN edge nodes close to your viewer populations. Work with your CDN
provider to:

    * Identify optimal edge node locations based on viewer
     demographics
    * Ensure sufficient capacity in each region
    * Monitor edge performance and adjust as needed

For implementation guidance, see [CloudFront edge locations](../../../AmazonCloudFront/latest/DeveloperGuide/LocationsOfEdgeServers.md "../../../AmazonCloudFront/latest/DeveloperGuide/LocationsOfEdgeServers.md") to identify available edge locations for
your audience regions. 4. For global audiences, consider implementing a multi-CDN strategy. This
approach:

    * Uses multiple CDN providers to improve reliability
    * Routes viewers to the best-performing CDN for their location
    * Provides failover options during CDN outages
    * Can optimize costs by leveraging different pricing models

For implementation details, see [Multi-CDN strategies](https://aws.amazon.com/blogs/networking-and-content-delivery/multi-cdn-strategies/ "https://aws.amazon.com/blogs/networking-and-content-delivery/multi-cdn-strategies/") on the AWS Networking & Content Delivery
Blog.
