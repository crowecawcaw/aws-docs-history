# RebootDBInstance

You might need to reboot your instance, usually for maintenance reasons. For
example, if you make certain changes, or if you change the cluster parameter group
that is associated with the instance, you must reboot the instance for the changes to
take effect.

Rebooting an instance restarts the database engine service. Rebooting an instance
results in a momentary outage, during which the instance status is set to
_rebooting_.

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

**DBInstanceIdentifier**

The instance identifier. This parameter is stored as a lowercase string.

Constraints:

- Must match the identifier of an existing `DBInstance`.

Type: String

Required: Yes

**ForceFailover**

When `true`, the reboot is conducted through a Multi-AZ failover.

Constraint: You can't specify `true` if the instance is not configured for
Multi-AZ.

Type: Boolean

Required: No

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

**InvalidDBInstanceState**

The specified instance isn't in the _available_ state.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/docdb-2014-10-31/RebootDBInstance.md "../../../goto/cli2/docdb-2014-10-31/RebootDBInstance.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/docdb-2014-10-31/RebootDBInstance.md "../../../goto/DotNetSDKV4/docdb-2014-10-31/RebootDBInstance.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/docdb-2014-10-31/RebootDBInstance.md "../../../goto/SdkForCpp/docdb-2014-10-31/RebootDBInstance.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/docdb-2014-10-31/RebootDBInstance.md "../../../goto/SdkForGoV2/docdb-2014-10-31/RebootDBInstance.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/docdb-2014-10-31/RebootDBInstance.md "../../../goto/SdkForJavaV2/docdb-2014-10-31/RebootDBInstance.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/RebootDBInstance.md "../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/RebootDBInstance.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/docdb-2014-10-31/RebootDBInstance.md "../../../goto/SdkForKotlin/docdb-2014-10-31/RebootDBInstance.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/docdb-2014-10-31/RebootDBInstance.md "../../../goto/SdkForPHPV3/docdb-2014-10-31/RebootDBInstance.md")
- [AWS SDK for Python](../../../goto/boto3/docdb-2014-10-31/RebootDBInstance.md "../../../goto/boto3/docdb-2014-10-31/RebootDBInstance.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/docdb-2014-10-31/RebootDBInstance.md "../../../goto/SdkForRubyV3/docdb-2014-10-31/RebootDBInstance.md")
