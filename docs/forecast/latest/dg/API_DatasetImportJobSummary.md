Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# DatasetImportJobSummary

Provides a summary of the dataset import job properties used in the [ListDatasetImportJobs](API_ListDatasetImportJobs.md "API_ListDatasetImportJobs.md") operation. To get the complete set of properties, call the
[DescribeDatasetImportJob](API_DescribeDatasetImportJob.md "API_DescribeDatasetImportJob.md") operation, and provide the
`DatasetImportJobArn`.

###### Important

Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

## Contents

**CreationTime**

When the dataset import job was created.

Type: Timestamp

Required: No

**DatasetImportJobArn**

The Amazon Resource Name (ARN) of the dataset import job.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

Required: No

**DatasetImportJobName**

The name of the dataset import job.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z][a-zA-Z0-9_]*`

Required: No

**DataSource**

The location of the training data to import and an AWS Identity and Access Management (IAM) role that Amazon Forecast
can assume to access the data. The training data must be stored in an Amazon S3 bucket.

If encryption is used, `DataSource` includes an AWS Key Management Service (KMS) key.

Type: [DataSource](API_DataSource.md "API_DataSource.md") object

Required: No

**ImportMode**

The import mode of the dataset import job, FULL or INCREMENTAL.

Type: String

Valid Values: `FULL | INCREMENTAL`

Required: No

**LastModificationTime**

The last time the resource was modified. The timestamp depends on the status of the
job:

- `CREATE_PENDING` - The `CreationTime`.
- `CREATE_IN_PROGRESS` - The current timestamp.
- `CREATE_STOPPING` - The current timestamp.
- `CREATE_STOPPED` - When the job stopped.
- `ACTIVE` or `CREATE_FAILED` - When the job finished or
  failed.

Type: Timestamp

Required: No

**Message**

If an error occurred, an informational message about the error.

Type: String

Required: No

**Status**

The status of the dataset import job. States include:

- `ACTIVE`
- `CREATE_PENDING`, `CREATE_IN_PROGRESS`,
  `CREATE_FAILED`
- `DELETE_PENDING`, `DELETE_IN_PROGRESS`,
  `DELETE_FAILED`
- `CREATE_STOPPING`, `CREATE_STOPPED`

Type: String

Length Constraints: Maximum length of 256.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/DatasetImportJobSummary.md "../../../goto/SdkForCpp/forecast-2018-06-26/DatasetImportJobSummary.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/DatasetImportJobSummary.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/DatasetImportJobSummary.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/DatasetImportJobSummary.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/DatasetImportJobSummary.md")
