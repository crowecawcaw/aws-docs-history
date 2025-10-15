# Owner

###### Important

End of support notice: Beginning November 21, 2025, Amazon S3 will stop returning `DisplayName`. Update your applications to use canonical IDs (unique identifier for 
 AWS accounts), AWS account ID (12 digit identifier) or IAM ARNs (full resource naming) as a direct replacement of `DisplayName`.


Between July 15, 2025 and November 21, 2025, you will begin to see an increasing rate of missing `DisplayName` in the Owner object.

This change affects the following AWS Regions: US East (N. Virginia) Region, US West (N. California) Region, US West (Oregon) Region, Asia Pacific (Singapore) Region, Asia Pacific (Sydney) Region, 
 Asia Pacific (Tokyo) Region, Europe (Ireland) Region, and South America (São Paulo) Region.

Container for the owner's display name and ID.


## Contents





**DisplayName** 


Container for the display name of the owner. This value is only supported in the following AWS
 Regions:



* US East (N. Virginia)
* US West (N. California)
* US West (Oregon)
* Asia Pacific (Singapore)
* Asia Pacific (Sydney)
* Asia Pacific (Tokyo)
* Europe (Ireland)
* South America (São Paulo)

###### Note

This functionality is not supported for directory buckets.


Type: String


Required: No




**ID** 


Container for the ID of the owner.


Type: String


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/Owner "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/Owner")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/Owner "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/Owner")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/Owner "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/Owner")
