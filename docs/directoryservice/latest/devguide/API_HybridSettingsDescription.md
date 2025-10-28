# HybridSettingsDescription

Describes the current hybrid directory configuration settings for a directory.

## Contents

**SelfManagedDnsIpAddrs**

The IP addresses of the DNS servers in your self-managed AD environment.

Type: Array of strings

Pattern: `^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$`

Required: No

**SelfManagedInstanceIds**

The identifiers of the self-managed instances with SSM used for hybrid directory
operations.

Type: Array of strings

Array Members: Fixed number of 2 items.

Pattern: `^(i-[0-9a-f]{8}|i-[0-9a-f]{17}|mi-[0-9a-f]{8}|mi-[0-9a-f]{17})$`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/HybridSettingsDescription.md "../../../goto/SdkForCpp/ds-2015-04-16/HybridSettingsDescription.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/HybridSettingsDescription.md "../../../goto/SdkForJavaV2/ds-2015-04-16/HybridSettingsDescription.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/HybridSettingsDescription.md "../../../goto/SdkForRubyV3/ds-2015-04-16/HybridSettingsDescription.md")
