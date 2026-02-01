# GetDataEndpoint

Gets an endpoint for a specified stream for either reading or writing. Use this
endpoint in your application to read from the specified stream (using the
`GetMedia` or `GetMediaForFragmentList` operations) or write
to it (using the `PutMedia` operation).

###### Note

The returned endpoint does not have the API name appended. The client needs to
add the API name to the returned endpoint.

In the request, specify the stream either by `StreamName` or
`StreamARN`.

## Request Syntax

```
POST /getDataEndpoint HTTP/1.1
Content-type: application/json

{
   "APIName": "`string`",
   "StreamARN": "`string`",
   "StreamName": "`string`"
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[APIName](#API_GetDataEndpoint_RequestSyntax "#API_GetDataEndpoint_RequestSyntax")**

The name of the API action for which to get an endpoint.

Type: String

Valid Values: `PUT_MEDIA | GET_MEDIA | LIST_FRAGMENTS | GET_MEDIA_FOR_FRAGMENT_LIST | GET_HLS_STREAMING_SESSION_URL | GET_DASH_STREAMING_SESSION_URL | GET_CLIP | GET_IMAGES`

Required: Yes

**[StreamARN](#API_GetDataEndpoint_RequestSyntax "#API_GetDataEndpoint_RequestSyntax")**

The Amazon Resource Name (ARN) of the stream that you want to get the endpoint for.
You must specify either this parameter or a `StreamName` in the request.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Pattern: `arn:[a-z\d-]+:kinesisvideo:[a-z0-9-]+:[0-9]+:[a-z]+/[a-zA-Z0-9_.-]+/[0-9]+`

Required: No

**[StreamName](#API_GetDataEndpoint_RequestSyntax "#API_GetDataEndpoint_RequestSyntax")**

The name of the stream that you want to get the endpoint for. You must specify
either this parameter or a `StreamARN` in the request.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `[a-zA-Z0-9_.-]+`

Required: No

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "DataEndpoint": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[DataEndpoint](#API_GetDataEndpoint_ResponseSyntax "#API_GetDataEndpoint_ResponseSyntax")**

The endpoint value. To read data from the stream or to write data to it, specify
this endpoint in your application.

Type: String

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**ClientLimitExceededException**

Kinesis Video Streams has throttled the request because you have exceeded the limit of
allowed client calls. Try making the call later.

HTTP Status Code: 400

**InvalidArgumentException**

The value for this input parameter is invalid.

HTTP Status Code: 400

**NotAuthorizedException**

The caller is not authorized to perform this operation.

HTTP Status Code: 401

**ResourceNotFoundException**

Amazon Kinesis Video Streams can't find the stream that you specified.

HTTP Status Code: 404

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/kinesisvideo-2017-09-30/GetDataEndpoint.md "../../../goto/cli2/kinesisvideo-2017-09-30/GetDataEndpoint.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/kinesisvideo-2017-09-30/GetDataEndpoint.md "../../../goto/DotNetSDKV4/kinesisvideo-2017-09-30/GetDataEndpoint.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisvideo-2017-09-30/GetDataEndpoint.md "../../../goto/SdkForCpp/kinesisvideo-2017-09-30/GetDataEndpoint.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/kinesisvideo-2017-09-30/GetDataEndpoint.md "../../../goto/SdkForGoV2/kinesisvideo-2017-09-30/GetDataEndpoint.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/GetDataEndpoint.md "../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/GetDataEndpoint.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/kinesisvideo-2017-09-30/GetDataEndpoint.md "../../../goto/SdkForJavaScriptV3/kinesisvideo-2017-09-30/GetDataEndpoint.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/kinesisvideo-2017-09-30/GetDataEndpoint.md "../../../goto/SdkForKotlin/kinesisvideo-2017-09-30/GetDataEndpoint.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/kinesisvideo-2017-09-30/GetDataEndpoint.md "../../../goto/SdkForPHPV3/kinesisvideo-2017-09-30/GetDataEndpoint.md")
- [AWS SDK for Python](../../../goto/boto3/kinesisvideo-2017-09-30/GetDataEndpoint.md "../../../goto/boto3/kinesisvideo-2017-09-30/GetDataEndpoint.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/GetDataEndpoint.md "../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/GetDataEndpoint.md")
