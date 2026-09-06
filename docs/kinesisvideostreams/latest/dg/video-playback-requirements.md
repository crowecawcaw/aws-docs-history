

# Video playback track requirements
<a name="video-playback-requirements"></a>

Amazon Kinesis Video Streams supports media encoded in multiple formats. If your Kinesis video stream uses a format not supported by one of the four APIs listed below, use [`GetMedia`](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_dataplane_GetMedia.html) or [`GetMediaForFragmentList`](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_reader_GetMediaForFragmentList.html), as they don't have track-type limitations. 

**Topics**
+ [GetClip requirements](#requirements-getclip)
+ [GetDASHStreamingSessionURL requirements](#requirements-getdash)
+ [GetHLSStreamingSessionURL requirements](#requirements-gethls)
+ [GetImages requirements](#requirements-getimages)

## GetClip requirements
<a name="requirements-getclip"></a>

For more information about this API, see [`GetClip`](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_reader_GetClip.html).


| Track 1 description | Track 1 codec ID | Track 2 description | Track 2 codec ID | 
| --- | --- | --- | --- | 
| H.264 video | V\_MPEG4/ISO/AVC | N/A | N/A | 
| H.264 video | V\_MPEG4/ISO/AVC | AAC audio | A\_AAC | 
| H.264 video | V\_MPEG4/ISO/AVC | G.711 audio (A-Law only) | A\_MS/ACM | 
| H.265 video | V\_MPEGH/ISO/HEVC | N/A | N/A | 
| H.265 video | V\_MPEGH/ISO/HEVC | AAC audio | A\_AAC | 

**Important**  
The codec private data (CPD) contained in each fragment contains codec-specific initialization information, such as frame rate, resolution, and encoding profile, which are necessary to properly decode the fragment. CPD changes aren't supported between the target fragments of the resulting clip. The CPD must remain consistent through the queried media, otherwise an error will be returned.

**Important**  
Track changes aren't supported. Tracks must remain consistent throughout the queried media. An error is returned if the fragments in the stream change from having only video to having both audio and video, or if an AAC audio track is changed to an A-Law audio track.

## GetDASHStreamingSessionURL requirements
<a name="requirements-getdash"></a>

For more information about this API, see [`GetDASHStreamingSessionURL`](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_reader_GetDASHStreamingSessionURL.html).


| Track 1 description | Track 1 codec ID | Track 2 description | Track 2 codec ID | 
| --- | --- | --- | --- | 
| H.264 video | V\_MPEG4/ISO/AVC | N/A | N/A | 
| H.264 video | V\_MPEG4/ISO/AVC | AAC audio | A\_AAC | 
| H.264 video | V\_MPEG4/ISO/AVC | G.711 audio (A-Law only) | A\_MS/ACM | 
| H.264 video | V\_MPEG4/ISO/AVC | G.711 audio (U-Law only) | A\_MS/ACM | 
| AAC audio | A\_AAC | N/A | N/A | 
| H.265 video | V\_MPEGH/ISO/HEVC | N/A | N/A | 
| H.265 video | V\_MPEGH/ISO/HEVC | AAC audio | A\_AAC | 

**Important**  
The codec private data (CPD) contained in each fragment contains codec-specific initialization information, such as frame rate, resolution, and encoding profile, which are necessary to properly decode the fragment. CPD changes aren't supported during a streaming session. The CPD must remain consistent through the queried media.

**Important**  
Track changes aren't supported. Tracks must remain consistent throughout the queried media. Streaming will fail if the fragments in the stream change from having only video to having both audio and video, or if an AAC audio track is changed to an A-Law audio track.

## GetHLSStreamingSessionURL requirements
<a name="requirements-gethls"></a>

For more information about this API, see [`GetHLSStreamingSessionURL`](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_reader_GetHLSStreamingSessionURL.html).


**HLS Mp4**  

| Track 1 description | Track 1 codec ID | Track 2 description | Track 2 codec ID | 
| --- | --- | --- | --- | 
| H.264 video | V\_MPEG4/ISO/AVC | N/A | N/A | 
| H.264 video | V\_MPEG4/ISO/AVC | AAC audio | A\_AAC | 
| AAC audio | A\_AAC | N/A | N/A | 
| H.265 video | V\_MPEGH/ISO/HEVC | N/A | N/A | 
| H.265 video | V\_MPEGH/ISO/HEVC | AAC audio | A\_AAC | 


**HLS TS**  

| Track 1 description | Track 1 codec ID | Track 2 description | Track 2 codec ID | 
| --- | --- | --- | --- | 
| H.264 video | V\_MPEG4/ISO/AVC | N/A | N/A | 
| H.264 video | V\_MPEG4/ISO/AVC | AAC audio | A\_AAC | 
| AAC audio | A\_AAC | N/A | N/A | 

**Note**  
The codec private data (CPD) contained in each fragment contains codec-specific initialization information, such as frame rate, resolution, and encoding profile, which are necessary to properly decode the fragment. For both TS and MP4, CPD changes are supported during a streaming session. Therefore, the fragments in a session can have a different information in the CPD without interrupting playback. For each streaming session, only 500 CPD changes are allowed.

**Important**  
Track changes aren't supported. Tracks must remain consistent throughout the queried media. Streaming will fail if the fragments in the stream change from having only video to having both audio and video, or if an AAC audio track is changed to an A-Law audio track.

## GetImages requirements
<a name="requirements-getimages"></a>

For more information about this API, see [`GetImages`](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_reader_GetImages.html).

**Note**  
The `GetImages` media should contain a video track in track 1.