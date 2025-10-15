# JobDescriptor

A container element for the job configuration and status information returned by a
 `Describe Job` request.


## Contents





**ConfirmationRequired** 


Indicates whether confirmation is required before Amazon S3 begins running the specified job.
 Confirmation is required only for jobs created through the Amazon S3 console.


Type: Boolean


Required: No




**CreationTime** 


A timestamp indicating when this job was created.


Type: Timestamp


Required: No




**Description** 


The description for this job, if one was provided in this job's `Create Job`
 request.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 256.


Required: No




**FailureReasons** 


If the specified job failed, this field contains information describing the
 failure.


Type: Array of [JobFailure](API_control_JobFailure.md "API_control_JobFailure.md") data types


Required: No




**GeneratedManifestDescriptor** 


The attribute of the JobDescriptor containing details about the job's generated
 manifest.


Type: [S3GeneratedManifestDescriptor](API_control_S3GeneratedManifestDescriptor.md "API_control_S3GeneratedManifestDescriptor.md") data type


Required: No




**JobArn** 


The Amazon Resource Name (ARN) for this job.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Pattern: `arn:[^:]+:s3:[a-zA-Z0-9\-]+:\d{12}:job\/.*`



Required: No




**JobId** 


The ID for the specified job.


Type: String


Length Constraints: Minimum length of 5. Maximum length of 36.


Pattern: `[a-zA-Z0-9\-\_]+`



Required: No




**Manifest** 


The configuration information for the specified job's manifest object.


Type: [JobManifest](API_control_JobManifest.md "API_control_JobManifest.md") data type


Required: No




**ManifestGenerator** 


The manifest generator that was used to generate a job manifest for this job.


Type: [JobManifestGenerator](API_control_JobManifestGenerator.md "API_control_JobManifestGenerator.md") data type



**Note:** This object is a Union. Only one member of this object can be specified or returned.


Required: No




**Operation** 


The operation that the specified job is configured to run on the objects listed in the
 manifest.


Type: [JobOperation](API_control_JobOperation.md "API_control_JobOperation.md") data type


Required: No




**Priority** 


The priority of the specified job.


Type: Integer


Valid Range: Minimum value of 0. Maximum value of 2147483647.


Required: No




**ProgressSummary** 


Describes the total number of tasks that the specified job has run, the number of tasks
 that succeeded, and the number of tasks that failed.


Type: [JobProgressSummary](API_control_JobProgressSummary.md "API_control_JobProgressSummary.md") data type


Required: No




**Report** 


Contains the configuration information for the job-completion report if you requested
 one in the `Create Job` request.


Type: [JobReport](API_control_JobReport.md "API_control_JobReport.md") data type


Required: No




**RoleArn** 


The Amazon Resource Name (ARN) for the AWS Identity and Access Management (IAM) role assigned to run the tasks
 for this job.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 2048.


Pattern: `arn:[^:]+:iam::\d{12}:role/.*`



Required: No




**Status** 


The current status of the specified job.


Type: String


Valid Values: `Active | Cancelled | Cancelling | Complete | Completing | Failed | Failing | New | Paused | Pausing | Preparing | Ready | Suspended`



Required: No




**StatusUpdateReason** 


The reason for updating the job.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 256.


Required: No




**SuspendedCause** 


The reason why the specified job was suspended. A job is only suspended if you create it
 through the Amazon S3 console. When you create the job, it enters the `Suspended`
 state to await confirmation before running. After you confirm the job, it automatically
 exits the `Suspended` state.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: No




**SuspendedDate** 


The timestamp when this job was suspended, if it has been suspended.


Type: Timestamp


Required: No




**TerminationDate** 


A timestamp indicating when this job terminated. A job's termination date is the date
 and time when it succeeded, failed, or was canceled.


Type: Timestamp


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/JobDescriptor "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/JobDescriptor")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/JobDescriptor "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/JobDescriptor")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/JobDescriptor "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/JobDescriptor")
