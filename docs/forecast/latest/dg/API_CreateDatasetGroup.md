Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# CreateDatasetGroup

Creates a dataset group, which holds a collection of related datasets. You can add
datasets to the dataset group when you create the dataset group, or later by using the [UpdateDatasetGroup](API_UpdateDatasetGroup.md "API_UpdateDatasetGroup.md") operation.

###### Important

Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

After creating a dataset group and adding datasets, you use the dataset group when you
create a predictor. For more information, see [Dataset groups](howitworks-datasets-groups.md "howitworks-datasets-groups.md").

To get a list of all your datasets groups, use the [ListDatasetGroups](API_ListDatasetGroups.md "API_ListDatasetGroups.md")
operation.

###### Note

The `Status` of a dataset group must be `ACTIVE` before you can
use the dataset group to create a predictor. To get the status, use the [DescribeDatasetGroup](API_DescribeDatasetGroup.md "API_DescribeDatasetGroup.md") operation.

## Request Syntax

```
{
   "DatasetArns": [ "`string`" ],
   "DatasetGroupName": "`string`",
   "Domain": "`string`",
   "Tags": [
      {
         "Key": "`string`",
         "Value": "`string`"
      }
   ]
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[DatasetArns](#API_CreateDatasetGroup_RequestSyntax "#API_CreateDatasetGroup_RequestSyntax")**

An array of Amazon Resource Names (ARNs) of the datasets that you want to include in the
dataset group.

Type: Array of strings

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

Required: No

**[DatasetGroupName](#API_CreateDatasetGroup_RequestSyntax "#API_CreateDatasetGroup_RequestSyntax")**

A name for the dataset group.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z][a-zA-Z0-9_]*`

Required: Yes

**[Domain](#API_CreateDatasetGroup_RequestSyntax "#API_CreateDatasetGroup_RequestSyntax")**

The domain associated with the dataset group. When you add a dataset to a dataset group,
this value and the value specified for the `Domain` parameter of the [CreateDataset](API_CreateDataset.md "API_CreateDataset.md")
operation must match.

The `Domain` and `DatasetType` that you choose determine the fields
that must be present in training data that you import to a dataset. For example, if you choose
the `RETAIL` domain and `TARGET_TIME_SERIES` as the
`DatasetType`, Amazon Forecast requires that `item_id`,
`timestamp`, and `demand` fields are present in your data. For more
information, see [Dataset groups](howitworks-datasets-groups.md "howitworks-datasets-groups.md").

Type: String

Valid Values: `RETAIL | CUSTOM | INVENTORY_PLANNING | EC2_CAPACITY | WORK_FORCE | WEB_TRAFFIC | METRICS`

Required: Yes

**[Tags](#API_CreateDatasetGroup_RequestSyntax "#API_CreateDatasetGroup_RequestSyntax")**

The optional metadata that you apply to the dataset group to help you categorize and
organize them. Each tag consists of a key and an optional value, both of which you
define.

The following basic restrictions apply to tags:

- Maximum number of tags per resource - 50.
- For each resource, each tag key must be unique, and each tag key can have only one
  value.
- Maximum key length - 128 Unicode characters in UTF-8.
- Maximum value length - 256 Unicode characters in UTF-8.
- If your tagging schema is used across multiple services and resources, remember that
  other services may have restrictions on allowed characters. Generally allowed characters
  are: letters, numbers, and spaces representable in UTF-8, and the following characters: +

* = . \_ : / @.

- Tag keys and values are case sensitive.
- Do not use `aws:`, `AWS:`, or any upper or lowercase combination
  of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag
  keys with this prefix. Values can have this prefix. If a tag value has `aws` as
  its prefix but the key does not, then Forecast considers it to be a user tag and will
  count against the limit of 50 tags. Tags with only the key prefix of `aws` do
  not count against your tags per resource limit.

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

Array Members: Minimum number of 0 items. Maximum number of 200 items.

Required: No

## Response Syntax

```
{
   "DatasetGroupArn": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[DatasetGroupArn](#API_CreateDatasetGroup_ResponseSyntax "#API_CreateDatasetGroup_ResponseSyntax")**

The Amazon Resource Name (ARN) of the dataset group.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

## Errors

**InvalidInputException**

We can't process the request because it includes an invalid value or a value that exceeds
the valid range.

HTTP Status Code: 400

**LimitExceededException**

The limit on the number of resources per account has been exceeded.

HTTP Status Code: 400

**ResourceAlreadyExistsException**

There is already a resource with this name. Try again with a different name.

HTTP Status Code: 400

**ResourceInUseException**

The specified resource is in use.

HTTP Status Code: 400

**ResourceNotFoundException**

We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try
again.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/forecast-2018-06-26/CreateDatasetGroup.md "../../../goto/cli2/forecast-2018-06-26/CreateDatasetGroup.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/forecast-2018-06-26/CreateDatasetGroup.md "../../../goto/DotNetSDKV4/forecast-2018-06-26/CreateDatasetGroup.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/CreateDatasetGroup.md "../../../goto/SdkForCpp/forecast-2018-06-26/CreateDatasetGroup.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/forecast-2018-06-26/CreateDatasetGroup.md "../../../goto/SdkForGoV2/forecast-2018-06-26/CreateDatasetGroup.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/CreateDatasetGroup.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/CreateDatasetGroup.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/forecast-2018-06-26/CreateDatasetGroup.md "../../../goto/SdkForJavaScriptV3/forecast-2018-06-26/CreateDatasetGroup.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/forecast-2018-06-26/CreateDatasetGroup.md "../../../goto/SdkForKotlin/forecast-2018-06-26/CreateDatasetGroup.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/forecast-2018-06-26/CreateDatasetGroup.md "../../../goto/SdkForPHPV3/forecast-2018-06-26/CreateDatasetGroup.md")
- [AWS SDK for Python](../../../goto/boto3/forecast-2018-06-26/CreateDatasetGroup.md "../../../goto/boto3/forecast-2018-06-26/CreateDatasetGroup.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/CreateDatasetGroup.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/CreateDatasetGroup.md")
