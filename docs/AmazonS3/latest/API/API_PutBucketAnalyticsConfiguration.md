# PutBucketAnalyticsConfiguration

###### Note

This operation is not supported for directory buckets.

Sets an analytics configuration for the bucket (specified by the analytics configuration ID). You
 can have up to 1,000 analytics configurations per bucket.

You can choose to have storage class analysis export analysis reports sent to a comma-separated
 values (CSV) flat file. See the `DataExport` request element. Reports are updated daily and
 are based on the object filters that you configure. When selecting data export, you specify a
 destination bucket and an optional destination prefix where the file is written. You can export the data
 to a destination bucket in a different account. However, the destination bucket must be in the same
 Region as the bucket that you are making the PUT analytics configuration to. For more information, see
 [Amazon S3 Analytics –
 Storage Class Analysis](https://docs.aws.amazon.com/AmazonS3/latest/dev/analytics-storage-class.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/analytics-storage-class.html"). 

###### Important

You must create a bucket policy on the destination bucket where the exported file is written to
 grant permissions to Amazon S3 to write objects to the bucket. For an example policy, see [Granting
 Permissions for Amazon S3 Inventory and Storage Class Analysis](https://docs.aws.amazon.com/AmazonS3/latest/dev/example-bucket-policies.html#example-bucket-policies-use-case-9 "https://docs.aws.amazon.com/AmazonS3/latest/dev/example-bucket-policies.html#example-bucket-policies-use-case-9").

To use this operation, you must have permissions to perform the
 `s3:PutAnalyticsConfiguration` action. The bucket owner has this permission by default. The
 bucket owner can grant this permission to others. For more information about permissions, see [Permissions Related to Bucket Subresource Operations](../userguide/using-with-s3-actions.md#using-with-s3-actions-related-to-bucket-subresources "../userguide/using-with-s3-actions.md#using-with-s3-actions-related-to-bucket-subresources") and [Managing Access Permissions to Your Amazon S3
 Resources](../userguide/s3-access-control.md "../userguide/s3-access-control.md").


`PutBucketAnalyticsConfiguration` has the following special errors:


* + *HTTP Error: HTTP 400 Bad Request*
	+ *Code: InvalidArgument*
	+ *Cause: Invalid argument.*
* + *HTTP Error: HTTP 400 Bad Request*
	+ *Code: TooManyConfigurations*
	+ *Cause: You are attempting to create a new configuration but have already reached
	 the 1,000-configuration limit.*
* + *HTTP Error: HTTP 403 Forbidden*
	+ *Code: AccessDenied*
	+ *Cause: You are not the owner of the specified bucket, or you do not have the
	 s3:PutAnalyticsConfiguration bucket permission to set the configuration on the
	 bucket.*
The following operations are related to `PutBucketAnalyticsConfiguration`:


* [GetBucketAnalyticsConfiguration](API_GetBucketAnalyticsConfiguration.md "API_GetBucketAnalyticsConfiguration.md")
* [DeleteBucketAnalyticsConfiguration](API_DeleteBucketAnalyticsConfiguration.md "API_DeleteBucketAnalyticsConfiguration.md")
* [ListBucketAnalyticsConfigurations](API_ListBucketAnalyticsConfigurations.md "API_ListBucketAnalyticsConfigurations.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
PUT /?analytics&id=`Id` HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
x-amz-expected-bucket-owner: `ExpectedBucketOwner`
<?xml version="1.0" encoding="UTF-8"?>
<[AnalyticsConfiguration](#AmazonS3-PutBucketAnalyticsConfiguration-request-AnalyticsConfiguration "#AmazonS3-PutBucketAnalyticsConfiguration-request-AnalyticsConfiguration") xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
   <[Id](#AmazonS3-PutBucketAnalyticsConfiguration-request-Id "#AmazonS3-PutBucketAnalyticsConfiguration-request-Id")>`string`</[Id](#AmazonS3-PutBucketAnalyticsConfiguration-request-Id "#AmazonS3-PutBucketAnalyticsConfiguration-request-Id")>
   <[Filter](#AmazonS3-PutBucketAnalyticsConfiguration-request-Filter "#AmazonS3-PutBucketAnalyticsConfiguration-request-Filter")>
      <[And](API_AnalyticsFilter.md#AmazonS3-Type-AnalyticsFilter-And "API_AnalyticsFilter.md#AmazonS3-Type-AnalyticsFilter-And")>
         <[Prefix](API_AnalyticsAndOperator.md#AmazonS3-Type-AnalyticsAndOperator-Prefix "API_AnalyticsAndOperator.md#AmazonS3-Type-AnalyticsAndOperator-Prefix")>`string`</[Prefix](API_AnalyticsAndOperator.md#AmazonS3-Type-AnalyticsAndOperator-Prefix "API_AnalyticsAndOperator.md#AmazonS3-Type-AnalyticsAndOperator-Prefix")>
         <[Tag](API_AnalyticsAndOperator.md#AmazonS3-Type-AnalyticsAndOperator-Tags "API_AnalyticsAndOperator.md#AmazonS3-Type-AnalyticsAndOperator-Tags")>
            <[Key](API_Tag.md#AmazonS3-Type-Tag-Key "API_Tag.md#AmazonS3-Type-Tag-Key")>`string`</[Key](API_Tag.md#AmazonS3-Type-Tag-Key "API_Tag.md#AmazonS3-Type-Tag-Key")>
            <[Value](API_Tag.md#AmazonS3-Type-Tag-Value "API_Tag.md#AmazonS3-Type-Tag-Value")>`string`</[Value](API_Tag.md#AmazonS3-Type-Tag-Value "API_Tag.md#AmazonS3-Type-Tag-Value")>
         </[Tag](API_AnalyticsAndOperator.md#AmazonS3-Type-AnalyticsAndOperator-Tags "API_AnalyticsAndOperator.md#AmazonS3-Type-AnalyticsAndOperator-Tags")>
         ...
      </[And](API_AnalyticsFilter.md#AmazonS3-Type-AnalyticsFilter-And "API_AnalyticsFilter.md#AmazonS3-Type-AnalyticsFilter-And")>
      <[Prefix](API_AnalyticsFilter.md#AmazonS3-Type-AnalyticsFilter-Prefix "API_AnalyticsFilter.md#AmazonS3-Type-AnalyticsFilter-Prefix")>`string`</[Prefix](API_AnalyticsFilter.md#AmazonS3-Type-AnalyticsFilter-Prefix "API_AnalyticsFilter.md#AmazonS3-Type-AnalyticsFilter-Prefix")>
      <[Tag](API_AnalyticsFilter.md#AmazonS3-Type-AnalyticsFilter-Tag "API_AnalyticsFilter.md#AmazonS3-Type-AnalyticsFilter-Tag")>
         <[Key](API_Tag.md#AmazonS3-Type-Tag-Key "API_Tag.md#AmazonS3-Type-Tag-Key")>`string`</[Key](API_Tag.md#AmazonS3-Type-Tag-Key "API_Tag.md#AmazonS3-Type-Tag-Key")>
         <[Value](API_Tag.md#AmazonS3-Type-Tag-Value "API_Tag.md#AmazonS3-Type-Tag-Value")>`string`</[Value](API_Tag.md#AmazonS3-Type-Tag-Value "API_Tag.md#AmazonS3-Type-Tag-Value")>
      </[Tag](API_AnalyticsFilter.md#AmazonS3-Type-AnalyticsFilter-Tag "API_AnalyticsFilter.md#AmazonS3-Type-AnalyticsFilter-Tag")>
   </[Filter](#AmazonS3-PutBucketAnalyticsConfiguration-request-Filter "#AmazonS3-PutBucketAnalyticsConfiguration-request-Filter")>
   <[StorageClassAnalysis](#AmazonS3-PutBucketAnalyticsConfiguration-request-StorageClassAnalysis "#AmazonS3-PutBucketAnalyticsConfiguration-request-StorageClassAnalysis")>
      <[DataExport](API_StorageClassAnalysis.md#AmazonS3-Type-StorageClassAnalysis-DataExport "API_StorageClassAnalysis.md#AmazonS3-Type-StorageClassAnalysis-DataExport")>
         <[Destination](API_StorageClassAnalysisDataExport.md#AmazonS3-Type-StorageClassAnalysisDataExport-Destination "API_StorageClassAnalysisDataExport.md#AmazonS3-Type-StorageClassAnalysisDataExport-Destination")>
            <[S3BucketDestination](API_AnalyticsExportDestination.md#AmazonS3-Type-AnalyticsExportDestination-S3BucketDestination "API_AnalyticsExportDestination.md#AmazonS3-Type-AnalyticsExportDestination-S3BucketDestination")>
               <[Bucket](API_AnalyticsS3BucketDestination.md#AmazonS3-Type-AnalyticsS3BucketDestination-Bucket "API_AnalyticsS3BucketDestination.md#AmazonS3-Type-AnalyticsS3BucketDestination-Bucket")>`string`</[Bucket](API_AnalyticsS3BucketDestination.md#AmazonS3-Type-AnalyticsS3BucketDestination-Bucket "API_AnalyticsS3BucketDestination.md#AmazonS3-Type-AnalyticsS3BucketDestination-Bucket")>
               <[BucketAccountId](API_AnalyticsS3BucketDestination.md#AmazonS3-Type-AnalyticsS3BucketDestination-BucketAccountId "API_AnalyticsS3BucketDestination.md#AmazonS3-Type-AnalyticsS3BucketDestination-BucketAccountId")>`string`</[BucketAccountId](API_AnalyticsS3BucketDestination.md#AmazonS3-Type-AnalyticsS3BucketDestination-BucketAccountId "API_AnalyticsS3BucketDestination.md#AmazonS3-Type-AnalyticsS3BucketDestination-BucketAccountId")>
               <[Format](API_AnalyticsS3BucketDestination.md#AmazonS3-Type-AnalyticsS3BucketDestination-Format "API_AnalyticsS3BucketDestination.md#AmazonS3-Type-AnalyticsS3BucketDestination-Format")>`string`</[Format](API_AnalyticsS3BucketDestination.md#AmazonS3-Type-AnalyticsS3BucketDestination-Format "API_AnalyticsS3BucketDestination.md#AmazonS3-Type-AnalyticsS3BucketDestination-Format")>
               <[Prefix](API_AnalyticsS3BucketDestination.md#AmazonS3-Type-AnalyticsS3BucketDestination-Prefix "API_AnalyticsS3BucketDestination.md#AmazonS3-Type-AnalyticsS3BucketDestination-Prefix")>`string`</[Prefix](API_AnalyticsS3BucketDestination.md#AmazonS3-Type-AnalyticsS3BucketDestination-Prefix "API_AnalyticsS3BucketDestination.md#AmazonS3-Type-AnalyticsS3BucketDestination-Prefix")>
            </[S3BucketDestination](API_AnalyticsExportDestination.md#AmazonS3-Type-AnalyticsExportDestination-S3BucketDestination "API_AnalyticsExportDestination.md#AmazonS3-Type-AnalyticsExportDestination-S3BucketDestination")>
         </[Destination](API_StorageClassAnalysisDataExport.md#AmazonS3-Type-StorageClassAnalysisDataExport-Destination "API_StorageClassAnalysisDataExport.md#AmazonS3-Type-StorageClassAnalysisDataExport-Destination")>
         <[OutputSchemaVersion](API_StorageClassAnalysisDataExport.md#AmazonS3-Type-StorageClassAnalysisDataExport-OutputSchemaVersion "API_StorageClassAnalysisDataExport.md#AmazonS3-Type-StorageClassAnalysisDataExport-OutputSchemaVersion")>`string`</[OutputSchemaVersion](API_StorageClassAnalysisDataExport.md#AmazonS3-Type-StorageClassAnalysisDataExport-OutputSchemaVersion "API_StorageClassAnalysisDataExport.md#AmazonS3-Type-StorageClassAnalysisDataExport-OutputSchemaVersion")>
      </[DataExport](API_StorageClassAnalysis.md#AmazonS3-Type-StorageClassAnalysis-DataExport "API_StorageClassAnalysis.md#AmazonS3-Type-StorageClassAnalysis-DataExport")>
   </[StorageClassAnalysis](#AmazonS3-PutBucketAnalyticsConfiguration-request-StorageClassAnalysis "#AmazonS3-PutBucketAnalyticsConfiguration-request-StorageClassAnalysis")>
</[AnalyticsConfiguration](#AmazonS3-PutBucketAnalyticsConfiguration-request-AnalyticsConfiguration "#AmazonS3-PutBucketAnalyticsConfiguration-request-AnalyticsConfiguration")>
```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_PutBucketAnalyticsConfiguration_RequestSyntax "#API_PutBucketAnalyticsConfiguration_RequestSyntax")**


The name of the bucket to which an analytics configuration is stored.


Required: Yes




**[id](#API_PutBucketAnalyticsConfiguration_RequestSyntax "#API_PutBucketAnalyticsConfiguration_RequestSyntax")**


The ID that identifies the analytics configuration.


Required: Yes




**[x-amz-expected-bucket-owner](#API_PutBucketAnalyticsConfiguration_RequestSyntax "#API_PutBucketAnalyticsConfiguration_RequestSyntax")**


The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).




## Request Body


The request accepts the following data in XML format.





**[AnalyticsConfiguration](#API_PutBucketAnalyticsConfiguration_RequestSyntax "#API_PutBucketAnalyticsConfiguration_RequestSyntax")**


Root level tag for the AnalyticsConfiguration parameters.


Required: Yes




**[Filter](#API_PutBucketAnalyticsConfiguration_RequestSyntax "#API_PutBucketAnalyticsConfiguration_RequestSyntax")**


The filter used to describe a set of objects for analyses. A filter must have exactly one prefix,
 one tag, or one conjunction (AnalyticsAndOperator). If no filter is provided, all objects will be
 considered in any analysis.


Type: [AnalyticsFilter](API_AnalyticsFilter.md "API_AnalyticsFilter.md") data type


Required: No




**[Id](#API_PutBucketAnalyticsConfiguration_RequestSyntax "#API_PutBucketAnalyticsConfiguration_RequestSyntax")**


The ID that identifies the analytics configuration.


Type: String


Required: Yes




**[StorageClassAnalysis](#API_PutBucketAnalyticsConfiguration_RequestSyntax "#API_PutBucketAnalyticsConfiguration_RequestSyntax")**


 Contains data related to access patterns to be collected and made available to analyze the
 tradeoffs between different storage classes. 


Type: [StorageClassAnalysis](API_StorageClassAnalysis.md "API_StorageClassAnalysis.md") data type


Required: Yes




## Response Syntax



```
HTTP/1.1 200

```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.


## Examples


### Example 1: Creating an analytics configuration


The following PUT request for the bucket `examplebucket` creates a new or replaces an
 existing analytics configuration with the ID `report1`. The configuration is defined in
 the request body. 



```

PUT /?analytics&id=report1 HTTP/1.1
Host: examplebucket.s3.<Region>.amazonaws.com
Date: Mon, 31 Oct 2016 12:00:00 GMT
Authorization: authorization string
Content-Length: length
 
<?xml version="1.0" encoding="UTF-8"?>
<AnalyticsConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
  <Id>report1</Id>
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

### Sample Response


This example illustrates one usage of PutBucketAnalyticsConfiguration.



```

HTTP/1.1 200 OK
x-amz-id-2: YgIPIfBiKa2bj0KMg95r/0zo3emzU4dzsD4rcKCHQUAdQkf3ShJTOOpXUueF6QKo
x-amz-request-id: 236A8905248E5A01
Date: Mon, 31 Oct 2016 12:00:00 GMT
Content-Length: 0
Server: AmazonS3
         
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/PutBucketAnalyticsConfiguration "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/PutBucketAnalyticsConfiguration")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/PutBucketAnalyticsConfiguration "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/PutBucketAnalyticsConfiguration")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/PutBucketAnalyticsConfiguration "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/PutBucketAnalyticsConfiguration")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/PutBucketAnalyticsConfiguration "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/PutBucketAnalyticsConfiguration")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/PutBucketAnalyticsConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/PutBucketAnalyticsConfiguration")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/PutBucketAnalyticsConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/PutBucketAnalyticsConfiguration")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/PutBucketAnalyticsConfiguration "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/PutBucketAnalyticsConfiguration")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/PutBucketAnalyticsConfiguration "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/PutBucketAnalyticsConfiguration")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/PutBucketAnalyticsConfiguration "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/PutBucketAnalyticsConfiguration")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/PutBucketAnalyticsConfiguration "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/PutBucketAnalyticsConfiguration")
