On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# ListRetrainingSchedulers

Lists all retraining schedulers in your account, filtering by model name prefix and
status.

## Request Syntax

```
{
   "MaxResults": `number`,
   "ModelNameBeginsWith": "`string`",
   "NextToken": "`string`",
   "Status": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[MaxResults](#API_ListRetrainingSchedulers_RequestSyntax "#API_ListRetrainingSchedulers_RequestSyntax")**

Specifies the maximum number of retraining schedulers to list.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 500.

Required: No

**[ModelNameBeginsWith](#API_ListRetrainingSchedulers_RequestSyntax "#API_ListRetrainingSchedulers_RequestSyntax")**

Specify this field to only list retraining schedulers whose machine learning models
begin with the value you specify.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 200.

Pattern: `^[0-9a-zA-Z_-]{1,200}$`

Required: No

**[NextToken](#API_ListRetrainingSchedulers_RequestSyntax "#API_ListRetrainingSchedulers_RequestSyntax")**

If the number of results exceeds the maximum, a pagination token is returned. Use the
token in the request to show the next page of retraining schedulers.

Type: String

Length Constraints: Maximum length of 8192.

Pattern: `\p{ASCII}{0,8192}`

Required: No

**[Status](#API_ListRetrainingSchedulers_RequestSyntax "#API_ListRetrainingSchedulers_RequestSyntax")**

Specify this field to only list retraining schedulers whose status matches the value you
specify.

Type: String

Valid Values: `PENDING | RUNNING | STOPPING | STOPPED`

Required: No

## Response Syntax

```
{
   "NextToken": "***string***",
   "RetrainingSchedulerSummaries": [
      {
         "LookbackWindow": "***string***",
         "ModelArn": "***string***",
         "ModelName": "***string***",
         "RetrainingFrequency": "***string***",
         "RetrainingStartDate": ***number***,
         "Status": "***string***"
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[NextToken](#API_ListRetrainingSchedulers_ResponseSyntax "#API_ListRetrainingSchedulers_ResponseSyntax")**

If the number of results exceeds the maximum, this pagination token is returned. Use
this token in the request to show the next page of retraining schedulers.

Type: String

Length Constraints: Maximum length of 8192.

Pattern: `\p{ASCII}{0,8192}`

**[RetrainingSchedulerSummaries](#API_ListRetrainingSchedulers_ResponseSyntax "#API_ListRetrainingSchedulers_ResponseSyntax")**

Provides information on the specified retraining scheduler, including the model name,
model ARN, status, and start date.

Type: Array of [RetrainingSchedulerSummary](API_RetrainingSchedulerSummary.md "API_RetrainingSchedulerSummary.md") objects

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

- [AWS Command Line Interface V2](../../../goto/cli2/lookoutequipment-2020-12-15/ListRetrainingSchedulers.md "../../../goto/cli2/lookoutequipment-2020-12-15/ListRetrainingSchedulers.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/lookoutequipment-2020-12-15/ListRetrainingSchedulers.md "../../../goto/DotNetSDKV4/lookoutequipment-2020-12-15/ListRetrainingSchedulers.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/lookoutequipment-2020-12-15/ListRetrainingSchedulers.md "../../../goto/SdkForCpp/lookoutequipment-2020-12-15/ListRetrainingSchedulers.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/lookoutequipment-2020-12-15/ListRetrainingSchedulers.md "../../../goto/SdkForGoV2/lookoutequipment-2020-12-15/ListRetrainingSchedulers.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/ListRetrainingSchedulers.md "../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/ListRetrainingSchedulers.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/ListRetrainingSchedulers.md "../../../goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/ListRetrainingSchedulers.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/lookoutequipment-2020-12-15/ListRetrainingSchedulers.md "../../../goto/SdkForKotlin/lookoutequipment-2020-12-15/ListRetrainingSchedulers.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/lookoutequipment-2020-12-15/ListRetrainingSchedulers.md "../../../goto/SdkForPHPV3/lookoutequipment-2020-12-15/ListRetrainingSchedulers.md")
- [AWS SDK for Python](../../../goto/boto3/lookoutequipment-2020-12-15/ListRetrainingSchedulers.md "../../../goto/boto3/lookoutequipment-2020-12-15/ListRetrainingSchedulers.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/ListRetrainingSchedulers.md "../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/ListRetrainingSchedulers.md")
