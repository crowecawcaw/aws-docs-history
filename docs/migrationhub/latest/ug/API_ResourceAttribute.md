AWS Migration Hub will no longer be open to new customers starting November 7, 2025. To continue using the service, sign up prior to November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# ResourceAttribute

Attribute associated with a resource.

Note the corresponding format required per type listed below:

IPV4

`x.x.x.x`

_where x is an integer in the range [0,255]_

IPV6

`y : y : y : y : y : y : y : y`

_where y is a hexadecimal between 0 and FFFF. [0,
FFFF]_

MAC_ADDRESS

`^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$`

FQDN

`^[^<>{}\\\\/?,=\\p{Cntrl}]{1,256}$`

## Contents

**Type**

Type of resource.

Type: String

Valid Values: `IPV4_ADDRESS | IPV6_ADDRESS | MAC_ADDRESS | FQDN | VM_MANAGER_ID | VM_MANAGED_OBJECT_REFERENCE | VM_NAME | VM_PATH | BIOS_ID | MOTHERBOARD_SERIAL_NUMBER`

Required: Yes

**Value**

Value of the resource type.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `^.{1,256}$`

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/AWSMigrationHub-2017-05-31/ResourceAttribute.md "../../../goto/SdkForCpp/AWSMigrationHub-2017-05-31/ResourceAttribute.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/AWSMigrationHub-2017-05-31/ResourceAttribute.md "../../../goto/SdkForJavaV2/AWSMigrationHub-2017-05-31/ResourceAttribute.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/AWSMigrationHub-2017-05-31/ResourceAttribute.md "../../../goto/SdkForRubyV3/AWSMigrationHub-2017-05-31/ResourceAttribute.md")
