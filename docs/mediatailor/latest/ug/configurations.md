# Using AWS Elemental MediaTailor to insert ads

A configuration is an object that you interact with in AWS Elemental MediaTailor. The configuration holds
the mapping information for the origin server and the ad decision server (ADS). You can also
define a default playback for MediaTailor to use when an ad isn't available or doesn't fill the
entire ad avail.

If you use a content delivery network (CDN) with MediaTailor, you must set up the
behavior rules in the CDN before you add CDN information to the configuration. For more
information about setting up your CDN, see [Using a CDN to optimize MediaTailor ad personalization and
content delivery](integrating-cdn.md "integrating-cdn.md").

###### Topics

- [Supported audio and video codecs](#supportedcodecs "#supportedcodecs")
- [Understanding AWS Elemental MediaTailor ad insertion behavior](ad-behavior.md "ad-behavior.md")
- [Understanding AWS Elemental MediaTailor server-guided ad insertion](server-guided.md "server-guided.md")
- [MediaTailor ad server integration requirements](vast.md "vast.md")
- [MediaTailor playback configuration
  management](working-with-configurations.md "working-with-configurations.md")
- [Integrating a content source for MediaTailor ad insertion](integrating-origin.md "integrating-origin.md")
- [Integrating AWS Elemental MediaTailor with Google Ad Manager](gam-integration.md "gam-integration.md")
- [Customizing ad break behavior with ad suppression](ad-rules.md "ad-rules.md")
- [MediaTailor bumper ad insertion](bumpers.md "bumpers.md")
- [MediaTailor pre-roll ad insertion](ad-behavior-preroll.md "ad-behavior-preroll.md")
- [MediaTailor slate ad insertion](slate-management.md "slate-management.md")
- [Prefetching ads](prefetching-ads.md "prefetching-ads.md")
- [Using preconditioned ads with AWS Elemental MediaTailor](precondition-ads.md "precondition-ads.md")
- [MediaTailor dynamic ad variables for ADS requests](variables.md "variables.md")
- [MediaTailor manifest query parameters](manifest-query-parameters.md "manifest-query-parameters.md")
- [Reporting ad tracking data](ad-reporting.md "ad-reporting.md")
- [Overlay ads](overlay-ads.md "overlay-ads.md")
- [Ad ID decoration](ad-id-decoration.md "ad-id-decoration.md")

## Supported audio and video codecs

MediaTailor supports the following codecs.

- Audio codecs: mp4a, ac-3, and
  ec-3
- Video codecs: h.264 (AVC), h.265
  (HEVC), av01 (AV1)
