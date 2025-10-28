# HybridUpdateInfoEntry

Contains detailed information about a specific update activity for a hybrid directory
component.

## Contents

**AssessmentId**

The identifier of the assessment performed to validate this update
configuration.

Type: String

Pattern: `^da-[0-9a-f]{18}$`

Required: No

**InitiatedBy**

Specifies if the update was initiated by the customer or AWS.

Type: String

Required: No

**LastUpdatedDateTime**

The date and time when the update activity status was last updated.

Type: Timestamp

Required: No

**NewValue**

The new configuration values being applied in this update.

Type: [HybridUpdateValue](API_HybridUpdateValue.md "API_HybridUpdateValue.md") object

Required: No

**PreviousValue**

The previous configuration values before this update was applied.

Type: [HybridUpdateValue](API_HybridUpdateValue.md "API_HybridUpdateValue.md") object

Required: No

**StartTime**

The date and time when the update activity was initiated.

Type: Timestamp

Required: No

**Status**

The current status of the update activity. Valid values include `UPDATED`,
`UPDATING`, and `UPDATE_FAILED`.

Type: String

Valid Values: `Updated | Updating | UpdateFailed`

Required: No

**StatusReason**

A human-readable description of the update status, including any error details or
progress information.

Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/HybridUpdateInfoEntry.md "../../../goto/SdkForCpp/ds-2015-04-16/HybridUpdateInfoEntry.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/HybridUpdateInfoEntry.md "../../../goto/SdkForJavaV2/ds-2015-04-16/HybridUpdateInfoEntry.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/HybridUpdateInfoEntry.md "../../../goto/SdkForRubyV3/ds-2015-04-16/HybridUpdateInfoEntry.md")
