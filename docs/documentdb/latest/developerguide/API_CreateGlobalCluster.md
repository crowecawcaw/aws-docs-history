# CreateGlobalCluster

Creates an Amazon DocumentDB global cluster that can span multiple multiple AWS Regions.
The global cluster contains one primary cluster with read-write capability, and up-to 10 read-only secondary clusters. Global clusters uses storage-based fast replication across regions with latencies less than one second, using dedicated infrastructure with no impact to your workload’s performance.

You can create a global cluster that is initially empty, and then add a primary and a secondary to it.
Or you can specify an existing cluster during the create operation, and this cluster becomes the primary of the global cluster.

###### Note

This action only applies to Amazon DocumentDB clusters.

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

**GlobalClusterIdentifier**

The cluster identifier of the new global cluster.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

Pattern: `[A-Za-z][0-9A-Za-z-:._]*`

Required: Yes

**DatabaseName**

The name for your database of up to 64 alpha-numeric characters. If you do not provide a name, Amazon DocumentDB will not create a database in the global cluster you are creating.

Type: String

Required: No

**DeletionProtection**

The deletion protection setting for the new global cluster. The global cluster can't be deleted when deletion protection is enabled.

Type: Boolean

Required: No

**Engine**

The name of the database engine to be used for this cluster.

Type: String

Required: No

**EngineVersion**

The engine version of the global cluster.

Type: String

Required: No

**SourceDBClusterIdentifier**

The Amazon Resource Name (ARN) to use as the primary cluster of the global cluster. This parameter is optional.

Type: String

Required: No

**StorageEncrypted**

The storage encryption setting for the new global cluster.

Type: Boolean

Required: No

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

**GlobalClusterAlreadyExistsFault**

The `GlobalClusterIdentifier` already exists. Choose a new global cluster identifier (unique name) to create a new global cluster.

HTTP Status Code: 400

**GlobalClusterQuotaExceededFault**

The number of global clusters for this account is already at the maximum allowed.

HTTP Status Code: 400

**InvalidDBClusterStateFault**

The cluster isn't in a valid state.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/docdb-2014-10-31/CreateGlobalCluster.md "../../../goto/cli2/docdb-2014-10-31/CreateGlobalCluster.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/docdb-2014-10-31/CreateGlobalCluster.md "../../../goto/DotNetSDKV3/docdb-2014-10-31/CreateGlobalCluster.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/docdb-2014-10-31/CreateGlobalCluster.md "../../../goto/SdkForCpp/docdb-2014-10-31/CreateGlobalCluster.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/docdb-2014-10-31/CreateGlobalCluster.md "../../../goto/SdkForGoV2/docdb-2014-10-31/CreateGlobalCluster.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/docdb-2014-10-31/CreateGlobalCluster.md "../../../goto/SdkForJavaV2/docdb-2014-10-31/CreateGlobalCluster.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/CreateGlobalCluster.md "../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/CreateGlobalCluster.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/docdb-2014-10-31/CreateGlobalCluster.md "../../../goto/SdkForKotlin/docdb-2014-10-31/CreateGlobalCluster.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/docdb-2014-10-31/CreateGlobalCluster.md "../../../goto/SdkForPHPV3/docdb-2014-10-31/CreateGlobalCluster.md")
- [AWS SDK for Python](../../../goto/boto3/docdb-2014-10-31/CreateGlobalCluster.md "../../../goto/boto3/docdb-2014-10-31/CreateGlobalCluster.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/docdb-2014-10-31/CreateGlobalCluster.md "../../../goto/SdkForRubyV3/docdb-2014-10-31/CreateGlobalCluster.md")
