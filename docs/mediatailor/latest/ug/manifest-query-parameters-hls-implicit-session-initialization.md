# MediaTailor

HLS implicit session initialization

AWS Elemental MediaTailor includes query parameters in links to MediaTailor resources when your request
includes query parameters with the key
`manifest.`\*``. The following example shows this
request format:

```
GET /v1/master/`111122223333`/`originId`/index.m3u8?manifest.test=123&other=456
```

Links don't include the `manifest.` prefix.

###### Parameter application in HLS

For HLS implicit sessions, MediaTailor applies parameters to the following locations in
the manifest hierarchy:

- Multivariant playlist URLs
- Media playlist URLs
- Content segment URLs
- Ad segment URLs
- HLS initialization URLs

###### Example multivariant playlist

The following example shows how MediaTailor includes the query parameters in the URL for
the multivariant playlist:

```
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-INDEPENDENT-SEGMENTS
#EXT-X-MEDIA:LANGUAGE="eng",AUTOSELECT=YES,FORCED=NO,TYPE=SUBTITLES,URI="../../../manifest/`111122223333`/`originId`/`session`/1.m3u8?test=123",GROUP-ID="subtitles",DEFAULT=YES,NAME="caption_1"
#EXT-X-STREAM-INF:CODECS="avc1.640029,mp4a.40.2",AVERAGE-BANDWIDTH=2525657,RESOLUTION=960x540,SUBTITLES="subtitles",FRAME-RATE=29.97,BANDWIDTH=2665212
../../../manifest/`111122223333`/`originId`/`session`/0.m3u8?test=123
```

###### Example media playlist

The following example shows how MediaTailor includes the query parameters in the URLs
for the content segments:

```
#EXTM3U
#EXT-X-VERSION:6
#EXT-X-TARGETDURATION:7
#EXT-X-MEDIA-SEQUENCE:28716269
#EXT-X-DISCONTINUITY-SEQUENCE:0
#EXTINF:6.006,
https://origin.com/contentSegment_1.ts?originQueryParam=foo&test=123
#EXT-X-DISCONTINUITY
#EXTINF:6.006,
../../../../segment/`111122223333`/`originId`/`session`/0/2?test=123
```
