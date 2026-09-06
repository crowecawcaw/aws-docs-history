

# Use Amazon Kinesis Video Streams with WebRTC to ingest and store media
<a name="webrtc-ingestion"></a>

Amazon Kinesis Video Streams offers capabilities to stream video and audio in real-time via WebRTC to the cloud for storage, playback, and analytical processing. Customers can use our enhanced WebRTC SDK and cloud APIs to enable real-time streaming, as well as media ingestion to the cloud.

To get started, you can install Amazon Kinesis Video Streams with [WebRTC SDK](https://github.com/awslabs/amazon-kinesis-video-streams-webrtc-sdk-c/tree/Release-WebRTC-Streams-Ingestion-Public-Preview) on any security camera or AWS IoT device with a video sensor and use our [APIs](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_Operations_Amazon_Kinesis_Video_Streams.html) to enable media streaming with sub 1-second latency, as well as ingestion and storage in the cloud. Once ingested, you can access your data through our easy-to-use APIs. Amazon Kinesis Video Streams enables you to playback video for live and on-demand viewing, as well as quickly build applications that take advantage of computer vision and video analytics through integration with Amazon Rekognition Video and SageMaker AI.

**Topics**
+ [API operations](#ingestion-apis)
+ [What is Amazon Kinesis Video Streams with WebRTC ingestion and storage?](getting-started-ingestion.md)
+ [Create a signaling channel](ingestion-create-channel.md)
+ [Create a video stream](ingestion-create-stream.md)
+ [Grant permission](ingestion-grant-permission.md)
+ [Configure destination](configure-ingestion.md)
+ [Ingest media](ingest-media.md)
+ [Playback ingested media](ingestion-view-media.md)
+ [Connect to the storage session](ingestion-initiate.md)
+ [Troubleshoot issues connecting with the storage session](troubleshoot-establish-storage.md)

## API operations
<a name="ingestion-apis"></a>

Use the following API operations to configure Amazon Kinesis Video Streams WebRTC ingestion:
+ [DescribeMappedResourceConfiguration](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_DescribeMappedResourceConfiguration.html)
+ [DescribeMediaStorageConfiguration](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_DescribeMediaStorageConfiguration.html)
+ [JoinStorageSession](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_webrtc_JoinStorageSession.html)
+ [JoinStorageSessionAsViewer](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_webrtc_JoinStorageSessionAsViewer.html)
+ [UpdateMediaStorageConfiguration](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_UpdateMediaStorageConfiguration.html)