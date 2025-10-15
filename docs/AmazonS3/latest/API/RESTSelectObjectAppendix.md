# Appendix: SelectObjectContent Response


## Description


The Amazon S3 Select operation filters the contents of an Amazon S3 object based on a simple structured query
 language (SQL) statement. Given the response size of this operation is unknown, Amazon S3 Select streams the response as a 
 series of messages and includes a `Transfer-Encoding` header with `chunked`
 as its value in the response. 


For more information about Amazon S3 Select, see 
 [Selecting Content from Objects](../userguide/selecting-content-from-objects.md "../userguide/selecting-content-from-objects.md")
 in the *Amazon Simple Storage Service User Guide*.


For more information about using SQL with Amazon S3 Select, see  [SQL Reference for Amazon S3
 Select and Amazon Glacier Select](../userguide/s3-glacier-select-sql-reference.md "../userguide/s3-glacier-select-sql-reference.md") in the *Amazon Simple Storage Service User Guide*.


## Responses


A successful Amazon S3 Select Operation returns `200 OK` status code.


### Response Headers


This implementation of the operation uses only response headers that are common to most responses. For more information, see [Common Response Headers](RESTCommonResponseHeaders.md "RESTCommonResponseHeaders.md").


### Response Body


Since the Amazon S3 Select response size is unknown, Amazon S3 streams the response as a series of messages and
 includes a `Transfer-Encoding` header with `chunked`
 as its value in the response. The following example shows the response format at the
 top level:




```
<Message 1>
<Message 2>
<Message 3>
......
<Message n>
```

Each message consists of two sections: the prelude and the data. The prelude section consists of 
 1) the total byte-length of the message, and 2) the combined byte-length of all the headers.
 The data section consists of 1) the headers, and 2) a payload.


Each section ends with a 4-byte big-endian integer checksum (CRC). Amazon S3 Select uses CRC32
 (often referred to as GZIP CRC32) to calculate both CRCs. For more information about
 CRC32, see [*GZIP file
 format specification version 4.3*](https://www.ietf.org/rfc/rfc1952.txt "https://www.ietf.org/rfc/rfc1952.txt").


Total message overhead including the prelude and
 both checksums is 16 bytes.


###### Note

All `integer` values within messages are in network byte order, or big-endian
 order.


The following diagram shows the components that make up a message and a header. Note that there are multiple
 headers per message.



![Screenshot of an example message structure showing total byte-length, header byte-length, prelude crc, header, payload, and message crc.](../../../images/AmazonS3/latest/API/images/s3select-frame-diagram-frame-overview.png)

###### Note

For Amazon S3 Select, the header value type is always 7 (type=String). For this type, the
 header value consists of two components, a 2-byte big-endian integer length, and
 a UTF-8 string that is of that byte-length. The following diagram shows the
 components that make up Amazon S3 Select headers.



![Screenshot of the headers structure showing header name byte-length, header name string, header value type, value byte-length and value string.](../../../images/AmazonS3/latest/API/images/s3select-frame-diagram-headers-overview.png)

Payload byte-length calculations (these two calculations are equivalent):



* payload\_length = total\_length - header\_length - sizeOf(total\_length) - sizeOf(header\_length) - 
 sizeOf(prelude\_crc) - sizeOf(message\_crc)
* payload\_length = total\_length - header\_length - 16


Each message contains the following components:



* **Prelude**: Always fixed size of 8 bytes (two fields of 4
 bytes each):




	+ *First four bytes*: Total byte-length: Big-endian integer
	 byte-length of the entire message (including the 4-byte total length
	 field itself).
	+ *Second four bytes*: Headers byte-length: Big-endian integer
	 byte-length of the headers portion of the message (excluding the
	 headers length field itself).
* **Prelude CRC**: 4-byte big-endian integer checksum (CRC)
 for the prelude portion of the message (excluding the CRC itself). The
 prelude has a separate CRC from the message CRC (see below), to ensure that
 corrupted byte-length information can be detected immediately, without
 causing pathological buffering behavior.
* **Headers**: A set of metadata annotating the message, such as the message
 type, payload format, and so on. Messages can have multiple headers, so this portion of the message can have
 different byte-lengths depending on the message type. Headers are key-value pairs, where both the
 key and value are UTF-8 strings. Headers can appear in any order within the headers portion of the message,
 and any given header type can only appear once.


For Amazon S3 Select, following is a list of header names and the set of valid values depending
 on the message type.




	+ *MessageType Header*:
	
	
	
	
		- HeaderName => ":message-type"
		- Valid HeaderValues => "error", "event"
	+ *EventType Header*:
	
	
	
	
		- HeaderName => ":event-type"
		- Valid HeaderValues => "Records", "Cont", "Progress", "Stats", "End"
	+ *ErrorCode Header*:
	
	
	
	
		- HeaderName => ":error-code"
		- Valid HeaderValues => Error Code from the table in the [List of SELECT Object Content Error
		 Codes](ErrorResponses.md#SelectObjectContentErrorCodeList "ErrorResponses.md#SelectObjectContentErrorCodeList") section.
	+ *ErrorMessage Header*:
	
	
	
	
		- HeaderName => ":error-message"
		- Valid HeaderValues => Error message returned by the service, to help diagnose
		 request-level errors.
* **Payload**: Can be anything.
* **Message CRC**: 4-byte big-endian integer checksum (CRC)
 from the start of the message to the start of the checksum (that is,
 everything in the message excluding the message CRC itself).

Each header contains the following components. There can be multiple headers per message.



* **Header Name Byte-Length**: Byte-length of the header name.
* **Header Name**: Name of the header, indicating the header
 type. Valid values: ":message-type" ":event-type" ":error-code"
 ":error-message"
* **Header Value Type**: Enum indicating the header value
 type. For Amazon S3 Select, this is always 7.
* **Value String Byte-Length**: (For Amazon S3 Select) Byte-length of the header value string.
* **Header Value String**: (For Amazon S3 Select) Value of the header string. Valid values for this field
 vary based on the type of the header. See the sections below for valid values for each header type and message type.

For Amazon S3 Select, responses can be messages of the following types:



* **Records message**: Can contain a single record, partial
 records, or multiple records. Depending on the size of the result, a
 response can contain one or more of these messages.
* **Continuation message**: Amazon S3 periodically sends this
 message to keep the TCP connection open. These messages appear in responses
 at random. The client must detect the message type and process
 accordingly.
* **Progress message**: Amazon S3 periodically sends this message,
 if requested. It contains information about the progress of a query that has
 started but has not yet completed.
* **Stats message**: Amazon S3 sends this message at the end of the
 request. It contains statistics about the query.
* **End message**: Indicates that the request is complete, and
 no more messages will be sent. You should not assume that the request is
 complete until the client receives an `End` message.
* **RequestLevelError message**: Amazon S3 sends this message if
 the request failed for any reason. It contains the error code and error
 message for the failure. If Amazon S3 sends a `RequestLevelError`
 message, it doesn't send an `End` message.

The following sections explain the structure of each message type in more detail.


For sample code and unit tests that use this protocol, see [AWS C Event Stream](https://github.com/awslabs/aws-c-event-stream "https://github.com/awslabs/aws-c-event-stream")
 on the GitHub website.


#### Records Message


##### Header specification


Records messages contain three headers, as follows:



![Screenshot of an example message structure including the headers for this record type.](../../../images/AmazonS3/latest/API/images/s3select-frame-diagram-record.png)

##### Payload specification


Records message payloads can contain a single record, partial records, or multiple records.


#### Continuation Message


##### Header specification


Continuation messages contain two headers, as follows:



![Screenshot of an example message structure including the headers for this record type.](../../../images/AmazonS3/latest/API/images/s3select-frame-diagram-cont.png)

##### Payload specification


Continuation messages have no payload.


#### Progress Message


##### Header specification


Progress messages contain three headers, as follows:



![Screenshot of an example message structure including the headers for this record type.](../../../images/AmazonS3/latest/API/images/s3select-frame-diagram-progress.png)

##### Payload specification


Progress message payload is an XML document containing information about the progress of a request.



* *BytesScanned* => Number of bytes that have been processed before
 being uncompressed (if the file is compressed).
* *BytesProcessed* => Number of bytes that have been processed after
 being uncompressed (if the file is compressed).
* *BytesReturned* => Current number of bytes of records payload data
 returned by Amazon S3.

For uncompressed files, `BytesScanned` and `BytesProcessed` are
 equal.



Example:



```
<?xml version="1.0" encoding="UTF-8"?>
<Progress>
     <BytesScanned>512</BytesScanned>
     <BytesProcessed>1024</BytesProcessed>
     <BytesReturned>1024</BytesReturned>
</Progress>
```

#### Stats Message


##### Header specification


Stats messages contain three headers, as follows:



![Screenshot of an example message structure including the headers for this record type.](../../../images/AmazonS3/latest/API/images/s3select-frame-diagram-stats.png)

##### Payload specification


Stats message payload is an XML document containing information about a request's stats
 when processing is complete.



* *BytesScanned* => Number of bytes that have been processed before
 being uncompressed (if the file is compressed).
* *BytesProcessed* => Number of bytes that have been processed after
 being uncompressed (if the file is compressed).
* *BytesReturned* => Total number of bytes of records payload data
 returned by Amazon S3.

For uncompressed files, `BytesScanned` and `BytesProcessed` are
 equal.



Example:



```
<?xml version="1.0" encoding="UTF-8"?>
<Stats>
     <BytesScanned>512</BytesScanned>
     <BytesProcessed>1024</BytesProcessed>
     <BytesReturned>1024</BytesReturned>
</Stats>
```

#### End Message


##### Header specification


End messages contain two headers, as follows:



![Screenshot of an example message structure including the headers for this record type.](../../../images/AmazonS3/latest/API/images/s3select-frame-diagram-end.png)

##### Payload specification


End messages have no payload.


#### Request Level Error Message


##### Header specification


Request-level error messages contain three headers, as follows:



![Screenshot of an example message structure including the headers for this record type.](../../../images/AmazonS3/latest/API/images/s3select-frame-diagram-error.png)

For a list of possible error codes and error messages, see the [List of SELECT Object Content Error
 Codes](ErrorResponses.md#SelectObjectContentErrorCodeList "ErrorResponses.md#SelectObjectContentErrorCodeList").


##### Payload specification


Request-level error messages have no payload.


## Related Resources



* [SelectObjectContent](API_SelectObjectContent.md "API_SelectObjectContent.md")
* [GetObject](API_GetObject.md "API_GetObject.md")
* [GetBucketLifecycleConfiguration](API_GetBucketLifecycleConfiguration.md "API_GetBucketLifecycleConfiguration.md")
* [PutBucketLifecycleConfiguration](API_PutBucketLifecycleConfiguration.md "API_PutBucketLifecycleConfiguration.md")
