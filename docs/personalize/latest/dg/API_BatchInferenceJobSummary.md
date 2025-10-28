# BatchInferenceJobSummary

A truncated version of the [BatchInferenceJob](API_BatchInferenceJob.md "API_BatchInferenceJob.md"). The
[ListBatchInferenceJobs](API_ListBatchInferenceJobs.md "API_ListBatchInferenceJobs.md") operation returns a list of batch inference job
summaries.

## Contents

**batchInferenceJobArn**

The Amazon Resource Name (ARN) of the batch inference job.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: No

**batchInferenceJobMode**

The job's mode.

Type: String

Valid Values: `BATCH_INFERENCE | THEME_GENERATION`

Required: No

**creationDateTime**

The time at which the batch inference job was created.

Type: Timestamp

Required: No

**failureReason**

If the batch inference job failed, the reason for the failure.

Type: String

Required: No

**jobName**

The name of the batch inference job.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z0-9][a-zA-Z0-9\-_]*`

Required: No

**lastUpdatedDateTime**

The time at which the batch inference job was last updated.

Type: Timestamp

Required: No

**solutionVersionArn**

The ARN of the solution version used by the batch inference job.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: No

**status**

The status of the batch inference job. The status is one of the following values:

- PENDING
- IN PROGRESS
- ACTIVE
- CREATE FAILED

Type: String

Length Constraints: Maximum length of 256.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/BatchInferenceJobSummary.md "../../../goto/SdkForCpp/personalize-2018-05-22/BatchInferenceJobSummary.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/BatchInferenceJobSummary.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/BatchInferenceJobSummary.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/BatchInferenceJobSummary.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/BatchInferenceJobSummary.md")
