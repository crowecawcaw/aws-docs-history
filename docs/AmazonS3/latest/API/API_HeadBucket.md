# HeadBucket

You can use this operation to determine if a bucket exists and if you have permission to access it.
 The action returns a `200 OK` HTTP status code if the bucket exists and you have 
 permission to access it. You can make a `HeadBucket` call on any bucket name to any 
 Region in the partition, and regardless of the permissions on the bucket, you will receive a 
 response header with the correct bucket location so that you can then make a proper, signed request 
 to the appropriate Regional endpoint.

###### Note

If the bucket doesn't exist or you don't have permission to access it, the `HEAD` 
 request returns a generic `400 Bad Request`, `403 Forbidden`, or 
 `404 Not Found` HTTP status code. A message body isn't included, so you can't determine 
 the exception beyond these HTTP response codes.



Authentication and authorization


**General purpose buckets** - Request to public buckets that
 grant the s3:ListBucket permission publicly do not need to be signed. All other
 `HeadBucket` requests must be authenticated and signed by using IAM credentials
 (access key ID and secret access key for the IAM identities). All headers with the
 `x-amz-` prefix, including `x-amz-copy-source`, must be signed. For more
 information, see [REST Authentication](https://docs.aws.amazon.com/AmazonS3/latest/dev/RESTAuthentication.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/RESTAuthentication.html").



**Directory buckets** - You must use IAM credentials to
 authenticate and authorize your access to the `HeadBucket` API operation, instead of
 using the temporary security credentials through the `CreateSession` API
 operation.



 AWS CLI or SDKs handles authentication and authorization on your behalf.



Permissions



* **General purpose bucket permissions** - To use this
 operation, you must have permissions to perform the `s3:ListBucket` action. The
 bucket owner has this permission by default and can grant this permission to others. For more
 information about permissions, see [Managing access permissions to your
 Amazon S3 resources](../userguide/s3-access-control.md "../userguide/s3-access-control.md") in the *Amazon S3 User Guide*.
* **Directory bucket permissions** - You must have the
 **`s3express:CreateSession`** permission in the
 `Action` element of a policy. By default, the session is in the
 `ReadWrite` mode. If you want to restrict the access, you can explicitly set the
 `s3express:SessionMode` condition key to `ReadOnly` on the
 bucket.


For more information about example bucket policies, see [Example
 bucket policies for S3 Express One Zone](../userguide/s3-express-security-iam-example-bucket-policies.md "../userguide/s3-express-security-iam-example-bucket-policies.md") and [AWS
 Identity and Access Management (IAM) identity-based policies for S3 Express One Zone](../userguide/s3-express-security-iam-identity-policies.md "../userguide/s3-express-security-iam-identity-policies.md") in the
 *Amazon S3 User Guide*.


HTTP Host header syntax


**Directory buckets**  - The HTTP Host header syntax is `*Bucket-name*.s3express-*zone-id*.*region-code*.amazonaws.com`.


###### Note

You must make requests for this API operation to the Zonal endpoint. These endpoints support virtual-hosted-style requests in the format `https://*bucket-name*.s3express-*zone-id*.*region-code*.amazonaws.com`. Path-style requests are not supported. For more information about endpoints in Availability Zones, see [Regional and Zonal endpoints for directory buckets in Availability Zones](../userguide/endpoint-directory-buckets-AZ.md "../userguide/endpoint-directory-buckets-AZ.md") in the
 *Amazon S3 User Guide*. For more information about endpoints in Local Zones, see [Concepts for directory buckets in Local Zones](../userguide/s3-lzs-for-directory-buckets.md "../userguide/s3-lzs-for-directory-buckets.md") in the
 *Amazon S3 User Guide*.



###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
HEAD / HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
x-amz-expected-bucket-owner: `ExpectedBucketOwner`

```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_HeadBucket_RequestSyntax "#API_HeadBucket_RequestSyntax")**


The bucket name.



**Directory buckets** - When you use this operation with a directory bucket, you must use virtual-hosted-style requests in the format `*Bucket-name*.s3express-*zone-id*.*region-code*.amazonaws.com`. Path-style requests are not supported. Directory bucket names must be unique in the chosen Zone (Availability Zone or Local Zone). Bucket names must follow the format `*bucket-base-name*--*zone-id*--x-s3` (for example, `*amzn-s3-demo-bucket*--*usw2-az1*--x-s3`). For information about bucket naming
 restrictions, see [Directory bucket naming
 rules](../userguide/directory-bucket-naming-rules.md "../userguide/directory-bucket-naming-rules.md") in the *Amazon S3 User Guide*.



**Access points** - When you use this action with an access point for general purpose buckets, you must provide the alias of the access point in place of the bucket name or specify the access point ARN. When you use this action with an access point for directory buckets, you must provide the access point name in place of the bucket name. When using the access point ARN, you must direct requests to the access point hostname. The access point hostname takes the form *AccessPointName*-*AccountId*.s3-accesspoint.*Region*.amazonaws.com. When using this action with an access point through the AWS SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see [Using access points](../userguide/using-access-points.md "../userguide/using-access-points.md") in the *Amazon S3 User Guide*.



**Object Lambda access points** - When you use this API operation with an Object Lambda access point, provide the alias of the Object Lambda access point in place of the bucket name. 
If the Object Lambda access point alias in a request is not valid, the error code `InvalidAccessPointAliasError` is returned. 
For more information about `InvalidAccessPointAliasError`, see [List of
 Error Codes](ErrorResponses.md#ErrorCodeList "ErrorResponses.md#ErrorCodeList").


###### Note

Object Lambda access points are not supported by directory buckets.



**S3 on Outposts** - When you use this action with S3 on Outposts, you must direct requests to the S3 on Outposts hostname. The S3 on Outposts hostname takes the 
 form `*AccessPointName*-*AccountId*.*outpostID*.s3-outposts.*Region*.amazonaws.com`. When you use this action with S3 on Outposts, the destination bucket must be the Outposts access point ARN or the access point alias. For more information about S3 on Outposts, see [What is S3 on Outposts?](../userguide/S3onOutposts.md "../userguide/S3onOutposts.md") in the *Amazon S3 User Guide*.


Required: Yes




**[x-amz-expected-bucket-owner](#API_HeadBucket_RequestSyntax "#API_HeadBucket_RequestSyntax")**


The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
x-amz-bucket-arn: `BucketArn`
x-amz-bucket-location-type: `BucketLocationType`
x-amz-bucket-location-name: `BucketLocationName`
x-amz-bucket-region: `BucketRegion`
x-amz-access-point-alias: `AccessPointAlias`

```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The response returns the following HTTP headers.





**[x-amz-access-point-alias](#API_HeadBucket_ResponseSyntax "#API_HeadBucket_ResponseSyntax")**


Indicates whether the bucket name used in the request is an access point alias.


###### Note

For directory buckets, the value of this field is `false`.




**[x-amz-bucket-arn](#API_HeadBucket_ResponseSyntax "#API_HeadBucket_ResponseSyntax")**


The Amazon Resource Name (ARN) of the S3 bucket. ARNs uniquely identify AWS resources across all
 of AWS.


###### Note

This parameter is only supported for S3 directory buckets. For more information, see [Using tags with
 directory buckets](../userguide/directory-buckets-tagging.md "../userguide/directory-buckets-tagging.md").


Length Constraints: Minimum length of 1. Maximum length of 128.


Pattern: `arn:[^:]+:(s3|s3express):.*`





**[x-amz-bucket-location-name](#API_HeadBucket_ResponseSyntax "#API_HeadBucket_ResponseSyntax")**


The name of the location where the bucket will be created.


For directory buckets, the Zone ID of the Availability Zone or the Local Zone where the bucket is created. An example
 Zone ID value for an Availability Zone is `usw2-az1`.


###### Note

This functionality is only supported by directory buckets.




**[x-amz-bucket-location-type](#API_HeadBucket_ResponseSyntax "#API_HeadBucket_ResponseSyntax")**


The type of location where the bucket is created.


###### Note

This functionality is only supported by directory buckets.


Valid Values: `AvailabilityZone | LocalZone`





**[x-amz-bucket-region](#API_HeadBucket_ResponseSyntax "#API_HeadBucket_ResponseSyntax")**


The Region that the bucket is located.


Length Constraints: Minimum length of 0. Maximum length of 20.




## Errors





**NoSuchBucket** 


The specified bucket does not exist.


HTTP Status Code: 404




## Examples


### Sample Request for general purpose buckets


This example illustrates one usage of HeadBucket.



```

            HEAD / HTTP/1.1
            Date: Fri, 10 Feb 2012 21:34:55 GMT
            Authorization: authorization string
            Host: myawsbucket.s3.amazonaws.com
            Connection: Keep-Alive
         
```

### Sample responses for general purpose buckets


This example illustrates one usage of HeadBucket.



```

            HTTP/1.1 200 OK
            x-amz-id-2: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
            x-amz-request-id: 28PG2CEB32F5EE25
            x-amz-bucket-region: us-west-2
            x-amz-access-point-alias: false
            Date: Fri, 10 2012 21:34:56 GMT
            Server: AmazonS3
         
```


```

            HTTP/1.1 301 Moved Permanantly
            x-amz-id-2: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
            x-amz-request-id: M8H3G2AJ0V6NQ8AJ 
            Date: Tue, 06 May 2025 21:29:41 GMT 
            x-amz-bucket-region: us-east-1 
            x-amz-access-point-alias: false
            Server: AmazonS3
            
```


```

            HTTP/1.1 403 Forbidden
            x-amz-bucket-region: us-east-1
            x-amz-request-id: P6K9QSW8EN5YEPS 
            x-amz-id-2: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
            Date: Tue, 06 May 2025 21:24:51 GMT
            Server: AmazonS3
            
```

### Example of anonymous request response


This example illustrates one usage of HeadBucket.



```

            HTTP/1.1 403 Forbidden
            x-amz-bucket-region: us-east-1 
            x-amz-request-id: 7B3WF90PGN6J8F2 
            x-amz-id-2: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
            Date: Tue, 06 May 2025 21:55:02 
            GMT Server: AmazonS3
            
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/HeadBucket "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/HeadBucket")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/HeadBucket "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/HeadBucket")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/HeadBucket "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/HeadBucket")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/HeadBucket "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/HeadBucket")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/HeadBucket "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/HeadBucket")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/HeadBucket "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/HeadBucket")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/HeadBucket "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/HeadBucket")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/HeadBucket "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/HeadBucket")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/HeadBucket "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/HeadBucket")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/HeadBucket "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/HeadBucket")
