# JobManifestLocation

Contains the information required to locate a manifest object. Manifests can't be
 imported from directory buckets. For more information, see [Directory
 buckets](../userguide/directory-buckets-overview.md "../userguide/directory-buckets-overview.md").


## Contents





**ETag** 


The ETag for the specified manifest object.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: Yes




**ObjectArn** 


The Amazon Resource Name (ARN) for a manifest object.


###### Important

When you're using XML requests, you must 
replace special characters (such as carriage returns) in object keys with their equivalent XML entity codes. 
For more information, see [XML-related object key constraints](../userguide/object-keys.md#object-key-xml-related-constraints "../userguide/object-keys.md#object-key-xml-related-constraints") in the *Amazon S3 User Guide*.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 2000.


Pattern: `arn:[^:]+:s3:.*`



Required: Yes




**ObjectVersionId** 


The optional version ID to identify a specific version of the manifest object.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 2000.


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/JobManifestLocation "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/JobManifestLocation")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/JobManifestLocation "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/JobManifestLocation")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/JobManifestLocation "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/JobManifestLocation")
