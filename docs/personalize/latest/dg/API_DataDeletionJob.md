# DataDeletionJob

Describes a job that deletes all
references to specific users from an Amazon Personalize dataset group in batches. For information about creating a data deletion job,
see [Deleting users](delete-records.md "delete-records.md").

## Contents

**creationDateTime**

The creation date and time (in Unix time) of the data deletion
job.

Type: Timestamp

Required: No

**dataDeletionJobArn**

The Amazon Resource Name (ARN) of the data deletion job.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: No

**datasetGroupArn**

The Amazon Resource Name (ARN) of the dataset group the job deletes records from.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: No

**dataSource**

Describes the data source that contains the data to upload to a dataset, or the list of
records to delete from Amazon Personalize.

Type: [DataSource](API_DataSource.md "API_DataSource.md") object

Required: No

**failureReason**

If a data deletion job fails, provides the reason why.

Type: String

Required: No

**jobName**

The name of the data deletion job.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z0-9][a-zA-Z0-9\-_]*`

Required: No

**lastUpdatedDateTime**

The date and time (in Unix time) the data deletion job was last updated.

Type: Timestamp

Required: No

**numDeleted**

The number of records deleted by a COMPLETED job.

Type: Integer

Required: No

**roleArn**

The Amazon Resource Name (ARN) of the IAM role that has permissions to read from the Amazon S3
data source.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`

Required: No

**status**

The status of the data deletion job.

A data deletion job can have one of the following statuses:

- PENDING > IN_PROGRESS > COMPLETED -or- FAILED

Type: String

Length Constraints: Maximum length of 256.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/DataDeletionJob.md "../../../goto/SdkForCpp/personalize-2018-05-22/DataDeletionJob.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/DataDeletionJob.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/DataDeletionJob.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/DataDeletionJob.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/DataDeletionJob.md")
