# Creating an MediaTailor playback

configuration

This topic shows how to create a configuration to start receiving content streams
with AWS Elemental MediaTailor. It also shows how to provide an access point for downstream playback
devices to request content.

You can use the AWS Elemental MediaTailor console, the AWS Command Line Interface (AWS CLI)>, or the
MediaTailor API to create a configuration. For information about creating a
configuration through the AWS CLI or MediaTailor API, see the [_AWS Elemental MediaTailor API Reference_](../apireference/what-is.md "../apireference/what-is.md")..

When you create a configuration, don't put sensitive identifying information into
free-form fields such as the **Configuration name**
field. Identifying information can include things like customer account numbers. In
addition, don't use identifying information when you work in the MediaTailor
console, REST API, the AWS CLI, or AWS SDKs. Any data that you enter into
MediaTailor might get picked up for inclusion in diagnostic logs or
Amazon CloudWatch Events.

###### To add a configuration (console)

1. Open the MediaTailor console at [https://console.aws.amazon.com/mediatailor/](https://console.aws.amazon.com/mediatailor/ "https://console.aws.amazon.com/mediatailor/").
2. On the **Configurations** page, choose **Create
   configuration**.
3. Complete the configuration and additional configuration fields as
   described in the following topics:
   - [Required settings](#configurations-create-main "#configurations-create-main")
   - [Optional configuration
     settings](#configurations-create-addl "#configurations-create-addl")

4. Choose **Create configuration**.

AWS Elemental MediaTailor displays the new configuration in the table on the
**Configurations** page. 5. (Recommended) Set up a CDN with AWS Elemental MediaTailor for manifest and
reporting requests. You can use the configuration playback URLs for the CDN
setup. For information about setting up a CDN for manifest and reporting
requests, see [Using a CDN to optimize MediaTailor ad personalization and
content delivery](integrating-cdn.md "integrating-cdn.md").

## Required settings

When you create a configuration, you must include the following required
settings.

**Name**

Enter a unique name that describes the configuration. The name is
the primary identifier for the configuration. The maximum length
allowed is 512 characters.

**Content source**

Enter the URL prefix for the manifest for this stream, minus the
asset ID. The maximum length is 512 characters.

For example, the URL prefix
`http://origin-server.com/a/` is valid for an HLS
multivariant playlist URL of
`http://origin-server.com/a/main.m3u8` and for a DASH
MPD URL of `http://origin-server.com/a/dash.mpd`.
Alternatively, you can enter a shorter prefix such as
`http://origin-server.com`, but the `/a/`
must be included in the asset ID in the player request for content.

###### Note

If your content origin uses HTTPS, its certificate must be
from a well-known certificate authority. It can't be a
self-signed certificate. If you use a self-signed certificate,
AWS Elemental MediaTailor fails to connect to the content origin and
can't serve manifests in response to player requests.

**Ad decision server**

Enter the URL for your ad decision server (ADS). This is either
the URL with variables as described in [Step 3: Configure ADS request
URL and query parameters](getting-started-ad-insertion.md#getting-started-configure-request "getting-started-ad-insertion.md#getting-started-configure-request") , or the
static VAST URL that you are using for testing purposes. The maximum
length is 25,000 characters.

###### Note

If your ADS uses HTTPS, its certificate must be from a
well-known certificate authority. It can't be a self-signed
certificate. The same also applies to mezzanine ad URLs returned
by the ADS. If you use a self-signed certificate, then
AWS Elemental MediaTailor can't retrieve and stitch ads into the
manifests from the content origin.

## Optional configuration

settings

You can optionally configure **configuration aliases**,
**personalization details**, and **advanced
settings** in the MediaTailor console, MediaTailor API, or the
AWS Command Line Interface (AWS CLI).

### Configuration

aliases

The following are optional configuration aliases that you can
configure in the MediaTailor console, or with the MediaTailor
API.

**Player parameter variable**

For dynamic domain configuration during session
initialization, add one or more player parameter
variables.

For more information about using player parameter variables to
dynamically configure domains, see [MediaTailor domain variables for multiple content
sources](variables-domains.md "variables-domains.md").

### Log

configuration

The following are log configuration settings.

**Percent
enabled**

Sets the percentage of playback configuration session logs
that MediaTailor writes to CloudWatch Logs. For example, if your playback
configuration has 1000 sessions, and you set percent enabled to
**60**, MediaTailor writes 600 session logs to
CloudWatch Logs.

When you enable this option, MediaTailor automatically creates a
service-linked role that allows MediaTailor to write and manage
session logs in your CloudWatch Logs account. For more information, see
[Using service-linked roles for
MediaTailor](using-service-linked-roles.md "using-service-linked-roles.md").

**Logging strategies**

Indicates the method used for collecting logs that MediaTailor
emits. To send logs directly to CloudWatch Logs, choose
`LEGACY_CLOUDWATCH`. To send logs to CloudWatch Logs, which
then vends logs to your destination of choice, choose
`VENDED_LOGS`. Supported destinations are a CloudWatch Logs
log group, Amazon S3 bucket, and Amazon Data Firehose stream.

Additional set up is required for vended logs. For set up, see
[Using vended logs](vended-logs.md "vended-logs.md").

**ADS interaction log opt-in events**

Indicates that MediaTailor will emit `RAW_ADS_RESPONSE`
logs for sessions that are initialized with this configuration.

The `RAW_ADS_RESPONSE` log event contains the
entire VAST or VMAP response from the ADS. As such, the logs can
be extensive and might increase your logging costs.

**ADS interaction log exclude events**

Indicates that MediaTailor won't emit the selected events in the
logs that describe interactions with the ADS.

For a description of ADS log events, see [ADS logs](ads-log-format.md "ads-log-format.md").

**Manifest service interaction log exclude events**

Indicates that MediaTailor won't emit the selected events in the
logs that describe interactions with the manifest
service.

For a description of manifest service log events, see [Manifest logs](log-types.md "log-types.md").

### Ad conditioning

The following determine what actions MediaTailor takes to condition ads before
stitching them into a content stream.

**Streaming media file conditioning**

Determines the logic that MediaTailor uses when deciding which ads
to stitch.

- When **Streaming media file conditioning** is set to
  **Transcode**, MediaTailor transcodes the media files with `progressive`
  delivery and stitches them into the manifest. If there aren't enough ads with
  `progressive` delivery media files to fill the avail, MediaTailor transcodes and uses
  those with `streaming` delivery.
- When **Streaming media file conditioning** is set to
  **None**, MediaTailor stitches ads with `streaming` delivery media files
  into the manifest without transcoding them. If there aren't enough ads with
  `streaming` delivery media files to fill the avail, MediaTailor transcodes and uses those
  with `progressive` delivery.

### Personalization

details

The following are personalization details that you can configure in
the MediaTailor console or with the MediaTailor API.

**Slate ad**

Enter the URL for a high-quality MP4 asset that MediaTailor uses to
fill unfilled ad time. Slate configuration is optional for most
workflows but mandatory for VPAID ads. For comprehensive
information about slate behavior, configuration requirements,
and when slate is shown, see [MediaTailor slate ad insertion](slate-management.md "slate-management.md").

**Start bumper**

The URL of the start bumper asset location. Bumpers are short
video or audio clips that play at the beginning or end of an ad
break. They can be stored on Amazon's S3, or a different storage
service. To learn more about bumpers, see [MediaTailor bumper ad insertion](bumpers.md "bumpers.md").

**End bumper**

The URL of the end bumper asset location. Bumpers are short
video or audio clips that play at the beginning or end of an ad
break. They can be stored on Amazon's S3, or a different storage
service. To learn more about bumpers, see [MediaTailor bumper ad insertion](bumpers.md "bumpers.md").

**Personalization threshold**

Only applies when used in conjunction with slate ad. Defines
the maximum duration of underfilled ad time (in seconds) allowed
in an ad break before MediaTailor abandons personalization and shows
underlying content. This feature applies to ad replacement in
live and VOD streams, rather than ad insertion, because it relies on an underlying content stream. For detailed behavior scenarios and
comprehensive information, see [How personalization threshold
works](slate-management.md#personalization-threshold-scenarios "slate-management.md#personalization-threshold-scenarios").

**Live pre-roll ad decision server**

To insert ads at the start of a live stream before the main
content starts playback, enter the URL for the ad pre-roll from
the ad decision server (ADS). This is either the URL with
variables as described in [Step 3: Configure ADS request
URL and query parameters](getting-started-ad-insertion.md#getting-started-configure-request "getting-started-ad-insertion.md#getting-started-configure-request"), or the
static VAST URL that you are using for testing purposes. The
maximum length is 25,000 characters.

###### Note

If your ADS uses HTTPS, its certificate must be from a
well-known certificate authority. It can't be a self-signed
certificate. The same also applies to mezzanine ad URLs
returned by the ADS. If you use a self-signed certificate,
then AWS Elemental MediaTailor can't retrieve and stitch ads into
the manifests from the content origin.

For information about how pre-roll works, see [MediaTailor pre-roll ad insertion](ad-behavior-preroll.md "ad-behavior-preroll.md").

**Live pre-roll maximum allowed duration**

When you're inserting ads at the start of a live stream, enter
the maximum allowed duration for the pre-roll ad avail.
MediaTailor won't go over this duration when inserting ads. If
the response from the ADS contains more ads than will fit in
this duration, MediaTailor fills the avail with as many ads as
possible, without going over the duration. For more details
about how MediaTailor fills avails, see [Live ad stitching behavior](ad-behavior.md#ad-behavior-live "ad-behavior.md#ad-behavior-live") .

**Avail suppression mode**

Sets the mode for avail suppression, also known as ad
suppression. By default, ad suppression is off and MediaTailor fills
all with ads or slate. When the mode is set to
`BEHIND_LIVE_EDGE`, ad suppression is active and
MediaTailor doesn't fill ad breaks on or behind the avail suppression
value time in the manifest lookback window. When the mode is set
to `AFTER_LIVE_EDGE`, ad suppression is active. MediaTailor
doesn't fill ad breaks on or behind the avail suppression
period, which is the live edge plus the avail suppression value
plus buffer time.

**Avail suppression value**

The avail suppression value is a live edge offset time in
`HH:MM:SS`. MediaTailor won't fill ad breaks on or
behind this time in the manifest lookback window.

**Insertion Mode**

Insertion Mode controls whether players can use stitched or
guided ad insertion. The default, `STITCHED_ONLY`,
forces all player sessions to use stitched (server-side) ad
insertion. Setting InsertionMode to `PLAYER_SELECT`
allows players to select either stitched or guided ad insertion
at session-initialization time. The default for players that do
not specify an insertion mode is stitched.

### Advanced settings

The following are optional settings are advanced. You can configure
these in the MediaTailor console, with the AWS Command Line Interface (AWS CLI), or using
the MediaTailor API.

**CDN content segment prefix**

Enables AWS Elemental MediaTailor to create manifests with URLs to
your CDN path for content segments. Before you do this step, set
up a rule in your CDN to pull segments from your origin server.
For **CDN content segment prefix**, enter the
CDN prefix path.

For more information about integrating MediaTailor with a
CDN, see [Using a CDN to optimize MediaTailor ad personalization and
content delivery](integrating-cdn.md "integrating-cdn.md").

**CDN ad segment prefix**

Enables AWS Elemental MediaTailor to create manifests with URLs to
your own CDN path for ad segments. By default, MediaTailor
serves ad segments from an internal Amazon CloudFront distribution with
default cache settings. Before you can complete the
**CDN ad segment prefix** field, you must
set up a rule in your CDN to pull ad segments from the following
origin, like in the following example.

```
https://segments.mediatailor.<`region`>.amazonaws.com
```

For **CDN ad segment prefix**, enter the name
of your CDN prefix in the configuration.

For more information about integrating MediaTailor with a
CDN, see [Using a CDN to optimize MediaTailor ad personalization and
content delivery](integrating-cdn.md "integrating-cdn.md").

**DASH origin manifest type**

If your origin server produces single-period DASH manifests,
open the dropdown list and choose
**SINGLE_PERIOD**. By default,
MediaTailor handles DASH manifests as multi-period manifests.
For more information, see [Integrating an MPEG-DASH source](manifest-dash.md "manifest-dash.md").

**DASH mpd location**

(Optional as needed for DASH) The media presentation
description (mpd) location. Choose **DISABLED**
for the following situation:

- You set up CDN routing rules for accessing
  MediaTailor manifests.
- You use client-side reporting, or your player supports
  sticky HTTP redirects.

For more information about the **Location**
feature, see [DASH location feature](dash-location-feature.md "dash-location-feature.md").

**Transcode profile name**

The name that associates this configuration with a custom
transcode profile. This name overrides the dynamic transcoding
defaults of MediaTailor. Complete this field only if you have
already set-up custom profiles with the help of AWS
Support.

**Ad marker passthrough**

For HLS, enables or disables ad marker passthrough. When ad
marker passthrough is enabled, MediaTailor passes through
`EXT-X-CUE-IN`, `EXT-X-CUE-OUT`, and
`EXT-X-SPLICEPOINT-SCTE35` ad markers from the
origin manifest to the MediaTailor personalized manifest. No
logic is applied to the ad marker values; they are passed from
the origin manifest to the personalized manifest as-is. For
example, if `EXT-X-CUE-OUT` has a value of
`60` in the origin manifest, but no ads are
placed, MediaTailor won't change the value to `0`
in the personalized manifest.
