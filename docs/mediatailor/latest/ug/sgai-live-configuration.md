# MediaTailor server-guided ad insertion configuration for live streams

AWS Elemental MediaTailor server-guided ad insertion for live content provides significant performance
benefits through cacheable manifests. Configuring SGAI for live content uses the same core
parameters as VOD, with specific considerations for live stream characteristics and
real-time processing.

## Requirements for live SGAI

Before you enable SGAI for live content, ensure that you have the following:

- Your live stream includes properly formatted DATERANGE markers
- Ad break durations are consistent and predictable
- Your CDN is configured to cache SGAI manifests appropriately
- Players support server-guided ad insertion workflows
- Your ad decision server can handle real-time requests for live content

### Player requirements

Players must be configured to handle SGAI live manifests properly:

- Support for server-guided ad insertion workflows
- Ability to process ad insertion guidance from manifests
- Proper handling of live stream timing and synchronization
- For HLS content: Support for HLS version 8 and EXT-X-DATERANGE with CLASS
  attribute. Version 11 for server-side beaconing.
- For HLS content: EXT-X-DEFINE variable substitution support

## Live playback configuration

To enable SGAI for live content, create a playback configuration that has the
following settings:

###### Example SGAI live playback configuration

```

{
  "Name": "LiveSGAIConfig",
  "VideoContentSourceUrl": "https://your-live-origin.com/live/stream.m3u8",
  "AdDecisionServerUrl": "https://your-ads.com/ads",
  "PersonalizationThresholdSeconds": 1,
  "InsertionMode": "PLAYER_SELECT"
}

```

The following are key considerations for live SGAI configuration:

`VideoContentSourceUrl`

Must point to a live HLS stream with properly formatted SCTE-35 DATERANGE markers.
The stream should maintain consistent segment durations and bitrate
variants.

## SGAI live manifest requests

SGAI live manifests use the same URL pattern as traditional ad insertion:

```

https://your-config.mediatailor.region.amazonaws.com/v1/master/config-name/manifest.m3u8?aws.insertionMode=GUIDED

```

## Testing SGAI live configuration

Verify your SGAI live setup with these validation steps:

1. **Test manifest generation**

Request the SGAI live manifest URL and verify it returns
cacheable content with proper ad insertion guidance. 2. **Verify CDN caching**

Check that your CDN is caching SGAI manifests according to
the configured TTL values. 3. **Test ad insertion**

Confirm that players can successfully insert ads using the
guidance provided in SGAI manifests. 4. **Monitor performance**

Use CloudWatch metrics to verify reduced origin load and
improved cache hit rates.
