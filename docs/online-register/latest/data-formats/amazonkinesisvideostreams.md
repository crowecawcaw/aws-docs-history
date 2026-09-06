

# Data retrieval APIs for Amazon Kinesis Video Streams
<a name="amazonkinesisvideostreams"></a>

Amazon Kinesis Video Streams provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="kinesisvideo-DescribeEdgeConfiguration"></a>[DescribeEdgeConfiguration](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_DescribeEdgeConfiguration.html) | Describe the edge configuration of your Kinesis Video Stream | Read | 
| <a name="kinesisvideo-DescribeImageGenerationConfiguration"></a>[DescribeImageGenerationConfiguration](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_DescribeImageGenerationConfiguration.html) | Describe the image generation configuration of your Kinesis video stream | Read | 
| <a name="kinesisvideo-DescribeMappedResourceConfiguration"></a>[DescribeMappedResourceConfiguration](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_DescribeMappedResourceConfiguration.html) | Describe the resource mapped to the Kinesis video stream | List | 
| <a name="kinesisvideo-DescribeMediaStorageConfiguration"></a>[DescribeMediaStorageConfiguration](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_DescribeMediaStorageConfiguration.html) | Describe the media storage configuration of a signaling channel | Read | 
| <a name="kinesisvideo-DescribeNotificationConfiguration"></a>[DescribeNotificationConfiguration](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_DescribeNotificationConfiguration.html) | Describe the notification configuration of your Kinesis video stream | Read | 
| <a name="kinesisvideo-DescribeSignalingChannel"></a>[DescribeSignalingChannel](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_DescribeSignalingChannel.html) | Describe the specified signaling channel | List | 
| <a name="kinesisvideo-DescribeStream"></a>[DescribeStream](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_DescribeStream.html) | Describe the specified Kinesis video stream | List | 
| <a name="kinesisvideo-DescribeStreamStorageConfiguration"></a>[DescribeStreamStorageConfiguration](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_DescribeStreamStorageConfiguration.html) | Describe the stream storage configuration of your Kinesis Video Stream | Read | 
| <a name="kinesisvideo-GetClip"></a>[GetClip](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_reader_GetClip.html) | Get a media clip from a video stream | Read | 
| <a name="kinesisvideo-GetDASHStreamingSessionURL"></a>[GetDASHStreamingSessionURL](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_reader_GetDASHStreamingSessionURL.html) | Create a URL for MPEG-DASH video streaming | Read | 
| <a name="kinesisvideo-GetDataEndpoint"></a>[GetDataEndpoint](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_GetDataEndpoint.html) | Get an endpoint for a specified stream for either reading or writing media data to Kinesis Video Streams | Read | 
| <a name="kinesisvideo-GetHLSStreamingSessionURL"></a>[GetHLSStreamingSessionURL](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_reader_GetHLSStreamingSessionURL.html) | Create a URL for HLS video streaming | Read | 
| <a name="kinesisvideo-GetIceServerConfig"></a>[GetIceServerConfig](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_signaling_GetIceServerConfig.html) | Get the ICE server configuration | Read | 
| <a name="kinesisvideo-GetImages"></a>[GetImages](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_reader_GetImages.html) | Get generated images from your Kinesis video stream | Read | 
| <a name="kinesisvideo-GetMedia"></a>[GetMedia](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_dataplane_GetMedia.html) | Return media content of a Kinesis video stream | Read | 
| <a name="kinesisvideo-GetMediaForFragmentList"></a>[GetMediaForFragmentList](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_reader_GetMediaForFragmentList.html) | Read and return media data only from persisted storage | Read | 
| <a name="kinesisvideo-GetSignalingChannelEndpoint"></a>[GetSignalingChannelEndpoint](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_GetSignalingChannelEndpoint.html) | Get endpoints for a specified combination of protocol and role for a signaling channel | Read | 
| <a name="kinesisvideo-ListEdgeAgentConfigurations"></a>[ListEdgeAgentConfigurations](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_ListEdgeAgentConfigurations.html) | List an edge agent configurations | List | 
| <a name="kinesisvideo-ListFragments"></a>[ListFragments](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_reader_ListFragments.html) | List the fragments from archival storage based on the pagination token or selector type with range specified | List | 
| <a name="kinesisvideo-ListSignalingChannels"></a>[ListSignalingChannels](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_ListSignalingChannels.html) | List your signaling channels | List | 
| <a name="kinesisvideo-ListStreams"></a>[ListStreams](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_ListStreams.html) | List your Kinesis video streams | List | 
| <a name="kinesisvideo-ListTagsForResource"></a>[ListTagsForResource](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_ListTagsForResource.html) | Fetch the tags associated with your resource | Read | 
| <a name="kinesisvideo-ListTagsForStream"></a>[ListTagsForStream](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_ListTagsForStream.html) | Fetch the tags associated with Kinesis video stream | Read | 