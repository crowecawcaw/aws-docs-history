# Kinesis Video Streams playback

You can view a Kinesis video stream using the following methods:

- **GetMedia** – You can use the `GetMedia` API to build
  your own applications to process Kinesis Video Streams. `GetMedia` is a real-time API with low latency. To create a
  player that uses `GetMedia`, you must build it yourself. For information about how to develop an
  application that displays a Kinesis video stream using `GetMedia`, see [Stream using parser library](parser-library.md "parser-library.md").
- **HLS** – [HTTP Live Streaming (HLS)](https://en.wikipedia.org/wiki/HTTP_Live_Streaming "https://en.wikipedia.org/wiki/HTTP_Live_Streaming") is an industry
  standard HTTP-based media streaming communications protocol. You can use HLS to view a Kinesis video stream, either for
  live playback or to view archived video.

You can use HLS for live playback. Latency is typically between 3–5 seconds, but it can be
between 1–10 seconds, depending on the use case, player, and network conditions. You can use a
third-party player (such as [Video.js](https://github.com/videojs/video.js/ "https://github.com/videojs/video.js/") or [Google Shaka Player](https://github.com/google/shaka-player "https://github.com/google/shaka-player")) to display the video stream by
providing the HLS streaming session URL, either programmatically or manually. You can also play back video by
entering the HLS streaming session URL in the **Location** bar of the [Apple Safari](https://www.apple.com/safari/ "https://www.apple.com/safari/") or [Microsoft Edge](https://www.microsoft.com/en-us/edge "https://www.microsoft.com/en-us/edge") browsers.

- **MPEG-DASH** – [Dynamic Adaptive Streaming over HTTP
  (DASH)](https://en.wikipedia.org/wiki/Dynamic_Adaptive_Streaming_over_HTTP "https://en.wikipedia.org/wiki/Dynamic_Adaptive_Streaming_over_HTTP"), also known as MPEG-DASH, is an adaptive bitrate streaming protocol that enables high quality
  streaming of media content over the internet delivered from conventional HTTP web servers.

You can use MPEG-DASH for live playback. Latency is typically between 3–5 seconds, but it can
be between 1–10 seconds, depending on the use case, player, and network conditions. You can use a
third-party player (such as [dash.js](https://github.com/Dash-Industry-Forum/dash.js/wiki "https://github.com/Dash-Industry-Forum/dash.js/wiki") or
[Google Shaka Player](https://github.com/google/shaka-player "https://github.com/google/shaka-player")) to display the video stream
by providing the MPEG-DASH streaming session URL, either programmatically or manually.

- **GetClip** – You can use the `GetClip` API to
  download a clip (in an MP4 file) containing the archived, on-demand media from the specified video stream over
  the specified time range. For more information, see the [GetClip](API_reader_GetClip.md "API_reader_GetClip.md") API
  Reference.

###### Topics

- [Video playback track requirements](video-playback-requirements.md "video-playback-requirements.md")
- [Video playback with HLS](hls-playback.md "hls-playback.md")
- [Video playback with MPEG-DASH](dash-playback.md "dash-playback.md")
