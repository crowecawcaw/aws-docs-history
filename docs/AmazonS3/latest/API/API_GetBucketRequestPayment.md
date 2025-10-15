# GetBucketRequestPayment

###### Note

This operation is not supported for directory buckets.

Returns the request payment configuration of a bucket. To use this version of the operation, you
 must be the bucket owner. For more information, see [Requester Pays Buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/RequesterPaysBuckets.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/RequesterPaysBuckets.html").

The following operations are related to `GetBucketRequestPayment`:


* [ListObjects](API_ListObjects.md "API_ListObjects.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
GET /?requestPayment HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
x-amz-expected-bucket-owner: `ExpectedBucketOwner`

```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_GetBucketRequestPayment_RequestSyntax "#API_GetBucketRequestPayment_RequestSyntax")**


The name of the bucket for which to get the payment request configuration


Required: Yes




**[x-amz-expected-bucket-owner](#API_GetBucketRequestPayment_RequestSyntax "#API_GetBucketRequestPayment_RequestSyntax")**


The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<[RequestPaymentConfiguration](#AmazonS3-GetBucketRequestPayment-response-GetBucketRequestPaymentOutput "#AmazonS3-GetBucketRequestPayment-response-GetBucketRequestPaymentOutput")>
   <[Payer](#AmazonS3-GetBucketRequestPayment-response-Payer "#AmazonS3-GetBucketRequestPayment-response-Payer")>***string***</[Payer](#AmazonS3-GetBucketRequestPayment-response-Payer "#AmazonS3-GetBucketRequestPayment-response-Payer")>
</[RequestPaymentConfiguration](#AmazonS3-GetBucketRequestPayment-response-GetBucketRequestPaymentOutput "#AmazonS3-GetBucketRequestPayment-response-GetBucketRequestPaymentOutput")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[RequestPaymentConfiguration](#API_GetBucketRequestPayment_ResponseSyntax "#API_GetBucketRequestPayment_ResponseSyntax")**


Root level tag for the RequestPaymentConfiguration parameters.


Required: Yes




**[Payer](#API_GetBucketRequestPayment_ResponseSyntax "#API_GetBucketRequestPayment_ResponseSyntax")**


Specifies who pays for the download and request fees.


Type: String


Valid Values: `Requester | BucketOwner`





## Examples


### Sample Request


The following request returns the payer for the bucket, `amzn-s3-demo-bucket`. 



```

            GET ?requestPayment HTTP/1.1
            Host: *amzn-s3-demo-bucket*.s3.<Region>.amazonaws.com
            Date: Wed, 01 Mar 2009 12:00:00 GMT
            Authorization: authorization string
         
```

### Sample Response


This response shows that the bucket is a Requester Pays bucket, meaning the person requesting a
 download from this bucket pays the transfer fees.



```

            HTTP/1.1 200 OK
            x-amz-id-2: YgIPIfBiKa2bj0KMg95r/0zo3emzU4dzsD4rcKCHQUAdQkf3ShJTOOpXUueF6QKo
            x-amz-request-id: 236A8905248E5A01
            Date: Wed, 01 Mar 2009 12:00:00 GMT
            Content-Type: [type]
            Content-Length: 0
            Connection: close
            Server: AmazonS3

            <?xml version="1.0" encoding="UTF-8"?>
            <RequestPaymentConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
              <Payer>Requester</Payer>
            </RequestPaymentConfiguration>
         
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetBucketRequestPayment "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetBucketRequestPayment")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/GetBucketRequestPayment "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/GetBucketRequestPayment")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetBucketRequestPayment "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetBucketRequestPayment")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetBucketRequestPayment "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetBucketRequestPayment")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetBucketRequestPayment "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetBucketRequestPayment")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetBucketRequestPayment "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetBucketRequestPayment")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetBucketRequestPayment "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetBucketRequestPayment")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetBucketRequestPayment "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetBucketRequestPayment")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetBucketRequestPayment "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetBucketRequestPayment")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetBucketRequestPayment "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetBucketRequestPayment")
