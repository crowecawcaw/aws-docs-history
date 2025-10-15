# UpdateJobStatus

Updates the status for the specified job. Use this operation to confirm that you want to
 run a job or to cancel an existing job. For more information, see [S3 Batch Operations](../userguide/batch-ops.md "../userguide/batch-ops.md") in the *Amazon S3 User Guide*.



Permissions

To use the `UpdateJobStatus` operation, you must have permission to
 perform the `s3:UpdateJobStatus` action.



Related actions include:


* [CreateJob](API_control_CreateJob.md "API_control_CreateJob.md")
* [ListJobs](API_control_ListJobs.md "API_control_ListJobs.md")
* [DescribeJob](API_control_DescribeJob.md "API_control_DescribeJob.md")
* [UpdateJobStatus](API_control_UpdateJobStatus.md "API_control_UpdateJobStatus.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
POST /v20180820/jobs/`id`/status?requestedJobStatus=`RequestedJobStatus`&statusUpdateReason=`StatusUpdateReason` HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: `AccountId`

```

## URI Request Parameters


The request uses the following URI parameters.





**[id](#API_control_UpdateJobStatus_RequestSyntax "#API_control_UpdateJobStatus_RequestSyntax")**


The ID of the job whose status you want to update.


Length Constraints: Minimum length of 5. Maximum length of 36.


Pattern: `[a-zA-Z0-9\-\_]+`



Required: Yes




**[requestedJobStatus](#API_control_UpdateJobStatus_RequestSyntax "#API_control_UpdateJobStatus_RequestSyntax")**


The status that you want to move the specified job to.


Valid Values: `Cancelled | Ready`



Required: Yes




**[statusUpdateReason](#API_control_UpdateJobStatus_RequestSyntax "#API_control_UpdateJobStatus_RequestSyntax")**


A description of the reason why you want to change the specified job's status. This
 field can be any string up to the maximum length.


Length Constraints: Minimum length of 1. Maximum length of 256.




**[x-amz-account-id](#API_control_UpdateJobStatus_RequestSyntax "#API_control_UpdateJobStatus_RequestSyntax")**


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
<[UpdateJobStatusResult](#AmazonS3-control_UpdateJobStatus-response-UpdateJobStatusResult "#AmazonS3-control_UpdateJobStatus-response-UpdateJobStatusResult")>
   <[JobId](#AmazonS3-control_UpdateJobStatus-response-JobId "#AmazonS3-control_UpdateJobStatus-response-JobId")>***string***</[JobId](#AmazonS3-control_UpdateJobStatus-response-JobId "#AmazonS3-control_UpdateJobStatus-response-JobId")>
   <[Status](#AmazonS3-control_UpdateJobStatus-response-Status "#AmazonS3-control_UpdateJobStatus-response-Status")>***string***</[Status](#AmazonS3-control_UpdateJobStatus-response-Status "#AmazonS3-control_UpdateJobStatus-response-Status")>
   <[StatusUpdateReason](#AmazonS3-control_UpdateJobStatus-response-StatusUpdateReason "#AmazonS3-control_UpdateJobStatus-response-StatusUpdateReason")>***string***</[StatusUpdateReason](#AmazonS3-control_UpdateJobStatus-response-StatusUpdateReason "#AmazonS3-control_UpdateJobStatus-response-StatusUpdateReason")>
</[UpdateJobStatusResult](#AmazonS3-control_UpdateJobStatus-response-UpdateJobStatusResult "#AmazonS3-control_UpdateJobStatus-response-UpdateJobStatusResult")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[UpdateJobStatusResult](#API_control_UpdateJobStatus_ResponseSyntax "#API_control_UpdateJobStatus_ResponseSyntax")**


Root level tag for the UpdateJobStatusResult parameters.


Required: Yes




**[JobId](#API_control_UpdateJobStatus_ResponseSyntax "#API_control_UpdateJobStatus_ResponseSyntax")**


The ID for the job whose status was updated.


Type: String


Length Constraints: Minimum length of 5. Maximum length of 36.


Pattern: `[a-zA-Z0-9\-\_]+`





**[Status](#API_control_UpdateJobStatus_ResponseSyntax "#API_control_UpdateJobStatus_ResponseSyntax")**


The current status for the specified job.


Type: String


Valid Values: `Active | Cancelled | Cancelling | Complete | Completing | Failed | Failing | New | Paused | Pausing | Preparing | Ready | Suspended`





**[StatusUpdateReason](#API_control_UpdateJobStatus_ResponseSyntax "#API_control_UpdateJobStatus_ResponseSyntax")**


The reason that the specified job's status was updated.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 256.




## Errors





**BadRequestException** 



HTTP Status Code: 400




**InternalServiceException** 



HTTP Status Code: 500




**JobStatusException** 



HTTP Status Code: 400




**NotFoundException** 



HTTP Status Code: 400




**TooManyRequestsException** 



HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/UpdateJobStatus "https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/UpdateJobStatus")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/UpdateJobStatus "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/UpdateJobStatus")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/UpdateJobStatus "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/UpdateJobStatus")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/UpdateJobStatus "https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/UpdateJobStatus")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/UpdateJobStatus "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/UpdateJobStatus")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/UpdateJobStatus "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/UpdateJobStatus")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/UpdateJobStatus "https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/UpdateJobStatus")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/UpdateJobStatus "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/UpdateJobStatus")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/UpdateJobStatus "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/UpdateJobStatus")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/UpdateJobStatus "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/UpdateJobStatus")
