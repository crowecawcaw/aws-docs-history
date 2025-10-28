# UpdateDataset

Update a dataset to replace its schema with a new or existing one. For more information, see [Replacing a dataset's schema](updating-dataset-schema.md "updating-dataset-schema.md").

## Request Syntax

```
{
   "datasetArn": "`string`",
   "schemaArn": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[datasetArn](#API_UpdateDataset_RequestSyntax "#API_UpdateDataset_RequestSyntax")**

The Amazon Resource Name (ARN) of the dataset that you want to update.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: Yes

**[schemaArn](#API_UpdateDataset_RequestSyntax "#API_UpdateDataset_RequestSyntax")**

The Amazon Resource Name (ARN) of the new schema you want use.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: Yes

## Response Syntax

```
{
   "datasetArn": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[datasetArn](#API_UpdateDataset_ResponseSyntax "#API_UpdateDataset_ResponseSyntax")**

The Amazon Resource Name (ARN) of the dataset you updated.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

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

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-2018-05-22/UpdateDataset.md "../../../goto/cli2/personalize-2018-05-22/UpdateDataset.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/personalize-2018-05-22/UpdateDataset.md "../../../goto/DotNetSDKV3/personalize-2018-05-22/UpdateDataset.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/UpdateDataset.md "../../../goto/SdkForCpp/personalize-2018-05-22/UpdateDataset.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-2018-05-22/UpdateDataset.md "../../../goto/SdkForGoV2/personalize-2018-05-22/UpdateDataset.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/UpdateDataset.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/UpdateDataset.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/UpdateDataset.md "../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/UpdateDataset.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-2018-05-22/UpdateDataset.md "../../../goto/SdkForKotlin/personalize-2018-05-22/UpdateDataset.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-2018-05-22/UpdateDataset.md "../../../goto/SdkForPHPV3/personalize-2018-05-22/UpdateDataset.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-2018-05-22/UpdateDataset.md "../../../goto/boto3/personalize-2018-05-22/UpdateDataset.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/UpdateDataset.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/UpdateDataset.md")
