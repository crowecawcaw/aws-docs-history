# FailoverDBCluster

Forces a failover for a cluster.

A failover for a cluster promotes one of the Amazon DocumentDB replicas (read-only instances) in the cluster to be the primary instance (the cluster writer).

If the primary instance fails, Amazon DocumentDB automatically fails over to an Amazon DocumentDB replica, if one exists. You can force a failover when you want to simulate a failure of a primary instance for testing.

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

**DBClusterIdentifier**

A cluster identifier to force a failover for. This parameter is not case sensitive.

Constraints:

- Must match the identifier of an existing `DBCluster`.

Type: String

Required: No

**TargetDBInstanceIdentifier**

The name of the instance to promote to the primary instance.

You must specify the instance identifier for an Amazon DocumentDB replica in the cluster. For
example, `mydbcluster-replica1`.

Type: String

Required: No

## Response Elements

The following element is returned by the service.

**DBCluster**

Detailed information about a cluster.

Type: [DBCluster](API_DBCluster.md "API_DBCluster.md") object

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**DBClusterNotFoundFault**

`DBClusterIdentifier` doesn't refer to an existing cluster.

HTTP Status Code: 404

**InvalidDBClusterStateFault**

The cluster isn't in a valid state.

HTTP Status Code: 400

**InvalidDBInstanceState**

The specified instance isn't in the _available_ state.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/docdb-2014-10-31/FailoverDBCluster.md "../../../goto/cli2/docdb-2014-10-31/FailoverDBCluster.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/docdb-2014-10-31/FailoverDBCluster.md "../../../goto/DotNetSDKV3/docdb-2014-10-31/FailoverDBCluster.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/docdb-2014-10-31/FailoverDBCluster.md "../../../goto/SdkForCpp/docdb-2014-10-31/FailoverDBCluster.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/docdb-2014-10-31/FailoverDBCluster.md "../../../goto/SdkForGoV2/docdb-2014-10-31/FailoverDBCluster.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/docdb-2014-10-31/FailoverDBCluster.md "../../../goto/SdkForJavaV2/docdb-2014-10-31/FailoverDBCluster.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/FailoverDBCluster.md "../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/FailoverDBCluster.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/docdb-2014-10-31/FailoverDBCluster.md "../../../goto/SdkForKotlin/docdb-2014-10-31/FailoverDBCluster.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/docdb-2014-10-31/FailoverDBCluster.md "../../../goto/SdkForPHPV3/docdb-2014-10-31/FailoverDBCluster.md")
- [AWS SDK for Python](../../../goto/boto3/docdb-2014-10-31/FailoverDBCluster.md "../../../goto/boto3/docdb-2014-10-31/FailoverDBCluster.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/docdb-2014-10-31/FailoverDBCluster.md "../../../goto/SdkForRubyV3/docdb-2014-10-31/FailoverDBCluster.md")
