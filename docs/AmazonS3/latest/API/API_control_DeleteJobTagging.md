# DeleteJobTagging

Removes the entire tag set from the specified S3 Batch Operations job.



Permissions

To use the `DeleteJobTagging` operation, you must have permission to
 perform the `s3:DeleteJobTagging` action. For more information, see
 [Controlling access and labeling jobs using tags](https://docs.aws.amazon.com/AmazonS3/latest/dev/batch-ops-managing-jobs.html#batch-ops-job-tags "https://docs.aws.amazon.com/AmazonS3/latest/dev/batch-ops-managing-jobs.html#batch-ops-job-tags") in the
 *Amazon S3 User Guide*.



Related actions include:


* [CreateJob](API_control_CreateJob.md "API_control_CreateJob.md")
* [GetJobTagging](API_control_GetJobTagging.md "API_control_GetJobTagging.md")
* [PutJobTagging](API_control_PutJobTagging.md "API_control_PutJobTagging.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
DELETE /v20180820/jobs/`id`/tagging HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: `AccountId`

```

## URI Request Parameters


The request uses the following URI parameters.





**[id](#API_control_DeleteJobTagging_RequestSyntax "#API_control_DeleteJobTagging_RequestSyntax")**


The ID for the S3 Batch Operations job whose tags you want to delete.


Length Constraints: Minimum length of 5. Maximum length of 36.


Pattern: `[a-zA-Z0-9\-\_]+`



Required: Yes




**[x-amz-account-id](#API_control_DeleteJobTagging_RequestSyntax "#API_control_DeleteJobTagging_RequestSyntax")**


The AWS account ID associated with the S3 Batch Operations job.


Length Constraints: Maximum length of 64.


Pattern: `^\d{12}$`



Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200

```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.


## Errors





**InternalServiceException** 



HTTP Status Code: 500




**NotFoundException** 



HTTP Status Code: 400




**TooManyRequestsException** 



HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/DeleteJobTagging "https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/DeleteJobTagging")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/DeleteJobTagging "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/DeleteJobTagging")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/DeleteJobTagging "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/DeleteJobTagging")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/DeleteJobTagging "https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/DeleteJobTagging")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/DeleteJobTagging "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/DeleteJobTagging")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/DeleteJobTagging "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/DeleteJobTagging")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/DeleteJobTagging "https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/DeleteJobTagging")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/DeleteJobTagging "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/DeleteJobTagging")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/DeleteJobTagging "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/DeleteJobTagging")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/DeleteJobTagging "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/DeleteJobTagging")
