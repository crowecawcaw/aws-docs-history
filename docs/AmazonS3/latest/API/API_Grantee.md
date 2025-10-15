# Grantee

###### Important

End of support notice: Beginning November 21, 2025, Amazon S3 will stop returning `DisplayName`. Update your applications to use canonical IDs (unique identifier for 
 AWS accounts), AWS account ID (12 digit identifier) or IAM ARNs (full resource naming) as a direct replacement of `DisplayName`.


Between July 15, 2025 and November 21, 2025, you will begin to see an increasing rate of missing `DisplayName` in the Owner object.

This change affects the following AWS Regions: US East (N. Virginia) Region, US West (N. California) Region, US West (Oregon) Region, Asia Pacific (Singapore) Region, Asia Pacific (Sydney) Region, 
 Asia Pacific (Tokyo) Region, Europe (Ireland) Region, and South America (São Paulo) Region.

Container for the person being granted permissions.


## Contents





**Type** 


Type of grantee


Type: String


Valid Values: `CanonicalUser | AmazonCustomerByEmail | Group`



Required: Yes




**DisplayName** 


Screen name of the grantee.


Type: String


Required: No




**EmailAddress** 


Email address of the grantee.


###### Note

Using email addresses to specify a grantee is only supported in the following AWS Regions: 


* US East (N. Virginia)
* US West (N. California)
* US West (Oregon)
* Asia Pacific (Singapore)
* Asia Pacific (Sydney)
* Asia Pacific (Tokyo)
* Europe (Ireland)
* South America (São Paulo)
For a list of all the Amazon S3 supported Regions and endpoints, see [Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region "https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region") in the AWS General Reference.


Type: String


Required: No




**ID** 


The canonical user ID of the grantee.


Type: String


Required: No




**URI** 


URI of the grantee group.


Type: String


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/Grantee "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/Grantee")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/Grantee "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/Grantee")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/Grantee "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/Grantee")
