# CreateDatasetImportJob

Creates a job that imports training data from your data source (an
Amazon S3 bucket) to an Amazon Personalize dataset. To allow Amazon Personalize to import the
training data, you must specify an IAM service role that has permission to
read from the data source, as Amazon Personalize makes a copy of your data and
processes it internally. For information on granting access to your Amazon S3
bucket, see [Giving
Amazon Personalize Access to Amazon S3 Resources](granting-personalize-s3-access.md "granting-personalize-s3-access.md").

If you already created a recommender or deployed a custom solution version with a campaign, how new bulk records
influence recommendations depends on the domain use case or recipe that you use. For more information, see [How new data influences
real-time recommendations](how-new-data-influences-recommendations.md "how-new-data-influences-recommendations.md").

###### Important

By default, a dataset import job replaces any existing data in the
dataset that you imported in bulk. To add new records without replacing
existing data, specify INCREMENTAL for the import mode in the
CreateDatasetImportJob operation.

**Status**

A dataset import job can be in one of the following states:

- CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE
  FAILED
  To get the status of the import job, call [DescribeDatasetImportJob](API_DescribeDatasetImportJob.md "API_DescribeDatasetImportJob.md"), providing the Amazon Resource Name
  (ARN) of the dataset import job. The dataset import is complete when the
  status shows as ACTIVE. If the status shows as CREATE FAILED, the response
  includes a `failureReason` key, which describes why the job
  failed.

###### Note

Importing takes time. You must wait until the status shows as ACTIVE
before training a model using the dataset.

###### Related APIs

- [ListDatasetImportJobs](API_ListDatasetImportJobs.md "API_ListDatasetImportJobs.md")
- [DescribeDatasetImportJob](API_DescribeDatasetImportJob.md "API_DescribeDatasetImportJob.md")

## Request Syntax

```
{
   "datasetArn": "`string`",
   "dataSource": {
      "dataLocation": "`string`"
   },
   "importMode": "`string`",
   "jobName": "`string`",
   "publishAttributionMetricsToS3": `boolean`,
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

**[datasetArn](#API_CreateDatasetImportJob_RequestSyntax "#API_CreateDatasetImportJob_RequestSyntax")**

The ARN of the dataset that receives the imported data.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: Yes

**[dataSource](#API_CreateDatasetImportJob_RequestSyntax "#API_CreateDatasetImportJob_RequestSyntax")**

The Amazon S3 bucket that contains the training data to import.

Type: [DataSource](API_DataSource.md "API_DataSource.md") object

Required: Yes

**[importMode](#API_CreateDatasetImportJob_RequestSyntax "#API_CreateDatasetImportJob_RequestSyntax")**

Specify how to add the new records to an existing dataset. The default
import mode is `FULL`. If you haven't imported bulk records into the dataset previously, you
can only specify `FULL`.

- Specify `FULL` to overwrite all existing bulk data in
  your dataset. Data you imported individually is not replaced.
- Specify `INCREMENTAL` to append the new records to the
  existing data in your dataset. Amazon Personalize replaces any record with the
  same ID with the new one.

Type: String

Valid Values: `FULL | INCREMENTAL`

Required: No

**[jobName](#API_CreateDatasetImportJob_RequestSyntax "#API_CreateDatasetImportJob_RequestSyntax")**

The name for the dataset import job.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z0-9][a-zA-Z0-9\-_]*`

Required: Yes

**[publishAttributionMetricsToS3](#API_CreateDatasetImportJob_RequestSyntax "#API_CreateDatasetImportJob_RequestSyntax")**

If you created a metric attribution, specify whether to publish metrics for this import job to Amazon S3

Type: Boolean

Required: No

**[roleArn](#API_CreateDatasetImportJob_RequestSyntax "#API_CreateDatasetImportJob_RequestSyntax")**

The ARN of the IAM role that has permissions to read from the Amazon S3
data source.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`

Required: Yes

**[tags](#API_CreateDatasetImportJob_RequestSyntax "#API_CreateDatasetImportJob_RequestSyntax")**

A list of [tags](tagging-resources.md "tagging-resources.md") to apply to the dataset import job.

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

Array Members: Minimum number of 0 items. Maximum number of 200 items.

Required: No

## Response Syntax

```
{
   "datasetImportJobArn": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[datasetImportJobArn](#API_CreateDatasetImportJob_ResponseSyntax "#API_CreateDatasetImportJob_ResponseSyntax")**

The ARN of the dataset import job.

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

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-2018-05-22/CreateDatasetImportJob.md "../../../goto/cli2/personalize-2018-05-22/CreateDatasetImportJob.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/personalize-2018-05-22/CreateDatasetImportJob.md "../../../goto/DotNetSDKV3/personalize-2018-05-22/CreateDatasetImportJob.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/CreateDatasetImportJob.md "../../../goto/SdkForCpp/personalize-2018-05-22/CreateDatasetImportJob.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-2018-05-22/CreateDatasetImportJob.md "../../../goto/SdkForGoV2/personalize-2018-05-22/CreateDatasetImportJob.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/CreateDatasetImportJob.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/CreateDatasetImportJob.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/CreateDatasetImportJob.md "../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/CreateDatasetImportJob.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-2018-05-22/CreateDatasetImportJob.md "../../../goto/SdkForKotlin/personalize-2018-05-22/CreateDatasetImportJob.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-2018-05-22/CreateDatasetImportJob.md "../../../goto/SdkForPHPV3/personalize-2018-05-22/CreateDatasetImportJob.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-2018-05-22/CreateDatasetImportJob.md "../../../goto/boto3/personalize-2018-05-22/CreateDatasetImportJob.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/CreateDatasetImportJob.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/CreateDatasetImportJob.md")
