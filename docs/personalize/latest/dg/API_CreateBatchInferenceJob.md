# CreateBatchInferenceJob

Generates batch recommendations based on a list of items or users stored in Amazon S3
and exports the recommendations to an Amazon S3 bucket.

To generate batch recommendations, specify the ARN of a solution version and an Amazon S3 URI for the input and output data.
For user personalization, popular items, and personalized ranking solutions, the batch inference job generates a list of
recommended items for each user ID in the input file. For related items solutions, the job generates a list of recommended
items for each item ID in the input file.

For more information, see [Creating a batch inference job](getting-batch-recommendations.md "getting-batch-recommendations.md") .

If you use the Similar-Items recipe, Amazon Personalize can add descriptive themes to batch recommendations.
To generate themes, set the job's mode to
`THEME_GENERATION` and specify the name of the field that contains item names in the
input data.

For more information about generating themes, see [Batch recommendations with themes from Content Generator](themed-batch-recommendations.md "themed-batch-recommendations.md") .

You can't get batch recommendations with the Trending-Now or Next-Best-Action recipes.

## Request Syntax

```
{
   "batchInferenceJobConfig": {
      "itemExplorationConfig": {
         "`string`" : "`string`"
      },
      "rankingInfluence": {
         "`string`" : `number`
      }
   },
   "batchInferenceJobMode": "`string`",
   "filterArn": "`string`",
   "jobInput": {
      "s3DataSource": {
         "kmsKeyArn": "`string`",
         "path": "`string`"
      }
   },
   "jobName": "`string`",
   "jobOutput": {
      "s3DataDestination": {
         "kmsKeyArn": "`string`",
         "path": "`string`"
      }
   },
   "numResults": `number`,
   "roleArn": "`string`",
   "solutionVersionArn": "`string`",
   "tags": [
      {
         "tagKey": "`string`",
         "tagValue": "`string`"
      }
   ],
   "themeGenerationConfig": {
      "fieldsForThemeGeneration": {
         "itemName": "`string`"
      }
   }
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[batchInferenceJobConfig](#API_CreateBatchInferenceJob_RequestSyntax "#API_CreateBatchInferenceJob_RequestSyntax")**

The configuration details of a batch inference job.

Type: [BatchInferenceJobConfig](API_BatchInferenceJobConfig.md "API_BatchInferenceJobConfig.md") object

Required: No

**[batchInferenceJobMode](#API_CreateBatchInferenceJob_RequestSyntax "#API_CreateBatchInferenceJob_RequestSyntax")**

The mode of the batch inference job. To generate descriptive themes for groups of similar items, set the
job mode to `THEME_GENERATION`. If you don't want to generate themes, use the default `BATCH_INFERENCE`.

When you get batch recommendations with themes, you will incur additional costs. For more information, see [Amazon Personalize pricing](https://aws.amazon.com/personalize/pricing/ "https://aws.amazon.com/personalize/pricing/").

Type: String

Valid Values: `BATCH_INFERENCE | THEME_GENERATION`

Required: No

**[filterArn](#API_CreateBatchInferenceJob_RequestSyntax "#API_CreateBatchInferenceJob_RequestSyntax")**

The ARN of the filter to apply to the batch inference job. For more information on using
filters, see
[Filtering batch recommendations](filter-batch.md "filter-batch.md").

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: No

**[jobInput](#API_CreateBatchInferenceJob_RequestSyntax "#API_CreateBatchInferenceJob_RequestSyntax")**

The Amazon S3 path that leads to the input file to base your recommendations on. The input
material must be in JSON format.

Type: [BatchInferenceJobInput](API_BatchInferenceJobInput.md "API_BatchInferenceJobInput.md") object

Required: Yes

**[jobName](#API_CreateBatchInferenceJob_RequestSyntax "#API_CreateBatchInferenceJob_RequestSyntax")**

The name of the batch inference job to create.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z0-9][a-zA-Z0-9\-_]*`

Required: Yes

**[jobOutput](#API_CreateBatchInferenceJob_RequestSyntax "#API_CreateBatchInferenceJob_RequestSyntax")**

The path to the Amazon S3 bucket where the job's output will be stored.

Type: [BatchInferenceJobOutput](API_BatchInferenceJobOutput.md "API_BatchInferenceJobOutput.md") object

Required: Yes

**[numResults](#API_CreateBatchInferenceJob_RequestSyntax "#API_CreateBatchInferenceJob_RequestSyntax")**

The number of recommendations to retrieve.

Type: Integer

Required: No

**[roleArn](#API_CreateBatchInferenceJob_RequestSyntax "#API_CreateBatchInferenceJob_RequestSyntax")**

The ARN of the Amazon Identity and Access Management role that has permissions to read and write to your input and output
Amazon S3 buckets respectively.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`

Required: Yes

**[solutionVersionArn](#API_CreateBatchInferenceJob_RequestSyntax "#API_CreateBatchInferenceJob_RequestSyntax")**

The Amazon Resource Name (ARN) of the solution version that will be used to generate the
batch inference recommendations.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: Yes

**[tags](#API_CreateBatchInferenceJob_RequestSyntax "#API_CreateBatchInferenceJob_RequestSyntax")**

A list of [tags](tagging-resources.md "tagging-resources.md") to apply to the batch inference job.

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

Array Members: Minimum number of 0 items. Maximum number of 200 items.

Required: No

**[themeGenerationConfig](#API_CreateBatchInferenceJob_RequestSyntax "#API_CreateBatchInferenceJob_RequestSyntax")**

For theme generation jobs, specify the name of the column in your Items
dataset that contains each item's name.

Type: [ThemeGenerationConfig](API_ThemeGenerationConfig.md "API_ThemeGenerationConfig.md") object

Required: No

## Response Syntax

```
{
   "batchInferenceJobArn": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[batchInferenceJobArn](#API_CreateBatchInferenceJob_ResponseSyntax "#API_CreateBatchInferenceJob_ResponseSyntax")**

The ARN of the batch inference job.

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

**ResourceInUseException**

The specified resource is in use.

HTTP Status Code: 400

**ResourceNotFoundException**

Could not find the specified resource.

HTTP Status Code: 400

**TooManyTagsException**

You have exceeded the maximum number of tags you can apply to this resource.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-2018-05-22/CreateBatchInferenceJob.md "../../../goto/cli2/personalize-2018-05-22/CreateBatchInferenceJob.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/personalize-2018-05-22/CreateBatchInferenceJob.md "../../../goto/DotNetSDKV3/personalize-2018-05-22/CreateBatchInferenceJob.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/CreateBatchInferenceJob.md "../../../goto/SdkForCpp/personalize-2018-05-22/CreateBatchInferenceJob.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-2018-05-22/CreateBatchInferenceJob.md "../../../goto/SdkForGoV2/personalize-2018-05-22/CreateBatchInferenceJob.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/CreateBatchInferenceJob.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/CreateBatchInferenceJob.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/CreateBatchInferenceJob.md "../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/CreateBatchInferenceJob.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-2018-05-22/CreateBatchInferenceJob.md "../../../goto/SdkForKotlin/personalize-2018-05-22/CreateBatchInferenceJob.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-2018-05-22/CreateBatchInferenceJob.md "../../../goto/SdkForPHPV3/personalize-2018-05-22/CreateBatchInferenceJob.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-2018-05-22/CreateBatchInferenceJob.md "../../../goto/boto3/personalize-2018-05-22/CreateBatchInferenceJob.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/CreateBatchInferenceJob.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/CreateBatchInferenceJob.md")
