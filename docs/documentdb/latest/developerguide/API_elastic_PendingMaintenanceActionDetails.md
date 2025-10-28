# PendingMaintenanceActionDetails

Retrieves the details of maintenance actions that are pending.

## Contents

###### Note

In the following list, the required parameters are described first.

**action**

Displays the specific action of a pending maintenance action.

Type: String

Required: Yes

**autoAppliedAfterDate**

Displays the date of the maintenance window when the action is applied.
The maintenance action is applied to the resource during its first maintenance window after this date.
If this date is specified, any `NEXT_MAINTENANCE`
`optInType` requests are ignored.

Type: String

Required: No

**currentApplyDate**

Displays the effective date when the pending maintenance action is applied to the resource.

Type: String

Required: No

**description**

Displays a description providing more detail about the maintenance action.

Type: String

Required: No

**forcedApplyDate**

Displays the date when the maintenance action is automatically applied.
The maintenance action is applied to the resource on this date regardless of the maintenance window for the resource.
If this date is specified, any `IMMEDIATE`
`optInType` requests are ignored.

Type: String

Required: No

**optInStatus**

Displays the type of `optInType` request that has been received for the resource.

Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/docdb-elastic-2022-11-28/PendingMaintenanceActionDetails.md "../../../goto/SdkForCpp/docdb-elastic-2022-11-28/PendingMaintenanceActionDetails.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/docdb-elastic-2022-11-28/PendingMaintenanceActionDetails.md "../../../goto/SdkForJavaV2/docdb-elastic-2022-11-28/PendingMaintenanceActionDetails.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/docdb-elastic-2022-11-28/PendingMaintenanceActionDetails.md "../../../goto/SdkForRubyV3/docdb-elastic-2022-11-28/PendingMaintenanceActionDetails.md")
