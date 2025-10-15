# DeleteBucketOwnershipControls

###### Note

This operation is not supported for directory buckets.

Removes `OwnershipControls` for an Amazon S3 bucket. To use this operation, you must have the
 `s3:PutBucketOwnershipControls` permission. For more information about Amazon S3 permissions,
 see [Specifying
 Permissions in a Policy](https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html").

For information about Amazon S3 Object Ownership, see [Using Object Ownership](https://docs.aws.amazon.com/AmazonS3/latest/dev/about-object-ownership.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/about-object-ownership.html"). 

The following operations are related to `DeleteBucketOwnershipControls`:


* [GetBucketOwnershipControls](API_GetBucketOwnershipControls.md "API_GetBucketOwnershipControls.md")
* [PutBucketOwnershipControls](API_PutBucketOwnershipControls.md "API_PutBucketOwnershipControls.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
DELETE /?ownershipControls HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
x-amz-expected-bucket-owner: `ExpectedBucketOwner`

```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_DeleteBucketOwnershipControls_RequestSyntax "#API_DeleteBucketOwnershipControls_RequestSyntax")**


The Amazon S3 bucket whose `OwnershipControls` you want to delete. 


Required: Yes




**[x-amz-expected-bucket-owner](#API_DeleteBucketOwnershipControls_RequestSyntax "#API_DeleteBucketOwnershipControls_RequestSyntax")**


The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 204

```

## Response Elements


If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.


## Examples


### Sample DeleteBucketOwnershipControls Request


This example illustrates one usage of DeleteBucketOwnershipControls.



```

          DELETE /example-bucket?/ownershipControls HTTP/1.1
          Host: examplebucket.s3.<Region>.amazonaws.com
          Date: Thu, 18 Jun 2017 00:17:22 GMT
          Authorization: signatureValue;
        
```

### Sample DeleteBucketOwnershipControls Response


This example illustrates one usage of DeleteBucketOwnershipControls.



```

          HTTP/1.1 204 No Content
          x-amz-id-2: dVrxJD3XHDcjZHFtd7eSB+ovpY8hQ6kSe9jPzyRVkWp27cij05qV1pTIvz/hjlsrupiy9gEkSdw=
          x-amz-request-id: 4BFC0B777B448C97
          Date: Thu, 18 Jun 2020 22:54:03 GMT
          Server: AmazonS3
        
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/DeleteBucketOwnershipControls "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/DeleteBucketOwnershipControls")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/DeleteBucketOwnershipControls "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/DeleteBucketOwnershipControls")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/DeleteBucketOwnershipControls "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/DeleteBucketOwnershipControls")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/DeleteBucketOwnershipControls "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/DeleteBucketOwnershipControls")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/DeleteBucketOwnershipControls "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/DeleteBucketOwnershipControls")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/DeleteBucketOwnershipControls "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/DeleteBucketOwnershipControls")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/DeleteBucketOwnershipControls "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/DeleteBucketOwnershipControls")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/DeleteBucketOwnershipControls "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/DeleteBucketOwnershipControls")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/DeleteBucketOwnershipControls "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/DeleteBucketOwnershipControls")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/DeleteBucketOwnershipControls "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/DeleteBucketOwnershipControls")
