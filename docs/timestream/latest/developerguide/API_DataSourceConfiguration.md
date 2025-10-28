For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# DataSourceConfiguration

Defines configuration details about the data source.

## Contents

**DataFormat**

This is currently CSV.

Type: String

Valid Values: `CSV`

Required: Yes

**DataSourceS3Configuration**

Configuration of an S3 location for a file which contains data to load.

Type: [DataSourceS3Configuration](API_DataSourceS3Configuration.md "API_DataSourceS3Configuration.md") object

Required: Yes

**CsvConfiguration**

A delimited data format where the column separator can be a comma and the record separator is a newline
character.

Type: [CsvConfiguration](API_CsvConfiguration.md "API_CsvConfiguration.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-write-2018-11-01/DataSourceConfiguration.md "../../../goto/SdkForCpp/timestream-write-2018-11-01/DataSourceConfiguration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-write-2018-11-01/DataSourceConfiguration.md "../../../goto/SdkForJavaV2/timestream-write-2018-11-01/DataSourceConfiguration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-write-2018-11-01/DataSourceConfiguration.md "../../../goto/SdkForRubyV3/timestream-write-2018-11-01/DataSourceConfiguration.md")
