# GetJobTagging

Returns the tags on an S3 Batch Operations job. 



Permissions

To use the `GetJobTagging` operation, you must have permission to
 perform the `s3:GetJobTagging` action. For more information, see [Controlling access and labeling jobs using tags](https://docs.aws.amazon.com/AmazonS3/latest/dev/batch-ops-managing-jobs.html#batch-ops-job-tags "https://docs.aws.amazon.com/AmazonS3/latest/dev/batch-ops-managing-jobs.html#batch-ops-job-tags") in the
 *Amazon S3 User Guide*.



Related actions include:


* [CreateJob](API_control_CreateJob.md "API_control_CreateJob.md")
* [PutJobTagging](API_control_PutJobTagging.md "API_control_PutJobTagging.md")
* [DeleteJobTagging](API_control_DeleteJobTagging.md "API_control_DeleteJobTagging.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
GET /v20180820/jobs/`id`/tagging HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: `AccountId`

```

## URI Request Parameters


The request uses the following URI parameters.





**[id](#API_control_GetJobTagging_RequestSyntax "#API_control_GetJobTagging_RequestSyntax")**


The ID for the S3 Batch Operations job whose tags you want to retrieve.


Length Constraints: Minimum length of 5. Maximum length of 36.


Pattern: `[a-zA-Z0-9\-\_]+`



Required: Yes




**[x-amz-account-id](#API_control_GetJobTagging_RequestSyntax "#API_control_GetJobTagging_RequestSyntax")**


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
<[GetJobTaggingResult](#AmazonS3-control_GetJobTagging-response-GetJobTaggingResult "#AmazonS3-control_GetJobTagging-response-GetJobTaggingResult")>
   <[Tags](#AmazonS3-control_GetJobTagging-response-Tags "#AmazonS3-control_GetJobTagging-response-Tags")>
      <S3Tag>
         <[Key](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key")>***string***</[Key](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key")>
         <[Value](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value")>***string***</[Value](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value")>
      </S3Tag>
   </[Tags](#AmazonS3-control_GetJobTagging-response-Tags "#AmazonS3-control_GetJobTagging-response-Tags")>
</[GetJobTaggingResult](#AmazonS3-control_GetJobTagging-response-GetJobTaggingResult "#AmazonS3-control_GetJobTagging-response-GetJobTaggingResult")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[GetJobTaggingResult](#API_control_GetJobTagging_ResponseSyntax "#API_control_GetJobTagging_ResponseSyntax")**


Root level tag for the GetJobTaggingResult parameters.


Required: Yes




**[Tags](#API_control_GetJobTagging_ResponseSyntax "#API_control_GetJobTagging_ResponseSyntax")**


The set of tags associated with the S3 Batch Operations job.


Type: Array of [S3Tag](API_control_S3Tag.md "API_control_S3Tag.md") data types




## Errors





**InternalServiceException** 



HTTP Status Code: 500




**NotFoundException** 



HTTP Status Code: 400




**TooManyRequestsException** 



HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/GetJobTagging "https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/GetJobTagging")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/GetJobTagging "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/GetJobTagging")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/GetJobTagging "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/GetJobTagging")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/GetJobTagging "https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/GetJobTagging")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/GetJobTagging "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/GetJobTagging")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/GetJobTagging "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/GetJobTagging")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/GetJobTagging "https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/GetJobTagging")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/GetJobTagging "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/GetJobTagging")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/GetJobTagging "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/GetJobTagging")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/GetJobTagging "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/GetJobTagging")
