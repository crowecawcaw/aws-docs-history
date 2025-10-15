# NamespaceSummary

Contains details about a namespace.


## Contents





**createdAt** 


The date and time the namespace was created at.


Type: Timestamp


Required: Yes




**createdBy** 


The ID of the account that created the namespace.


Type: String


Length Constraints: Fixed length of 12.


Pattern: `[0-9].*`



Required: Yes




**namespace** 


The name of the namespace.


Type: Array of strings


Length Constraints: Minimum length of 1. Maximum length of 255.


Pattern: `[0-9a-z_]*`



Required: Yes




**ownerAccountId** 


The ID of the account that owns the namespace.


Type: String


Length Constraints: Fixed length of 12.


Pattern: `[0-9].*`



Required: Yes




**namespaceId** 


The system-assigned unique identifier for the namespace.


Type: String


Required: No




**tableBucketId** 


The system-assigned unique identifier for the table bucket that contains this namespace.


Type: String


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/NamespaceSummary "https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/NamespaceSummary")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/NamespaceSummary "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/NamespaceSummary")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/NamespaceSummary "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/NamespaceSummary")
