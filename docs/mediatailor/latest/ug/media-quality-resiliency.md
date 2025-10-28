# Implement multi-Region resilience for MediaTailor with

MQAR

AWS Elemental MediaTailor multi-Region resilience is enhanced through Media Quality-Aware Resiliency (MQAR), an advanced Amazon CloudFront feature that helps MediaTailor
deliver the best possible streaming experience. It automatically selects the origin with the
highest quality score when you have multiple origins in different AWS Regions. This
feature is particularly valuable for live streaming where you need uninterrupted
service.

## How MQAR works

MQAR enables CloudFront to select the origin with the highest quality score automatically.
This ensures that viewers receive the best possible streaming experience. When
configured properly, MQAR provides these benefits:

- Automatic selection of the highest quality origin
- Seamless failover between AWS Regions during outages
- Improved viewer experience with minimal interruptions
- Real-time quality monitoring and adaptation

## Step 1: Verify MQAR requirements

Before implementing MQAR, verify that your infrastructure meets these requirements.
MQAR works by comparing quality scores from multiple origins, so you need identical
content available in multiple AWS Regions.

- Encoders sending aligned ingest streams to all MediaPackage channels using
  epoch-locked CMAF ingest streamsets
- Two identical MediaPackage channels in different AWS Regions, with identical origin
  endpoints
- CMAF ingest for MediaPackage channels (enabled by default)
- CloudFront distribution configured to support MQAR
- MediaTailor configurations for each MediaPackage endpoint

## Step 2: Configure your encoders for MQAR

Your encoders need to produce consistent, synchronized outputs across all Regions for
MQAR to work effectively. This consistency allows CloudFront to make accurate quality
comparisons between origins.

Configure your MediaLive outputs with these settings:

- Ensure all video framerates in the CMAF output group are consistent (all
  fractional or all integer framerates).
- Avoid transitions between fractional and integer framerates across encoding
  sessions.
- Configure output segment sequence numbers so they never go backward across
  encoding sessions.
- Use identical encoder output names across all Regions.

For more information about configuring MediaLive for MQAR, see [Working with MQCS](../../../medialive/latest/ug/mqcs.md "../../../medialive/latest/ug/mqcs.md") in the MediaLive user
guide.

## Step 3: Configure MediaPackage for MQAR

Set up your MediaPackage channels and endpoints with these configurations:

###### To configure MediaPackage for MQAR

1. Create identical channel and endpoint configurations in each AWS
   Region.
2. Use CMAF as the channel input type.
3. For the primary MediaPackage origin, enable **Force endpoint error**
   configuration with these settings:
   - Stale multivariant playlists, media playlists, or MPDs
   - Incomplete multivariant playlist, media playlist, or MPD
   - Slate input

4. For back-up MediaPackage origins, do not enable these error configurations to
   maximize chances of successful failover.

For more information about configuring MediaPackage for MQAR, see [Leveraging media quality scores by
using AWS Elemental MediaPackage](../../../mediapackage/latest/userguide/mqcs.md "../../../mediapackage/latest/userguide/mqcs.md") in the MediaPackage user guide.

## Step 4: Configure CloudFront for MQAR

In the CloudFront configuration, you enable MQAR and define how it selects between your
origins. Create an origin group with the Media quality score option enabled.

###### To configure CloudFront for MQAR

1. Create a CloudFront distribution with origins pointing to your MediaTailor
   endpoints.
2. Create an origin group that includes these origins.
3. In the origin group settings, enable the **Media quality
   score** option.
4. Configure failover criteria to include 404 Not Found response codes. You can
   optionally include other 4xx/5xx codes.
5. Create separate cache behaviors for each channel's path pattern. This prevents
   mixing scores when the same origin group serves multiple channels.

###### Note

MQAR is not available when using Lambda@Edge functions in origin-facing triggers
(origin request and origin response) that are associated with your distribution's
cache behavior.

For more information about configuring CloudFront for MQAR, see [Media
quality-aware resiliency](../../../AmazonCloudFront/latest/DeveloperGuide/media-quality-score.md "../../../AmazonCloudFront/latest/DeveloperGuide/media-quality-score.md") in the CloudFront developer guide.

## Step 5: Configure MediaTailor for MQAR

To complete your MQAR setup, configure MediaTailor in each Region to work with your
multi-Region architecture. This ensures consistent ad insertion regardless of which
origin CloudFront selects.

###### To configure MediaTailor for MQAR

1. Create identical MediaTailor configurations in each Region, pointing to the
   corresponding MediaPackage endpoints.
2. Configure the CDN content segment prefix to use your CloudFront distribution
   domain.
3. Ensure that the ad decision server configurations are identical across
   Regions.

This setup ensures that regardless of which origin CloudFront selects based on quality
scores, MediaTailor can continue to personalize ads consistently.

## Step 6: Test your MQAR configuration

After setting up MQAR, test your configuration to ensure it works as expected:

###### To test your MQAR configuration

1. Request content through your CloudFront distribution.
2. Monitor real-time logs to verify that CloudFront is selecting origins based on
   quality scores.
3. Simulate a failure in your primary AWS Region to test failover behavior.
4. Verify that ad insertion continues to work correctly during failover.

## Next steps

After implementing MQAR, consider these next steps:

- Set up monitoring and troubleshooting for your MQAR configuration (see [Monitor and troubleshoot your CloudFront and
  MediaTailor integration](monitoring-and-troubleshooting.md "monitoring-and-troubleshooting.md"))
- Implement automated deployment using AWS CloudFormation (see [Automate MediaTailor and CDN with AWS CloudFormation](automating-cdn-integration.md "automating-cdn-integration.md"))
