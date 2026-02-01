# UntagResource

Removes one or more tags from the specified pipes.

## Request Syntax

```
DELETE /tags/`resourceArn`?tagKeys=`tagKeys` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[resourceArn](#API_UntagResource_RequestSyntax "#API_UntagResource_RequestSyntax")**

The ARN of the pipe.

Length Constraints: Minimum length of 1. Maximum length of 1600.

Pattern: `arn:aws([a-z]|\-)*:([a-zA-Z0-9\-]+):([a-z]|\d|\-)*:([0-9]{12})?:(.+)`

Required: Yes

**[tagKeys](#API_UntagResource_RequestSyntax "#API_UntagResource_RequestSyntax")**

The list of tag keys to remove from the pipe.

Array Members: Minimum number of 0 items. Maximum number of 50 items.

Length Constraints: Minimum length of 1. Maximum length of 128.

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200

```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

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

- [AWS Command Line Interface V2](../../../goto/cli2/pipes-2015-10-07/UntagResource.md "../../../goto/cli2/pipes-2015-10-07/UntagResource.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/pipes-2015-10-07/UntagResource.md "../../../goto/DotNetSDKV4/pipes-2015-10-07/UntagResource.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/pipes-2015-10-07/UntagResource.md "../../../goto/SdkForCpp/pipes-2015-10-07/UntagResource.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/pipes-2015-10-07/UntagResource.md "../../../goto/SdkForGoV2/pipes-2015-10-07/UntagResource.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/pipes-2015-10-07/UntagResource.md "../../../goto/SdkForJavaV2/pipes-2015-10-07/UntagResource.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/pipes-2015-10-07/UntagResource.md "../../../goto/SdkForJavaScriptV3/pipes-2015-10-07/UntagResource.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/pipes-2015-10-07/UntagResource.md "../../../goto/SdkForKotlin/pipes-2015-10-07/UntagResource.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/pipes-2015-10-07/UntagResource.md "../../../goto/SdkForPHPV3/pipes-2015-10-07/UntagResource.md")
- [AWS SDK for Python](../../../goto/boto3/pipes-2015-10-07/UntagResource.md "../../../goto/boto3/pipes-2015-10-07/UntagResource.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/pipes-2015-10-07/UntagResource.md "../../../goto/SdkForRubyV3/pipes-2015-10-07/UntagResource.md")
