End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# UntagResource

Removes tags from a bot, bot alias or bot channel.

## Request Syntax

```
DELETE /tags/`resourceArn`?tagKeys=`tagKeys` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[resourceArn](#API_UntagResource_RequestSyntax "#API_UntagResource_RequestSyntax")**

The Amazon Resource Name (ARN) of the resource to remove the tags
from.

Length Constraints: Minimum length of 1. Maximum length of 1011.

Required: Yes

**[tagKeys](#API_UntagResource_RequestSyntax "#API_UntagResource_RequestSyntax")**

A list of tag keys to remove from the resource. If a tag key does not
exist on the resource, it is ignored.

Array Members: Minimum number of 0 items. Maximum number of 200 items.

Length Constraints: Minimum length of 1. Maximum length of 128.

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 204

```

## Response Elements

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors

**BadRequestException**

The request is not well formed. For example, a value is invalid or
a required field is missing. Check the field values, and try
again.

HTTP Status Code: 400

**ConflictException**

There was a conflict processing the request. Try your request
again.

HTTP Status Code: 409

**InternalFailureException**

An internal Amazon Lex error occurred. Try your request again.

HTTP Status Code: 500

**LimitExceededException**

The request exceeded a limit. Try your request again.

HTTP Status Code: 429

**NotFoundException**

The resource specified in the request was not found. Check the
resource and try again.

HTTP Status Code: 404

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/lex-models-2017-04-19/UntagResource.md "../../../goto/cli2/lex-models-2017-04-19/UntagResource.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/lex-models-2017-04-19/UntagResource.md "../../../goto/DotNetSDKV3/lex-models-2017-04-19/UntagResource.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/lex-models-2017-04-19/UntagResource.md "../../../goto/SdkForCpp/lex-models-2017-04-19/UntagResource.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/lex-models-2017-04-19/UntagResource.md "../../../goto/SdkForGoV2/lex-models-2017-04-19/UntagResource.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lex-models-2017-04-19/UntagResource.md "../../../goto/SdkForJavaV2/lex-models-2017-04-19/UntagResource.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/lex-models-2017-04-19/UntagResource.md "../../../goto/SdkForJavaScriptV3/lex-models-2017-04-19/UntagResource.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/lex-models-2017-04-19/UntagResource.md "../../../goto/SdkForKotlin/lex-models-2017-04-19/UntagResource.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/lex-models-2017-04-19/UntagResource.md "../../../goto/SdkForPHPV3/lex-models-2017-04-19/UntagResource.md")
- [AWS SDK for Python](../../../goto/boto3/lex-models-2017-04-19/UntagResource.md "../../../goto/boto3/lex-models-2017-04-19/UntagResource.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lex-models-2017-04-19/UntagResource.md "../../../goto/SdkForRubyV3/lex-models-2017-04-19/UntagResource.md")
