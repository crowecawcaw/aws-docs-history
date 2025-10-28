# StartDBCluster

Restarts the stopped cluster that is specified by `DBClusterIdentifier`.
For more information, see [Stopping and
Starting an Amazon DocumentDB Cluster](db-cluster-stop-start.md "db-cluster-stop-start.md").

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

**DBClusterIdentifier**

The identifier of the cluster to restart. Example:
`docdb-2019-05-28-15-24-52`

Type: String

Required: Yes

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

- [AWS Command Line Interface V2](../../../goto/cli2/docdb-2014-10-31/StartDBCluster.md "../../../goto/cli2/docdb-2014-10-31/StartDBCluster.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/docdb-2014-10-31/StartDBCluster.md "../../../goto/DotNetSDKV3/docdb-2014-10-31/StartDBCluster.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/docdb-2014-10-31/StartDBCluster.md "../../../goto/SdkForCpp/docdb-2014-10-31/StartDBCluster.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/docdb-2014-10-31/StartDBCluster.md "../../../goto/SdkForGoV2/docdb-2014-10-31/StartDBCluster.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/docdb-2014-10-31/StartDBCluster.md "../../../goto/SdkForJavaV2/docdb-2014-10-31/StartDBCluster.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/StartDBCluster.md "../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/StartDBCluster.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/docdb-2014-10-31/StartDBCluster.md "../../../goto/SdkForKotlin/docdb-2014-10-31/StartDBCluster.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/docdb-2014-10-31/StartDBCluster.md "../../../goto/SdkForPHPV3/docdb-2014-10-31/StartDBCluster.md")
- [AWS SDK for Python](../../../goto/boto3/docdb-2014-10-31/StartDBCluster.md "../../../goto/boto3/docdb-2014-10-31/StartDBCluster.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/docdb-2014-10-31/StartDBCluster.md "../../../goto/SdkForRubyV3/docdb-2014-10-31/StartDBCluster.md")
