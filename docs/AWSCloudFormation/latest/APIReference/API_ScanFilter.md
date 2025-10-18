# ScanFilter

A filter that is used to specify which resource types to scan.


## Contents





**Types.member.N** 


An array of strings where each string represents an AWS resource type you want to scan.
 Each string defines the resource type using the format
 `AWS::ServiceName::ResourceType`, for example, `AWS::DynamoDB::Table`. For
 the full list of supported resource types, see the [Resource type
 support](../UserGuide/resource-import-supported-resources.md "../UserGuide/resource-import-supported-resources.md") table in the *AWS CloudFormation User Guide*.


To scan all resource types within a service, you can use a wildcard, represented by an
 asterisk (`*`). You can place an asterisk at only the end of the string, for example,
 `AWS::S3::*`.


Type: Array of strings


Array Members: Maximum number of 100 items.


Length Constraints: Minimum length of 1. Maximum length of 100.


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/ScanFilter "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/ScanFilter")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/ScanFilter "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/ScanFilter")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/ScanFilter "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/ScanFilter")
