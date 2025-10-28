# CreateDatasetExportJob

Creates a job that exports data from your dataset to an Amazon S3 bucket.
To allow Amazon Personalize to export the training data, you must specify an
service-linked IAM role that gives Amazon Personalize `PutObject`
permissions for your Amazon S3 bucket. For information, see [Exporting a dataset](export-data.md "export-data.md") in the Amazon Personalize developer guide.

**Status**

A dataset export job can be in one of the following states:

- CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE
  FAILED
  To get the status of the export job, call [DescribeDatasetExportJob](API_DescribeDatasetExportJob.md "API_DescribeDatasetExportJob.md"), and specify the Amazon Resource Name
  (ARN) of the dataset export job. The dataset export is complete when the
  status shows as ACTIVE. If the status shows as CREATE FAILED, the response
  includes a `failureReason` key, which describes why the job
  failed.

## Request Syntax

```
{
   "datasetArn": "`string`",
   "ingestionMode": "`string`",
   "jobName": "`string`",
   "jobOutput": {
      "s3DataDestination": {
         "kmsKeyArn": "`string`",
         "path": "`string`"
      }
   },
   "roleArn": "`string`",
   "tags": [
      {
         "tagKey": "`string`",
         "tagValue": "`string`"
      }
   ]
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[datasetArn](#API_CreateDatasetExportJob_RequestSyntax "#API_CreateDatasetExportJob_RequestSyntax")**

The Amazon Resource Name (ARN) of the dataset that contains the data
to export.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: Yes

**[ingestionMode](#API_CreateDatasetExportJob_RequestSyntax "#API_CreateDatasetExportJob_RequestSyntax")**

The data to export, based on how you imported the data. You can choose
to export only `BULK` data that you imported using a dataset
import job, only `PUT` data that you imported incrementally
(using the console, PutEvents, PutUsers and PutItems operations), or
`ALL` for both types. The default value is `PUT`.

Type: String

Valid Values: `BULK | PUT | ALL`

Required: No

**[jobName](#API_CreateDatasetExportJob_RequestSyntax "#API_CreateDatasetExportJob_RequestSyntax")**

The name for the dataset export job.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z0-9][a-zA-Z0-9\-_]*`

Required: Yes

**[jobOutput](#API_CreateDatasetExportJob_RequestSyntax "#API_CreateDatasetExportJob_RequestSyntax")**

The path to the Amazon S3 bucket where the job's output is stored.

Type: [DatasetExportJobOutput](API_DatasetExportJobOutput.md "API_DatasetExportJobOutput.md") object

Required: Yes

**[roleArn](#API_CreateDatasetExportJob_RequestSyntax "#API_CreateDatasetExportJob_RequestSyntax")**

The Amazon Resource Name (ARN) of the IAM service role that has
permissions to add data to your output Amazon S3 bucket.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`

Required: Yes

**[tags](#API_CreateDatasetExportJob_RequestSyntax "#API_CreateDatasetExportJob_RequestSyntax")**

A list of [tags](tagging-resources.md "tagging-resources.md") to apply to the dataset export job.

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

Array Members: Minimum number of 0 items. Maximum number of 200 items.

Required: No

## Response Syntax

```
{
   "datasetExportJobArn": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[datasetExportJobArn](#API_CreateDatasetExportJob_ResponseSyntax "#API_CreateDatasetExportJob_ResponseSyntax")**

The Amazon Resource Name (ARN) of the dataset export job.

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

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-2018-05-22/CreateDatasetExportJob.md "../../../goto/cli2/personalize-2018-05-22/CreateDatasetExportJob.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/personalize-2018-05-22/CreateDatasetExportJob.md "../../../goto/DotNetSDKV3/personalize-2018-05-22/CreateDatasetExportJob.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/CreateDatasetExportJob.md "../../../goto/SdkForCpp/personalize-2018-05-22/CreateDatasetExportJob.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-2018-05-22/CreateDatasetExportJob.md "../../../goto/SdkForGoV2/personalize-2018-05-22/CreateDatasetExportJob.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/CreateDatasetExportJob.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/CreateDatasetExportJob.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/CreateDatasetExportJob.md "../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/CreateDatasetExportJob.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-2018-05-22/CreateDatasetExportJob.md "../../../goto/SdkForKotlin/personalize-2018-05-22/CreateDatasetExportJob.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-2018-05-22/CreateDatasetExportJob.md "../../../goto/SdkForPHPV3/personalize-2018-05-22/CreateDatasetExportJob.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-2018-05-22/CreateDatasetExportJob.md "../../../goto/boto3/personalize-2018-05-22/CreateDatasetExportJob.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/CreateDatasetExportJob.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/CreateDatasetExportJob.md")
