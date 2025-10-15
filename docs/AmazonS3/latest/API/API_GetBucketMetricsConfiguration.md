# GetBucketMetricsConfiguration

###### Note

This operation is not supported for directory buckets.

Gets a metrics configuration (specified by the metrics configuration ID) from the bucket. Note that
 this doesn't include the daily storage metrics.

 To use this operation, you must have permissions to perform the
 `s3:GetMetricsConfiguration` action. The bucket owner has this permission by default. The
 bucket owner can grant this permission to others. For more information about permissions, see [Permissions Related to Bucket Subresource Operations](../userguide/using-with-s3-actions.md#using-with-s3-actions-related-to-bucket-subresources "../userguide/using-with-s3-actions.md#using-with-s3-actions-related-to-bucket-subresources") and [Managing Access Permissions to Your Amazon S3
 Resources](../userguide/s3-access-control.md "../userguide/s3-access-control.md").

 For information about CloudWatch request metrics for Amazon S3, see [Monitoring Metrics with Amazon
 CloudWatch](https://docs.aws.amazon.com/AmazonS3/latest/dev/cloudwatch-monitoring.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/cloudwatch-monitoring.html").

The following operations are related to `GetBucketMetricsConfiguration`:


* [PutBucketMetricsConfiguration](API_PutBucketMetricsConfiguration.md "API_PutBucketMetricsConfiguration.md")
* [DeleteBucketMetricsConfiguration](API_DeleteBucketMetricsConfiguration.md "API_DeleteBucketMetricsConfiguration.md")
* [ListBucketMetricsConfigurations](API_ListBucketMetricsConfigurations.md "API_ListBucketMetricsConfigurations.md")
* [Monitoring
 Metrics with Amazon CloudWatch](https://docs.aws.amazon.com/AmazonS3/latest/dev/cloudwatch-monitoring.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/cloudwatch-monitoring.html")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
GET /?metrics&id=`Id` HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
x-amz-expected-bucket-owner: `ExpectedBucketOwner`

```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_GetBucketMetricsConfiguration_RequestSyntax "#API_GetBucketMetricsConfiguration_RequestSyntax")**


The name of the bucket containing the metrics configuration to retrieve.


Required: Yes




**[id](#API_GetBucketMetricsConfiguration_RequestSyntax "#API_GetBucketMetricsConfiguration_RequestSyntax")**


The ID used to identify the metrics configuration. The ID has a 64 character limit and can only
 contain letters, numbers, periods, dashes, and underscores.


Required: Yes




**[x-amz-expected-bucket-owner](#API_GetBucketMetricsConfiguration_RequestSyntax "#API_GetBucketMetricsConfiguration_RequestSyntax")**


The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<[MetricsConfiguration](#AmazonS3-GetBucketMetricsConfiguration-response-MetricsConfiguration "#AmazonS3-GetBucketMetricsConfiguration-response-MetricsConfiguration")>
   <[Id](#AmazonS3-GetBucketMetricsConfiguration-response-Id "#AmazonS3-GetBucketMetricsConfiguration-response-Id")>***string***</[Id](#AmazonS3-GetBucketMetricsConfiguration-response-Id "#AmazonS3-GetBucketMetricsConfiguration-response-Id")>
   <[Filter](#AmazonS3-GetBucketMetricsConfiguration-response-Filter "#AmazonS3-GetBucketMetricsConfiguration-response-Filter")>
      <[AccessPointArn](API_MetricsFilter.md#AmazonS3-Type-MetricsFilter-AccessPointArn "API_MetricsFilter.md#AmazonS3-Type-MetricsFilter-AccessPointArn")>***string***</[AccessPointArn](API_MetricsFilter.md#AmazonS3-Type-MetricsFilter-AccessPointArn "API_MetricsFilter.md#AmazonS3-Type-MetricsFilter-AccessPointArn")>
      <[And](API_MetricsFilter.md#AmazonS3-Type-MetricsFilter-And "API_MetricsFilter.md#AmazonS3-Type-MetricsFilter-And")>
         <[AccessPointArn](API_MetricsAndOperator.md#AmazonS3-Type-MetricsAndOperator-AccessPointArn "API_MetricsAndOperator.md#AmazonS3-Type-MetricsAndOperator-AccessPointArn")>***string***</[AccessPointArn](API_MetricsAndOperator.md#AmazonS3-Type-MetricsAndOperator-AccessPointArn "API_MetricsAndOperator.md#AmazonS3-Type-MetricsAndOperator-AccessPointArn")>
         <[Prefix](API_MetricsAndOperator.md#AmazonS3-Type-MetricsAndOperator-Prefix "API_MetricsAndOperator.md#AmazonS3-Type-MetricsAndOperator-Prefix")>***string***</[Prefix](API_MetricsAndOperator.md#AmazonS3-Type-MetricsAndOperator-Prefix "API_MetricsAndOperator.md#AmazonS3-Type-MetricsAndOperator-Prefix")>
         <[Tag](API_MetricsAndOperator.md#AmazonS3-Type-MetricsAndOperator-Tags "API_MetricsAndOperator.md#AmazonS3-Type-MetricsAndOperator-Tags")>
            <[Key](API_Tag.md#AmazonS3-Type-Tag-Key "API_Tag.md#AmazonS3-Type-Tag-Key")>***string***</[Key](API_Tag.md#AmazonS3-Type-Tag-Key "API_Tag.md#AmazonS3-Type-Tag-Key")>
            <[Value](API_Tag.md#AmazonS3-Type-Tag-Value "API_Tag.md#AmazonS3-Type-Tag-Value")>***string***</[Value](API_Tag.md#AmazonS3-Type-Tag-Value "API_Tag.md#AmazonS3-Type-Tag-Value")>
         </[Tag](API_MetricsAndOperator.md#AmazonS3-Type-MetricsAndOperator-Tags "API_MetricsAndOperator.md#AmazonS3-Type-MetricsAndOperator-Tags")>
         ...
      </[And](API_MetricsFilter.md#AmazonS3-Type-MetricsFilter-And "API_MetricsFilter.md#AmazonS3-Type-MetricsFilter-And")>
      <[Prefix](API_MetricsFilter.md#AmazonS3-Type-MetricsFilter-Prefix "API_MetricsFilter.md#AmazonS3-Type-MetricsFilter-Prefix")>***string***</[Prefix](API_MetricsFilter.md#AmazonS3-Type-MetricsFilter-Prefix "API_MetricsFilter.md#AmazonS3-Type-MetricsFilter-Prefix")>
      <[Tag](API_MetricsFilter.md#AmazonS3-Type-MetricsFilter-Tag "API_MetricsFilter.md#AmazonS3-Type-MetricsFilter-Tag")>
         <[Key](API_Tag.md#AmazonS3-Type-Tag-Key "API_Tag.md#AmazonS3-Type-Tag-Key")>***string***</[Key](API_Tag.md#AmazonS3-Type-Tag-Key "API_Tag.md#AmazonS3-Type-Tag-Key")>
         <[Value](API_Tag.md#AmazonS3-Type-Tag-Value "API_Tag.md#AmazonS3-Type-Tag-Value")>***string***</[Value](API_Tag.md#AmazonS3-Type-Tag-Value "API_Tag.md#AmazonS3-Type-Tag-Value")>
      </[Tag](API_MetricsFilter.md#AmazonS3-Type-MetricsFilter-Tag "API_MetricsFilter.md#AmazonS3-Type-MetricsFilter-Tag")>
   </[Filter](#AmazonS3-GetBucketMetricsConfiguration-response-Filter "#AmazonS3-GetBucketMetricsConfiguration-response-Filter")>
</[MetricsConfiguration](#AmazonS3-GetBucketMetricsConfiguration-response-MetricsConfiguration "#AmazonS3-GetBucketMetricsConfiguration-response-MetricsConfiguration")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[MetricsConfiguration](#API_GetBucketMetricsConfiguration_ResponseSyntax "#API_GetBucketMetricsConfiguration_ResponseSyntax")**


Root level tag for the MetricsConfiguration parameters.


Required: Yes




**[Filter](#API_GetBucketMetricsConfiguration_ResponseSyntax "#API_GetBucketMetricsConfiguration_ResponseSyntax")**


Specifies a metrics configuration filter. The metrics configuration will only include objects that
 meet the filter's criteria. A filter must be a prefix, an object tag, an access point ARN, or a
 conjunction (MetricsAndOperator).


Type: [MetricsFilter](API_MetricsFilter.md "API_MetricsFilter.md") data type




**[Id](#API_GetBucketMetricsConfiguration_ResponseSyntax "#API_GetBucketMetricsConfiguration_ResponseSyntax")**


The ID used to identify the metrics configuration. The ID has a 64 character limit and can only
 contain letters, numbers, periods, dashes, and underscores.


Type: String




## Examples


### First Sample Request


Retrieve a metrics configuration that filters metrics based on a specified prefix.



```

            GET /?metrics&id=Documents HTTP/1.1
            Host: amzn-s3-demo-bucket.s3.<Region>.amazonaws.com
            x-amz-date: Thu, 15 Nov 2016 00:17:21 GMT
            Authorization: signatureValue
         
```

### First Sample Response


This example illustrates one usage of GetBucketMetricsConfiguration.



```

            HTTP/1.1 200 OK
            x-amz-id-2: ITnGT1y4REXAMPLEPi4hklTXouTf0hccUjo0iCPEXAMPLEutBj3M7fPGlWO2SEWp
            x-amz-request-id: 51991EXAMPLE5321
            Date: Thu, 15 Nov 2016 00:17:22 GMT
            Server: AmazonS3
            Content-Length: 180
 
            <?xml version="1.0" encoding="UTF-8"?>
            <MetricsConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
               <Id>Documents</Id>
              <Filter>
                  <Prefix>documents/</Prefix>
              </Filter>
            </MetricsConfiguration>
         
```

### Second Sample Request


Retrieve a metrics configuration that enables metrics for objects that start with a particular
 prefix and have specific tags applied.



```

            GET /?metrics&id=ImportantBlueDocuments HTTP/1.1
            Host: amzn-s3-demo-bucket.s3.<Region>.amazonaws.com
            x-amz-date: Thu, 15 Nov 2016 00:17:21 GMT
            Authorization: signatureValue
         
```

### Second Sample Response


This example illustrates one usage of GetBucketMetricsConfiguration.



```

            HTTP/1.1 200 OK
            x-amz-id-2: ITnGT1y4REXAMPLEPi4hklTXouTf0hccUjo0iCPEXAMPLEutBj3M7fPGlWO2SEWp
            x-amz-request-id: 51991EXAMPLE5321
            Date: Thu, 15 Nov 2016 00:17:22 GMT
            Server: AmazonS3
            Content-Length: 480

            <?xml version="1.0" encoding="UTF-8"?>
            <MetricsConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
              <Id>ImportantBlueDocuments</Id>
              <Filter>
                  <And>
                      <Prefix>documents/</Prefix>
                      <Tag>
                          <Key>priority</Key>
                          <Value>high</Value>
                      </Tag>
                      <Tag>
                            <Key>class</Key>
                            <Value>blue</Value>
                      </Tag>
                   </And>
               </Filter>
            </MetricsConfiguration>
         
```

### Third Sample Request


Retrieve a metrics configuration that enables metrics for a specific access point.



```

            GET /?metrics&id=ImportantDocumentsAccessPoint HTTP/1.1
            Host: amzn-s3-demo-bucket.s3.<Region>.amazonaws.com
            x-amz-date: Thu, 26 Aug 2021 00:17:21 GMT
            Authorization: signatureValue
         
```

### Third Sample Response


This example illustrates one usage of GetBucketMetricsConfiguration.



```

            HTTP/1.1 200 OK
            x-amz-id-2: ITnGT1y4REXAMPLEPi4hklTXouTf0hccUjo0iCPEXAMPLEutBj3M7fPGlWO2SEWp
            x-amz-request-id: 51991EXAMPLE5321
            Date: Thu, 26 Aug 2021 00:17:22 GMT
            Server: AmazonS3
            Content-Length: 480

            <?xml version="1.0" encoding="UTF-8"?>
            <MetricsConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
              <Id>ImportantDocumentsAccessPoint</Id>
              <Filter>
                  <AccessPointArn>arn:aws:s3:us-west-2:123456789012:accesspoint/test</AccessPointArn>
               </Filter>
            </MetricsConfiguration>
         
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetBucketMetricsConfiguration "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetBucketMetricsConfiguration")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/GetBucketMetricsConfiguration "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/GetBucketMetricsConfiguration")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetBucketMetricsConfiguration "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetBucketMetricsConfiguration")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetBucketMetricsConfiguration "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetBucketMetricsConfiguration")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetBucketMetricsConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetBucketMetricsConfiguration")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetBucketMetricsConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetBucketMetricsConfiguration")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetBucketMetricsConfiguration "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetBucketMetricsConfiguration")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetBucketMetricsConfiguration "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetBucketMetricsConfiguration")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetBucketMetricsConfiguration "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetBucketMetricsConfiguration")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetBucketMetricsConfiguration "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetBucketMetricsConfiguration")
