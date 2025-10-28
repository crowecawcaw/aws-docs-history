# ApplyPendingMaintenanceAction

Applies a pending maintenance action to a resource (for example,
to an Amazon DocumentDB instance).

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

**ApplyAction**

The pending maintenance action to apply to this resource.

Valid values: `system-update`, `db-upgrade`

Type: String

Required: Yes

**OptInType**

A value that specifies the type of opt-in request or undoes an
opt-in request. An opt-in request of type `immediate`
can't be undone.

Valid values:

- `immediate` - Apply the maintenance action
  immediately.
- `next-maintenance` - Apply the maintenance
  action during the next maintenance window for the resource.
- `undo-opt-in` - Cancel any existing
  `next-maintenance` opt-in requests.

Type: String

Required: Yes

**ResourceIdentifier**

The Amazon Resource Name (ARN) of the resource that the pending
maintenance action applies to.

Type: String

Required: Yes

## Response Elements

The following element is returned by the service.

**ResourcePendingMaintenanceActions**

Represents the output of [ApplyPendingMaintenanceAction](API_ApplyPendingMaintenanceAction.md "API_ApplyPendingMaintenanceAction.md").

Type: [ResourcePendingMaintenanceActions](API_ResourcePendingMaintenanceActions.md "API_ResourcePendingMaintenanceActions.md") object

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**InvalidDBClusterStateFault**

The cluster isn't in a valid state.

HTTP Status Code: 400

**InvalidDBInstanceState**

The specified instance isn't in the _available_ state.

HTTP Status Code: 400

**ResourceNotFoundFault**

The specified resource ID was not found.

HTTP Status Code: 404

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/docdb-2014-10-31/ApplyPendingMaintenanceAction.md "../../../goto/cli2/docdb-2014-10-31/ApplyPendingMaintenanceAction.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/docdb-2014-10-31/ApplyPendingMaintenanceAction.md "../../../goto/DotNetSDKV3/docdb-2014-10-31/ApplyPendingMaintenanceAction.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/docdb-2014-10-31/ApplyPendingMaintenanceAction.md "../../../goto/SdkForCpp/docdb-2014-10-31/ApplyPendingMaintenanceAction.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/docdb-2014-10-31/ApplyPendingMaintenanceAction.md "../../../goto/SdkForGoV2/docdb-2014-10-31/ApplyPendingMaintenanceAction.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/docdb-2014-10-31/ApplyPendingMaintenanceAction.md "../../../goto/SdkForJavaV2/docdb-2014-10-31/ApplyPendingMaintenanceAction.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/ApplyPendingMaintenanceAction.md "../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/ApplyPendingMaintenanceAction.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/docdb-2014-10-31/ApplyPendingMaintenanceAction.md "../../../goto/SdkForKotlin/docdb-2014-10-31/ApplyPendingMaintenanceAction.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/docdb-2014-10-31/ApplyPendingMaintenanceAction.md "../../../goto/SdkForPHPV3/docdb-2014-10-31/ApplyPendingMaintenanceAction.md")
- [AWS SDK for Python](../../../goto/boto3/docdb-2014-10-31/ApplyPendingMaintenanceAction.md "../../../goto/boto3/docdb-2014-10-31/ApplyPendingMaintenanceAction.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/docdb-2014-10-31/ApplyPendingMaintenanceAction.md "../../../goto/SdkForRubyV3/docdb-2014-10-31/ApplyPendingMaintenanceAction.md")
