Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# TimeAlignmentBoundary

The time boundary Forecast uses to align and aggregate your data to match your forecast frequency. Provide the unit of time and the time boundary as a key value pair. If you
don't provide a time boundary, Forecast uses a set of [Default Time Boundaries](data-aggregation.md#default-time-boundaries "data-aggregation.md#default-time-boundaries").

For more information about aggregation,
see [Data Aggregation for Different Forecast Frequencies](data-aggregation.md "data-aggregation.md").
For more information setting a custom time boundary,
see [Specifying a Time Boundary](data-aggregation.md#specifying-time-boundary "data-aggregation.md#specifying-time-boundary").

## Contents

**DayOfMonth**

The day of the month to use for time alignment during aggregation.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 28.

Required: No

**DayOfWeek**

The day of week to use for time alignment during aggregation. The day must be in uppercase.

Type: String

Valid Values: `MONDAY | TUESDAY | WEDNESDAY | THURSDAY | FRIDAY | SATURDAY | SUNDAY`

Required: No

**Hour**

The hour of day to use for time alignment during aggregation.

Type: Integer

Valid Range: Minimum value of 0. Maximum value of 23.

Required: No

**Month**

The month to use for time alignment during aggregation. The month must be in uppercase.

Type: String

Valid Values: `JANUARY | FEBRUARY | MARCH | APRIL | MAY | JUNE | JULY | AUGUST | SEPTEMBER | OCTOBER | NOVEMBER | DECEMBER`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/TimeAlignmentBoundary.md "../../../goto/SdkForCpp/forecast-2018-06-26/TimeAlignmentBoundary.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/TimeAlignmentBoundary.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/TimeAlignmentBoundary.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/TimeAlignmentBoundary.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/TimeAlignmentBoundary.md")
