On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# ListDataIngestionJobs

Provides a list of all data ingestion jobs, including dataset name and ARN, S3 location
of the input data, status, and so on.

## Request Syntax

```
{
   "DatasetName": "`string`",
   "MaxResults": `number`,
   "NextToken": "`string`",
   "Status": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[DatasetName](#API_ListDataIngestionJobs_RequestSyntax "#API_ListDataIngestionJobs_RequestSyntax")**

The name of the dataset being used for the data ingestion job.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 200.

Pattern: `^[0-9a-zA-Z_-]{1,200}$`

Required: No

**[MaxResults](#API_ListDataIngestionJobs_RequestSyntax "#API_ListDataIngestionJobs_RequestSyntax")**

Specifies the maximum number of data ingestion jobs to list.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 500.

Required: No

**[NextToken](#API_ListDataIngestionJobs_RequestSyntax "#API_ListDataIngestionJobs_RequestSyntax")**

An opaque pagination token indicating where to continue the listing of data ingestion
jobs.

Type: String

Length Constraints: Maximum length of 8192.

Pattern: `\p{ASCII}{0,8192}`

Required: No

**[Status](#API_ListDataIngestionJobs_RequestSyntax "#API_ListDataIngestionJobs_RequestSyntax")**

Indicates the status of the data ingestion job.

Type: String

Valid Values: `IN_PROGRESS | SUCCESS | FAILED | IMPORT_IN_PROGRESS`

Required: No

## Response Syntax

```
{
   "DataIngestionJobSummaries": [
      {
         "DatasetArn": "***string***",
         "DatasetName": "***string***",
         "IngestionInputConfiguration": {
            "S3InputConfiguration": {
               "Bucket": "***string***",
               "KeyPattern": "***string***",
               "Prefix": "***string***"
            }
         },
         "JobId": "***string***",
         "Status": "***string***"
      }
   ],
   "NextToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[DataIngestionJobSummaries](#API_ListDataIngestionJobs_ResponseSyntax "#API_ListDataIngestionJobs_ResponseSyntax")**

Specifies information about the specific data ingestion job, including dataset name and
status.

Type: Array of [DataIngestionJobSummary](API_DataIngestionJobSummary.md "API_DataIngestionJobSummary.md") objects

**[NextToken](#API_ListDataIngestionJobs_ResponseSyntax "#API_ListDataIngestionJobs_ResponseSyntax")**

An opaque pagination token indicating where to continue the listing of data ingestion
jobs.

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

- [AWS Command Line Interface V2](../../../goto/cli2/lookoutequipment-2020-12-15/ListDataIngestionJobs.md "../../../goto/cli2/lookoutequipment-2020-12-15/ListDataIngestionJobs.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/lookoutequipment-2020-12-15/ListDataIngestionJobs.md "../../../goto/DotNetSDKV3/lookoutequipment-2020-12-15/ListDataIngestionJobs.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/lookoutequipment-2020-12-15/ListDataIngestionJobs.md "../../../goto/SdkForCpp/lookoutequipment-2020-12-15/ListDataIngestionJobs.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/lookoutequipment-2020-12-15/ListDataIngestionJobs.md "../../../goto/SdkForGoV2/lookoutequipment-2020-12-15/ListDataIngestionJobs.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/ListDataIngestionJobs.md "../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/ListDataIngestionJobs.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/ListDataIngestionJobs.md "../../../goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/ListDataIngestionJobs.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/lookoutequipment-2020-12-15/ListDataIngestionJobs.md "../../../goto/SdkForKotlin/lookoutequipment-2020-12-15/ListDataIngestionJobs.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/lookoutequipment-2020-12-15/ListDataIngestionJobs.md "../../../goto/SdkForPHPV3/lookoutequipment-2020-12-15/ListDataIngestionJobs.md")
- [AWS SDK for Python](../../../goto/boto3/lookoutequipment-2020-12-15/ListDataIngestionJobs.md "../../../goto/boto3/lookoutequipment-2020-12-15/ListDataIngestionJobs.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/ListDataIngestionJobs.md "../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/ListDataIngestionJobs.md")
