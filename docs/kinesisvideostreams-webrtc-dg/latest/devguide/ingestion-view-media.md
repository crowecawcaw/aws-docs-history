

# Playback ingested media
<a name="ingestion-view-media"></a>

You can consume media data by either viewing it in the console, or by creating an application that reads media data from a stream using Hypertext Live Streaming (HLS).

## View media in the console
<a name="ingestion-view-media-console"></a>

In another browser tab, open the AWS Management Console. In the Kinesis Video Streams Dashboard, select [Video streams](https://us-west-2.console.aws.amazon.com/kinesisvideo/home?region=us-west-2#/streams).

Select the name of your stream in the list of streams. Use the search bar, if necessary.

Expand the **Media playback** section. If the video is still uploading, it will be shown. If the upload has finished, select the double-left arrow.

## Consume media data using HLS
<a name="ingestion-consume-hls"></a>

You can create a client application that consumes data from a Kinesis video stream using HLS. For information about creating an application that consumes media data using HLS, see [Kinesis Video Streams playback](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/how-playback.html).

## View media using the sample media viewer application
<a name="ingestion-view-application"></a>

Amazon Kinesis Video Streams created a sample web page implementation of a media viewer capable of playing back Kinesis Video Streams in HLS or DASH. You can view the source code on [GitHub](https://github.com/aws-samples/amazon-kinesis-video-streams-media-viewer) and try using the [hosted web page](https://aws-samples.github.io/amazon-kinesis-video-streams-media-viewer/).

1. Open the [Amazon Kinesis Video Streams Media Viewer](https://aws-samples.github.io/amazon-kinesis-video-streams-media-viewer/).

1. Complete the following fields:
   + **Region** - Select **us-west-2**.
   + **AWS Access Key**
   + **AWS Secret Key**
   + **Stream name**
   + **Playback Mode** - Select **Live**.

1. Select **Start Playback**.