# DescribeSchema

Describes a schema. For more information on schemas, see
[CreateSchema](API_CreateSchema.md "API_CreateSchema.md").

## Request Syntax

```
{
   "schemaArn": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[schemaArn](#API_DescribeSchema_RequestSyntax "#API_DescribeSchema_RequestSyntax")**

The Amazon Resource Name (ARN) of the schema to retrieve.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: Yes

## Response Syntax

```
{
   "schema": {
      "creationDateTime": ***number***,
      "domain": "***string***",
      "lastUpdatedDateTime": ***number***,
      "name": "***string***",
      "schema": "***string***",
      "schemaArn": "***string***"
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[schema](#API_DescribeSchema_ResponseSyntax "#API_DescribeSchema_ResponseSyntax")**

The requested schema.

Type: [DatasetSchema](API_DatasetSchema.md "API_DatasetSchema.md") object

## Errors

**InvalidInputException**

Provide a valid value for the field or parameter.

HTTP Status Code: 400

**ResourceNotFoundException**

Could not find the specified resource.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-2018-05-22/DescribeSchema.md "../../../goto/cli2/personalize-2018-05-22/DescribeSchema.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/personalize-2018-05-22/DescribeSchema.md "../../../goto/DotNetSDKV3/personalize-2018-05-22/DescribeSchema.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/DescribeSchema.md "../../../goto/SdkForCpp/personalize-2018-05-22/DescribeSchema.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-2018-05-22/DescribeSchema.md "../../../goto/SdkForGoV2/personalize-2018-05-22/DescribeSchema.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/DescribeSchema.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/DescribeSchema.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/DescribeSchema.md "../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/DescribeSchema.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-2018-05-22/DescribeSchema.md "../../../goto/SdkForKotlin/personalize-2018-05-22/DescribeSchema.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-2018-05-22/DescribeSchema.md "../../../goto/SdkForPHPV3/personalize-2018-05-22/DescribeSchema.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-2018-05-22/DescribeSchema.md "../../../goto/boto3/personalize-2018-05-22/DescribeSchema.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/DescribeSchema.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/DescribeSchema.md")
