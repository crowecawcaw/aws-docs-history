On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# StartDataIngestionJob

Starts a data ingestion job. Amazon Lookout for Equipment returns the job status.

## Request Syntax

```
{
   "ClientToken": "`string`",
   "DatasetName": "`string`",
   "IngestionInputConfiguration": {
      "S3InputConfiguration": {
         "Bucket": "`string`",
         "KeyPattern": "`string`",
         "Prefix": "`string`"
      }
   },
   "RoleArn": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[ClientToken](#API_StartDataIngestionJob_RequestSyntax "#API_StartDataIngestionJob_RequestSyntax")**

A unique identifier for the request. If you do not set the client request token, Amazon
Lookout for Equipment generates one.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `\p{ASCII}{1,256}`

Required: Yes

**[DatasetName](#API_StartDataIngestionJob_RequestSyntax "#API_StartDataIngestionJob_RequestSyntax")**

The name of the dataset being used by the data ingestion job.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 200.

Pattern: `^[0-9a-zA-Z_-]{1,200}$`

Required: Yes

**[IngestionInputConfiguration](#API_StartDataIngestionJob_RequestSyntax "#API_StartDataIngestionJob_RequestSyntax")**

Specifies information for the input data for the data ingestion job, including dataset
S3 location.

Type: [IngestionInputConfiguration](API_IngestionInputConfiguration.md "API_IngestionInputConfiguration.md") object

Required: Yes

**[RoleArn](#API_StartDataIngestionJob_RequestSyntax "#API_StartDataIngestionJob_RequestSyntax")**

The Amazon Resource Name (ARN) of a role with permission to access the data source for
the data ingestion job.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Pattern: `arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+`

Required: Yes

## Response Syntax

```
{
   "JobId": "***string***",
   "Status": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[JobId](#API_StartDataIngestionJob_ResponseSyntax "#API_StartDataIngestionJob_ResponseSyntax")**

Indicates the job ID of the data ingestion job.

Type: String

Length Constraints: Maximum length of 32.

Pattern: `[A-Fa-f0-9]{0,32}`

**[Status](#API_StartDataIngestionJob_ResponseSyntax "#API_StartDataIngestionJob_ResponseSyntax")**

Indicates the status of the `StartDataIngestionJob` operation.

Type: String

Valid Values: `IN_PROGRESS | SUCCESS | FAILED | IMPORT_IN_PROGRESS`

## Errors

**AccessDeniedException**

The request could not be completed because you do not have access to the resource.

HTTP Status Code: 400

**ConflictException**

The request could not be completed due to a conflict with the current state of the
target resource.

HTTP Status Code: 400

**InternalServerException**

Processing of the request has failed because of an unknown error, exception or failure.

HTTP Status Code: 500

**ResourceNotFoundException**

The resource requested could not be found. Verify the resource ID and retry your
request.

HTTP Status Code: 400

**ServiceQuotaExceededException**

Resource limitations have been exceeded.

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

- [AWS Command Line Interface V2](../../../goto/cli2/lookoutequipment-2020-12-15/StartDataIngestionJob.md "../../../goto/cli2/lookoutequipment-2020-12-15/StartDataIngestionJob.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/lookoutequipment-2020-12-15/StartDataIngestionJob.md "../../../goto/DotNetSDKV4/lookoutequipment-2020-12-15/StartDataIngestionJob.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/lookoutequipment-2020-12-15/StartDataIngestionJob.md "../../../goto/SdkForCpp/lookoutequipment-2020-12-15/StartDataIngestionJob.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/lookoutequipment-2020-12-15/StartDataIngestionJob.md "../../../goto/SdkForGoV2/lookoutequipment-2020-12-15/StartDataIngestionJob.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/StartDataIngestionJob.md "../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/StartDataIngestionJob.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/StartDataIngestionJob.md "../../../goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/StartDataIngestionJob.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/lookoutequipment-2020-12-15/StartDataIngestionJob.md "../../../goto/SdkForKotlin/lookoutequipment-2020-12-15/StartDataIngestionJob.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/lookoutequipment-2020-12-15/StartDataIngestionJob.md "../../../goto/SdkForPHPV3/lookoutequipment-2020-12-15/StartDataIngestionJob.md")
- [AWS SDK for Python](../../../goto/boto3/lookoutequipment-2020-12-15/StartDataIngestionJob.md "../../../goto/boto3/lookoutequipment-2020-12-15/StartDataIngestionJob.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/StartDataIngestionJob.md "../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/StartDataIngestionJob.md")
