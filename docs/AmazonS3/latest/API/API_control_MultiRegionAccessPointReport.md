# MultiRegionAccessPointReport

A collection of statuses for a Multi-Region Access Point in the various Regions it supports.


## Contents





**Alias** 


The alias for the Multi-Region Access Point. For more information about the distinction between the name
 and the alias of an Multi-Region Access Point, see [Rules for naming Amazon S3 Multi-Region Access Points](../userguide/CreatingMultiRegionAccessPoints.md#multi-region-access-point-naming "../userguide/CreatingMultiRegionAccessPoints.md#multi-region-access-point-naming").


Type: String


Length Constraints: Maximum length of 63.


Pattern: `^[a-z][a-z0-9]*[.]mrap$`



Required: No




**CreatedAt** 


When the Multi-Region Access Point create request was received.


Type: Timestamp


Required: No




**Name** 


The name of the Multi-Region Access Point.


Type: String


Length Constraints: Maximum length of 50.


Pattern: `^[a-z0-9][-a-z0-9]{1,48}[a-z0-9]$`



Required: No




**PublicAccessBlock** 


The `PublicAccessBlock` configuration that you want to apply to this Amazon S3
 account. You can enable the configuration options in any combination. For more information
 about when Amazon S3 considers a bucket or object public, see [The Meaning of "Public"](https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html#access-control-block-public-access-policy-status "https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html#access-control-block-public-access-policy-status") in the *Amazon S3 User Guide*.


This data type is not supported for Amazon S3 on Outposts.


Type: [PublicAccessBlockConfiguration](API_control_PublicAccessBlockConfiguration.md "API_control_PublicAccessBlockConfiguration.md") data type


Required: No




**Regions** 


A collection of the Regions and buckets associated with the Multi-Region Access Point.


Type: Array of [RegionReport](API_control_RegionReport.md "API_control_RegionReport.md") data types


Required: No




**Status** 


The current status of the Multi-Region Access Point.



`CREATING` and `DELETING` are temporary states that exist while
 the request is propagating and being completed. If a Multi-Region Access Point has a status of
 `PARTIALLY_CREATED`, you can retry creation or send a request to delete the
 Multi-Region Access Point. If a Multi-Region Access Point has a status of `PARTIALLY_DELETED`, you can retry a delete
 request to finish the deletion of the Multi-Region Access Point.


Type: String


Valid Values: `READY | INCONSISTENT_ACROSS_REGIONS | CREATING | PARTIALLY_CREATED | PARTIALLY_DELETED | DELETING`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/MultiRegionAccessPointReport "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/MultiRegionAccessPointReport")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/MultiRegionAccessPointReport "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/MultiRegionAccessPointReport")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/MultiRegionAccessPointReport "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/MultiRegionAccessPointReport")
