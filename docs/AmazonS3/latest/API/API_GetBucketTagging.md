# GetBucketTagging

###### Note

This operation is not supported for directory buckets.

Returns the tag set associated with the bucket.

To use this operation, you must have permission to perform the `s3:GetBucketTagging`
 action. By default, the bucket owner has this permission and can grant this permission to others.


`GetBucketTagging` has the following special error:


* Error code: `NoSuchTagSet`





	+ Description: There is no tag set associated with the bucket.
The following operations are related to `GetBucketTagging`:


* [PutBucketTagging](API_PutBucketTagging.md "API_PutBucketTagging.md")
* [DeleteBucketTagging](API_DeleteBucketTagging.md "API_DeleteBucketTagging.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
GET /?tagging HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
x-amz-expected-bucket-owner: `ExpectedBucketOwner`

```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_GetBucketTagging_RequestSyntax "#API_GetBucketTagging_RequestSyntax")**


The name of the bucket for which to get the tagging information.


Required: Yes




**[x-amz-expected-bucket-owner](#API_GetBucketTagging_RequestSyntax "#API_GetBucketTagging_RequestSyntax")**


The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<[Tagging](#AmazonS3-GetBucketTagging-response-GetBucketTaggingOutput "#AmazonS3-GetBucketTagging-response-GetBucketTaggingOutput")>
   <[TagSet](#AmazonS3-GetBucketTagging-response-TagSet "#AmazonS3-GetBucketTagging-response-TagSet")>
      <Tag>
         <[Key](API_Tag.md#AmazonS3-Type-Tag-Key "API_Tag.md#AmazonS3-Type-Tag-Key")>***string***</[Key](API_Tag.md#AmazonS3-Type-Tag-Key "API_Tag.md#AmazonS3-Type-Tag-Key")>
         <[Value](API_Tag.md#AmazonS3-Type-Tag-Value "API_Tag.md#AmazonS3-Type-Tag-Value")>***string***</[Value](API_Tag.md#AmazonS3-Type-Tag-Value "API_Tag.md#AmazonS3-Type-Tag-Value")>
      </Tag>
   </[TagSet](#AmazonS3-GetBucketTagging-response-TagSet "#AmazonS3-GetBucketTagging-response-TagSet")>
</[Tagging](#AmazonS3-GetBucketTagging-response-GetBucketTaggingOutput "#AmazonS3-GetBucketTagging-response-GetBucketTaggingOutput")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[Tagging](#API_GetBucketTagging_ResponseSyntax "#API_GetBucketTagging_ResponseSyntax")**


Root level tag for the Tagging parameters.


Required: Yes




**[TagSet](#API_GetBucketTagging_ResponseSyntax "#API_GetBucketTagging_ResponseSyntax")**


Contains the tag set.


Type: Array of [Tag](API_Tag.md "API_Tag.md") data types




## Examples


### Sample Request


The following request returns the tag set of the specified bucket.



```

            GET ?tagging HTTP/1.1
            Host: amzn-s3-demo-bucket.s3.<Region>.amazonaws.com
            Date: Wed, 28 Oct 2009 22:32:00 GMT
            Authorization: authorization string
         
```

### Sample Response


Delete the metric configuration with a specified ID, which disables the CloudWatch metrics with
 the `ExampleMetrics` value for the `FilterId` dimension. 



```

         HTTP/1.1 200 OK
         Date: Wed, 25 Nov 2009 12:00:00 GMT
         Connection: close
         Server: AmazonS3

         <Tagging>
           <TagSet>
              <Tag>
                <Key>Project</Key>
               <Value>Project One</Value>
              </Tag>
              <Tag>
                <Key>User</Key>
                <Value>jsmith</Value>
              </Tag>
           </TagSet>
         </Tagging> 
         
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetBucketTagging "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetBucketTagging")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/GetBucketTagging "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/GetBucketTagging")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetBucketTagging "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetBucketTagging")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetBucketTagging "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetBucketTagging")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetBucketTagging "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetBucketTagging")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetBucketTagging "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetBucketTagging")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetBucketTagging "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetBucketTagging")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetBucketTagging "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetBucketTagging")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetBucketTagging "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetBucketTagging")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetBucketTagging "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetBucketTagging")
