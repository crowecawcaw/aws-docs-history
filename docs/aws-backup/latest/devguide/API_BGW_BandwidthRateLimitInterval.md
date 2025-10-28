# BandwidthRateLimitInterval

Describes a bandwidth rate limit interval for a gateway. A bandwidth
rate limit schedule consists of one or more bandwidth rate limit intervals.
A bandwidth rate limit interval defines a period of time on one or more days
of the week, during which bandwidth rate limits are specified for uploading,
downloading, or both.

## Contents

**DaysOfWeek**

The days of the week component of the bandwidth rate limit interval,
represented as ordinal numbers from 0 to 6, where 0 represents Sunday and 6 represents
Saturday.

Type: Array of integers

Array Members: Minimum number of 1 item. Maximum number of 7 items.

Valid Range: Minimum value of 0. Maximum value of 6.

Required: Yes

**EndHourOfDay**

The hour of the day to end the bandwidth rate limit interval.

Type: Integer

Valid Range: Minimum value of 0. Maximum value of 23.

Required: Yes

**EndMinuteOfHour**

The minute of the hour to end the bandwidth rate limit interval.

###### Important

The bandwidth rate limit interval ends at the end of the minute.
To end an interval at the end of an hour, use the value `59`.

Type: Integer

Valid Range: Minimum value of 0. Maximum value of 59.

Required: Yes

**StartHourOfDay**

The hour of the day to start the bandwidth rate limit interval.

Type: Integer

Valid Range: Minimum value of 0. Maximum value of 23.

Required: Yes

**StartMinuteOfHour**

The minute of the hour to start the bandwidth rate limit interval. The
interval begins at the start of that minute. To begin an interval exactly at
the start of the hour, use the value `0`.

Type: Integer

Valid Range: Minimum value of 0. Maximum value of 59.

Required: Yes

**AverageUploadRateLimitInBitsPerSec**

The average upload rate limit component of the bandwidth rate limit
interval, in bits per second. This field does not appear in the response if
the upload rate limit is not set.

Type: Long

Valid Range: Minimum value of 51200. Maximum value of 8000000000000.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/backup-gateway-2021-01-01/BandwidthRateLimitInterval.md "../../../goto/SdkForCpp/backup-gateway-2021-01-01/BandwidthRateLimitInterval.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-gateway-2021-01-01/BandwidthRateLimitInterval.md "../../../goto/SdkForJavaV2/backup-gateway-2021-01-01/BandwidthRateLimitInterval.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-gateway-2021-01-01/BandwidthRateLimitInterval.md "../../../goto/SdkForRubyV3/backup-gateway-2021-01-01/BandwidthRateLimitInterval.md")
