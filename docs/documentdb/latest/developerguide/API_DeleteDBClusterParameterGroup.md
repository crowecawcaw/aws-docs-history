# DeleteDBClusterParameterGroup

Deletes a specified cluster parameter group. The cluster parameter group to be deleted can't be associated with any clusters.

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

**DBClusterParameterGroupName**

The name of the cluster parameter group.

Constraints:

- Must be the name of an existing cluster parameter group.
- You can't delete a default cluster parameter group.
- Cannot be associated with any clusters.

Type: String

Required: Yes

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**DBParameterGroupNotFound**

`DBParameterGroupName` doesn't refer to an existing parameter group.

HTTP Status Code: 404

**InvalidDBParameterGroupState**

The parameter group is in use, or it is in a state that is not valid. If you are trying to delete the parameter group, you can't delete it when the parameter group is in this state.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/docdb-2014-10-31/DeleteDBClusterParameterGroup.md "../../../goto/cli2/docdb-2014-10-31/DeleteDBClusterParameterGroup.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/docdb-2014-10-31/DeleteDBClusterParameterGroup.md "../../../goto/DotNetSDKV4/docdb-2014-10-31/DeleteDBClusterParameterGroup.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/docdb-2014-10-31/DeleteDBClusterParameterGroup.md "../../../goto/SdkForCpp/docdb-2014-10-31/DeleteDBClusterParameterGroup.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/docdb-2014-10-31/DeleteDBClusterParameterGroup.md "../../../goto/SdkForGoV2/docdb-2014-10-31/DeleteDBClusterParameterGroup.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/docdb-2014-10-31/DeleteDBClusterParameterGroup.md "../../../goto/SdkForJavaV2/docdb-2014-10-31/DeleteDBClusterParameterGroup.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/DeleteDBClusterParameterGroup.md "../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/DeleteDBClusterParameterGroup.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/docdb-2014-10-31/DeleteDBClusterParameterGroup.md "../../../goto/SdkForKotlin/docdb-2014-10-31/DeleteDBClusterParameterGroup.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/docdb-2014-10-31/DeleteDBClusterParameterGroup.md "../../../goto/SdkForPHPV3/docdb-2014-10-31/DeleteDBClusterParameterGroup.md")
- [AWS SDK for Python](../../../goto/boto3/docdb-2014-10-31/DeleteDBClusterParameterGroup.md "../../../goto/boto3/docdb-2014-10-31/DeleteDBClusterParameterGroup.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/docdb-2014-10-31/DeleteDBClusterParameterGroup.md "../../../goto/SdkForRubyV3/docdb-2014-10-31/DeleteDBClusterParameterGroup.md")
