# S3JobManifestGenerator

The container for the service that will create the S3 manifest.


## Contents





**EnableManifestOutput** 


Determines whether or not to write the job's generated manifest to a bucket.


Type: Boolean


Required: Yes




**SourceBucket** 


The ARN of the source bucket used by the ManifestGenerator.


###### Note


**Directory buckets** - Directory buckets
 aren't supported as the source buckets used by `S3JobManifestGenerator` to
 generate the job manifest.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 128.


Pattern: `arn:[^:]+:s3:.*`



Required: Yes




**ExpectedBucketOwner** 


The AWS account ID that owns the bucket the generated manifest is written to. If
 provided the generated manifest bucket's owner AWS account ID must match this value, else
 the job fails.


Type: String


Length Constraints: Maximum length of 64.


Pattern: `^\d{12}$`



Required: No




**Filter** 


Specifies rules the S3JobManifestGenerator should use to decide whether an object in the
 source bucket should or should not be included in the generated job manifest.


Type: [JobManifestGeneratorFilter](API_control_JobManifestGeneratorFilter.md "API_control_JobManifestGeneratorFilter.md") data type


Required: No




**ManifestOutputLocation** 


Specifies the location the generated manifest will be written to. Manifests can't be
 written to directory buckets. For more information, see [Directory
 buckets](../userguide/directory-buckets-overview.md "../userguide/directory-buckets-overview.md").


Type: [S3ManifestOutputLocation](API_control_S3ManifestOutputLocation.md "API_control_S3ManifestOutputLocation.md") data type


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/S3JobManifestGenerator "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/S3JobManifestGenerator")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/S3JobManifestGenerator "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/S3JobManifestGenerator")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/S3JobManifestGenerator "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/S3JobManifestGenerator")
