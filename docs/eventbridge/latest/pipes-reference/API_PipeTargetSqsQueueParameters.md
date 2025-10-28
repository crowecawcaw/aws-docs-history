# PipeTargetSqsQueueParameters

The parameters for using a Amazon SQS stream as a target.

## Contents

**MessageDeduplicationId**

This parameter applies only to FIFO (first-in-first-out) queues.

The token used for deduplication of sent messages.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 100.

Required: No

**MessageGroupId**

The FIFO message group ID to use as the target.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 100.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/pipes-2015-10-07/PipeTargetSqsQueueParameters.md "../../../goto/SdkForCpp/pipes-2015-10-07/PipeTargetSqsQueueParameters.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/pipes-2015-10-07/PipeTargetSqsQueueParameters.md "../../../goto/SdkForJavaV2/pipes-2015-10-07/PipeTargetSqsQueueParameters.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/pipes-2015-10-07/PipeTargetSqsQueueParameters.md "../../../goto/SdkForRubyV3/pipes-2015-10-07/PipeTargetSqsQueueParameters.md")
