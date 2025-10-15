# DeleteBucketInventoryConfiguration

###### Note

This operation is not supported for directory buckets.

Deletes an S3 Inventory configuration (identified by the inventory ID) from the bucket.

To use this operation, you must have permissions to perform the
 `s3:PutInventoryConfiguration` action. The bucket owner has this permission by default. The
 bucket owner can grant this permission to others. For more information about permissions, see [Permissions Related to Bucket Subresource Operations](../userguide/using-with-s3-actions.md#using-with-s3-actions-related-to-bucket-subresources "../userguide/using-with-s3-actions.md#using-with-s3-actions-related-to-bucket-subresources") and [Managing Access Permissions to Your Amazon S3
 Resources](../userguide/s3-access-control.md "../userguide/s3-access-control.md").

For information about the Amazon S3 inventory feature, see [Amazon S3 Inventory](https://docs.aws.amazon.com/AmazonS3/latest/dev/storage-inventory.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/storage-inventory.html").

Operations related to `DeleteBucketInventoryConfiguration` include: 


* [GetBucketInventoryConfiguration](API_GetBucketInventoryConfiguration.md "API_GetBucketInventoryConfiguration.md")
* [PutBucketInventoryConfiguration](API_PutBucketInventoryConfiguration.md "API_PutBucketInventoryConfiguration.md")
* [ListBucketInventoryConfigurations](API_ListBucketInventoryConfigurations.md "API_ListBucketInventoryConfigurations.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
DELETE /?inventory&id=`Id` HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
x-amz-expected-bucket-owner: `ExpectedBucketOwner`

```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_DeleteBucketInventoryConfiguration_RequestSyntax "#API_DeleteBucketInventoryConfiguration_RequestSyntax")**


The name of the bucket containing the inventory configuration to delete.


Required: Yes




**[id](#API_DeleteBucketInventoryConfiguration_RequestSyntax "#API_DeleteBucketInventoryConfiguration_RequestSyntax")**


The ID used to identify the inventory configuration.


Required: Yes




**[x-amz-expected-bucket-owner](#API_DeleteBucketInventoryConfiguration_RequestSyntax "#API_DeleteBucketInventoryConfiguration_RequestSyntax")**


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


### Sample Request


The following DELETE request deletes the inventory configuration with the ID
 `list1`.



```

        DELETE ?/inventory&id=list1 HTTP/1.1
        Host: amzn-s3-demo-bucket.s3.<Region>.amazonaws.com  
        Date: Wed, 14 May 2014 02:11:22 GMT
        Authorization: signatureValue 
     
```

### Sample Response


The following successful response shows Amazon S3 returning a `204 No Content` response.
 The inventory configuration with the ID `list1` for the bucket has been removed.



```

       HTTP/1.1 204 No Content
       x-amz-id-2: 0FmFIWsh/PpBuzZ0JFRC55ZGVmQW4SHJ7xVDqKwhEdJmf3q63RtrvH8ZuxW1Bol5
       x-amz-request-id: 0CF038E9BCF63097
       Date: Wed, 14 May 2014 02:11:22 GMT
       Server: AmazonS3
     
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/DeleteBucketInventoryConfiguration "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/DeleteBucketInventoryConfiguration")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/DeleteBucketInventoryConfiguration "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/DeleteBucketInventoryConfiguration")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/DeleteBucketInventoryConfiguration "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/DeleteBucketInventoryConfiguration")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/DeleteBucketInventoryConfiguration "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/DeleteBucketInventoryConfiguration")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/DeleteBucketInventoryConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/DeleteBucketInventoryConfiguration")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/DeleteBucketInventoryConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/DeleteBucketInventoryConfiguration")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/DeleteBucketInventoryConfiguration "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/DeleteBucketInventoryConfiguration")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/DeleteBucketInventoryConfiguration "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/DeleteBucketInventoryConfiguration")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/DeleteBucketInventoryConfiguration "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/DeleteBucketInventoryConfiguration")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/DeleteBucketInventoryConfiguration "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/DeleteBucketInventoryConfiguration")
