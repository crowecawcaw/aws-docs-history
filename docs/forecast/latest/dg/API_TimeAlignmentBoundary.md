

 Amazon Forecast is no longer available to new customers. Existing customers of Amazon Forecast can continue to use the service as normal. [Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/)

# TimeAlignmentBoundary
<a name="API_TimeAlignmentBoundary"></a>

The time boundary Forecast uses to align and aggregate your data to match your forecast frequency. Provide the unit of time and the time boundary as a key value pair. If you don't provide a time boundary, Forecast uses a set of [Default Time Boundaries](https://docs.aws.amazon.com/forecast/latest/dg/data-aggregation.html#default-time-boundaries). 

For more information about aggregation, see [Data Aggregation for Different Forecast Frequencies](https://docs.aws.amazon.com/forecast/latest/dg/data-aggregation.html). For more information setting a custom time boundary, see [Specifying a Time Boundary](https://docs.aws.amazon.com/forecast/latest/dg/data-aggregation.html#specifying-time-boundary). 

## Contents
<a name="API_TimeAlignmentBoundary_Contents"></a>

 ** DayOfMonth **   <a name="forecast-Type-TimeAlignmentBoundary-DayOfMonth"></a>
The day of the month to use for time alignment during aggregation.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 28.  
Required: No

 ** DayOfWeek **   <a name="forecast-Type-TimeAlignmentBoundary-DayOfWeek"></a>
The day of week to use for time alignment during aggregation. The day must be in uppercase.  
Type: String  
Valid Values: `MONDAY | TUESDAY | WEDNESDAY | THURSDAY | FRIDAY | SATURDAY | SUNDAY`   
Required: No

 ** Hour **   <a name="forecast-Type-TimeAlignmentBoundary-Hour"></a>
The hour of day to use for time alignment during aggregation.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 23.  
Required: No

 ** Month **   <a name="forecast-Type-TimeAlignmentBoundary-Month"></a>
The month to use for time alignment during aggregation. The month must be in uppercase.  
Type: String  
Valid Values: `JANUARY | FEBRUARY | MARCH | APRIL | MAY | JUNE | JULY | AUGUST | SEPTEMBER | OCTOBER | NOVEMBER | DECEMBER`   
Required: No

## See Also
<a name="API_TimeAlignmentBoundary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/forecast-2018-06-26/TimeAlignmentBoundary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/forecast-2018-06-26/TimeAlignmentBoundary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/forecast-2018-06-26/TimeAlignmentBoundary) 