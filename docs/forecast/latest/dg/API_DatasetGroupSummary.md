Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# DatasetGroupSummary

Provides a summary of the dataset group properties used in the [ListDatasetGroups](API_ListDatasetGroups.md "API_ListDatasetGroups.md") operation. To
get the complete set of properties, call the [DescribeDatasetGroup](API_DescribeDatasetGroup.md "API_DescribeDatasetGroup.md")
operation, and provide the `DatasetGroupArn`.

###### Important

Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

## Contents

**CreationTime**

When the dataset group was created.

Type: Timestamp

Required: No

**DatasetGroupArn**

The Amazon Resource Name (ARN) of the dataset group.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

Required: No

**DatasetGroupName**

The name of the dataset group.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z][a-zA-Z0-9_]*`

Required: No

**LastModificationTime**

When the dataset group was created or last updated from a call to the [UpdateDatasetGroup](API_UpdateDatasetGroup.md "API_UpdateDatasetGroup.md") operation. While the dataset group is being updated,
`LastModificationTime` is the current time of the `ListDatasetGroups`
call.

Type: Timestamp

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/DatasetGroupSummary.md "../../../goto/SdkForCpp/forecast-2018-06-26/DatasetGroupSummary.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/DatasetGroupSummary.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/DatasetGroupSummary.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/DatasetGroupSummary.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/DatasetGroupSummary.md")
