# ListResourcesForTagOption

Lists the resources associated with the specified TagOption.

## Request Syntax

```
{
   "PageSize": `number`,
   "PageToken": "`string`",
   "ResourceType": "`string`",
   "TagOptionId": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[PageSize](#API_ListResourcesForTagOption_RequestSyntax "#API_ListResourcesForTagOption_RequestSyntax")**

The maximum number of items to return with this call.

Type: Integer

Valid Range: Minimum value of 0. Maximum value of 20.

Required: No

**[PageToken](#API_ListResourcesForTagOption_RequestSyntax "#API_ListResourcesForTagOption_RequestSyntax")**

The page token for the next set of results. To retrieve the first set of results, use null.

Type: String

Length Constraints: Maximum length of 2024.

Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`

Required: No

**[ResourceType](#API_ListResourcesForTagOption_RequestSyntax "#API_ListResourcesForTagOption_RequestSyntax")**

The resource type.

- `Portfolio`
- `Product`

Type: String

Required: No

**[TagOptionId](#API_ListResourcesForTagOption_RequestSyntax "#API_ListResourcesForTagOption_RequestSyntax")**

The TagOption identifier.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Required: Yes

## Response Syntax

```
{
   "PageToken": "***string***",
   "ResourceDetails": [
      {
         "ARN": "***string***",
         "CreatedTime": ***number***,
         "Description": "***string***",
         "Id": "***string***",
         "Name": "***string***"
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[PageToken](#API_ListResourcesForTagOption_ResponseSyntax "#API_ListResourcesForTagOption_ResponseSyntax")**

The page token for the next set of results. To retrieve the first set of results, use null.

Type: String

Length Constraints: Maximum length of 2024.

Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`

**[ResourceDetails](#API_ListResourcesForTagOption_ResponseSyntax "#API_ListResourcesForTagOption_ResponseSyntax")**

Information about the resources.

Type: Array of [ResourceDetail](API_ResourceDetail.md "API_ResourceDetail.md") objects

## Errors

**InvalidParametersException**

One or more parameters provided to the operation are not valid.

HTTP Status Code: 400

**ResourceNotFoundException**

The specified resource was not found.

HTTP Status Code: 400

**TagOptionNotMigratedException**

An operation requiring TagOptions failed because the TagOptions migration process has
not been performed for this account. Use the AWS Management Console to perform the migration
process before retrying the operation.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/servicecatalog-2015-12-10/ListResourcesForTagOption.md "../../../goto/cli2/servicecatalog-2015-12-10/ListResourcesForTagOption.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/ListResourcesForTagOption.md "../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/ListResourcesForTagOption.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/ListResourcesForTagOption.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/ListResourcesForTagOption.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/servicecatalog-2015-12-10/ListResourcesForTagOption.md "../../../goto/SdkForGoV2/servicecatalog-2015-12-10/ListResourcesForTagOption.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/ListResourcesForTagOption.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/ListResourcesForTagOption.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/ListResourcesForTagOption.md "../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/ListResourcesForTagOption.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/servicecatalog-2015-12-10/ListResourcesForTagOption.md "../../../goto/SdkForKotlin/servicecatalog-2015-12-10/ListResourcesForTagOption.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/ListResourcesForTagOption.md "../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/ListResourcesForTagOption.md")
- [AWS SDK for Python](../../../goto/boto3/servicecatalog-2015-12-10/ListResourcesForTagOption.md "../../../goto/boto3/servicecatalog-2015-12-10/ListResourcesForTagOption.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/ListResourcesForTagOption.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/ListResourcesForTagOption.md")
