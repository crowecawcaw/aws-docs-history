# DeleteGlobalCluster

Deletes a global cluster. The primary and secondary clusters must already be detached or deleted before attempting to delete a global cluster.

###### Note

This action only applies to Amazon DocumentDB clusters.

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

**GlobalClusterIdentifier**

The cluster identifier of the global cluster being deleted.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

Pattern: `[A-Za-z][0-9A-Za-z-:._]*`

Required: Yes

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

- [AWS Command Line Interface V2](../../../goto/cli2/docdb-2014-10-31/DeleteGlobalCluster.md "../../../goto/cli2/docdb-2014-10-31/DeleteGlobalCluster.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/docdb-2014-10-31/DeleteGlobalCluster.md "../../../goto/DotNetSDKV4/docdb-2014-10-31/DeleteGlobalCluster.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/docdb-2014-10-31/DeleteGlobalCluster.md "../../../goto/SdkForCpp/docdb-2014-10-31/DeleteGlobalCluster.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/docdb-2014-10-31/DeleteGlobalCluster.md "../../../goto/SdkForGoV2/docdb-2014-10-31/DeleteGlobalCluster.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/docdb-2014-10-31/DeleteGlobalCluster.md "../../../goto/SdkForJavaV2/docdb-2014-10-31/DeleteGlobalCluster.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/DeleteGlobalCluster.md "../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/DeleteGlobalCluster.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/docdb-2014-10-31/DeleteGlobalCluster.md "../../../goto/SdkForKotlin/docdb-2014-10-31/DeleteGlobalCluster.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/docdb-2014-10-31/DeleteGlobalCluster.md "../../../goto/SdkForPHPV3/docdb-2014-10-31/DeleteGlobalCluster.md")
- [AWS SDK for Python](../../../goto/boto3/docdb-2014-10-31/DeleteGlobalCluster.md "../../../goto/boto3/docdb-2014-10-31/DeleteGlobalCluster.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/docdb-2014-10-31/DeleteGlobalCluster.md "../../../goto/SdkForRubyV3/docdb-2014-10-31/DeleteGlobalCluster.md")
