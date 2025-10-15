# StorageLensConfiguration

A container for the Amazon S3 Storage Lens configuration.


## Contents





**AccountLevel** 


A container for all the account-level configurations of your S3 Storage Lens
 configuration.


Type: [AccountLevel](API_control_AccountLevel.md "API_control_AccountLevel.md") data type


Required: Yes




**Id** 


A container for the Amazon S3 Storage Lens configuration ID.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 64.


Pattern: `[a-zA-Z0-9\-\_\.]+`



Required: Yes




**IsEnabled** 


A container for whether the S3 Storage Lens configuration is enabled.


Type: Boolean


Required: Yes




**AwsOrg** 


A container for the AWS organization for this S3 Storage Lens configuration.


Type: [StorageLensAwsOrg](API_control_StorageLensAwsOrg.md "API_control_StorageLensAwsOrg.md") data type


Required: No




**DataExport** 


A container to specify the properties of your S3 Storage Lens metrics export including, the
 destination, schema and format.


Type: [StorageLensDataExport](API_control_StorageLensDataExport.md "API_control_StorageLensDataExport.md") data type


Required: No




**Exclude** 


A container for what is excluded in this configuration. This container can only be valid
 if there is no `Include` container submitted, and it's not empty. 


Type: [Exclude](API_control_Exclude.md "API_control_Exclude.md") data type


Required: No




**Include** 


A container for what is included in this configuration. This container can only be valid
 if there is no `Exclude` container submitted, and it's not empty. 


Type: [Include](API_control_Include.md "API_control_Include.md") data type


Required: No




**StorageLensArn** 


The Amazon Resource Name (ARN) of the S3 Storage Lens configuration. This property is read-only
 and follows the following format: `arn:aws:s3:*us-east-1*:*example-account-id*:storage-lens/*your-dashboard-name*`



Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Pattern: `arn:[a-z\-]+:s3:[a-z0-9\-]+:\d{12}:storage\-lens\/.*`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/StorageLensConfiguration "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/StorageLensConfiguration")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/StorageLensConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/StorageLensConfiguration")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/StorageLensConfiguration "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/StorageLensConfiguration")
