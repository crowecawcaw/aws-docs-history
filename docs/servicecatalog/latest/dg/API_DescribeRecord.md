# DescribeRecord

Gets information about the specified request operation.

Use this operation after calling a request operation (for example, [ProvisionProduct](API_ProvisionProduct.md "API_ProvisionProduct.md"),
[TerminateProvisionedProduct](API_TerminateProvisionedProduct.md "API_TerminateProvisionedProduct.md"), or [UpdateProvisionedProduct](API_UpdateProvisionedProduct.md "API_UpdateProvisionedProduct.md")).

###### Note

If a provisioned product was transferred to a new owner using [UpdateProvisionedProductProperties](API_UpdateProvisionedProductProperties.md "API_UpdateProvisionedProductProperties.md"), the new owner
will be able to describe all past records for that product. The previous owner will no longer be able to describe the records, but will be able to
use [ListRecordHistory](API_ListRecordHistory.md "API_ListRecordHistory.md") to see the product's history from when he was the owner.

## Request Syntax

```
{
   "AcceptLanguage": "`string`",
   "Id": "`string`",
   "PageSize": `number`,
   "PageToken": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[AcceptLanguage](#API_DescribeRecord_RequestSyntax "#API_DescribeRecord_RequestSyntax")**

The language code.

- `jp` - Japanese
- `zh` - Chinese

Type: String

Length Constraints: Maximum length of 100.

Required: No

**[Id](#API_DescribeRecord_RequestSyntax "#API_DescribeRecord_RequestSyntax")**

The record identifier of the provisioned product. This identifier is returned by the
request operation.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: Yes

**[PageSize](#API_DescribeRecord_RequestSyntax "#API_DescribeRecord_RequestSyntax")**

The maximum number of items to return with this call.

Type: Integer

Valid Range: Minimum value of 0. Maximum value of 20.

Required: No

**[PageToken](#API_DescribeRecord_RequestSyntax "#API_DescribeRecord_RequestSyntax")**

The page token for the next set of results. To retrieve the first set of results, use null.

Type: String

Length Constraints: Maximum length of 2024.

Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`

Required: No

## Response Syntax

```
{
   "NextPageToken": "***string***",
   "RecordDetail": {
      "CreatedTime": ***number***,
      "LaunchRoleArn": "***string***",
      "PathId": "***string***",
      "ProductId": "***string***",
      "ProvisionedProductId": "***string***",
      "ProvisionedProductName": "***string***",
      "ProvisionedProductType": "***string***",
      "ProvisioningArtifactId": "***string***",
      "RecordErrors": [
         {
            "Code": "***string***",
            "Description": "***string***"
         }
      ],
      "RecordId": "***string***",
      "RecordTags": [
         {
            "Key": "***string***",
            "Value": "***string***"
         }
      ],
      "RecordType": "***string***",
      "Status": "***string***",
      "UpdatedTime": ***number***
   },
   "RecordOutputs": [
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

**[NextPageToken](#API_DescribeRecord_ResponseSyntax "#API_DescribeRecord_ResponseSyntax")**

The page token to use to retrieve the next set of results. If there are no additional results, this value is null.

Type: String

Length Constraints: Maximum length of 2024.

Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`

**[RecordDetail](#API_DescribeRecord_ResponseSyntax "#API_DescribeRecord_ResponseSyntax")**

Information about the product.

Type: [RecordDetail](API_RecordDetail.md "API_RecordDetail.md") object

**[RecordOutputs](#API_DescribeRecord_ResponseSyntax "#API_DescribeRecord_ResponseSyntax")**

Information about the product created as the result of a request. For example, the output for
a CloudFormation-backed product that creates an S3 bucket would include the S3 bucket URL.

Type: Array of [RecordOutput](API_RecordOutput.md "API_RecordOutput.md") objects

## Errors

**ResourceNotFoundException**

The specified resource was not found.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/servicecatalog-2015-12-10/DescribeRecord.md "../../../goto/cli2/servicecatalog-2015-12-10/DescribeRecord.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/servicecatalog-2015-12-10/DescribeRecord.md "../../../goto/DotNetSDKV3/servicecatalog-2015-12-10/DescribeRecord.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/DescribeRecord.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/DescribeRecord.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/servicecatalog-2015-12-10/DescribeRecord.md "../../../goto/SdkForGoV2/servicecatalog-2015-12-10/DescribeRecord.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/DescribeRecord.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/DescribeRecord.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/DescribeRecord.md "../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/DescribeRecord.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/servicecatalog-2015-12-10/DescribeRecord.md "../../../goto/SdkForKotlin/servicecatalog-2015-12-10/DescribeRecord.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/DescribeRecord.md "../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/DescribeRecord.md")
- [AWS SDK for Python](../../../goto/boto3/servicecatalog-2015-12-10/DescribeRecord.md "../../../goto/boto3/servicecatalog-2015-12-10/DescribeRecord.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/DescribeRecord.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/DescribeRecord.md")
