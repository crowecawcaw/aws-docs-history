# GetBucketAnalyticsConfiguration

###### Note

This operation is not supported for directory buckets.

This implementation of the GET action returns an analytics configuration (identified by the
 analytics configuration ID) from the bucket.

To use this operation, you must have permissions to perform the
 `s3:GetAnalyticsConfiguration` action. The bucket owner has this permission by default. The
 bucket owner can grant this permission to others. For more information about permissions, see  [Permissions Related to Bucket Subresource Operations](../userguide/using-with-s3-actions.md#using-with-s3-actions-related-to-bucket-subresources "../userguide/using-with-s3-actions.md#using-with-s3-actions-related-to-bucket-subresources") and [Managing Access Permissions to Your Amazon S3
 Resources](../userguide/s3-access-control.md "../userguide/s3-access-control.md") in the *Amazon S3 User Guide*. 

For information about Amazon S3 analytics feature, see [Amazon S3 Analytics – Storage Class Analysis](https://docs.aws.amazon.com/AmazonS3/latest/dev/analytics-storage-class.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/analytics-storage-class.html")
 in the *Amazon S3 User Guide*.

The following operations are related to `GetBucketAnalyticsConfiguration`:


* [DeleteBucketAnalyticsConfiguration](API_DeleteBucketAnalyticsConfiguration.md "API_DeleteBucketAnalyticsConfiguration.md")
* [ListBucketAnalyticsConfigurations](API_ListBucketAnalyticsConfigurations.md "API_ListBucketAnalyticsConfigurations.md")
* [PutBucketAnalyticsConfiguration](API_PutBucketAnalyticsConfiguration.md "API_PutBucketAnalyticsConfiguration.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
GET /?analytics&id=`Id` HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
x-amz-expected-bucket-owner: `ExpectedBucketOwner`

```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_GetBucketAnalyticsConfiguration_RequestSyntax "#API_GetBucketAnalyticsConfiguration_RequestSyntax")**


The name of the bucket from which an analytics configuration is retrieved.


Required: Yes




**[id](#API_GetBucketAnalyticsConfiguration_RequestSyntax "#API_GetBucketAnalyticsConfiguration_RequestSyntax")**


The ID that identifies the analytics configuration.


Required: Yes




**[x-amz-expected-bucket-owner](#API_GetBucketAnalyticsConfiguration_RequestSyntax "#API_GetBucketAnalyticsConfiguration_RequestSyntax")**


The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<[AnalyticsConfiguration](#AmazonS3-GetBucketAnalyticsConfiguration-response-AnalyticsConfiguration "#AmazonS3-GetBucketAnalyticsConfiguration-response-AnalyticsConfiguration")>
   <[Id](#AmazonS3-GetBucketAnalyticsConfiguration-response-Id "#AmazonS3-GetBucketAnalyticsConfiguration-response-Id")>***string***</[Id](#AmazonS3-GetBucketAnalyticsConfiguration-response-Id "#AmazonS3-GetBucketAnalyticsConfiguration-response-Id")>
   <[Filter](#AmazonS3-GetBucketAnalyticsConfiguration-response-Filter "#AmazonS3-GetBucketAnalyticsConfiguration-response-Filter")>
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
   </[Filter](#AmazonS3-GetBucketAnalyticsConfiguration-response-Filter "#AmazonS3-GetBucketAnalyticsConfiguration-response-Filter")>
   <[StorageClassAnalysis](#AmazonS3-GetBucketAnalyticsConfiguration-response-StorageClassAnalysis "#AmazonS3-GetBucketAnalyticsConfiguration-response-StorageClassAnalysis")>
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
   </[StorageClassAnalysis](#AmazonS3-GetBucketAnalyticsConfiguration-response-StorageClassAnalysis "#AmazonS3-GetBucketAnalyticsConfiguration-response-StorageClassAnalysis")>
</[AnalyticsConfiguration](#AmazonS3-GetBucketAnalyticsConfiguration-response-AnalyticsConfiguration "#AmazonS3-GetBucketAnalyticsConfiguration-response-AnalyticsConfiguration")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[AnalyticsConfiguration](#API_GetBucketAnalyticsConfiguration_ResponseSyntax "#API_GetBucketAnalyticsConfiguration_ResponseSyntax")**


Root level tag for the AnalyticsConfiguration parameters.


Required: Yes




**[Filter](#API_GetBucketAnalyticsConfiguration_ResponseSyntax "#API_GetBucketAnalyticsConfiguration_ResponseSyntax")**


The filter used to describe a set of objects for analyses. A filter must have exactly one prefix,
 one tag, or one conjunction (AnalyticsAndOperator). If no filter is provided, all objects will be
 considered in any analysis.


Type: [AnalyticsFilter](API_AnalyticsFilter.md "API_AnalyticsFilter.md") data type




**[Id](#API_GetBucketAnalyticsConfiguration_ResponseSyntax "#API_GetBucketAnalyticsConfiguration_ResponseSyntax")**


The ID that identifies the analytics configuration.


Type: String




**[StorageClassAnalysis](#API_GetBucketAnalyticsConfiguration_ResponseSyntax "#API_GetBucketAnalyticsConfiguration_ResponseSyntax")**


 Contains data related to access patterns to be collected and made available to analyze the
 tradeoffs between different storage classes. 


Type: [StorageClassAnalysis](API_StorageClassAnalysis.md "API_StorageClassAnalysis.md") data type




## Examples


### Configure an Analytics Report


The following GET request for the bucket `amzn-s3-demo-bucket` returns the inventory
 configuration with the ID `list1`: 



```

GET /?analytics&id=list1 HTTP/1.1
Host: amzn-s3-demo-bucket.s3.<Region>.amazonaws.com
Date: Mon, 31 Oct 2016 12:00:00 GMT
Authorization: authorization string
           
```

### Example


The following is a sample response to the preceding GET request.



```

HTTP/1.1 200 OK
x-amz-id-2: YgIPIfBiKa2bj0KMgUAdQkf3ShJTOOpXUueF6QKo
x-amz-request-id: 236A8905248E5A02
Date: Mon, 31 Oct 2016 12:00:00 GMT
Server: AmazonS3
Content-Length: length

<?xml version="1.0" encoding="UTF-8"?>
<AnalyticsConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
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
           
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetBucketAnalyticsConfiguration "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetBucketAnalyticsConfiguration")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/GetBucketAnalyticsConfiguration "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/GetBucketAnalyticsConfiguration")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetBucketAnalyticsConfiguration "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetBucketAnalyticsConfiguration")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetBucketAnalyticsConfiguration "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetBucketAnalyticsConfiguration")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetBucketAnalyticsConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetBucketAnalyticsConfiguration")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetBucketAnalyticsConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetBucketAnalyticsConfiguration")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetBucketAnalyticsConfiguration "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetBucketAnalyticsConfiguration")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetBucketAnalyticsConfiguration "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetBucketAnalyticsConfiguration")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetBucketAnalyticsConfiguration "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetBucketAnalyticsConfiguration")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetBucketAnalyticsConfiguration "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetBucketAnalyticsConfiguration")
