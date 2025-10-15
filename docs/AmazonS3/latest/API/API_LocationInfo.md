# LocationInfo

Specifies the location where the bucket will be created.

For directory buckets, the location type is Availability Zone or Local Zone. For more information about
 directory buckets, see [Working with
 directory buckets](../userguide/directory-buckets-overview.md "../userguide/directory-buckets-overview.md") in the *Amazon S3 User Guide*.

###### Note

This functionality is only supported by directory buckets.


## Contents





**Name** 


The name of the location where the bucket will be created.


For directory buckets, the name of the location is the Zone ID of the Availability Zone (AZ) or Local Zone (LZ) where
 the bucket will be created. An example AZ ID value is `usw2-az1`.


Type: String


Required: No




**Type** 


The type of location where the bucket will be created.


Type: String


Valid Values: `AvailabilityZone | LocalZone`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/LocationInfo "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/LocationInfo")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/LocationInfo "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/LocationInfo")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/LocationInfo "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/LocationInfo")
