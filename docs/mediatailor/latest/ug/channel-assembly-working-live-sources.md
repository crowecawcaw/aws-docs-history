# Working with live

sources

A _live source_ represents a single live stream, such
as a live football game or news broadcast, that you add to your source location. After
you create your channel, you add one or more live sources to your source location, and
then associate each live source with a program.

MediaTailor supports these types of linear channel assembly:

- VOD sources for a channel that contains VOD-to-live content
- Live sources for a channel that contains live-to-live content intermixed with
  VOD-to-live content
  An example of VOD-to-live content is a channel that assembles a library of VOD assets
  into a live stream. One example of live-to-live content mixed with VOD-to-live content
  is a channel that shows mostly VOD content, except for a nightly news event or a
  pre-scheduled live sporting event. Another example of live-to-live content mixed with
  VOD-to-live content is an all live-to-live channel with origins that vary based on the
  time of day.

You can use live sources to set up a regional channel that shows mostly national
programming, but also includes regioinal programming overrides, and has VOD content
mixed in. To do so, you run one encoder/packager pair for the national content, then run
regional encoders when those regions are live. Then, you create regional
channel-assembly channels, each with their own schedules. This way, viewers can switch
back and forth as needed. This setup helps you minimize encoding/packaging costs.

Each live source must have at least one package configuration. A _package configuration_ specifies a package format, manifest
location, and source group for your live source. When you create your channel, you use
the package configuration's source groups to create the corresponding outputs on your
channel. For example, if your source is packaged in two different formats—HLS and
DASH—then you'd create two package configurations, one for DASH and one for HLS.
Then, you'd create two channel outputs, one for each package configuration. Each channel
output provides an endpoint that's used for playback requests. In this example, the
channel provides an endpoint for HLS playback requests and an endpoint for DASH playback
requests.

## General requirements

for using live sources

When you use live sources, your content must align with the following general
requirements:

- HLS live sources - You must provide `#EXT-X-PROGRAM-DATE-TIME`
  tags for the first segment in the manifest window, and on every
  discontinuity.
- HLS - You must configure ad markers as `DATERANGE`.
- Source manifest window - We recommend using a manifest window with a
  duration that's at least as long as the manifest window on your MediaTailor
  Channel Assembly channel. As a best practice, consider using a manifest
  window duration that's 30 seconds or longer than the manifest window on the
  Channel Assembly channel.
- Make the target duration match the duration of the existing
  sources.
- Make the number of child playlists match that of the existing
  sources.

## Configurations

If you use other AWS Elemental media services as part of your live sources
workflow, we recommend following best practices when setting up your MediaPackage
configuration. The following table describes how to configure MediaPackage settings based
on the streaming standard you use.

| MediaPackage setup for live sources | Standard                         | Setting                                                     | Value                                    | Necessity                                                                                                                        | Notes |
| ----------------------------------- | -------------------------------- | ----------------------------------------------------------- | ---------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | ----- |
| HLS                                 | Endpoint type                    | `Apple HLS`                                                 | Required unless using CMAF               | To match HLS `ts` AWS Elemental MediaConvert jobs                                                                                |
| HLS                                 | Endpoint type                    | `CMAF`                                                      | Required unless using Apple HLS          | To match HLS `mp4` AWS Elemental MediaConvert jobs                                                                               |
| HLS                                 | `ProgramDateTimeIntervalSeconds` | `1`                                                         | Required                                 | You must specify `#EXT-X-PROGRAM-DATE-TIME` on every segment in order to prevent playback issues when there are discontinuities. |
| HLS                                 | `PlaylistWindowSeconds`          | 30 seconds longer than the channel assembly manifest window | Required                                 |                                                                                                                                  |
| HLS                                 | `AdMarkers`                      | `DATERANGE`                                                 | Required when passing through ad markers |                                                                                                                                  |
| HLS                                 | `IncludeIframeOnlyStream`        | Disabled                                                    | Recommended                              |                                                                                                                                  |
| DASH                                | `ManifestLayout`                 | `FULL`                                                      | Recommended                              |                                                                                                                                  |
| DASH                                | `SegmentTemplateFormat`          | `NUMBER_WITH_TIMELINE` or `TIME_WITH_TIMELINE`              | Recommended                              | `NUMBER_WITH_DURATION` is not supported.                                                                                         |
| DASH                                | `ManifestWindowSeconds`          | 30 seconds longer than the channel assembly manifest window | Required                                 |                                                                                                                                  |
| DASH                                | `PeriodTriggers`                 | `ADS`                                                       | Required when passing through ad markers |                                                                                                                                  |
