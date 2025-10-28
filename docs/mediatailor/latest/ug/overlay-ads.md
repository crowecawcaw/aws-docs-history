# Overlay ads

For live-streaming workflows where you want to increase monetization without interrupting
the viewing experience with mid-roll ads, you can leverage your current AWS Elemental MediaTailor
integration to guide an advertising format that is rendered client-side. This type of
advertising is known as _overlay ads_. Overlay ads are
non-linear video ads that appear in the form of 'L-band ads,' 'non-linear video ads,'
'picture-in-picture ads,' 'motion overlays', 'in-content advertising', or 'frame
ads.'

MediaTailor detects a SCTE-35 marker with segmentation type `id=0x38` as an in-band
signal for an overlay ad-insertion opportunity. The SCTE-35 marker causes MediaTailor to send a
request to the Ad Decision Server (ADS), which then responds with a non-linear ad payload in
the VAST response. MediaTailor parses the VAST response in order to support overlay ad insertion.
MediaTailor does not perform any stitching of linear ads, but rather signals to the player that
there's a non-linear overlay ad available to play. This signaling allows the player to fetch
and correlate the non-linear ads to play from the client-side tracking endpoint. The player
then handles the display, reporting, and other tasks related to those ads. For example, the
player's developer can use a device SDK from a vendor that supports overlay-ad formats. For
more information about client-side tracking integrations, see [Client-side ad-tracking
integrations](ad-reporting-client-side-ad-tracking-integrations.md "ad-reporting-client-side-ad-tracking-integrations.md").

![The image depicts a timeline of various ad types displayed alongside a content video. Linear ads play before and after the content video. The ad before the content video is called a pre-roll ad. The ad after the content video is called a post-roll ad. A non-linear ad overlaps a portion of the content video itself. The non-linear ad is called an overlay ad.](images/client-side-overlays.png)

###### Topics

- [Prerequisites for using overlay ads with MediaTailor](overlay-ads-prerequisites.md "overlay-ads-prerequisites.md")
- [Getting started using overlay ads with MediaTailor](overlay-ads-getting-started.md "overlay-ads-getting-started.md")
- [Logging and metrics for overlay ads in MediaTailor](overlay-ads-logging-and-metrics.md "overlay-ads-logging-and-metrics.md")
- [Billing for overlay ads in MediaTailor](overlay-ads-billing.md "overlay-ads-billing.md")
