# ResetDBClusterParameterGroup

Modifies the parameters of a cluster parameter group to the default value. To
reset specific parameters, submit a list of the following: `ParameterName`
and `ApplyMethod`. To reset the entire cluster parameter group, specify
the `DBClusterParameterGroupName` and `ResetAllParameters`
parameters.

When you reset the entire group, dynamic parameters are updated immediately and
static parameters are set to `pending-reboot` to take effect on the next DB
instance reboot.

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

**DBClusterParameterGroupName**

The name of the cluster parameter group to reset.

Type: String

Required: Yes

**Parameters.Parameter.N**

A list of parameter names in the cluster parameter group to reset to the default
values. You can't use this parameter if the `ResetAllParameters` parameter is
set to `true`.

Type: Array of [Parameter](API_Parameter.md "API_Parameter.md") objects

Required: No

**ResetAllParameters**

A value that is set to `true` to reset all parameters in the cluster
parameter group to their default values, and `false` otherwise. You can't use
this parameter if there is a list of parameter names specified for the
`Parameters` parameter.

Type: Boolean

Required: No

## Response Elements

The following element is returned by the service.

**DBClusterParameterGroupName**

The name of a cluster parameter group.

Constraints:

- Must be from 1 to 255 letters or numbers.
- The first character must be a letter.
- Cannot end with a hyphen or contain two consecutive hyphens.

###### Note

This value is stored as a lowercase string.

Type: String

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

- [AWS Command Line Interface V2](../../../goto/cli2/docdb-2014-10-31/ResetDBClusterParameterGroup.md "../../../goto/cli2/docdb-2014-10-31/ResetDBClusterParameterGroup.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/docdb-2014-10-31/ResetDBClusterParameterGroup.md "../../../goto/DotNetSDKV3/docdb-2014-10-31/ResetDBClusterParameterGroup.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/docdb-2014-10-31/ResetDBClusterParameterGroup.md "../../../goto/SdkForCpp/docdb-2014-10-31/ResetDBClusterParameterGroup.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/docdb-2014-10-31/ResetDBClusterParameterGroup.md "../../../goto/SdkForGoV2/docdb-2014-10-31/ResetDBClusterParameterGroup.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/docdb-2014-10-31/ResetDBClusterParameterGroup.md "../../../goto/SdkForJavaV2/docdb-2014-10-31/ResetDBClusterParameterGroup.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/ResetDBClusterParameterGroup.md "../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/ResetDBClusterParameterGroup.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/docdb-2014-10-31/ResetDBClusterParameterGroup.md "../../../goto/SdkForKotlin/docdb-2014-10-31/ResetDBClusterParameterGroup.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/docdb-2014-10-31/ResetDBClusterParameterGroup.md "../../../goto/SdkForPHPV3/docdb-2014-10-31/ResetDBClusterParameterGroup.md")
- [AWS SDK for Python](../../../goto/boto3/docdb-2014-10-31/ResetDBClusterParameterGroup.md "../../../goto/boto3/docdb-2014-10-31/ResetDBClusterParameterGroup.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/docdb-2014-10-31/ResetDBClusterParameterGroup.md "../../../goto/SdkForRubyV3/docdb-2014-10-31/ResetDBClusterParameterGroup.md")
