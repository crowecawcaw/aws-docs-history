# SendAlexaOfferToMaster

###### Note

Before using this API, you must call the `GetSignalingChannelEndpoint`
API to get an endpoint. You then specify the endpoint and region in your
`SendAlexaOfferToMaster` API request.

This API allows you to connect WebRTC-enabled devices with Alexa display devices. When
invoked, it sends the Alexa Session Description Protocol (SDP) offer to the master peer.
The offer is delivered as soon as the master is connected to the specified signaling
channel. This API returns the SDP answer from the connected master. If the master is not
connected to the signaling channel, redelivery requests are made until the message
expires.

## Request Syntax

```
POST /v1/send-alexa-offer-to-master HTTP/1.1
Content-type: application/json

{
   "ChannelARN": "`string`",
   "MessagePayload": "`string`",
   "SenderClientId": "`string`"
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[ChannelARN](#API_signaling_SendAlexaOfferToMaster_RequestSyntax "#API_signaling_SendAlexaOfferToMaster_RequestSyntax")**

The Amazon Resource Name (ARN) of the signaling channel by which Alexa and the master
peer communicate.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Pattern: `arn:[a-z\d-]+:kinesisvideo:[a-z0-9-]+:[0-9]+:[a-z]+/[a-zA-Z0-9_.-]+/[0-9]+`

Required: Yes

**[MessagePayload](#API_signaling_SendAlexaOfferToMaster_RequestSyntax "#API_signaling_SendAlexaOfferToMaster_RequestSyntax")**

The base64-encoded SDP offer content.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 10000.

Pattern: `[a-zA-Z0-9+/=]+`

Required: Yes

**[SenderClientId](#API_signaling_SendAlexaOfferToMaster_RequestSyntax "#API_signaling_SendAlexaOfferToMaster_RequestSyntax")**

The unique identifier for the sender client.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `[a-zA-Z0-9_.-]+`

Required: Yes

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "Answer": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[Answer](#API_signaling_SendAlexaOfferToMaster_ResponseSyntax "#API_signaling_SendAlexaOfferToMaster_ResponseSyntax")**

The base64-encoded SDP answer content.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 10000.

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**ClientLimitExceededException**

Your request was throttled because you have exceeded the limit of allowed client
calls. Try making the call later.

HTTP Status Code: 400

**InvalidArgumentException**

The value for this input parameter is invalid.

HTTP Status Code: 400

**NotAuthorizedException**

The caller is not authorized to perform this operation.

HTTP Status Code: 401

**ResourceNotFoundException**

The specified resource is not found.

HTTP Status Code: 404

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/kinesis-video-signaling-2019-12-04/SendAlexaOfferToMaster.md "../../../goto/cli2/kinesis-video-signaling-2019-12-04/SendAlexaOfferToMaster.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/kinesis-video-signaling-2019-12-04/SendAlexaOfferToMaster.md "../../../goto/DotNetSDKV3/kinesis-video-signaling-2019-12-04/SendAlexaOfferToMaster.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/kinesis-video-signaling-2019-12-04/SendAlexaOfferToMaster.md "../../../goto/SdkForCpp/kinesis-video-signaling-2019-12-04/SendAlexaOfferToMaster.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/kinesis-video-signaling-2019-12-04/SendAlexaOfferToMaster.md "../../../goto/SdkForGoV2/kinesis-video-signaling-2019-12-04/SendAlexaOfferToMaster.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesis-video-signaling-2019-12-04/SendAlexaOfferToMaster.md "../../../goto/SdkForJavaV2/kinesis-video-signaling-2019-12-04/SendAlexaOfferToMaster.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/kinesis-video-signaling-2019-12-04/SendAlexaOfferToMaster.md "../../../goto/SdkForJavaScriptV3/kinesis-video-signaling-2019-12-04/SendAlexaOfferToMaster.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/kinesis-video-signaling-2019-12-04/SendAlexaOfferToMaster.md "../../../goto/SdkForKotlin/kinesis-video-signaling-2019-12-04/SendAlexaOfferToMaster.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/kinesis-video-signaling-2019-12-04/SendAlexaOfferToMaster.md "../../../goto/SdkForPHPV3/kinesis-video-signaling-2019-12-04/SendAlexaOfferToMaster.md")
- [AWS SDK for Python](../../../goto/boto3/kinesis-video-signaling-2019-12-04/SendAlexaOfferToMaster.md "../../../goto/boto3/kinesis-video-signaling-2019-12-04/SendAlexaOfferToMaster.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesis-video-signaling-2019-12-04/SendAlexaOfferToMaster.md "../../../goto/SdkForRubyV3/kinesis-video-signaling-2019-12-04/SendAlexaOfferToMaster.md")
