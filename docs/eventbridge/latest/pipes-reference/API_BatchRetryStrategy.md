

# BatchRetryStrategy
<a name="API_BatchRetryStrategy"></a>

The retry strategy that's associated with a job. For more information, see [ Automated job retries](https://docs.aws.amazon.com/batch/latest/userguide/job_retries.html) in the * AWS Batch User Guide*.

## Contents
<a name="API_BatchRetryStrategy_Contents"></a>

 ** Attempts **   <a name="eventbridge-Type-BatchRetryStrategy-Attempts"></a>
The number of times to move a job to the `RUNNABLE` status. If the value of `attempts` is greater than one, the job is retried on failure the same number of attempts as the value.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 10.  
Required: No

## See Also
<a name="API_BatchRetryStrategy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pipes-2015-10-07/BatchRetryStrategy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pipes-2015-10-07/BatchRetryStrategy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pipes-2015-10-07/BatchRetryStrategy) 