# SelfManagedKafkaAccessConfigurationVpc

This structure specifies the VPC subnets and security groups for the stream, and whether
a public IP address is to be used.

## Contents

**SecurityGroup**

Specifies the security groups associated with the stream. These security groups must all
be in the same VPC. You can specify as many as five security groups.

Type: Array of strings

Array Members: Minimum number of 1 item. Maximum number of 5 items.

Length Constraints: Minimum length of 1. Maximum length of 1024.

Pattern: `sg-[0-9a-zA-Z]*`

Required: No

**Subnets**

Specifies the subnets associated with the stream. These subnets must all be in the same
VPC. You can specify as many as 16 subnets.

Type: Array of strings

Array Members: Minimum number of 1 item. Maximum number of 16 items.

Length Constraints: Minimum length of 1. Maximum length of 1024.

Pattern: `subnet-[0-9a-z]*`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/pipes-2015-10-07/SelfManagedKafkaAccessConfigurationVpc.md "../../../goto/SdkForCpp/pipes-2015-10-07/SelfManagedKafkaAccessConfigurationVpc.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/pipes-2015-10-07/SelfManagedKafkaAccessConfigurationVpc.md "../../../goto/SdkForJavaV2/pipes-2015-10-07/SelfManagedKafkaAccessConfigurationVpc.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/pipes-2015-10-07/SelfManagedKafkaAccessConfigurationVpc.md "../../../goto/SdkForRubyV3/pipes-2015-10-07/SelfManagedKafkaAccessConfigurationVpc.md")
