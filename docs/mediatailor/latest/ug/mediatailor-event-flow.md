# AWS Elemental MediaTailor ad insertion event

flow

AWS Elemental MediaTailor processes manifest personalization for server-side ad insertion through a
predictable sequence of events. Understanding this event flow helps you comprehend how
MediaTailor transforms ad opportunities into personalized viewing experiences and provides a
foundation for troubleshooting when issues occur.

Each ad insertion opportunity follows a chronological sequence of events that MediaTailor
logs for visibility and monitoring. These events represent key milestones in the
manifest personalization process, from detecting an ad opportunity to delivering
tracking information.

## Standard event sequence

When MediaTailor successfully processes an ad insertion opportunity, the following
sequence of events typically occurs:

1. **Ad opportunity detection** - MediaTailor detects
   an ad marker (such as SCTE-35) in the content manifest, indicating an ad
   personalization opportunity is available.
2. **Ad decision server request** - MediaTailor sends
   a request to the configured ad decision server (ADS) to retrieve
   advertisements for the detected opportunity, including viewer parameters and
   ad break duration.
3. **Ad response processing** - MediaTailor receives a
   response from the ADS containing ad creative information, tracking URLs, and
   metadata about the advertisements to be included. For more information about
   VAST, VMAP, and VPAID response formats, see [Ad server integration requirements](vast.md "vast.md").
4. **Manifest personalization** - MediaTailor
   successfully processes the ad response, transcodes the advertisements if
   necessary, and generates a personalized manifest that includes relative URLs
   for both the ad segments and origin content. MediaTailor then sends the
   personalized manifest to the playback device.
5. **Tracking beacon activation** - A tracking
   beacon is fired to report ad events (such as impressions, quartiles, and
   completion) back to the ad server or other measurement systems. In
   server-side reporting mode (default), MediaTailor fires the beacon based on player
   segment requests. In client-side reporting mode, the playback device fires
   the beacon using URLs provided in the personalized manifest.

**Typical timing:** This entire sequence usually
completes within 2-5 seconds, depending on ad decision server response time and ad
creative processing requirements.

## Common event variations

Not all ad insertion attempts follow the standard successful sequence. MediaTailor
handles various scenarios that can alter the event flow:

### Empty ad response scenario

When the ad decision server returns no advertisements:

1. Ad opportunity detection occurs normally
2. Ad decision server request is sent successfully
3. ADS returns an empty response with zero ads
4. No ads are included in the personalized manifest for this
   opportunity

This is a normal scenario that can occur due to ad inventory availability,
targeting criteria, or business rules configured in the ad decision server. In
this case, the underlying content will be displayed unless the stream is a live
or live-to-VOD stream and slate has been configured. For more information, see
[MediaTailor slate ad insertion](slate-management.md "slate-management.md").

### Error scenarios

When technical issues prevent successful ad insertion, the event flow might be
interrupted at various points:

- **Ad decision server timeout** - The
  request to the ADS exceeds the configured timeout threshold, preventing
  ad retrieval.
- **Communication errors** - Network or
  connectivity issues prevent MediaTailor from reaching the ad decision
  server.
- **Response parsing errors** - The ADS
  returns a response that MediaTailor cannot parse due to invalid VAST format or
  structure.

In error scenarios, MediaTailor typically continues with content playback without
ads, ensuring uninterrupted viewer experience. For live or live-to-VOD streams
with slate configured, slate content might be displayed instead. For more
information, see [MediaTailor slate ad insertion](slate-management.md "slate-management.md").

### VAST redirect scenarios

When the initial VAST response contains a redirect to another ad
server:

1. Ad opportunity detection and initial ADS request occur normally
2. Initial response contains a redirect instruction
3. MediaTailor follows the redirect to retrieve the final ad response
4. Manifest personalization proceeds with the final ad content
5. Tracking beacon activation occurs normally

VAST redirects are common in programmatic advertising and allow for ad server
chaining and real-time decisioning. MediaTailor allows up to 7 wrapper redirects and
unlimited HTTP redirects during the ad retrieval process.

## Event timing overview

Understanding the timing characteristics of MediaTailor event flows helps set
appropriate expectations for ad insertion performance:

- **Ad opportunity detection** - Occurs when
  MediaTailor receives a `GetManifest` request from the player and
  encounters the ad markers in the content manifest.
- **Ad decision server interaction** -
  Typically takes 100-500 milliseconds, depending on ADS response time and
  network conditions.
- **Manifest personalization** - Usually
  completes within 50-200 milliseconds after receiving the ADS
  response.
- **Tracking beacon timing** - Varies by
  reporting mode. For server-side beacons, timing is based on segment requests
  from the client player; client-side beacons fire based on player
  implementation.

**Performance considerations:** The total time from
ad opportunity detection to manifest delivery should typically remain under 5
seconds to maintain optimal viewer experience. Individual components complete in
milliseconds as described above. However, the 5-second threshold accounts for
potential timeout values, retry attempts, and network variability that can occur
during the complete ad insertion workflow. Longer delays might indicate ADS
performance issues or network connectivity problems.

## Using event flow knowledge

Understanding MediaTailor event flow provides the foundation for:

- **Implementation planning** - Knowing the
  event sequence helps in designing player integration and ad server
  configuration.
- **Performance optimization** - Understanding
  timing expectations enables identification of bottlenecks and optimization
  opportunities.
- **Troubleshooting preparation** - Familiarity
  with normal event flows makes it easier to identify when something goes
  wrong.

For detailed troubleshooting guidance using event flow analysis, see [Troubleshooting](troubleshooting.md "troubleshooting.md"). For technical
details about event logging and monitoring, see [Viewing logs](monitoring-through-logs.md "monitoring-through-logs.md").
