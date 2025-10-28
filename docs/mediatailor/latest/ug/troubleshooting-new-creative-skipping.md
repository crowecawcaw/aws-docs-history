# MediaTailor NEW_CREATIVE ad skipping

troubleshooting

When ads are skipped with the `NEW_CREATIVE` reason, AWS Elemental MediaTailor encountered
an ad that requires transcoding before insertion. This troubleshooting guide explains
the causes and provides step-by-step resolution procedures.

## What causes NEW_CREATIVE skipping

MediaTailor transcodes ads based on three key factors: creative ID, AWS Account ID, and
transcode variant set (the playback renditions for the underlying content stream).
When any part of the creative ID or transcode variant set differs, MediaTailor recognizes
the ad as a new variant that requires transcoding.

### Bitrate changes

Bitrate changes can cause NEW_CREATIVE skipping when the bitrate doesn't match
after rounding to the nearest 8,000 bits. This commonly occurs in the following
situations:

- The underlying content stream changes the primary manifest
- New sessions are created with different variants than existing
  sessions
- Content stream bitrates are inconsistent across playback
  sessions

#### Harvest job bandwidth

variance

For harvest jobs, MediaTailor uses a 15% bandwidth variance threshold when
matching ads to content streams. If there is a difference of 15% or more
between the bandwidth of the live stream and the bandwidth of the harvested
HLS file, the ad will be transcoded again. This can result in NEW_CREATIVE
skipping during the transcoding process.

This behavior commonly occurs when:

- The same pre-transcoded ads are used for both live streaming and
  VOD content
- The harvested content has different encoding parameters than the
  original live stream
- Bandwidth differences exceed the 15% threshold between live and
  harvested content

### Creative ID conflicts

When MediaTailor encounters a different creative ID for a media file that was
already transcoded, the following sequence occurs:

1. The ad is skipped with reason NEW_CREATIVE
2. This leads to an unnecessary transcoding attempt
3. The creative is marked as DUPLICATE_TRANSCODE or COPY_DEDUP

###### Note

MediaTailor does not expire or delete transcoded ads. We store them in a
MediaTailor-owned S3 bucket indefinitely.

## Resolution steps

To resolve NEW_CREATIVE ad skipping issues:

1. Verify that your ad decision server returns consistent creative IDs for
   the same ad content.
2. Check that your content stream maintains consistent bitrates and variant
   sets.
3. Consider implementing ad prefetching to ensure ads are transcoded before
   playback. For more information, see [Prefetching ads](prefetching-ads.md "prefetching-ads.md").
4. For persistent issues, contact [AWS Support](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/") for additional troubleshooting
   assistance.

## Monitoring NEW_CREATIVE patterns

Use this CloudWatch Logs Insights query to analyze patterns in NEW_CREATIVE ad
skipping:

````

fields @timestamp, sessionId, creativeId, skipReason, MediaFileSourceUrl
| filter skipReason = "NEW_CREATIVE"
| stats count() by creativeId, MediaFileSourceUrl
| sort count desc
| limit 50 ```
````
