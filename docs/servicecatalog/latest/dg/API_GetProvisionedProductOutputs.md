# GetProvisionedProductOutputs

This API takes either a `ProvisonedProductId` or a `ProvisionedProductName`, along with a list of one or more output keys, and responds with the key/value pairs of those outputs.

## Request Syntax

```
{
   "AcceptLanguage": "`string`",
   "OutputKeys": [ "`string`" ],
   "PageSize": `number`,
   "PageToken": "`string`",
   "ProvisionedProductId": "`string`",
   "ProvisionedProductName": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[AcceptLanguage](#API_GetProvisionedProductOutputs_RequestSyntax "#API_GetProvisionedProductOutputs_RequestSyntax")**

The language code.

- `jp` - Japanese
- `zh` - Chinese

Type: String

Length Constraints: Maximum length of 100.

Required: No

**[OutputKeys](#API_GetProvisionedProductOutputs_RequestSyntax "#API_GetProvisionedProductOutputs_RequestSyntax")**

The list of keys that the API should return with their values. If none are provided, the API will return all outputs of the provisioned product.

Type: Array of strings

Array Members: Maximum number of 60 items.

Required: No

**[PageSize](#API_GetProvisionedProductOutputs_RequestSyntax "#API_GetProvisionedProductOutputs_RequestSyntax")**

The maximum number of items to return with this call.

Type: Integer

Valid Range: Minimum value of 0. Maximum value of 20.

Required: No

**[PageToken](#API_GetProvisionedProductOutputs_RequestSyntax "#API_GetProvisionedProductOutputs_RequestSyntax")**

The page token for the next set of results. To retrieve the first set of results, use null.

Type: String

Length Constraints: Maximum length of 2024.

Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`

Required: No

**[ProvisionedProductId](#API_GetProvisionedProductOutputs_RequestSyntax "#API_GetProvisionedProductOutputs_RequestSyntax")**

The identifier of the provisioned product that you want the outputs from.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: No

**[ProvisionedProductName](#API_GetProvisionedProductOutputs_RequestSyntax "#API_GetProvisionedProductOutputs_RequestSyntax")**

The name of the provisioned product that you want the outputs from.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `[a-zA-Z0-9][a-zA-Z0-9._-]*`

Required: No

## Response Syntax

```
{
   "NextPageToken": "***string***",
   "Outputs": [
      {
         "Description": "***string***",
         "OutputKey": "***string***",
         "OutputValue": "***string***"
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[NextPageToken](#API_GetProvisionedProductOutputs_ResponseSyntax "#API_GetProvisionedProductOutputs_ResponseSyntax")**

The page token to use to retrieve the next set of results. If there are no additional results, this value is null.

Type: String

Length Constraints: Maximum length of 2024.

Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`

**[Outputs](#API_GetProvisionedProductOutputs_ResponseSyntax "#API_GetProvisionedProductOutputs_ResponseSyntax")**

Information about the product created as the result of a request. For example, the output for a CloudFormation-backed product that creates an S3 bucket would include the S3 bucket URL.

Type: Array of [RecordOutput](API_RecordOutput.md "API_RecordOutput.md") objects

## Errors

**InvalidParametersException**

One or more parameters provided to the operation are not valid.

HTTP Status Code: 400

**ResourceNotFoundException**

The specified resource was not found.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/servicecatalog-2015-12-10/GetProvisionedProductOutputs.md "../../../goto/cli2/servicecatalog-2015-12-10/GetProvisionedProductOutputs.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/servicecatalog-2015-12-10/GetProvisionedProductOutputs.md "../../../goto/DotNetSDKV3/servicecatalog-2015-12-10/GetProvisionedProductOutputs.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/GetProvisionedProductOutputs.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/GetProvisionedProductOutputs.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/servicecatalog-2015-12-10/GetProvisionedProductOutputs.md "../../../goto/SdkForGoV2/servicecatalog-2015-12-10/GetProvisionedProductOutputs.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/GetProvisionedProductOutputs.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/GetProvisionedProductOutputs.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/GetProvisionedProductOutputs.md "../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/GetProvisionedProductOutputs.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/servicecatalog-2015-12-10/GetProvisionedProductOutputs.md "../../../goto/SdkForKotlin/servicecatalog-2015-12-10/GetProvisionedProductOutputs.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/GetProvisionedProductOutputs.md "../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/GetProvisionedProductOutputs.md")
- [AWS SDK for Python](../../../goto/boto3/servicecatalog-2015-12-10/GetProvisionedProductOutputs.md "../../../goto/boto3/servicecatalog-2015-12-10/GetProvisionedProductOutputs.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/GetProvisionedProductOutputs.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/GetProvisionedProductOutputs.md")
