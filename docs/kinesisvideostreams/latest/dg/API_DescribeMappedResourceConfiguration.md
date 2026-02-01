# DescribeMappedResourceConfiguration

Returns the most current information about the stream. The `streamName`
or `streamARN` should be provided in the input.

## Request Syntax

```
POST /describeMappedResourceConfiguration HTTP/1.1
Content-type: application/json

{
   "MaxResults": `number`,
   "NextToken": "`string`",
   "StreamARN": "`string`",
   "StreamName": "`string`"
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[MaxResults](#API_DescribeMappedResourceConfiguration_RequestSyntax "#API_DescribeMappedResourceConfiguration_RequestSyntax")**

The maximum number of results to return in the response.

Type: Integer

Valid Range: Fixed value of 1.

Required: No

**[NextToken](#API_DescribeMappedResourceConfiguration_RequestSyntax "#API_DescribeMappedResourceConfiguration_RequestSyntax")**

The token to provide in your next request, to get another batch of results.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 1024.

Pattern: `[a-zA-Z0-9+/=]*`

Required: No

**[StreamARN](#API_DescribeMappedResourceConfiguration_RequestSyntax "#API_DescribeMappedResourceConfiguration_RequestSyntax")**

The Amazon Resource Name (ARN) of the stream.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Pattern: `arn:[a-z\d-]+:kinesisvideo:[a-z0-9-]+:[0-9]+:[a-z]+/[a-zA-Z0-9_.-]+/[0-9]+`

Required: No

**[StreamName](#API_DescribeMappedResourceConfiguration_RequestSyntax "#API_DescribeMappedResourceConfiguration_RequestSyntax")**

The name of the stream.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `[a-zA-Z0-9_.-]+`

Required: No

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "MappedResourceConfigurationList": [
      {
         "ARN": "***string***",
         "Type": "***string***"
      }
   ],
   "NextToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[MappedResourceConfigurationList](#API_DescribeMappedResourceConfiguration_ResponseSyntax "#API_DescribeMappedResourceConfiguration_ResponseSyntax")**

A structure that encapsulates, or contains, the media storage configuration properties.

Type: Array of [MappedResourceConfigurationListItem](API_MappedResourceConfigurationListItem.md "API_MappedResourceConfigurationListItem.md") objects

Array Members: Minimum number of 0 items. Maximum number of 1 item.

**[NextToken](#API_DescribeMappedResourceConfiguration_ResponseSyntax "#API_DescribeMappedResourceConfiguration_ResponseSyntax")**

The token that was used in the `NextToken`request to fetch the next set of results.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 1024.

Pattern: `[a-zA-Z0-9+/=]*`

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

**ResourceNotFoundException**

Amazon Kinesis Video Streams can't find the stream that you specified.

HTTP Status Code: 404

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/kinesisvideo-2017-09-30/DescribeMappedResourceConfiguration.md "../../../goto/cli2/kinesisvideo-2017-09-30/DescribeMappedResourceConfiguration.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/kinesisvideo-2017-09-30/DescribeMappedResourceConfiguration.md "../../../goto/DotNetSDKV4/kinesisvideo-2017-09-30/DescribeMappedResourceConfiguration.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisvideo-2017-09-30/DescribeMappedResourceConfiguration.md "../../../goto/SdkForCpp/kinesisvideo-2017-09-30/DescribeMappedResourceConfiguration.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/kinesisvideo-2017-09-30/DescribeMappedResourceConfiguration.md "../../../goto/SdkForGoV2/kinesisvideo-2017-09-30/DescribeMappedResourceConfiguration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/DescribeMappedResourceConfiguration.md "../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/DescribeMappedResourceConfiguration.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/kinesisvideo-2017-09-30/DescribeMappedResourceConfiguration.md "../../../goto/SdkForJavaScriptV3/kinesisvideo-2017-09-30/DescribeMappedResourceConfiguration.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/kinesisvideo-2017-09-30/DescribeMappedResourceConfiguration.md "../../../goto/SdkForKotlin/kinesisvideo-2017-09-30/DescribeMappedResourceConfiguration.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/kinesisvideo-2017-09-30/DescribeMappedResourceConfiguration.md "../../../goto/SdkForPHPV3/kinesisvideo-2017-09-30/DescribeMappedResourceConfiguration.md")
- [AWS SDK for Python](../../../goto/boto3/kinesisvideo-2017-09-30/DescribeMappedResourceConfiguration.md "../../../goto/boto3/kinesisvideo-2017-09-30/DescribeMappedResourceConfiguration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/DescribeMappedResourceConfiguration.md "../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/DescribeMappedResourceConfiguration.md")
