# OwnerDirectoryDescription

Contains the directory owner account details shared with the directory consumer
account.

## Contents

**AccountId**

Identifier of the directory owner account.

Type: String

Pattern: `^(\d{12})$`

Required: No

**DirectoryId**

Identifier of the AWS Managed Microsoft AD directory in the directory owner account.

Type: String

Pattern: `^d-[0-9a-f]{10}$`

Required: No

**DnsIpAddrs**

IP address of the directory’s domain controllers.

Type: Array of strings

Pattern: `^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$`

Required: No

**DnsIpv6Addrs**

IPv6 addresses of the directory’s domain controllers.

Type: Array of strings

Pattern: `^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$`

Required: No

**NetworkType**

Network type of the directory in the directory owner account.

Type: String

Valid Values: `Dual-stack | IPv4 | IPv6`

Required: No

**RadiusSettings**

Information about the [RadiusSettings](API_RadiusSettings.md "API_RadiusSettings.md") object server configuration.

Type: [RadiusSettings](API_RadiusSettings.md "API_RadiusSettings.md") object

Required: No

**RadiusStatus**

The status of the RADIUS server.

Type: String

Valid Values: `Creating | Completed | Failed`

Required: No

**VpcSettings**

Information about the VPC settings for the directory.

Type: [DirectoryVpcSettingsDescription](API_DirectoryVpcSettingsDescription.md "API_DirectoryVpcSettingsDescription.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/OwnerDirectoryDescription.md "../../../goto/SdkForCpp/ds-2015-04-16/OwnerDirectoryDescription.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/OwnerDirectoryDescription.md "../../../goto/SdkForJavaV2/ds-2015-04-16/OwnerDirectoryDescription.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/OwnerDirectoryDescription.md "../../../goto/SdkForRubyV3/ds-2015-04-16/OwnerDirectoryDescription.md")
