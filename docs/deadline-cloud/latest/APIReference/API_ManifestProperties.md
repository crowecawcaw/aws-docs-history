# ManifestProperties

The details of the manifest that links a job's source information.


## Contents





**rootPath** 


The file's root path.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: Yes




**rootPathFormat** 


The format of the root path.


Type: String


Valid Values: `windows | posix`



Required: Yes




**fileSystemLocationName** 


The file system location name.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 64.


Pattern: `[0-9A-Za-z ]*`



Required: No




**inputManifestHash** 


The hash value of the file.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 256.


Required: No




**inputManifestPath** 


The file path.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 512.


Required: No




**outputRelativeDirectories** 


The file path relative to the directory.


Type: Array of strings


Array Members: Minimum number of 0 items. Maximum number of 100 items.


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/ManifestProperties "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/ManifestProperties")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/ManifestProperties "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/ManifestProperties")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/ManifestProperties "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/ManifestProperties")
