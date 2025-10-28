# ClientAuthenticationSettingInfo

Contains information about a client authentication method for a directory.

## Contents

**LastUpdatedDateTime**

The date and time when the status of the client authentication type was last
updated.

Type: Timestamp

Required: No

**Status**

Whether the client authentication type is enabled or disabled for the specified
directory.

Type: String

Valid Values: `Enabled | Disabled`

Required: No

**Type**

The type of client authentication for the specified directory. If no type is specified, a
list of all client authentication types that are supported for the directory is retrieved.

Type: String

Valid Values: `SmartCard | SmartCardOrPassword`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/ClientAuthenticationSettingInfo.md "../../../goto/SdkForCpp/ds-2015-04-16/ClientAuthenticationSettingInfo.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/ClientAuthenticationSettingInfo.md "../../../goto/SdkForJavaV2/ds-2015-04-16/ClientAuthenticationSettingInfo.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/ClientAuthenticationSettingInfo.md "../../../goto/SdkForRubyV3/ds-2015-04-16/ClientAuthenticationSettingInfo.md")
