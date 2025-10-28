# Working with streaming video events

You can use Amazon Rekognition Video to detect and recognize faces or detect objects in streaming video.
Amazon Rekognition Video uses Amazon Kinesis Video Streams to receive and process a video stream. You create a stream
processor with parameters that show what you want the stream processor to detect from the
video stream. Rekognition sends label detection results from streaming video events as Amazon SNS and
Amazon S3 notifications. Rekognition outputs face search results to a Kinesis data stream.

Face search stream processors use `FaceSearchSettings` to search for faces from a collection. For more information
about how to implement face search stream processors to analyze faces in streaming video,
see [Searching faces in a collection in streaming video](collections-streaming.md "collections-streaming.md").

Label detection stream processors use `ConnectedHomeSettings` to search for
people, packages, and pets in streaming video events. For more information about how to
implement label detection stream processors, see [Detecting labels in streaming video events](streaming-video-detect-labels.md "streaming-video-detect-labels.md").

## Overview of Amazon Rekognition Video stream processor operations

You start analyzing a streaming video by starting an Amazon Rekognition Video stream processor and
streaming video into Amazon Rekognition Video. An Amazon Rekognition Video stream processor allows you to start, stop,
and manage stream processors. You create a stream processor by calling [CreateStreamProcessor](../APIReference/API_CreateStreamProcessor.md "../APIReference/API_CreateStreamProcessor.md"). The request parameters for creating a face search stream processor include the Amazon
Resource Names (ARNs) for the Kinesis video stream, the Kinesis data stream, and the identifier for the collection
that's used to recognize faces in the streaming video. The request parameters for creating a security monitoring stream processor include the Amazon Resource Names (ARNs) for the Kinesis video stream and the Amazon SNS topic,
the types of objects you want to detect in the video stream, and information for an Amazon S3 bucket for the output results. You also include a name that
you specify for the stream processor.

You start processing a video by calling the [StartStreamProcessor](../APIReference/API_StartStreamProcessor.md "../APIReference/API_StartStreamProcessor.md")
operation. To get status information for a stream processor, call [DescribeStreamProcessor](../APIReference/API_DescribeStreamProcessor.md "../APIReference/API_DescribeStreamProcessor.md"). Other operations you can call are
[TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md") to tag a stream processor and
[DeleteStreamProcessor](../APIReference/API_DeleteStreamProcessor.md "../APIReference/API_DeleteStreamProcessor.md") to delete a stream processor. If you are using a face search stream processor, you can also use
[StopStreamProcessor](../APIReference/API_StopStreamProcessor.md "../APIReference/API_StopStreamProcessor.md") to stop a stream processor. To get a list of
stream processors in your account, call [ListStreamProcessors](../APIReference/API_ListStreamProcessors.md "../APIReference/API_ListStreamProcessors.md").

After the stream processor starts running, you stream the video into Amazon Rekognition Video through
the Kinesis video stream that you specified in `CreateStreamProcessor`.
You can use the Kinesis Video Streams SDK [PutMedia](../../../kinesisvideostreams/latest/dg/API_dataplane_PutMedia.md "../../../kinesisvideostreams/latest/dg/API_dataplane_PutMedia.md") operation to deliver video into the Kinesis video stream.
For an example, see [PutMedia
API Example](../../../kinesisvideostreams/latest/dg/examples-putmedia.md "../../../kinesisvideostreams/latest/dg/examples-putmedia.md").

For information about how your application can consume Amazon Rekognition Video analysis results from a face search stream processor, see
[Reading streaming video analysis
results](streaming-video-kinesis-output.md "streaming-video-kinesis-output.md").
