# CreateDBSubnetGroup

Creates a new subnet group. subnet groups must contain at least one subnet in at
least two Availability Zones in the AWS Region.

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

**DBSubnetGroupDescription**

The description for the subnet group.

Type: String

Required: Yes

**DBSubnetGroupName**

The name for the subnet group. This value is stored as a lowercase string.

Constraints: Must contain no more than 255 letters, numbers, periods, underscores,
spaces, or hyphens. Must not be default.

Example: `mySubnetgroup`

Type: String

Required: Yes

**SubnetIds.SubnetIdentifier.N**

The Amazon EC2 subnet IDs for the subnet group.

Type: Array of strings

Required: Yes

**Tags.Tag.N**

The tags to be assigned to the subnet group.

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

Required: No

## Response Elements

The following element is returned by the service.

**DBSubnetGroup**

Detailed information about a subnet group.

Type: [DBSubnetGroup](API_DBSubnetGroup.md "API_DBSubnetGroup.md") object

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**DBSubnetGroupAlreadyExists**

`DBSubnetGroupName` is already being used by an existing subnet group.

HTTP Status Code: 400

**DBSubnetGroupDoesNotCoverEnoughAZs**

Subnets in the subnet group should cover at least two Availability Zones unless there is only one Availability Zone.

HTTP Status Code: 400

**DBSubnetGroupQuotaExceeded**

The request would cause you to exceed the allowed number of subnet groups.

HTTP Status Code: 400

**DBSubnetQuotaExceededFault**

The request would cause you to exceed the allowed number of subnets in a subnet group.

HTTP Status Code: 400

**InvalidSubnet**

The requested subnet is not valid, or multiple subnets were requested that are not all
in a common virtual private cloud (VPC).

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/docdb-2014-10-31/CreateDBSubnetGroup.md "../../../goto/cli2/docdb-2014-10-31/CreateDBSubnetGroup.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/docdb-2014-10-31/CreateDBSubnetGroup.md "../../../goto/DotNetSDKV4/docdb-2014-10-31/CreateDBSubnetGroup.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/docdb-2014-10-31/CreateDBSubnetGroup.md "../../../goto/SdkForCpp/docdb-2014-10-31/CreateDBSubnetGroup.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/docdb-2014-10-31/CreateDBSubnetGroup.md "../../../goto/SdkForGoV2/docdb-2014-10-31/CreateDBSubnetGroup.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/docdb-2014-10-31/CreateDBSubnetGroup.md "../../../goto/SdkForJavaV2/docdb-2014-10-31/CreateDBSubnetGroup.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/CreateDBSubnetGroup.md "../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/CreateDBSubnetGroup.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/docdb-2014-10-31/CreateDBSubnetGroup.md "../../../goto/SdkForKotlin/docdb-2014-10-31/CreateDBSubnetGroup.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/docdb-2014-10-31/CreateDBSubnetGroup.md "../../../goto/SdkForPHPV3/docdb-2014-10-31/CreateDBSubnetGroup.md")
- [AWS SDK for Python](../../../goto/boto3/docdb-2014-10-31/CreateDBSubnetGroup.md "../../../goto/boto3/docdb-2014-10-31/CreateDBSubnetGroup.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/docdb-2014-10-31/CreateDBSubnetGroup.md "../../../goto/SdkForRubyV3/docdb-2014-10-31/CreateDBSubnetGroup.md")
