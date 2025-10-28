# CDN configuration for MSS in AWS Elemental MediaPackage

This topic explains how to configure your Content Delivery Network (CDN) to properly
handle Microsoft Smooth Streaming (MSS) content from AWS Elemental MediaPackage.

## Optimizing cache settings for MSS delivery

Configure appropriate cache control headers for MSS content:

Live manifests

Set a short TTL (Time To Live) for live manifests, typically 5-10 seconds,
to ensure viewers receive updated content.

Example: `Cache-Control: max-age=5`

VOD manifests

For video-on-demand content, you can set longer TTLs for manifests,
typically 60 seconds or more.

Example: `Cache-Control: max-age=60`

Segments

Set longer TTLs for segments since they don't change once created.

Example: `Cache-Control: max-age=86400` (24 hours)

## MIME types for MSS content

Configure your CDN to serve MSS content with the correct MIME types:

MSS manifests

MIME type: `text/xml`

File pattern: `*.ism/Manifest`

MSS segments

MIME type: `video/mp4`

File pattern: `*Fragments*`

## Configuring your CDN for PlayReady DRM

If your MSS content is encrypted with PlayReady DRM:

- Ensure your CDN passes through the PlayReady header in the manifest without
  modification
- Configure your CDN to handle the proper CORS (Cross-Origin Resource Sharing)
  headers if your players require them
- Verify that your CDN doesn't modify the encrypted segments in any way

For detailed information about MSS encryption and PlayReady DRM, see [MSS encryption and DRM in AWS Elemental MediaPackage](mss-encryption.md "mss-encryption.md").

## Setting up Amazon CloudFront for MSS delivery

Amazon CloudFront (CloudFront) works well with MSS content from MediaPackage. To configure CloudFront for
MSS:

1. Create a new CloudFront distribution or use an existing one
2. Set the origin to your MediaPackage endpoint domain
3. Configure cache behaviors with the appropriate TTLs for manifests and
   segments
4. If using DRM, ensure that CloudFront is configured to forward the necessary
   headers

Here's a real-world example of CloudFront configuration for MSS content:

###### Example CloudFront configuration for a global MSS deployment

A global media company delivering MSS content to legacy devices across multiple
regions implemented the following CloudFront configuration:

- **Origin settings**:
  - Origin domain: their MediaPackage endpoint domain
  - Origin protocol policy: Match viewer
  - Origin keep-alive timeout: 5 seconds

- **Cache behavior for manifests
  (.ism/Manifest)**:
  - Path pattern: \*.ism/Manifest
  - TTL settings: Minimum 0, Default 5, Maximum 10 (seconds)
  - Compress objects automatically: Yes

- **Cache behavior for segments**:

      + Path pattern: \*Fragments\*
      + TTL settings: Minimum 3600, Default 86400, Maximum 604800
       (seconds)
      + Compress objects automatically: No (to avoid modifying encrypted
       segments)

  This configuration ensured that manifests were refreshed frequently while segments
  were cached for longer periods, optimizing both content freshness and CDN cost
  efficiency. The company also implemented regional price classes in CloudFront to balance
  performance and cost based on their audience distribution.

For Microsoft Smooth Streaming endpoints, you should create a cache behavior with the
path pattern `out/v1/your-endpoint-id/index.ism/*` to properly route manifest
requests.

For more information about using CloudFront with MediaPackage, see [Working with AWS Elemental MediaPackage and CDNs](cdns.md "cdns.md").
