# Set up CDN integration with MediaTailor

This section provides guidance on integrating AWS Elemental MediaTailor with a content delivery network
(CDN).

Effective CDN integration with MediaTailor is essential for delivering high-quality streaming
experiences with personalized ads at scale. This guide walks you through the complete
process of setting up, configuring, and optimizing your CDN integration.

For additional information, see the following links:

- For information about passing query parameters through CDNs for authorization and
  ad targeting, see [MediaTailor manifest query parameters](manifest-query-parameters.md "manifest-query-parameters.md").
- For advanced routing using dynamic variables and configuration aliases, see [MediaTailor dynamic ad variables for ADS requests](variables.md "variables.md").
- For information about creating MediaTailor configurations, see [Using AWS Elemental MediaTailor to insert ads](configurations.md "configurations.md").
- For information about creating a CloudFront distribution, see [Creating a distribution](../../../AmazonCloudFront/latest/DeveloperGuide/distribution-web-creating-console.md "../../../AmazonCloudFront/latest/DeveloperGuide/distribution-web-creating-console.md") in the CloudFront Developer Guide.
  To ensure clarity in this guide, the following terminology is used to describe different
  types of manifests:

- **HLS manifests**:
  - _Multivariant playlist_: The top-level manifest that
    contains links to media playlists
  - _Media playlist_: The second-level manifest with links
    to content segments

- **DASH manifests**:

      + *MPD (Media Presentation Description)*: The standard
       term for DASH manifests

  Integrating MediaTailor with a CDN provides the following benefits:

- Reduced latency for viewers
- Improved scalability for high-traffic events
- Enhanced reliability through redundant delivery paths
- Optimized costs by reducing origin traffic
- Better protection against DDoS attacks

## CDN integration components and

requirements

A successful CDN integration with MediaTailor involves configuring the following key
components:

**CDN routing behaviors**

Rules that determine how different types of requests (manifests, content
segments, ad segments) are routed through your CDN.

**CDN mapping in MediaTailor**

Configuration in MediaTailor that ensures manifests reference your CDN domain
instead of directly referencing origin servers.

**Security settings**

Configurations that protect your content and infrastructure, including
transport security, access control, and monitoring.

**Testing and validation**

Procedures to verify that your CDN integration is working correctly before
deploying to production.

## Prerequisites for CDN integration

Before configuring your CDN integration, ensure you have the following:

1.  A MediaTailor configuration with the following settings:

        * Your content origin as the **Content source**
        * Your ADS as the **Ad decision server**

    You need the origin and ADS URLs in the CDN integration steps as well.

2.  Access to your CDN's configuration interface
3.  Understanding of your CDN's specific terminology for behaviors, rules, and
    cache settings
4.  Knowledge of your content structure, including file extensions used for
    segments (such as .ts, .mp4, or .m4s)

## CDN integration setup steps

The process of integrating MediaTailor with a CDN follows these high-level steps:

1. **Configure CDN routing behaviors** - Set up your
   CDN to route different types of requests appropriately.
2. **Configure CDN mapping in MediaTailor** - Update your
   MediaTailor configuration to use your CDN domain names.
3. **Implement security best practices** - Configure
   security settings to protect your content and infrastructure.
4. **Test your integration** - Verify that your CDN
   integration is working correctly.

## Required headers for MediaTailor CDN

integration

For MediaTailor to function correctly with your CDN, you must configure your CDN to forward
specific HTTP headers. These headers are essential for proper functionality including
compression, device detection, ad personalization, and geo-targeting.

Configure your CDN to forward the following headers to MediaTailor:

**`Accept-Encoding`**

**Purpose**: Required for compression
functionality

**Details**: This header tells MediaTailor which
compression methods the client supports. MediaTailor uses this information to
compress manifests when possible, reducing bandwidth usage and improving
performance. Legacy devices that don't support compression won't send this
header, and MediaTailor will return uncompressed manifests.

**`User-Agent`**

**Purpose**: Required for device detection
and ad personalization

**Details**: MediaTailor analyzes the User-Agent
header to identify the client device type, browser, and capabilities. This
information is used for ad targeting, device-specific optimizations, and
ensuring compatibility with different playback clients.

**`Host`**

**Purpose**: Required for proper request
routing

**Details**: The `Host` header
ensures that requests are routed to the correct MediaTailor endpoint. This is
particularly important in multi-tenant environments and when using custom
domain configurations.

Many CDNs, including Amazon CloudFront, do not forward the `Host` header
by default. For CloudFront users: See [Configuring cache behaviors](cloudfront-basic-setup.md#cf-cache-behaviors "cloudfront-basic-setup.md#cf-cache-behaviors") for configuration
instructions.

**`X-Forwarded-For`**

**Purpose**: Required for client IP detection
and geo-targeting

**Details**: This header preserves the
original client IP address when requests pass through your CDN. MediaTailor uses
this information for geographic ad targeting, analytics, and compliance with
regional content restrictions.

###### Important

All four headers are required for full MediaTailor functionality. Missing any of these
headers can result in reduced functionality, including:

- Inability to compress manifests (missing Accept-Encoding)
- Poor ad targeting and device compatibility issues (missing
  User-Agent)
- Request routing failures (missing Host)
- Inaccurate geo-targeting and analytics (missing X-Forwarded-For)

For CDN-specific configuration instructions, see the routing behaviors and caching
sections that reference this header list.

The following topics provide detailed instructions for each aspect of CDN
integration.

###### Topics

- [Set up CDN routing behaviors for MediaTailor](cdn-routing-behaviors.md "cdn-routing-behaviors.md")
- [Set up CDN mapping in MediaTailor](cdn-mapping-mediatailor.md "cdn-mapping-mediatailor.md")
- [CDN integration security best practices for
  MediaTailor](cdn-security-best-practices.md "cdn-security-best-practices.md")
