

# Actions, resources, and condition keys for Amazon Kinesis Video Streams
<a name="list_kinesis-video-streams"></a>

Amazon Kinesis Video Streams (service prefix: `kinesisvideo`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/what-is-kinesis-video.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_Reference.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/how-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/kinesisvideo/kinesisvideo.json) for this service.

**Topics**
+ [API operations defined by Amazon Kinesis Video Streams](#list_kinesis-video-streams-operations)
+ [Actions defined by Amazon Kinesis Video Streams](#list_kinesis-video-streams-actions-as-permissions)
+ [Resource types defined by Amazon Kinesis Video Streams](#list_kinesis-video-streams-resources-for-iam-policies)
+ [Condition keys for Amazon Kinesis Video Streams](#list_kinesis-video-streams-policy-keys)

## API operations defined by Amazon Kinesis Video Streams
<a name="list_kinesis-video-streams-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_kinesis-video-streams-actions-as-permissions).




- **   GetClip  **
  - **SDK client:** kinesis-video-archived-media
  - **IAM action:**  [kinesisvideo:GetClip](#list_kinesis-video-streams-action-GetClip) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDASHStreamingSessionURL  **
  - **SDK client:** kinesis-video-archived-media
  - **IAM action:**  [kinesisvideo:GetDASHStreamingSessionURL](#list_kinesis-video-streams-action-GetDASHStreamingSessionURL) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetHLSStreamingSessionURL  **
  - **SDK client:** kinesis-video-archived-media
  - **IAM action:**  [kinesisvideo:GetHLSStreamingSessionURL](#list_kinesis-video-streams-action-GetHLSStreamingSessionURL) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetImages  **
  - **SDK client:** kinesis-video-archived-media
  - **IAM action:**  [kinesisvideo:GetImages](#list_kinesis-video-streams-action-GetImages) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMediaForFragmentList  **
  - **SDK client:** kinesis-video-archived-media
  - **IAM action:**  [kinesisvideo:GetMediaForFragmentList](#list_kinesis-video-streams-action-GetMediaForFragmentList) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListFragments  **
  - **SDK client:** kinesis-video-archived-media
  - **IAM action:**  [kinesisvideo:ListFragments](#list_kinesis-video-streams-action-ListFragments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetMedia  **
  - **SDK client:** kinesis-video-media
  - **IAM action:**  [kinesisvideo:GetMedia](#list_kinesis-video-streams-action-GetMedia) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetIceServerConfig  **
  - **SDK client:** kinesis-video-signaling
  - **IAM action:**  [kinesisvideo:GetIceServerConfig](#list_kinesis-video-streams-action-GetIceServerConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   SendAlexaOfferToMaster  **
  - **SDK client:** kinesis-video-signaling
  - **IAM action:**  [kinesisvideo:SendAlexaOfferToMaster](#list_kinesis-video-streams-action-SendAlexaOfferToMaster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   JoinStorageSession  **
  - **SDK client:** kinesis-video-webrtc-storage
  - **IAM action:**  [kinesisvideo:JoinStorageSession](#list_kinesis-video-streams-action-JoinStorageSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   JoinStorageSessionAsViewer  **
  - **SDK client:** kinesis-video-webrtc-storage
  - **IAM action:**  [kinesisvideo:JoinStorageSessionAsViewer](#list_kinesis-video-streams-action-JoinStorageSessionAsViewer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateSignalingChannel  **
  - **SDK client:** kinesisvideo
  - **IAM action:**  [kinesisvideo:CreateSignalingChannel](#list_kinesis-video-streams-action-CreateSignalingChannel)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [kinesisvideo:TagResource](#list_kinesis-video-streams-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateStream  **
  - **SDK client:** kinesisvideo
  - **IAM action:**  [kinesisvideo:CreateStream](#list_kinesis-video-streams-action-CreateStream)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [kinesisvideo:TagStream](#list_kinesis-video-streams-action-TagStream)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteEdgeConfiguration  **
  - **SDK client:** kinesisvideo
  - **IAM action:**  [kinesisvideo:DeleteEdgeConfiguration](#list_kinesis-video-streams-action-DeleteEdgeConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSignalingChannel  **
  - **SDK client:** kinesisvideo
  - **IAM action:**  [kinesisvideo:DeleteSignalingChannel](#list_kinesis-video-streams-action-DeleteSignalingChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteStream  **
  - **SDK client:** kinesisvideo
  - **IAM action:**  [kinesisvideo:DeleteStream](#list_kinesis-video-streams-action-DeleteStream) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeEdgeConfiguration  **
  - **SDK client:** kinesisvideo
  - **IAM action:**  [kinesisvideo:DescribeEdgeConfiguration](#list_kinesis-video-streams-action-DescribeEdgeConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeImageGenerationConfiguration  **
  - **SDK client:** kinesisvideo
  - **IAM action:**  [kinesisvideo:DescribeImageGenerationConfiguration](#list_kinesis-video-streams-action-DescribeImageGenerationConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeMappedResourceConfiguration  **
  - **SDK client:** kinesisvideo
  - **IAM action:**  [kinesisvideo:DescribeMappedResourceConfiguration](#list_kinesis-video-streams-action-DescribeMappedResourceConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeMediaStorageConfiguration  **
  - **SDK client:** kinesisvideo
  - **IAM action:**  [kinesisvideo:DescribeMediaStorageConfiguration](#list_kinesis-video-streams-action-DescribeMediaStorageConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeNotificationConfiguration  **
  - **SDK client:** kinesisvideo
  - **IAM action:**  [kinesisvideo:DescribeNotificationConfiguration](#list_kinesis-video-streams-action-DescribeNotificationConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeSignalingChannel  **
  - **SDK client:** kinesisvideo
  - **IAM action:**  [kinesisvideo:DescribeSignalingChannel](#list_kinesis-video-streams-action-DescribeSignalingChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeStream  **
  - **SDK client:** kinesisvideo
  - **IAM action:**  [kinesisvideo:DescribeStream](#list_kinesis-video-streams-action-DescribeStream) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeStreamStorageConfiguration  **
  - **SDK client:** kinesisvideo
  - **IAM action:**  [kinesisvideo:DescribeStreamStorageConfiguration](#list_kinesis-video-streams-action-DescribeStreamStorageConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDataEndpoint  **
  - **SDK client:** kinesisvideo
  - **IAM action:**  [kinesisvideo:GetDataEndpoint](#list_kinesis-video-streams-action-GetDataEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSignalingChannelEndpoint  **
  - **SDK client:** kinesisvideo
  - **IAM action:**  [kinesisvideo:GetSignalingChannelEndpoint](#list_kinesis-video-streams-action-GetSignalingChannelEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListEdgeAgentConfigurations  **
  - **SDK client:** kinesisvideo
  - **IAM action:**  [kinesisvideo:ListEdgeAgentConfigurations](#list_kinesis-video-streams-action-ListEdgeAgentConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSignalingChannels  **
  - **SDK client:** kinesisvideo
  - **IAM action:**  [kinesisvideo:ListSignalingChannels](#list_kinesis-video-streams-action-ListSignalingChannels) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListStreams  **
  - **SDK client:** kinesisvideo
  - **IAM action:**  [kinesisvideo:ListStreams](#list_kinesis-video-streams-action-ListStreams) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **SDK client:** kinesisvideo
  - **IAM action:**  [kinesisvideo:ListTagsForResource](#list_kinesis-video-streams-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTagsForStream  **
  - **SDK client:** kinesisvideo
  - **IAM action:**  [kinesisvideo:ListTagsForStream](#list_kinesis-video-streams-action-ListTagsForStream) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   StartEdgeConfigurationUpdate  **
  - **SDK client:** kinesisvideo
  - **IAM action:**  [kinesisvideo:StartEdgeConfigurationUpdate](#list_kinesis-video-streams-action-StartEdgeConfigurationUpdate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **SDK client:** kinesisvideo
  - **IAM action:**  [kinesisvideo:TagResource](#list_kinesis-video-streams-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   TagStream  **
  - **SDK client:** kinesisvideo
  - **IAM action:**  [kinesisvideo:TagStream](#list_kinesis-video-streams-action-TagStream) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **SDK client:** kinesisvideo
  - **IAM action:**  [kinesisvideo:UntagResource](#list_kinesis-video-streams-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagStream  **
  - **SDK client:** kinesisvideo
  - **IAM action:**  [kinesisvideo:UntagStream](#list_kinesis-video-streams-action-UntagStream) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateDataRetention  **
  - **SDK client:** kinesisvideo
  - **IAM action:**  [kinesisvideo:UpdateDataRetention](#list_kinesis-video-streams-action-UpdateDataRetention) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateImageGenerationConfiguration  **
  - **SDK client:** kinesisvideo
  - **IAM action:**  [kinesisvideo:UpdateImageGenerationConfiguration](#list_kinesis-video-streams-action-UpdateImageGenerationConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateMediaStorageConfiguration  **
  - **SDK client:** kinesisvideo
  - **IAM action:**  [kinesisvideo:UpdateMediaStorageConfiguration](#list_kinesis-video-streams-action-UpdateMediaStorageConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateNotificationConfiguration  **
  - **SDK client:** kinesisvideo
  - **IAM action:**  [kinesisvideo:UpdateNotificationConfiguration](#list_kinesis-video-streams-action-UpdateNotificationConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSignalingChannel  **
  - **SDK client:** kinesisvideo
  - **IAM action:**  [kinesisvideo:UpdateSignalingChannel](#list_kinesis-video-streams-action-UpdateSignalingChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateStream  **
  - **SDK client:** kinesisvideo
  - **IAM action:**  [kinesisvideo:UpdateStream](#list_kinesis-video-streams-action-UpdateStream) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateStreamStorageConfiguration  **
  - **SDK client:** kinesisvideo
  - **IAM action:**  [kinesisvideo:UpdateStreamStorageConfiguration](#list_kinesis-video-streams-action-UpdateStreamStorageConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon Kinesis Video Streams
<a name="list_kinesis-video-streams-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [ConnectAsMaster](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_ConnectAsMaster.html)  **
  - **Description:** Grants permission to connect as a master to the signaling channel specified by the endpoint
  - **Resource types (\*required):** [channel\*](#list_kinesis-video-streams-resource-channel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-video-streams-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ConnectAsViewer](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_ConnectAsViewer.html)  **
  - **Description:** Grants permission to connect as a viewer to the signaling channel specified by the endpoint
  - **Resource types (\*required):** [channel\*](#list_kinesis-video-streams-resource-channel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-video-streams-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateSignalingChannel](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_CreateSignalingChannel.html)  **
  - **Description:** Grants permission to create a signaling channel
  - **Resource types (\*required):** [channel\*](#list_kinesis-video-streams-resource-channel)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_kinesis-video-streams-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_kinesis-video-streams-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kinesis-video-streams-aws_TagKeys)
  - **Access level:** Write

- **   [CreateStream](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_CreateStream.html)  **
  - **Description:** Grants permission to create a Kinesis video stream
  - **Resource types (\*required):** [stream\*](#list_kinesis-video-streams-resource-stream)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_kinesis-video-streams-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_kinesis-video-streams-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kinesis-video-streams-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteEdgeConfiguration](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_DeleteEdgeConfiguration.html)  **
  - **Description:** Grants permission to delete the edge configuration of your Kinesis Video Stream
  - **Resource types (\*required):** [stream\*](#list_kinesis-video-streams-resource-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-video-streams-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSignalingChannel](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_DeleteSignalingChannel.html)  **
  - **Description:** Grants permission to delete an existing signaling channel
  - **Resource types (\*required):** [channel\*](#list_kinesis-video-streams-resource-channel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-video-streams-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteStream](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_DeleteStream.html)  **
  - **Description:** Grants permission to delete an existing Kinesis video stream
  - **Resource types (\*required):** [stream\*](#list_kinesis-video-streams-resource-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-video-streams-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeEdgeConfiguration](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_DescribeEdgeConfiguration.html)  **
  - **Description:** Grants permission to describe the edge configuration of your Kinesis Video Stream
  - **Resource types (\*required):** [stream\*](#list_kinesis-video-streams-resource-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-video-streams-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeImageGenerationConfiguration](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_DescribeImageGenerationConfiguration.html)  **
  - **Description:** Grants permission to describe the image generation configuration of your Kinesis video stream
  - **Resource types (\*required):** [stream\*](#list_kinesis-video-streams-resource-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-video-streams-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeMappedResourceConfiguration](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_DescribeMappedResourceConfiguration.html)  **
  - **Description:** Grants permission to describe the resource mapped to the Kinesis video stream
  - **Resource types (\*required):** [stream\*](#list_kinesis-video-streams-resource-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-video-streams-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [DescribeMediaStorageConfiguration](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_DescribeMediaStorageConfiguration.html)  **
  - **Description:** Grants permission to describe the media storage configuration of a signaling channel
  - **Resource types (\*required):** [channel\*](#list_kinesis-video-streams-resource-channel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-video-streams-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeNotificationConfiguration](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_DescribeNotificationConfiguration.html)  **
  - **Description:** Grants permission to describe the notification configuration of your Kinesis video stream
  - **Resource types (\*required):** [stream\*](#list_kinesis-video-streams-resource-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-video-streams-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeSignalingChannel](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_DescribeSignalingChannel.html)  **
  - **Description:** Grants permission to describe the specified signaling channel
  - **Resource types (\*required):** [channel\*](#list_kinesis-video-streams-resource-channel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-video-streams-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [DescribeStream](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_DescribeStream.html)  **
  - **Description:** Grants permission to describe the specified Kinesis video stream
  - **Resource types (\*required):** [stream\*](#list_kinesis-video-streams-resource-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-video-streams-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [DescribeStreamStorageConfiguration](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_DescribeStreamStorageConfiguration.html)  **
  - **Description:** Grants permission to describe the stream storage configuration of your Kinesis Video Stream
  - **Resource types (\*required):** [stream\*](#list_kinesis-video-streams-resource-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-video-streams-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetClip](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_reader_GetClip.html)  **
  - **Description:** Grants permission to get a media clip from a video stream
  - **Resource types (\*required):** [stream\*](#list_kinesis-video-streams-resource-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-video-streams-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDASHStreamingSessionURL](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_reader_GetDASHStreamingSessionURL.html)  **
  - **Description:** Grants permission to create a URL for MPEG-DASH video streaming
  - **Resource types (\*required):** [stream\*](#list_kinesis-video-streams-resource-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-video-streams-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDataEndpoint](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_GetDataEndpoint.html)  **
  - **Description:** Grants permission to get an endpoint for a specified stream for either reading or writing media data to Kinesis Video Streams
  - **Resource types (\*required):** [stream\*](#list_kinesis-video-streams-resource-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-video-streams-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetHLSStreamingSessionURL](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_reader_GetHLSStreamingSessionURL.html)  **
  - **Description:** Grants permission to create a URL for HLS video streaming
  - **Resource types (\*required):** [stream\*](#list_kinesis-video-streams-resource-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-video-streams-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetIceServerConfig](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_signaling_GetIceServerConfig.html)  **
  - **Description:** Grants permission to get the ICE server configuration
  - **Resource types (\*required):** [channel\*](#list_kinesis-video-streams-resource-channel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-video-streams-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetImages](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_reader_GetImages.html)  **
  - **Description:** Grants permission to get generated images from your Kinesis video stream
  - **Resource types (\*required):** [stream\*](#list_kinesis-video-streams-resource-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-video-streams-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetMedia](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_dataplane_GetMedia.html)  **
  - **Description:** Grants permission to return media content of a Kinesis video stream
  - **Resource types (\*required):** [stream\*](#list_kinesis-video-streams-resource-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-video-streams-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetMediaForFragmentList](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_reader_GetMediaForFragmentList.html)  **
  - **Description:** Grants permission to read and return media data only from persisted storage
  - **Resource types (\*required):** [stream\*](#list_kinesis-video-streams-resource-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-video-streams-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSignalingChannelEndpoint](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_GetSignalingChannelEndpoint.html)  **
  - **Description:** Grants permission to get endpoints for a specified combination of protocol and role for a signaling channel
  - **Resource types (\*required):** [channel\*](#list_kinesis-video-streams-resource-channel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-video-streams-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [JoinStorageSession](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_webrtc_JoinStorageSession.html)  **
  - **Description:** Grants permission to join a storage session for a channel
  - **Resource types (\*required):** [channel\*](#list_kinesis-video-streams-resource-channel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-video-streams-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [JoinStorageSessionAsViewer](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_webrtc_JoinStorageSessionAsViewer.html)  **
  - **Description:** Grants permission to join a storage session for a channel as viewer
  - **Resource types (\*required):** [channel\*](#list_kinesis-video-streams-resource-channel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-video-streams-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ListEdgeAgentConfigurations](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_ListEdgeAgentConfigurations.html)  **
  - **Description:** Grants permission to list an edge agent configurations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListFragments](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_reader_ListFragments.html)  **
  - **Description:** Grants permission to list the fragments from archival storage based on the pagination token or selector type with range specified
  - **Resource types (\*required):** [stream\*](#list_kinesis-video-streams-resource-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-video-streams-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListSignalingChannels](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_ListSignalingChannels.html)  **
  - **Description:** Grants permission to list your signaling channels
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListStreams](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_ListStreams.html)  **
  - **Description:** Grants permission to list your Kinesis video streams
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to fetch the tags associated with your resource
  - **Resource types (\*required):** [channel](#list_kinesis-video-streams-resource-channel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-video-streams-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [stream](#list_kinesis-video-streams-resource-stream) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-video-streams-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListTagsForStream](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_ListTagsForStream.html)  **
  - **Description:** Grants permission to fetch the tags associated with Kinesis video stream
  - **Resource types (\*required):** [stream\*](#list_kinesis-video-streams-resource-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-video-streams-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PutMedia](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_dataplane_PutMedia.html)  **
  - **Description:** Grants permission to send media data to a Kinesis video stream
  - **Resource types (\*required):** [stream\*](#list_kinesis-video-streams-resource-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-video-streams-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SendAlexaOfferToMaster](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_signaling_SendAlexaOfferToMaster.html)  **
  - **Description:** Grants permission to send the Alexa SDP offer to the master
  - **Resource types (\*required):** [channel\*](#list_kinesis-video-streams-resource-channel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-video-streams-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartEdgeConfigurationUpdate](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_StartEdgeConfigurationUpdate.html)  **
  - **Description:** Grants permission to start edge configuration update of your Kinesis Video Stream
  - **Resource types (\*required):** [stream\*](#list_kinesis-video-streams-resource-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-video-streams-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_TagResource.html)  **
  - **Description:** Grants permission to attach set of tags to your resource
  - **Resource types (\*required):** [channel](#list_kinesis-video-streams-resource-channel) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_kinesis-video-streams-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_kinesis-video-streams-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kinesis-video-streams-aws_TagKeys)
  - **Resource types (\*required):** [stream](#list_kinesis-video-streams-resource-stream) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_kinesis-video-streams-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_kinesis-video-streams-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kinesis-video-streams-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [TagStream](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_TagStream.html)  **
  - **Description:** Grants permission to attach set of tags to your Kinesis video streams
  - **Resource types (\*required):** [stream\*](#list_kinesis-video-streams-resource-stream)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_kinesis-video-streams-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_kinesis-video-streams-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kinesis-video-streams-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_UntagResource.html)  **
  - **Description:** Grants permission to remove one or more tags from your resource
  - **Resource types (\*required):** [channel](#list_kinesis-video-streams-resource-channel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-video-streams-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kinesis-video-streams-aws_TagKeys)
  - **Resource types (\*required):** [stream](#list_kinesis-video-streams-resource-stream) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-video-streams-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kinesis-video-streams-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagStream](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_UntagStream.html)  **
  - **Description:** Grants permission to remove one or more tags from your Kinesis video streams
  - **Resource types (\*required):** [stream\*](#list_kinesis-video-streams-resource-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-video-streams-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kinesis-video-streams-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateDataRetention](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_UpdateDataRetention.html)  **
  - **Description:** Grants permission to update the data retention period of your Kinesis video stream
  - **Resource types (\*required):** [stream\*](#list_kinesis-video-streams-resource-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-video-streams-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateImageGenerationConfiguration](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_UpdateImageGenerationConfiguration.html)  **
  - **Description:** Grants permission to update the image generation configuration of your Kinesis video stream
  - **Resource types (\*required):** [stream\*](#list_kinesis-video-streams-resource-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-video-streams-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateMediaStorageConfiguration](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_UpdateMediaStorageConfiguration.html)  **
  - **Description:** Grants permission to create or update an mapping between a signaling channel and stream
  - **Resource types (\*required):** [channel\*](#list_kinesis-video-streams-resource-channel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-video-streams-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateNotificationConfiguration](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_UpdateNotificationConfiguration.html)  **
  - **Description:** Grants permission to update the notification configuration of your Kinesis video stream
  - **Resource types (\*required):** [stream\*](#list_kinesis-video-streams-resource-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-video-streams-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSignalingChannel](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_UpdateSignalingChannel.html)  **
  - **Description:** Grants permission to update an existing signaling channel
  - **Resource types (\*required):** [channel\*](#list_kinesis-video-streams-resource-channel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-video-streams-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateStream](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_UpdateStream.html)  **
  - **Description:** Grants permission to update an existing Kinesis video stream
  - **Resource types (\*required):** [stream\*](#list_kinesis-video-streams-resource-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-video-streams-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateStreamStorageConfiguration](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_UpdateStreamStorageConfiguration.html)  **
  - **Description:** Grants permission to update the stream storage configuration of your Kinesis Video Stream
  - **Resource types (\*required):** [stream\*](#list_kinesis-video-streams-resource-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesis-video-streams-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon Kinesis Video Streams
<a name="list_kinesis-video-streams-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [channel](https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/kvswebrtc-how-it-works.html)  | arn:${Partition}:kinesisvideo:${Region}:${Account}:channel/${ChannelName}/${CreationTime} | [aws:ResourceTag/${TagKey}](#list_kinesis-video-streams-aws_ResourceTag___TagKey_) | 
|  [stream](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/how-it-works.html)  | arn:${Partition}:kinesisvideo:${Region}:${Account}:stream/${StreamName}/${CreationTime} | [aws:ResourceTag/${TagKey}](#list_kinesis-video-streams-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon Kinesis Video Streams
<a name="list_kinesis-video-streams-policy-keys"></a>

Amazon Kinesis Video Streams defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters requests based on the allowed set of values for each of the tags | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters actions based on tag-value assoicated with the stream | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters requests based on the presence of mandatory tag keys in the request | ArrayOfString | 