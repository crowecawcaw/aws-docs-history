# DatasetImportJob

Describes a job that imports training data from a data source (Amazon S3
bucket) to an Amazon Personalize dataset. For more information, see [CreateDatasetImportJob](API_CreateDatasetImportJob.md "API_CreateDatasetImportJob.md").

A dataset import job can be in one of the following states:

- CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE
  FAILED

## Contents

**creationDateTime**

The creation date and time (in Unix time) of the dataset import
job.

Type: Timestamp

Required: No

**datasetArn**

The Amazon Resource Name (ARN) of the dataset that receives the
imported data.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: No

**datasetImportJobArn**

The ARN of the dataset import job.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: No

**dataSource**

The Amazon S3 bucket that contains the training data to import.

Type: [DataSource](API_DataSource.md "API_DataSource.md") object

Required: No

**failureReason**

If a dataset import job fails, provides the reason why.

Type: String

Required: No

**importMode**

The import mode used by the dataset import job to import new
records.

Type: String

Valid Values: `FULL | INCREMENTAL`

Required: No

**jobName**

The name of the import job.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z0-9][a-zA-Z0-9\-_]*`

Required: No

**lastUpdatedDateTime**

The date and time (in Unix time) the dataset was last updated.

Type: Timestamp

Required: No

**publishAttributionMetricsToS3**

Whether the job publishes metrics to Amazon S3 for a metric attribution.

Type: Boolean

Required: No

**roleArn**

The ARN of the IAM role that has permissions to read from the Amazon S3
data source.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: No

**status**

The status of the dataset import job.

A dataset import job can be in one of the following states:

- CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE
  FAILED

Type: String

Length Constraints: Maximum length of 256.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/DatasetImportJob.md "../../../goto/SdkForCpp/personalize-2018-05-22/DatasetImportJob.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/DatasetImportJob.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/DatasetImportJob.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/DatasetImportJob.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/DatasetImportJob.md")
