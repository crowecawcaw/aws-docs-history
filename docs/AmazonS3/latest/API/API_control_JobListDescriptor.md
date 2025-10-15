# JobListDescriptor

Contains the configuration and status information for a single job retrieved as part of
 a job list.


## Contents





**CreationTime** 


A timestamp indicating when the specified job was created.


Type: Timestamp


Required: No




**Description** 


The user-specified description that was included in the specified job's `Create
 Job` request.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 256.


Required: No




**JobId** 


The ID for the specified job.


Type: String


Length Constraints: Minimum length of 5. Maximum length of 36.


Pattern: `[a-zA-Z0-9\-\_]+`



Required: No




**Operation** 


The operation that the specified job is configured to run on every object listed in the
 manifest.


Type: String


Valid Values: `LambdaInvoke | S3PutObjectCopy | S3PutObjectAcl | S3PutObjectTagging | S3DeleteObjectTagging | S3InitiateRestoreObject | S3PutObjectLegalHold | S3PutObjectRetention | S3ReplicateObject | S3ComputeObjectChecksum`



Required: No




**Priority** 


The current priority for the specified job.


Type: Integer


Valid Range: Minimum value of 0. Maximum value of 2147483647.


Required: No




**ProgressSummary** 


Describes the total number of tasks that the specified job has run, the number of tasks
 that succeeded, and the number of tasks that failed.


Type: [JobProgressSummary](API_control_JobProgressSummary.md "API_control_JobProgressSummary.md") data type


Required: No




**Status** 


The specified job's current status.


Type: String


Valid Values: `Active | Cancelled | Cancelling | Complete | Completing | Failed | Failing | New | Paused | Pausing | Preparing | Ready | Suspended`



Required: No




**TerminationDate** 


A timestamp indicating when the specified job terminated. A job's termination date is
 the date and time when it succeeded, failed, or was canceled.


Type: Timestamp


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/JobListDescriptor "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/JobListDescriptor")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/JobListDescriptor "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/JobListDescriptor")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/JobListDescriptor "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/JobListDescriptor")
