# JobReport

Contains the configuration parameters for a job-completion report.


## Contents





**Enabled** 


Indicates whether the specified job will generate a job-completion report.


Type: Boolean


Required: Yes




**Bucket** 


The Amazon Resource Name (ARN) for the bucket where specified job-completion report will
 be stored.


###### Note


**Directory buckets** - Directory buckets
 aren't supported as a location for Batch Operations to store job completion reports.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 128.


Pattern: `arn:[^:]+:s3:.*`



Required: No




**ExpectedBucketOwner** 


Lists the AWS account ID that owns the target bucket, where the completion report is received.


Type: String


Length Constraints: Maximum length of 64.


Pattern: `^\d{12}$`



Required: No




**Format** 


The format of the specified job-completion report.


Type: String


Valid Values: `Report_CSV_20180820`



Required: No




**Prefix** 


An optional prefix to describe where in the specified bucket the job-completion report
 will be stored. Amazon S3 stores the job-completion report at
 `<prefix>/job-<job-id>/report.json`.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 512.


Required: No




**ReportScope** 


Indicates whether the job-completion report will include details of all tasks or only
 failed tasks.


Type: String


Valid Values: `AllTasks | FailedTasksOnly`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/JobReport "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/JobReport")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/JobReport "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/JobReport")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/JobReport "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/JobReport")
