# ScanRange

Specifies the byte range of the object to get the records from. A record is processed when its first
 byte is contained by the range. This parameter is optional, but when specified, it must not be empty.
 See RFC 2616, Section 14.35.1 about how to specify the start and end of the range.


## Contents





**End** 


Specifies the end of the byte range. This parameter is optional. Valid values: non-negative
 integers. The default value is one less than the size of the object being queried. If only the End
 parameter is supplied, it is interpreted to mean scan the last N bytes of the file. For example,
 `<scanrange><end>50</end></scanrange>` means scan the last 50
 bytes.


Type: Long


Required: No




**Start** 


Specifies the start of the byte range. This parameter is optional. Valid values: non-negative
 integers. The default value is 0. If only `start` is supplied, it means scan from that point
 to the end of the file. For example,
 `<scanrange><start>50</start></scanrange>` means scan from byte 50
 until the end of the file.


Type: Long


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/ScanRange "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/ScanRange")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/ScanRange "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/ScanRange")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/ScanRange "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/ScanRange")
