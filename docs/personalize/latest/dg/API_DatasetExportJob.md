# DatasetExportJob

Describes a job that exports a dataset to an Amazon S3 bucket. For more
information, see [CreateDatasetExportJob](API_CreateDatasetExportJob.md "API_CreateDatasetExportJob.md").

A dataset export job can be in one of the following states:

- CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE
  FAILED

## Contents

**creationDateTime**

The creation date and time (in Unix time) of the dataset export
job.

Type: Timestamp

Required: No

**datasetArn**

The Amazon Resource Name (ARN) of the dataset to export.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: No

**datasetExportJobArn**

The Amazon Resource Name (ARN) of the dataset export job.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: No

**failureReason**

If a dataset export job fails, provides the reason why.

Type: String

Required: No

**ingestionMode**

The data to export, based on how you imported the data. You can choose
to export `BULK` data that you imported using a dataset import
job, `PUT` data that you imported incrementally (using the
console, PutEvents, PutUsers and PutItems operations), or `ALL`
for both types. The default value is `PUT`.

Type: String

Valid Values: `BULK | PUT | ALL`

Required: No

**jobName**

The name of the export job.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z0-9][a-zA-Z0-9\-_]*`

Required: No

**jobOutput**

The path to the Amazon S3 bucket where the job's output is stored. For
example:

`s3://bucket-name/folder-name/`

Type: [DatasetExportJobOutput](API_DatasetExportJobOutput.md "API_DatasetExportJobOutput.md") object

Required: No

**lastUpdatedDateTime**

The date and time (in Unix time) the status of the dataset export job
was last updated.

Type: Timestamp

Required: No

**roleArn**

The Amazon Resource Name (ARN) of the IAM service role that has
permissions to add data to your output Amazon S3 bucket.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: No

**status**

The status of the dataset export job.

A dataset export job can be in one of the following states:

- CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE
  FAILED

Type: String

Length Constraints: Maximum length of 256.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/DatasetExportJob.md "../../../goto/SdkForCpp/personalize-2018-05-22/DatasetExportJob.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/DatasetExportJob.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/DatasetExportJob.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/DatasetExportJob.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/DatasetExportJob.md")
