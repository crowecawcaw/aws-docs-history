# GetSignalingChannelEndpoint

Provides an endpoint for the specified signaling channel to send and receive messages.
This API uses the `SingleMasterChannelEndpointConfiguration` input parameter,
which consists of the `Protocols` and `Role` properties.

`Protocols` is used to determine the communication mechanism. For example,
if you specify `WSS` as the protocol, this API produces a secure websocket
endpoint. If you specify `HTTPS` as the protocol, this API generates an HTTPS
endpoint. If you specify `WEBRTC` as the protocol, but the signaling channel isn't
configured for ingestion, you will receive the error
`InvalidArgumentException`.

`Role` determines the messaging permissions. A `MASTER` role
results in this API generating an endpoint that a client can use to communicate with any
of the viewers on the channel. A `VIEWER` role results in this API generating
an endpoint that a client can use to communicate only with a `MASTER`.

## Request Syntax

```
POST /getSignalingChannelEndpoint HTTP/1.1
Content-type: application/json

{
   "ChannelARN": "`string`",
   "SingleMasterChannelEndpointConfiguration": {
      "Protocols": [ "`string`" ],
      "Role": "`string`"
   }
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[ChannelARN](#API_GetSignalingChannelEndpoint_RequestSyntax "#API_GetSignalingChannelEndpoint_RequestSyntax")**

The Amazon Resource Name (ARN) of the signalling channel for which you want to get an
endpoint.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Pattern: `arn:[a-z\d-]+:kinesisvideo:[a-z0-9-]+:[0-9]+:[a-z]+/[a-zA-Z0-9_.-]+/[0-9]+`

Required: Yes

**[SingleMasterChannelEndpointConfiguration](#API_GetSignalingChannelEndpoint_RequestSyntax "#API_GetSignalingChannelEndpoint_RequestSyntax")**

A structure containing the endpoint configuration for the `SINGLE_MASTER`
channel type.

Type: [SingleMasterChannelEndpointConfiguration](API_SingleMasterChannelEndpointConfiguration.md "API_SingleMasterChannelEndpointConfiguration.md") object

Required: No

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "ResourceEndpointList": [
      {
         "Protocol": "***string***",
         "ResourceEndpoint": "***string***"
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[ResourceEndpointList](#API_GetSignalingChannelEndpoint_ResponseSyntax "#API_GetSignalingChannelEndpoint_ResponseSyntax")**

A list of endpoints for the specified signaling channel.

Type: Array of [ResourceEndpointListItem](API_ResourceEndpointListItem.md "API_ResourceEndpointListItem.md") objects

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**AccessDeniedException**

You do not have required permissions to perform this operation.

HTTP Status Code: 401

**ClientLimitExceededException**

Kinesis Video Streams has throttled the request because you have exceeded the limit of
allowed client calls. Try making the call later.

HTTP Status Code: 400

**InvalidArgumentException**

The value for this input parameter is invalid.

HTTP Status Code: 400

**ResourceInUseException**

When the input `StreamARN` or `ChannelARN`
in `CLOUD_STORAGE_MODE` is already mapped to a different
Kinesis Video Stream resource, or if the provided input `StreamARN`
or `ChannelARN` is not in Active status, try one of the following :

1. The `DescribeMediaStorageConfiguration` API to determine what the stream given channel is mapped to.
2. The `DescribeMappedResourceConfiguration` API to determine the channel that the given stream is mapped to.
3. The `DescribeStream` or `DescribeSignalingChannel` API to determine the status of the resource.

HTTP Status Code: 400

**ResourceNotFoundException**

Amazon Kinesis Video Streams can't find the stream that you specified.

HTTP Status Code: 404

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/kinesisvideo-2017-09-30/GetSignalingChannelEndpoint.md "../../../goto/cli2/kinesisvideo-2017-09-30/GetSignalingChannelEndpoint.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/kinesisvideo-2017-09-30/GetSignalingChannelEndpoint.md "../../../goto/DotNetSDKV3/kinesisvideo-2017-09-30/GetSignalingChannelEndpoint.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisvideo-2017-09-30/GetSignalingChannelEndpoint.md "../../../goto/SdkForCpp/kinesisvideo-2017-09-30/GetSignalingChannelEndpoint.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/kinesisvideo-2017-09-30/GetSignalingChannelEndpoint.md "../../../goto/SdkForGoV2/kinesisvideo-2017-09-30/GetSignalingChannelEndpoint.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/GetSignalingChannelEndpoint.md "../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/GetSignalingChannelEndpoint.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/kinesisvideo-2017-09-30/GetSignalingChannelEndpoint.md "../../../goto/SdkForJavaScriptV3/kinesisvideo-2017-09-30/GetSignalingChannelEndpoint.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/kinesisvideo-2017-09-30/GetSignalingChannelEndpoint.md "../../../goto/SdkForKotlin/kinesisvideo-2017-09-30/GetSignalingChannelEndpoint.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/kinesisvideo-2017-09-30/GetSignalingChannelEndpoint.md "../../../goto/SdkForPHPV3/kinesisvideo-2017-09-30/GetSignalingChannelEndpoint.md")
- [AWS SDK for Python](../../../goto/boto3/kinesisvideo-2017-09-30/GetSignalingChannelEndpoint.md "../../../goto/boto3/kinesisvideo-2017-09-30/GetSignalingChannelEndpoint.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/GetSignalingChannelEndpoint.md "../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/GetSignalingChannelEndpoint.md")
