# DeleteVectorBucketPolicy

###### Note

Amazon S3 Vectors is in preview release for Amazon S3 and is subject to change.

Deletes a vector bucket policy. To specify the bucket, you must use either the vector
 bucket name or the vector bucket Amazon Resource Name (ARN).



Permissions

You must have the `s3vectors:DeleteVectorBucketPolicy` permission to
 use this operation. 




## Request Syntax



```
POST /DeleteVectorBucketPolicy HTTP/1.1
Content-type: application/json

{
   "[vectorBucketArn](#AmazonS3-S3VectorBuckets_DeleteVectorBucketPolicy-request-vectorBucketArn "#AmazonS3-S3VectorBuckets_DeleteVectorBucketPolicy-request-vectorBucketArn")": "`string`",
   "[vectorBucketName](#AmazonS3-S3VectorBuckets_DeleteVectorBucketPolicy-request-vectorBucketName "#AmazonS3-S3VectorBuckets_DeleteVectorBucketPolicy-request-vectorBucketName")": "`string`"
}
```

## URI Request Parameters


The request does not use any URI parameters.


## Request Body


The request accepts the following data in JSON format.





**[vectorBucketArn](#API_S3VectorBuckets_DeleteVectorBucketPolicy_RequestSyntax "#API_S3VectorBuckets_DeleteVectorBucketPolicy_RequestSyntax")**


The ARN of the vector bucket to delete the policy from.


Type: String


Required: No




**[vectorBucketName](#API_S3VectorBuckets_DeleteVectorBucketPolicy_RequestSyntax "#API_S3VectorBuckets_DeleteVectorBucketPolicy_RequestSyntax")**


The name of the vector bucket to delete the policy from.


Type: String


Length Constraints: Minimum length of 3. Maximum length of 63.


Required: No




## Response Syntax



```
HTTP/1.1 200

```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.


## Errors





**AccessDeniedException** 


Access denied.


HTTP Status Code: 403




**InternalServerException** 


The request failed due to an internal server error.


HTTP Status Code: 500




**NotFoundException** 


The request was rejected because the specified resource can't be found.


HTTP Status Code: 404




**ServiceQuotaExceededException** 


Your request exceeds a service quota. 


HTTP Status Code: 402




**ServiceUnavailableException** 


The service is unavailable. Wait briefly and retry your request. If it continues to
 fail, increase your waiting time between retries.


HTTP Status Code: 503




**TooManyRequestsException** 


The request was denied due to request throttling.


HTTP Status Code: 429




**ValidationException** 


The requested action isn't valid.





**fieldList** 


A list of specific validation failures that are encountered during input processing. Each entry
 in the list contains a path to the field that failed validation and a detailed message that 
 explains why the validation failed. To satisfy multiple constraints, a field can appear multiple times in this list if it
 failed. You can use the information to identify and fix
 the specific validation issues in your request.




HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3vectors-2025-07-15/DeleteVectorBucketPolicy "https://docs.aws.amazon.com/goto/cli2/s3vectors-2025-07-15/DeleteVectorBucketPolicy")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3vectors-2025-07-15/DeleteVectorBucketPolicy "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3vectors-2025-07-15/DeleteVectorBucketPolicy")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3vectors-2025-07-15/DeleteVectorBucketPolicy "https://docs.aws.amazon.com/goto/SdkForCpp/s3vectors-2025-07-15/DeleteVectorBucketPolicy")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3vectors-2025-07-15/DeleteVectorBucketPolicy "https://docs.aws.amazon.com/goto/SdkForGoV2/s3vectors-2025-07-15/DeleteVectorBucketPolicy")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3vectors-2025-07-15/DeleteVectorBucketPolicy "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3vectors-2025-07-15/DeleteVectorBucketPolicy")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3vectors-2025-07-15/DeleteVectorBucketPolicy "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3vectors-2025-07-15/DeleteVectorBucketPolicy")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3vectors-2025-07-15/DeleteVectorBucketPolicy "https://docs.aws.amazon.com/goto/SdkForKotlin/s3vectors-2025-07-15/DeleteVectorBucketPolicy")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3vectors-2025-07-15/DeleteVectorBucketPolicy "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3vectors-2025-07-15/DeleteVectorBucketPolicy")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3vectors-2025-07-15/DeleteVectorBucketPolicy "https://docs.aws.amazon.com/goto/boto3/s3vectors-2025-07-15/DeleteVectorBucketPolicy")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3vectors-2025-07-15/DeleteVectorBucketPolicy "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3vectors-2025-07-15/DeleteVectorBucketPolicy")
