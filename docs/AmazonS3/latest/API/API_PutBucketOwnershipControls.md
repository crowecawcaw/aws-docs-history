# PutBucketOwnershipControls

###### Note

This operation is not supported for directory buckets.

Creates or modifies `OwnershipControls` for an Amazon S3 bucket. To use this operation, you
 must have the `s3:PutBucketOwnershipControls` permission. For more information about Amazon S3
 permissions, see [Specifying permissions in a policy](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/using-with-s3-actions.html "https://docs.aws.amazon.com/AmazonS3/latest/user-guide/using-with-s3-actions.html"). 

For information about Amazon S3 Object Ownership, see [Using object ownership](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/about-object-ownership.html "https://docs.aws.amazon.com/AmazonS3/latest/user-guide/about-object-ownership.html"). 

The following operations are related to `PutBucketOwnershipControls`:


* [GetBucketOwnershipControls](API_GetBucketOwnershipControls.md "API_GetBucketOwnershipControls.md")
* [DeleteBucketOwnershipControls](API_DeleteBucketOwnershipControls.md "API_DeleteBucketOwnershipControls.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
PUT /?ownershipControls HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
Content-MD5: `ContentMD5`
x-amz-expected-bucket-owner: `ExpectedBucketOwner`
x-amz-sdk-checksum-algorithm: `ChecksumAlgorithm`
<?xml version="1.0" encoding="UTF-8"?>
<[OwnershipControls](#AmazonS3-PutBucketOwnershipControls-request-OwnershipControls "#AmazonS3-PutBucketOwnershipControls-request-OwnershipControls") xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
   <[Rule](#AmazonS3-PutBucketOwnershipControls-request-Rules "#AmazonS3-PutBucketOwnershipControls-request-Rules")>
      <[ObjectOwnership](API_OwnershipControlsRule.md#AmazonS3-Type-OwnershipControlsRule-ObjectOwnership "API_OwnershipControlsRule.md#AmazonS3-Type-OwnershipControlsRule-ObjectOwnership")>`string`</[ObjectOwnership](API_OwnershipControlsRule.md#AmazonS3-Type-OwnershipControlsRule-ObjectOwnership "API_OwnershipControlsRule.md#AmazonS3-Type-OwnershipControlsRule-ObjectOwnership")>
   </[Rule](#AmazonS3-PutBucketOwnershipControls-request-Rules "#AmazonS3-PutBucketOwnershipControls-request-Rules")>
   ...
</[OwnershipControls](#AmazonS3-PutBucketOwnershipControls-request-OwnershipControls "#AmazonS3-PutBucketOwnershipControls-request-OwnershipControls")>
```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_PutBucketOwnershipControls_RequestSyntax "#API_PutBucketOwnershipControls_RequestSyntax")**


The name of the Amazon S3 bucket whose `OwnershipControls` you want to set.


Required: Yes




**[Content-MD5](#API_PutBucketOwnershipControls_RequestSyntax "#API_PutBucketOwnershipControls_RequestSyntax")**


The MD5 hash of the `OwnershipControls` request body. 


For requests made using the AWS Command Line Interface (CLI) or AWS SDKs, this field is calculated automatically.




**[x-amz-expected-bucket-owner](#API_PutBucketOwnershipControls_RequestSyntax "#API_PutBucketOwnershipControls_RequestSyntax")**


The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).




**[x-amz-sdk-checksum-algorithm](#API_PutBucketOwnershipControls_RequestSyntax "#API_PutBucketOwnershipControls_RequestSyntax")**


 Indicates the algorithm used to create the checksum for the object when you use the SDK. This
 header will not provide any additional functionality if you don't use the SDK. When you send this
 header, there must be a corresponding `x-amz-checksum-*algorithm*` header
 sent. Otherwise, Amazon S3 fails the request with the HTTP status code `400 Bad Request`. For more
 information, see [Checking object integrity](../userguide/checking-object-integrity.md "../userguide/checking-object-integrity.md") in
 the *Amazon S3 User Guide*.


If you provide an individual checksum, Amazon S3 ignores any provided `ChecksumAlgorithm`
 parameter. 


Valid Values: `CRC32 | CRC32C | SHA1 | SHA256 | CRC64NVME`





## Request Body


The request accepts the following data in XML format.





**[OwnershipControls](#API_PutBucketOwnershipControls_RequestSyntax "#API_PutBucketOwnershipControls_RequestSyntax")**


Root level tag for the OwnershipControls parameters.


Required: Yes




**[Rule](#API_PutBucketOwnershipControls_RequestSyntax "#API_PutBucketOwnershipControls_RequestSyntax")**


The container element for an ownership control rule.


Type: Array of [OwnershipControlsRule](API_OwnershipControlsRule.md "API_OwnershipControlsRule.md") data types


Required: Yes




## Response Syntax



```
HTTP/1.1 200

```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.


## Examples


### Sample Request with BucketOwnerEnforced OwnershipControls


The following request puts a bucket `OwnershipControls` that specifies
 BucketOwnerEnforced.



```

          PUT /amzn-s3-demo-bucket?ownershipControls= HTTP/1.1
          Host:amzn-s3-demo-bucket.s3.<Region>.amazonaws.com
          x-amz-date: 20211130T230132Z
          x-amz-content-sha256: bafb46c18574a73704c8227aef060df1c12ea0d964e19b949d06e9f763805fe2
          Authorization: authorization string

          <?xml version="1.0" encoding="UTF-8"?>
          <OwnershipControls xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
            <Rule>
              <ObjectOwnership>BucketOwnerEnforced</ObjectOwnership>
            </Rule>
          </OwnershipControls>
        
```

### Sample Response with BucketOwnerEnforced OwnershipControls


This example illustrates one usage of PutBucketOwnershipControls.



```

          HTTP/1.1 200 OK
          x-amz-id-2: zkDVX0gbz8oKcjNz7GPz8XhXkhNArHtA8/WOf5hyEj6SbisSRdqITZvSuAMik7HK4PY+izDZZI0=
          x-amz-request-id: BK7Y8M3G7Z0RFRCP
          Date: Tue, 30 Nov 2021 23:01:33 GMT
          Content-Length: 0
          Server: AmazonS3
        
```

### Sample Request with BucketOwnerPreferred OwnershipControls


The following request puts a bucket `OwnershipControls` that specifies
 BucketOwnerPreferred.



```

          PUT /amzn-s3-demo-bucket?ownershipControls= HTTP/1.1
          Host:amzn-s3-demo-bucket.s3.<Region>.amazonaws.com
          x-amz-date: 20200618T230132Z
          x-amz-content-sha256: bafb46c18574a73704c8227aef060df1c12ea0d964e19b949d06e9f763805fe2
          Authorization: authorization string

          <?xml version="1.0" encoding="UTF-8"?>
          <OwnershipControls xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
            <Rule>
              <ObjectOwnership>BucketOwnerPreferred</ObjectOwnership>
            </Rule>
          </OwnershipControls>
        
```

### Sample Response with BucketOwnerPreferred OwnershipControls


This example illustrates one usage of PutBucketOwnershipControls.



```

          HTTP/1.1 200 OK
          x-amz-id-2: zkDVX0gbz8oKcjNz7GPz8XhXkhNArHtA8/WOf5hyEj6SbisSRdqITZvSuAMik7HK4PY+izDZZI0=
          x-amz-request-id: BK7Y8M3G7Z0RFRCP
          Date: Thu, 18 Jun 2020 23:01:33 GMT
          Content-Length: 0
          Server: AmazonS3
        
```

### Sample Request with ObjectWriter OwnershipControls


The following request puts a bucket `OwnershipControls` that specifies
 ObjectWriter.



```

          PUT /amzn-s3-demo-bucket?ownershipControls= HTTP/1.1
          Host:amzn-s3-demo-bucket.s3.<Region>.amazonaws.com
          x-amz-date: 20200618T230132Z
          x-amz-content-sha256: bafb46c18574a73704c8227aef060df1c12ea0d964e19b949d06e9f763805fe2
          Authorization: authorization string

          <?xml version="1.0" encoding="UTF-8"?>
          <OwnershipControls xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
            <Rule>
              <ObjectOwnership>ObjectWriter</ObjectOwnership>
            </Rule>
          </OwnershipControls>
        
```

### Sample Response with ObjectWriter OwnershipControls


This example illustrates one usage of PutBucketOwnershipControls.



```

          HTTP/1.1 200 OK
          x-amz-id-2: zkDVX0gbz8oKcjNz7GPz8XhXkhNArHtA8/WOf5hyEj6SbisSRdqITZvSuAMik7HK4PY+izDZZI0=
          x-amz-request-id: BK7Y8M3G7Z0RFRCP
          Date: Thu, 18 Jun 2020 23:01:33 GMT
          Content-Length: 0
          Server: AmazonS3
        
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/PutBucketOwnershipControls "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/PutBucketOwnershipControls")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/PutBucketOwnershipControls "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/PutBucketOwnershipControls")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/PutBucketOwnershipControls "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/PutBucketOwnershipControls")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/PutBucketOwnershipControls "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/PutBucketOwnershipControls")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/PutBucketOwnershipControls "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/PutBucketOwnershipControls")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/PutBucketOwnershipControls "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/PutBucketOwnershipControls")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/PutBucketOwnershipControls "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/PutBucketOwnershipControls")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/PutBucketOwnershipControls "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/PutBucketOwnershipControls")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/PutBucketOwnershipControls "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/PutBucketOwnershipControls")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/PutBucketOwnershipControls "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/PutBucketOwnershipControls")
