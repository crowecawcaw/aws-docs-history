# DescribeBatchInferenceJob

Gets the properties of a batch inference job including name, Amazon Resource Name (ARN),
status, input and output configurations, and the ARN of the solution version used to generate
the recommendations.

## Request Syntax

```
{
   "batchInferenceJobArn": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[batchInferenceJobArn](#API_DescribeBatchInferenceJob_RequestSyntax "#API_DescribeBatchInferenceJob_RequestSyntax")**

The ARN of the batch inference job to describe.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: Yes

## Response Syntax

```
{
   "batchInferenceJob": {
      "batchInferenceJobArn": "***string***",
      "batchInferenceJobConfig": {
         "itemExplorationConfig": {
            "***string***" : "***string***"
         }
      },
      "batchInferenceJobMode": "***string***",
      "creationDateTime": ***number***,
      "failureReason": "***string***",
      "filterArn": "***string***",
      "jobInput": {
         "s3DataSource": {
            "kmsKeyArn": "***string***",
            "path": "***string***"
         }
      },
      "jobName": "***string***",
      "jobOutput": {
         "s3DataDestination": {
            "kmsKeyArn": "***string***",
            "path": "***string***"
         }
      },
      "lastUpdatedDateTime": ***number***,
      "numResults": ***number***,
      "roleArn": "***string***",
      "solutionVersionArn": "***string***",
      "status": "***string***",
      "themeGenerationConfig": {
         "fieldsForThemeGeneration": {
            "itemName": "***string***"
         }
      }
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[batchInferenceJob](#API_DescribeBatchInferenceJob_ResponseSyntax "#API_DescribeBatchInferenceJob_ResponseSyntax")**

Information on the specified batch inference job.

Type: [BatchInferenceJob](API_BatchInferenceJob.md "API_BatchInferenceJob.md") object

## Errors

**InvalidInputException**

Provide a valid value for the field or parameter.

HTTP Status Code: 400

**ResourceNotFoundException**

Could not find the specified resource.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-2018-05-22/DescribeBatchInferenceJob.md "../../../goto/cli2/personalize-2018-05-22/DescribeBatchInferenceJob.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/personalize-2018-05-22/DescribeBatchInferenceJob.md "../../../goto/DotNetSDKV3/personalize-2018-05-22/DescribeBatchInferenceJob.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/DescribeBatchInferenceJob.md "../../../goto/SdkForCpp/personalize-2018-05-22/DescribeBatchInferenceJob.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-2018-05-22/DescribeBatchInferenceJob.md "../../../goto/SdkForGoV2/personalize-2018-05-22/DescribeBatchInferenceJob.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/DescribeBatchInferenceJob.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/DescribeBatchInferenceJob.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/DescribeBatchInferenceJob.md "../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/DescribeBatchInferenceJob.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-2018-05-22/DescribeBatchInferenceJob.md "../../../goto/SdkForKotlin/personalize-2018-05-22/DescribeBatchInferenceJob.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-2018-05-22/DescribeBatchInferenceJob.md "../../../goto/SdkForPHPV3/personalize-2018-05-22/DescribeBatchInferenceJob.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-2018-05-22/DescribeBatchInferenceJob.md "../../../goto/boto3/personalize-2018-05-22/DescribeBatchInferenceJob.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/DescribeBatchInferenceJob.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/DescribeBatchInferenceJob.md")
