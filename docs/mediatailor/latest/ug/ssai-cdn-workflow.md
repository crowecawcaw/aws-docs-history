# Set up SSAI with a CDN for personalized video

advertising

This section provides comprehensive guidance for integrating AWS Elemental MediaTailor server-side ad
insertion (SSAI) with a content delivery network (CDN). Follow these steps to set up,
configure, and optimize your SSAI CDN integration.

Server-side ad insertion (SSAI) is a technology that seamlessly inserts personalized
advertisements into video streams at the server level rather than the client level. When
combined with a CDN, you create a robust, scalable solution for delivering personalized
advertising to global audiences with minimal latency.

In this topic, we use the term _manifests_ to refer collectively to
multivariant playlists, media playlists, and MPDs.

## What you'll need

Before setting up MediaTailor ad insertion with a CDN, gather these required resources:

**AWS account and permissions**

An AWS account with appropriate permissions to create and manage MediaTailor
resources

IAM permissions for MediaTailor, CloudFront (if using), and related services

For detailed permission requirements, see [Security in AWS Elemental MediaTailor](security.md "security.md").

**Required services**

AWS Elemental MediaTailor configured and running

A content delivery network (CDN) account (Amazon CloudFront or third-party
CDN)

Origin server for your content (HLS or DASH)

Ad decision server (ADS) that supports VAST or VMAP

**Content requirements**

Content properly encoded and packaged in HLS or DASH format

Ad break markers in your content (for VOD) or SCTE-35 markers (for
live)

## Before you begin

Complete these setup tasks before implementing MediaTailor ad insertion with a CDN:

1. Configure network connectivity between your CDN, MediaTailor, and origin servers
2. Set up HTTPS for secure content delivery
3. Configure DNS settings for your CDN domain
4. For basic MediaTailor setup, complete the steps in [Setting up](setting-up.md "setting-up.md") and [Getting started with MediaTailor ad
   insertion](getting-started-ad-insertion.md "getting-started-ad-insertion.md").

### Knowledge prerequisites

To successfully implement this solution, you should have:

- Understanding of streaming protocols (HLS/DASH)
- Basic knowledge of CDN configuration principles
- Familiarity with ad insertion concepts

## Benefits of CDN integration

Integrating SSAI with a CDN delivers these key benefits:

**Improved viewer experience**

Properly configured CDNs reduce buffering, startup times, and playback
errors during ad transitions. This results in higher viewer engagement and
satisfaction.

**Cost reduction**

Efficient caching strategies minimize origin requests. This reduces data
transfer costs and origin server load, particularly important for
high-volume ad-supported content.

**Scalability**

Optimized CDN configurations handle traffic spikes during popular events
without degrading performance, ensuring your personalized ads are delivered
even during peak viewing times.

**Global reach**

Properly configured CDNs deliver content with low latency to viewers
worldwide, regardless of their location, expanding your potential
audience.

**Seamless ad transitions**

Optimized CDN configuration ensures smooth transitions between content and
ads, creating a broadcast-quality viewing experience.

The following topics provide comprehensive guidance on configuring MediaTailor with a CDN for optimal performance.

###### Topics

- [Understand CDN architecture](ssai-cdn-architecture-overview.md "ssai-cdn-architecture-overview.md")
- [Set up basic ad insertion](configuring-ssai-cdn.md "configuring-ssai-cdn.md")
- [SSAI with channel assembly](ssai-ca-integration.md "ssai-ca-integration.md")
- [Optimize CDN performance](ssai-cdn-performance.md "ssai-cdn-performance.md")
- [Monitor CDN operations](ssai-cdn-monitor.md "ssai-cdn-monitor.md")
- [Troubleshoot ad insertion with
  CDNs](troubleshooting-ssai-cdn.md "troubleshooting-ssai-cdn.md")
