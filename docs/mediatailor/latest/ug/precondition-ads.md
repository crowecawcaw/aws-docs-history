# Using preconditioned ads with AWS Elemental MediaTailor

In a [typical ad insertion workflow](what-is-flow.md "what-is-flow.md"), MediaTailor dynamically
transcodes ads to match the content stream, saves them, and stitches the ads into the live stream.
Because this process happens only after MediaTailor receives the ad in a VAST response from the ad
decision server (ADS), there is a delay for when the ad is available for stitching. If additional
latency is introduced to the ad stitching workflow (either because of ADS timeout or other content
or network issues), MediaTailor could partially fill the avail, or miss the ad break altogether.

To reduce the time needed to stitch ads into your content, you can use preconditioned ads. A
preconditioned ad is one that you transcode before using it in MediaTailor ad insertion. Instead of
providing URLs for the unconditioned ads to your ADS, you provide the URLs for the preconditioned
ads. In its VAST response to the MediaTailor request, the ADS includes direct links to the
preconditioned ads. By removing the transcoding part of ad stitching, MediaTailor needs to just save the
ad and stitch it into the content stream. The ad stitching process with preconditioned ads reduces
the time between when MediaTailor is made aware of an ad through the VAST response and when the ad is
stitched into the content.

Alternatively, you can also use ad prefetching, which is when you configure MediaTailor to perform
the ad stitching process at a scheduled time before the ad break is needed. For more information
about ad prefetching, see [Prefetching ads](prefetching-ads.md "prefetching-ads.md").

## Preconditioned ads requirements

The following are requirements to consider when setting up an ad stitching workflow with
preconditioned ads.

### `MediaFiles` requirements

The VAST response that the ad server sends to MediaTailor must include `MediaFiles` that meet these requirements:

The ad (`Creative`) must have variants that conform to the bitrate variants of the
content stream._It's your responsibility to ensure that the VAST
response uses the right ad variants to match template manifests._

While using preconditioned ads can help make ad insertion more efficient, MediaTailor does not
have the ability to manage the transcoding process to ensure that the media files for the ads
are compatible with the content manifest specifications. If the ad doesn't match the content
stream, MediaTailor could miss the insertion or the mismatch could cause the playback device to error.

Additionally, to be stitched into the content stream without MediaTailor transcoding, a
`MediaFile` must meet these requirements:

- It must be accessible on the public internet so that MediaTailor can download it.
- It must use streaming delivery, denoted as `delivery="streaming"` in the VAST
  response.
- It must be either a `.m3u8` (for HLS) or `.mpd` (for DASH) file.

###### Example VAST response

From the following example VAST response, MediaTailor inserts the `MediaFile` with
the following URLs:

- For an HLS stream, MediaTailor uses
  `https://example-ad-origin.amazonaws.com/ad1/index_low.m3u8`. This is the first
  `MediaFile` with streaming delivery and a supported file extension
  (.`m3u8`).
- For a DASH stream, MediaTailor uses
  `https://example-ad-origin.amazonaws.com/ad1/index.mpd`. This is the first
  `MediaFile` with streaming delivery and a supported file extension
  (.`mpd`).

```
<?xml version="1.0" encoding="UTF-8"?>
<VAST xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" version="3.0">
    <Ad id="ad1">
        <InLine>
            <AdSystem>ExampleAdSystem</AdSystem>
            <AdTitle>ad1</AdTitle>
            <Impression><![CDATA[https://example-impression.amazonaws.com]]></Impression>
            <AdServingId>de8e0d33-9c72-4d77-bb3a-f7e566ffc605</AdServingId>
            <Creatives>
                <Creative id="creativeId1" sequence="1">
                    <Linear skipoffset="00:00:05">
                        <Duration>00:00:30</Duration>
                        <MediaFiles>
                            <MediaFile delivery="progressive" width="1280" height="720" type="video/mp4" bitrate="533" scalable="true" maintainAspectRatio="true"><![CDATA[https://example-ad-origin.amazonaws.com/ad1/ad1.mp4]]></MediaFile>
                            <MediaFile delivery="streaming" width="1280" height="720" type="application/dash+xml" bitrate="533" scalable="true" maintainAspectRatio="true"><![CDATA[https://example-ad-origin.amazonaws.com/ad1/index.mpd]]></MediaFile>
                            <MediaFile delivery="streaming" width="640" height="360" type="application/x-mpegURL" bitrate="262" scalable="true" maintainAspectRatio="true"><![CDATA[https://example-ad-origin.amazonaws.com/ad1/index_low.m3u8]]></MediaFile>
                            <MediaFile delivery="streaming" width="2560" height="1440" type="application/x-mpegURL" bitrate="1066" scalable="true" maintainAspectRatio="true"><![CDATA[https://example-ad-origin.amazonaws.com/ad1/index_high.m3u8]]></MediaFile>
                        </MediaFiles>
                    </Linear>
                </Creative>
            </Creatives>
        </InLine>
    </Ad>
</VAST>
```

### Ad manifest requirements

To use preconditioned ads, your parent and child ad manifests must meet these
requirements:

- The manifest that's linked in the `Creative` section of the VAST response must
  be the parent ad manifest.
- The URLs for the child ad manifests must be relative paths.
- The child ad manifests must be in the same directory as the parent multivariant playlist, at the same
  level. Child manifests can't be in a sub-directory or other location.

###### Example supported parent multivariant playlist

The following parent ad multivariant playlist contains relative URLs for child ad media
playlists. The child playlists are also in the same directory as the parent multivariant
playlist.

```
#EXTM3U
#EXT-X-STREAM-INF:BANDWIDTH=150000,RESOLUTION=416x234,CODECS="avc1.42e00a,mp4a.40.2"
index_1.m3u8
#EXT-X-STREAM-INF:BANDWIDTH=440000,RESOLUTION=416x234,CODECS="avc1.42e00a,mp4a.40.2"
index_2.m3u8
#EXT-X-STREAM-INF:BANDWIDTH=640000,RESOLUTION=640x360,CODECS="avc1.42e00a,mp4a.40.2"
index_3.m3u8
```

###### Example unsupported parent multivariant playlist: subdirectories

The following parent ad multivariant playlist contains child playlists that are in sub-directories relative to the parent multivariant playlist. It is not a supported playlist for preconditioned ads.

```
#EXTM3U
#EXT-X-STREAM-INF:BANDWIDTH=150000,RESOLUTION=416x234,CODECS="avc1.42e00a,mp4a.40.2"
child/index_1.m3u8
#EXT-X-STREAM-INF:BANDWIDTH=440000,RESOLUTION=416x234,CODECS="avc1.42e00a,mp4a.40.2"
child/index_2.m3u8
#EXT-X-STREAM-INF:BANDWIDTH=640000,RESOLUTION=640x360,CODECS="avc1.42e00a,mp4a.40.2"
child/index_3.m3u8
```

###### Example unsupported parent multivariant playlist: absolute URLs

The following parent ad multivariant playlist contains child playlists with absolute URLs. It is not a supported playlist for preconditioned ads.

```
#EXTM3U
#EXT-X-STREAM-INF:BANDWIDTH=150000,RESOLUTION=416x234,CODECS="avc1.42e00a,mp4a.40.2"
https://example.mediatailor.us-west-2.amazonaws.com/index_1.m3u8
#EXT-X-STREAM-INF:BANDWIDTH=440000,RESOLUTION=416x234,CODECS="avc1.42e00a,mp4a.40.2"
https://example.mediatailor.us-west-2.amazonaws.com/index_2.m3u8
#EXT-X-STREAM-INF:BANDWIDTH=640000,RESOLUTION=640x360,CODECS="avc1.42e00a,mp4a.40.2"
https://example.mediatailor.us-west-2.amazonaws.com/index_3.m3u8
```

## Preconditioned ads workflow

The following is a basic description of how preconditioned ads work in an ad stitching
workflow with MediaTailor. The first part of the workflow are actions that you must take to get set up
for using preconditioned ads. The second part describes how MediaTailor processes the ads.

###### Part 1: Preconditioned ads set up

Complete the following steps to set up a workflow that uses preconditioned ads in
MediaTailor.

1. Use a transcoder service, such as AWS Elemental MediaConvert, to condition your creatives into variants
   that support the different bitrates, resolutions, and codecs of your template manifests.
2. Provide the URLs for the pre-transcoded media files to your ADS, for use in VAST
   responses.
3. [Create your playback](configurations-create.md "configurations-create.md") configuration in MediaTailor.
   To use preconditioned ads, select **None** for the **Streaming media
   file conditioning** setting in the configuration.
4. Continue with your content delivery set up as you normally would.

###### Part 2: MediaTailor ad processing

MediaTailor ad stitching completes as described in [How MediaTailor ad insertion works](what-is-flow.md "what-is-flow.md"). When MediaTailor receives a VAST response from the ADS, it uses the
following logic to determine what actions to take for the ads. This logic is dictated by the
**Streaming media file conditioning** setting on the playback configuration.

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
