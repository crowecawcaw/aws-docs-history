# DatasetImportJobSummary

Provides a summary of the properties of a dataset import job. For a complete listing, call the
[DescribeDatasetImportJob](API_DescribeDatasetImportJob.md "API_DescribeDatasetImportJob.md") API.

## Contents

**creationDateTime**

The date and time (in Unix time) that the dataset import job was created.

Type: Timestamp

Required: No

**datasetImportJobArn**

The Amazon Resource Name (ARN) of the dataset import job.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: No

**failureReason**

If a dataset import job fails, the reason behind the failure.

Type: String

Required: No

**importMode**

The import mode the dataset import job used to update the data in the dataset.
For more information see [Updating existing bulk
data](updating-existing-bulk-data.md "updating-existing-bulk-data.md").

Type: String

Valid Values: `FULL | INCREMENTAL`

Required: No

**jobName**

The name of the dataset import job.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z0-9][a-zA-Z0-9\-_]*`

Required: No

**lastUpdatedDateTime**

The date and time (in Unix time) that the dataset import job status was last updated.

Type: Timestamp

Required: No

**status**

The status of the dataset import job.

A dataset import job can be in one of the following states:

- CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED

Type: String

Length Constraints: Maximum length of 256.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/DatasetImportJobSummary.md "../../../goto/SdkForCpp/personalize-2018-05-22/DatasetImportJobSummary.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/DatasetImportJobSummary.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/DatasetImportJobSummary.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/DatasetImportJobSummary.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/DatasetImportJobSummary.md")
