# CreateFilter

Creates a recommendation filter. For more information, see [Filtering recommendations and user segments](filter.md "filter.md").

## Request Syntax

```
{
   "datasetGroupArn": "`string`",
   "filterExpression": "`string`",
   "name": "`string`",
   "tags": [
      {
         "tagKey": "`string`",
         "tagValue": "`string`"
      }
   ]
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[datasetGroupArn](#API_CreateFilter_RequestSyntax "#API_CreateFilter_RequestSyntax")**

The ARN of the dataset group that the filter will belong to.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: Yes

**[filterExpression](#API_CreateFilter_RequestSyntax "#API_CreateFilter_RequestSyntax")**

The filter expression defines which items are included or excluded from recommendations. Filter expression must follow specific format rules.
For information about filter expression structure and syntax, see
[Filter expressions](filter-expressions.md "filter-expressions.md").

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2500.

Required: Yes

**[name](#API_CreateFilter_RequestSyntax "#API_CreateFilter_RequestSyntax")**

The name of the filter to create.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z0-9][a-zA-Z0-9\-_]*`

Required: Yes

**[tags](#API_CreateFilter_RequestSyntax "#API_CreateFilter_RequestSyntax")**

A list of [tags](tagging-resources.md "tagging-resources.md") to apply to the filter.

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

Array Members: Minimum number of 0 items. Maximum number of 200 items.

Required: No

## Response Syntax

```
{
   "filterArn": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[filterArn](#API_CreateFilter_ResponseSyntax "#API_CreateFilter_ResponseSyntax")**

The ARN of the new filter.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

## Errors

**InvalidInputException**

Provide a valid value for the field or parameter.

HTTP Status Code: 400

**LimitExceededException**

The limit on the number of requests per second has been exceeded.

HTTP Status Code: 400

**ResourceAlreadyExistsException**

The specified resource already exists.

HTTP Status Code: 400

**ResourceNotFoundException**

Could not find the specified resource.

HTTP Status Code: 400

**TooManyTagsException**

You have exceeded the maximum number of tags you can apply to this resource.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-2018-05-22/CreateFilter.md "../../../goto/cli2/personalize-2018-05-22/CreateFilter.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/personalize-2018-05-22/CreateFilter.md "../../../goto/DotNetSDKV3/personalize-2018-05-22/CreateFilter.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/CreateFilter.md "../../../goto/SdkForCpp/personalize-2018-05-22/CreateFilter.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-2018-05-22/CreateFilter.md "../../../goto/SdkForGoV2/personalize-2018-05-22/CreateFilter.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/CreateFilter.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/CreateFilter.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/CreateFilter.md "../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/CreateFilter.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-2018-05-22/CreateFilter.md "../../../goto/SdkForKotlin/personalize-2018-05-22/CreateFilter.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-2018-05-22/CreateFilter.md "../../../goto/SdkForPHPV3/personalize-2018-05-22/CreateFilter.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-2018-05-22/CreateFilter.md "../../../goto/boto3/personalize-2018-05-22/CreateFilter.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/CreateFilter.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/CreateFilter.md")
