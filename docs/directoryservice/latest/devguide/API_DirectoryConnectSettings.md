# DirectoryConnectSettings

Contains connection settings for creating an AD
Connector with the [ConnectDirectory](API_ConnectDirectory.md "API_ConnectDirectory.md") action.

## Contents

**CustomerUserName**

The user name of an account in your self-managed directory that is used to connect to the
directory. This account must have the following permissions:

- Read users and groups
- Create computer objects
- Join computers to the domain

Type: String

Length Constraints: Minimum length of 1.

Pattern: `[a-zA-Z0-9._-]+`

Required: Yes

**SubnetIds**

A list of subnet identifiers in the VPC in which the AD Connector is created.

Type: Array of strings

Pattern: `^(subnet-[0-9a-f]{8}|subnet-[0-9a-f]{17})$`

Required: Yes

**VpcId**

The identifier of the VPC in which the AD Connector is created.

Type: String

Pattern: `^(vpc-[0-9a-f]{8}|vpc-[0-9a-f]{17})$`

Required: Yes

**CustomerDnsIps**

The IP addresses of DNS servers or domain controllers in your
self-managed directory.

Type: Array of strings

Pattern: `^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$`

Required: No

**CustomerDnsIpsV6**

The IPv6 addresses of DNS servers or domain controllers in your
self-managed directory.

Type: Array of strings

Pattern: `^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/DirectoryConnectSettings.md "../../../goto/SdkForCpp/ds-2015-04-16/DirectoryConnectSettings.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/DirectoryConnectSettings.md "../../../goto/SdkForJavaV2/ds-2015-04-16/DirectoryConnectSettings.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/DirectoryConnectSettings.md "../../../goto/SdkForRubyV3/ds-2015-04-16/DirectoryConnectSettings.md")
