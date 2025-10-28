# ListTagsForResource

Get a list of [tags](tagging-resources.md "tagging-resources.md") attached to a resource.

## Request Syntax

```
{
   "resourceArn": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[resourceArn](#API_ListTagsForResource_RequestSyntax "#API_ListTagsForResource_RequestSyntax")**

The resource's Amazon Resource Name (ARN).

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: Yes

## Response Syntax

```
{
   "tags": [
      {
         "tagKey": "***string***",
         "tagValue": "***string***"
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[tags](#API_ListTagsForResource_ResponseSyntax "#API_ListTagsForResource_ResponseSyntax")**

The resource's tags.

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

Array Members: Minimum number of 0 items. Maximum number of 200 items.

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

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-2018-05-22/ListTagsForResource.md "../../../goto/cli2/personalize-2018-05-22/ListTagsForResource.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/personalize-2018-05-22/ListTagsForResource.md "../../../goto/DotNetSDKV3/personalize-2018-05-22/ListTagsForResource.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/ListTagsForResource.md "../../../goto/SdkForCpp/personalize-2018-05-22/ListTagsForResource.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-2018-05-22/ListTagsForResource.md "../../../goto/SdkForGoV2/personalize-2018-05-22/ListTagsForResource.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/ListTagsForResource.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/ListTagsForResource.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/ListTagsForResource.md "../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/ListTagsForResource.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-2018-05-22/ListTagsForResource.md "../../../goto/SdkForKotlin/personalize-2018-05-22/ListTagsForResource.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-2018-05-22/ListTagsForResource.md "../../../goto/SdkForPHPV3/personalize-2018-05-22/ListTagsForResource.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-2018-05-22/ListTagsForResource.md "../../../goto/boto3/personalize-2018-05-22/ListTagsForResource.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/ListTagsForResource.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/ListTagsForResource.md")
