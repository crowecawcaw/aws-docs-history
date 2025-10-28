# SettingEntry

Contains information about the specified configurable setting for a directory.

## Contents

**AllowedValues**

The valid range of values for the directory setting. These values depend on the
`DataType` of your directory.

Type: String

Required: No

**AppliedValue**

The value of the directory setting that is applied to the directory.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

Pattern: `^[a-zA-Z0-9_]*$`

Required: No

**DataType**

The data type of a directory setting. This is used to define the
`AllowedValues` of a setting. For example a data type can be
`Boolean`, `DurationInSeconds`, or `Enum`.

Type: String

Required: No

**LastRequestedDateTime**

The date and time when the request to update a directory setting was last
submitted.

Type: Timestamp

Required: No

**LastUpdatedDateTime**

The date and time when the directory setting was last updated.

Type: Timestamp

Required: No

**Name**

The name of the directory setting. For example:

`TLS_1_0`

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

Pattern: `^[a-zA-Z0-9-/. _]*$`

Required: No

**RequestDetailedStatus**

Details about the status of the request to update the directory setting. If the directory
setting is deployed in more than one region, status is returned for the request in each region
where the setting is deployed.

Type: String to string map

Key Length Constraints: Minimum length of 8. Maximum length of 32.

Valid Values: `Requested | Updating | Updated | Failed | Default`

Required: No

**RequestedValue**

The value that was last requested for the directory setting.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

Pattern: `^[a-zA-Z0-9_]*$`

Required: No

**RequestStatus**

The overall status of the request to update the directory setting request. If the
directory setting is deployed in more than one region, and the request fails in any region,
the overall status is `Failed`.

Type: String

Valid Values: `Requested | Updating | Updated | Failed | Default`

Required: No

**RequestStatusMessage**

The last status message for the directory status request.

Type: String

Required: No

**Type**

The type, or category, of a directory setting. Similar settings have the same type. For
example, `Protocol`, `Cipher`, or `Certificate-Based
 Authentication`.

Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/SettingEntry.md "../../../goto/SdkForCpp/ds-2015-04-16/SettingEntry.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/SettingEntry.md "../../../goto/SdkForJavaV2/ds-2015-04-16/SettingEntry.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/SettingEntry.md "../../../goto/SdkForRubyV3/ds-2015-04-16/SettingEntry.md")
