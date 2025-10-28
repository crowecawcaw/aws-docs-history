Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# TimeSeriesReplacementsDataSource

A replacement dataset is a modified version of the baseline related time series that contains only the values
that you want to include in a what-if forecast. The replacement dataset must contain the forecast dimensions and
item identifiers in the baseline related time series as well as at least 1 changed time series. This dataset is
merged with the baseline related time series to create a transformed dataset that is used for the what-if
forecast.

## Contents

**S3Config**

The path to the file(s) in an Amazon Simple Storage Service (Amazon S3) bucket, and an AWS Identity and Access Management (IAM) role that
Amazon Forecast can assume to access the file(s). Optionally, includes an AWS Key Management Service (KMS) key. This
object is part of the [DataSource](API_DataSource.md "API_DataSource.md") object that is submitted in the [CreateDatasetImportJob](API_CreateDatasetImportJob.md "API_CreateDatasetImportJob.md") request, and part of the [DataDestination](API_DataDestination.md "API_DataDestination.md") object.

Type: [S3Config](API_S3Config.md "API_S3Config.md") object

Required: Yes

**Schema**

Defines the fields of a dataset.

Type: [Schema](API_Schema.md "API_Schema.md") object

Required: Yes

**Format**

The format of the replacement data, which must be CSV.

Type: String

Length Constraints: Maximum length of 7.

Pattern: `^CSV|PARQUET$`

Required: No

**TimestampFormat**

The timestamp format of the replacement data.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `^[a-zA-Z0-9\-\:\.\,\'\s]+$`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/TimeSeriesReplacementsDataSource.md "../../../goto/SdkForCpp/forecast-2018-06-26/TimeSeriesReplacementsDataSource.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/TimeSeriesReplacementsDataSource.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/TimeSeriesReplacementsDataSource.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/TimeSeriesReplacementsDataSource.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/TimeSeriesReplacementsDataSource.md")
