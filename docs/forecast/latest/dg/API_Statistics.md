Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# Statistics

Provides statistics for each data field imported into to an Amazon Forecast dataset with
the [CreateDatasetImportJob](API_CreateDatasetImportJob.md "API_CreateDatasetImportJob.md") operation.

## Contents

**Avg**

For a numeric field, the average value in the field.

Type: Double

Required: No

**Count**

The number of values in the field. If the response value is -1, refer to
`CountLong`.

Type: Integer

Required: No

**CountDistinct**

The number of distinct values in the field. If the response value is -1, refer to
`CountDistinctLong`.

Type: Integer

Required: No

**CountDistinctLong**

The number of distinct values in the field. `CountDistinctLong` is used instead
of `CountDistinct` if the value is greater than 2,147,483,647.

Type: Long

Required: No

**CountLong**

The number of values in the field. `CountLong` is used instead of
`Count` if the value is greater than 2,147,483,647.

Type: Long

Required: No

**CountNan**

The number of NAN (not a number) values in the field. If the response value is -1, refer
to `CountNanLong`.

Type: Integer

Required: No

**CountNanLong**

The number of NAN (not a number) values in the field. `CountNanLong` is used
instead of `CountNan` if the value is greater than 2,147,483,647.

Type: Long

Required: No

**CountNull**

The number of null values in the field. If the response value is -1, refer to
`CountNullLong`.

Type: Integer

Required: No

**CountNullLong**

The number of null values in the field. `CountNullLong` is used instead of
`CountNull` if the value is greater than 2,147,483,647.

Type: Long

Required: No

**Max**

For a numeric field, the maximum value in the field.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `^[a-zA-Z0-9\_]+$`

Required: No

**Min**

For a numeric field, the minimum value in the field.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `^[a-zA-Z0-9\_]+$`

Required: No

**Stddev**

For a numeric field, the standard deviation.

Type: Double

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/Statistics.md "../../../goto/SdkForCpp/forecast-2018-06-26/Statistics.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/Statistics.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/Statistics.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/Statistics.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/Statistics.md")
