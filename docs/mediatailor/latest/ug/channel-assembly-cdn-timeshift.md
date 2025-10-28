# Configure time-shifted viewing for

MediaTailor channel assembly

AWS Elemental MediaTailor channel assembly supports time-shifted viewing capabilities that enable
DVR-like functionality such as pause, rewind, and start-over for your linear channels.
Enable these features by configuring your content delivery network (CDN) to support
time-shifted viewing, which allows viewers to control their viewing experience.

## Understanding time-shifted

viewing

Time-shifted viewing enables DVR-like functionality for linear channels,
including:

- **Start-over**: Viewers can start watching a
  program from the beginning, even if they join after it has started
- **Pause and resume**: Viewers can pause
  content and resume watching later
- **Rewind and fast-forward**: Viewers can
  navigate backward and forward through available content
- **Delayed viewing**: Viewers can watch
  content that aired earlier in the channel's schedule

Time-shifted viewing works by adding a `start` parameter to the
channel's playback URL. The parameter specifies an offset in seconds relative to the
current time:

- Negative values indicate a time in the past (such as
  `start=-3600` means "start from 1 hour ago")
- Positive values indicate a time in the future (such as
  `start=3600` means "start from 1 hour in the future")

Example URL with time-shift parameter:

```
https://example-cdn.com/out/v1/channel-name/index.m3u8?start=-3600
```

## Time delay resolution

To support time-shifted viewing with a CDN:

1. Configure your CDN to forward the `start` query parameter to
   channel assembly.
2. Set up cache behaviors that include the `start` parameter in
   the cache key.
3. For manifests with time-shift parameters, use a short TTL or no
   caching.

This ensures that each viewer receives the correct manifest for their requested
time position.

## CDN requirements for

time-shifting

Your CDN must meet these requirements to support time-shifted viewing with channel
assembly:

- Forward all query parameters to channel assembly.
- Include the `start` parameter in the cache key.
- Support proper cache invalidation for time-shifted manifests.
- Handle varying manifest responses based on query parameters.
