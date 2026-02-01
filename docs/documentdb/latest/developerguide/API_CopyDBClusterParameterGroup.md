# CopyDBClusterParameterGroup

Copies the specified cluster parameter group.

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

**SourceDBClusterParameterGroupIdentifier**

The identifier or Amazon Resource Name (ARN) for the source cluster parameter group.

Constraints:

- Must specify a valid cluster parameter group.
- If the source cluster parameter group is in the same AWS Region as the copy, specify a valid parameter group identifier; for example, `my-db-cluster-param-group`, or a valid ARN.
- If the source parameter group is in a different AWS Region than the copy, specify a valid cluster parameter group ARN; for example, `arn:aws:rds:us-east-1:123456789012:sample-cluster:sample-parameter-group`.

Type: String

Required: Yes

**TargetDBClusterParameterGroupDescription**

A description for the copied cluster parameter group.

Type: String

Required: Yes

**TargetDBClusterParameterGroupIdentifier**

The identifier for the copied cluster parameter group.

Constraints:

- Cannot be null, empty, or blank.
- Must contain from 1 to 255 letters, numbers, or hyphens.
- The first character must be a letter.
- Cannot end with a hyphen or contain two consecutive hyphens.

Example: `my-cluster-param-group1`

Type: String

Required: Yes

**Tags.Tag.N**

The tags that are to be assigned to the parameter group.

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

**DBParameterGroupNotFound**

`DBParameterGroupName` doesn't refer to an existing parameter group.

HTTP Status Code: 404

**DBParameterGroupQuotaExceeded**

This request would cause you to exceed the allowed number of parameter groups.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/docdb-2014-10-31/CopyDBClusterParameterGroup.md "../../../goto/cli2/docdb-2014-10-31/CopyDBClusterParameterGroup.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/docdb-2014-10-31/CopyDBClusterParameterGroup.md "../../../goto/DotNetSDKV4/docdb-2014-10-31/CopyDBClusterParameterGroup.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/docdb-2014-10-31/CopyDBClusterParameterGroup.md "../../../goto/SdkForCpp/docdb-2014-10-31/CopyDBClusterParameterGroup.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/docdb-2014-10-31/CopyDBClusterParameterGroup.md "../../../goto/SdkForGoV2/docdb-2014-10-31/CopyDBClusterParameterGroup.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/docdb-2014-10-31/CopyDBClusterParameterGroup.md "../../../goto/SdkForJavaV2/docdb-2014-10-31/CopyDBClusterParameterGroup.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/CopyDBClusterParameterGroup.md "../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/CopyDBClusterParameterGroup.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/docdb-2014-10-31/CopyDBClusterParameterGroup.md "../../../goto/SdkForKotlin/docdb-2014-10-31/CopyDBClusterParameterGroup.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/docdb-2014-10-31/CopyDBClusterParameterGroup.md "../../../goto/SdkForPHPV3/docdb-2014-10-31/CopyDBClusterParameterGroup.md")
- [AWS SDK for Python](../../../goto/boto3/docdb-2014-10-31/CopyDBClusterParameterGroup.md "../../../goto/boto3/docdb-2014-10-31/CopyDBClusterParameterGroup.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/docdb-2014-10-31/CopyDBClusterParameterGroup.md "../../../goto/SdkForRubyV3/docdb-2014-10-31/CopyDBClusterParameterGroup.md")
