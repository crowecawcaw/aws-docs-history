# GetObjectAttributesParts

A collection of parts associated with a multipart upload.


## Contents





**IsTruncated** 


Indicates whether the returned list of parts is truncated. A value of `true` indicates
 that the list was truncated. A list can be truncated if the number of parts exceeds the limit returned
 in the `MaxParts` element.


Type: Boolean


Required: No




**MaxParts** 


The maximum number of parts allowed in the response.


Type: Integer


Required: No




**NextPartNumberMarker** 


When a list is truncated, this element specifies the last part in the list, as well as the value to
 use for the `PartNumberMarker` request parameter in a subsequent request.


Type: Integer


Required: No




**PartNumberMarker** 


The marker for the current part.


Type: Integer


Required: No




**Parts** 


A container for elements related to a particular part. A response can contain zero or more
 `Parts` elements.


###### Note


* **General purpose buckets** - For
 `GetObjectAttributes`, if an additional checksum (including
 `x-amz-checksum-crc32`, `x-amz-checksum-crc32c`,
 `x-amz-checksum-sha1`, or `x-amz-checksum-sha256`) isn't applied to the
 object specified in the request, the response doesn't return the `Part` element.
* **Directory buckets** - For
 `GetObjectAttributes`, regardless of whether an additional checksum is applied to the
 object specified in the request, the response returns the `Part` element.

Type: Array of [ObjectPart](API_ObjectPart.md "API_ObjectPart.md") data types


Required: No




**TotalPartsCount** 


The total number of parts.


Type: Integer


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetObjectAttributesParts "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetObjectAttributesParts")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetObjectAttributesParts "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetObjectAttributesParts")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetObjectAttributesParts "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetObjectAttributesParts")
