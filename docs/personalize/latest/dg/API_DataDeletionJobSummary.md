# DataDeletionJobSummary

Provides a summary of the properties of a data deletion job. For a complete listing, call the [DescribeDataDeletionJob](API_DescribeDataDeletionJob.md "API_DescribeDataDeletionJob.md")
API operation.

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

The Amazon Resource Name (ARN) of the dataset group the job deleted records from.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

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

**status**

The status of the data deletion job.

A data deletion job can have one of the following statuses:

- PENDING > IN_PROGRESS > COMPLETED -or- FAILED

Type: String

Length Constraints: Maximum length of 256.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/DataDeletionJobSummary.md "../../../goto/SdkForCpp/personalize-2018-05-22/DataDeletionJobSummary.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/DataDeletionJobSummary.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/DataDeletionJobSummary.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/DataDeletionJobSummary.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/DataDeletionJobSummary.md")
