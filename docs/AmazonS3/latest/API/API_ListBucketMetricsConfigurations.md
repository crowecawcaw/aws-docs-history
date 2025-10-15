# ListBucketMetricsConfigurations

###### Note

This operation is not supported for directory buckets.

Lists the metrics configurations for the bucket. The metrics configurations are only for the request
 metrics of the bucket and do not provide information on daily storage metrics. You can have up to 1,000
 configurations per bucket.

This action supports list pagination and does not return more than 100 configurations at a time.
 Always check the `IsTruncated` element in the response. If there are no more configurations
 to list, `IsTruncated` is set to false. If there are more configurations to list,
 `IsTruncated` is set to true, and there is a value in `NextContinuationToken`.
 You use the `NextContinuationToken` value to continue the pagination of the list by passing
 the value in `continuation-token` in the request to `GET` the next page.

To use this operation, you must have permissions to perform the
 `s3:GetMetricsConfiguration` action. The bucket owner has this permission by default. The
 bucket owner can grant this permission to others. For more information about permissions, see [Permissions Related to Bucket Subresource Operations](../userguide/using-with-s3-actions.md#using-with-s3-actions-related-to-bucket-subresources "../userguide/using-with-s3-actions.md#using-with-s3-actions-related-to-bucket-subresources") and [Managing Access Permissions to Your Amazon S3
 Resources](../userguide/s3-access-control.md "../userguide/s3-access-control.md").

For more information about metrics configurations and CloudWatch request metrics, see [Monitoring Metrics with
 Amazon CloudWatch](https://docs.aws.amazon.com/AmazonS3/latest/dev/cloudwatch-monitoring.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/cloudwatch-monitoring.html").

The following operations are related to `ListBucketMetricsConfigurations`:


* [PutBucketMetricsConfiguration](API_PutBucketMetricsConfiguration.md "API_PutBucketMetricsConfiguration.md")
* [GetBucketMetricsConfiguration](API_GetBucketMetricsConfiguration.md "API_GetBucketMetricsConfiguration.md")
* [DeleteBucketMetricsConfiguration](API_DeleteBucketMetricsConfiguration.md "API_DeleteBucketMetricsConfiguration.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
GET /?metrics&continuation-token=`ContinuationToken` HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
x-amz-expected-bucket-owner: `ExpectedBucketOwner`

```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_ListBucketMetricsConfigurations_RequestSyntax "#API_ListBucketMetricsConfigurations_RequestSyntax")**


The name of the bucket containing the metrics configurations to retrieve.


Required: Yes




**[continuation-token](#API_ListBucketMetricsConfigurations_RequestSyntax "#API_ListBucketMetricsConfigurations_RequestSyntax")**


The marker that is used to continue a metrics configuration listing that has been truncated. Use the
 `NextContinuationToken` from a previously truncated list response to continue the listing.
 The continuation token is an opaque value that Amazon S3 understands.




**[x-amz-expected-bucket-owner](#API_ListBucketMetricsConfigurations_RequestSyntax "#API_ListBucketMetricsConfigurations_RequestSyntax")**


The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<[ListMetricsConfigurationsResult](#AmazonS3-ListBucketMetricsConfigurations-response-ListBucketMetricsConfigurationsOutput "#AmazonS3-ListBucketMetricsConfigurations-response-ListBucketMetricsConfigurationsOutput")>
   <[IsTruncated](#AmazonS3-ListBucketMetricsConfigurations-response-IsTruncated "#AmazonS3-ListBucketMetricsConfigurations-response-IsTruncated")>***boolean***</[IsTruncated](#AmazonS3-ListBucketMetricsConfigurations-response-IsTruncated "#AmazonS3-ListBucketMetricsConfigurations-response-IsTruncated")>
   <[ContinuationToken](#AmazonS3-ListBucketMetricsConfigurations-response-ContinuationToken "#AmazonS3-ListBucketMetricsConfigurations-response-ContinuationToken")>***string***</[ContinuationToken](#AmazonS3-ListBucketMetricsConfigurations-response-ContinuationToken "#AmazonS3-ListBucketMetricsConfigurations-response-ContinuationToken")>
   <[NextContinuationToken](#AmazonS3-ListBucketMetricsConfigurations-response-NextContinuationToken "#AmazonS3-ListBucketMetricsConfigurations-response-NextContinuationToken")>***string***</[NextContinuationToken](#AmazonS3-ListBucketMetricsConfigurations-response-NextContinuationToken "#AmazonS3-ListBucketMetricsConfigurations-response-NextContinuationToken")>
   <[MetricsConfiguration](#AmazonS3-ListBucketMetricsConfigurations-response-MetricsConfigurationList "#AmazonS3-ListBucketMetricsConfigurations-response-MetricsConfigurationList")>
      <[Filter](API_MetricsConfiguration.md#AmazonS3-Type-MetricsConfiguration-Filter "API_MetricsConfiguration.md#AmazonS3-Type-MetricsConfiguration-Filter")>
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
      </[Filter](API_MetricsConfiguration.md#AmazonS3-Type-MetricsConfiguration-Filter "API_MetricsConfiguration.md#AmazonS3-Type-MetricsConfiguration-Filter")>
      <[Id](API_MetricsConfiguration.md#AmazonS3-Type-MetricsConfiguration-Id "API_MetricsConfiguration.md#AmazonS3-Type-MetricsConfiguration-Id")>***string***</[Id](API_MetricsConfiguration.md#AmazonS3-Type-MetricsConfiguration-Id "API_MetricsConfiguration.md#AmazonS3-Type-MetricsConfiguration-Id")>
   </[MetricsConfiguration](#AmazonS3-ListBucketMetricsConfigurations-response-MetricsConfigurationList "#AmazonS3-ListBucketMetricsConfigurations-response-MetricsConfigurationList")>
   ...
</[ListMetricsConfigurationsResult](#AmazonS3-ListBucketMetricsConfigurations-response-ListBucketMetricsConfigurationsOutput "#AmazonS3-ListBucketMetricsConfigurations-response-ListBucketMetricsConfigurationsOutput")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[ListMetricsConfigurationsResult](#API_ListBucketMetricsConfigurations_ResponseSyntax "#API_ListBucketMetricsConfigurations_ResponseSyntax")**


Root level tag for the ListMetricsConfigurationsResult parameters.


Required: Yes




**[ContinuationToken](#API_ListBucketMetricsConfigurations_ResponseSyntax "#API_ListBucketMetricsConfigurations_ResponseSyntax")**


The marker that is used as a starting point for this metrics configuration list response. This value
 is present if it was sent in the request.


Type: String




**[IsTruncated](#API_ListBucketMetricsConfigurations_ResponseSyntax "#API_ListBucketMetricsConfigurations_ResponseSyntax")**


Indicates whether the returned list of metrics configurations is complete. A value of true indicates
 that the list is not complete and the NextContinuationToken will be provided for a subsequent
 request.


Type: Boolean




**[MetricsConfiguration](#API_ListBucketMetricsConfigurations_ResponseSyntax "#API_ListBucketMetricsConfigurations_ResponseSyntax")**


The list of metrics configurations for a bucket.


Type: Array of [MetricsConfiguration](API_MetricsConfiguration.md "API_MetricsConfiguration.md") data types




**[NextContinuationToken](#API_ListBucketMetricsConfigurations_ResponseSyntax "#API_ListBucketMetricsConfigurations_ResponseSyntax")**


The marker used to continue a metrics configuration listing that has been truncated. Use the
 `NextContinuationToken` from a previously truncated list response to continue the listing.
 The continuation token is an opaque value that Amazon S3 understands.


Type: String




## Examples


### Sample Request


Delete the metric configuration with a specified ID, which disables the CloudWatch metrics with
 the `ExampleMetrics` value for the `FilterId` dimension. 



```

GET /?metrics HTTP/1.1
Host: examplebucket.s3.<Region>.amazonaws.com
x-amz-date: Thu, 15 Nov 2016 00:17:21 GMT
Authorization: signatureValue
         
```

### Sample Response


Delete the metric configuration with a specified ID, which disables the CloudWatch metrics with
 the `ExampleMetrics` value for the `FilterId` dimension. 



```

HTTP/1.1 200 OK
x-amz-id-2: ITnGT1y4REXAMPLEPi4hklTXouTf0hccUjo0iCPEXAMPLEutBj3M7fPGlWO2SEWp
x-amz-request-id: 51991EXAMPLE5321
Date: Thu, 15 Nov 2016 00:17:22 GMT
Server: AmazonS3
Content-Length: 758
 
<?xml version="1.0" encoding="UTF-8"?>
<ListMetricsConfigurationsResult xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
    <MetricsConfiguration>
        <Id>EntireBucket</Id>
    </MetricsConfiguration>
    <MetricsConfiguration>
        <Id>Documents</Id>
        <Filter>
            <Prefix>documents/</Prefix>
        </Filter>
    </MetricsConfiguration>
    <MetricsConfiguration>
        <Id>BlueDocuments</Id>
        <Filter>
            <And>
                <Prefix>documents/</Prefix>
                <Tag>
                    <Key>class</Key>
                    <Value>blue</Value>
                </Tag>
            </And>
        </Filter>
    </MetricsConfiguration>
    <IsTruncated>false</IsTruncated>
</ListMetricsConfigurationsResult>
         
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/ListBucketMetricsConfigurations "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/ListBucketMetricsConfigurations")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/ListBucketMetricsConfigurations "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/ListBucketMetricsConfigurations")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/ListBucketMetricsConfigurations "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/ListBucketMetricsConfigurations")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/ListBucketMetricsConfigurations "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/ListBucketMetricsConfigurations")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/ListBucketMetricsConfigurations "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/ListBucketMetricsConfigurations")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/ListBucketMetricsConfigurations "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/ListBucketMetricsConfigurations")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/ListBucketMetricsConfigurations "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/ListBucketMetricsConfigurations")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/ListBucketMetricsConfigurations "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/ListBucketMetricsConfigurations")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/ListBucketMetricsConfigurations "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/ListBucketMetricsConfigurations")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/ListBucketMetricsConfigurations "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/ListBucketMetricsConfigurations")
