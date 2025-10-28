# NetworkUpdateSettings

Contains the network configuration for directory update operations.

## Contents

**CustomerDnsIpsV6**

IPv6 addresses of DNS servers or domain controllers in the self-managed directory.
Required only when updating an AD Connector directory.

Type: Array of strings

Pattern: `^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$`

Required: No

**NetworkType**

The target network type for the directory update.

Type: String

Valid Values: `Dual-stack | IPv4 | IPv6`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/NetworkUpdateSettings.md "../../../goto/SdkForCpp/ds-2015-04-16/NetworkUpdateSettings.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/NetworkUpdateSettings.md "../../../goto/SdkForJavaV2/ds-2015-04-16/NetworkUpdateSettings.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/NetworkUpdateSettings.md "../../../goto/SdkForRubyV3/ds-2015-04-16/NetworkUpdateSettings.md")
