# Video playback track requirements

Amazon Kinesis Video Streams supports media encoded in multiple formats. If your Kinesis video stream uses a format
not supported by one of the four APIs listed below, use [`GetMedia`](API_dataplane_GetMedia.md "API_dataplane_GetMedia.md") or [`GetMediaForFragmentList`](API_reader_GetMediaForFragmentList.md "API_reader_GetMediaForFragmentList.md"), as they don't have track-type
limitations.

###### Topics

- [GetClip requirements](#requirements-getclip "#requirements-getclip")
- [GetDASHStreamingSessionURL requirements](#requirements-getdash "#requirements-getdash")
- [GetHLSStreamingSessionURL requirements](#requirements-gethls "#requirements-gethls")
- [GetImages requirements](#requirements-getimages "#requirements-getimages")

## GetClip requirements

For more information about this API, see [`GetClip`](API_reader_GetClip.md "API_reader_GetClip.md").

| Track 1 description | Track 1 codec ID | Track 2 description      | Track 2 codec ID |
| ------------------- | ---------------- | ------------------------ | ---------------- |
| H.264 video         | V_MPEG4/ISO/AVC  | N/A                      | N/A              |
| H.264 video         | V_MPEG4/ISO/AVC  | AAC audio                | A_AAC            |
| H.264 video         | V_MPEG4/ISO/AVC  | G.711 audio (A-Law only) | A_MS/ACM         |
| H.265 video         | V_MPEGH/ISO/HEVC | N/A                      | N/A              |
| H.265 video         | V_MPEGH/ISO/HEVC | AAC audio                | A_AAC            |

###### Important

The codec private data (CPD) contained in each fragment contains codec-specific initialization
information, such as frame rate, resolution, and encoding profile, which are
necessary to properly decode the fragment. CPD changes aren't supported between
the target fragments of the resulting clip. The CPD must remain consistent
through the queried media, otherwise an error will be returned.

###### Important

Track changes aren't supported. Tracks must remain consistent throughout the
queried media. An error is returned if the fragments in the stream change from
having only video to having both audio and video, or if an AAC audio track is
changed to an A-Law audio track.

## GetDASHStreamingSessionURL requirements

For more information about this API, see [`GetDASHStreamingSessionURL`](API_reader_GetDASHStreamingSessionURL.md "API_reader_GetDASHStreamingSessionURL.md").

| Track 1 description | Track 1 codec ID | Track 2 description      | Track 2 codec ID |
| ------------------- | ---------------- | ------------------------ | ---------------- |
| H.264 video         | V_MPEG4/ISO/AVC  | N/A                      | N/A              |
| H.264 video         | V_MPEG4/ISO/AVC  | AAC audio                | A_AAC            |
| H.264 video         | V_MPEG4/ISO/AVC  | G.711 audio (A-Law only) | A_MS/ACM         |
| H.264 video         | V_MPEG4/ISO/AVC  | G.711 audio (U-Law only) | A_MS/ACM         |
| AAC audio           | A_AAC            | N/A                      | N/A              |
| H.265 video         | V_MPEGH/ISO/HEVC | N/A                      | N/A              |
| H.265 video         | V_MPEGH/ISO/HEVC | AAC audio                | A_AAC            |

###### Important

The codec private data (CPD) contained in each fragment contains codec-specific
initialization information, such as frame rate, resolution, and encoding
profile, which are necessary to properly decode the fragment. CPD changes aren't
supported during a streaming session. The CPD must remain consistent through the
queried media.

###### Important

Track changes aren't supported. Tracks must remain consistent throughout the
queried media. Streaming will fail if the fragments in the stream change from
having only video to having both audio and video, or if an AAC audio track is
changed to an A-Law audio track.

## GetHLSStreamingSessionURL requirements

For more information about this API, see [`GetHLSStreamingSessionURL`](API_reader_GetHLSStreamingSessionURL.md "API_reader_GetHLSStreamingSessionURL.md").

| HLS Mp4     | Track 1 description | Track 1 codec ID | Track 2 description | Track 2 codec ID |
| ----------- | ------------------- | ---------------- | ------------------- | ---------------- |
| H.264 video | V_MPEG4/ISO/AVC     | N/A              | N/A                 |
| H.264 video | V_MPEG4/ISO/AVC     | AAC audio        | A_AAC               |
| AAC audio   | A_AAC               | N/A              | N/A                 |
| H.265 video | V_MPEGH/ISO/HEVC    | N/A              | N/A                 |
| H.265 video | V_MPEGH/ISO/HEVC    | AAC audio        | A_AAC               |

| HLS TS      | Track 1 description | Track 1 codec ID | Track 2 description | Track 2 codec ID |
| ----------- | ------------------- | ---------------- | ------------------- | ---------------- |
| H.264 video | V_MPEG4/ISO/AVC     | N/A              | N/A                 |
| H.264 video | V_MPEG4/ISO/AVC     | AAC audio        | A_AAC               |
| AAC audio   | A_AAC               | N/A              | N/A                 |

###### Note

The codec private data (CPD) contained in each fragment contains codec-specific initialization
information, such as frame rate, resolution, and encoding profile, which are
necessary to properly decode the fragment. For both TS and MP4, CPD changes are
supported during a streaming session. Therefore, the fragments in a session can
have a different information in the CPD without interrupting playback. For each
streaming session, only 500 CPD changes are allowed.

###### Important

Track changes aren't supported. Tracks must remain consistent throughout the queried media. Streaming will fail if the fragments in the stream change from having only video to having both audio and video, or if an AAC audio track is changed to an A-Law audio track.

## GetImages requirements

For more information about this API, see [`GetImages`](API_reader_GetImages.md "API_reader_GetImages.md").

###### Note

The `GetImages` media should contain a video track in track 1.
