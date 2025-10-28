# MediaTailor ad server integration requirements

To integrate your ad server with AWS Elemental MediaTailor, your ad server must send XML that conforms
to the IAB specifications for the supported versions of VAST and VMAP. You can use a
public VAST validator to ensure that your tags are well-formed.

AWS Elemental MediaTailor supports VAST and VMAP responses from ad decision servers.
AWS Elemental MediaTailor also supports the proxying of VPAID metadata through our client-side
reporting API for client-side ad insertion. For information about client-side reporting,
see [Client-side ad tracking](ad-reporting-client-side.md "ad-reporting-client-side.md").

MediaTailor supports the following versions of VAST, VMAP, and VPAID:

- Up to [VAST 4.3](https://iabtechlab.com/standards/vast/ "https://iabtechlab.com/standards/vast/")

MediaTailor accepts response versions through VAST 4.3, but some advanced features
from VAST 4.0 and up are not be supported.

- [VMAP 1.0](https://www.iab.com/guidelines/digital-video-multiple-ad-playlist-vmap-1-0-1/ "https://www.iab.com/guidelines/digital-video-multiple-ad-playlist-vmap-1-0-1/")
- [VPAID 2.0](https://www.iab.com/guidelines/digital-video-player-ad-interface-definition-vpaid-2-0/ "https://www.iab.com/guidelines/digital-video-player-ad-interface-definition-vpaid-2-0/")

## VAST requirements

Your ad server's VAST response must contain IAB compliant
`TrackingEvents` elements and standard event types, like
`impression`. If you include non-standard tracking events,
AWS Elemental MediaTailor rejects the VAST response and doesn't provide an ad for the
avail.

VAST 3.0 introduced support for ad pods, which is the delivery of a set of
sequential linear ads. If a specific ad in an ad pod is not available,
AWS Elemental MediaTailor logs an error on CloudWatch, in the interactions log of the ADS. It then
tries to insert the next ad in the pod. In this way, MediaTailor iterates through
the ads in the pod until it finds one that it can use.

### Targeting

To target specific players for your ads, you can create templates for your ad
tags and URLs. For more information, see [MediaTailor dynamic ad variables for ADS requests](variables.md "variables.md").

AWS Elemental MediaTailor proxies the player's `user-agent` and
`x-forwarded-for` headers when it sends the ad server VAST
request and when it makes the server-side tracking calls. Make sure that your ad
server can handle these headers. Alternatively, you can use
`[session.user_agent]` or `[session.client_ip]` and
pass these values in query strings on the ad tag and ad URL. For more
information, see [MediaTailor session variables for ADS requests](variables-session.md "variables-session.md").

### Ad calls

AWS Elemental MediaTailor calls your VAST ads URL as defined in your configuration. It
substitutes any player-specific or session-specific parameters when making the
ad call. MediaTailor follows up to seven levels of VAST wrappers and redirects
in the VAST response. In live streaming scenarios, MediaTailor makes ad calls
simultaneously at the ad avail start for connected players. In practice, due to
jitter, these ad calls can be spread out over a few seconds. Make sure that your
ad server can handle the number of concurrent connections this type of calling
requires. MediaTailor supports prefetching VAST responses for live workflows.
For more information, see [Prefetching ads](prefetching-ads.md "prefetching-ads.md").

### Creative handling

When AWS Elemental MediaTailor receives the ADS VAST response, for each creative it
identifies the highest bitrate `MediaFile` for transcoding and uses
this as its source. It sends this file to the on-the-fly transcoder for
transformation into renditions that fit the player's multivariant playlist
bitrates and resolutions. For best results, make sure that your highest bitrate
media file is a high-quality MP4 asset with valid manifest presets. When
manifest presets aren't valid, the transcode jobs fail, resulting in no ad
shown. Examples of presets that aren't valid include unsupported input file
formats, like ProRes, and certain rendition specifications, like the resolution
855X481.

For a list of supported formats for media file inputs, see the **MP4** row of [Supported input formats](../../../mediaconvert/latest/ug/reference-codecs-containers-input.md "../../../mediaconvert/latest/ug/reference-codecs-containers-input.md") in the _AWS Elemental MediaConvert
User Guide_.

###### Creative indexing

AWS Elemental MediaTailor uniquely indexes each creative by the value of the
`id` attribute provided in the `<Creative>`
element. If a creative's ID is not specified, MediaTailor uses the media
file URL for the index.

The following example declaration shows the creative ID.

```
<Creatives>
        <Creative id="57859154776" sequence="1">
```

If you define your own creative IDs, use a new, unique ID for each creative.
Don't reuse creative IDs. AWS Elemental MediaTailor stores creative content for repeated
use, and finds each by its indexed ID. When a new creative comes in, the service
first checks its ID against the index. If the ID is present, MediaTailor uses
the stored content, rather than reprocessing the incoming content. If you reuse
a creative ID, MediaTailor uses the older, stored ad and doesn't play your new
ad.

###### VAST extensions provided by ad-serving partners

To help prevent collisions with creative IDs, you can use extensions
provided by ad-serving partners for the VAST response. MediaTailor supports
extensions from SpringServe, Publica, and FreeWheel. When you enable VAST
extension overrides, MediaTailor replaces the default creative ID with the
extension value.

To enable this feature, [submit an AWS Support
ticket](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/") to request VAST extension-based creative IDs to be enabled.
Include the following information in the Support ticket:

- AWS Region
- AWS account ID
- MediaTailor playback configuration names

To validate that VAST extension-based creative IDs are enabled on your
account, we recommend that you also request `RAW_ADS_RESPONSE`
logging to be enabled on a staging or testing playback configuration. With
logging, you can view the original VAST response that the ADS receives and
confirm that the correct creative IDs are used.

## VPAID requirements

VPAID allows publishers to serve highly interactive video ads and to provide
viewability metrics on their monetized streams. For information about VPAID, see the
[VPAID specification](https://www.iab.com/guidelines/digital-video-player-ad-interface-definition-vpaid-2-0/ "https://www.iab.com/guidelines/digital-video-player-ad-interface-definition-vpaid-2-0/").

AWS Elemental MediaTailor supports a mix of server-side-stitched VAST MP4 linear ads and
client-side-inserted VPAID interactive creatives in the same ad avail. It preserves
the order in which they appear in the VAST response. MediaTailor follows VPAID
redirects through a maximum of seven levels of wrappers. The client-side reporting
response includes the unwrapped VPAID metadata.

To use VPAID, follow these guidelines:

- Configure an MP4 slate for your VPAID creatives. AWS Elemental MediaTailor fills
  the VPAID ad slots with your configured slate, and provides VPAID ad
  metadata for the client player to use to run the interactive ads. If you
  don't have a slate configured, when a VPAID ad appears, MediaTailor
  provides the ad metadata through client-side reporting as usual. It also
  logs an error in CloudWatch about the missing slate. For more information, see
  [MediaTailor slate ad insertion](slate-management.md "slate-management.md") and
  [Creating an MediaTailor playback
  configuration](configurations-create.md "configurations-create.md").
- Use client-side reporting. AWS Elemental MediaTailor supports VPAID through our
  client-side reporting API. For more information, see [Client-side ad tracking](ad-reporting-client-side.md "ad-reporting-client-side.md").

It is theoretically possible to use the default server-side reporting mode
with VPAID. However, if you use server-side reporting, you lose any
information about the presence of the VPAID ad and the metadata surrounding
it, because that is available only through the client-side API.

- In live scenarios, make sure that your ad avails, denoted by
  `EXT-X-CUE-OUT: Duration`, are long enough to accommodate any
  user interactivity on VPAID. For example, if the VAST XML specifies a VPAID
  ad that is 30 seconds long, consider configuring your ad avail to be more
  than 30 seconds. This additional time gives users more chance to interact
  with the ad. If you don't add time, you could lose the VPAID metadata
  because the remaining duration in the ad avail is not long enough to
  accommodate the VPAID ad.
