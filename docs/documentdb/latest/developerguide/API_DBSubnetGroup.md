# DBSubnetGroup

Detailed information about a subnet group.

## Contents

###### Note

In the following list, the required parameters are described first.

**DBSubnetGroupArn**

The Amazon Resource Name (ARN) for the DB subnet group.

Type: String

Required: No

**DBSubnetGroupDescription**

Provides the description of the subnet group.

Type: String

Required: No

**DBSubnetGroupName**

The name of the subnet group.

Type: String

Required: No

**SubnetGroupStatus**

Provides the status of the subnet group.

Type: String

Required: No

**Subnets.Subnet.N**

Detailed information about one or more subnets within a subnet group.

Type: Array of [Subnet](API_Subnet.md "API_Subnet.md") objects

Required: No

**SupportedNetworkTypes.member.N**

The network type of the DB subnet group.

Valid Values: `IPV4` | `DUAL`

A `DBSubnetGroup` can support only the IPv4 protocol or the IPv4 and the IPv6 protocols (DUAL).

Type: Array of strings

Required: No

**VpcId**

Provides the virtual private cloud (VPC) ID of the subnet group.

Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/docdb-2014-10-31/DBSubnetGroup.md "../../../goto/SdkForCpp/docdb-2014-10-31/DBSubnetGroup.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/docdb-2014-10-31/DBSubnetGroup.md "../../../goto/SdkForJavaV2/docdb-2014-10-31/DBSubnetGroup.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/docdb-2014-10-31/DBSubnetGroup.md "../../../goto/SdkForRubyV3/docdb-2014-10-31/DBSubnetGroup.md")
