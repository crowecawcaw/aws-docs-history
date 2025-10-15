# UpdateJobPriority

Updates an existing S3 Batch Operations job's priority. For more information, see [S3 Batch Operations](../userguide/batch-ops.md "../userguide/batch-ops.md") in the *Amazon S3 User Guide*.



Permissions

To use the `UpdateJobPriority` operation, you must have permission
 to perform the `s3:UpdateJobPriority` action.



Related actions include:


* [CreateJob](API_control_CreateJob.md "API_control_CreateJob.md")
* [ListJobs](API_control_ListJobs.md "API_control_ListJobs.md")
* [DescribeJob](API_control_DescribeJob.md "API_control_DescribeJob.md")
* [UpdateJobStatus](API_control_UpdateJobStatus.md "API_control_UpdateJobStatus.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
POST /v20180820/jobs/`id`/priority?priority=`Priority` HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: `AccountId`

```

## URI Request Parameters


The request uses the following URI parameters.





**[id](#API_control_UpdateJobPriority_RequestSyntax "#API_control_UpdateJobPriority_RequestSyntax")**


The ID for the job whose priority you want to update.


Length Constraints: Minimum length of 5. Maximum length of 36.


Pattern: `[a-zA-Z0-9\-\_]+`



Required: Yes




**[priority](#API_control_UpdateJobPriority_RequestSyntax "#API_control_UpdateJobPriority_RequestSyntax")**


The priority you want to assign to this job.


Valid Range: Minimum value of 0. Maximum value of 2147483647.


Required: Yes




**[x-amz-account-id](#API_control_UpdateJobPriority_RequestSyntax "#API_control_UpdateJobPriority_RequestSyntax")**


The AWS account ID associated with the S3 Batch Operations job.


Length Constraints: Maximum length of 64.


Pattern: `^\d{12}$`



Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<[UpdateJobPriorityResult](#AmazonS3-control_UpdateJobPriority-response-UpdateJobPriorityResult "#AmazonS3-control_UpdateJobPriority-response-UpdateJobPriorityResult")>
   <[JobId](#AmazonS3-control_UpdateJobPriority-response-JobId "#AmazonS3-control_UpdateJobPriority-response-JobId")>***string***</[JobId](#AmazonS3-control_UpdateJobPriority-response-JobId "#AmazonS3-control_UpdateJobPriority-response-JobId")>
   <[Priority](#AmazonS3-control_UpdateJobPriority-response-Priority "#AmazonS3-control_UpdateJobPriority-response-Priority")>***integer***</[Priority](#AmazonS3-control_UpdateJobPriority-response-Priority "#AmazonS3-control_UpdateJobPriority-response-Priority")>
</[UpdateJobPriorityResult](#AmazonS3-control_UpdateJobPriority-response-UpdateJobPriorityResult "#AmazonS3-control_UpdateJobPriority-response-UpdateJobPriorityResult")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[UpdateJobPriorityResult](#API_control_UpdateJobPriority_ResponseSyntax "#API_control_UpdateJobPriority_ResponseSyntax")**


Root level tag for the UpdateJobPriorityResult parameters.


Required: Yes




**[JobId](#API_control_UpdateJobPriority_ResponseSyntax "#API_control_UpdateJobPriority_ResponseSyntax")**


The ID for the job whose priority Amazon S3 updated.


Type: String


Length Constraints: Minimum length of 5. Maximum length of 36.


Pattern: `[a-zA-Z0-9\-\_]+`





**[Priority](#API_control_UpdateJobPriority_ResponseSyntax "#API_control_UpdateJobPriority_ResponseSyntax")**


The new priority assigned to the specified job.


Type: Integer


Valid Range: Minimum value of 0. Maximum value of 2147483647.




## Errors





**BadRequestException** 



HTTP Status Code: 400




**InternalServiceException** 



HTTP Status Code: 500




**NotFoundException** 



HTTP Status Code: 400




**TooManyRequestsException** 



HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/UpdateJobPriority "https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/UpdateJobPriority")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/UpdateJobPriority "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/UpdateJobPriority")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/UpdateJobPriority "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/UpdateJobPriority")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/UpdateJobPriority "https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/UpdateJobPriority")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/UpdateJobPriority "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/UpdateJobPriority")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/UpdateJobPriority "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/UpdateJobPriority")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/UpdateJobPriority "https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/UpdateJobPriority")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/UpdateJobPriority "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/UpdateJobPriority")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/UpdateJobPriority "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/UpdateJobPriority")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/UpdateJobPriority "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/UpdateJobPriority")
