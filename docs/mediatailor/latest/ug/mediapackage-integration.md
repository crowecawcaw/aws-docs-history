# Integrate MediaTailor with MediaPackage and CDN

AWS Elemental MediaTailor integrates with AWS Elemental MediaPackage to deliver personalized video ads through a content delivery network (CDN). MediaPackage is a just-in-time video packaging and origination service that prepares and
protects your video content for delivery over the internet. It takes your live or on-demand
video content and packages it into streaming formats like HLS and DASH, making it ready for
viewers on various devices.

When you combine MediaPackage with MediaTailor and a CDN, you create a
complete streaming workflow that delivers personalized ads at scale. The CDN distributes
your content globally, reducing latency and improving viewer experience, while MediaTailor inserts
targeted advertisements into your streams.

This topic focuses on the essential integration steps to get MediaTailor, MediaPackage, and your CDN
working together. For advanced configuration options, troubleshooting, and monitoring
guidance, see [Next steps](#emp-cdn-next-steps "#emp-cdn-next-steps").

## Understanding the MediaPackage and CDN workflow

Before configuring your integration, it's important to understand how MediaPackage, MediaTailor,
and your CDN work together:

1. **Content preparation**: MediaPackage receives your live
   or on-demand video content and packages it into streaming formats (HLS or DASH
   manifests and segments).
2. **Ad insertion**: MediaTailor requests manifests from
   MediaPackage, inserts personalized ads, and serves the modified manifests to
   viewers.
3. **Global distribution**: Your CDN caches and
   distributes both the content segments (from MediaPackage) and ad segments (from MediaTailor)
   to viewers worldwide.
4. **Viewer playback**: Video players request
   manifests through the CDN, which routes requests appropriately between MediaTailor
   (for manifests) and MediaPackage (for content segments).

This architecture provides several benefits:

- **Scalability**: The CDN handles high viewer
  loads without impacting your origin servers
- **Performance**: Content is delivered from edge
  locations closest to viewers
- **Cost efficiency**: Reduced bandwidth costs
  through caching
- **Reliability**: Multiple edge locations provide
  redundancy

## Prerequisites

Before you begin, ensure you have the following components configured:

1. **MediaPackage endpoint**: A configured MediaPackage endpoint
   that's receiving and packaging your video content. For setup instructions, see
   [Getting started with MediaPackage](../../../mediapackage/latest/ug/getting-started.md "../../../mediapackage/latest/ug/getting-started.md") in the MediaPackage user guide.
2. **MediaTailor configuration**: A MediaTailor configuration
   that uses your MediaPackage endpoint as the content origin. For setup instructions, see
   [Integrating a content source for MediaTailor ad insertion](integrating-origin.md "integrating-origin.md").
3. **CDN distribution**: A CDN distribution (such as
   CloudFront) configured to work with streaming media. For setup instructions, see
   [Creating a distribution](../../../AmazonCloudFront/latest/DeveloperGuide/distribution-web-creating-console.md "../../../AmazonCloudFront/latest/DeveloperGuide/distribution-web-creating-console.md") in the CloudFront developer guide.
4. **Ad decision server**: A configured ad decision
   server that returns VAST or VMAP responses for ad insertion.

## Step 1: Configure essential CDN

settings

Proper CDN configuration is critical for successful MediaPackage integration. Incorrect
settings can cause playback failures, poor cache performance, and increased costs.
Without the right cache policies and query parameter forwarding, your CDN might not
deliver manifests correctly or might bypass caching entirely, leading to high origin
server load and degraded viewer experience.

### Configure basic cache settings

Configuring basic caching is essential because MediaPackage uses specific cache-control
headers to optimize content delivery. Without proper cache settings, your CDN might
ignore these headers, leading to unnecessary origin requests and increased latency.
Follow these steps to ensure optimal caching behavior:

To configure basic caching that works with MediaPackage:

1. Open your CloudFront distribution settings in the CloudFront console.
2. Select or create a cache policy for your MediaPackage origin.
3. Enable the "Origin Cache-Control Headers" option.
4. Allow MediaPackage to control caching behavior through its cache-control
   headers.

This basic configuration allows MediaPackage to set appropriate cache durations for
different content types automatically. To implement advanced cache optimization with
specific TTL values and performance tuning, complete this basic setup first, then
continue to [Optimize CDN caching for MediaTailor and MediaPackage content
delivery](cdn-emp-caching.md "cdn-emp-caching.md").

### Configure essential query

parameters

Query parameter configuration is crucial for MediaPackage functionality. Your CDN must
forward specific query parameters to enable features like time-shifted viewing and
low-latency streaming. Incorrect query parameter settings can prevent these features
from working and I'm concerned reduce cache efficiency. Follow these steps to
configure query parameter forwarding:

To ensure your CDN forwards the required query parameters to MediaPackage:

1. In your CloudFront distribution settings, select or create a cache policy for
   manifest requests.
2. Under "Cache key settings," select "Include specified query
   strings."
3. Add the following essential query parameters:
   - `start` and `end` - For time-shifted viewing
     functionality. These parameters are passed through to MediaPackage to
     define specific content windows for startover and catch-up
     viewing
   - `_HLS_msn` and `_HLS_part` - For supporting
     LL-HLS playback requests
   - `m` - For capturing the modified ti/compame of the
     endpoint. MediaPackage responses always include the `?m=###` tag
     to capture the modified time of the endpoint. If content is already
     cached with a different value for this tag, CloudFront requests a new
     manifest instead of serving the cached version
   - `aws.manifestfilter` - For manifest filtering
     functionality. If you're using manifest filtering, this parameter
     must be included to configure the distribution to forward the
     `aws.manifestfilter` query string to the MediaPackage
     origin, which is required for the manifest filtering feature to
     work

4. Only include the query strings that MediaPackage uses. Including unnecessary
   query strings reduces cache efficiency by creating multiple cache variations
   for the same content.

These parameters enable basic MediaPackage functionality with your CDN. If you need to
implement content filtering for different subscription tiers or device types,
complete this basic query parameter setup first, then proceed to [Set up manifest filtering with MediaTailor, MediaPackage,
and CDN](cdn-emp-manifest-filtering.md "cdn-emp-manifest-filtering.md").

For information about how MediaTailor passes query parameters like `start`
and `end` through to MediaPackage for time-shifted viewing, see [MediaTailor query parameter handling for
origins](origin-query-parameters.md "origin-query-parameters.md") in
[MediaTailor manifest query parameters](manifest-query-parameters.md "manifest-query-parameters.md").

### Configure response timeout for

LL-HLS

Timeout configuration is critical for low-latency HLS because LL-HLS uses a
"blocking requests" mechanism where the CDN waits for new content segments. If your
timeout is too short, requests will fail before MediaPackage can respond with new segments,
causing playback interruptions and poor viewer experience. Configure appropriate
timeouts to ensure smooth LL-HLS playback:

If you're using low-latency HLS, configure your CDN timeout settings:

1. In your CDN settings, locate the origin timeout configuration.
2. Set the response timeout value to at least three times your parts
   duration.
3. For example, if your parts duration is 0.3 seconds, set the timeout to at
   least 0.9 seconds.

This ensures the CDN waits long enough for MediaPackage to respond when using the
Blocking Requests mechanism.

## Step 2: Verify your integration

Testing your integration is essential to ensure that all components work together
correctly before your viewers experience issues. A failed integration can result in
broken playback, missing ads, or poor performance. This verification process helps you
identify and resolve issues in a controlled environment.

After configuring your CDN settings, verify that your integration is working correctly
by testing the complete workflow from content request to ad insertion.

### Step 2.1: Test basic playback

Basic playback testing verifies that your CDN correctly handles manifest requests
and forwards them to MediaTailor. This test helps identify configuration issues with cache
policies, query parameter forwarding, and manifest handling. Follow these steps to
test basic manifest delivery:

Test that your basic integration is working by requesting a manifest through your
CDN:

1. Use a web browser or curl to request a manifest URL through your
   CDN.
2. Verify that the manifest loads successfully and contains both content and
   ad segments.
3. Check that content segment URLs in the manifest point to your CDN
   domain.
4. Confirm that ad segment URLs also point to your CDN domain.

If the manifest loads correctly and contains the expected URLs, your basic
integration is working. For comprehensive testing methodologies and advanced validation procedures, see [Testing and validation
for CDN and MediaTailor integrations](cdn-integration-testing.md "cdn-integration-testing.md"). To set up comprehensive monitoring of your integration's
performance and health, see [Monitor performance for MediaPackage, CDN, and MediaTailor
integrations](cdn-emp-monitoring.md "cdn-emp-monitoring.md").

### Step 2.2: Test video

playback

Video playback testing ensures that your complete integration works end-to-end,
including ad insertion and content delivery through your CDN. This test verifies
that both content segments and ad segments are properly cached and delivered, and
that the viewer experience meets your quality standards. Follow these steps to test
complete playback functionality:

Test that video playback works correctly with ads inserted:

1. Use a video player (such as Video.js or HLS.js) to play your content
   through the CDN.
2. Verify that the video plays smoothly without buffering issues.
3. Confirm that ads are inserted at the expected times during
   playback.
4. Check that both content and ad segments load from your CDN (not directly
   from origins).

If playback works smoothly with ads, your integration is functioning correctly. For comprehensive testing methodologies and advanced validation procedures, see [Testing and validation
for CDN and MediaTailor integrations](cdn-integration-testing.md "cdn-integration-testing.md"). If
you experience any playback issues, buffering, or ad insertion problems, see [Troubleshoot MediaPackage, CDN, and MediaTailor
integrations](cdn-emp-troubleshooting.md "cdn-emp-troubleshooting.md").

## Next steps

After completing the basic integration, you can implement advanced features and optimizations:

**Advanced CDN optimization**

For detailed cache optimization, TTL configuration, and performance tuning, see [Optimize CDN caching for MediaTailor and MediaPackage content
delivery](cdn-emp-caching.md "cdn-emp-caching.md").

**Manifest filtering**

To implement content filtering for tiered services, device optimization, or access control, see [Set up manifest filtering with MediaTailor, MediaPackage,
and CDN](cdn-emp-manifest-filtering.md "cdn-emp-manifest-filtering.md").

**Troubleshooting**

If you encounter issues with your integration, see [Troubleshoot MediaPackage, CDN, and MediaTailor
integrations](cdn-emp-troubleshooting.md "cdn-emp-troubleshooting.md").

**Performance monitoring**

To set up comprehensive monitoring and understand key performance metrics, see [Monitor performance for MediaPackage, CDN, and MediaTailor
integrations](cdn-emp-monitoring.md "cdn-emp-monitoring.md").
