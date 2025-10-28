On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# ListModels

Generates a list of all models in the account, including model name and ARN, dataset,
and status.

## Request Syntax

```
{
   "DatasetNameBeginsWith": "`string`",
   "MaxResults": `number`,
   "ModelNameBeginsWith": "`string`",
   "NextToken": "`string`",
   "Status": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[DatasetNameBeginsWith](#API_ListModels_RequestSyntax "#API_ListModels_RequestSyntax")**

The beginning of the name of the dataset of the machine learning models to be listed.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 200.

Pattern: `^[0-9a-zA-Z_-]{1,200}$`

Required: No

**[MaxResults](#API_ListModels_RequestSyntax "#API_ListModels_RequestSyntax")**

Specifies the maximum number of machine learning models to list.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 500.

Required: No

**[ModelNameBeginsWith](#API_ListModels_RequestSyntax "#API_ListModels_RequestSyntax")**

The beginning of the name of the machine learning models being listed.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 200.

Pattern: `^[0-9a-zA-Z_-]{1,200}$`

Required: No

**[NextToken](#API_ListModels_RequestSyntax "#API_ListModels_RequestSyntax")**

An opaque pagination token indicating where to continue the listing of machine learning
models.

Type: String

Length Constraints: Maximum length of 8192.

Pattern: `\p{ASCII}{0,8192}`

Required: No

**[Status](#API_ListModels_RequestSyntax "#API_ListModels_RequestSyntax")**

The status of the machine learning model.

Type: String

Valid Values: `IN_PROGRESS | SUCCESS | FAILED | IMPORT_IN_PROGRESS`

Required: No

## Response Syntax

```
{
   "ModelSummaries": [
      {
         "ActiveModelVersion": ***number***,
         "ActiveModelVersionArn": "***string***",
         "CreatedAt": ***number***,
         "DatasetArn": "***string***",
         "DatasetName": "***string***",
         "LatestScheduledRetrainingModelVersion": ***number***,
         "LatestScheduledRetrainingStartTime": ***number***,
         "LatestScheduledRetrainingStatus": "***string***",
         "ModelArn": "***string***",
         "ModelDiagnosticsOutputConfiguration": {
            "KmsKeyId": "***string***",
            "S3OutputConfiguration": {
               "Bucket": "***string***",
               "Prefix": "***string***"
            }
         },
         "ModelName": "***string***",
         "ModelQuality": "***string***",
         "NextScheduledRetrainingStartDate": ***number***,
         "RetrainingSchedulerStatus": "***string***",
         "Status": "***string***"
      }
   ],
   "NextToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[ModelSummaries](#API_ListModels_ResponseSyntax "#API_ListModels_ResponseSyntax")**

Provides information on the specified model, including created time, model and dataset
ARNs, and status.

Type: Array of [ModelSummary](API_ModelSummary.md "API_ModelSummary.md") objects

**[NextToken](#API_ListModels_ResponseSyntax "#API_ListModels_ResponseSyntax")**

An opaque pagination token indicating where to continue the listing of machine learning
models.

Type: String

Length Constraints: Maximum length of 8192.

Pattern: `\p{ASCII}{0,8192}`

## Errors

**AccessDeniedException**

The request could not be completed because you do not have access to the resource.

HTTP Status Code: 400

**InternalServerException**

Processing of the request has failed because of an unknown error, exception or failure.

HTTP Status Code: 500

**ThrottlingException**

The request was denied due to request throttling.

HTTP Status Code: 400

**ValidationException**

The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related AWS
service that's being utilized.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/lookoutequipment-2020-12-15/ListModels.md "../../../goto/cli2/lookoutequipment-2020-12-15/ListModels.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/lookoutequipment-2020-12-15/ListModels.md "../../../goto/DotNetSDKV3/lookoutequipment-2020-12-15/ListModels.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/lookoutequipment-2020-12-15/ListModels.md "../../../goto/SdkForCpp/lookoutequipment-2020-12-15/ListModels.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/lookoutequipment-2020-12-15/ListModels.md "../../../goto/SdkForGoV2/lookoutequipment-2020-12-15/ListModels.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/ListModels.md "../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/ListModels.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/ListModels.md "../../../goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/ListModels.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/lookoutequipment-2020-12-15/ListModels.md "../../../goto/SdkForKotlin/lookoutequipment-2020-12-15/ListModels.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/lookoutequipment-2020-12-15/ListModels.md "../../../goto/SdkForPHPV3/lookoutequipment-2020-12-15/ListModels.md")
- [AWS SDK for Python](../../../goto/boto3/lookoutequipment-2020-12-15/ListModels.md "../../../goto/boto3/lookoutequipment-2020-12-15/ListModels.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/ListModels.md "../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/ListModels.md")
