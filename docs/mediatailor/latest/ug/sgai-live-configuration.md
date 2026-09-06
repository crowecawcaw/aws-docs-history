

# MediaTailor server-guided ad insertion configuration for live streams
<a name="sgai-live-configuration"></a>

AWS Elemental MediaTailor server-guided ad insertion for live content provides significant performance benefits through cacheable manifests. Configuring SGAI for live content uses the same core parameters as VOD, with specific considerations for live stream characteristics and real-time processing.

## Requirements for live SGAI
<a name="sgai-live-requirements"></a>

Before you enable SGAI for live content, ensure that you have the following:
+ Your live stream includes properly formatted DATERANGE markers
+ Ad break durations are consistent and predictable
+ Your CDN is configured to cache SGAI manifests appropriately
+ Players support server-guided ad insertion workflows
+ Your ad decision server can handle real-time requests for live content

### Player requirements
<a name="sgai-live-player-integration"></a>

Players must be configured to handle SGAI live manifests properly:
+ Support for server-guided ad insertion workflows
+ Ability to process ad insertion guidance from manifests
+ Proper handling of live stream timing and synchronization
+ For HLS content: Support for HLS version 8 and EXT-X-DATERANGE with CLASS attribute. Version 11 for server-side beaconing.
+ For HLS content: EXT-X-DEFINE variable substitution support

## Live playback configuration
<a name="sgai-live-playback-config"></a>

To enable SGAI for live content, create a playback configuration that has the following settings:

**Example SGAI live playback configuration**  

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
Must point to a live HLS stream with properly formatted SCTE-35 DATERANGE markers. The stream should maintain consistent segment durations and bitrate variants.

## SGAI live manifest requests
<a name="sgai-live-manifest-requests"></a>

SGAI live manifests use the same URL pattern as traditional ad insertion:

```
https://your-config.mediatailor.region.amazonaws.com/v1/master/config-name/manifest.m3u8?aws.insertionMode=GUIDED
```

## Manifest-based prefetch for live SGAI
<a name="sgai-live-guided-prefetch"></a>

For live SGAI workflows, you can enable manifest-based prefetch heartbeating to reduce ad fill latency. Add `aws.guidedPrefetchMode=MANIFEST` to the manifest request:

```
https://your-config.mediatailor.region.amazonaws.com/v1/master/config-name/manifest.m3u8?aws.insertionMode=GUIDED&aws.guidedPrefetchMode=MANIFEST
```

When enabled, MediaTailor appends a session identifier (`?aws.sessionId=<id>`) as a query parameter to each interstitial media manifest (`/v1/i-media`) URL in the multivariant playlist. Each time the player refreshes an i-media manifest, the request reaches MediaTailor with the session ID, which MediaTailor uses to identify the session and enqueue prefetch requests for upcoming ad breaks.

**Important**  
**Do not cache i-media manifests in your CDN when using guided prefetch.** The prefetch heartbeating mechanism depends on the player's manifest refresh requests reaching MediaTailor directly. If your CDN caches and serves `/v1/i-media` responses, MediaTailor does not receive the heartbeat requests and cannot trigger prefetching. Configure your CDN to pass through `/v1/i-media/*` requests to MediaTailor when `aws.guidedPrefetchMode=MANIFEST` is in use.

Guided prefetch is independent of the reporting mode. Whether you use server-side (default) or client-side (`aws.reportingMode=CLIENT`) tracking, beacons fire at playback time, not when ads are prefetched. For general information about how ad prefetching works in MediaTailor, see [Prefetching ads](prefetching-ads.md).

## Testing SGAI live configuration
<a name="sgai-live-testing"></a>

Verify your SGAI live setup with these validation steps:

1. **Test manifest generation**

   Request the SGAI live manifest URL and verify it returns cacheable content with proper ad insertion guidance.

1. **Verify CDN caching**

   Check that your CDN is caching SGAI manifests according to the configured TTL values.

1. **Test ad insertion**

   Confirm that players can successfully insert ads using the guidance provided in SGAI manifests.

1. **Monitor performance**

   Use CloudWatch metrics to verify reduced origin load and improved cache hit rates.