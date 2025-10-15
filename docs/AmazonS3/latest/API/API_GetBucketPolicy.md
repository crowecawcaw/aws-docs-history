# GetBucketPolicy

Returns the policy of a specified bucket.

###### Note


**Directory buckets**  - For directory buckets, you must make requests for this API operation to the Regional endpoint. These endpoints support path-style requests in the format `https://s3express-control.*region-code*.amazonaws.com/*bucket-name*`. Virtual-hosted-style requests aren't supported. 
For more information about endpoints in Availability Zones, see [Regional and Zonal endpoints for directory buckets in Availability Zones](../userguide/endpoint-directory-buckets-AZ.md "../userguide/endpoint-directory-buckets-AZ.md") in the
 *Amazon S3 User Guide*. For more information about endpoints in Local Zones, see [Concepts for directory buckets in Local Zones](../userguide/s3-lzs-for-directory-buckets.md "../userguide/s3-lzs-for-directory-buckets.md") in the
 *Amazon S3 User Guide*.



Permissions

If you are using an identity other than the root user of the AWS account that owns the
 bucket, the calling identity must both have the `GetBucketPolicy` permissions on the
 specified bucket and belong to the bucket owner's account in order to use this operation.


If you don't have `GetBucketPolicy` permissions, Amazon S3 returns a `403 Access
 Denied` error. If you have the correct permissions, but you're not using an identity that
 belongs to the bucket owner's account, Amazon S3 returns a `405 Method Not Allowed`
 error.


###### Important

To ensure that bucket owners don't inadvertently lock themselves out of their own buckets,
 the root principal in a bucket owner's AWS account can perform the
 `GetBucketPolicy`, `PutBucketPolicy`, and
 `DeleteBucketPolicy` API actions, even if their bucket policy explicitly denies the
 root principal's access. Bucket owner root principals can only be blocked from performing these
 API actions by VPC endpoint policies and AWS Organizations policies.



* **General purpose bucket permissions** - The
 `s3:GetBucketPolicy` permission is required in a policy. For more information
 about general purpose buckets bucket policies, see [Using Bucket Policies and User
 Policies](https://docs.aws.amazon.com/AmazonS3/latest/dev/using-iam-policies.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/using-iam-policies.html") in the *Amazon S3 User Guide*.
* **Directory bucket permissions** - To grant access to
 this API operation, you must have the `s3express:GetBucketPolicy` permission in
 an IAM identity-based policy instead of a bucket policy. Cross-account access to this API operation isn't supported. This operation can only be performed by the AWS account that owns the resource.
 For more information about directory bucket policies and permissions, see [AWS Identity and Access Management (IAM) for S3 Express One Zone](../userguide/s3-express-security-iam.md "../userguide/s3-express-security-iam.md") in the *Amazon S3 User Guide*.


Example bucket policies


**General purpose buckets example bucket policies** - See [Bucket policy
 examples](../userguide/example-bucket-policies.md "../userguide/example-bucket-policies.md") in the *Amazon S3 User Guide*.



**Directory bucket example bucket policies** - See [Example
 bucket policies for S3 Express One Zone](../userguide/s3-express-security-iam-example-bucket-policies.md "../userguide/s3-express-security-iam-example-bucket-policies.md") in the *Amazon S3 User Guide*.



HTTP Host header syntax


**Directory buckets**  - The HTTP Host header syntax is `s3express-control.*region-code*.amazonaws.com`.



The following action is related to `GetBucketPolicy`:


* [GetObject](API_GetObject.md "API_GetObject.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
GET /?policy HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
x-amz-expected-bucket-owner: `ExpectedBucketOwner`

```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_GetBucketPolicy_RequestSyntax "#API_GetBucketPolicy_RequestSyntax")**


The bucket name to get the bucket policy for.



**Directory buckets**  - When you use this operation with a directory bucket, you must use path-style requests in the format `https://s3express-control.*region-code*.amazonaws.com/*bucket-name*`. Virtual-hosted-style requests aren't supported. Directory bucket names must be unique in the chosen Zone (Availability Zone or Local Zone). Bucket names must also follow the format `*bucket-base-name*--*zone-id*--x-s3` (for example, `*DOC-EXAMPLE-BUCKET*--*usw2-az1*--x-s3`). For information about bucket naming restrictions, see [Directory bucket naming rules](../userguide/directory-bucket-naming-rules.md "../userguide/directory-bucket-naming-rules.md") in the *Amazon S3 User Guide*




**Access points** - When you use this API operation with an access point, provide the alias of the access point in place of the bucket name.



**Object Lambda access points** - When you use this API operation with an Object Lambda access point, provide the alias of the Object Lambda access point in place of the bucket name. 
If the Object Lambda access point alias in a request is not valid, the error code `InvalidAccessPointAliasError` is returned. 
For more information about `InvalidAccessPointAliasError`, see [List of
 Error Codes](ErrorResponses.md#ErrorCodeList "ErrorResponses.md#ErrorCodeList").


###### Note

Object Lambda access points are not supported by directory buckets.


Required: Yes




**[x-amz-expected-bucket-owner](#API_GetBucketPolicy_RequestSyntax "#API_GetBucketPolicy_RequestSyntax")**


The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).


###### Note

For directory buckets, this header is not supported in this API operation. If you specify this header, the request fails with the HTTP status code 
`501 Not Implemented`.




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200

{ `Policy` *in JSON format* }
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.



**[Policy](#API_GetBucketPolicy_ResponseSyntax "#API_GetBucketPolicy_ResponseSyntax")**


## Examples


### Sample Request for general purpose buckets


The following request returns the policy of the specified bucket.



```

           GET ?policy HTTP/1.1
           Host: amzn-s3-demo-bucket.s3.<Region>.amazonaws.com
           Date: Wed, 28 Oct 2009 22:32:00 GMT
           Authorization: authorization string
         
```

### Sample Response for general purpose buckets


This example illustrates one usage of GetBucketPolicy.



```

            HTTP/1.1 200 OK  
            x-amz-id-2: Uuag1LuByru9pO4SAMPLEAtRPfTaOFg==  
            x-amz-request-id: 656c76696e67SAMPLE57374  
            Date: Tue, 04 Apr 2010 20:34:56 GMT  
            Connection: keep-alive  
            Server: AmazonS3    


            {
            "Version":"2008-10-17",		 	 	 
            "Id":"aaaa-bbbb-cccc-dddd",
            "Statement" : [
                {
                    "Effect":"Deny",
                    "Sid":"1", 
                    "Principal" : {
                       "AWS":["111122223333","444455556666"]
                    },
                    "Action":["s3:*"],
                    "Resource":"arn:aws:s3:::bucket/*"
                }
             ] 
            }
         
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetBucketPolicy "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetBucketPolicy")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/GetBucketPolicy "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/GetBucketPolicy")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetBucketPolicy "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetBucketPolicy")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetBucketPolicy "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetBucketPolicy")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetBucketPolicy "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetBucketPolicy")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetBucketPolicy "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetBucketPolicy")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetBucketPolicy "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetBucketPolicy")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetBucketPolicy "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetBucketPolicy")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetBucketPolicy "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetBucketPolicy")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetBucketPolicy "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetBucketPolicy")
