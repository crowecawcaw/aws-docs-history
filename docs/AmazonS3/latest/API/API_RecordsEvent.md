# RecordsEvent

The container for the records event.


## Contents





**Payload** 


The byte array of partial, one or more result records. S3 Select doesn't guarantee that a record
 will be self-contained in one record frame. To ensure continuous streaming of data, S3 Select might
 split the same record across multiple record frames instead of aggregating the results in memory. Some
 S3 clients (for example, the AWS SDK for Java) handle this behavior by creating a
 `ByteStream` out of the response by default. Other clients might not handle this behavior
 by default. In those cases, you must aggregate the results on the client side and parse the
 response.


Type: Base64-encoded binary data object


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/RecordsEvent "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/RecordsEvent")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/RecordsEvent "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/RecordsEvent")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/RecordsEvent "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/RecordsEvent")
