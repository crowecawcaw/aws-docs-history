Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# Dataset Guidelines for Forecast

Consult to the following guidelines if Amazon Forecast fails to import your dataset, or if your
dataset doesn't function as expected.

**Timestamp Format**

For Year (`Y`), Month (`M`), Week (`W`), and Day
(`D`) collection frequencies, Forecast supports the `yyyy-MM-dd`
timestamp format (for example, `2019-08-21`) and, optionally, the
`HH:mm:ss` format (for example, `2019-08-21 15:00:00`).

For Hour (`H`) and Minute (`M`) frequencies, Forecast supports only
the `yyyy-MM-dd HH:mm:ss` format (for example `2019-08-21
 15:00:00`).

Guideline: Change the timestamp format for the collection frequency of your dataset to
the supported format.

**Amazon S3 File or Bucket**

When you import a dataset, you can specify either the path to a CSV or Parquet file in your Amazon Simple Storage Service
(Amazon S3) bucket that contains your data or the name of the S3 bucket that contains your data. If you specify a
CSV or Parquet file, Forecast imports just that file. If you specify an S3 bucket, Forecast imports all of the CSV
or Parquet files in the bucket up to 10,000 files. If you import multiple files by specifying a bucket name,
all CSV or Parquet files must conform to the specified schema.

Guideline: Specify a specific file or an S3 bucket using the following syntax:

`s3://bucket-name/example-object.csv`

`s3://bucket-name/example-object.parquet`

`s3://bucket-name/prefix/`

`s3://bucket-name`

Parquet files can have the extension .parquet, .parq, .pqt, or no extension at all.

**Full Dataset Updates**

Your first dataset import is always a full import, subsequent imports can either be full or incremental updates. You must use the Forecast API to specify the import mode.

With a full update, all existing data is replaced with the newly imported data. Because full dataset import jobs are not aggregated, your most recent dataset import is the one that is used when training a predictor or generating a forecast.

Guideline: Create an incremental dataset update to append your new data to the existing data. Otherwise, ensure that your most recent dataset import contains all of the data you want to model, and not just the new data collected since the previous import.

**Incremental Dataset Updates**

Fields such as timestamp, data format, geolocation, etc. are read from the currently active dataset. You do not need to include this information with an incremental dataset import. If they are included, they must match the originally provided values.

Guideline: Perform a full dataset import to change any of these values.

**Attribute Order**

The order of attributes specified in the schema definition must match the column order in the CSV or
Parquet file that you are importing. For example, if you defined `timestamp` as the first
attribute, then `timestamp` must also be the first column in the input file.

Guideline: Verify that the columns in the input file are in the same order as the schema attributes that
you created.

**Weather Index**

In order to apply the Weather Index, you must include a [geolocation attribute](weather.md#adding-geolocation "weather.md#adding-geolocation") in your target time series and any related time series
datasets. You also need to specify [time zones](weather.md#specifying-timezones "weather.md#specifying-timezones")
for your target time series timestamps.

Guideline: Ensure that your datasets include a geolocation attribute and that your
timestamps have an assigned time zone. For more information, refer to the Weather Index [Conditions and Restrictions.](weather.md#weather-conditions-restrictions "weather.md#weather-conditions-restrictions")

**Dataset Header**

A dataset header in your input CSV may cause a validation error. We recommend omitting a header for CSV
files.

Guideline: Delete the dataset header and try the import again.

A dataset header is required for Parquet files.

**Dataset Status**

Before you can import training data with the [CreateDatasetImportJob](API_CreateDatasetImportJob.md "API_CreateDatasetImportJob.md") operation, the `Status` of the dataset
must be `ACTIVE`.

Guideline: Use the [DescribeDataset](API_DescribeDataset.md "API_DescribeDataset.md") operation to get the dataset's status. If the
creation or update of the dataset failed, check the formatting of your dataset file and
attempt to create it again.

**Default File Format**

The default file format is CSV.

**File Format and Delimiter**

Forecast supports only the comma-separated values (CSV) file format and Parquet format.
You can't separate values using tabs, spaces, colons, or any other characters.

Guideline: Convert your dataset to CSV format (using only commas as your delimiter) or
Parquet format and try importing the file again.

**File Name**

File names must contain at least one alphabetic character. Files with names that are
only numeric can't be imported.

Guideline: Rename your input data file to include at least one alphabetic character
and try importing the file again.

**Partitioned Parquet Data**

Forecast does not read partitioned Parquet files.

**What-if analysis Dataset Requirements**

What-if analyses require CSV datasets. The TimeSeriesSelector operation of the [CreateWhatIfAnalysis](API_CreateWhatIfAnalysis.md "API_CreateWhatIfAnalysis.md") action and the TimeSeriesReplacementDataSource operation of the [CreateWhatIfForecast](API_CreateWhatIfForecast.md "API_CreateWhatIfForecast.md") do not accept Parquet files.
