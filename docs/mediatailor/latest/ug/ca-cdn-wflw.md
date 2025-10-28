# Build MediaTailor linear channels with channel assembly and

CDN

This section provides comprehensive guidance for integrating AWS Elemental MediaTailor channel assembly
with a content delivery network (CDN). Follow these steps to set up, configure, and optimize
your channel assembly CDN integration.

You can also combine channel assembly with server-side ad insertion (SSAI) to create
monetized linear channels with personalized advertising. This powerful integration enables
you to deliver targeted ads to different viewers watching the same channel content,
increasing your revenue opportunities while maintaining a broadcast-quality viewing
experience. For information about SSAI with CDNs, see [Ad insertion with CDN](ssai-cdn-workflow.md "ssai-cdn-workflow.md").

In this topic, we use the term _manifests_ to refer collectively to
multivariant playlists, media playlists, and MPDs.

For more information about MediaTailor channel assembly, see [Using AWS Elemental MediaTailor to create linear assembled
streams](channel-assembly.md "channel-assembly.md").

## What you'll need

Before setting up MediaTailor channel assembly with a CDN, gather these required
resources:

**AWS account and permissions**

An AWS account with appropriate permissions to create and manage MediaTailor
resources

IAM permissions for MediaTailor, CloudFront (if using), and related services

For detailed permission requirements, see [Security in AWS Elemental MediaTailor](security.md "security.md").

**Required services**

A running MediaTailor channel assembly channel (not just an SSAI
configuration)

A content delivery network (CDN) account (Amazon CloudFront or third-party
CDN)

Origin storage for your VOD content (Amazon S3, MediaPackage, or other origin
server)

**Content requirements**

VOD sources properly encoded and packaged in HLS or DASH format. For
information about working with source locations and VOD sources, see [Working with source locations](channel-assembly-source-locations.md "channel-assembly-source-locations.md").

Content with consistent segment durations (recommended minimum: 1
second)

Ad slate content for ad breaks (if implementing ad insertion). For
information about configuring slate, see [MediaTailor slate ad insertion](slate-management.md "slate-management.md").

## Before you begin

###### Important

This workflow requires a running MediaTailor channel assembly channel. Having only a
MediaTailor SSAI configuration is not sufficient for this integration. You must have
an active channel assembly channel configured and operational before proceeding with
CDN integration.

Complete these setup tasks before implementing MediaTailor channel assembly with a
CDN:

1. Configure network connectivity between your CDN, MediaTailor, and origin
   servers
2. Set up HTTPS for secure content delivery
3. Configure DNS settings for your CDN domain

### Knowledge prerequisites

To successfully implement this solution, you should have:

- Understanding of streaming protocols (HLS/DASH)
- Basic knowledge of CDN configuration principles
- Familiarity with MediaTailor channel assembly concepts

For basic MediaTailor setup, refer to [Setting up](setting-up.md "setting-up.md") and [Getting started with MediaTailor channel
assembly](channel-assembly-getting-started.md "channel-assembly-getting-started.md"). For information about working
with source locations and VOD sources, see [Working with source locations](channel-assembly-source-locations.md "channel-assembly-source-locations.md"). For information about
configuring slate, see [MediaTailor slate ad insertion](slate-management.md "slate-management.md").

## Benefits of CDN integration

Integrating channel assembly with a CDN delivers these key benefits.

**Improved viewer experience**

Properly configured CDNs reduce buffering, startup times, and playback
errors for linear channels. This results in higher viewer engagement and
satisfaction.

**Cost reduction**

Efficient caching strategies minimize origin requests. This reduces data
transfer costs and origin server load, particularly important for
high-volume linear channels.

**Scalability**

Optimized CDN configurations handle traffic spikes during popular events
without degrading performance, ensuring your linear channels remain
available even during peak viewing times.

**Global reach**

Properly configured CDNs deliver content with low latency to viewers
worldwide, regardless of their location, expanding your potential
audience.

**Seamless program transitions**

Optimized CDN configuration ensures smooth transitions between programs in
your linear channel, creating a broadcast-quality viewing experience.

###### Topics

- [Understand CDN
  architecture](channel-assembly-cdn-architecture.md "channel-assembly-cdn-architecture.md")
- [Basic setup](ca-cdn-setup-basic.md "ca-cdn-setup-basic.md")
- [Configure base
  URLs](channel-assembly-cdn-baseurl.md "channel-assembly-cdn-baseurl.md")
- [Implement ad insertion](ca-cdn-setup-advanced.md "ca-cdn-setup-advanced.md")
- [Configure time-shifted
  viewing](channel-assembly-cdn-timeshift.md "channel-assembly-cdn-timeshift.md")
- [Monitor CDN operations](ca-cdn-monitor.md "ca-cdn-monitor.md")
- [Complete optimization
  guide](ca-cdn-optimize-reference.md "ca-cdn-optimize-reference.md")
