# DirectoryConnectSettingsDescription

Contains information about an AD Connector directory.

## Contents

**AvailabilityZones**

The Availability Zones that the directory is in.

Type: Array of strings

Required: No

**ConnectIps**

The IP addresses of the AD Connector servers.

Type: Array of strings

Pattern: `^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$`

Required: No

**ConnectIpsV6**

The IPv6 addresses of the AD Connector servers.

Type: Array of strings

Pattern: `^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$`

Required: No

**CustomerUserName**

The user name of the service account in your self-managed directory.

Type: String

Length Constraints: Minimum length of 1.

Pattern: `[a-zA-Z0-9._-]+`

Required: No

**SecurityGroupId**

The security group identifier for the AD Connector directory.

Type: String

Pattern: `^(sg-[0-9a-f]{8}|sg-[0-9a-f]{17})$`

Required: No

**SubnetIds**

A list of subnet identifiers in the VPC that the AD Connector is in.

Type: Array of strings

Pattern: `^(subnet-[0-9a-f]{8}|subnet-[0-9a-f]{17})$`

Required: No

**VpcId**

The identifier of the VPC that the AD Connector is in.

Type: String

Pattern: `^(vpc-[0-9a-f]{8}|vpc-[0-9a-f]{17})$`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/DirectoryConnectSettingsDescription.md "../../../goto/SdkForCpp/ds-2015-04-16/DirectoryConnectSettingsDescription.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/DirectoryConnectSettingsDescription.md "../../../goto/SdkForJavaV2/ds-2015-04-16/DirectoryConnectSettingsDescription.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/DirectoryConnectSettingsDescription.md "../../../goto/SdkForRubyV3/ds-2015-04-16/DirectoryConnectSettingsDescription.md")
