# Play back media from your Kinesis video stream

Open the [Kinesis Video Streams console](https://console.aws.amazon.com/kinesisvideo/home/ "https://console.aws.amazon.com/kinesisvideo/home/") and
select the **Stream name** for the stream you created.

The video stream that is sent from the Raspberry Pi appears in the console.

###### Note

It may take a few seconds before the video appears in the console.

Once the stream is playing, you can experiment with the following features in the
console:

- In the **Video preview** section, use the navigation controls to rewind or fast-forward the stream.
- In the **Stream info** section, review the codec, resolution,
  and bit rate of the stream. The resolution and bit rate values are set
  purposefully low on the Raspberry Pi to minimize bandwidth usage for this
  tutorial.

To view the Amazon CloudWatch metrics that are being created for your stream, select
**View stream metrics in CloudWatch**.

- Under **Data retention period**, notice that the video stream
  is retained for one day. You can edit this value and set it to **No data
  retention**, or set a value from one day to several years.
- Under **Server-side encryption**, notice that your data is
  being encrypted at rest using a key maintained by the AWS Key Management Service (AWS KMS).

## Playback issues

The following are some frequently encountered playback issues, and how to troubleshoot them.

### No media, but there are PERSISTED Acks in the logs

If you see PERSISTED Acks in the logs, Kinesis Video Streams has successfully ingested and stored the media that was uploaded by `kvssink`. Acks received from Kinesis Video Streams look like this. In the JSON, look at the value for the `"EventType"` key.

```
{"EventType":"RECEIVED","FragmentTimecode":252200,"FragmentNumber":"12345678901234567890123456724587702494771079511"}
{"EventType":"BUFFERING","FragmentTimecode":252467,"FragmentNumber":"12345678901234567890123456781729223736853277017"}
{"EventType":"RECEIVED","FragmentTimecode":252467,"FragmentNumber":"12345678901234567890123456781729223736853277017"}
{"EventType":"BUFFERING","FragmentTimecode":253000,"FragmentNumber":"12345678901234567890123456738870744847093249408"}
{"EventType":"PERSISTED","FragmentTimecode":252200,"FragmentNumber":"12345678901234567890123456724587702494771079511"}
{"EventType":"PERSISTED","FragmentTimecode":252467,"FragmentNumber":"1234567890123456789012345671729223736853277017"}
```

**Resolution:**

Wait a minute or two in the Kinesis Video Streams console, then use the double-right arrow. If no
media appears, verify that your stream is being sent to the correct region and
review the spelling of the stream name. You can find this information in the
logs.

See [Provide a region to
kvssink](examples-gstreamer-plugin-parameters.md#kvssink-region "examples-gstreamer-plugin-parameters.md#kvssink-region") for more information on how kvssink determines which region to use.

### The media takes a long time to load in the AWS Management Console

###### Important

The console playback experience is different than the HLS and DASH playback experience. Use
the sample media player [hosted web page](https://aws-samples.github.io/amazon-kinesis-video-streams-media-viewer/ "https://aws-samples.github.io/amazon-kinesis-video-streams-media-viewer/") in GitHub to test the playback, too. The source
code for the webpage can be found [here](https://github.com/aws-samples/amazon-kinesis-video-streams-media-viewer "https://github.com/aws-samples/amazon-kinesis-video-streams-media-viewer").

Media may load slowly in the console because of poor network bandwidth or a
constrained device, but can also be related to video encoding and fragmentation.

**Video Encoding Basics:**

- H.264 and H.265 encoders use key-frames (I-Frames) and
  predicted-frames (P-Frames) for efficient compression.
- Key-frames contain complete image data, while P-frames only contain
  changes from previous frames.
- The "key-frame interval" determines how often key-frames occur in the
  video stream.

**Fragmentation in Streaming:**

- In Kinesis Video Streams, new fragments start with each key-frame. For more information, see [Kinesis Video Streams data model](how-data.md "how-data.md").
- Fragment length (in seconds) can be estimated as: _key-frame interval_ ÷ _frame rate_

**Example:**

For a stream with a key-frame interval of 30 and a frame rate of 15 fps:

Fragment Length = 30 ÷ 15 = 2 seconds

Due to larger key-frame intervals, longer fragments increase latency in streaming
media.

**Resolution:**

To improve loading times, consider reducing the key-frame interval. This will
create shorter fragments, decreasing latency, but it'll also increase the size of
the video file.

For the `x264enc` GStreamer element, you can explicitly set the
key-frame interval via the `key-int-max` property:

```
x264enc bframes=0 key-int-max=60
```

When reviewing the log output, note how often the uploading client receives ACKs
from Kinesis Video Streams. The more keyframes that are generated, the more ACKs that are returned.

### The media is distorted or has artifacts

To troubleshoot this issue, make sure that all cables are tightly connected.
Review the output of `libcamera-hello` (or `raspistill` for
legacy Pi cameras) for camera modules.

In your GStreamer pipeline, replace `kvssink` with
`autovideosink` or `matroskamux` and
`filesink`. For example:

```
... x264enc tune=zerolatency speed-preset=ultrafast bframes=0 key-int-max=60 byte-stream=true ! h264parse ! matroskamux ! filesink location=output.mkv
```

Review the output file for `filesink` or the media player that opens
when using `autovideosink` to see if the artifacts are there as
well.

Also review the output of the following pipeline:

```
gst-launch-1.0 autovideosrc ! videoconvert ! autovideosink
```

Adding elements to your pipeline, like [dewarp](https://gstreamer.freedesktop.org/documentation/opencv/dewarp.html?gi-language=c "https://gstreamer.freedesktop.org/documentation/opencv/dewarp.html?gi-language=c"), can correct fish eye camera outputs.

Review the supported output codecs for your camera and adjust the elements as
needed.

For example, if your USB camera only supports JPEG output, then you will need
to use the `jpegparse` and `jpegdec` elements to transform
the media before encoding it into H.264 using `x264enc`. Search for
assistance on the GStreamer forums for other users with similar pipelines and/or
web cam setups.
