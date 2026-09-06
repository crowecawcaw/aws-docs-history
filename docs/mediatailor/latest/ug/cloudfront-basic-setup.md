

# Set up basic CloudFront integration with MediaTailor
<a name="cloudfront-basic-setup"></a>

AWS Elemental MediaTailor integration with Amazon CloudFront improves content delivery performance for your viewers. This topic guides you through setting up a basic CloudFront distribution for MediaTailor. With this integration, your viewers can access personalized content through the CloudFront network. You'll also learn how to configure proper caching for different content types.

For information about passing query parameters through CloudFront for authorization and routing, see [MediaTailor manifest query parameters](manifest-query-parameters.md). For advanced routing using dynamic variables, see [MediaTailor domain variables for multiple content sources](variables-domains.md).

## Prerequisites
<a name="cf-basic-prerequisites"></a>

Before configuring CloudFront with MediaTailor, ensure you have the following:
+ An active AWS account with permissions to create and manage CloudFront distributions
+ A configured MediaTailor playback configuration (see [Using AWS Elemental MediaTailor to insert ads](configurations.md))
+ Your content origin server properly set up and accessible
+ Basic understanding of video streaming concepts (HLS/DASH)

## Configuring CloudFront distribution
<a name="cf-basic-configuration"></a>

Follow these steps to create and configure a CloudFront distribution for MediaTailor:

**To create a CloudFront distribution for MediaTailor**

1. Sign in to the AWS Management Console and open the CloudFront console at [https://console.aws.amazon.com/cloudfront/v3/home](https://console.aws.amazon.com/cloudfront/v3/home).

1. Choose **Create Distribution**.

1. For **Origin domain**, enter your MediaTailor endpoint URL (for example, `a1b2c3d4.mediatailor.us-west-2.amazonaws.com`).

1. For **Protocol**, select **HTTPS only**.

1. For **Name**, enter a name that helps you identify this origin (for example, `mediatailor-origin`).

1. Configure the default cache behavior settings:

   1. For **Path pattern**, use the default value (`*`).

   1. For **Compress objects automatically**, select **Yes**.

   1. For **Viewer protocol policy**, select **Redirect HTTP to HTTPS**.

   1. For **Allowed HTTP methods**, select **GET, HEAD**.

   1. For **Cache policy**, select **CachingDisabled**.

   1. For **Origin request policy**, select **AllViewer** to forward all headers for the default behavior.
**Note**  
The default behavior uses AllViewer to safely handle any content that doesn't match specific path patterns. Specific cache behaviors for manifests and segments will be configured separately with appropriate policies.

1. Configure the distribution settings:

   1. For **Price class**, select the option that best matches your audience locations.

   1. For **AWS WAF web ACL**, select an existing web ACL or leave as **Do not enable security protections**.

   1. For **Default root object**, leave empty.

   1. For **Standard logging**, select **On** to enable logging.

1. Choose **Create Distribution**.

## Configuring cache behaviors
<a name="cf-cache-behaviors"></a>

After creating your distribution, you need to configure additional cache behaviors to handle different types of content appropriately. This section covers basic cache behavior setup for CloudFront.

For comprehensive caching optimization including advanced TTL settings, cache key configurations, and performance tuning, see [Caching optimization for CDN and MediaTailor integrations](cdn-optimize-caching.md) in the CDN optimization guide.

### Configuring manifest cache behavior
<a name="cf-manifest-behavior"></a>

Do not cache manifests because they contain personalized content. Follow these steps to configure the cache behavior:

**To configure manifest cache behavior**

1. In the CloudFront console, select your distribution.

1. Choose the **Behaviors** tab.

1. Choose **Create behavior**.

1. For **Path pattern**, enter `*.m3u8` to match HLS multivariant and media playlists.

1. For **Origin**, select your MediaTailor origin.

1. For **Cache policy**, select **CachingDisabled**.

1. For **Origin request policy**, select **AllViewer** to forward all required headers for dynamic content.

1. Choose **Create**.

1. Repeat these steps for DASH manifests using the path pattern `*.mpd` to match MPDs.

This configuration ensures that each viewer receives a personalized manifest with their specific ad content. The CDN doesn't cache these manifests, so each request goes directly to MediaTailor.

### Configuring segment cache behavior
<a name="cf-segment-behavior"></a>

Configure separate cache behaviors for ad segments and content segments to optimize performance and ensure proper CORS handling.

#### Configuring ad segment cache behavior
<a name="cf-ad-segment-behavior"></a>

Ad segments served through the `/tm/*` path pattern require specific configuration to handle CORS properly. Follow these steps:

**To configure ad segment cache behavior**

1. In the CloudFront console, select your distribution.

1. Choose the **Behaviors** tab.

1. Choose **Create behavior**.

1. For **Path pattern**, enter `/tm/*` to match ad segments served by MediaTailor.

1. For **Origin**, select your MediaTailor segments origin (using the `segments.mediatailor.region.amazonaws.com` hostname).

1. For **Cache policy**, select **CachingOptimized**.

1. For **Origin request policy**, select **None**.

1. For **Response headers policy**, select **CORS-with-preflight-and-SecurityHeadersPolicy** to ensure proper CORS headers are included in responses.

1. Choose **Create**.

#### Configuring content segment cache behavior
<a name="cf-content-segment-behavior"></a>

Content segments can use standard caching policies for optimal performance. Configure separate behaviors for different segment formats:

**To configure content segment cache behavior**

1. In the CloudFront console, select your distribution.

1. Choose the **Behaviors** tab.

1. Choose **Create behavior**.

1. For **Path pattern**, enter `*.ts` to match HLS content segments.

1. For **Origin**, select your content origin.

1. For **Cache policy**, select **CachingOptimized**.

1. For **Origin request policy**, select **None**.

1. For **Response headers policy**, select **CORS-with-preflight-and-SecurityHeadersPolicy** to ensure consistent CORS handling across all content types.

1. Choose **Create**.

1. Repeat these steps for other content segment formats using appropriate path patterns:
   + `*.mp4` for MP4 segments
   + `*.m4s` for DASH segments
   + `*.cmfv` and `*.cmfa` for CMAF segments

This configuration ensures that ad segments and content segments are cached appropriately with proper CORS handling. Ad segments use the MediaTailor segments origin with CORS protection, while content segments use your content origin with optimized caching policies.

## Updating MediaTailor configuration
<a name="cf-mediatailor-config"></a>

After setting up your CloudFront distribution, update your MediaTailor configuration to use the CloudFront domain:

**To update your MediaTailor configuration**

1. Open the [MediaTailor console](https://console.aws.amazon.com/mediatailor/home).

1. Select the configuration you want to update.

1. In the **CDN configuration** section, enter your CloudFront distribution domain name (for example, `d1234abcdef.cloudfront.net`) in the **CDN content segment prefix** field.

1. Save your changes.

With this configuration, MediaTailor generates manifests with URLs that point to your CloudFront distribution instead of directly to the origin.

## Testing your integration
<a name="cf-basic-testing"></a>

After configuring your CloudFront distribution and updating your MediaTailor configuration, test the integration:

**To test your CloudFront and MediaTailor integration**

1. Request a manifest through your CloudFront distribution (for example, `https://d1234abcdef.cloudfront.net/v1/master/12345/my-config/index.m3u8`).

1. Verify that the manifest contains segment URLs that point to your CloudFront domain.

1. Play the content through a video player and verify that both content and ads play correctly.

1. Check CloudFront logs to ensure requests are being routed correctly.

## Example configuration
<a name="cf-basic-example"></a>

Here's an example of a CloudFront distribution configuration for MediaTailor with proper cache behaviors:

**Example CloudFront distribution configuration example**  

```
{
  "DefaultCacheBehavior": {
    "TargetOriginId": "mediatailor-origin",
    "ViewerProtocolPolicy": "redirect-to-https",
    "AllowedMethods": {
      "Quantity": 2,
      "Items": ["GET", "HEAD"]
    },
    "CachePolicyId": "4135ea2d-6df8-44a3-9df3-4b5a84be39ad",
    "OriginRequestPolicyId": "59781a5b-3903-41f3-afcb-af62929ccde1",
    "Comment": "Default behavior with CachingDisabled and AllViewer"
  },
  "CacheBehaviors": [
    {
      "PathPattern": "*.m3u8",
      "TargetOriginId": "mediatailor-origin",
      "ViewerProtocolPolicy": "redirect-to-https",
      "CachePolicyId": "4135ea2d-6df8-44a3-9df3-4b5a84be39ad",
      "OriginRequestPolicyId": "59781a5b-3903-41f3-afcb-af62929ccde1",
      "Comment": "Manifest behavior with CachingDisabled and AllViewer"
    },
    {
      "PathPattern": "*.ts",
      "TargetOriginId": "mediatailor-origin", 
      "ViewerProtocolPolicy": "redirect-to-https",
      "CachePolicyId": "658327ea-f89d-4fab-a63d-7e88639e58f6",
      "OriginRequestPolicyId": "88a5eaf4-2fd4-4709-b370-b4c650ea3fcf",
      "Comment": "Segment behavior with CachingOptimized and HostHeaderOnly"
    }
  ]
}
```

This example shows:
+ **Default behavior**: Uses `CachingDisabled` and `AllViewer` to safely handle any content that doesn't match specific path patterns
+ **Manifest behavior (\*.m3u8)**: Uses `CachingDisabled` and `AllViewer` for dynamic content
+ **Segment behavior (\*.ts)**: Uses `CachingOptimized` and `CORS-with-preflight-and-SecurityHeadersPolicy`

## Next steps
<a name="cf-basic-next-steps"></a>

After setting up your basic CloudFront integration with MediaTailor, consider these next steps:
+ Optimize performance with additional CloudFront features (see [Optimizing MediaTailor performance with CloudFront features](cloudfront-performance-optimization.md))
+ Implement multi-Region resilience with MQAR (see [Implement multi-Region resilience for MediaTailor with MQAR](media-quality-resiliency.md))
+ Set up monitoring and troubleshooting (see [Monitor and troubleshoot your CloudFront and MediaTailor integration](monitoring-and-troubleshooting.md))