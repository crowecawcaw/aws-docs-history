# SelectObjectContent

###### Note

This operation is not supported for directory buckets.

This action filters the contents of an Amazon S3 object based on a simple structured query language (SQL)
 statement. In the request, along with the SQL expression, you must also specify a data serialization
 format (JSON, CSV, or Apache Parquet) of the object. Amazon S3 uses this format to parse object data into
 records, and returns only records that match the specified SQL expression. You must also specify the
 data serialization format for the response.

This functionality is not supported for Amazon S3 on Outposts.

For more information about Amazon S3 Select, see [Selecting Content from Objects](https://docs.aws.amazon.com/AmazonS3/latest/dev/selecting-content-from-objects.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/selecting-content-from-objects.html")
 and [SELECT Command](../userguide/s3-glacier-select-sql-reference-select.md "../userguide/s3-glacier-select-sql-reference-select.md") in
 the *Amazon S3 User Guide*.



Permissions

You must have the `s3:GetObject` permission for this operation. Amazon S3 Select does
 not support anonymous access. For more information about permissions, see [Specifying Permissions
 in a Policy](https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html") in the *Amazon S3 User Guide*.



Object Data Formats

You can use Amazon S3 Select to query objects that have the following format properties:



* *CSV, JSON, and Parquet* - Objects must be in CSV, JSON, or Parquet
 format.
* *UTF-8* - UTF-8 is the only encoding type Amazon S3 Select supports.
* *GZIP or BZIP2* - CSV and JSON files can be compressed using GZIP or
 BZIP2. GZIP and BZIP2 are the only compression formats that Amazon S3 Select supports for CSV and
 JSON files. Amazon S3 Select supports columnar compression for Parquet using GZIP or Snappy. Amazon S3
 Select does not support whole-object compression for Parquet objects.
* *Server-side encryption* - Amazon S3 Select supports querying objects that
 are protected with server-side encryption.


For objects that are encrypted with customer-provided encryption keys (SSE-C), you must
 use HTTPS, and you must use the headers that are documented in the [GetObject](API_GetObject.md "API_GetObject.md"). For more information about
 SSE-C, see [Server-Side Encryption
 (Using Customer-Provided Encryption Keys)](https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html") in the
 *Amazon S3 User Guide*.


For objects that are encrypted with Amazon S3 managed keys (SSE-S3) and AWS KMS keys
 (SSE-KMS), server-side encryption is handled transparently, so you don't need to specify
 anything. For more information about server-side encryption, including SSE-S3 and SSE-KMS, see
 [Protecting
 Data Using Server-Side Encryption](https://docs.aws.amazon.com/AmazonS3/latest/dev/serv-side-encryption.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/serv-side-encryption.html") in the
 *Amazon S3 User Guide*.


Working with the Response Body

Given the response size is unknown, Amazon S3 Select streams the response as a series of messages
 and includes a `Transfer-Encoding` header with `chunked` as its value in the
 response. For more information, see [Appendix: SelectObjectContent
 Response](RESTSelectObjectAppendix.md "RESTSelectObjectAppendix.md").



GetObject Support

The `SelectObjectContent` action does not support the following
 `GetObject` functionality. For more information, see [GetObject](API_GetObject.md "API_GetObject.md").



* `Range`: Although you can specify a scan range for an Amazon S3 Select request (see
 [SelectObjectContentRequest - ScanRange](API_SelectObjectContent.md#AmazonS3-SelectObjectContent-request-ScanRange "API_SelectObjectContent.md#AmazonS3-SelectObjectContent-request-ScanRange") in the request parameters), you
 cannot specify the range of bytes of an object to return.
* The `GLACIER`, `DEEP_ARCHIVE`, and `REDUCED_REDUNDANCY`
 storage classes, or the `ARCHIVE_ACCESS` and `DEEP_ARCHIVE_ACCESS`
 access tiers of the `INTELLIGENT_TIERING` storage class: You cannot query objects
 in the `GLACIER`, `DEEP_ARCHIVE`, or `REDUCED_REDUNDANCY`
 storage classes, nor objects in the `ARCHIVE_ACCESS` or
 `DEEP_ARCHIVE_ACCESS` access tiers of the `INTELLIGENT_TIERING`
 storage class. For more information about storage classes, see [Using Amazon S3 storage classes](../userguide/storage-class-intro.md "../userguide/storage-class-intro.md")
 in the *Amazon S3 User Guide*.


Special Errors

For a list of special errors for this operation, see [List of SELECT
 Object Content Error Codes](ErrorResponses.md#SelectObjectContentErrorCodeList "ErrorResponses.md#SelectObjectContentErrorCodeList")




The following operations are related to `SelectObjectContent`:


* [GetObject](API_GetObject.md "API_GetObject.md")
* [GetBucketLifecycleConfiguration](API_GetBucketLifecycleConfiguration.md "API_GetBucketLifecycleConfiguration.md")
* [PutBucketLifecycleConfiguration](API_PutBucketLifecycleConfiguration.md "API_PutBucketLifecycleConfiguration.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
POST /{Key+}?select&select-type=2 HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
x-amz-server-side-encryption-customer-algorithm: `SSECustomerAlgorithm`
x-amz-server-side-encryption-customer-key: `SSECustomerKey`
x-amz-server-side-encryption-customer-key-MD5: `SSECustomerKeyMD5`
x-amz-expected-bucket-owner: `ExpectedBucketOwner`
<?xml version="1.0" encoding="UTF-8"?>
<[SelectObjectContentRequest](#AmazonS3-SelectObjectContent-request-SelectObjectContentRequest "#AmazonS3-SelectObjectContent-request-SelectObjectContentRequest") xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
   <[Expression](#AmazonS3-SelectObjectContent-request-Expression "#AmazonS3-SelectObjectContent-request-Expression")>`string`</[Expression](#AmazonS3-SelectObjectContent-request-Expression "#AmazonS3-SelectObjectContent-request-Expression")>
   <[ExpressionType](#AmazonS3-SelectObjectContent-request-ExpressionType "#AmazonS3-SelectObjectContent-request-ExpressionType")>`string`</[ExpressionType](#AmazonS3-SelectObjectContent-request-ExpressionType "#AmazonS3-SelectObjectContent-request-ExpressionType")>
   <[RequestProgress](#AmazonS3-SelectObjectContent-request-RequestProgress "#AmazonS3-SelectObjectContent-request-RequestProgress")>
      <[Enabled](API_RequestProgress.md#AmazonS3-Type-RequestProgress-Enabled "API_RequestProgress.md#AmazonS3-Type-RequestProgress-Enabled")>`boolean`</[Enabled](API_RequestProgress.md#AmazonS3-Type-RequestProgress-Enabled "API_RequestProgress.md#AmazonS3-Type-RequestProgress-Enabled")>
   </[RequestProgress](#AmazonS3-SelectObjectContent-request-RequestProgress "#AmazonS3-SelectObjectContent-request-RequestProgress")>
   <[InputSerialization](#AmazonS3-SelectObjectContent-request-InputSerialization "#AmazonS3-SelectObjectContent-request-InputSerialization")>
      <[CompressionType](API_InputSerialization.md#AmazonS3-Type-InputSerialization-CompressionType "API_InputSerialization.md#AmazonS3-Type-InputSerialization-CompressionType")>`string`</[CompressionType](API_InputSerialization.md#AmazonS3-Type-InputSerialization-CompressionType "API_InputSerialization.md#AmazonS3-Type-InputSerialization-CompressionType")>
      <[CSV](API_InputSerialization.md#AmazonS3-Type-InputSerialization-CSV "API_InputSerialization.md#AmazonS3-Type-InputSerialization-CSV")>
         <[AllowQuotedRecordDelimiter](API_CSVInput.md#AmazonS3-Type-CSVInput-AllowQuotedRecordDelimiter "API_CSVInput.md#AmazonS3-Type-CSVInput-AllowQuotedRecordDelimiter")>`boolean`</[AllowQuotedRecordDelimiter](API_CSVInput.md#AmazonS3-Type-CSVInput-AllowQuotedRecordDelimiter "API_CSVInput.md#AmazonS3-Type-CSVInput-AllowQuotedRecordDelimiter")>
         <[Comments](API_CSVInput.md#AmazonS3-Type-CSVInput-Comments "API_CSVInput.md#AmazonS3-Type-CSVInput-Comments")>`string`</[Comments](API_CSVInput.md#AmazonS3-Type-CSVInput-Comments "API_CSVInput.md#AmazonS3-Type-CSVInput-Comments")>
         <[FieldDelimiter](API_CSVInput.md#AmazonS3-Type-CSVInput-FieldDelimiter "API_CSVInput.md#AmazonS3-Type-CSVInput-FieldDelimiter")>`string`</[FieldDelimiter](API_CSVInput.md#AmazonS3-Type-CSVInput-FieldDelimiter "API_CSVInput.md#AmazonS3-Type-CSVInput-FieldDelimiter")>
         <[FileHeaderInfo](API_CSVInput.md#AmazonS3-Type-CSVInput-FileHeaderInfo "API_CSVInput.md#AmazonS3-Type-CSVInput-FileHeaderInfo")>`string`</[FileHeaderInfo](API_CSVInput.md#AmazonS3-Type-CSVInput-FileHeaderInfo "API_CSVInput.md#AmazonS3-Type-CSVInput-FileHeaderInfo")>
         <[QuoteCharacter](API_CSVInput.md#AmazonS3-Type-CSVInput-QuoteCharacter "API_CSVInput.md#AmazonS3-Type-CSVInput-QuoteCharacter")>`string`</[QuoteCharacter](API_CSVInput.md#AmazonS3-Type-CSVInput-QuoteCharacter "API_CSVInput.md#AmazonS3-Type-CSVInput-QuoteCharacter")>
         <[QuoteEscapeCharacter](API_CSVInput.md#AmazonS3-Type-CSVInput-QuoteEscapeCharacter "API_CSVInput.md#AmazonS3-Type-CSVInput-QuoteEscapeCharacter")>`string`</[QuoteEscapeCharacter](API_CSVInput.md#AmazonS3-Type-CSVInput-QuoteEscapeCharacter "API_CSVInput.md#AmazonS3-Type-CSVInput-QuoteEscapeCharacter")>
         <[RecordDelimiter](API_CSVInput.md#AmazonS3-Type-CSVInput-RecordDelimiter "API_CSVInput.md#AmazonS3-Type-CSVInput-RecordDelimiter")>`string`</[RecordDelimiter](API_CSVInput.md#AmazonS3-Type-CSVInput-RecordDelimiter "API_CSVInput.md#AmazonS3-Type-CSVInput-RecordDelimiter")>
      </[CSV](API_InputSerialization.md#AmazonS3-Type-InputSerialization-CSV "API_InputSerialization.md#AmazonS3-Type-InputSerialization-CSV")>
      <[JSON](API_InputSerialization.md#AmazonS3-Type-InputSerialization-JSON "API_InputSerialization.md#AmazonS3-Type-InputSerialization-JSON")>
         <[Type](API_JSONInput.md#AmazonS3-Type-JSONInput-Type "API_JSONInput.md#AmazonS3-Type-JSONInput-Type")>`string`</[Type](API_JSONInput.md#AmazonS3-Type-JSONInput-Type "API_JSONInput.md#AmazonS3-Type-JSONInput-Type")>
      </[JSON](API_InputSerialization.md#AmazonS3-Type-InputSerialization-JSON "API_InputSerialization.md#AmazonS3-Type-InputSerialization-JSON")>
      <[Parquet](API_InputSerialization.md#AmazonS3-Type-InputSerialization-Parquet "API_InputSerialization.md#AmazonS3-Type-InputSerialization-Parquet")>
      </[Parquet](API_InputSerialization.md#AmazonS3-Type-InputSerialization-Parquet "API_InputSerialization.md#AmazonS3-Type-InputSerialization-Parquet")>
   </[InputSerialization](#AmazonS3-SelectObjectContent-request-InputSerialization "#AmazonS3-SelectObjectContent-request-InputSerialization")>
   <[OutputSerialization](#AmazonS3-SelectObjectContent-request-OutputSerialization "#AmazonS3-SelectObjectContent-request-OutputSerialization")>
      <[CSV](API_OutputSerialization.md#AmazonS3-Type-OutputSerialization-CSV "API_OutputSerialization.md#AmazonS3-Type-OutputSerialization-CSV")>
         <[FieldDelimiter](API_CSVOutput.md#AmazonS3-Type-CSVOutput-FieldDelimiter "API_CSVOutput.md#AmazonS3-Type-CSVOutput-FieldDelimiter")>`string`</[FieldDelimiter](API_CSVOutput.md#AmazonS3-Type-CSVOutput-FieldDelimiter "API_CSVOutput.md#AmazonS3-Type-CSVOutput-FieldDelimiter")>
         <[QuoteCharacter](API_CSVOutput.md#AmazonS3-Type-CSVOutput-QuoteCharacter "API_CSVOutput.md#AmazonS3-Type-CSVOutput-QuoteCharacter")>`string`</[QuoteCharacter](API_CSVOutput.md#AmazonS3-Type-CSVOutput-QuoteCharacter "API_CSVOutput.md#AmazonS3-Type-CSVOutput-QuoteCharacter")>
         <[QuoteEscapeCharacter](API_CSVOutput.md#AmazonS3-Type-CSVOutput-QuoteEscapeCharacter "API_CSVOutput.md#AmazonS3-Type-CSVOutput-QuoteEscapeCharacter")>`string`</[QuoteEscapeCharacter](API_CSVOutput.md#AmazonS3-Type-CSVOutput-QuoteEscapeCharacter "API_CSVOutput.md#AmazonS3-Type-CSVOutput-QuoteEscapeCharacter")>
         <[QuoteFields](API_CSVOutput.md#AmazonS3-Type-CSVOutput-QuoteFields "API_CSVOutput.md#AmazonS3-Type-CSVOutput-QuoteFields")>`string`</[QuoteFields](API_CSVOutput.md#AmazonS3-Type-CSVOutput-QuoteFields "API_CSVOutput.md#AmazonS3-Type-CSVOutput-QuoteFields")>
         <[RecordDelimiter](API_CSVOutput.md#AmazonS3-Type-CSVOutput-RecordDelimiter "API_CSVOutput.md#AmazonS3-Type-CSVOutput-RecordDelimiter")>`string`</[RecordDelimiter](API_CSVOutput.md#AmazonS3-Type-CSVOutput-RecordDelimiter "API_CSVOutput.md#AmazonS3-Type-CSVOutput-RecordDelimiter")>
      </[CSV](API_OutputSerialization.md#AmazonS3-Type-OutputSerialization-CSV "API_OutputSerialization.md#AmazonS3-Type-OutputSerialization-CSV")>
      <[JSON](API_OutputSerialization.md#AmazonS3-Type-OutputSerialization-JSON "API_OutputSerialization.md#AmazonS3-Type-OutputSerialization-JSON")>
         <[RecordDelimiter](API_JSONOutput.md#AmazonS3-Type-JSONOutput-RecordDelimiter "API_JSONOutput.md#AmazonS3-Type-JSONOutput-RecordDelimiter")>`string`</[RecordDelimiter](API_JSONOutput.md#AmazonS3-Type-JSONOutput-RecordDelimiter "API_JSONOutput.md#AmazonS3-Type-JSONOutput-RecordDelimiter")>
      </[JSON](API_OutputSerialization.md#AmazonS3-Type-OutputSerialization-JSON "API_OutputSerialization.md#AmazonS3-Type-OutputSerialization-JSON")>
   </[OutputSerialization](#AmazonS3-SelectObjectContent-request-OutputSerialization "#AmazonS3-SelectObjectContent-request-OutputSerialization")>
   <[ScanRange](#AmazonS3-SelectObjectContent-request-ScanRange "#AmazonS3-SelectObjectContent-request-ScanRange")>
      <[End](API_ScanRange.md#AmazonS3-Type-ScanRange-End "API_ScanRange.md#AmazonS3-Type-ScanRange-End")>`long`</[End](API_ScanRange.md#AmazonS3-Type-ScanRange-End "API_ScanRange.md#AmazonS3-Type-ScanRange-End")>
      <[Start](API_ScanRange.md#AmazonS3-Type-ScanRange-Start "API_ScanRange.md#AmazonS3-Type-ScanRange-Start")>`long`</[Start](API_ScanRange.md#AmazonS3-Type-ScanRange-Start "API_ScanRange.md#AmazonS3-Type-ScanRange-Start")>
   </[ScanRange](#AmazonS3-SelectObjectContent-request-ScanRange "#AmazonS3-SelectObjectContent-request-ScanRange")>
</[SelectObjectContentRequest](#AmazonS3-SelectObjectContent-request-SelectObjectContentRequest "#AmazonS3-SelectObjectContent-request-SelectObjectContentRequest")>
```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_SelectObjectContent_RequestSyntax "#API_SelectObjectContent_RequestSyntax")**


The S3 bucket.


Required: Yes




**[Key](#API_SelectObjectContent_RequestSyntax "#API_SelectObjectContent_RequestSyntax")**


The object key.


Length Constraints: Minimum length of 1.


Required: Yes




**[x-amz-expected-bucket-owner](#API_SelectObjectContent_RequestSyntax "#API_SelectObjectContent_RequestSyntax")**


The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).




**[x-amz-server-side-encryption-customer-algorithm](#API_SelectObjectContent_RequestSyntax "#API_SelectObjectContent_RequestSyntax")**


The server-side encryption (SSE) algorithm used to encrypt the object. This parameter is needed only when the object was created 
 using a checksum algorithm. For more information,
 see [Protecting data using SSE-C keys](https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html") in the
 *Amazon S3 User Guide*.




**[x-amz-server-side-encryption-customer-key](#API_SelectObjectContent_RequestSyntax "#API_SelectObjectContent_RequestSyntax")**


The server-side encryption (SSE) customer managed key. This parameter is needed only when the object was created using a checksum algorithm. 
 For more information, see
 [Protecting data using SSE-C keys](https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html") in the
 *Amazon S3 User Guide*.




**[x-amz-server-side-encryption-customer-key-MD5](#API_SelectObjectContent_RequestSyntax "#API_SelectObjectContent_RequestSyntax")**


The MD5 server-side encryption (SSE) customer managed key. This parameter is needed only when the object was created using a checksum 
 algorithm. For more information,
 see [Protecting data using SSE-C keys](https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html") in the
 *Amazon S3 User Guide*.




## Request Body


The request accepts the following data in XML format.





**[SelectObjectContentRequest](#API_SelectObjectContent_RequestSyntax "#API_SelectObjectContent_RequestSyntax")**


Root level tag for the SelectObjectContentRequest parameters.


Required: Yes




**[Expression](#API_SelectObjectContent_RequestSyntax "#API_SelectObjectContent_RequestSyntax")**


The expression that is used to query the object.


Type: String


Required: Yes




**[ExpressionType](#API_SelectObjectContent_RequestSyntax "#API_SelectObjectContent_RequestSyntax")**


The type of the provided expression (for example, SQL).


Type: String


Valid Values: `SQL`



Required: Yes




**[InputSerialization](#API_SelectObjectContent_RequestSyntax "#API_SelectObjectContent_RequestSyntax")**


Describes the format of the data in the object that is being queried.


Type: [InputSerialization](API_InputSerialization.md "API_InputSerialization.md") data type


Required: Yes




**[OutputSerialization](#API_SelectObjectContent_RequestSyntax "#API_SelectObjectContent_RequestSyntax")**


Describes the format of the data that you want Amazon S3 to return in response.


Type: [OutputSerialization](API_OutputSerialization.md "API_OutputSerialization.md") data type


Required: Yes




**[RequestProgress](#API_SelectObjectContent_RequestSyntax "#API_SelectObjectContent_RequestSyntax")**


Specifies if periodic request progress information should be enabled.


Type: [RequestProgress](API_RequestProgress.md "API_RequestProgress.md") data type


Required: No




**[ScanRange](#API_SelectObjectContent_RequestSyntax "#API_SelectObjectContent_RequestSyntax")**


Specifies the byte range of the object to get the records from. A record is processed when its first
 byte is contained by the range. This parameter is optional, but when specified, it must not be empty.
 See RFC 2616, Section 14.35.1 about how to specify the start and end of the range.



`ScanRange`may be used in the following ways:



* `<scanrange><start>50</start><end>100</end></scanrange>`
 - process only the records starting between the bytes 50 and 100 (inclusive, counting from
 zero)
* `<scanrange><start>50</start></scanrange>` - process only the
 records starting after the byte 50
* `<scanrange><end>50</end></scanrange>` - process only the
 records within the last 50 bytes of the file.

Type: [ScanRange](API_ScanRange.md "API_ScanRange.md") data type


Required: No




## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<[Payload](#AmazonS3-SelectObjectContent-response-Payload "#AmazonS3-SelectObjectContent-response-Payload")>
   <[Records](#AmazonS3-SelectObjectContent-response-Records "#AmazonS3-SelectObjectContent-response-Records")>
      <[Payload](API_RecordsEvent.md#AmazonS3-Type-RecordsEvent-Payload "API_RecordsEvent.md#AmazonS3-Type-RecordsEvent-Payload")>***blob***</[Payload](API_RecordsEvent.md#AmazonS3-Type-RecordsEvent-Payload "API_RecordsEvent.md#AmazonS3-Type-RecordsEvent-Payload")>
   </[Records](#AmazonS3-SelectObjectContent-response-Records "#AmazonS3-SelectObjectContent-response-Records")>
   <[Stats](#AmazonS3-SelectObjectContent-response-Stats "#AmazonS3-SelectObjectContent-response-Stats")>
      <[Details](API_StatsEvent.md#AmazonS3-Type-StatsEvent-Details "API_StatsEvent.md#AmazonS3-Type-StatsEvent-Details")>
         <[BytesProcessed](API_Stats.md#AmazonS3-Type-Stats-BytesProcessed "API_Stats.md#AmazonS3-Type-Stats-BytesProcessed")>***long***</[BytesProcessed](API_Stats.md#AmazonS3-Type-Stats-BytesProcessed "API_Stats.md#AmazonS3-Type-Stats-BytesProcessed")>
         <[BytesReturned](API_Stats.md#AmazonS3-Type-Stats-BytesReturned "API_Stats.md#AmazonS3-Type-Stats-BytesReturned")>***long***</[BytesReturned](API_Stats.md#AmazonS3-Type-Stats-BytesReturned "API_Stats.md#AmazonS3-Type-Stats-BytesReturned")>
         <[BytesScanned](API_Stats.md#AmazonS3-Type-Stats-BytesScanned "API_Stats.md#AmazonS3-Type-Stats-BytesScanned")>***long***</[BytesScanned](API_Stats.md#AmazonS3-Type-Stats-BytesScanned "API_Stats.md#AmazonS3-Type-Stats-BytesScanned")>
      </[Details](API_StatsEvent.md#AmazonS3-Type-StatsEvent-Details "API_StatsEvent.md#AmazonS3-Type-StatsEvent-Details")>
   </[Stats](#AmazonS3-SelectObjectContent-response-Stats "#AmazonS3-SelectObjectContent-response-Stats")>
   <[Progress](#AmazonS3-SelectObjectContent-response-Progress "#AmazonS3-SelectObjectContent-response-Progress")>
      <[Details](API_ProgressEvent.md#AmazonS3-Type-ProgressEvent-Details "API_ProgressEvent.md#AmazonS3-Type-ProgressEvent-Details")>
         <[BytesProcessed](API_Progress.md#AmazonS3-Type-Progress-BytesProcessed "API_Progress.md#AmazonS3-Type-Progress-BytesProcessed")>***long***</[BytesProcessed](API_Progress.md#AmazonS3-Type-Progress-BytesProcessed "API_Progress.md#AmazonS3-Type-Progress-BytesProcessed")>
         <[BytesReturned](API_Progress.md#AmazonS3-Type-Progress-BytesReturned "API_Progress.md#AmazonS3-Type-Progress-BytesReturned")>***long***</[BytesReturned](API_Progress.md#AmazonS3-Type-Progress-BytesReturned "API_Progress.md#AmazonS3-Type-Progress-BytesReturned")>
         <[BytesScanned](API_Progress.md#AmazonS3-Type-Progress-BytesScanned "API_Progress.md#AmazonS3-Type-Progress-BytesScanned")>***long***</[BytesScanned](API_Progress.md#AmazonS3-Type-Progress-BytesScanned "API_Progress.md#AmazonS3-Type-Progress-BytesScanned")>
      </[Details](API_ProgressEvent.md#AmazonS3-Type-ProgressEvent-Details "API_ProgressEvent.md#AmazonS3-Type-ProgressEvent-Details")>
   </[Progress](#AmazonS3-SelectObjectContent-response-Progress "#AmazonS3-SelectObjectContent-response-Progress")>
   <[Cont](#AmazonS3-SelectObjectContent-response-Cont "#AmazonS3-SelectObjectContent-response-Cont")>
   </[Cont](#AmazonS3-SelectObjectContent-response-Cont "#AmazonS3-SelectObjectContent-response-Cont")>
   <[End](#AmazonS3-SelectObjectContent-response-End "#AmazonS3-SelectObjectContent-response-End")>
   </[End](#AmazonS3-SelectObjectContent-response-End "#AmazonS3-SelectObjectContent-response-End")>
</[Payload](#AmazonS3-SelectObjectContent-response-Payload "#AmazonS3-SelectObjectContent-response-Payload")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[Payload](#API_SelectObjectContent_ResponseSyntax "#API_SelectObjectContent_ResponseSyntax")**


Root level tag for the Payload parameters.


Required: Yes




**[Cont](#API_SelectObjectContent_ResponseSyntax "#API_SelectObjectContent_ResponseSyntax")**


The Continuation Event.


Type: [ContinuationEvent](API_ContinuationEvent.md "API_ContinuationEvent.md") data type




**[End](#API_SelectObjectContent_ResponseSyntax "#API_SelectObjectContent_ResponseSyntax")**


The End Event.


Type: [EndEvent](API_EndEvent.md "API_EndEvent.md") data type




**[Progress](#API_SelectObjectContent_ResponseSyntax "#API_SelectObjectContent_ResponseSyntax")**


The Progress Event.


Type: [ProgressEvent](API_ProgressEvent.md "API_ProgressEvent.md") data type




**[Records](#API_SelectObjectContent_ResponseSyntax "#API_SelectObjectContent_ResponseSyntax")**


The Records Event.


Type: [RecordsEvent](API_RecordsEvent.md "API_RecordsEvent.md") data type




**[Stats](#API_SelectObjectContent_ResponseSyntax "#API_SelectObjectContent_ResponseSyntax")**


The Stats Event.


Type: [StatsEvent](API_StatsEvent.md "API_StatsEvent.md") data type




## Examples


### Example 1: CSV object


The following select request retrieves all records from an object with data stored in CSV
 format. The OutputSerialization element directs Amazon S3 to return results in CSV.


You can try different queries in the `Expression` element:



* Assuming that you are not using column headers, you can identify columns using positional
 headers:



`SELECT s._1, s._2 FROM S3Object s WHERE s._3 > 100`
* If you have column headers and you set the `FileHeaderInfo` to `Use`,
 you can identify columns by name in the expression:



`SELECT s.Id, s.FirstName, s.SSN FROM S3Object s`
* You can specify functions in the SQL expression:



`SELECT count(*) FROM S3Object s WHERE s._1 < 1`


```

POST /exampleobject.csv?select&select-type=2 HTTP/1.1
Host: examplebucket.s3.<Region>.amazonaws.com
Date: Tue, 17 Oct 2017 01:49:52 GMT
Authorization: authorization string
Content-Length: content length

<?xml version="1.0" encoding="UTF-8"?>
<SelectRequest>
    <Expression>Select * from S3Object</Expression>
    <ExpressionType>SQL</ExpressionType>
    <InputSerialization>
        <CompressionType>GZIP</CompressionType>
        <CSV>
            <FileHeaderInfo>IGNORE</FileHeaderInfo>
            <RecordDelimiter>\n</RecordDelimiter>
            <FieldDelimiter>,</FieldDelimiter>
            <QuoteCharacter>"</QuoteCharacter>
            <QuoteEscapeCharacter>"</QuoteEscapeCharacter>
            <Comments>#</Comments>
        </CSV>
    </InputSerialization>
    <OutputSerialization>
        <CSV>
            <QuoteFields>ASNEEDED</QuoteFields>
            <RecordDelimiter>\n</RecordDelimiter>
            <FieldDelimiter>,</FieldDelimiter>
            <QuoteCharacter>"</QuoteCharacter>
            <QuoteEscapeCharacter>"</QuoteEscapeCharacter>
        </CSV>                               
    </OutputSerialization>
</SelectRequest> 
         
```

### Example


The following is a sample response.



```

HTTP/1.1 200 OK
x-amz-id-2: GFihv3y6+kE7KG11GEkQhU7/2/cHR3Yb2fCb2S04nxI423Dqwg2XiQ0B/UZlzYQvPiBlZNRcovw=
x-amz-request-id: 9F341CD3C4BA79E0
Date: Tue, 17 Oct 2017 23:54:05 GMT

A series of messages
         
```

### Example 2: JSON object


The following select request retrieves all records from an object with data stored in JSON
 format. The OutputSerialization directs Amazon S3 to return results in CSV.


You can try different queries in the `Expression` element:



* You can filter by string comparison using record keys:



`SELECT s.country, s.city from S3Object s where s.city = 'Seattle'`
* You can specify functions in the SQL expression:



`SELECT count(*) FROM S3Object s`


```

POST /exampleobject.json?select&select-type=2 HTTP/1.1
Host: examplebucket.s3.<Region>.amazonaws.com
Date: Tue, 17 Oct 2017 01:49:52 GMT
Authorization: authorization string
Content-Length: content length

<?xml version="1.0" encoding="UTF-8"?>
<SelectRequest>
    <Expression>Select * from S3Object</Expression>
    <ExpressionType>SQL</ExpressionType>
    <InputSerialization>
        <CompressionType>GZIP</CompressionType>
        <JSON>
            <Type>DOCUMENT</Type>
        </JSON>
    </InputSerialization>
    <OutputSerialization>
        <CSV>
            <QuoteFields>ASNEEDED</QuoteFields>
            <RecordDelimiter>\n</RecordDelimiter>
            <FieldDelimiter>,</FieldDelimiter>
            <QuoteCharacter>"</QuoteCharacter>
            <QuoteEscapeCharacter>"</QuoteEscapeCharacter>
        </CSV>                               
    </OutputSerialization>
</SelectRequest> 
         
```

### Example


The following is a sample response.



```

HTTP/1.1 200 OK
x-amz-id-2: GFihv3y6+kE7KG11GEkQhU7/2/cHR3Yb2fCb2S04nxI423Dqwg2XiQ0B/UZlzYQvPiBlZNRcovw=
x-amz-request-id: 9F341CD3C4BA79E0
Date: Tue, 17 Oct 2017 23:54:05 GMT

A series of messages
         
```

### Example 3: Parquet object



* The `InputSerialization` element describes the format of the data in the object
 that is being queried. It must specify `CSV`, `JSON`, or
 `Parquet`.
* The `OutputSerialization`  element describes the format of the data that you want
 Amazon S3 to return in response to the query. It must specify `CSV`, `JSON`.
 Amazon S3 doesn't support outputting data in the `Parquet` format.
* The format of the `InputSerialization` doesn't need to match the format of the
 `OutputSerialization`. So, for example, you can specify `JSON` in the
 `InputSerialization` and `CSV` in the `OutputSerialization`.


```

POST /exampleobject.parquet?select&select-type=2 HTTP/1.1
Host: examplebucket.s3.<Region>.amazonaws.com
Date: Tue, 17 Oct 2017 01:49:52 GMT
Authorization: authorization string
Content-Length: content length

<?xml version="1.0" encoding="UTF-8"?>
<SelectRequest>
    <Expression>Select * from S3Object</Expression>
    <ExpressionType>SQL</ExpressionType>
    <InputSerialization>
        <CompressionType>NONE</CompressionType>
        <Parquet>
        </Parquet>
    </InputSerialization>
    <OutputSerialization>
        <CSV>
            <QuoteFields>ASNEEDED</QuoteFields>
            <RecordDelimiter>\n</RecordDelimiter>
            <FieldDelimiter>,</FieldDelimiter>
            <QuoteCharacter>"</QuoteCharacter>
            <QuoteEscapeCharacter>"</QuoteEscapeCharacter>
        </CSV>
    </OutputSerialization>
</SelectRequest>
         
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/SelectObjectContent "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/SelectObjectContent")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/SelectObjectContent "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/SelectObjectContent")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/SelectObjectContent "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/SelectObjectContent")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/SelectObjectContent "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/SelectObjectContent")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/SelectObjectContent "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/SelectObjectContent")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/SelectObjectContent "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/SelectObjectContent")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/SelectObjectContent "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/SelectObjectContent")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/SelectObjectContent "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/SelectObjectContent")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/SelectObjectContent "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/SelectObjectContent")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/SelectObjectContent "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/SelectObjectContent")
