# DeleteDBSubnetGroup

Deletes a subnet group.

###### Note

The specified database subnet group must not be associated with any DB
instances.

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

**DBSubnetGroupName**

The name of the database subnet group to delete.

###### Note

You can't delete the default subnet group.

Constraints:

Must match the name of an existing `DBSubnetGroup`. Must not be default.

Example: `mySubnetgroup`

Type: String

Required: Yes

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**DBSubnetGroupNotFoundFault**

`DBSubnetGroupName` doesn't refer to an existing subnet group.

HTTP Status Code: 404

**InvalidDBSubnetGroupStateFault**

The subnet group can't be deleted because it's in use.

HTTP Status Code: 400

**InvalidDBSubnetStateFault**

The subnet isn't in the _available_ state.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/docdb-2014-10-31/DeleteDBSubnetGroup.md "../../../goto/cli2/docdb-2014-10-31/DeleteDBSubnetGroup.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/docdb-2014-10-31/DeleteDBSubnetGroup.md "../../../goto/DotNetSDKV4/docdb-2014-10-31/DeleteDBSubnetGroup.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/docdb-2014-10-31/DeleteDBSubnetGroup.md "../../../goto/SdkForCpp/docdb-2014-10-31/DeleteDBSubnetGroup.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/docdb-2014-10-31/DeleteDBSubnetGroup.md "../../../goto/SdkForGoV2/docdb-2014-10-31/DeleteDBSubnetGroup.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/docdb-2014-10-31/DeleteDBSubnetGroup.md "../../../goto/SdkForJavaV2/docdb-2014-10-31/DeleteDBSubnetGroup.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/DeleteDBSubnetGroup.md "../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/DeleteDBSubnetGroup.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/docdb-2014-10-31/DeleteDBSubnetGroup.md "../../../goto/SdkForKotlin/docdb-2014-10-31/DeleteDBSubnetGroup.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/docdb-2014-10-31/DeleteDBSubnetGroup.md "../../../goto/SdkForPHPV3/docdb-2014-10-31/DeleteDBSubnetGroup.md")
- [AWS SDK for Python](../../../goto/boto3/docdb-2014-10-31/DeleteDBSubnetGroup.md "../../../goto/boto3/docdb-2014-10-31/DeleteDBSubnetGroup.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/docdb-2014-10-31/DeleteDBSubnetGroup.md "../../../goto/SdkForRubyV3/docdb-2014-10-31/DeleteDBSubnetGroup.md")
