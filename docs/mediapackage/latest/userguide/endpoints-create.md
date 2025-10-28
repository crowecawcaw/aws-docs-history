# Creating an origin endpoint in AWS Elemental MediaPackage

These steps shows how to create an origin endpoint (endpoint) on a channel to define
how MediaPackage prepares content for delivery. Content can't be served from a channel until it
has an endpoint. If you're using input redundancy, each endpoint receives content from
one ingest URL at a time. If MediaPackage performs a failover on the inputs for one ingest
input URL, the endpoints automatically start receiving content from the other ingest
URL. For more information about input redundancy and failover, see [Live input redundancy AWS Elemental MediaPackage processing
flow](what-is-flow-ir.md "what-is-flow-ir.md").

You can use the MediaPackage console, MediaPackage API, or AWS CLI to create an origin endpoint.
When you're creating an origin endpoint, don't put sensitive identifying information
like customer account numbers into free-form fields such as the name or description
field. MediaPackage doesn’t require that you supply any customer data. This includes when
you work with MediaPackage using the MediaPackage console, MediaPackage API, AWS CLI, or AWS SDKs. Any
data that you enter into MediaPackage might get picked up for inclusion in diagnostic logs
or Amazon CloudWatch Events.

###### To create an endpoint

1. Access the channel that the endpoint will be associated with, as described in [Viewing channel details in AWS Elemental MediaPackage](channels-view.md "channels-view.md").
2. Choose **Create endpoint** from the **Origin endpoints** list.
3. Complete the fields as described in the following topics:
   - [Endpoint settings fields](#endpoints-settings "#endpoints-settings")
   - [Segment settings fields](#endpoints-segment "#endpoints-segment")
   - [Encryption fields](#endpoints-encryption "#endpoints-encryption")
   - [Endpoint policy fields](#endpoints-policy "#endpoints-policy")
   - [Manifest fields](#endpoints-manifest "#endpoints-manifest")

4. Choose **Create**.

When you're creating an endpoint, you will receive an error if you exceed the quotas on the account. An error similar to **`Too many requests,
 please try again. Resource limit exceeded`** means that either you've exceeded the API request quotas, or you've already reached the
maximum number of endpoints permitted on this channel.

## Endpoint settings fields

The endpoint settings fields hold general information about the endpoint.

1. For **Name**, enter a name that describes the origin endpoint. This is the
   name that you use for API and console interactions. The name is the primary
   identifier for the endpoint and must be unique for your account in the
   AWS Region and channel. Supported characters are **A-Z**, **a-z**, **0-9**, **\_**
   (underscore), and **-** (hyphen) with a length
   of 1 to 256 characters. You can't use spaces in the name, and you can't
   change the name after you create the endpoint.
2. (Optional) For **Description**, enter any descriptive text that helps you to identify the origin endpoint.
3. For **Container type**, choose the type of container to attach to this origin endpoint. The container type you choose impacts
   the segment settings, encryption methods, and manifests you can choose.

The container type options are:

    * TS (available for HLS and LL-HLS manifests)
    * CMAF (available for HLS, LL-HLS, and DASH manifests)
    * ISM (available for MSS manifests only. Note: MSS only supports
     PlayReady DRM, does not support SCTE-35, key rotation, or constant
     IV)

4. For **Startover window (sec.)**, enter the size of the window (in seconds) to
   create a window of the live stream that's available for on-demand viewing.
   Viewers can start-over or catch-up on content that falls within the window.
   The maximum startover window is 1,209,600 seconds (14 days). For more
   information about implementing start-over and catch-up TV, see [Time-shifted viewing](time-shifted.md "time-shifted.md").

You must define a startover window if you're using some settings in the
**Filter configuration** fields in the [Manifest fields](#endpoints-manifest "#endpoints-manifest"). 5. For **Force endpoint error configuration**, choose the
types of problematic situations where you want MediaPackage to return a 404
response on manifests and segments requests:

    * **Stale Manifests**: MediaPackage stops receiving ingest
     streams on its input, indicating the encoder or network path have
     failed. This results in output stale manifests that don’t get
     updated any more, which results in playback sessions
     stopping.
    * **Incomplete Manifests**: MediaPackage is receiving
     ingest segments, but there are gaps in the timeline. This results in
     manifests presenting an incomplete timeline for some renditions,
     potentially generating playback problems.
    * **Missing DRM Keys**: MediaPackage was unable to
     retrieve an encryption key on a key-rotation operation. This results
     in the old encryption key still being used after the key-rotation
     time. While it will not affect playback, it could be problematic
     from a business or content-rights-entitlement perspective.
    * **Slate Input**: MediaPackage detects that the ingest
     stream(s) are flagged as including a significant proportion of slate
     contents (black video frames, audio silence). While playback
     continues, no content will be displayed by the players, which is a
     valid reason to failover to a different MediaPackage origin.

When MediaPackage is configured to react to these problems, it will return 404
responses until it can present a consistent timeline in the manifests -
meaning that all problematic segments will need to be evicted from the
exposed DVR window in the manifest.

###### Important

Triggering such forced 404 responses is an optional behavior that
should be used only if you want to implement CDN-driven failover between
multiple MediaPackage origins. For more information on this types of workflow,
see [Cross-Region failover](cross-region-failover.md "cross-region-failover.md").

## Segment settings fields

The segment settings fields hold general information about the segment.

1. For **Segment name**, enter a name that describes the segment. The name is the base name of the segment used in
   all content manifests inside of the endpoint. Supported characters are **A-Z**, **a-z**, **0-9**, **\_** (underscore), and **-** (hyphen) with a
   length of 1 to 256 characters. You can't use spaces in the name.
2. For **Segment duration (sec.)**, enter the duration (in seconds) of each segment. Enter a value equal to,
   or a multiple of, the input segment duration. The maximum segment duration is 30 seconds. If the value that you enter is
   different from the input segment duration, MediaPackage
   rounds segments to the nearest multiple of the input segment duration.
3. Select **Include IFrame-only stream** to include an additional I-frame only stream along with the
   other tracks in the manifest. MediaPackage generates an I-frame only stream from the first rendition in the manifest.
   The service inserts `EXT-I-FRAMES-ONLY` tags in the output manifest, and then generates and includes an I-frames only playlist
   in the stream. This playlist enables player functionality like fast forward and rewind.
4. For TS containers only, select **Use audio rendition group** to group all
   audio tracks into a single rendition group. All other tracks in the stream
   can be used with any audio rendition from the group. For more information
   about rendition groups, see [AWS Elemental MediaPackage rendition groups reference](rendition-groups.md "rendition-groups.md").
5. For TS containers only, select **Include DVB subtitles** to pass through
   digital video broadcasting (DVB) subtitles into the output. By default,
   MediaPackage excludes all DVB subtitles from the output.
6. Select **Enable SCTE support** to include SCTE configuration options. If you select this,
   you can further define your SCTE configuration in additional fields.
7. For **SCTE filtering**, choose the SCTE-35 message types that will be ad markers in the output. If you don't make a selection here, by default, MediaPackage inserts all ad markers in the output manifest.
   - Splice insert
   - Break
   - Provider advertisement
   - Distributor advertisement
   - Provider placement opportunity
   - Distributor placement opportunity
   - Provider overlay placement opportunity
   - Distributor overlay placement opportunity
   - Program

## Encryption fields

Protect your content from unauthorized use through content encryption and digital rights management (DRM). MediaPackage uses the
[AWS Secure Packager and Encoder Key Exchange (SPEKE) API](https://aws.amazon.com/media/tech/speke-basics-secure-packager-encoder-key-exchange-api/ "https://aws.amazon.com/media/tech/speke-basics-secure-packager-encoder-key-exchange-api/") to
facilitate content encryption and decryption by a DRM provider. Using SPEKE, the DRM provider supplies encryption keys to MediaPackage through the SPEKE API.
The DRM provider also supplies licenses to supported media players for decryption. For more information about how SPEKE is used with services and features
running in the cloud, see [AWS cloud-based architecture](../../../speke/latest/documentation/what-is-speke.md#services-architecture "../../../speke/latest/documentation/what-is-speke.md#services-architecture")
in the _Secure Packager and Encoder Key Exchange API Specification guide_.

###### Note

To encrypt content, you must have a DRM provider, and be set up to use encryption. For information, see [Content encryption and DRM in AWS Elemental MediaPackage](using-encryption.md "using-encryption.md").

1. Choose **Encrypt content** to serve content with
   copyright protection.
2. For **Encryption method**, choose the encryption method
   to use. If you don't see your preferred encryption method, confirm you
   choose the correct container type. The encryption method you choose impacts
   the DRM system providers you can choose. For supported encryption methods
   and DRM system providers, see [Container and DRM system support with
   SPEKE](using-encryption.md#encryption-choosing-speke-version "using-encryption.md#encryption-choosing-speke-version").
   - The valid encryption methods for TS container types are:
     - AES-128
     - Sample AES

   - The valid encryption methods for CMAF container types are:
     - CENC
     - CBCS

   - The valid encryption method for ISM container types is:
     - CENC

3. For **DRM systems**, choose the DRM system providers
   you're using to protect your content during distribution. You can choose
   more than one. If you don't see your DRM system provider, confirm you choose
   the correct container type and encryption method. For supported DRM system
   providers, see [Container and DRM system support with
   SPEKE](using-encryption.md#encryption-choosing-speke-version "using-encryption.md#encryption-choosing-speke-version").

The valid DRM systems for TS container types are:

    * Fairplay (Sample AES only)
    * Clear Key AES-128 (AES-128 only)

The valid DRM systems for CMAF container types are:

    * PlayReady
    * Widevine
    * Irdeto (CENC only)
    * Fairplay (CBCS only)

The valid DRM system for ISM container types is:

    * PlayReady

4. For **Resource ID**, enter an identifier for the content. The service sends this to the key server to
   identify the current endpoint. How unique you make this depends on how fine-grained you want access controls to be. The service does
   not permit you to use the same ID for two simultaneous encryption processes. The resource ID is also known as the content ID.

The following example shows a resource ID.

```
MovieNight20171126093045
```

5. For **Key server URL**, enter the URL of the API Gateway proxy that you set up to talk to your key server.
   The API Gateway proxy must reside in the same AWS Region as MediaPackage.

The following example shows a URL.

```
https://1wm2dx1f33.execute-api.us-west-2.amazonaws.com/SpekeSample/copyProtection
```

6. For **Role ARN**, enter the Amazon Resource Name (ARN) of the IAM role that provides you access to
   send your requests through API Gateway. Get this from your DRM solution provider.

The following example shows a role ARN.

```
"arn:aws:iam::`accountID`:role/SpekeAccess
```

7. For **Video encryption preset** and **Audio
   encryption preset**, select the preset for encrypting audio and
   video. For information about presets, see [Encryption presets in AWS Elemental MediaPackage](drm-content-speke-v2-presets.md "drm-content-speke-v2-presets.md").
8. (Optional) For **Constant initialization vector** enter a
   128-bit, 16-byte hex value represented by a 32-character string, used in
   conjunction with the key for encrypting content. If you don't specify a
   value, then MediaPackage creates the constant initialization vector (IV).
9. For **Key rotation interval (sec.)**, enter the frequency
   (in seconds) of key changes for live workflows, in which content is streamed
   real time. The service retrieves content keys before the live content begins
   streaming, and then retrieves them as needed over the lifetime of the
   workflow. By default, key rotation is 300 seconds (5 minutes), the minimum
   rotation interval, which is equivalent to setting it to `300`.
   The maximum key rotation interval is 31,536,000 seconds (1 year). If you
   don't enter an interval, content keys aren't rotated.

The following example setting causes the service to rotate keys every
thirty minutes.

```
1800
```

For information about key rotation, see [AWS Elemental MediaPackage key rotation behavior](drm-content-key-rotation.md "drm-content-key-rotation.md"). 10. (Optional) Select **Exclude segment DRM metadata** to
omit SEIG and SGPD boxes from CMAF segments. This can improve compatibility
with certain devices and players that don't support these DRM metadata
boxes.

###### Note

This option is only available for CMAF container formats. For TS
containers, this option is disabled because TS containers don't include
SEIG and SGPD boxes.

When enabled, MediaPackage excludes segment-level DRM metadata boxes while
preserving other essential DRM functionality. Key rotation can still be
handled through media playlist signaling. For more information about DRM
segment metadata, see [Managing DRM segment metadata](drm-segment-metadata-management.md "drm-segment-metadata-management.md").

## Endpoint policy fields

You must assign a channel policy to enable content to flow into your channel from sources outside of your account.

1. Under **Endpoint policy**, choose an endpoint policy to enable content to flow into your channel from
   sources outside of your account. For more information about policies,
   see [Resource-based policy examples](using-iam-policies.md "using-iam-policies.md").
   - **Don't attach a policy** - Restrict access to only those who have access to this account's credentials.
   - **Attach a custom policy** - Define your own policy and restrict access to as few or as many as you want.
     Enter a valid JSON object with the same structure as other IAM policies.
     The policy should follow the standard security advice of granting least privilege, or granting only the permissions required to perform a task.
   - **Attach a public policy** - Accept all incoming client requests to a channel's output. Enter a valid JSON object
     with the same structure as other IAM policies.

## Manifest fields

The manifests fields hold general information about the manifest. You must attach
at least one manifest to an origin endpoint. You can attach up to twenty five
manifests to a single origin endpoint, and request a quota increase if
necessary.

Choose the type of manifest to use. You can choose an HLS manifest, LL-HLS
manifest, DASH manifest, or MSS manifest. The available manifest types depend on the
container type you selected:

- TS container: HLS and LL-HLS manifests
- CMAF container: HLS, LL-HLS, and DASH manifests
- ISM container: MSS manifests only

###### Note

Microsoft Smooth Streaming (MSS) is primarily used for legacy devices
such as older smart TVs, Xbox consoles, and platforms that use Microsoft
Silverlight. If you need to support these devices, select the ISM
container type and create an MSS manifest. For more information about
MSS, see [MSS in AWS Elemental MediaPackage](mss-overview.md "mss-overview.md").

###### Topics

###### To create an HLS or LL-HLS manifest

1. For **Manifest name** enter a short string that
   will be appended to the endpoint URL. The manifest name creates a
   unique path to this endpoint. If you don't enter a value, MediaPackage uses
   the default manifest name, _index_. MediaPackage
   automatically inserts the format extension, such as .m3u8. Supported
   characters are **A-Z**, **a-z**, **0-9**, and **-** (hyphen).
   You can't use underscores in the name.
2. (Optional) For **Child manifest name** enter a
   short string that will be appended to the endpoint URL. The child
   manifest name creates a unique path to this endpoint. Supported
   characters are **A-Z**, **a-z**, **0-9**, and **-** (hyphen).
   You can't use underscores in the name.
3. For **Manifest window (sec.)** enter the total
   duration (in seconds) of the manifest's content. The maximum
   manifest window is 900 seconds (15 minutes).
4. For **Program date/time interval (sec.)** enter
   the interval (in seconds) for MediaPackage to insert the
   `EXT-X-PROGRAM-DATE-TIME` tags in the manifest.
   Program date time (PDT) is optional when using HLS manifests, but is
   required when using low-latency HLS manifests.

The maximum PDT interval is 1,209,600 seconds (14 days). If you
don't enter an interval, `EXT-X-PROGRAM-DATE-TIME` tags
aren't included in the manifest.

The `EXT-X-PROGRAM-DATE-TIME` tag holds the time of the
segment. When PDT information is available in the source content,
MediaPackage uses this same information on the output content. Otherwise,
MediaPackage uses Coordinated Universal Time (UTC) for the PDT.

The PDT information helps downstream players to synchronize the
stream to the wall clock, enabling functionality like viewer seek in
the playback timeline and time display on the player. 5. Select **URL-encode HLS child manifest query
parameters** if you need query parameters to be encoded
to comply with AWS Signature Version 4 signing. For more
information about this setting, see [URL encoding query parameters](msettings-params.md#msettings-parameters-encoding "msettings-params.md#msettings-parameters-encoding"). 6. Choose **Enable start tag** to insert an
`EXT-X-START` tag in your manifest. Set the offset
for when the tag appears, and indicate if this is a precise offset.
MediaPackage adds `EXT-X-START` tags to the output manifest
based on your specified offset settings.

    * If the offset is *positive*, it must be less than the
     configured manifest duration, minus three times the
     configured segment target duration (in accordance with the
     [HLS specification](https://datatracker.ietf.org/doc/html/draft-pantos-hls-rfc8216bis-16#section-4.4.2.2 "https://datatracker.ietf.org/doc/html/draft-pantos-hls-rfc8216bis-16#section-4.4.2.2")).
    * If the offset is *negative*, the absolute value must be three
     times the configured segment target duration and it must be
     smaller than the configured manifest duration.

7. If you chose **Enable SCTE support**, for
   **Ad markers**, choose how ad markers are
   included in the packaged content. If you include ad markers in the
   content stream in your upstream encoders, then you need to inform
   MediaPackage what to do with the ad markers in the output. If you don't see
   this field, select **Enable SCTE support** in the
   origin endpoint segment settings. Choose from the following
   options:
   - **Daterange** – Insert `EXT-X-DATERANGE` tags to signal ads and program transition events
     in TS and CMAF output manifests. If you choose daterange, you _must_ also enter a **Program date/time interval
     (sec.)** value of 1 or greater.
   - **SCTE-35 enhanced** – Generate industry-standard CUE tag ad markers in HLS
     manifests based on SCTE-35 input messages from the input stream. This option
     inserts EXT-X-CUE-OUT, EXT-X-CUE-IN, and related CUE tags to signal ads and
     program transition events, providing the same SCTE-35 information as DATERANGE
     tags but in a format compatible with legacy ad insertion systems.

8. Select **Enable filter configuration** if you
   want to optionally add filters and settings to modify manifests.
   These filters apply to all manifests that originate from this
   endpoint.

To automatically fill these values from an existing query string,
choose **Import from query string**.
For example, this string provides the following filters:
`aws.manifestfilter=video_codec:h265;audio_language:fr,en-US,de&start=2023-10-20T12:20:50Z&end=2023-10-20T13:20:50Z&time_delay=10`

**Filter key**
`video_codec`, **Filter value**
`h265`, **Filter key**
`audio_language`, **Filter value**
`fr,en-US`, **Start time**
`2023-10-20T12:20:50Z`, **End time**
`2023-10-20T13:20:50Z`, and **Time
delay**
`10` seconds.

###### Note

When you include a Manifest filter, you cannot use
matching query parameters for the manifest's endpoint URL.
If you do, you will receive a `404` HTTP error
code instead. For example, if you include a Manifest filter
with a `audio_sample_rate` Filter key and
`44100` Filter value, and you make an HTTP
request for
`https://<example-url>/?aws.manifestfilter=audio_sample_rate:44100`,
you will receive a `404` error.

**Manifest filter**

Optionally specify one or more manifest filters for
all of your manifest egress requests.

You enter a **Filter key** and
**Filter value** pair for each
manifest filter. Your filter values can be a range,
single value, or combination of both.

For a list of supported keys and values, see [Manifest filtering query
parameters](manifest-filter-query-parameters.md "manifest-filter-query-parameters.md").

**Start time and End time**

Optionally specify the start or end time for all of
your manifest egress requests. To use this setting, you
must have a startover window defined.

For more information about start and end times, see
[Start and end parameters](start-and-end-parameters-rules.md "start-and-end-parameters-rules.md").

If you enter a start or end time using the API, or
import using **Import from query
string** in the MediaPackage console,
enter dates in an ISO-8601 format.

**Time delay**

Optionally specify the time delay (in seconds) for all
of your manifest egress requests. To use this setting,
you must have a startover window defined.

For more information about using time delays, see
[Time delay](time-delay.md "time-delay.md").

**Clip start time data and time**

When using a time delay, optionally specify the clip
start time for all of your manifest egress requests.
This option specifies the earliest content that can be
included in the manifest. Content ingested before the
clip start time will not be included in the manifest.
Cannot be used with start time or end time filters. To
use this setting, you must have a startover window
defined.

For more information about clip start and time delay,
see [Using clip start with time delay](time-delay.md#clip-start "time-delay.md#clip-start").

###### Important

If you're using this setting to limit content
playback for contractual reasons, this parameter
should be set at your CDN, and not at the client.
Use the following steps to configure the endpoint to create manifests that
are compliant with DASH.

###### DVB-DASH requirements

If the outputs from this endpoint will be compliant with DVB-DASH, you
must adhere to the following requirements:

- The channel must use CMAF input
- The endpoint must not use **UTC Direct** for UTC
  timing mode

###### To create a DASH manifest

1.  For **Manifest name**, enter a short string that
    will be appended to the endpoint URL. The manifest name creates a
    unique path to this endpoint. If you don't enter a value, MediaPackage uses
    the default manifest name, _index_. MediaPackage
    automatically inserts the format extension, such as .mpd. Supported
    characters are **A-Z**, **a-z**, **0-9**, and **-** (hyphen).
    You can't use underscores in the name.
2.  For **Manifest window (sec.)** enter the total
    duration (in seconds) of the manifest's content. The maximum
    manifest window is 900 seconds (15 minutes). You can request a quota
    increase if necessary.
3.  For **Min update period (sec.)**, enter the
    minimum amount of time (in seconds) that the player should wait
    before requesting manifest updates. A lower value means that
    manifests are updated more frequently, but a lower value also
    contributes to request and response network traffic.
4.  For **Min buffer time (sec.)**, enter the minimum
    amount of time (in seconds) that a player must keep in the buffer.
    If network conditions interrupt playback, the player will have
    additional buffered content before playback fails, allowing for
    recovery time before the viewer's experience is affected.
5.  For **Suggested presentation delay (sec.)**,
    enter the amount of time (in seconds) that the player should be from
    the end of the manifest. This sets the content start point back x
    seconds from the end of the manifest (the point where content is
    live). For example, with a 35-second presentation delay, requests at
    5:30 receive content from 5:29:25. When used with time delay,
    MediaPackage adds the suggested presentation delay to the time
    delay duration.
6.  For **Segment template format**, choose how
    MediaPackage and playback requests refer to each segment.
    - For **Number with timeline**,
      MediaPackage uses the `$Number$` variable to
      refer to the segment in the `media` attribute of
      the `SegmentTemplate` tag. The value of the
      variable is the sequential number of the segment.
      `SegmentTimeline` is included in each segment
      template.

7.  For **Manifest compactness**, indicate if you
    want MediaPackage to serve a standard (compacted) or full manifest (no
    compacting) in response to playback requests.

        * If you choose **None**, MediaPackage
         presents the `SegmentTemplate` and
         `SegmentTimeline` tags for every
         `Representation` in the manifest.
        * **Standard** is the default selection. It
         indicates that MediaPackage combines duplicate
         `SegmentTemplate` tags and presents them at
         the start of the manifest. This shortens the manifest and
         makes it easier for some devices to process it.

    For more information about the manifest layout options, see [DASH manifest compactness](compacted.md "compacted.md").

8.  For **Profiles**, optionally choose if the output
    is compliant with DVB-DASH. Review the DVB-DASH requirements to
    ensure the endpoint is compliant with this profile:
    - The channel must use CMAF input
    - The endpoint must not use **UTC Direct**
      for UTC timing mode

9.  For **UTC timing**, select the method that the
    player uses to synchronize to coordinated universal time (UTC) wall
    clock time. This enables the player and MediaPackage to run on the
    same UTC wall clock time. This is a requirement, otherwise playback
    timing or synchronization issues can occur. Choose from the
    following options:
    - `UTC Direct`
    - `HTTP Head`
    - `HTTP Iso`
    - `HTTP Xsdate`

10. For **UTC timing source**, specify a URI to use
    for UTC synchronization. This is the URI used to fetch the timing
    data according to the scheme defined by **UTC
    timing**. This value is only valid if **UTC
    timing** is not `NONE` or `UTC
DIRECT`. This value will be set as the `@value`
    attribute for the `UTCTiming` element. For information
    about `@value`, see [DASH clock synchronization](https://dashif.org/dash.js/pages/usage/clock-sync.html "https://dashif.org/dash.js/pages/usage/clock-sync.html").
11. For **DASH period triggers**, choose how
    MediaPackage creates media presentation description (MPD) periods
    in the DASH output manifest. For more information, see [Multi-period DASH in AWS Elemental MediaPackage](multi-period.md "multi-period.md"). Choose
    from the following options:
    - **Avails** – Avails that pass the
      `ScteFilter` will create new periods.
    - **DRM key rotation** – Encryption
      key rotation will create new periods.
    - **Source changes** – Changes in
      the stream set will create new periods.
    - **Source disruptions** – Gaps in
      all content streams will create new periods.
    - **None** – MediaPackage formats
      the manifest as a single period. It doesn't create
      additional periods, unless DRM settings change.

12. Select **Configure subtitle TTML profile** to
    optionally configure the profile that TTML subtitles use.

**Subtitle TTML profile**

The profile that MediaPackage uses when signaling subtitles
in the manifest. **IMSC** is the
default profile. **EBU-TT-D** produces
subtitles that are compliant with the EBU-TT-D TTML
profile. MediaPackage passes through subtitle styles to the
manifest. For more information about EBU-TT-D subtitles,
see [EBU-TT-D Subtitling Distribution
Format](https://tech.ebu.ch/publications/tech3380 "https://tech.ebu.ch/publications/tech3380"). 13. Select **Configure program information** to
optionally provide details about the content that you want MediaPackage to
pass through in the manifest to the playback device. To read more
about program information, see the _Program
information_ section of the [ISO 23009-1 DASH
standards](https://dashif.org/news/5th-edition/ "https://dashif.org/news/5th-edition/").

**Title**

The title for the manifest.

**Source**

Information about the content provider.

**Copyright**

A copyright statement about the content.

**Language code**

The language code for this manifest.

**More information URL**

An absolute URL that contains more information about
this content. 14. Select **Configure DASH base URLs** to optionally
specify one or more locations for the segments. For more
information, see the _Base URL
section_ of the [ISO 23009-1 DASH
standards](https://dashif.org/news/5th-edition/ "https://dashif.org/news/5th-edition/") and _Handling of
BaseURLs by players_ in the DVB.org [MPEG-DASH Profile for Transport of ISO BMFF Based DVB Services
over IP Based Networks document](https://dvb.org/wp-content/uploads/2021/06/A168r4_MPEG-DASH-Profile-for-Transport-of-ISO-BMFF-Based-DVB-Services_Draft-ts_103-285-v140_November_2021.pdf "https://dvb.org/wp-content/uploads/2021/06/A168r4_MPEG-DASH-Profile-for-Transport-of-ISO-BMFF-Based-DVB-Services_Draft-ts_103-285-v140_November_2021.pdf").

**URL**

The Base URL.

**Service location**

The name of the Base URL location.

**DVB priority**

For endpoints that use the DVB-DASH profile only. The
priority that the playback device should use this Base
URL. Lower values are higher priority.

**DVB weight**

For endpoints that use the DVB-DASH profile only. The
weighting for Base URLs with the same priority. 15. For endpoints that use the DVB-DASH profile, select
**Configure DVB-DASH settings** to optionally
pass to the player information for downloading subtitle fonts and
sending error reports to pass through in the manifest to the
playback device. For more information about these settings, see
_DVB font download scheme_ and
_DVB metrics reporting_ in the
DVB.org [MPEG-DASH Profile for Transport of ISO BMFF Based DVB Services
over IP Based Networks document](https://dvb.org/wp-content/uploads/2021/06/A168r4_MPEG-DASH-Profile-for-Transport-of-ISO-BMFF-Based-DVB-Services_Draft-ts_103-285-v140_November_2021.pdf "https://dvb.org/wp-content/uploads/2021/06/A168r4_MPEG-DASH-Profile-for-Transport-of-ISO-BMFF-Based-DVB-Services_Draft-ts_103-285-v140_November_2021.pdf").

These settings are compatible only with the DASH-DVB profile.
**Profiles** must be set to
**DVB-DASH** to set these fields.

**Font download URL**

The URL of the font to download for subtitles.

**Font family**

The `fontFamily` name for subtitles, as
described in [EBU-TT-D Subtitling Distribution
Format](https://tech.ebu.ch/publications/tech3380 "https://tech.ebu.ch/publications/tech3380").

**MIME type**

The `mimeType` of the resource that's at
the indicated **Font download URL**.
Options are **application/font-sfnt**
and **application/font-woff**, as
described in the [DVB.org DASH document](https://dvb.org/wp-content/uploads/2021/06/A168r4_MPEG-DASH-Profile-for-Transport-of-ISO-BMFF-Based-DVB-Services_Draft-ts_103-285-v140_November_2021.pdf "https://dvb.org/wp-content/uploads/2021/06/A168r4_MPEG-DASH-Profile-for-Transport-of-ISO-BMFF-Based-DVB-Services_Draft-ts_103-285-v140_November_2021.pdf") linked above.

**Error metrics reporting URL**

The URL to which a reporting player will send error
reports.

**Probability**

The number of playback devices per 1000 that will send
error reports to the reporting URL. This integer
represents the probability that the playback device will
be a reporting player for this session. 16. For **Ad markers**, choose how ad markers are
signaled in the output manifests. All the non-ad markers that you
include in the content stream in your upstream encoders will also be
present in the output manifests. Choose from the following
options:

    * **Binary** – The SCTE-35 marker is
     expressed as a hex-string (Base64 string) rather than full
     XML.
    * **XML** – The SCTE marker is
     expressed fully in XML.

17. Select **Enable filter configuration** if you
    want to optionally add filters and settings to modify manifests.
    These filters apply to all manifests that originate from this
    endpoint.

To automatically fill these values from an existing query string,
choose **Import from query string**.
For example, this string provides the following filters:
`aws.manifestfilter=video_codec:h265;audio_language:fr,en-US,de&start=2023-10-20T12:20:50Z&end=2023-10-20T13:20:50Z&time_delay=10`

**Filter key**
`video_codec`, **Filter value**
`h265`, **Filter key**
`audio_language`, **Filter value**
`fr,en-US`, **Start time**
`2023-10-20T12:20:50Z`, **End time**
`2023-10-20T13:20:50Z`, and **Time
delay**
`10` seconds.

###### Note

When you include a Manifest filter, you cannot use
matching query parameters for the manifest's endpoint URL.
If you do, you will receive a `404` HTTP error
code instead. For example, if you include a Manifest filter
with a `audio_sample_rate` Filter key and
`44100` Filter value, and you make an HTTP
request for
`https://<example-url>/?aws.manifestfilter=audio_sample_rate:44100`,
you will receive a `404` error.

**Manifest filter**

Optionally specify one or more manifest filters for
all of your manifest egress requests.

You enter a **Filter key** and
**Filter value** pair for each
manifest filter. Your filter values can be a range,
single value, or combination of both.

For a list of supported keys and values, see [Manifest filtering query
parameters](manifest-filter-query-parameters.md "manifest-filter-query-parameters.md").

**Start time and End time**

Optionally specify the start or end time for all of
your manifest egress requests. To use this setting, you
must have a startover window defined.

For more information about start and end times, see
[Start and end parameters](start-and-end-parameters-rules.md "start-and-end-parameters-rules.md").

If you enter a start or end time using the API, or
import using **Import from query
string** in the MediaPackage console,
enter dates in an ISO-8601 format.

**Time delay**

Optionally specify the time delay (in seconds) for all
of your manifest egress requests. To use this setting,
you must have a startover window defined.

For more information about using time delays, see
[Time delay](time-delay.md "time-delay.md").

**Clip start time data and time**

When using a time delay, optionally specify the clip
start time for all of your manifest egress requests.
This option specifies the earliest time that the content
can result in a manifest. Content ingested before the
clip start time will not be included in the manifest.
Cannot be used with start time or end time filters. To
use this setting, you must have a startover window
defined.

For more information about clip start and time delay,
see [Using clip start with time delay](time-delay.md#clip-start "time-delay.md#clip-start").

###### Important

If you're using this setting to limit content
playback for contractual reasons, this parameter
should be set at your CDN, and not at the client.
This topic shows you how to configure an endpoint in AWS Elemental MediaPackage to create Microsoft Smooth
Streaming (MSS) manifests. MSS manifests require the ISM container type.

###### MSS requirements and limitations

When creating an MSS manifest, note the following requirements and limitations:

**Configuration requirements**

- You must select ISM as the container type
- Only PlayReady DRM is supported for encryption
  **Feature limitations**

- SCTE-35 is not supported
- Key rotation is not supported for encrypted content
- Lookahead fragments are automatically set to 2 and are not configurable
- CDK constructs support may be limited (contact AWS Support for current status)
- Auto support for ISM constructs is not enabled
  **Technical specifications**

- URLs end with `.ism/Manifest` instead of `.html`
- Manifest MIME type is `text/xml`
  For information about URL limits and endpoint quotas, see [Quotas in AWS Elemental MediaPackage](quotas.md "quotas.md").

###### To create an MSS manifest

1.  For **Manifest name**, enter a short string that will be appended
    to the endpoint URL. The manifest name creates a unique path to this endpoint. If
    you don't enter a value, MediaPackage uses the default manifest name,
    _index_. MediaPackage automatically inserts the format extension,
    such as .isml. Supported characters are **A-Z**,
    **a-z**, **0-9**, and
    **-** (hyphen). You can't use underscores in the
    name.
2.  For **Manifest window (sec.)** enter the total duration (in
    seconds) of the manifest's content. The default value is 60 seconds. The maximum manifest window is 900 seconds (15
    minutes). You can request a quota increase if necessary.
3.  For **Manifest layout**, choose how MediaPackage formats the
    manifest:

        * **Full** – Each fragment in the sequence has an
         explicit value for the duration field and an implicit value for the time
         field, except the first fragment, whose start-time is explicit.
        * **Compact** – Uses the FragmentRepeat field on
         segments that share the same attributes and length to reduce manifest size.
         This can significantly reduce manifest length for streams with consistent
         segment durations.

    For most use cases, **Compact** is recommended as it reduces
    manifest size and network overhead.

4.  For **Lookahead fragment count**, the value is automatically set
    to 2 and cannot be changed for MSS manifests. This buffer helps ensure smooth
    playback.

MSS includes the concept of server lookahead, where a buffer of segments is held
back by the server until future segments are available. This means that segments
right at the live edge will not be included in the manifest until the specified
number of lookahead fragments are internally available.

The lookahead is ignored when the stream has ended or when there's a discontinuity
between segments. 5. Select **Enable filter configuration** if you want to optionally
add filters and settings to modify manifests. These filters apply to all manifests
that originate from this endpoint.

To automatically fill these values from an existing query string, choose **Import from query string**.

###### Note

When you include a Manifest filter, you cannot use matching query
parameters for the manifest's endpoint URL. If you do, you will receive a
`404` HTTP error code instead.

**Manifest filter**

Optionally specify one or more manifest filters for all of your
manifest egress requests.

You enter a **Filter key** and **Filter
value** pair for each manifest filter. Your filter values
can be a range, single value, or combination of both.

For a list of supported keys and values, see [Manifest filtering query
parameters](manifest-filter-query-parameters.md "manifest-filter-query-parameters.md").

**Start time and End time**

Optionally specify the start or end time for all of your manifest
egress requests. To use this setting, you must have a startover window
defined.

For more information about start and end times, see [Start and end parameters](start-and-end-parameters-rules.md "start-and-end-parameters-rules.md").

If you enter a start or end time using the API, or import using
**Import from query string** in the MediaPackage
console, enter dates in an ISO-8601 format.

**Time delay**

Optionally specify the time delay (in seconds) for all of your
manifest egress requests. To use this setting, you must have a startover
window defined.

For more information about using time delays, see [Time delay](time-delay.md "time-delay.md").

**Clip start time data and time**

When using a time delay, optionally specify the clip start time for
all of your manifest egress requests. This option specifies the earliest
content that can be included in the manifest. Content ingested before
the clip start time will not be included in the manifest. Cannot be used
with start time or end time filters. To use this setting, you must have
a startover window defined.

For more information about clip start and time delay, see [Using clip start with time delay](time-delay.md#clip-start "time-delay.md#clip-start").

###### Important

If you're using this setting to limit content playback for
contractual reasons, this parameter should be set at your CDN, and
not at the client.
After you've configured your MSS manifest, choose **Create** to create
the endpoint. For information about testing your MSS endpoint, see [Testing MSS playback in AWS Elemental MediaPackage](mss-testing-playback.md "mss-testing-playback.md"). For
troubleshooting information, see [Troubleshooting MSS endpoints in AWS Elemental MediaPackage](mss-troubleshooting.md "mss-troubleshooting.md").
