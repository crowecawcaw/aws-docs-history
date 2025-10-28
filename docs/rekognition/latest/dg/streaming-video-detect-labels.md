# Detecting labels in streaming video events

You can use Amazon Rekognition Video to detect labels in streaming video. To do this, you create a
stream processor ([CreateStreamProcessor](../APIReference/API_CreateStreamProcessor.md "../APIReference/API_CreateStreamProcessor.md")) to start and
manage the analysis of streaming video.

Amazon Rekognition Video uses Amazon Kinesis Video Streams to receive and process a video stream. When you create the
stream processor, you choose what you want the stream processor to detect. You can choose
people, packages and pets, or people and packages. The analysis results are output to your
Amazon S3 bucket and in Amazon SNS notifications. Note that Amazon Rekognition Video detects the presence of a person
in the video, but does not detect whether the person is a specific individual. To search for
a face from a collection in a streaming video, see [Searching faces in a collection in streaming video](collections-streaming.md "collections-streaming.md").

To use Amazon Rekognition Video with streaming video, your application requires the following:

- A Kinesis video stream for sending streaming video to Amazon Rekognition Video. For more information, see the
  [Amazon Kinesis Video Streams
  Developer Guide](../../../kinesisvideostreams/latest/dg/what-is-kinesis-video.md "../../../kinesisvideostreams/latest/dg/what-is-kinesis-video.md").
- An Amazon Rekognition Video stream processor to manage the analysis of the streaming video. For
  more information, see [Overview of Amazon Rekognition Video stream processor operations](streaming-video.md#using-rekognition-video-stream-processor "streaming-video.md#using-rekognition-video-stream-processor").
- An Amazon S3 bucket. Amazon Rekognition Video publishes session output to the S3 bucket. The output
  includes the image frame where a person or object of interest was detected for first
  time. You must be the owner of the S3 bucket.
- An Amazon SNS topic that Amazon Rekognition Video publishes smart alerts and an end-of-session summary to.

###### Topics

- [Setting
  up your Amazon Rekognition Video and Amazon Kinesis resources](streaming-labels-setting-up.md "streaming-labels-setting-up.md")
- [Calling label detection operations for streaming video events](streaming-labels-detection.md "streaming-labels-detection.md")
