# UpdateInfoEntry

An entry of update information related to a requested update type.

## Contents

**InitiatedBy**

This specifies if the update was initiated by the customer or by the service team.

Type: String

Required: No

**LastUpdatedDateTime**

The last updated date and time of a particular directory setting.

Type: Timestamp

Required: No

**NewValue**

The new value of the target setting.

Type: [UpdateValue](API_UpdateValue.md "API_UpdateValue.md") object

Required: No

**PreviousValue**

The old value of the target setting.

Type: [UpdateValue](API_UpdateValue.md "API_UpdateValue.md") object

Required: No

**Region**

The name of the Region.

Type: String

Length Constraints: Minimum length of 8. Maximum length of 32.

Required: No

**StartTime**

The start time of the `UpdateDirectorySetup` for the particular type.

Type: Timestamp

Required: No

**Status**

The status of the update performed on the directory.

Type: String

Valid Values: `Updated | Updating | UpdateFailed`

Required: No

**StatusReason**

The reason for the current status of the update type activity.

Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/UpdateInfoEntry.md "../../../goto/SdkForCpp/ds-2015-04-16/UpdateInfoEntry.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/UpdateInfoEntry.md "../../../goto/SdkForJavaV2/ds-2015-04-16/UpdateInfoEntry.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/UpdateInfoEntry.md "../../../goto/SdkForRubyV3/ds-2015-04-16/UpdateInfoEntry.md")
