# UntagResource

Removes the specified tags that are attached to a resource. For more information, see [Removing tags from Amazon Personalize resources](tags-remove.md "tags-remove.md").

## Request Syntax

```
{
   "resourceArn": "`string`",
   "tagKeys": [ "`string`" ]
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[resourceArn](#API_UntagResource_RequestSyntax "#API_UntagResource_RequestSyntax")**

The resource's Amazon Resource Name (ARN).

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: Yes

**[tagKeys](#API_UntagResource_RequestSyntax "#API_UntagResource_RequestSyntax")**

The keys of the tags to be removed.

Type: Array of strings

Array Members: Minimum number of 0 items. Maximum number of 200 items.

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`

Required: Yes

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

**InvalidInputException**

Provide a valid value for the field or parameter.

HTTP Status Code: 400

**ResourceInUseException**

The specified resource is in use.

HTTP Status Code: 400

**ResourceNotFoundException**

Could not find the specified resource.

HTTP Status Code: 400

**TooManyTagKeysException**

The request contains more tag keys than can be associated with a resource (50 tag keys per resource).

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-2018-05-22/UntagResource.md "../../../goto/cli2/personalize-2018-05-22/UntagResource.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/personalize-2018-05-22/UntagResource.md "../../../goto/DotNetSDKV4/personalize-2018-05-22/UntagResource.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/UntagResource.md "../../../goto/SdkForCpp/personalize-2018-05-22/UntagResource.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-2018-05-22/UntagResource.md "../../../goto/SdkForGoV2/personalize-2018-05-22/UntagResource.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/UntagResource.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/UntagResource.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/UntagResource.md "../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/UntagResource.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-2018-05-22/UntagResource.md "../../../goto/SdkForKotlin/personalize-2018-05-22/UntagResource.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-2018-05-22/UntagResource.md "../../../goto/SdkForPHPV3/personalize-2018-05-22/UntagResource.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-2018-05-22/UntagResource.md "../../../goto/boto3/personalize-2018-05-22/UntagResource.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/UntagResource.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/UntagResource.md")
