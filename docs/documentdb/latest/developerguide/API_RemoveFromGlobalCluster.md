# RemoveFromGlobalCluster

Detaches an Amazon DocumentDB secondary cluster from a global cluster. The cluster becomes a standalone cluster with read-write capability instead of being read-only and receiving data from a primary in a different region.

###### Note

This action only applies to Amazon DocumentDB clusters.

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

**DbClusterIdentifier**

The Amazon Resource Name (ARN) identifying the cluster that was detached from the Amazon DocumentDB global cluster.

Type: String

Required: Yes

**GlobalClusterIdentifier**

The cluster identifier to detach from the Amazon DocumentDB global cluster.

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

**DBClusterNotFoundFault**

`DBClusterIdentifier` doesn't refer to an existing cluster.

HTTP Status Code: 404

**GlobalClusterNotFoundFault**

The `GlobalClusterIdentifier` doesn't refer to an existing global cluster.

HTTP Status Code: 404

**InvalidGlobalClusterStateFault**

The requested operation can't be performed while the cluster is in this state.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/docdb-2014-10-31/RemoveFromGlobalCluster.md "../../../goto/cli2/docdb-2014-10-31/RemoveFromGlobalCluster.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/docdb-2014-10-31/RemoveFromGlobalCluster.md "../../../goto/DotNetSDKV3/docdb-2014-10-31/RemoveFromGlobalCluster.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/docdb-2014-10-31/RemoveFromGlobalCluster.md "../../../goto/SdkForCpp/docdb-2014-10-31/RemoveFromGlobalCluster.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/docdb-2014-10-31/RemoveFromGlobalCluster.md "../../../goto/SdkForGoV2/docdb-2014-10-31/RemoveFromGlobalCluster.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/docdb-2014-10-31/RemoveFromGlobalCluster.md "../../../goto/SdkForJavaV2/docdb-2014-10-31/RemoveFromGlobalCluster.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/RemoveFromGlobalCluster.md "../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/RemoveFromGlobalCluster.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/docdb-2014-10-31/RemoveFromGlobalCluster.md "../../../goto/SdkForKotlin/docdb-2014-10-31/RemoveFromGlobalCluster.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/docdb-2014-10-31/RemoveFromGlobalCluster.md "../../../goto/SdkForPHPV3/docdb-2014-10-31/RemoveFromGlobalCluster.md")
- [AWS SDK for Python](../../../goto/boto3/docdb-2014-10-31/RemoveFromGlobalCluster.md "../../../goto/boto3/docdb-2014-10-31/RemoveFromGlobalCluster.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/docdb-2014-10-31/RemoveFromGlobalCluster.md "../../../goto/SdkForRubyV3/docdb-2014-10-31/RemoveFromGlobalCluster.md")
