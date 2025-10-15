# JobManifest

Contains the configuration information for a job's manifest.


## Contents





**Location** 


Contains the information required to locate the specified job's manifest. Manifests
 can't be imported from directory buckets. For more information, see [Directory buckets](../userguide/directory-buckets-overview.md "../userguide/directory-buckets-overview.md").


Type: [JobManifestLocation](API_control_JobManifestLocation.md "API_control_JobManifestLocation.md") data type


Required: Yes




**Spec** 


Describes the format of the specified job's manifest. If the manifest is in CSV format,
 also describes the columns contained within the manifest.


Type: [JobManifestSpec](API_control_JobManifestSpec.md "API_control_JobManifestSpec.md") data type


Required: Yes




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/JobManifest "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/JobManifest")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/JobManifest "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/JobManifest")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/JobManifest "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/JobManifest")
