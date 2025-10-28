# DatasetExportJobSummary

Provides a summary of the properties of a dataset export job. For a complete listing, call the
[DescribeDatasetExportJob](API_DescribeDatasetExportJob.md "API_DescribeDatasetExportJob.md") API.

## Contents

**creationDateTime**

The date and time (in Unix time) that the dataset export job was created.

Type: Timestamp

Required: No

**datasetExportJobArn**

The Amazon Resource Name (ARN) of the dataset export job.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: No

**failureReason**

If a dataset export job fails, the reason behind the failure.

Type: String

Required: No

**jobName**

The name of the dataset export job.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z0-9][a-zA-Z0-9\-_]*`

Required: No

**lastUpdatedDateTime**

The date and time (in Unix time) that the dataset export job status was last updated.

Type: Timestamp

Required: No

**status**

The status of the dataset export job.

A dataset export job can be in one of the following states:

- CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED

Type: String

Length Constraints: Maximum length of 256.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/DatasetExportJobSummary.md "../../../goto/SdkForCpp/personalize-2018-05-22/DatasetExportJobSummary.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/DatasetExportJobSummary.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/DatasetExportJobSummary.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/DatasetExportJobSummary.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/DatasetExportJobSummary.md")
