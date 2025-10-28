# Video playback with HLS

[HTTP Live Streaming
(HLS)](https://en.wikipedia.org/wiki/HTTP_Live_Streaming "https://en.wikipedia.org/wiki/HTTP_Live_Streaming") is an industry standard HTTP-based media streaming communications
protocol. You can use HLS to view a Kinesis video stream, either for live playback or to view archived
video.

You can use HLS for live playback. Latency is typically between 3–5 seconds, but it can be
between 1–10 seconds, depending on the use case, player, and network conditions. You can use
a third-party player (such as [Video.js](https://github.com/videojs/video.js/ "https://github.com/videojs/video.js/") or
[Google Shaka Player](https://github.com/google/shaka-player "https://github.com/google/shaka-player")) to display the video stream
by providing the HLS streaming session URL, either programmatically or manually. You can
also play back video by entering the HLS streaming session URL in the Location bar of the
[Apple Safari](https://www.apple.com/safari/ "https://www.apple.com/safari/") or [Microsoft Edge](https://www.microsoft.com/en-us/edge "https://www.microsoft.com/en-us/edge") browsers.

To view a Kinesis video stream using HLS, first create a streaming session using [GetHLSStreamingSessionURL](API_reader_GetHLSStreamingSessionURL.md "API_reader_GetHLSStreamingSessionURL.md"). This action
returns a URL (containing a session token) for accessing the HLS session. You can then use the URL in a media player
or a standalone application to display the stream.

###### Important

Not all media sent to Kinesis Video Streams can be played back through HLS. See [GetHLSStreamingSessionURL](API_reader_GetHLSStreamingSessionURL.md "API_reader_GetHLSStreamingSessionURL.md") for specific uploading requirements.

###### Topics

- [Use the AWS CLI to retrieve an HLS streaming session URL](#retrieve-hls-url "#retrieve-hls-url")
- [Example: Use HLS in HTML and JavaScript](#how-hls-ex1 "#how-hls-ex1")
- [Troubleshooting HLS issues](#how-hls-ex1-ts "#how-hls-ex1-ts")

## Use the AWS CLI to retrieve an HLS streaming session URL

The following procedure demonstrates how to use the AWS CLI to generate an HLS streaming session URL for a Kinesis video stream.

For installation instructions, see the [AWS Command Line Interface User Guide](../../../cli/latest/userguide/getting-started-install.md#getting-started-install-instructions "../../../cli/latest/userguide/getting-started-install.md#getting-started-install-instructions"). After installation, [configure the AWS CLI](../../../cli/latest/userguide/getting-started-quickstart.md#getting-started-quickstart-new "../../../cli/latest/userguide/getting-started-quickstart.md#getting-started-quickstart-new") with credentials and region.

Alternatively, open the AWS CloudShell terminal, which has the AWS CLI installed and
configured. See the [AWS CloudShell User Guide](../../../cloudshell/latest/userguide/welcome.md#how-to-get-started "../../../cloudshell/latest/userguide/welcome.md#how-to-get-started") for more information.

###### Retrieve the HLS URL endpoint for your Kinesis video stream.

1. Type the following into the terminal:

```
aws kinesisvideo get-data-endpoint \
  --api-name GET_HLS_STREAMING_SESSION_URL \
  --stream-name `YourStreamName`
```

You'll receive a response that looks like this:

```
{
    "DataEndpoint": "https://b-`1234abcd`.kinesisvideo.`aws-region`.amazonaws.com"
}
```

2. Make the HLS streaming session URL request to that returned endpoint.

Live
For live playback, the HLS media playlist is continually updated
with the latest media as it becomes available. When you play this
type of session in a media player, the user interface typically
displays a "**live**" notification,
with no scrubber control for choosing the position in the playback
window to display.

Make sure that you are uploading media to this stream when you run
this command.

```
aws kinesis-video-archived-media get-hls-streaming-session-url \
  --endpoint-url https://b-`1234abcd`.kinesisvideo.`aws-region`.amazonaws.com \
  --stream-name `YourStreamName` \
  --playback-mode LIVE
```

Live replay
For live replay, playback starts from a specified start time. The
HLS media playlist is also continually updated with the latest media
as it becomes available. The session will continue to include newly
ingested media until the session expires, or until the specified end
time, whichever comes first. This mode is useful to be able to start
playback from when an event is detected and continue live streaming
media that has not yet been ingested as of the time of the session
creation.

Determine a start timestamp.

For this example, we use the **Unix Epoch time
in seconds** format. Refer to the [Timestamps](../../../cli/latest/userguide/cli-usage-parameters-types.md#parameter-type-timestamp "../../../cli/latest/userguide/cli-usage-parameters-types.md#parameter-type-timestamp") section in the AWS Command Line Interface User Guide for more
information on timestamp formatting.

See [UnixTime.org](https://unixtime.org/ "https://unixtime.org/") for a conversion tool.

    * **1708471800** is equal to
     **February 20, 2024 3:30:00 PM
     GMT-08:00**

In this example, we don't specify an end timestamp, meaning that
the session will continue to include newly ingested media until the
session expires.

Invoke the `GetHLSStreamingSessionURL` API with
`LIVE_REPLAY` playback mode and an [HLS Fragment Selector](API_reader_GetHLSStreamingSessionURL.md#KinesisVideo-reader_GetHLSStreamingSessionURL-request-HLSFragmentSelector "API_reader_GetHLSStreamingSessionURL.md#KinesisVideo-reader_GetHLSStreamingSessionURL-request-HLSFragmentSelector") specified.

```
aws kinesis-video-archived-media get-hls-streaming-session-url \
  --endpoint-url https://b-`1234abcd`.kinesisvideo.`aws-region`.amazonaws.com \
  --stream-name `YourStreamName` \
  --playback-mode LIVE_REPLAY \
  --hls-fragment-selector \
    "FragmentSelectorType=SERVER_TIMESTAMP,TimestampRange={StartTimestamp=`1708471800`}"
```

On-demand
For on demand playback, the HLS media playlist contains the media
specified by the HLS fragment selector. When this type of session is
played in a media player, the user interface typically displays a
scrubber control for choosing the position in the playback window to
display.

To create a URL for a certain section of stream, first determine
start and end timestamps.

For this example, we use the **Unix Epoch time
in seconds** format. Refer to the [Timestamps](../../../cli/latest/userguide/cli-usage-parameters-types.md#parameter-type-timestamp "../../../cli/latest/userguide/cli-usage-parameters-types.md#parameter-type-timestamp") section in the AWS Command Line Interface User Guide for more
information on timestamp formatting.

See [UnixTime.org](https://unixtime.org/ "https://unixtime.org/") for a conversion tool.

    * **1708471800** is equal to
     **February 20, 2024 3:30:00 PM
     GMT-08:00**
    * **1708471860** is equal to
     **February 20, 2024 3:31:00 PM
     GMT-08:00**

Invoke the `GetHLSStreamingSessionURL` API with
`ON_DEMAND` playback mode and an [HLS Fragment Selector](API_reader_GetHLSStreamingSessionURL.md#KinesisVideo-reader_GetHLSStreamingSessionURL-request-HLSFragmentSelector "API_reader_GetHLSStreamingSessionURL.md#KinesisVideo-reader_GetHLSStreamingSessionURL-request-HLSFragmentSelector") specified.

```
aws kinesis-video-archived-media get-hls-streaming-session-url \
  --endpoint-url https://b-`1234abcd`.kinesisvideo.`aws-region`.amazonaws.com \
  --stream-name `YourStreamName` \
  --playback-mode ON_DEMAND \
  --hls-fragment-selector \
    "FragmentSelectorType=SERVER_TIMESTAMP,TimestampRange={StartTimestamp=`1708471800`,EndTimestamp=`1708471860`}"
```

###### Note

The timestamps must be within 24-hours of each other, as
mentioned in the [HLSTimestampRange](API_reader_HLSTimestampRange.md "API_reader_HLSTimestampRange.md")
documentation.

You'll receive a response that looks like this:

```
{
    "HLSStreamingSessionURL": "https://b-`1234abcd`.kinesisvideo.`aws-region`.amazonaws.com/hls/v1/getHLSMasterPlaylist.m3u8?SessionToken=`CiAz...DkRE6M`~"
}
```

###### Important

Don't share or store this token where an unauthorized entity could access it. The token
provides access to the content of the stream. Safeguard the token with the
same measures that you would use with your AWS credentials.

You can use this URL and any HLS player to view the HLS stream.

For example, use VLC media player.

You can also play the HLS Stream by entering the HLS streaming session URL in
the Location bar of the Apple Safari or Microsoft Edge browsers.

## Example: Use HLS in HTML and JavaScript

The following example shows how to use the AWS SDK for JavaScript v2 to retrieve
an HLS streaming session for a Kinesis video stream and play it back in a web page. The example
shows how to play back video in the following players:

- [Video.js](https://github.com/videojs/video.js/ "https://github.com/videojs/video.js/")
- [Google Shaka
  Player](https://github.com/google/shaka-player "https://github.com/google/shaka-player")
- [hls.js](https://github.com/video-dev/hls.js/ "https://github.com/video-dev/hls.js/")

View the [complete example code](https://github.com/aws-samples/amazon-kinesis-video-streams-media-viewer "https://github.com/aws-samples/amazon-kinesis-video-streams-media-viewer") and [hosted web page](https://aws-samples.github.io/amazon-kinesis-video-streams-media-viewer/ "https://aws-samples.github.io/amazon-kinesis-video-streams-media-viewer/") in GitHub. This static webpage simplifies testing and
experimenting with HLS and MPEG-DASH output from Amazon Kinesis video stream. The example page
provides input fields for the following parameters:

- AWS Region: The Region where your Kinesis video stream is located
- Stream name: The name of your Kinesis video stream
- Playback mode: The HLS playback mode (LIVE, LIVE_REPLAY, or ON_DEMAND)
- Fragment selector type: The method used to select fragments (SERVER_TIMESTAMP or PRODUCER_TIMESTAMP)
- Fragment number: The starting fragment number (when applicable)
- Container format: The format of the media container (FRAGMENTED_MP4 or MPEG_TS)

The application retrieves these values from the input boxes on the HTML page and uses them to construct the request for an HLS streaming session that displays on the page.

###### Code walk through topics:

- [Import the AWS SDK for JavaScript for browsers](#how-hls-ex1-import "#how-hls-ex1-import")
- [Set up the Kinesis Video Streams client](#how-hls-ex1-setup "#how-hls-ex1-setup")
- [Retrieve the endpoint for HLS
  playback](#how-hls-ex1-endpoint "#how-hls-ex1-endpoint")
- [Set up the Kinesis Video Streams archived media client](#how-hls-ex1-session "#how-hls-ex1-session")
- [Retrieve the HLS streaming session URL](#how-hls-ex1-retrieve-url "#how-hls-ex1-retrieve-url")
- [Display the HLS stream on the web
  page](#how-hls-ex1-display "#how-hls-ex1-display")

### Import the AWS SDK for JavaScript for browsers

In the web page, include the following script tag to import the AWS SDK for
JavaScript v2 into the project.

```
<script src="https://cdnjs.cloudflare.com/ajax/libs/aws-sdk/2.490.0/aws-sdk.min.js"></script>
```

For more information, refer to the [AWS SDK for JavaScript](../../../sdk-for-javascript/v2/developer-guide/loading-the-jssdk.md "../../../sdk-for-javascript/v2/developer-guide/loading-the-jssdk.md") documentation.

### Set up the Kinesis Video Streams client

To access streaming video with HLS, first create and configure the Kinesis Video Streams
client. See [Setting Credentials in a Web Browser](../../../sdk-for-javascript/v2/developer-guide/setting-credentials-browser.md "../../../sdk-for-javascript/v2/developer-guide/setting-credentials-browser.md") for other authentication
methods.

```
const clientConfig = {
    accessKeyId: '`YourAccessKey`',
    secretAccessKey: '`YourSecretKey`',
    region: '`us-west-2`'
};
const kinesisVideoClient = new AWS.KinesisVideo(clientConfig);
```

The application retrieves the necessary values from input boxes on the HTML page.

### Retrieve the endpoint for HLS

playback

Use the Kinesis Video Streams client to invoke the [GetDataEndpoint](API_GetDataEndpoint.md "API_GetDataEndpoint.md") API to retrieve the
endpoint.

```
const getDataEndpointOptions = {
    StreamName: '`YourStreamName`',
    APIName: 'GET_HLS_STREAMING_SESSION_URL'
};
const getDataEndpointResponse = await kinesisVideoClient
    .getDataEndpoint(getDataEndpointOptions)
    .promise();
const hlsDataEndpoint = getDataEndpointResponse.DataEndpoint;
```

This code stores the endpoint in the `hlsDataEndpoint`
variable.

### Set up the Kinesis Video Streams archived media client

In the client configuration for the Kinesis Video Streams archived media client, specify the endpoint that you obtained in the previous step.

```
const archivedMediaClientConfig = {
    accessKeyId: '`YourAccessKey'`,
    secretAccessKey: '`YourSecretKey'`,
    region: '`us-west-2`',
    endpoint: hlsDataEndpoint
};
const kinesisVideoArchivedMediaClient = new AWS.KinesisVideoArchivedMedia(archivedMediaClientConfig);
```

### Retrieve the HLS streaming session URL

Use the Kinesis Video Streams archived media client to invoke the [GetHLSStreamingSessionURL](API_reader_GetHLSStreamingSessionURL.md "API_reader_GetHLSStreamingSessionURL.md") API to retrieve the HLS playback URL.

```
const getHLSStreamingSessionURLOptions = {
    StreamName: '`YourStreamName`',
    PlaybackMode: 'LIVE'
};
const getHLSStreamingSessionURLResponse = await kinesisVideoArchivedMediaClient
    .getHLSStreamingSessionURL(getHLSStreamingSessionURLOptions)
    .promise();
const hlsUrl = getHLSStreamingSessionURLResponse.HLSStreamingSessionURL;
```

### Display the HLS stream on the web

page

When you have the HLS streaming session URL, provide it to the video player.
The method for providing the URL to the video player is specific to the player
used.

Video.js
Do the following to import [Video.js](https://github.com/videojs/video.js/ "https://github.com/videojs/video.js/") and its
CSS classes into our browser script:

```
<link rel="stylesheet" href="https://vjs.zencdn.net/6.6.3/video-js.css">
<script src="https://vjs.zencdn.net/6.6.3/video.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/videojs-contrib-hls/5.14.1/videojs-contrib-hls.js"></script>
```

Create a `video` HTML element to display the
video:

```
<video id="videojs" class="player video-js vjs-default-skin" controls autoplay></video>
```

Set the HLS URL as the HTML video element source:

```
const playerElement = document.getElementById('videojs');
const player = videojs(playerElement);
player.src({
    src: `hlsUrl`,
    type: 'application/x-mpegURL'
});
player.play();
```

Shaka
Do the following to import the [Google Shaka player](https://github.com/shaka-project/shaka-player "https://github.com/shaka-project/shaka-player") into our browser script:

```
<script src="https://cdnjs.cloudflare.com/ajax/libs/shaka-player/2.4.1/shaka-player.compiled.js"></script>
```

Create a `video` HTML element to display the video:

```
<video id="shaka" class="player" controls autoplay></video>
```

Create a Shaka player specifying the video element and call the
load method:

```
const playerElement = document.getElementById('shaka');
const player = new shaka.Player(playerElement);
player.load(`hlsUrl`);
```

hls.js
Do the following to import [hls.js](https://github.com/video-dev/hls.js/ "https://github.com/video-dev/hls.js/") into our browser script:

```
<script src="https://cdn.jsdelivr.net/npm/hls.js@latest"></script>
```

Create a `video` HTML element to display the video:

```
<video id="hlsjs" class="player" controls autoplay></video>
```

Create an hls.js player, give it the HLS URL, and tell it to
play:

```
const playerElement = document.getElementById('hlsjs');
const player = new Hls();
player.loadSource(`hlsUrl`);
player.attachMedia(playerElement);
player.on(Hls.Events.MANIFEST_PARSED, function() {
    video.play();
});
```

## Troubleshooting HLS issues

This section describes issues that you might encounter when using HTTP Live Streaming
(HLS) with Kinesis Video Streams.

###### Issues

- [Retrieving HLS streaming session URL
  succeeds, but playback fails in video player](#troubleshooting-hls-playback "#troubleshooting-hls-playback")
- [Latency too high between producer and
  player](#troubleshooting-hls-latency "#troubleshooting-hls-latency")

### Retrieving HLS streaming session URL

succeeds, but playback fails in video player

This situation occurs when you can successfully retrieve an HLS streaming session
URL using `GetHLSStreamingSessionURL`, but the video fails to play back
when the URL is provided to a video player.

To troubleshoot this situation, try the following:

- Determine whether the video stream plays back in the Kinesis Video Streams console.
  Consider any errors that the console shows.
- If the fragment duration is less than one second, increase it to one second. If the fragment
  duration is too short, the service might throttle the player because it's making requests for video
  fragments too frequently.
- Verify that each HLS streaming session URL is being used by only one
  player. If more than one player is using a single HLS streaming session URL,
  the service might receive too many requests and throttle them.
- Verify that your player supports all of the options that you're specifying for the HLS
  streaming session. Try different combinations of values for the following parameters:

      + `ContainerFormat`
      + `PlaybackMode`
      + `FragmentSelectorType`
      + `DiscontinuityMode`
      + `MaxMediaPlaylistFragmentResults`

  Some media players (like HTML5 and mobile players) typically only support HLS with the fMP4
  container format. Other media players (like Flash and custom players) might only support HLS with the MPEG
  TS container format. We recommend experimenting with the `ContainerFormat` parameter to start
  troubleshooting.

- Verify that each fragment has a consistent number of tracks. Verify that fragments in the
  stream are not changing between having both an audio and video track and only a video track. Also verify
  that the encoder settings (resolution and frame rate) are not changing between fragments in each
  track.

### Latency too high between producer and

player

This situation occurs when the latency is too high from when the video is captured
to when it is played in the video player.

Video is played back through HLS on a per-fragment basis. Therefore, latency can't
be less than fragment duration. Latency also includes the time needed for buffering
and transferring data. If your solution requires latency of less than one second,
consider using the `GetMedia` API instead.

You can adjust the following parameters to reduce the overall latency, but
adjusting these parameters might also reduce the video quality or increase the
rebuffering rate.

- **Fragment duration** – The fragment duration is the
  amount of video between divisions in the stream as controlled by the frequency of keyframes generated by the
  video encoder. The recommended value is one second. Having a shorter fragment duration means that less time
  is spent waiting for the fragment to complete before transmitting the video data to the service. Shorter
  fragments are also faster for the service to process. However, if the fragment duration is too short, the
  probability increases that the player will run out of content and have to stop and buffer content. If the
  fragment duration is less than 500 milliseconds, the producer might create too many requests, causing the
  service to throttle them.
- **Bitrate** – A video stream with a lower bitrate takes
  less time to read, write, and transmit. However, a video stream with a lower bitrate usually has a lower
  video quality.
- **Fragment count in media playlists** – A
  latency-sensitive player should only load the newest fragments in a media playlist. Most players start at
  the earliest fragment instead. By reducing the number of fragments in the playlist, you reduce the time
  separation between the previous and new fragments. With a smaller playlist size, it's possible for a
  fragment to be skipped during playback if there's a delay in adding new fragments to the playlist, or if
  there's a delay in the player getting an updated playlist. We recommend using 3–5 fragments, and to
  use a player that's configured to load only the newest fragments from a playlist.
- **Player buffer size** – Most video players have a
  configurable minimum buffer duration, usually with a 10-second default. For the lowest latency, you can set
  this value to 0 seconds. However, doing so means that the player rebuffers if there's any delay producing
  fragments because the player will have no buffer for absorbing the delay.
- **Player "catch up"** – Video players typically don't
  automatically catch playback up to the front of the video buffer if the buffer fills up, like when a delayed
  fragment causes a backlog of fragments to play. A custom player can avoid this by either dropping frames, or
  increasing the playback speed (for example, to 1.1x) to catch up to the front of the buffer. This causes
  playback to be choppy or increase in speed as the player catches up, and rebuffering might be more frequent
  as the buffer size is kept short.
