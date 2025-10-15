# PutJobTagging

Sets the supplied tag-set on an S3 Batch Operations job.

A tag is a key-value pair. You can associate S3 Batch Operations tags with any job by sending
 a PUT request against the tagging subresource that is associated with the job. To modify
 the existing tag set, you can either replace the existing tag set entirely, or make changes
 within the existing tag set by retrieving the existing tag set using [GetJobTagging](API_control_GetJobTagging.md "API_control_GetJobTagging.md"), modify that tag set, and use this operation to replace the tag
 set with the one you modified. For more information, see [Controlling
 access and labeling jobs using tags](https://docs.aws.amazon.com/AmazonS3/latest/dev/batch-ops-managing-jobs.html#batch-ops-job-tags "https://docs.aws.amazon.com/AmazonS3/latest/dev/batch-ops-managing-jobs.html#batch-ops-job-tags") in the *Amazon S3 User Guide*. 

###### Note


* If you send this request with an empty tag set, Amazon S3 deletes the existing
 tag set on the Batch Operations job. If you use this method, you are charged for a Tier
 1 Request (PUT). For more information, see [Amazon S3 pricing](http://aws.amazon.com/s3/pricing/ "http://aws.amazon.com/s3/pricing/").
* For deleting existing tags for your Batch Operations job, a [DeleteJobTagging](API_control_DeleteJobTagging.md "API_control_DeleteJobTagging.md") request is preferred because it achieves the same
 result without incurring charges.
* A few things to consider about using tags:




	+ Amazon S3 limits the maximum number of tags to 50 tags per job.
	+ You can associate up to 50 tags with a job as long as they have unique
	 tag keys.
	+ A tag key can be up to 128 Unicode characters in length, and tag values
	 can be up to 256 Unicode characters in length.
	+ The key and values are case sensitive.
	+ For tagging-related restrictions related to characters and encodings, see
	 [User-Defined Tag Restrictions](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/allocation-tag-restrictions.html "https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/allocation-tag-restrictions.html") in the *AWS Billing and Cost Management User Guide*.


Permissions

To use the `PutJobTagging` operation, you must have permission to
 perform the `s3:PutJobTagging` action.



Related actions include:


* [CreateJob](API_control_CreateJob.md "API_control_CreateJob.md")
* [GetJobTagging](API_control_GetJobTagging.md "API_control_GetJobTagging.md")
* [DeleteJobTagging](API_control_DeleteJobTagging.md "API_control_DeleteJobTagging.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
PUT /v20180820/jobs/`id`/tagging HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: `AccountId`
<?xml version="1.0" encoding="UTF-8"?>
<[PutJobTaggingRequest](#AmazonS3-control_PutJobTagging-request-PutJobTaggingRequest "#AmazonS3-control_PutJobTagging-request-PutJobTaggingRequest") xmlns="http://awss3control.amazonaws.com/doc/2018-08-20/">
   <[Tags](#AmazonS3-control_PutJobTagging-request-Tags "#AmazonS3-control_PutJobTagging-request-Tags")>
      <S3Tag>
         <[Key](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key")>`string`</[Key](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key")>
         <[Value](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value")>`string`</[Value](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value")>
      </S3Tag>
   </[Tags](#AmazonS3-control_PutJobTagging-request-Tags "#AmazonS3-control_PutJobTagging-request-Tags")>
</[PutJobTaggingRequest](#AmazonS3-control_PutJobTagging-request-PutJobTaggingRequest "#AmazonS3-control_PutJobTagging-request-PutJobTaggingRequest")>
```

## URI Request Parameters


The request uses the following URI parameters.





**[id](#API_control_PutJobTagging_RequestSyntax "#API_control_PutJobTagging_RequestSyntax")**


The ID for the S3 Batch Operations job whose tags you want to replace.


Length Constraints: Minimum length of 5. Maximum length of 36.


Pattern: `[a-zA-Z0-9\-\_]+`



Required: Yes




**[x-amz-account-id](#API_control_PutJobTagging_RequestSyntax "#API_control_PutJobTagging_RequestSyntax")**


The AWS account ID associated with the S3 Batch Operations job.


Length Constraints: Maximum length of 64.


Pattern: `^\d{12}$`



Required: Yes




## Request Body


The request accepts the following data in XML format.





**[PutJobTaggingRequest](#API_control_PutJobTagging_RequestSyntax "#API_control_PutJobTagging_RequestSyntax")**


Root level tag for the PutJobTaggingRequest parameters.


Required: Yes




**[Tags](#API_control_PutJobTagging_RequestSyntax "#API_control_PutJobTagging_RequestSyntax")**


The set of tags to associate with the S3 Batch Operations job.


Type: Array of [S3Tag](API_control_S3Tag.md "API_control_S3Tag.md") data types


Required: Yes




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




**TooManyTagsException** 


Amazon S3 throws this exception if you have too many tags in your tag set.


HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/PutJobTagging "https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/PutJobTagging")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/PutJobTagging "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/PutJobTagging")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/PutJobTagging "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/PutJobTagging")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/PutJobTagging "https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/PutJobTagging")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/PutJobTagging "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/PutJobTagging")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/PutJobTagging "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/PutJobTagging")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/PutJobTagging "https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/PutJobTagging")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/PutJobTagging "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/PutJobTagging")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/PutJobTagging "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/PutJobTagging")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/PutJobTagging "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/PutJobTagging")
