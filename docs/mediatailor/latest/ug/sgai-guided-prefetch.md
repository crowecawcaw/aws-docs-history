

# Guided prefetch with manifest heartbeating
<a name="sgai-guided-prefetch"></a>

For live SGAI streams, you can enable manifest-based ad prefetching by adding `aws.guidedPrefetchMode=MANIFEST` to your session initialization request:

```
https://777788889999.mediatailor.us-east-1.amazonaws.com/v1/master/777788889999/myOrigin/index.m3u8?aws.insertionMode=GUIDED&aws.guidedPrefetchMode=MANIFEST
```

When enabled, MediaTailor appends a session identifier (`?aws.sessionId=<id>`) as a query parameter to each interstitial media manifest (`/v1/i-media`) URL in the multivariant playlist. Each time the player refreshes an i-media manifest, the request reaches MediaTailor with the session ID, which MediaTailor uses to enqueue prefetch requests for upcoming ad breaks.
+ The `aws.guidedPrefetchMode` parameter accepts two values: `MANIFEST` (enabled) and `OFF` (disabled, default).
+ Guided prefetch mode is only valid for SGAI sessions. Using it with stitched sessions returns an error.
+ DASH does not yet support guided prefetch mode.
+ Guided prefetch is independent of reporting mode — beacons fire at playback time, not at prefetch time.
+ **Do not cache i-media manifests in your CDN when using guided prefetch.** The prefetch mechanism depends on the player's manifest refresh requests reaching MediaTailor directly. If your CDN caches `/v1/i-media` responses, MediaTailor does not receive the heartbeat requests and cannot trigger prefetching.