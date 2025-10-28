# ModifyGlobalCluster

Modify a setting for an Amazon DocumentDB global cluster. You can change one or more configuration parameters (for example: deletion protection), or the global cluster identifier by specifying these parameters and the new values in the request.

###### Note

This action only applies to Amazon DocumentDB clusters.

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

**GlobalClusterIdentifier**

The identifier for the global cluster being modified. This parameter isn't case-sensitive.

Constraints:

- Must match the identifier of an existing global cluster.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

Pattern: `[A-Za-z][0-9A-Za-z-:._]*`

Required: Yes

**DeletionProtection**

Indicates if the global cluster has deletion protection enabled. The global cluster can't be deleted when deletion protection is enabled.

Type: Boolean

Required: No

**NewGlobalClusterIdentifier**

The new identifier for a global cluster when you modify a global cluster. This value is stored as a lowercase string.

- Must contain from 1 to 63 letters, numbers, or hyphens

The first character must be a letter

Can't end with a hyphen or contain two consecutive hyphens

Example: `my-cluster2`

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

Pattern: `[A-Za-z][0-9A-Za-z-:._]*`

Required: No

## Response Elements

The following element is returned by the service.

**GlobalCluster**

A data type representing an Amazon DocumentDB global cluster.

Type: [GlobalCluster](API_GlobalCluster.md "API_GlobalCluster.md") object

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**GlobalClusterNotFoundFault**

The `GlobalClusterIdentifier` doesn't refer to an existing global cluster.

HTTP Status Code: 404

**InvalidGlobalClusterStateFault**

The requested operation can't be performed while the cluster is in this state.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/docdb-2014-10-31/ModifyGlobalCluster.md "../../../goto/cli2/docdb-2014-10-31/ModifyGlobalCluster.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/docdb-2014-10-31/ModifyGlobalCluster.md "../../../goto/DotNetSDKV3/docdb-2014-10-31/ModifyGlobalCluster.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/docdb-2014-10-31/ModifyGlobalCluster.md "../../../goto/SdkForCpp/docdb-2014-10-31/ModifyGlobalCluster.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/docdb-2014-10-31/ModifyGlobalCluster.md "../../../goto/SdkForGoV2/docdb-2014-10-31/ModifyGlobalCluster.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/docdb-2014-10-31/ModifyGlobalCluster.md "../../../goto/SdkForJavaV2/docdb-2014-10-31/ModifyGlobalCluster.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/ModifyGlobalCluster.md "../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/ModifyGlobalCluster.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/docdb-2014-10-31/ModifyGlobalCluster.md "../../../goto/SdkForKotlin/docdb-2014-10-31/ModifyGlobalCluster.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/docdb-2014-10-31/ModifyGlobalCluster.md "../../../goto/SdkForPHPV3/docdb-2014-10-31/ModifyGlobalCluster.md")
- [AWS SDK for Python](../../../goto/boto3/docdb-2014-10-31/ModifyGlobalCluster.md "../../../goto/boto3/docdb-2014-10-31/ModifyGlobalCluster.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/docdb-2014-10-31/ModifyGlobalCluster.md "../../../goto/SdkForRubyV3/docdb-2014-10-31/ModifyGlobalCluster.md")
