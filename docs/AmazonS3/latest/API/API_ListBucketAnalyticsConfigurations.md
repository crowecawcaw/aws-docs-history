# ListBucketAnalyticsConfigurations

###### Note

This operation is not supported for directory buckets.

Lists the analytics configurations for the bucket. You can have up to 1,000 analytics configurations
 per bucket.

This action supports list pagination and does not return more than 100 configurations at a time. You
 should always check the `IsTruncated` element in the response. If there are no more
 configurations to list, `IsTruncated` is set to false. If there are more configurations to
 list, `IsTruncated` is set to true, and there will be a value in
 `NextContinuationToken`. You use the `NextContinuationToken` value to continue
 the pagination of the list by passing the value in continuation-token in the request to `GET`
 the next page.

To use this operation, you must have permissions to perform the
 `s3:GetAnalyticsConfiguration` action. The bucket owner has this permission by default. The
 bucket owner can grant this permission to others. For more information about permissions, see [Permissions Related to Bucket Subresource Operations](../userguide/using-with-s3-actions.md#using-with-s3-actions-related-to-bucket-subresources "../userguide/using-with-s3-actions.md#using-with-s3-actions-related-to-bucket-subresources") and [Managing Access Permissions to Your Amazon S3
 Resources](../userguide/s3-access-control.md "../userguide/s3-access-control.md").

For information about Amazon S3 analytics feature, see [Amazon S3 Analytics – Storage Class
 Analysis](https://docs.aws.amazon.com/AmazonS3/latest/dev/analytics-storage-class.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/analytics-storage-class.html"). 

The following operations are related to `ListBucketAnalyticsConfigurations`:


* [GetBucketAnalyticsConfiguration](API_GetBucketAnalyticsConfiguration.md "API_GetBucketAnalyticsConfiguration.md")
* [DeleteBucketAnalyticsConfiguration](API_DeleteBucketAnalyticsConfiguration.md "API_DeleteBucketAnalyticsConfiguration.md")
* [PutBucketAnalyticsConfiguration](API_PutBucketAnalyticsConfiguration.md "API_PutBucketAnalyticsConfiguration.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
GET /?analytics&continuation-token=`ContinuationToken` HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
x-amz-expected-bucket-owner: `ExpectedBucketOwner`

```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_ListBucketAnalyticsConfigurations_RequestSyntax "#API_ListBucketAnalyticsConfigurations_RequestSyntax")**


The name of the bucket from which analytics configurations are retrieved.


Required: Yes




**[continuation-token](#API_ListBucketAnalyticsConfigurations_RequestSyntax "#API_ListBucketAnalyticsConfigurations_RequestSyntax")**


The `ContinuationToken` that represents a placeholder from where this request should
 begin.




**[x-amz-expected-bucket-owner](#API_ListBucketAnalyticsConfigurations_RequestSyntax "#API_ListBucketAnalyticsConfigurations_RequestSyntax")**


The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<[ListBucketAnalyticsConfigurationResult](#AmazonS3-ListBucketAnalyticsConfigurations-response-ListBucketAnalyticsConfigurationsOutput "#AmazonS3-ListBucketAnalyticsConfigurations-response-ListBucketAnalyticsConfigurationsOutput")>
   <[IsTruncated](#AmazonS3-ListBucketAnalyticsConfigurations-response-IsTruncated "#AmazonS3-ListBucketAnalyticsConfigurations-response-IsTruncated")>***boolean***</[IsTruncated](#AmazonS3-ListBucketAnalyticsConfigurations-response-IsTruncated "#AmazonS3-ListBucketAnalyticsConfigurations-response-IsTruncated")>
   <[ContinuationToken](#AmazonS3-ListBucketAnalyticsConfigurations-response-ContinuationToken "#AmazonS3-ListBucketAnalyticsConfigurations-response-ContinuationToken")>***string***</[ContinuationToken](#AmazonS3-ListBucketAnalyticsConfigurations-response-ContinuationToken "#AmazonS3-ListBucketAnalyticsConfigurations-response-ContinuationToken")>
   <[NextContinuationToken](#AmazonS3-ListBucketAnalyticsConfigurations-response-NextContinuationToken "#AmazonS3-ListBucketAnalyticsConfigurations-response-NextContinuationToken")>***string***</[NextContinuationToken](#AmazonS3-ListBucketAnalyticsConfigurations-response-NextContinuationToken "#AmazonS3-ListBucketAnalyticsConfigurations-response-NextContinuationToken")>
   <[AnalyticsConfiguration](#AmazonS3-ListBucketAnalyticsConfigurations-response-AnalyticsConfigurationList "#AmazonS3-ListBucketAnalyticsConfigurations-response-AnalyticsConfigurationList")>
      <[Filter](API_AnalyticsConfiguration.md#AmazonS3-Type-AnalyticsConfiguration-Filter "API_AnalyticsConfiguration.md#AmazonS3-Type-AnalyticsConfiguration-Filter")>
         <[And](API_AnalyticsFilter.md#AmazonS3-Type-AnalyticsFilter-And "API_AnalyticsFilter.md#AmazonS3-Type-AnalyticsFilter-And")>
            <[Prefix](API_AnalyticsAndOperator.md#AmazonS3-Type-AnalyticsAndOperator-Prefix "API_AnalyticsAndOperator.md#AmazonS3-Type-AnalyticsAndOperator-Prefix")>***string***</[Prefix](API_AnalyticsAndOperator.md#AmazonS3-Type-AnalyticsAndOperator-Prefix "API_AnalyticsAndOperator.md#AmazonS3-Type-AnalyticsAndOperator-Prefix")>
            <[Tag](API_AnalyticsAndOperator.md#AmazonS3-Type-AnalyticsAndOperator-Tags "API_AnalyticsAndOperator.md#AmazonS3-Type-AnalyticsAndOperator-Tags")>
               <[Key](API_Tag.md#AmazonS3-Type-Tag-Key "API_Tag.md#AmazonS3-Type-Tag-Key")>***string***</[Key](API_Tag.md#AmazonS3-Type-Tag-Key "API_Tag.md#AmazonS3-Type-Tag-Key")>
               <[Value](API_Tag.md#AmazonS3-Type-Tag-Value "API_Tag.md#AmazonS3-Type-Tag-Value")>***string***</[Value](API_Tag.md#AmazonS3-Type-Tag-Value "API_Tag.md#AmazonS3-Type-Tag-Value")>
            </[Tag](API_AnalyticsAndOperator.md#AmazonS3-Type-AnalyticsAndOperator-Tags "API_AnalyticsAndOperator.md#AmazonS3-Type-AnalyticsAndOperator-Tags")>
            ...
         </[And](API_AnalyticsFilter.md#AmazonS3-Type-AnalyticsFilter-And "API_AnalyticsFilter.md#AmazonS3-Type-AnalyticsFilter-And")>
         <[Prefix](API_AnalyticsFilter.md#AmazonS3-Type-AnalyticsFilter-Prefix "API_AnalyticsFilter.md#AmazonS3-Type-AnalyticsFilter-Prefix")>***string***</[Prefix](API_AnalyticsFilter.md#AmazonS3-Type-AnalyticsFilter-Prefix "API_AnalyticsFilter.md#AmazonS3-Type-AnalyticsFilter-Prefix")>
         <[Tag](API_AnalyticsFilter.md#AmazonS3-Type-AnalyticsFilter-Tag "API_AnalyticsFilter.md#AmazonS3-Type-AnalyticsFilter-Tag")>
            <[Key](API_Tag.md#AmazonS3-Type-Tag-Key "API_Tag.md#AmazonS3-Type-Tag-Key")>***string***</[Key](API_Tag.md#AmazonS3-Type-Tag-Key "API_Tag.md#AmazonS3-Type-Tag-Key")>
            <[Value](API_Tag.md#AmazonS3-Type-Tag-Value "API_Tag.md#AmazonS3-Type-Tag-Value")>***string***</[Value](API_Tag.md#AmazonS3-Type-Tag-Value "API_Tag.md#AmazonS3-Type-Tag-Value")>
         </[Tag](API_AnalyticsFilter.md#AmazonS3-Type-AnalyticsFilter-Tag "API_AnalyticsFilter.md#AmazonS3-Type-AnalyticsFilter-Tag")>
      </[Filter](API_AnalyticsConfiguration.md#AmazonS3-Type-AnalyticsConfiguration-Filter "API_AnalyticsConfiguration.md#AmazonS3-Type-AnalyticsConfiguration-Filter")>
      <[Id](API_AnalyticsConfiguration.md#AmazonS3-Type-AnalyticsConfiguration-Id "API_AnalyticsConfiguration.md#AmazonS3-Type-AnalyticsConfiguration-Id")>***string***</[Id](API_AnalyticsConfiguration.md#AmazonS3-Type-AnalyticsConfiguration-Id "API_AnalyticsConfiguration.md#AmazonS3-Type-AnalyticsConfiguration-Id")>
      <[StorageClassAnalysis](API_AnalyticsConfiguration.md#AmazonS3-Type-AnalyticsConfiguration-StorageClassAnalysis "API_AnalyticsConfiguration.md#AmazonS3-Type-AnalyticsConfiguration-StorageClassAnalysis")>
         <[DataExport](API_StorageClassAnalysis.md#AmazonS3-Type-StorageClassAnalysis-DataExport "API_StorageClassAnalysis.md#AmazonS3-Type-StorageClassAnalysis-DataExport")>
            <[Destination](API_StorageClassAnalysisDataExport.md#AmazonS3-Type-StorageClassAnalysisDataExport-Destination "API_StorageClassAnalysisDataExport.md#AmazonS3-Type-StorageClassAnalysisDataExport-Destination")>
               <[S3BucketDestination](API_AnalyticsExportDestination.md#AmazonS3-Type-AnalyticsExportDestination-S3BucketDestination "API_AnalyticsExportDestination.md#AmazonS3-Type-AnalyticsExportDestination-S3BucketDestination")>
                  <[Bucket](API_AnalyticsS3BucketDestination.md#AmazonS3-Type-AnalyticsS3BucketDestination-Bucket "API_AnalyticsS3BucketDestination.md#AmazonS3-Type-AnalyticsS3BucketDestination-Bucket")>***string***</[Bucket](API_AnalyticsS3BucketDestination.md#AmazonS3-Type-AnalyticsS3BucketDestination-Bucket "API_AnalyticsS3BucketDestination.md#AmazonS3-Type-AnalyticsS3BucketDestination-Bucket")>
                  <[BucketAccountId](API_AnalyticsS3BucketDestination.md#AmazonS3-Type-AnalyticsS3BucketDestination-BucketAccountId "API_AnalyticsS3BucketDestination.md#AmazonS3-Type-AnalyticsS3BucketDestination-BucketAccountId")>***string***</[BucketAccountId](API_AnalyticsS3BucketDestination.md#AmazonS3-Type-AnalyticsS3BucketDestination-BucketAccountId "API_AnalyticsS3BucketDestination.md#AmazonS3-Type-AnalyticsS3BucketDestination-BucketAccountId")>
                  <[Format](API_AnalyticsS3BucketDestination.md#AmazonS3-Type-AnalyticsS3BucketDestination-Format "API_AnalyticsS3BucketDestination.md#AmazonS3-Type-AnalyticsS3BucketDestination-Format")>***string***</[Format](API_AnalyticsS3BucketDestination.md#AmazonS3-Type-AnalyticsS3BucketDestination-Format "API_AnalyticsS3BucketDestination.md#AmazonS3-Type-AnalyticsS3BucketDestination-Format")>
                  <[Prefix](API_AnalyticsS3BucketDestination.md#AmazonS3-Type-AnalyticsS3BucketDestination-Prefix "API_AnalyticsS3BucketDestination.md#AmazonS3-Type-AnalyticsS3BucketDestination-Prefix")>***string***</[Prefix](API_AnalyticsS3BucketDestination.md#AmazonS3-Type-AnalyticsS3BucketDestination-Prefix "API_AnalyticsS3BucketDestination.md#AmazonS3-Type-AnalyticsS3BucketDestination-Prefix")>
               </[S3BucketDestination](API_AnalyticsExportDestination.md#AmazonS3-Type-AnalyticsExportDestination-S3BucketDestination "API_AnalyticsExportDestination.md#AmazonS3-Type-AnalyticsExportDestination-S3BucketDestination")>
            </[Destination](API_StorageClassAnalysisDataExport.md#AmazonS3-Type-StorageClassAnalysisDataExport-Destination "API_StorageClassAnalysisDataExport.md#AmazonS3-Type-StorageClassAnalysisDataExport-Destination")>
            <[OutputSchemaVersion](API_StorageClassAnalysisDataExport.md#AmazonS3-Type-StorageClassAnalysisDataExport-OutputSchemaVersion "API_StorageClassAnalysisDataExport.md#AmazonS3-Type-StorageClassAnalysisDataExport-OutputSchemaVersion")>***string***</[OutputSchemaVersion](API_StorageClassAnalysisDataExport.md#AmazonS3-Type-StorageClassAnalysisDataExport-OutputSchemaVersion "API_StorageClassAnalysisDataExport.md#AmazonS3-Type-StorageClassAnalysisDataExport-OutputSchemaVersion")>
         </[DataExport](API_StorageClassAnalysis.md#AmazonS3-Type-StorageClassAnalysis-DataExport "API_StorageClassAnalysis.md#AmazonS3-Type-StorageClassAnalysis-DataExport")>
      </[StorageClassAnalysis](API_AnalyticsConfiguration.md#AmazonS3-Type-AnalyticsConfiguration-StorageClassAnalysis "API_AnalyticsConfiguration.md#AmazonS3-Type-AnalyticsConfiguration-StorageClassAnalysis")>
   </[AnalyticsConfiguration](#AmazonS3-ListBucketAnalyticsConfigurations-response-AnalyticsConfigurationList "#AmazonS3-ListBucketAnalyticsConfigurations-response-AnalyticsConfigurationList")>
   ...
</[ListBucketAnalyticsConfigurationResult](#AmazonS3-ListBucketAnalyticsConfigurations-response-ListBucketAnalyticsConfigurationsOutput "#AmazonS3-ListBucketAnalyticsConfigurations-response-ListBucketAnalyticsConfigurationsOutput")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[ListBucketAnalyticsConfigurationResult](#API_ListBucketAnalyticsConfigurations_ResponseSyntax "#API_ListBucketAnalyticsConfigurations_ResponseSyntax")**


Root level tag for the ListBucketAnalyticsConfigurationResult parameters.


Required: Yes




**[AnalyticsConfiguration](#API_ListBucketAnalyticsConfigurations_ResponseSyntax "#API_ListBucketAnalyticsConfigurations_ResponseSyntax")**


The list of analytics configurations for a bucket.


Type: Array of [AnalyticsConfiguration](API_AnalyticsConfiguration.md "API_AnalyticsConfiguration.md") data types




**[ContinuationToken](#API_ListBucketAnalyticsConfigurations_ResponseSyntax "#API_ListBucketAnalyticsConfigurations_ResponseSyntax")**


The marker that is used as a starting point for this analytics configuration list response. This
 value is present if it was sent in the request.


Type: String




**[IsTruncated](#API_ListBucketAnalyticsConfigurations_ResponseSyntax "#API_ListBucketAnalyticsConfigurations_ResponseSyntax")**


Indicates whether the returned list of analytics configurations is complete. A value of true
 indicates that the list is not complete and the NextContinuationToken will be provided for a subsequent
 request.


Type: Boolean




**[NextContinuationToken](#API_ListBucketAnalyticsConfigurations_ResponseSyntax "#API_ListBucketAnalyticsConfigurations_ResponseSyntax")**



`NextContinuationToken` is sent when `isTruncated` is true, which indicates
 that there are more analytics configurations to list. The next request must include this
 `NextContinuationToken`. The token is obfuscated and is not a usable value.


Type: String




## Examples


### Sample Request


Delete the metric configuration with a specified ID, which disables the CloudWatch metrics with
 the `ExampleMetrics` value for the `FilterId` dimension. 



```

            GET /?analytics HTTP/1.1
            Host: example-bucket.s3.<Region>.amazonaws.com
            x-amz-date: 20160430T233541Z
            Authorization: authorization string
         
```

### Sample Response


This example illustrates one usage of ListBucketAnalyticsConfigurations.



```

HTTP/1.1 200 OK
x-amz-id-2: gyB+3jRPnrkN98ZajxHXr3u7EFM67bNgSAxexeEHndCX/7GRnfTXxReKUQF28IfP
x-amz-request-id: 3B3C7C725673C630
Date: Sat, 30 Apr 2016 23:29:37 GMT
Content-Length: length
Server: AmazonS3

<ListBucketAnalyticsConfigurationResult xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
    <AnalyticsConfiguration>
        <Id>list1</Id>
        <Filter>
            <And>
                <Prefix>images/</Prefix>
                <Tag>
                    <Key>dog</Key>
                    <Value>corgi</Value>
                </Tag>
            </And>
        </Filter>
        <StorageClassAnalysis>
            <DataExport>
                <OutputSchemaVersion>V_1</OutputSchemaVersion>
                <Destination>
                    <S3BucketDestination>
                        <Format>CSV</Format>
                        <BucketAccountId>123456789012</BucketAccountId>
                        <Bucket>arn:aws:s3:::destination-bucket</Bucket>
                        <Prefix>destination-prefix</Prefix>
                    </S3BucketDestination>
                </Destination>
            </DataExport>
        </StorageClassAnalysis>
    </AnalyticsConfiguration>

    <AnalyticsConfiguration>
        <Id>report1</Id>
        <Filter>
            <And>
                <Prefix>images/</Prefix>
                <Tag>
                    <Key>dog</Key>
                    <Value>bulldog</Value>
                </Tag>
            </And>
        </Filter>
        <StorageClassAnalysis>
            <DataExport>
                <OutputSchemaVersion>V_1</OutputSchemaVersion>
                <Destination>
                    <S3BucketDestination>
                        <Format>CSV</Format>
                        <BucketAccountId>123456789012</BucketAccountId>
                        <Bucket>arn:aws:s3:::destination-bucket</Bucket>
                        <Prefix>destination-prefix</Prefix>
                    </S3BucketDestination>
                </Destination>
            </DataExport>
        </StorageClassAnalysis>
    </AnalyticsConfiguration>
    ...
    <IsTruncated>false</IsTruncated>
    <!-- If ContinuationToken was provided in the request. -->
    <ContinuationToken>...</ContinuationToken>
    <!-- if IsTruncated == true -->
    <IsTruncated>true</IsTruncated>
   <NextContinuationToken>...</NextContinuationToken>
</ListBucketAnalyticsConfigurationResult>
         
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/ListBucketAnalyticsConfigurations "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/ListBucketAnalyticsConfigurations")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/ListBucketAnalyticsConfigurations "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/ListBucketAnalyticsConfigurations")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/ListBucketAnalyticsConfigurations "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/ListBucketAnalyticsConfigurations")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/ListBucketAnalyticsConfigurations "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/ListBucketAnalyticsConfigurations")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/ListBucketAnalyticsConfigurations "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/ListBucketAnalyticsConfigurations")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/ListBucketAnalyticsConfigurations "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/ListBucketAnalyticsConfigurations")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/ListBucketAnalyticsConfigurations "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/ListBucketAnalyticsConfigurations")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/ListBucketAnalyticsConfigurations "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/ListBucketAnalyticsConfigurations")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/ListBucketAnalyticsConfigurations "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/ListBucketAnalyticsConfigurations")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/ListBucketAnalyticsConfigurations "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/ListBucketAnalyticsConfigurations")
