# CreateDBClusterParameterGroup

Creates a new cluster parameter group.

Parameters in a cluster parameter group apply to all of the
instances in a cluster.

A cluster parameter group is initially created with the default
parameters for the database engine used by instances in the cluster.
In Amazon DocumentDB, you cannot make modifications directly to the
`default.docdb3.6` cluster parameter group. If your
Amazon DocumentDB cluster is using the default cluster parameter group and you
want to modify a value in it, you must first [create a new parameter group](cluster_parameter_group-create.md "cluster_parameter_group-create.md")
or [copy an existing parameter group](cluster_parameter_group-copy.md "cluster_parameter_group-copy.md"),
modify it, and then apply the modified parameter group to your
cluster. For the new cluster parameter group and associated settings
to take effect, you must then reboot the instances in the cluster
without failover. For more information,
see [Modifying Amazon DocumentDB Cluster Parameter Groups](cluster_parameter_group-modify.md "cluster_parameter_group-modify.md").

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

**DBClusterParameterGroupName**

The name of the cluster parameter group.

Constraints:

- Must not match the name of an existing
  `DBClusterParameterGroup`.

###### Note

This value is stored as a lowercase string.

Type: String

Required: Yes

**DBParameterGroupFamily**

The cluster parameter group family name.

Type: String

Required: Yes

**Description**

The description for the cluster parameter group.

Type: String

Required: Yes

**Tags.Tag.N**

The tags to be assigned to the cluster parameter group.

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

Required: No

## Response Elements

The following element is returned by the service.

**DBClusterParameterGroup**

Detailed information about a cluster parameter group.

Type: [DBClusterParameterGroup](API_DBClusterParameterGroup.md "API_DBClusterParameterGroup.md") object

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**DBParameterGroupAlreadyExists**

A parameter group with the same name already exists.

HTTP Status Code: 400

**DBParameterGroupQuotaExceeded**

This request would cause you to exceed the allowed number of parameter groups.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/docdb-2014-10-31/CreateDBClusterParameterGroup.md "../../../goto/cli2/docdb-2014-10-31/CreateDBClusterParameterGroup.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/docdb-2014-10-31/CreateDBClusterParameterGroup.md "../../../goto/DotNetSDKV4/docdb-2014-10-31/CreateDBClusterParameterGroup.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/docdb-2014-10-31/CreateDBClusterParameterGroup.md "../../../goto/SdkForCpp/docdb-2014-10-31/CreateDBClusterParameterGroup.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/docdb-2014-10-31/CreateDBClusterParameterGroup.md "../../../goto/SdkForGoV2/docdb-2014-10-31/CreateDBClusterParameterGroup.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/docdb-2014-10-31/CreateDBClusterParameterGroup.md "../../../goto/SdkForJavaV2/docdb-2014-10-31/CreateDBClusterParameterGroup.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/CreateDBClusterParameterGroup.md "../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/CreateDBClusterParameterGroup.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/docdb-2014-10-31/CreateDBClusterParameterGroup.md "../../../goto/SdkForKotlin/docdb-2014-10-31/CreateDBClusterParameterGroup.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/docdb-2014-10-31/CreateDBClusterParameterGroup.md "../../../goto/SdkForPHPV3/docdb-2014-10-31/CreateDBClusterParameterGroup.md")
- [AWS SDK for Python](../../../goto/boto3/docdb-2014-10-31/CreateDBClusterParameterGroup.md "../../../goto/boto3/docdb-2014-10-31/CreateDBClusterParameterGroup.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/docdb-2014-10-31/CreateDBClusterParameterGroup.md "../../../goto/SdkForRubyV3/docdb-2014-10-31/CreateDBClusterParameterGroup.md")
