# CreateDataDeletionJob

Creates a batch job that deletes all
references to specific users from an Amazon Personalize dataset group in batches. You specify the users to delete in a CSV file of userIds in
an Amazon S3 bucket. After a job completes, Amazon Personalize no longer trains
on the users’ data and no longer considers the users when generating user segments.
For more information about creating a data deletion job, see [Deleting users](delete-records.md "delete-records.md").

- Your input file must be a CSV file with a single USER_ID column that lists the users IDs. For more information
  about preparing the CSV file, see [Preparing your data deletion file and uploading it to Amazon S3](prepare-deletion-input-file.md "prepare-deletion-input-file.md").
- To give Amazon Personalize permission to access your input CSV file of userIds, you must specify an IAM service role that has permission to
  read from the data source. This role
  needs `GetObject` and `ListBucket` permissions for the bucket and its content.
  These permissions are the same as importing data. For information on granting access to your Amazon S3
  bucket, see [Giving
  Amazon Personalize Access to Amazon S3 Resources](granting-personalize-s3-access.md "granting-personalize-s3-access.md").

After you create a job, it can take up to a day to delete all references to the users from datasets and models. Until the job completes,
Amazon Personalize continues to use the data when training. And if you use a User Segmentation recipe, the users might appear in user segments.

**Status**

A data deletion job can have one of the following statuses:

- PENDING > IN_PROGRESS > COMPLETED -or- FAILED
  To get the status of the data deletion job, call [DescribeDataDeletionJob](API_DescribeDataDeletionJob.md "API_DescribeDataDeletionJob.md") API operation and specify the Amazon Resource Name
  (ARN) of the job. If the status is FAILED, the response
  includes a `failureReason` key, which describes why the job
  failed.

###### Related APIs

- [ListDataDeletionJobs](API_ListDataDeletionJobs.md "API_ListDataDeletionJobs.md")
- [DescribeDataDeletionJob](API_DescribeDataDeletionJob.md "API_DescribeDataDeletionJob.md")

## Request Syntax

```
{
   "datasetGroupArn": "`string`",
   "dataSource": {
      "dataLocation": "`string`"
   },
   "jobName": "`string`",
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

**[datasetGroupArn](#API_CreateDataDeletionJob_RequestSyntax "#API_CreateDataDeletionJob_RequestSyntax")**

The Amazon Resource Name (ARN) of the dataset group that has the datasets you want to
delete records from.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: Yes

**[dataSource](#API_CreateDataDeletionJob_RequestSyntax "#API_CreateDataDeletionJob_RequestSyntax")**

The Amazon S3 bucket that contains the list of userIds of the users to delete.

Type: [DataSource](API_DataSource.md "API_DataSource.md") object

Required: Yes

**[jobName](#API_CreateDataDeletionJob_RequestSyntax "#API_CreateDataDeletionJob_RequestSyntax")**

The name for the data deletion job.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z0-9][a-zA-Z0-9\-_]*`

Required: Yes

**[roleArn](#API_CreateDataDeletionJob_RequestSyntax "#API_CreateDataDeletionJob_RequestSyntax")**

The Amazon Resource Name (ARN) of the IAM role that has permissions to read from the Amazon S3
data source.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`

Required: Yes

**[tags](#API_CreateDataDeletionJob_RequestSyntax "#API_CreateDataDeletionJob_RequestSyntax")**

A list of [tags](tagging-resources.md "tagging-resources.md") to apply to the data deletion job.

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

Array Members: Minimum number of 0 items. Maximum number of 200 items.

Required: No

## Response Syntax

```
{
   "dataDeletionJobArn": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[dataDeletionJobArn](#API_CreateDataDeletionJob_ResponseSyntax "#API_CreateDataDeletionJob_ResponseSyntax")**

The Amazon Resource Name (ARN) of the data deletion job.

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

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-2018-05-22/CreateDataDeletionJob.md "../../../goto/cli2/personalize-2018-05-22/CreateDataDeletionJob.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/personalize-2018-05-22/CreateDataDeletionJob.md "../../../goto/DotNetSDKV3/personalize-2018-05-22/CreateDataDeletionJob.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/CreateDataDeletionJob.md "../../../goto/SdkForCpp/personalize-2018-05-22/CreateDataDeletionJob.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-2018-05-22/CreateDataDeletionJob.md "../../../goto/SdkForGoV2/personalize-2018-05-22/CreateDataDeletionJob.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/CreateDataDeletionJob.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/CreateDataDeletionJob.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/CreateDataDeletionJob.md "../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/CreateDataDeletionJob.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-2018-05-22/CreateDataDeletionJob.md "../../../goto/SdkForKotlin/personalize-2018-05-22/CreateDataDeletionJob.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-2018-05-22/CreateDataDeletionJob.md "../../../goto/SdkForPHPV3/personalize-2018-05-22/CreateDataDeletionJob.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-2018-05-22/CreateDataDeletionJob.md "../../../goto/boto3/personalize-2018-05-22/CreateDataDeletionJob.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/CreateDataDeletionJob.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/CreateDataDeletionJob.md")
