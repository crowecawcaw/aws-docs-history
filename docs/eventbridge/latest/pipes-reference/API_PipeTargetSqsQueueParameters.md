

# PipeTargetSqsQueueParameters
<a name="API_PipeTargetSqsQueueParameters"></a>

The parameters for using a Amazon SQS stream as a target.

## Contents
<a name="API_PipeTargetSqsQueueParameters_Contents"></a>

 ** MessageDeduplicationId **   <a name="eventbridge-Type-PipeTargetSqsQueueParameters-MessageDeduplicationId"></a>
This parameter applies only to FIFO (first-in-first-out) queues.  
The token used for deduplication of sent messages.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 100.  
Required: No

 ** MessageGroupId **   <a name="eventbridge-Type-PipeTargetSqsQueueParameters-MessageGroupId"></a>
The FIFO message group ID to use as the target.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 100.  
Required: No

## See Also
<a name="API_PipeTargetSqsQueueParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pipes-2015-10-07/PipeTargetSqsQueueParameters) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pipes-2015-10-07/PipeTargetSqsQueueParameters) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pipes-2015-10-07/PipeTargetSqsQueueParameters) 