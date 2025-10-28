# BatchRetryStrategy

The retry strategy that's associated with a job. For more information, see [Automated job
retries](../../../batch/latest/userguide/job_retries.md "../../../batch/latest/userguide/job_retries.md") in the _AWS Batch User Guide_.

## Contents

**Attempts**

The number of times to move a job to the `RUNNABLE` status. If the value of
`attempts` is greater than one, the job is retried on failure the same number
of attempts as the value.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 10.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/pipes-2015-10-07/BatchRetryStrategy.md "../../../goto/SdkForCpp/pipes-2015-10-07/BatchRetryStrategy.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/pipes-2015-10-07/BatchRetryStrategy.md "../../../goto/SdkForJavaV2/pipes-2015-10-07/BatchRetryStrategy.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/pipes-2015-10-07/BatchRetryStrategy.md "../../../goto/SdkForRubyV3/pipes-2015-10-07/BatchRetryStrategy.md")
