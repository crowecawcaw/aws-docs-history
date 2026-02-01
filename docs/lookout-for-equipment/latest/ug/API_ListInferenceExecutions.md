On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# ListInferenceExecutions

Lists all inference executions that have been performed by the specified inference
scheduler.

## Request Syntax

```
{
   "DataEndTimeBefore": `number`,
   "DataStartTimeAfter": `number`,
   "InferenceSchedulerName": "`string`",
   "MaxResults": `number`,
   "NextToken": "`string`",
   "Status": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[DataEndTimeBefore](#API_ListInferenceExecutions_RequestSyntax "#API_ListInferenceExecutions_RequestSyntax")**

The time reference in the inferenced dataset before which Amazon Lookout for Equipment stopped the
inference execution.

Type: Timestamp

Required: No

**[DataStartTimeAfter](#API_ListInferenceExecutions_RequestSyntax "#API_ListInferenceExecutions_RequestSyntax")**

The time reference in the inferenced dataset after which Amazon Lookout for Equipment started the inference
execution.

Type: Timestamp

Required: No

**[InferenceSchedulerName](#API_ListInferenceExecutions_RequestSyntax "#API_ListInferenceExecutions_RequestSyntax")**

The name of the inference scheduler for the inference execution listed.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 200.

Pattern: `^[0-9a-zA-Z_-]{1,200}$`

Required: Yes

**[MaxResults](#API_ListInferenceExecutions_RequestSyntax "#API_ListInferenceExecutions_RequestSyntax")**

Specifies the maximum number of inference executions to list.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 500.

Required: No

**[NextToken](#API_ListInferenceExecutions_RequestSyntax "#API_ListInferenceExecutions_RequestSyntax")**

An opaque pagination token indicating where to continue the listing of inference
executions.

Type: String

Length Constraints: Maximum length of 8192.

Pattern: `\p{ASCII}{0,8192}`

Required: No

**[Status](#API_ListInferenceExecutions_RequestSyntax "#API_ListInferenceExecutions_RequestSyntax")**

The status of the inference execution.

Type: String

Valid Values: `IN_PROGRESS | SUCCESS | FAILED`

Required: No

## Response Syntax

```
{
   "InferenceExecutionSummaries": [
      {
         "CustomerResultObject": {
            "Bucket": "***string***",
            "Key": "***string***"
         },
         "DataEndTime": ***number***,
         "DataInputConfiguration": {
            "InferenceInputNameConfiguration": {
               "ComponentTimestampDelimiter": "***string***",
               "TimestampFormat": "***string***"
            },
            "InputTimeZoneOffset": "***string***",
            "S3InputConfiguration": {
               "Bucket": "***string***",
               "Prefix": "***string***"
            }
         },
         "DataOutputConfiguration": {
            "KmsKeyId": "***string***",
            "S3OutputConfiguration": {
               "Bucket": "***string***",
               "Prefix": "***string***"
            }
         },
         "DataStartTime": ***number***,
         "FailedReason": "***string***",
         "InferenceSchedulerArn": "***string***",
         "InferenceSchedulerName": "***string***",
         "ModelArn": "***string***",
         "ModelName": "***string***",
         "ModelVersion": ***number***,
         "ModelVersionArn": "***string***",
         "ScheduledStartTime": ***number***,
         "Status": "***string***"
      }
   ],
   "NextToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[InferenceExecutionSummaries](#API_ListInferenceExecutions_ResponseSyntax "#API_ListInferenceExecutions_ResponseSyntax")**

Provides an array of information about the individual inference executions returned from
the `ListInferenceExecutions` operation, including model used, inference
scheduler, data configuration, and so on.

###### Note

If you don't supply the `InferenceSchedulerName` request parameter, or
if you supply the name of an inference scheduler that doesn't exist,
`ListInferenceExecutions` returns an empty array in
`InferenceExecutionSummaries`.

Type: Array of [InferenceExecutionSummary](API_InferenceExecutionSummary.md "API_InferenceExecutionSummary.md") objects

**[NextToken](#API_ListInferenceExecutions_ResponseSyntax "#API_ListInferenceExecutions_ResponseSyntax")**

An opaque pagination token indicating where to continue the listing of inference
executions.

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

**ResourceNotFoundException**

The resource requested could not be found. Verify the resource ID and retry your
request.

HTTP Status Code: 400

**ThrottlingException**

The request was denied due to request throttling.

HTTP Status Code: 400

**ValidationException**

The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related AWS
service that's being utilized.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/lookoutequipment-2020-12-15/ListInferenceExecutions.md "../../../goto/cli2/lookoutequipment-2020-12-15/ListInferenceExecutions.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/lookoutequipment-2020-12-15/ListInferenceExecutions.md "../../../goto/DotNetSDKV4/lookoutequipment-2020-12-15/ListInferenceExecutions.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/lookoutequipment-2020-12-15/ListInferenceExecutions.md "../../../goto/SdkForCpp/lookoutequipment-2020-12-15/ListInferenceExecutions.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/lookoutequipment-2020-12-15/ListInferenceExecutions.md "../../../goto/SdkForGoV2/lookoutequipment-2020-12-15/ListInferenceExecutions.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/ListInferenceExecutions.md "../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/ListInferenceExecutions.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/ListInferenceExecutions.md "../../../goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/ListInferenceExecutions.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/lookoutequipment-2020-12-15/ListInferenceExecutions.md "../../../goto/SdkForKotlin/lookoutequipment-2020-12-15/ListInferenceExecutions.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/lookoutequipment-2020-12-15/ListInferenceExecutions.md "../../../goto/SdkForPHPV3/lookoutequipment-2020-12-15/ListInferenceExecutions.md")
- [AWS SDK for Python](../../../goto/boto3/lookoutequipment-2020-12-15/ListInferenceExecutions.md "../../../goto/boto3/lookoutequipment-2020-12-15/ListInferenceExecutions.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/ListInferenceExecutions.md "../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/ListInferenceExecutions.md")
