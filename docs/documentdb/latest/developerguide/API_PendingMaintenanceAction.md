# PendingMaintenanceAction

Provides information about a pending maintenance action for a resource.

## Contents

###### Note

In the following list, the required parameters are described first.

**Action**

The type of pending maintenance action that is available for the resource.

Type: String

Required: No

**AutoAppliedAfterDate**

The date of the maintenance window when the action is applied. The maintenance action
is applied to the resource during its first maintenance window after this date. If this
date is specified, any `next-maintenance` opt-in requests are ignored.

Type: Timestamp

Required: No

**CurrentApplyDate**

The effective date when the pending maintenance action is applied to the
resource.

Type: Timestamp

Required: No

**Description**

A description providing more detail about the maintenance action.

Type: String

Required: No

**ForcedApplyDate**

The date when the maintenance action is automatically applied. The maintenance action
is applied to the resource on this date regardless of the maintenance window for the
resource. If this date is specified, any `immediate` opt-in requests are
ignored.

Type: Timestamp

Required: No

**OptInStatus**

Indicates the type of opt-in request that has been received for the resource.

Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/docdb-2014-10-31/PendingMaintenanceAction.md "../../../goto/SdkForCpp/docdb-2014-10-31/PendingMaintenanceAction.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/docdb-2014-10-31/PendingMaintenanceAction.md "../../../goto/SdkForJavaV2/docdb-2014-10-31/PendingMaintenanceAction.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/docdb-2014-10-31/PendingMaintenanceAction.md "../../../goto/SdkForRubyV3/docdb-2014-10-31/PendingMaintenanceAction.md")
