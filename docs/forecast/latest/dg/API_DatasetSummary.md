Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# DatasetSummary

Provides a summary of the dataset properties used in the [ListDatasets](API_ListDatasets.md "API_ListDatasets.md") operation. To get the
complete set of properties, call the [DescribeDataset](API_DescribeDataset.md "API_DescribeDataset.md") operation, and
provide the `DatasetArn`.

###### Important

Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

## Contents

**CreationTime**

When the dataset was created.

Type: Timestamp

Required: No

**DatasetArn**

The Amazon Resource Name (ARN) of the dataset.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

Required: No

**DatasetName**

The name of the dataset.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z][a-zA-Z0-9_]*`

Required: No

**DatasetType**

The dataset type.

Type: String

Valid Values: `TARGET_TIME_SERIES | RELATED_TIME_SERIES | ITEM_METADATA`

Required: No

**Domain**

The domain associated with the dataset.

Type: String

Valid Values: `RETAIL | CUSTOM | INVENTORY_PLANNING | EC2_CAPACITY | WORK_FORCE | WEB_TRAFFIC | METRICS`

Required: No

**LastModificationTime**

When you create a dataset, `LastModificationTime` is the same as
`CreationTime`. While data is being imported to the dataset,
`LastModificationTime` is the current time of the `ListDatasets` call.
After a [CreateDatasetImportJob](API_CreateDatasetImportJob.md "API_CreateDatasetImportJob.md") operation has finished, `LastModificationTime` is
when the import job completed or failed.

Type: Timestamp

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/DatasetSummary.md "../../../goto/SdkForCpp/forecast-2018-06-26/DatasetSummary.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/DatasetSummary.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/DatasetSummary.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/DatasetSummary.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/DatasetSummary.md")
