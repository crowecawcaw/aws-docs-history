# ModifyDBClusterParameterGroup

Modifies the parameters of a cluster parameter group. To modify more than one
parameter, submit a list of the following: `ParameterName`,
`ParameterValue`, and `ApplyMethod`. A maximum of 20
parameters can be modified in a single request.

###### Note

Changes to dynamic parameters are applied immediately. Changes to static
parameters require a reboot or maintenance window

before the change can take effect.

###### Important

After you create a cluster parameter group, you should wait at least 5 minutes
before creating your first cluster that uses that cluster parameter group as
the default parameter group. This allows Amazon DocumentDB to fully complete the create action
before the parameter group is used as the default for a new cluster. This step is
especially important for parameters that are critical when creating the default
database for a cluster, such as the character set for the default database
defined by the `character_set_database` parameter.

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

**DBClusterParameterGroupName**

The name of the cluster parameter group to modify.

Type: String

Required: Yes

**Parameters.Parameter.N**

A list of parameters in the cluster parameter group to modify.

Type: Array of [Parameter](API_Parameter.md "API_Parameter.md") objects

Required: Yes

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

- [AWS Command Line Interface V2](../../../goto/cli2/docdb-2014-10-31/ModifyDBClusterParameterGroup.md "../../../goto/cli2/docdb-2014-10-31/ModifyDBClusterParameterGroup.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/docdb-2014-10-31/ModifyDBClusterParameterGroup.md "../../../goto/DotNetSDKV3/docdb-2014-10-31/ModifyDBClusterParameterGroup.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/docdb-2014-10-31/ModifyDBClusterParameterGroup.md "../../../goto/SdkForCpp/docdb-2014-10-31/ModifyDBClusterParameterGroup.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/docdb-2014-10-31/ModifyDBClusterParameterGroup.md "../../../goto/SdkForGoV2/docdb-2014-10-31/ModifyDBClusterParameterGroup.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/docdb-2014-10-31/ModifyDBClusterParameterGroup.md "../../../goto/SdkForJavaV2/docdb-2014-10-31/ModifyDBClusterParameterGroup.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/ModifyDBClusterParameterGroup.md "../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/ModifyDBClusterParameterGroup.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/docdb-2014-10-31/ModifyDBClusterParameterGroup.md "../../../goto/SdkForKotlin/docdb-2014-10-31/ModifyDBClusterParameterGroup.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/docdb-2014-10-31/ModifyDBClusterParameterGroup.md "../../../goto/SdkForPHPV3/docdb-2014-10-31/ModifyDBClusterParameterGroup.md")
- [AWS SDK for Python](../../../goto/boto3/docdb-2014-10-31/ModifyDBClusterParameterGroup.md "../../../goto/boto3/docdb-2014-10-31/ModifyDBClusterParameterGroup.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/docdb-2014-10-31/ModifyDBClusterParameterGroup.md "../../../goto/SdkForRubyV3/docdb-2014-10-31/ModifyDBClusterParameterGroup.md")
