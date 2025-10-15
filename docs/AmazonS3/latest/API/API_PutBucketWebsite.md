# PutBucketWebsite

###### Note

This operation is not supported for directory buckets.

Sets the configuration of the website that is specified in the `website` subresource. To
 configure a bucket as a website, you can add this subresource on the bucket with website configuration
 information such as the file name of the index document and any redirect rules. For more information,
 see [Hosting Websites on
 Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html").

This PUT action requires the `S3:PutBucketWebsite` permission. By default, only the
 bucket owner can configure the website attached to a bucket; however, bucket owners can allow other
 users to set the website configuration by writing a bucket policy that grants them the
 `S3:PutBucketWebsite` permission.

To redirect all website requests sent to the bucket's website endpoint, you add a website
 configuration with the following elements. Because all requests are sent to another website, you don't
 need to provide index document name for the bucket.


* `WebsiteConfiguration`
* `RedirectAllRequestsTo`
* `HostName`
* `Protocol`
If you want granular control over redirects, you can use the following elements to add routing rules
 that describe conditions for redirecting requests and information about the redirect destination. In
 this case, the website configuration must provide an index document for the bucket, because some
 requests might not be redirected. 


* `WebsiteConfiguration`
* `IndexDocument`
* `Suffix`
* `ErrorDocument`
* `Key`
* `RoutingRules`
* `RoutingRule`
* `Condition`
* `HttpErrorCodeReturnedEquals`
* `KeyPrefixEquals`
* `Redirect`
* `Protocol`
* `HostName`
* `ReplaceKeyPrefixWith`
* `ReplaceKeyWith`
* `HttpRedirectCode`
Amazon S3 has a limitation of 50 routing rules per website configuration. If you require more than 50
 routing rules, you can use object redirect. For more information, see [Configuring an Object Redirect](https://docs.aws.amazon.com/AmazonS3/latest/dev/how-to-page-redirect.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/how-to-page-redirect.html") in the
 *Amazon S3 User Guide*.

The maximum request length is limited to 128 KB.

###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
PUT /?website HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
Content-MD5: `ContentMD5`
x-amz-sdk-checksum-algorithm: `ChecksumAlgorithm`
x-amz-expected-bucket-owner: `ExpectedBucketOwner`
<?xml version="1.0" encoding="UTF-8"?>
<[WebsiteConfiguration](#AmazonS3-PutBucketWebsite-request-WebsiteConfiguration "#AmazonS3-PutBucketWebsite-request-WebsiteConfiguration") xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
   <[ErrorDocument](#AmazonS3-PutBucketWebsite-request-ErrorDocument "#AmazonS3-PutBucketWebsite-request-ErrorDocument")>
      <[Key](API_ErrorDocument.md#AmazonS3-Type-ErrorDocument-Key "API_ErrorDocument.md#AmazonS3-Type-ErrorDocument-Key")>`string`</[Key](API_ErrorDocument.md#AmazonS3-Type-ErrorDocument-Key "API_ErrorDocument.md#AmazonS3-Type-ErrorDocument-Key")>
   </[ErrorDocument](#AmazonS3-PutBucketWebsite-request-ErrorDocument "#AmazonS3-PutBucketWebsite-request-ErrorDocument")>
   <[IndexDocument](#AmazonS3-PutBucketWebsite-request-IndexDocument "#AmazonS3-PutBucketWebsite-request-IndexDocument")>
      <[Suffix](API_IndexDocument.md#AmazonS3-Type-IndexDocument-Suffix "API_IndexDocument.md#AmazonS3-Type-IndexDocument-Suffix")>`string`</[Suffix](API_IndexDocument.md#AmazonS3-Type-IndexDocument-Suffix "API_IndexDocument.md#AmazonS3-Type-IndexDocument-Suffix")>
   </[IndexDocument](#AmazonS3-PutBucketWebsite-request-IndexDocument "#AmazonS3-PutBucketWebsite-request-IndexDocument")>
   <[RedirectAllRequestsTo](#AmazonS3-PutBucketWebsite-request-RedirectAllRequestsTo "#AmazonS3-PutBucketWebsite-request-RedirectAllRequestsTo")>
      <[HostName](API_RedirectAllRequestsTo.md#AmazonS3-Type-RedirectAllRequestsTo-HostName "API_RedirectAllRequestsTo.md#AmazonS3-Type-RedirectAllRequestsTo-HostName")>`string`</[HostName](API_RedirectAllRequestsTo.md#AmazonS3-Type-RedirectAllRequestsTo-HostName "API_RedirectAllRequestsTo.md#AmazonS3-Type-RedirectAllRequestsTo-HostName")>
      <[Protocol](API_RedirectAllRequestsTo.md#AmazonS3-Type-RedirectAllRequestsTo-Protocol "API_RedirectAllRequestsTo.md#AmazonS3-Type-RedirectAllRequestsTo-Protocol")>`string`</[Protocol](API_RedirectAllRequestsTo.md#AmazonS3-Type-RedirectAllRequestsTo-Protocol "API_RedirectAllRequestsTo.md#AmazonS3-Type-RedirectAllRequestsTo-Protocol")>
   </[RedirectAllRequestsTo](#AmazonS3-PutBucketWebsite-request-RedirectAllRequestsTo "#AmazonS3-PutBucketWebsite-request-RedirectAllRequestsTo")>
   <[RoutingRules](#AmazonS3-PutBucketWebsite-request-RoutingRules "#AmazonS3-PutBucketWebsite-request-RoutingRules")>
      <RoutingRule>
         <[Condition](API_RoutingRule.md#AmazonS3-Type-RoutingRule-Condition "API_RoutingRule.md#AmazonS3-Type-RoutingRule-Condition")>
            <[HttpErrorCodeReturnedEquals](API_Condition.md#AmazonS3-Type-Condition-HttpErrorCodeReturnedEquals "API_Condition.md#AmazonS3-Type-Condition-HttpErrorCodeReturnedEquals")>`string`</[HttpErrorCodeReturnedEquals](API_Condition.md#AmazonS3-Type-Condition-HttpErrorCodeReturnedEquals "API_Condition.md#AmazonS3-Type-Condition-HttpErrorCodeReturnedEquals")>
            <[KeyPrefixEquals](API_Condition.md#AmazonS3-Type-Condition-KeyPrefixEquals "API_Condition.md#AmazonS3-Type-Condition-KeyPrefixEquals")>`string`</[KeyPrefixEquals](API_Condition.md#AmazonS3-Type-Condition-KeyPrefixEquals "API_Condition.md#AmazonS3-Type-Condition-KeyPrefixEquals")>
         </[Condition](API_RoutingRule.md#AmazonS3-Type-RoutingRule-Condition "API_RoutingRule.md#AmazonS3-Type-RoutingRule-Condition")>
         <[Redirect](API_RoutingRule.md#AmazonS3-Type-RoutingRule-Redirect "API_RoutingRule.md#AmazonS3-Type-RoutingRule-Redirect")>
            <[HostName](API_Redirect.md#AmazonS3-Type-Redirect-HostName "API_Redirect.md#AmazonS3-Type-Redirect-HostName")>`string`</[HostName](API_Redirect.md#AmazonS3-Type-Redirect-HostName "API_Redirect.md#AmazonS3-Type-Redirect-HostName")>
            <[HttpRedirectCode](API_Redirect.md#AmazonS3-Type-Redirect-HttpRedirectCode "API_Redirect.md#AmazonS3-Type-Redirect-HttpRedirectCode")>`string`</[HttpRedirectCode](API_Redirect.md#AmazonS3-Type-Redirect-HttpRedirectCode "API_Redirect.md#AmazonS3-Type-Redirect-HttpRedirectCode")>
            <[Protocol](API_Redirect.md#AmazonS3-Type-Redirect-Protocol "API_Redirect.md#AmazonS3-Type-Redirect-Protocol")>`string`</[Protocol](API_Redirect.md#AmazonS3-Type-Redirect-Protocol "API_Redirect.md#AmazonS3-Type-Redirect-Protocol")>
            <[ReplaceKeyPrefixWith](API_Redirect.md#AmazonS3-Type-Redirect-ReplaceKeyPrefixWith "API_Redirect.md#AmazonS3-Type-Redirect-ReplaceKeyPrefixWith")>`string`</[ReplaceKeyPrefixWith](API_Redirect.md#AmazonS3-Type-Redirect-ReplaceKeyPrefixWith "API_Redirect.md#AmazonS3-Type-Redirect-ReplaceKeyPrefixWith")>
            <[ReplaceKeyWith](API_Redirect.md#AmazonS3-Type-Redirect-ReplaceKeyWith "API_Redirect.md#AmazonS3-Type-Redirect-ReplaceKeyWith")>`string`</[ReplaceKeyWith](API_Redirect.md#AmazonS3-Type-Redirect-ReplaceKeyWith "API_Redirect.md#AmazonS3-Type-Redirect-ReplaceKeyWith")>
         </[Redirect](API_RoutingRule.md#AmazonS3-Type-RoutingRule-Redirect "API_RoutingRule.md#AmazonS3-Type-RoutingRule-Redirect")>
      </RoutingRule>
   </[RoutingRules](#AmazonS3-PutBucketWebsite-request-RoutingRules "#AmazonS3-PutBucketWebsite-request-RoutingRules")>
</[WebsiteConfiguration](#AmazonS3-PutBucketWebsite-request-WebsiteConfiguration "#AmazonS3-PutBucketWebsite-request-WebsiteConfiguration")>
```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_PutBucketWebsite_RequestSyntax "#API_PutBucketWebsite_RequestSyntax")**


The bucket name.


Required: Yes




**[Content-MD5](#API_PutBucketWebsite_RequestSyntax "#API_PutBucketWebsite_RequestSyntax")**


The Base64 encoded 128-bit `MD5` digest of the data. You must use this header as a
 message integrity check to verify that the request body was not corrupted in transit. For more
 information, see [RFC 1864](http://www.ietf.org/rfc/rfc1864.txt "http://www.ietf.org/rfc/rfc1864.txt").


For requests made using the AWS Command Line Interface (CLI) or AWS SDKs, this field is calculated automatically.




**[x-amz-expected-bucket-owner](#API_PutBucketWebsite_RequestSyntax "#API_PutBucketWebsite_RequestSyntax")**


The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).




**[x-amz-sdk-checksum-algorithm](#API_PutBucketWebsite_RequestSyntax "#API_PutBucketWebsite_RequestSyntax")**


Indicates the algorithm used to create the checksum for the request when you use the SDK. This header will not provide any
 additional functionality if you don't use the SDK. When you send this header, there must be a corresponding `x-amz-checksum` or
 `x-amz-trailer` header sent. Otherwise, Amazon S3 fails the request with the HTTP status code `400 Bad Request`. For more
 information, see [Checking object integrity](../userguide/checking-object-integrity.md "../userguide/checking-object-integrity.md") in
 the *Amazon S3 User Guide*.


If you provide an individual checksum, Amazon S3 ignores any provided `ChecksumAlgorithm`
 parameter.


Valid Values: `CRC32 | CRC32C | SHA1 | SHA256 | CRC64NVME`





## Request Body


The request accepts the following data in XML format.





**[WebsiteConfiguration](#API_PutBucketWebsite_RequestSyntax "#API_PutBucketWebsite_RequestSyntax")**


Root level tag for the WebsiteConfiguration parameters.


Required: Yes




**[ErrorDocument](#API_PutBucketWebsite_RequestSyntax "#API_PutBucketWebsite_RequestSyntax")**


The name of the error document for the website.


Type: [ErrorDocument](API_ErrorDocument.md "API_ErrorDocument.md") data type


Required: No




**[IndexDocument](#API_PutBucketWebsite_RequestSyntax "#API_PutBucketWebsite_RequestSyntax")**


The name of the index document for the website.


Type: [IndexDocument](API_IndexDocument.md "API_IndexDocument.md") data type


Required: No




**[RedirectAllRequestsTo](#API_PutBucketWebsite_RequestSyntax "#API_PutBucketWebsite_RequestSyntax")**


The redirect behavior for every request to this bucket's website endpoint.


###### Important

If you specify this property, you can't specify any other property.


Type: [RedirectAllRequestsTo](API_RedirectAllRequestsTo.md "API_RedirectAllRequestsTo.md") data type


Required: No




**[RoutingRules](#API_PutBucketWebsite_RequestSyntax "#API_PutBucketWebsite_RequestSyntax")**


Rules that define when a redirect is applied and the redirect behavior.


Type: Array of [RoutingRule](API_RoutingRule.md "API_RoutingRule.md") data types


Required: No




## Response Syntax



```
HTTP/1.1 200

```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.


## Examples


### Example 1: Configure bucket as a website (add website configuration)


The following request configures a bucket example.com as a website. The configuration in the
 request specifies index.html as the index document. It also specifies the optional error document,
 SomeErrorDocument.html.



```

PUT ?website HTTP/1.1
Host: example.com.s3.<Region>.amazonaws.com
Content-Length: 256
Date: Thu, 27 Jan 2011 12:00:00 GMT
Authorization: signatureValue

<WebsiteConfiguration xmlns='http://s3.amazonaws.com/doc/2006-03-01/'>
    <IndexDocument>
        <Suffix>index.html</Suffix>
    </IndexDocument>
    <ErrorDocument>
        <Key>SomeErrorDocument.html</Key>
    </ErrorDocument>
</WebsiteConfiguration>
         
```

### Sample Response


This example illustrates one usage of PutBucketWebsite.



```

HTTP/1.1 200 OK
x-amz-id-2: YgIPIfBiKa2bj0KMgUAdQkf3ShJTOOpXUueF6QKo
x-amz-request-id: 80CD4368BD211111
Date: Thu, 27 Jan 2011 00:00:00 GMT
Content-Length: 0
Server: AmazonS3
         
```

### Example 2: Configure bucket as a website but redirect all requests


The following request configures a bucket `www.example.com` as a website. However,
 the configuration specifies that all GET requests for the www.example.com bucket's website endpoint
 will be redirected to host example.com. This redirect can be useful when you want to serve requests
 for both `http://www.example.com` and `http://example.com`, but you want to
 maintain the website content in only one bucket, in this case, `example.com`. 



```

PUT ?website HTTP/1.1
Host: www.example.com.s3.<Region>.amazonaws.com
Content-Length: length-value
Date: Thu, 27 Jan 2011 12:00:00 GMT
Authorization: signatureValue

<WebsiteConfiguration xmlns='http://s3.amazonaws.com/doc/2006-03-01/'>
   <RedirectAllRequestsTo>
      <HostName>example.com</HostName>
    </RedirectAllRequestsTo>
</WebsiteConfiguration>
         
```

### Example 3: Configure bucket as a website and specify optional redirection rules


Example 1 is the simplest website configuration. It configures a bucket as a website by
 providing only an index document and an error document. You can further customize the website
 configuration by adding routing rules that redirect requests for one or more objects. For example,
 suppose that your bucket contained the following objects:



* index.html
* docs/article1.html
* docs/article2.html

If you decided to rename the folder from `docs/` to `documents/`, you
 would need to redirect requests for prefix `/docs` to `documents/`. For
 example, a request for docs/article1.html will need to be redirected to
 documents/article1.html.


In this case, you update the website configuration and add a routing rule as shown in the
 following request.



```

PUT ?website HTTP/1.1
Host: www.example.com.s3.<Region>.amazonaws.com
Content-Length: length-value
Date: Thu, 27 Jan 2011 12:00:00 GMT
Authorization: signatureValue

<WebsiteConfiguration xmlns='http://s3.amazonaws.com/doc/2006-03-01/'>
  <IndexDocument>
    <Suffix>index.html</Suffix>
  </IndexDocument>
  <ErrorDocument>
    <Key>Error.html</Key>
  </ErrorDocument>

  <RoutingRules>
    <RoutingRule>
    <Condition>
      <KeyPrefixEquals>docs/</KeyPrefixEquals>
    </Condition>
    <Redirect>
      <ReplaceKeyPrefixWith>documents/</ReplaceKeyPrefixWith>
    </Redirect>
    </RoutingRule>
  </RoutingRules>
</WebsiteConfiguration>
         
```

### Example 4: Configure a bucket as a website and redirect errors


You can use a routing rule to specify a condition that checks for a specific HTTP error code.
 When a page request results in this error, you can optionally reroute requests. For example, you
 might route requests to another host and optionally process the error. The routing rule in the
 following requests redirects requests to an EC2 instance in the event of an HTTP error 404. For
 illustration, the redirect also inserts an object key prefix `report-404/` in the
 redirect. For example, if you request a page `ExamplePage.html` and it results in an HTTP
 404 error, the request is routed to a page `report-404/testPage.html` on the specified
 EC2 instance. If there is no routing rule and the HTTP error 404 occurred, then
 `Error.html` would be returned.



```

PUT ?website HTTP/1.1
Host: www.example.com.s3.<Region>.amazonaws.com
Content-Length: 580
Date: Thu, 27 Jan 2011 12:00:00 GMT
Authorization: signatureValue

<WebsiteConfiguration xmlns='http://s3.amazonaws.com/doc/2006-03-01/'>
  <IndexDocument>
    <Suffix>index.html</Suffix>
  </IndexDocument>
  <ErrorDocument>
    <Key>Error.html</Key>
  </ErrorDocument>

  <RoutingRules>
    <RoutingRule>
    <Condition>
      <HttpErrorCodeReturnedEquals>404</HttpErrorCodeReturnedEquals >
    </Condition>
    <Redirect>
      <HostName>ec2-11-22-333-44.compute-1.amazonaws.com</HostName>
      <ReplaceKeyPrefixWith>report-404/</ReplaceKeyPrefixWith>
    </Redirect>
    </RoutingRule>
  </RoutingRules>
</WebsiteConfiguration>
         
```

### Example 5: Configure a bucket as a website and redirect folder requests to a page


Suppose you have the following pages in your bucket:



* images/photo1.jpg
* images/photo2.jpg
* images/photo3.jpg

Now you want to route requests for all pages with the images/ prefix to go to a single page,
 errorpage.html. You can add a website configuration to your bucket with the routing rule shown in
 the following request.



```

PUT ?website HTTP/1.1
Host: www.example.com.s3.<Region>.amazonaws.com
Content-Length: 481
Date: Thu, 27 Jan 2011 12:00:00 GMT
Authorization: signatureValue

<WebsiteConfiguration xmlns='http://s3.amazonaws.com/doc/2006-03-01/'>
  <IndexDocument>
    <Suffix>index.html</Suffix>
  </IndexDocument>
  <ErrorDocument>
    <Key>Error.html</Key>
  </ErrorDocument>

  <RoutingRules>
    <RoutingRule>
    <Condition>
      <KeyPrefixEquals>images/</KeyPrefixEquals>
    </Condition>
    <Redirect>
      <ReplaceKeyWith>errorpage.html</ReplaceKeyWith>
    </Redirect>
    </RoutingRule>
  </RoutingRules>
</WebsiteConfiguration>
         
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/PutBucketWebsite "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/PutBucketWebsite")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/PutBucketWebsite "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/PutBucketWebsite")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/PutBucketWebsite "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/PutBucketWebsite")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/PutBucketWebsite "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/PutBucketWebsite")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/PutBucketWebsite "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/PutBucketWebsite")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/PutBucketWebsite "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/PutBucketWebsite")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/PutBucketWebsite "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/PutBucketWebsite")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/PutBucketWebsite "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/PutBucketWebsite")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/PutBucketWebsite "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/PutBucketWebsite")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/PutBucketWebsite "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/PutBucketWebsite")
