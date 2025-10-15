# GetObjectTorrent

###### Note

This operation is not supported for directory buckets.

Returns torrent files from a bucket. BitTorrent can save you bandwidth when you're distributing
 large files.

###### Note

You can get torrent only for objects that are less than 5 GB in size, and that are not encrypted
 using server-side encryption with a customer-provided encryption key.

To use GET, you must have READ access to the object.

This functionality is not supported for Amazon S3 on Outposts.

The following action is related to `GetObjectTorrent`:


* [GetObject](API_GetObject.md "API_GetObject.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
GET /{Key+}?torrent HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
x-amz-request-payer: `RequestPayer`
x-amz-expected-bucket-owner: `ExpectedBucketOwner`

```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_GetObjectTorrent_RequestSyntax "#API_GetObjectTorrent_RequestSyntax")**


The name of the bucket containing the object for which to get the torrent files.


Required: Yes




**[Key](#API_GetObjectTorrent_RequestSyntax "#API_GetObjectTorrent_RequestSyntax")**


The object key for which to get the information.


Length Constraints: Minimum length of 1.


Required: Yes




**[x-amz-expected-bucket-owner](#API_GetObjectTorrent_RequestSyntax "#API_GetObjectTorrent_RequestSyntax")**


The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).




**[x-amz-request-payer](#API_GetObjectTorrent_RequestSyntax "#API_GetObjectTorrent_RequestSyntax")**


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

`Body`
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The response returns the following HTTP headers.





**[x-amz-request-charged](#API_GetObjectTorrent_ResponseSyntax "#API_GetObjectTorrent_ResponseSyntax")**


If present, indicates that the requester was successfully charged for the request. For more
 information, see [Using Requester Pays buckets for storage transfers and usage](../userguide/RequesterPaysBuckets.md "../userguide/RequesterPaysBuckets.md") in the *Amazon Simple
 Storage Service user guide*.


###### Note

This functionality is not supported for directory buckets.


Valid Values: `requester`





The following data is returned in binary format by the service.



**[Body](#API_GetObjectTorrent_ResponseSyntax "#API_GetObjectTorrent_ResponseSyntax")**


## Examples


### Getting torrent files in a bucket


This example retrieves the `Torrent` file for the `Nelson` object in the
 `quotes` bucket.



```

            GET /quotes/Nelson?torrent HTTP/1.0
            Host: bucket.s3.<Region>.amazonaws.com
            Date: Wed, 28 Oct 2009 22:32:00 GMT
            Authorization: authorization string 
         
```

### Sample Response


This example illustrates one usage of GetObjectTorrent.



```

            HTTP/1.1 200 OK
            x-amz-request-id: 7CD745EBB7AB5ED9
            Date: Wed, 25 Nov 2009 12:00:00 GMT
            Content-Disposition: attachment; filename=Nelson.torrent;
            Content-Type: application/x-bittorrent
            Content-Length: 537
            Server: AmazonS3

            <body: a Bencoded dictionary as defined by the BitTorrent specification>
         
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetObjectTorrent "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetObjectTorrent")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/GetObjectTorrent "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/GetObjectTorrent")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetObjectTorrent "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetObjectTorrent")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetObjectTorrent "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetObjectTorrent")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetObjectTorrent "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetObjectTorrent")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetObjectTorrent "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetObjectTorrent")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetObjectTorrent "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetObjectTorrent")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetObjectTorrent "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetObjectTorrent")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetObjectTorrent "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetObjectTorrent")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetObjectTorrent "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetObjectTorrent")
