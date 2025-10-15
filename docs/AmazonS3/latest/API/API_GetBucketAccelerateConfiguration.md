# GetBucketAccelerateConfiguration

###### Note

This operation is not supported for directory buckets.

This implementation of the GET action uses the `accelerate` subresource to return the
 Transfer Acceleration state of a bucket, which is either `Enabled` or `Suspended`.
 Amazon S3 Transfer Acceleration is a bucket-level feature that enables you to perform faster data transfers
 to and from Amazon S3.

To use this operation, you must have permission to perform the
 `s3:GetAccelerateConfiguration` action. The bucket owner has this permission by default.
 The bucket owner can grant this permission to others. For more information about permissions, see [Permissions Related to Bucket Subresource Operations](../userguide/using-with-s3-actions.md#using-with-s3-actions-related-to-bucket-subresources "../userguide/using-with-s3-actions.md#using-with-s3-actions-related-to-bucket-subresources") and [Managing Access Permissions to your Amazon S3
 Resources](../userguide/s3-access-control.md "../userguide/s3-access-control.md") in the *Amazon S3 User Guide*.

You set the Transfer Acceleration state of an existing bucket to `Enabled` or
 `Suspended` by using the [PutBucketAccelerateConfiguration](API_PutBucketAccelerateConfiguration.md "API_PutBucketAccelerateConfiguration.md") operation. 

A GET `accelerate` request does not return a state value for a bucket that has no
 transfer acceleration state. A bucket has no Transfer Acceleration state if a state has never been set
 on the bucket. 

For more information about transfer acceleration, see [Transfer Acceleration](https://docs.aws.amazon.com/AmazonS3/latest/dev/transfer-acceleration.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/transfer-acceleration.html") in the
 Amazon S3 User Guide.

The following operations are related to `GetBucketAccelerateConfiguration`:


* [PutBucketAccelerateConfiguration](API_PutBucketAccelerateConfiguration.md "API_PutBucketAccelerateConfiguration.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
GET /?accelerate HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
x-amz-expected-bucket-owner: `ExpectedBucketOwner`
x-amz-request-payer: `RequestPayer`

```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_GetBucketAccelerateConfiguration_RequestSyntax "#API_GetBucketAccelerateConfiguration_RequestSyntax")**


The name of the bucket for which the accelerate configuration is retrieved.


Required: Yes




**[x-amz-expected-bucket-owner](#API_GetBucketAccelerateConfiguration_RequestSyntax "#API_GetBucketAccelerateConfiguration_RequestSyntax")**


The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).




**[x-amz-request-payer](#API_GetBucketAccelerateConfiguration_RequestSyntax "#API_GetBucketAccelerateConfiguration_RequestSyntax")**


Confirms that the requester knows that they will be charged for the request. Bucket owners need not
 specify this parameter in their requests. If either the source or destination S3 bucket has Requester
 Pays enabled, the requester will pay for corresponding charges to copy the object. For information about
 downloading objects from Requester Pays buckets, see [Downloading Objects in Requester Pays
 Buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html") in the *Amazon S3 User Guide*.


###### Note

This functionality is not supported for directory buckets.


Valid Values: `requester`





## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
x-amz-request-charged: `RequestCharged`
<?xml version="1.0" encoding="UTF-8"?>
<[AccelerateConfiguration](#AmazonS3-GetBucketAccelerateConfiguration-response-GetBucketAccelerateConfigurationOutput "#AmazonS3-GetBucketAccelerateConfiguration-response-GetBucketAccelerateConfigurationOutput")>
   <[Status](#AmazonS3-GetBucketAccelerateConfiguration-response-Status "#AmazonS3-GetBucketAccelerateConfiguration-response-Status")>***string***</[Status](#AmazonS3-GetBucketAccelerateConfiguration-response-Status "#AmazonS3-GetBucketAccelerateConfiguration-response-Status")>
</[AccelerateConfiguration](#AmazonS3-GetBucketAccelerateConfiguration-response-GetBucketAccelerateConfigurationOutput "#AmazonS3-GetBucketAccelerateConfiguration-response-GetBucketAccelerateConfigurationOutput")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The response returns the following HTTP headers.





**[x-amz-request-charged](#API_GetBucketAccelerateConfiguration_ResponseSyntax "#API_GetBucketAccelerateConfiguration_ResponseSyntax")**


If present, indicates that the requester was successfully charged for the request. For more
 information, see [Using Requester Pays buckets for storage transfers and usage](../userguide/RequesterPaysBuckets.md "../userguide/RequesterPaysBuckets.md") in the *Amazon Simple
 Storage Service user guide*.


###### Note

This functionality is not supported for directory buckets.


Valid Values: `requester`





The following data is returned in XML format by the service.





**[AccelerateConfiguration](#API_GetBucketAccelerateConfiguration_ResponseSyntax "#API_GetBucketAccelerateConfiguration_ResponseSyntax")**


Root level tag for the AccelerateConfiguration parameters.


Required: Yes




**[Status](#API_GetBucketAccelerateConfiguration_ResponseSyntax "#API_GetBucketAccelerateConfiguration_ResponseSyntax")**


The accelerate configuration of the bucket.


Type: String


Valid Values: `Enabled | Suspended`





## Examples


This implementation of the GET action returns the following responses.


### Example


If the transfer acceleration state is set to `Enabled` on a bucket, the response is
 as follows:



```

<AccelerateConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
  <Status>Enabled</Status>
</AccelerateConfiguration>                 
              
```

### Example


If the transfer acceleration state is set to `Suspended` on a bucket, the response is
 as follows:



```

<AccelerateConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
  <Status>Suspended</Status>
</AccelerateConfiguration>                 
              
```

### Example


If the transfer acceleration state on a bucket has never been set to `Enabled` or
 `Suspended`, the response is as follows:



```

<AccelerateConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/" />
              
```

###  Retrieve the transfer acceleration configuration for a bucket


The following example shows a GET /?`accelerate` request to retrieve the transfer
 acceleration state of the bucket named `amzn-s3-demo-bucket`.



```

GET /?accelerate HTTP/1.1
Host: amzn-s3-demo-bucket.s3.<Region>.amazonaws.com
Date: Mon, 11 Apr 2016 12:00:00 GMT
Authorization: authorization string
Content-Type: text/plain

```

### Example


The following is a sample of the response body (only) that shows bucket transfer acceleration is
 enabled.



```

<AccelerateConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
  <Status>Enabled</Status>
</AccelerateConfiguration>
              
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetBucketAccelerateConfiguration "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetBucketAccelerateConfiguration")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/GetBucketAccelerateConfiguration "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/GetBucketAccelerateConfiguration")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetBucketAccelerateConfiguration "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetBucketAccelerateConfiguration")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetBucketAccelerateConfiguration "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetBucketAccelerateConfiguration")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetBucketAccelerateConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetBucketAccelerateConfiguration")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetBucketAccelerateConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetBucketAccelerateConfiguration")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetBucketAccelerateConfiguration "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetBucketAccelerateConfiguration")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetBucketAccelerateConfiguration "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetBucketAccelerateConfiguration")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetBucketAccelerateConfiguration "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetBucketAccelerateConfiguration")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetBucketAccelerateConfiguration "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetBucketAccelerateConfiguration")
