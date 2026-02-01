# TagResource

Assigns one or more tags (key-value pairs) to the specified pipe. Tags can help you
organize and categorize your resources. You can also use them to scope user permissions by
granting a user permission to access or change only resources with certain tag
values.

Tags don't have any semantic meaning to AWS and are interpreted strictly
as strings of characters.

You can use the `TagResource` action with a pipe that already has tags. If
you specify a new tag key, this tag is appended to the list of tags associated with the
pipe. If you specify a tag key that is already associated with the pipe, the new tag value
that you specify replaces the previous value for that tag.

You can associate as many as 50 tags with a pipe.

## Request Syntax

```
POST /tags/`resourceArn` HTTP/1.1
Content-type: application/json

{
   "tags": {
      "`string`" : "`string`"
   }
}
```

## URI Request Parameters

The request uses the following URI parameters.

**[resourceArn](#API_TagResource_RequestSyntax "#API_TagResource_RequestSyntax")**

The ARN of the pipe.

Length Constraints: Minimum length of 1. Maximum length of 1600.

Pattern: `arn:aws([a-z]|\-)*:([a-zA-Z0-9\-]+):([a-z]|\d|\-)*:([0-9]{12})?:(.+)`

Required: Yes

## Request Body

The request accepts the following data in JSON format.

**[tags](#API_TagResource_RequestSyntax "#API_TagResource_RequestSyntax")**

The list of key-value pairs associated with the pipe.

Type: String to string map

Map Entries: Maximum number of 50 items.

Key Length Constraints: Minimum length of 1. Maximum length of 128.

Value Length Constraints: Minimum length of 0. Maximum length of 256.

Required: Yes

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

- [AWS Command Line Interface V2](../../../goto/cli2/pipes-2015-10-07/TagResource.md "../../../goto/cli2/pipes-2015-10-07/TagResource.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/pipes-2015-10-07/TagResource.md "../../../goto/DotNetSDKV4/pipes-2015-10-07/TagResource.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/pipes-2015-10-07/TagResource.md "../../../goto/SdkForCpp/pipes-2015-10-07/TagResource.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/pipes-2015-10-07/TagResource.md "../../../goto/SdkForGoV2/pipes-2015-10-07/TagResource.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/pipes-2015-10-07/TagResource.md "../../../goto/SdkForJavaV2/pipes-2015-10-07/TagResource.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/pipes-2015-10-07/TagResource.md "../../../goto/SdkForJavaScriptV3/pipes-2015-10-07/TagResource.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/pipes-2015-10-07/TagResource.md "../../../goto/SdkForKotlin/pipes-2015-10-07/TagResource.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/pipes-2015-10-07/TagResource.md "../../../goto/SdkForPHPV3/pipes-2015-10-07/TagResource.md")
- [AWS SDK for Python](../../../goto/boto3/pipes-2015-10-07/TagResource.md "../../../goto/boto3/pipes-2015-10-07/TagResource.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/pipes-2015-10-07/TagResource.md "../../../goto/SdkForRubyV3/pipes-2015-10-07/TagResource.md")
