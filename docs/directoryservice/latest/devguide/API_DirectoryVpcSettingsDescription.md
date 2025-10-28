# DirectoryVpcSettingsDescription

Contains information about the directory.

## Contents

**AvailabilityZones**

The list of Availability Zones that the directory is in.

Type: Array of strings

Required: No

**SecurityGroupId**

The domain controller security group identifier for the directory.

Type: String

Pattern: `^(sg-[0-9a-f]{8}|sg-[0-9a-f]{17})$`

Required: No

**SubnetIds**

The identifiers of the subnets for the directory servers.

Type: Array of strings

Pattern: `^(subnet-[0-9a-f]{8}|subnet-[0-9a-f]{17})$`

Required: No

**VpcId**

The identifier of the VPC that the directory is in.

Type: String

Pattern: `^(vpc-[0-9a-f]{8}|vpc-[0-9a-f]{17})$`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/DirectoryVpcSettingsDescription.md "../../../goto/SdkForCpp/ds-2015-04-16/DirectoryVpcSettingsDescription.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/DirectoryVpcSettingsDescription.md "../../../goto/SdkForJavaV2/ds-2015-04-16/DirectoryVpcSettingsDescription.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/DirectoryVpcSettingsDescription.md "../../../goto/SdkForRubyV3/ds-2015-04-16/DirectoryVpcSettingsDescription.md")
