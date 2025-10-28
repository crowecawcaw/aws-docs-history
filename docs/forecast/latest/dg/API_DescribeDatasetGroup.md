Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# DescribeDatasetGroup

Describes a dataset group created using the [CreateDatasetGroup](API_CreateDatasetGroup.md "API_CreateDatasetGroup.md")
operation.

###### Important

Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

In addition to listing the parameters provided in the `CreateDatasetGroup`
request, this operation includes the following properties:

- `DatasetArns` - The datasets belonging to the group.
- `CreationTime`
- `LastModificationTime`
- `Status`

## Request Syntax

```
{
   "DatasetGroupArn": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[DatasetGroupArn](#API_DescribeDatasetGroup_RequestSyntax "#API_DescribeDatasetGroup_RequestSyntax")**

The Amazon Resource Name (ARN) of the dataset group.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

Required: Yes

## Response Syntax

```
{
   "CreationTime": ***number***,
   "DatasetArns": [ "***string***" ],
   "DatasetGroupArn": "***string***",
   "DatasetGroupName": "***string***",
   "Domain": "***string***",
   "LastModificationTime": ***number***,
   "Status": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[CreationTime](#API_DescribeDatasetGroup_ResponseSyntax "#API_DescribeDatasetGroup_ResponseSyntax")**

When the dataset group was created.

Type: Timestamp

**[DatasetArns](#API_DescribeDatasetGroup_ResponseSyntax "#API_DescribeDatasetGroup_ResponseSyntax")**

An array of Amazon Resource Names (ARNs) of the datasets contained in the dataset
group.

Type: Array of strings

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

**[DatasetGroupArn](#API_DescribeDatasetGroup_ResponseSyntax "#API_DescribeDatasetGroup_ResponseSyntax")**

The ARN of the dataset group.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

**[DatasetGroupName](#API_DescribeDatasetGroup_ResponseSyntax "#API_DescribeDatasetGroup_ResponseSyntax")**

The name of the dataset group.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z][a-zA-Z0-9_]*`

**[Domain](#API_DescribeDatasetGroup_ResponseSyntax "#API_DescribeDatasetGroup_ResponseSyntax")**

The domain associated with the dataset group.

Type: String

Valid Values: `RETAIL | CUSTOM | INVENTORY_PLANNING | EC2_CAPACITY | WORK_FORCE | WEB_TRAFFIC | METRICS`

**[LastModificationTime](#API_DescribeDatasetGroup_ResponseSyntax "#API_DescribeDatasetGroup_ResponseSyntax")**

When the dataset group was created or last updated from a call to the [UpdateDatasetGroup](API_UpdateDatasetGroup.md "API_UpdateDatasetGroup.md") operation. While the dataset group is being updated,
`LastModificationTime` is the current time of the
`DescribeDatasetGroup` call.

Type: Timestamp

**[Status](#API_DescribeDatasetGroup_ResponseSyntax "#API_DescribeDatasetGroup_ResponseSyntax")**

The status of the dataset group. States include:

- `ACTIVE`
- `CREATE_PENDING`, `CREATE_IN_PROGRESS`,
  `CREATE_FAILED`
- `DELETE_PENDING`, `DELETE_IN_PROGRESS`,
  `DELETE_FAILED`
- `UPDATE_PENDING`, `UPDATE_IN_PROGRESS`,
  `UPDATE_FAILED`

The `UPDATE` states apply when you call the [UpdateDatasetGroup](API_UpdateDatasetGroup.md "API_UpdateDatasetGroup.md")
operation.

###### Note

The `Status` of the dataset group must be `ACTIVE` before you can
use the dataset group to create a predictor.

Type: String

Length Constraints: Maximum length of 256.

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

- [AWS Command Line Interface V2](../../../goto/cli2/forecast-2018-06-26/DescribeDatasetGroup.md "../../../goto/cli2/forecast-2018-06-26/DescribeDatasetGroup.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/forecast-2018-06-26/DescribeDatasetGroup.md "../../../goto/DotNetSDKV3/forecast-2018-06-26/DescribeDatasetGroup.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/DescribeDatasetGroup.md "../../../goto/SdkForCpp/forecast-2018-06-26/DescribeDatasetGroup.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/forecast-2018-06-26/DescribeDatasetGroup.md "../../../goto/SdkForGoV2/forecast-2018-06-26/DescribeDatasetGroup.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/DescribeDatasetGroup.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/DescribeDatasetGroup.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/forecast-2018-06-26/DescribeDatasetGroup.md "../../../goto/SdkForJavaScriptV3/forecast-2018-06-26/DescribeDatasetGroup.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/forecast-2018-06-26/DescribeDatasetGroup.md "../../../goto/SdkForKotlin/forecast-2018-06-26/DescribeDatasetGroup.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/forecast-2018-06-26/DescribeDatasetGroup.md "../../../goto/SdkForPHPV3/forecast-2018-06-26/DescribeDatasetGroup.md")
- [AWS SDK for Python](../../../goto/boto3/forecast-2018-06-26/DescribeDatasetGroup.md "../../../goto/boto3/forecast-2018-06-26/DescribeDatasetGroup.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/DescribeDatasetGroup.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/DescribeDatasetGroup.md")
