Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# DescribeDatasetImportJob

Describes a dataset import job created using the [CreateDatasetImportJob](API_CreateDatasetImportJob.md "API_CreateDatasetImportJob.md")
operation.

###### Important

Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

In addition to listing the parameters provided in the `CreateDatasetImportJob`
request, this operation includes the following properties:

- `CreationTime`
- `LastModificationTime`
- `DataSize`
- `FieldStatistics`
- `Status`
- `Message` - If an error occurred, information about the error.

## Request Syntax

```
{
   "DatasetImportJobArn": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[DatasetImportJobArn](#API_DescribeDatasetImportJob_RequestSyntax "#API_DescribeDatasetImportJob_RequestSyntax")**

The Amazon Resource Name (ARN) of the dataset import job.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

Required: Yes

## Response Syntax

```
{
   "CreationTime": ***number***,
   "DatasetArn": "***string***",
   "DatasetImportJobArn": "***string***",
   "DatasetImportJobName": "***string***",
   "DataSize": ***number***,
   "DataSource": {
      "S3Config": {
         "KMSKeyArn": "***string***",
         "Path": "***string***",
         "RoleArn": "***string***"
      }
   },
   "EstimatedTimeRemainingInMinutes": ***number***,
   "FieldStatistics": {
      "***string***" : {
         "Avg": ***number***,
         "Count": ***number***,
         "CountDistinct": ***number***,
         "CountDistinctLong": ***number***,
         "CountLong": ***number***,
         "CountNan": ***number***,
         "CountNanLong": ***number***,
         "CountNull": ***number***,
         "CountNullLong": ***number***,
         "Max": "***string***",
         "Min": "***string***",
         "Stddev": ***number***
      }
   },
   "Format": "***string***",
   "GeolocationFormat": "***string***",
   "ImportMode": "***string***",
   "LastModificationTime": ***number***,
   "Message": "***string***",
   "Status": "***string***",
   "TimestampFormat": "***string***",
   "TimeZone": "***string***",
   "UseGeolocationForTimeZone": ***boolean***
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[CreationTime](#API_DescribeDatasetImportJob_ResponseSyntax "#API_DescribeDatasetImportJob_ResponseSyntax")**

When the dataset import job was created.

Type: Timestamp

**[DatasetArn](#API_DescribeDatasetImportJob_ResponseSyntax "#API_DescribeDatasetImportJob_ResponseSyntax")**

The Amazon Resource Name (ARN) of the dataset that the training data was imported
to.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

**[DatasetImportJobArn](#API_DescribeDatasetImportJob_ResponseSyntax "#API_DescribeDatasetImportJob_ResponseSyntax")**

The ARN of the dataset import job.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

**[DatasetImportJobName](#API_DescribeDatasetImportJob_ResponseSyntax "#API_DescribeDatasetImportJob_ResponseSyntax")**

The name of the dataset import job.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z][a-zA-Z0-9_]*`

**[DataSize](#API_DescribeDatasetImportJob_ResponseSyntax "#API_DescribeDatasetImportJob_ResponseSyntax")**

The size of the dataset in gigabytes (GB) after the import job has finished.

Type: Double

**[DataSource](#API_DescribeDatasetImportJob_ResponseSyntax "#API_DescribeDatasetImportJob_ResponseSyntax")**

The location of the training data to import and an AWS Identity and Access Management (IAM) role that Amazon Forecast
can assume to access the data.

If encryption is used, `DataSource` includes an AWS Key Management Service (KMS) key.

Type: [DataSource](API_DataSource.md "API_DataSource.md") object

**[EstimatedTimeRemainingInMinutes](#API_DescribeDatasetImportJob_ResponseSyntax "#API_DescribeDatasetImportJob_ResponseSyntax")**

The estimated time remaining in minutes for the dataset import job to complete.

Type: Long

**[FieldStatistics](#API_DescribeDatasetImportJob_ResponseSyntax "#API_DescribeDatasetImportJob_ResponseSyntax")**

Statistical information about each field in the input data.

Type: String to [Statistics](API_Statistics.md "API_Statistics.md") object map

Key Length Constraints: Maximum length of 256.

Key Pattern: `^[a-zA-Z0-9\_]+$`

**[Format](#API_DescribeDatasetImportJob_ResponseSyntax "#API_DescribeDatasetImportJob_ResponseSyntax")**

The format of the imported data, CSV or PARQUET.

Type: String

Length Constraints: Maximum length of 7.

Pattern: `^CSV|PARQUET$`

**[GeolocationFormat](#API_DescribeDatasetImportJob_ResponseSyntax "#API_DescribeDatasetImportJob_ResponseSyntax")**

The format of the geolocation attribute. Valid Values:`"LAT_LONG"` and
`"CC_POSTALCODE"`.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `^[a-zA-Z0-9_]+$`

**[ImportMode](#API_DescribeDatasetImportJob_ResponseSyntax "#API_DescribeDatasetImportJob_ResponseSyntax")**

The import mode of the dataset import job, FULL or INCREMENTAL.

Type: String

Valid Values: `FULL | INCREMENTAL`

**[LastModificationTime](#API_DescribeDatasetImportJob_ResponseSyntax "#API_DescribeDatasetImportJob_ResponseSyntax")**

The last time the resource was modified. The timestamp depends on the status of the
job:

- `CREATE_PENDING` - The `CreationTime`.
- `CREATE_IN_PROGRESS` - The current timestamp.
- `CREATE_STOPPING` - The current timestamp.
- `CREATE_STOPPED` - When the job stopped.
- `ACTIVE` or `CREATE_FAILED` - When the job finished or
  failed.

Type: Timestamp

**[Message](#API_DescribeDatasetImportJob_ResponseSyntax "#API_DescribeDatasetImportJob_ResponseSyntax")**

If an error occurred, an informational message about the error.

Type: String

**[Status](#API_DescribeDatasetImportJob_ResponseSyntax "#API_DescribeDatasetImportJob_ResponseSyntax")**

The status of the dataset import job. States include:

- `ACTIVE`
- `CREATE_PENDING`, `CREATE_IN_PROGRESS`,
  `CREATE_FAILED`
- `DELETE_PENDING`, `DELETE_IN_PROGRESS`,
  `DELETE_FAILED`
- `CREATE_STOPPING`, `CREATE_STOPPED`

Type: String

Length Constraints: Maximum length of 256.

**[TimestampFormat](#API_DescribeDatasetImportJob_ResponseSyntax "#API_DescribeDatasetImportJob_ResponseSyntax")**

The format of timestamps in the dataset. The format that you specify depends on the
`DataFrequency` specified when the dataset was created. The following formats are
supported

- "yyyy-MM-dd"

For the following data frequencies: Y, M, W, and D

- "yyyy-MM-dd HH:mm:ss"

For the following data frequencies: H, 30min, 15min, and 1min; and optionally, for: Y,
M, W, and D

Type: String

Length Constraints: Maximum length of 256.

Pattern: `^[a-zA-Z0-9\-\:\.\,\'\s]+$`

**[TimeZone](#API_DescribeDatasetImportJob_ResponseSyntax "#API_DescribeDatasetImportJob_ResponseSyntax")**

The single time zone applied to every item in the dataset

Type: String

Length Constraints: Maximum length of 256.

Pattern: `^[a-zA-Z0-9\/\+\-\_]+$`

**[UseGeolocationForTimeZone](#API_DescribeDatasetImportJob_ResponseSyntax "#API_DescribeDatasetImportJob_ResponseSyntax")**

Whether `TimeZone` is automatically derived from the geolocation
attribute.

Type: Boolean

## Errors

**InvalidInputException**

We can't process the request because it includes an invalid value or a value that exceeds
the valid range.

HTTP Status Code: 400

**ResourceNotFoundException**

We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try
again.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/forecast-2018-06-26/DescribeDatasetImportJob.md "../../../goto/cli2/forecast-2018-06-26/DescribeDatasetImportJob.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/forecast-2018-06-26/DescribeDatasetImportJob.md "../../../goto/DotNetSDKV3/forecast-2018-06-26/DescribeDatasetImportJob.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/DescribeDatasetImportJob.md "../../../goto/SdkForCpp/forecast-2018-06-26/DescribeDatasetImportJob.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/forecast-2018-06-26/DescribeDatasetImportJob.md "../../../goto/SdkForGoV2/forecast-2018-06-26/DescribeDatasetImportJob.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/DescribeDatasetImportJob.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/DescribeDatasetImportJob.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/forecast-2018-06-26/DescribeDatasetImportJob.md "../../../goto/SdkForJavaScriptV3/forecast-2018-06-26/DescribeDatasetImportJob.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/forecast-2018-06-26/DescribeDatasetImportJob.md "../../../goto/SdkForKotlin/forecast-2018-06-26/DescribeDatasetImportJob.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/forecast-2018-06-26/DescribeDatasetImportJob.md "../../../goto/SdkForPHPV3/forecast-2018-06-26/DescribeDatasetImportJob.md")
- [AWS SDK for Python](../../../goto/boto3/forecast-2018-06-26/DescribeDatasetImportJob.md "../../../goto/boto3/forecast-2018-06-26/DescribeDatasetImportJob.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/DescribeDatasetImportJob.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/DescribeDatasetImportJob.md")
