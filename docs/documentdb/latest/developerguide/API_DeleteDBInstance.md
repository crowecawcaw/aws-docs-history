# DeleteDBInstance

Deletes a previously provisioned instance.

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

**DBInstanceIdentifier**

The instance identifier for the instance to be deleted. This parameter isn't
case sensitive.

Constraints:

- Must match the name of an existing instance.

Type: String

Required: Yes

## Response Elements

The following element is returned by the service.

**DBInstance**

Detailed information about an instance.

Type: [DBInstance](API_DBInstance.md "API_DBInstance.md") object

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**DBInstanceNotFound**

`DBInstanceIdentifier` doesn't refer to an existing instance.

HTTP Status Code: 404

**DBSnapshotAlreadyExists**

`DBSnapshotIdentifier` is already being used by an existing snapshot.

HTTP Status Code: 400

**InvalidDBClusterStateFault**

The cluster isn't in a valid state.

HTTP Status Code: 400

**InvalidDBInstanceState**

The specified instance isn't in the _available_ state.

HTTP Status Code: 400

**SnapshotQuotaExceeded**

The request would cause you to exceed the allowed number of snapshots.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/docdb-2014-10-31/DeleteDBInstance.md "../../../goto/cli2/docdb-2014-10-31/DeleteDBInstance.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/docdb-2014-10-31/DeleteDBInstance.md "../../../goto/DotNetSDKV4/docdb-2014-10-31/DeleteDBInstance.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/docdb-2014-10-31/DeleteDBInstance.md "../../../goto/SdkForCpp/docdb-2014-10-31/DeleteDBInstance.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/docdb-2014-10-31/DeleteDBInstance.md "../../../goto/SdkForGoV2/docdb-2014-10-31/DeleteDBInstance.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/docdb-2014-10-31/DeleteDBInstance.md "../../../goto/SdkForJavaV2/docdb-2014-10-31/DeleteDBInstance.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/DeleteDBInstance.md "../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/DeleteDBInstance.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/docdb-2014-10-31/DeleteDBInstance.md "../../../goto/SdkForKotlin/docdb-2014-10-31/DeleteDBInstance.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/docdb-2014-10-31/DeleteDBInstance.md "../../../goto/SdkForPHPV3/docdb-2014-10-31/DeleteDBInstance.md")
- [AWS SDK for Python](../../../goto/boto3/docdb-2014-10-31/DeleteDBInstance.md "../../../goto/boto3/docdb-2014-10-31/DeleteDBInstance.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/docdb-2014-10-31/DeleteDBInstance.md "../../../goto/SdkForRubyV3/docdb-2014-10-31/DeleteDBInstance.md")
