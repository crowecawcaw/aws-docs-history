# ListTagsForResource

Displays the tags associated with a pipe.

## Request Syntax

```
GET /tags/`resourceArn` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[resourceArn](#API_ListTagsForResource_RequestSyntax "#API_ListTagsForResource_RequestSyntax")**

The ARN of the pipe for which you want to view tags.

Length Constraints: Minimum length of 1. Maximum length of 1600.

Pattern: `arn:aws([a-z]|\-)*:([a-zA-Z0-9\-]+):([a-z]|\d|\-)*:([0-9]{12})?:(.+)`

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "tags": {
      "***string***" : "***string***"
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[tags](#API_ListTagsForResource_ResponseSyntax "#API_ListTagsForResource_ResponseSyntax")**

The list of key-value pairs to associate with the pipe.

Type: String to string map

Map Entries: Maximum number of 50 items.

Key Length Constraints: Minimum length of 1. Maximum length of 128.

Value Length Constraints: Minimum length of 0. Maximum length of 256.

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**InternalException**

This exception occurs due to unexpected causes.

**retryAfterSeconds**

The number of seconds to wait before retrying the action that caused the
exception.

HTTP Status Code: 500

**NotFoundException**

An entity that you specified does not exist.

HTTP Status Code: 404

**ValidationException**

Indicates that an error has occurred while performing a validate operation.

**fieldList**

The list of fields for which validation failed and the corresponding failure
messages.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/pipes-2015-10-07/ListTagsForResource.md "../../../goto/cli2/pipes-2015-10-07/ListTagsForResource.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/pipes-2015-10-07/ListTagsForResource.md "../../../goto/DotNetSDKV4/pipes-2015-10-07/ListTagsForResource.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/pipes-2015-10-07/ListTagsForResource.md "../../../goto/SdkForCpp/pipes-2015-10-07/ListTagsForResource.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/pipes-2015-10-07/ListTagsForResource.md "../../../goto/SdkForGoV2/pipes-2015-10-07/ListTagsForResource.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/pipes-2015-10-07/ListTagsForResource.md "../../../goto/SdkForJavaV2/pipes-2015-10-07/ListTagsForResource.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/pipes-2015-10-07/ListTagsForResource.md "../../../goto/SdkForJavaScriptV3/pipes-2015-10-07/ListTagsForResource.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/pipes-2015-10-07/ListTagsForResource.md "../../../goto/SdkForKotlin/pipes-2015-10-07/ListTagsForResource.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/pipes-2015-10-07/ListTagsForResource.md "../../../goto/SdkForPHPV3/pipes-2015-10-07/ListTagsForResource.md")
- [AWS SDK for Python](../../../goto/boto3/pipes-2015-10-07/ListTagsForResource.md "../../../goto/boto3/pipes-2015-10-07/ListTagsForResource.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/pipes-2015-10-07/ListTagsForResource.md "../../../goto/SdkForRubyV3/pipes-2015-10-07/ListTagsForResource.md")
