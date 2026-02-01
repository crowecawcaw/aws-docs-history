Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# DescribeDataset

Describes an Amazon Forecast dataset created using the [CreateDataset](API_CreateDataset.md "API_CreateDataset.md") operation.

###### Important

Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

In addition to listing the parameters specified in the `CreateDataset` request,
this operation includes the following dataset properties:

- `CreationTime`
- `LastModificationTime`
- `Status`

## Request Syntax

```
{
   "DatasetArn": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[DatasetArn](#API_DescribeDataset_RequestSyntax "#API_DescribeDataset_RequestSyntax")**

The Amazon Resource Name (ARN) of the dataset.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

Required: Yes

## Response Syntax

```
{
   "CreationTime": ***number***,
   "DataFrequency": "***string***",
   "DatasetArn": "***string***",
   "DatasetName": "***string***",
   "DatasetType": "***string***",
   "Domain": "***string***",
   "EncryptionConfig": {
      "KMSKeyArn": "***string***",
      "RoleArn": "***string***"
   },
   "LastModificationTime": ***number***,
   "Schema": {
      "Attributes": [
         {
            "AttributeName": "***string***",
            "AttributeType": "***string***"
         }
      ]
   },
   "Status": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[CreationTime](#API_DescribeDataset_ResponseSyntax "#API_DescribeDataset_ResponseSyntax")**

When the dataset was created.

Type: Timestamp

**[DataFrequency](#API_DescribeDataset_ResponseSyntax "#API_DescribeDataset_ResponseSyntax")**

The frequency of data collection.

Valid intervals are Y (Year), M (Month), W (Week), D (Day), H (Hour), 30min (30 minutes),
15min (15 minutes), 10min (10 minutes), 5min (5 minutes), and 1min (1 minute). For example,
"M" indicates every month and "30min" indicates every 30 minutes.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 5.

Pattern: `^Y|M|W|D|H|30min|15min|10min|5min|1min$`

**[DatasetArn](#API_DescribeDataset_ResponseSyntax "#API_DescribeDataset_ResponseSyntax")**

The Amazon Resource Name (ARN) of the dataset.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

**[DatasetName](#API_DescribeDataset_ResponseSyntax "#API_DescribeDataset_ResponseSyntax")**

The name of the dataset.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z][a-zA-Z0-9_]*`

**[DatasetType](#API_DescribeDataset_ResponseSyntax "#API_DescribeDataset_ResponseSyntax")**

The dataset type.

Type: String

Valid Values: `TARGET_TIME_SERIES | RELATED_TIME_SERIES | ITEM_METADATA`

**[Domain](#API_DescribeDataset_ResponseSyntax "#API_DescribeDataset_ResponseSyntax")**

The domain associated with the dataset.

Type: String

Valid Values: `RETAIL | CUSTOM | INVENTORY_PLANNING | EC2_CAPACITY | WORK_FORCE | WEB_TRAFFIC | METRICS`

**[EncryptionConfig](#API_DescribeDataset_ResponseSyntax "#API_DescribeDataset_ResponseSyntax")**

The AWS Key Management Service (KMS) key and the AWS Identity and Access Management (IAM) role that Amazon Forecast can assume to access
the key.

Type: [EncryptionConfig](API_EncryptionConfig.md "API_EncryptionConfig.md") object

**[LastModificationTime](#API_DescribeDataset_ResponseSyntax "#API_DescribeDataset_ResponseSyntax")**

When you create a dataset, `LastModificationTime` is the same as
`CreationTime`. While data is being imported to the dataset,
`LastModificationTime` is the current time of the `DescribeDataset`
call. After a [CreateDatasetImportJob](API_CreateDatasetImportJob.md "API_CreateDatasetImportJob.md")
operation has finished, `LastModificationTime` is when the import job completed or
failed.

Type: Timestamp

**[Schema](#API_DescribeDataset_ResponseSyntax "#API_DescribeDataset_ResponseSyntax")**

An array of `SchemaAttribute` objects that specify the dataset fields. Each
`SchemaAttribute` specifies the name and data type of a field.

Type: [Schema](API_Schema.md "API_Schema.md") object

**[Status](#API_DescribeDataset_ResponseSyntax "#API_DescribeDataset_ResponseSyntax")**

The status of the dataset. States include:

- `ACTIVE`
- `CREATE_PENDING`, `CREATE_IN_PROGRESS`,
  `CREATE_FAILED`
- `DELETE_PENDING`, `DELETE_IN_PROGRESS`,
  `DELETE_FAILED`
- `UPDATE_PENDING`, `UPDATE_IN_PROGRESS`,
  `UPDATE_FAILED`

The `UPDATE` states apply while data is imported to the dataset from a call to
the [CreateDatasetImportJob](API_CreateDatasetImportJob.md "API_CreateDatasetImportJob.md") operation and reflect the status of the dataset import job.
For example, when the import job status is `CREATE_IN_PROGRESS`, the status of the
dataset is `UPDATE_IN_PROGRESS`.

###### Note

The `Status` of the dataset must be `ACTIVE` before you can import
training data.

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

- [AWS Command Line Interface V2](../../../goto/cli2/forecast-2018-06-26/DescribeDataset.md "../../../goto/cli2/forecast-2018-06-26/DescribeDataset.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/forecast-2018-06-26/DescribeDataset.md "../../../goto/DotNetSDKV4/forecast-2018-06-26/DescribeDataset.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/DescribeDataset.md "../../../goto/SdkForCpp/forecast-2018-06-26/DescribeDataset.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/forecast-2018-06-26/DescribeDataset.md "../../../goto/SdkForGoV2/forecast-2018-06-26/DescribeDataset.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/DescribeDataset.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/DescribeDataset.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/forecast-2018-06-26/DescribeDataset.md "../../../goto/SdkForJavaScriptV3/forecast-2018-06-26/DescribeDataset.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/forecast-2018-06-26/DescribeDataset.md "../../../goto/SdkForKotlin/forecast-2018-06-26/DescribeDataset.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/forecast-2018-06-26/DescribeDataset.md "../../../goto/SdkForPHPV3/forecast-2018-06-26/DescribeDataset.md")
- [AWS SDK for Python](../../../goto/boto3/forecast-2018-06-26/DescribeDataset.md "../../../goto/boto3/forecast-2018-06-26/DescribeDataset.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/DescribeDataset.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/DescribeDataset.md")
