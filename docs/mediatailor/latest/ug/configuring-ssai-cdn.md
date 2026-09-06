

# Set up basic MediaTailor SSAI with a CDN for optimal ad delivery
<a name="configuring-ssai-cdn"></a>

This section provides step-by-step instructions for configuring AWS Elemental MediaTailor dynamic ad insertion with a content delivery network (CDN) to optimize your video monetization workflow.

For advanced ad server configuration using dynamic variables, see [MediaTailor dynamic ad variables for ADS requests](variables.md). For information about passing parameters through CDNs for ad targeting, see [MediaTailor manifest query parameters](manifest-query-parameters.md).

For conceptual information about SSAI with CDNs, see [Understand ad insertion architecture for CDN and MediaTailor integrations](ssai-cdn-architecture-overview.md).

## Prerequisites
<a name="prerequisites-ad-insertion-cdn"></a>

Before setting up ad insertion with a CDN, ensure you have:
+ An active AWS Elemental MediaTailor configuration
+ A content origin server delivering HLS or DASH content with appropriate ad markers

  For information about ad markers, see [Understanding ad insertion behavior](ad-behavior.md).
+ An ad decision server (ADS) that supports VAST or VMAP for ad targeting
+ A CDN account (such as Amazon CloudFront or another CDN provider)
+ Basic knowledge of manifest manipulation and dynamic ad insertion concepts

## Step 1: Configure CDN caching for optimal ad delivery
<a name="configure-cdn-caching"></a>

Proper CDN caching configuration is critical for optimal performance of your video monetization workflow. The caching requirements differ between server-side ad insertion (SSAI) and server-guided ad insertion (SGAI). Use these recommended settings to ensure efficient delivery of both content and personalized advertising:

### SSAI CDN caching settings
<a name="ssai-caching-settings"></a>

For server-side ad insertion workflows, proper caching configuration is critical for optimal performance. SSAI requires specific TTL values and cache key settings to ensure personalized manifests are not cached while segments are cached efficiently.

For detailed SSAI caching settings including TTL values, path patterns, and cache key configurations, see [Server-side ad insertion (SSAI) caching](cdn-optimize-caching.md#ssai-caching-optimization) in the CDN optimization guide.

Key caching principles for SSAI:
+ **Manifests**: Set TTL to 0 seconds to prevent caching of personalized content
+ **Segments**: Cache aggressively (24\+ hours) to reduce origin load
+ **Cache keys**: Include all query parameters for manifests, URL path only for segments

### SGAI CDN caching settings
<a name="sgai-caching-settings"></a>

For server-guided ad insertion workflows, caching requirements differ from SSAI because SGAI manifests can be cached for short periods while still providing personalized ad experiences.

For comprehensive SGAI caching settings including VOD and live TTL values, see the optimization guide's caching tables. SGAI allows for better cache efficiency than SSAI while maintaining ad personalization capabilities.

Key SGAI caching differences:
+ **Manifests**: Can be cached for short periods (5-30 minutes for VOD, 2-10 seconds for live)
+ **Segments**: Cache aggressively like SSAI (24\+ hours for most content)
+ **Performance benefit**: Better cache hit ratios than SSAI due to cacheable manifests

For Amazon CloudFront, you can implement these settings using cache behaviors with different TTL values and cache key policies. For other CDNs, refer to their specific documentation for implementing similar caching rules.

## Step 2: Implement hybrid approaches (if needed)
<a name="implement-hybrid-approach"></a>

If your architecture requires a hybrid approach with a separate CDN or caching layer between the content origin and MediaTailor:

1. Implement clear separation of concerns in your CDN configuration.

1. Configure specific CDN settings to prevent the technical issues described in the previous section.

1. Thoroughly test your configuration to verify that manifest personalization functions correctly.

1. Monitor performance metrics to ensure optimal delivery of multivariant playlists, media playlists, MPDs, and segments.

When implementing a hybrid approach, consider these specific configurations:
+ For the CDN between content origin and MediaTailor:
  + Configure compression passthrough for manifest files to preserve the original compression state from your origin
  + Include all query parameters in the cache key
  + Set short TTL values for live content manifests
+ For the CDN between MediaTailor and viewers:
  + Configure longer cache times for ad segments
  + Set appropriate TTLs for personalized manifests
  + Implement proper origin routing for content vs. ad segments

## Step 3: Complete your CDN setup
<a name="complete-cdn-setup"></a>

After choosing your architecture and understanding the request flow, complete your setup by following the detailed configuration steps in [Set up CDN integration](cdn-configuration.md).

For specific CDN providers, refer to these additional resources:
+ Amazon CloudFront: See [CloudFront integration](cloudfront-specific-recommendations.md) for CloudFront-specific configuration steps
+ Other CDNs: Apply the general principles outlined in this guide, adapting them to your specific CDN's configuration options

## Step 4: Verify your configuration
<a name="verification-steps"></a>

After completing your CDN setup, verify that your dynamic ad insertion workflow is functioning correctly:

1. Test playback through your CDN with a sample player

1. Verify that personalized advertising is inserted correctly at designated ad break points

1. Check CDN logs to confirm proper request routing

1. Monitor cache hit rates to ensure optimal performance for both content and ad segments

1. Confirm that ad targeting parameters are being properly passed through the workflow

For comprehensive testing and validation procedures, see [Testing and validation for CDN and MediaTailor integrations](cdn-integration-testing.md). For detailed information on monitoring your SSAI implementation, see [Monitor operations for CDN and MediaTailor integrations](ssai-cdn-monitor.md). To optimize performance, see [Optimize performance for CDN and MediaTailor integrations](ssai-cdn-performance.md).