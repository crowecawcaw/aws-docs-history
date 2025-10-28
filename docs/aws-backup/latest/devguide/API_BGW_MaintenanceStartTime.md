# MaintenanceStartTime

This is your gateway's weekly maintenance start time including the day and time of the week.
Note that values are in terms of the gateway's time zone. Can be weekly or monthly.

## Contents

**HourOfDay**

The hour component of the maintenance start time represented as _hh_,
where _hh_ is the hour (0 to 23). The hour of the day is in the time zone of the gateway.

Type: Integer

Valid Range: Minimum value of 0. Maximum value of 23.

Required: Yes

**MinuteOfHour**

The minute component of the maintenance start time represented as _mm_, where
_mm_ is the minute (0 to 59). The minute of the hour is in the time zone of the gateway.

Type: Integer

Valid Range: Minimum value of 0. Maximum value of 59.

Required: Yes

**DayOfMonth**

The day of the month component of the maintenance start time represented as an ordinal number from
1 to 28, where 1 represents the first day of the month and 28 represents the last day of the month.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 31.

Required: No

**DayOfWeek**

An ordinal number between 0 and 6 that represents the day of the week, where 0 represents Sunday
and 6 represents Saturday. The day of week is in the time zone of the gateway.

Type: Integer

Valid Range: Minimum value of 0. Maximum value of 6.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/backup-gateway-2021-01-01/MaintenanceStartTime.md "../../../goto/SdkForCpp/backup-gateway-2021-01-01/MaintenanceStartTime.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-gateway-2021-01-01/MaintenanceStartTime.md "../../../goto/SdkForJavaV2/backup-gateway-2021-01-01/MaintenanceStartTime.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-gateway-2021-01-01/MaintenanceStartTime.md "../../../goto/SdkForRubyV3/backup-gateway-2021-01-01/MaintenanceStartTime.md")
