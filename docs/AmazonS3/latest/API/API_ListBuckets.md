# ListBuckets

###### Important

End of support notice: Beginning November 21, 2025, Amazon S3 will stop returning `DisplayName`. Update your applications to use canonical IDs (unique identifier for 
 AWS accounts), AWS account ID (12 digit identifier) or IAM ARNs (full resource naming) as a direct replacement of `DisplayName`.


Between July 15, 2025 and November 21, 2025, you will begin to see an increasing rate of missing `DisplayName` in the Owner object.

This change affects the following AWS Regions: US East (N. Virginia) Region, US West (N. California) Region, US West (Oregon) Region, Asia Pacific (Singapore) Region, Asia Pacific (Sydney) Region, 
 Asia Pacific (Tokyo) Region, Europe (Ireland) Region, and South America (São Paulo) Region.

###### Note

This operation is not supported for directory buckets.

Returns a list of all buckets owned by the authenticated sender of the request. To grant IAM
 permission to use this operation, you must add the `s3:ListAllMyBuckets` policy action. 

For information about Amazon S3 buckets, see [Creating, configuring, and working with Amazon S3
 buckets](../userguide/creating-buckets-s3.md "../userguide/creating-buckets-s3.md").

###### Important

We strongly recommend using only paginated `ListBuckets` requests. Unpaginated
 `ListBuckets` requests are only supported for AWS accounts set to the default general
 purpose bucket quota of 10,000. If you have an approved general purpose bucket quota above 10,000, you
 must send paginated `ListBuckets` requests to list your account’s buckets. All unpaginated
 `ListBuckets` requests will be rejected for AWS accounts with a general purpose bucket
 quota greater than 10,000. 

###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
GET /?bucket-region=`BucketRegion`&continuation-token=`ContinuationToken`&max-buckets=`MaxBuckets`&prefix=`Prefix` HTTP/1.1
Host: s3.amazonaws.com

```

## URI Request Parameters


The request uses the following URI parameters.





**[bucket-region](#API_ListBuckets_RequestSyntax "#API_ListBuckets_RequestSyntax")**


Limits the response to buckets that are located in the specified AWS Region. The AWS Region must
 be expressed according to the AWS Region code, such as `us-west-2` for the US West (Oregon)
 Region. For a list of the valid values for all of the AWS Regions, see [Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region "https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region").


###### Note

Requests made to a Regional endpoint that is different from the `bucket-region`
 parameter are not supported. For example, if you want to limit the response to your buckets in Region
 `us-west-2`, the request must be made to an endpoint in Region
 `us-west-2`.




**[continuation-token](#API_ListBuckets_RequestSyntax "#API_ListBuckets_RequestSyntax")**



`ContinuationToken` indicates to Amazon S3 that the list is being continued on this bucket
 with a token. `ContinuationToken` is obfuscated and is not a real key. You can use this
 `ContinuationToken` for pagination of the list results. 


Length Constraints: Minimum length of 0. Maximum length of 1024.


Required: No.


###### Note

If you specify the `bucket-region`, `prefix`, or
 `continuation-token` query parameters without using `max-buckets` to set the
 maximum number of buckets returned in the response, Amazon S3 applies a default page size of 10,000 and
 provides a continuation token if there are more buckets.




**[max-buckets](#API_ListBuckets_RequestSyntax "#API_ListBuckets_RequestSyntax")**


Maximum number of buckets to be returned in response. When the number is more than the count of
 buckets that are owned by an AWS account, return all the buckets in response.


Valid Range: Minimum value of 1. Maximum value of 10000.




**[prefix](#API_ListBuckets_RequestSyntax "#API_ListBuckets_RequestSyntax")**


Limits the response to bucket names that begin with the specified bucket name prefix.




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<[ListAllMyBucketsResult](#AmazonS3-ListBuckets-response-ListBucketsOutput "#AmazonS3-ListBuckets-response-ListBucketsOutput")>
   <[Buckets](#AmazonS3-ListBuckets-response-Buckets "#AmazonS3-ListBuckets-response-Buckets")>
      <Bucket>
         <[BucketArn](API_Bucket.md#AmazonS3-Type-Bucket-BucketArn "API_Bucket.md#AmazonS3-Type-Bucket-BucketArn")>***string***</[BucketArn](API_Bucket.md#AmazonS3-Type-Bucket-BucketArn "API_Bucket.md#AmazonS3-Type-Bucket-BucketArn")>
         <[BucketRegion](API_Bucket.md#AmazonS3-Type-Bucket-BucketRegion "API_Bucket.md#AmazonS3-Type-Bucket-BucketRegion")>***string***</[BucketRegion](API_Bucket.md#AmazonS3-Type-Bucket-BucketRegion "API_Bucket.md#AmazonS3-Type-Bucket-BucketRegion")>
         <[CreationDate](API_Bucket.md#AmazonS3-Type-Bucket-CreationDate "API_Bucket.md#AmazonS3-Type-Bucket-CreationDate")>***timestamp***</[CreationDate](API_Bucket.md#AmazonS3-Type-Bucket-CreationDate "API_Bucket.md#AmazonS3-Type-Bucket-CreationDate")>
         <[Name](API_Bucket.md#AmazonS3-Type-Bucket-Name "API_Bucket.md#AmazonS3-Type-Bucket-Name")>***string***</[Name](API_Bucket.md#AmazonS3-Type-Bucket-Name "API_Bucket.md#AmazonS3-Type-Bucket-Name")>
      </Bucket>
   </[Buckets](#AmazonS3-ListBuckets-response-Buckets "#AmazonS3-ListBuckets-response-Buckets")>
   <[Owner](#AmazonS3-ListBuckets-response-Owner "#AmazonS3-ListBuckets-response-Owner")>
      <[DisplayName](API_Owner.md#AmazonS3-Type-Owner-DisplayName "API_Owner.md#AmazonS3-Type-Owner-DisplayName")>***string***</[DisplayName](API_Owner.md#AmazonS3-Type-Owner-DisplayName "API_Owner.md#AmazonS3-Type-Owner-DisplayName")>
      <[ID](API_Owner.md#AmazonS3-Type-Owner-ID "API_Owner.md#AmazonS3-Type-Owner-ID")>***string***</[ID](API_Owner.md#AmazonS3-Type-Owner-ID "API_Owner.md#AmazonS3-Type-Owner-ID")>
   </[Owner](#AmazonS3-ListBuckets-response-Owner "#AmazonS3-ListBuckets-response-Owner")>
   <[ContinuationToken](#AmazonS3-ListBuckets-response-ContinuationToken "#AmazonS3-ListBuckets-response-ContinuationToken")>***string***</[ContinuationToken](#AmazonS3-ListBuckets-response-ContinuationToken "#AmazonS3-ListBuckets-response-ContinuationToken")>
   <[Prefix](#AmazonS3-ListBuckets-response-Prefix "#AmazonS3-ListBuckets-response-Prefix")>***string***</[Prefix](#AmazonS3-ListBuckets-response-Prefix "#AmazonS3-ListBuckets-response-Prefix")>
</[ListAllMyBucketsResult](#AmazonS3-ListBuckets-response-ListBucketsOutput "#AmazonS3-ListBuckets-response-ListBucketsOutput")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[ListAllMyBucketsResult](#API_ListBuckets_ResponseSyntax "#API_ListBuckets_ResponseSyntax")**


Root level tag for the ListAllMyBucketsResult parameters.


Required: Yes




**[Buckets](#API_ListBuckets_ResponseSyntax "#API_ListBuckets_ResponseSyntax")**


The list of buckets owned by the requester.


Type: Array of [Bucket](API_Bucket.md "API_Bucket.md") data types




**[ContinuationToken](#API_ListBuckets_ResponseSyntax "#API_ListBuckets_ResponseSyntax")**



`ContinuationToken` is included in the response when there are more buckets that can be
 listed with pagination. The next `ListBuckets` request to Amazon S3 can be continued with this
 `ContinuationToken`. `ContinuationToken` is obfuscated and is not a real
 bucket.


Type: String




**[Owner](#API_ListBuckets_ResponseSyntax "#API_ListBuckets_ResponseSyntax")**


The owner of the buckets listed.


Type: [Owner](API_Owner.md "API_Owner.md") data type




**[Prefix](#API_ListBuckets_ResponseSyntax "#API_ListBuckets_ResponseSyntax")**


If `Prefix` was sent with the request, it is included in the response.


All bucket names in the response begin with the specified bucket name prefix.


Type: String




## Examples


### Example 1: Unpaginated ListBuckets request


This example lists all the buckets in your account in a single unpaginated response. Unpaginated
 requests are only supported for AWS accounts that have the default service quota of 10,000
 buckets. If you have an approved general purpose bucket quota that is greater than 10,000 buckets,
 all unpaginated requests will be rejected for your account.



```
GET / host:s3.us-east-2.amazonaws.com HTTP/1.1
```


```

HTTP/1.1 200 OK
<ListAllMyBucketsResult>
   <Buckets>
      <Bucket>
         <CreationDate>2019-12-11T23:32:47+00:00</CreationDate>
         <Name>amzn-s3-demo-bucket</Name>
      </Bucket>
      <Bucket>
         <CreationDate>2019-11-10T23:32:13+00:00</CreationDate>
         <Name>amzn-s3-demo-bucket1</Name>
      </Bucket>
   </Buckets>
   <Owner>
      <DisplayName>Account+Name</DisplayName>
      <ID>AIDACKCEVSQ6C2EXAMPLE</ID>
   </Owner>  
</ListAllMyBucketsResult>   
         
```

### Example 2: Paginated ListBuckets request


The following example request lists all buckets in your account using pagination. It gets the
 first page of results with the page size set to 1000 buckets. The response returns a
 `ContinuationToken` that is used in **Example 3** to list
 the next 1000 buckets.



```
GET /?max-buckets=1000&host:s3.us-east-2.amazonaws.com HTTP/1.1
```


```

HTTP/1.1 200 OK
<ListAllMyBucketsResult>
   <Buckets>
      <Bucket>
         <CreationDate>2024-11-14T23:32:47+00:00</CreationDate>
         <Name>amzn-s3-demo-bucket</Name>
         <BucketRegion>us-east-1</BucketRegion>
      </Bucket>
      <Bucket>
         <CreationDate>2024-11-14T23:32:13+00:00</CreationDate>
         <Name>amzn-s3-demo-bucket1</Name>
         <BucketRegion>us-east-2</BucketRegion>
      </Bucket>
   </Buckets>
   <Owner>
      <DisplayName>Account+Name</DisplayName>
      <ID>AIDACKCEVSQ6C2EXAMPLE</ID>
   </Owner>  
   <ContinuationToken>eyJNYXJrZXIiOiBudWxsLCAiYm90b190cnVuY2F0ZV9hbW91bnQiOiAxfQ==</ContinuationToken>      
</ListAllMyBucketsResult>   
         
```

### Example 3: Paginated ListBuckets request with continuation token


This example request uses the token returned in **Example 2** to
 return the next 1000 buckets. Continue until there are no more results. If you do not receive a
 continuation token with your initial paginated ListBuckets request, then your single paginated
 request returned all of the buckets in your account.



```
GET /?max-buckets=1000&continuation-token=eyJNYXJrZXIiOiBudWxsLCAiYm90b190cnVuY2F0ZV9hbW91bnQiOiAxfQ== host:s3.us-east-2.amazonaws.com HTTP/1.1
```


```

HTTP/1.1 200 OK
<ListAllMyBucketsResult>
   <Buckets>
      <Bucket>
         <CreationDate>2024-11-14T23:32:47+00:00</CreationDate>
         <Name>amzn-s3-demo-bucket</Name>
         <BucketRegion>us-east-1</BucketRegion>
      </Bucket>
      <Bucket>
         <CreationDate>2024-11-14T23:32:13+00:00</CreationDate>
         <Name>amzn-s3-demo-bucket1</Name>
         <BucketRegion>us-east-2</BucketRegion>
      </Bucket>
   </Buckets>
   <Owner>
      <DisplayName>Account+Name</DisplayName>
      <ID>AIDACKCEVSQ6C2EXAMPLE</ID>
   </Owner>  
   <ContinuationToken>eyJOZXh0VG9rZW4iOiBudWxsLCAiYm90b190cnVuY2F0ZV9hbW91bnQiEXAMPLE=</ContinuationToken>      
</ListAllMyBucketsResult>   
         
```

### Example 4: Paginated ListBuckets request for buckets in US East (Ohio) (us-east-2)


The following example lists all the buckets in your account in the `us-east-2`
 Region. The first paginated response will return up to 1000 buckets. Requests made to a Regional
 endpoint that is different from the `bucket-region` parameter are not supported. 



```
GET /?bucket-region=us-east-2&max-buckets=1000 host:s3.us-east-2.amazonaws.com HTTP/1.1
```


```

HTTP/1.1 200 OK
<ListAllMyBucketsResult>
   <Buckets>
      <Bucket>
         <CreationDate>2024-11-14T23:32:47+00:00</CreationDate>
         <Name>DOC-EXAMPLE-BUCKET</Name>
         <BucketRegion>us-east-2</BucketRegion>
      </Bucket>
      <Bucket>
         <CreationDate>2024-11-14T23:32:13+00:00</CreationDate>
         <Name>DOC-EXAMPLE-BUCKET1002</Name>
         <BucketRegion>us-east-2</BucketRegion>
      </Bucket>
   </Buckets>
   <Owner>
      <DisplayName>Account+Name</DisplayName>
      <ID>AIDACKCEVSQ6C2EXAMPLE</ID>
   </Owner>  
   <ContinuationToken>eyJOZXh0VG9rZW4iOiBudWxsLCAiYm90b190cnVuY2F0ZV9hbW91bnQiEXAMPLEcd =</ContinuationToken>      
</ListAllMyBucketsResult>   
         
```

### Example 5: Paginated ListBuckets request for buckets in your account that begin with amzn-s3-demo-bucket in US East (Ohio) (us-east-2)


The following example lists all the buckets in your account located in the
 `us-east-2` Region that begin with the `amzn-s3-demo-bucket`
 bucket prefix. This request uses pagination.



```
GET /?bucket-region=us-east-2&max-buckets=1000&prefix=amzn-s3-demo-bucket host:s3.us-east-2.amazonaws.com HTTP/1.1
```


```

HTTP/1.1 200 OK
<ListAllMyBucketsResult>
   <Buckets>
      <Bucket>
         <CreationDate>2024-11-14T23:32:47+00:00</CreationDate>
         <Name>amzn-s3-demo-bucket</Name>
         <BucketRegion>us-east-2</BucketRegion>
      </Bucket>
   </Buckets>
   <Owner>
      <DisplayName>Account+Name</DisplayName>
      <ID>AIDACKCEVSQ6C2EXAMPLE</ID>
   </Owner>  
   <Prefix>
       amzn-s3-demo-bucket
   </Prefix>
   <ContinuationToken>eyJOZXh0VG9rZW4iOiBudWxsLCAiYm90b190cnVuY2F0ZV9hbW91bnQiEXAMPLE=</ContinuationToken>
</ListAllMyBucketsResult>   
         
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/ListBuckets "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/ListBuckets")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/ListBuckets "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/ListBuckets")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/ListBuckets "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/ListBuckets")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/ListBuckets "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/ListBuckets")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/ListBuckets "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/ListBuckets")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/ListBuckets "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/ListBuckets")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/ListBuckets "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/ListBuckets")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/ListBuckets "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/ListBuckets")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/ListBuckets "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/ListBuckets")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/ListBuckets "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/ListBuckets")
