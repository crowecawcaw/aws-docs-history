# CreateBucketConfiguration

The configuration information for the bucket.


## Contents





**Bucket** 


Specifies the information about the bucket that will be created.


###### Note

This functionality is only supported by directory buckets.


Type: [BucketInfo](API_BucketInfo.md "API_BucketInfo.md") data type


Required: No




**Location** 


Specifies the location where the bucket will be created.



**Directory buckets**  - The location type is Availability Zone or Local Zone. To
 use the Local Zone location type, your account must be enabled
 for Local Zones. Otherwise, you get an HTTP `403 Forbidden` error with the error code
 `AccessDenied`. To learn more,
 see [Enable
 accounts for Local Zones](../userguide/opt-in-directory-bucket-lz.md "../userguide/opt-in-directory-bucket-lz.md") in the *Amazon S3 User Guide*. 


###### Note

This functionality is only supported by directory buckets.


Type: [LocationInfo](API_LocationInfo.md "API_LocationInfo.md") data type


Required: No




**LocationConstraint** 


Specifies the Region where the bucket will be created. You might choose a Region to optimize
 latency, minimize costs, or address regulatory requirements. For example, if you reside in Europe, you
 will probably find it advantageous to create buckets in the Europe (Ireland) Region.


If you don't specify a Region, the bucket is created in the US East (N. Virginia) Region (us-east-1)
 by default. Configurations using the value `EU` will create a bucket in
 `eu-west-1`.


For a list of the valid values for all of the AWS Regions, see [Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region "https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region").


###### Note

This functionality is not supported for directory buckets.


Type: String


Valid Values: `af-south-1 | ap-east-1 | ap-northeast-1 | ap-northeast-2 | ap-northeast-3 | ap-south-1 | ap-south-2 | ap-southeast-1 | ap-southeast-2 | ap-southeast-3 | ap-southeast-4 | ap-southeast-5 | ca-central-1 | cn-north-1 | cn-northwest-1 | EU | eu-central-1 | eu-central-2 | eu-north-1 | eu-south-1 | eu-south-2 | eu-west-1 | eu-west-2 | eu-west-3 | il-central-1 | me-central-1 | me-south-1 | sa-east-1 | us-east-2 | us-gov-east-1 | us-gov-west-1 | us-west-1 | us-west-2`



Required: No




**Tags** 


An array of tags that you can apply to the bucket that you're creating. Tags are key-value pairs of
 metadata used to categorize and organize your buckets, track costs, and control access. 


###### Note


* This parameter is only supported for S3 directory buckets. For more information, see [Using tags with
 directory buckets](../userguide/directory-buckets-tagging.md "../userguide/directory-buckets-tagging.md").
* You must have the `s3express:TagResource` permission to create a directory bucket with tags.

Type: Array of [Tag](API_Tag.md "API_Tag.md") data types


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/CreateBucketConfiguration "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/CreateBucketConfiguration")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/CreateBucketConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/CreateBucketConfiguration")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/CreateBucketConfiguration "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/CreateBucketConfiguration")
