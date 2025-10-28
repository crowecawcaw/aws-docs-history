# Monitoring manifest update time in

AWS Elemental MediaPackage

MediaPackage playback responses include the following custom headers that indicate
when MediaPackage last modified the manifest in non-dynamic ad insertion workflows. These
headers are helpful when troubleshooting issues related to stale manifests.

**X-Amzn-Mediapackage-Manifest-Last-Part**

This is only provided on requests for low-latency HLS manifests, and is the highest
part sequence number in the manifest.

**X-MediaPackage-Manifest-Last-Sequence**

This is the highest segment sequence number in the manifest.

For HLS and CMAF, this is the highest segment number in the media playlist.

See the following section for [manifest
example](#manifest-last-updated "#manifest-last-updated").

**X-MediaPackage-Manifest-Last-Updated**

The epoch timestamp in milliseconds when MediaPackage generates the segment referred to in
`X-MediaPackage-Manifest-Last-Sequence`.

## HLS manifest example

### HLS manifest

MediaPackage determines the `X-MediaPackage-Manifest-Last-Sequence` value from the
last segment in the manifest. For example, in the following manifest
`index_1_3.ts` is the highest segment sequence number, so the value of
`X-MediaPackage-Manifest-Last-Sequence` is `3`. The value of
`X-MediaPackage-Manifest-Last-Updated` corresponds to the epoch timestamp in
milliseconds when MediaPackage generates the last segment in the manifest.

```
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-TARGETDURATION:8
#EXT-X-MEDIA-SEQUENCE:0
#EXTINF:7.500,
index_1_0.ts?m=1583172400
#EXTINF:7.500,
index_1_1.ts?m=1583172400
#EXTINF:7.500,
index_1_2.ts?m=1583172400
#EXTINF:7.500,
index_1_3.ts?m=1583172400
#EXT-X-ENDLIST

```
