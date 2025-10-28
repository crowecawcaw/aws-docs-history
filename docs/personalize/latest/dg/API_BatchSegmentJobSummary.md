# BatchSegmentJobSummary

A truncated version of the [BatchSegmentJob](API_BatchSegmentJob.md "API_BatchSegmentJob.md") datatype.
[ListBatchSegmentJobs](API_ListBatchSegmentJobs.md "API_ListBatchSegmentJobs.md") operation returns a list of batch segment job
summaries.

## Contents

**batchSegmentJobArn**

The Amazon Resource Name (ARN) of the batch segment job.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: No

**creationDateTime**

The time at which the batch segment job was created.

Type: Timestamp

Required: No

**failureReason**

If the batch segment job failed, the reason for the failure.

Type: String

Required: No

**jobName**

The name of the batch segment job.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z0-9][a-zA-Z0-9\-_]*`

Required: No

**lastUpdatedDateTime**

The time at which the batch segment job was last updated.

Type: Timestamp

Required: No

**solutionVersionArn**

The Amazon Resource Name (ARN) of the solution version used by the batch segment job to generate batch segments.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: No

**status**

The status of the batch segment job. The status is one of the following values:

- PENDING
- IN PROGRESS
- ACTIVE
- CREATE FAILED

Type: String

Length Constraints: Maximum length of 256.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/BatchSegmentJobSummary.md "../../../goto/SdkForCpp/personalize-2018-05-22/BatchSegmentJobSummary.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/BatchSegmentJobSummary.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/BatchSegmentJobSummary.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/BatchSegmentJobSummary.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/BatchSegmentJobSummary.md")
