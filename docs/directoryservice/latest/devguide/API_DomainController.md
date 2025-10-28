# DomainController

Contains information about the domain controllers for a specified directory.

## Contents

**AvailabilityZone**

The Availability Zone where the domain controller is located.

Type: String

Required: No

**DirectoryId**

Identifier of the directory where the domain controller resides.

Type: String

Pattern: `^d-[0-9a-f]{10}$`

Required: No

**DnsIpAddr**

The IP address of the domain controller.

Type: String

Pattern: `^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$`

Required: No

**DnsIpv6Addr**

The IPv6 address of the domain controller.

Type: String

Pattern: `^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$`

Required: No

**DomainControllerId**

Identifies a specific domain controller in the directory.

Type: String

Pattern: `^dc-[0-9a-f]{10}$`

Required: No

**LaunchTime**

Specifies when the domain controller was created.

Type: Timestamp

Required: No

**Status**

The status of the domain controller.

Type: String

Valid Values: `Creating | Active | Impaired | Restoring | Deleting | Deleted | Failed | Updating`

Required: No

**StatusLastUpdatedDateTime**

The date and time that the status was last updated.

Type: Timestamp

Required: No

**StatusReason**

A description of the domain controller state.

Type: String

Required: No

**SubnetId**

Identifier of the subnet in the VPC that contains the domain controller.

Type: String

Pattern: `^(subnet-[0-9a-f]{8}|subnet-[0-9a-f]{17})$`

Required: No

**VpcId**

The identifier of the VPC that contains the domain controller.

Type: String

Pattern: `^(vpc-[0-9a-f]{8}|vpc-[0-9a-f]{17})$`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/DomainController.md "../../../goto/SdkForCpp/ds-2015-04-16/DomainController.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/DomainController.md "../../../goto/SdkForJavaV2/ds-2015-04-16/DomainController.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/DomainController.md "../../../goto/SdkForRubyV3/ds-2015-04-16/DomainController.md")
