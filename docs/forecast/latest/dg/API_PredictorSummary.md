Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# PredictorSummary

Provides a summary of the predictor properties that are used in the [ListPredictors](API_ListPredictors.md "API_ListPredictors.md") operation. To get the complete set of properties, call the [DescribePredictor](API_DescribePredictor.md "API_DescribePredictor.md") operation, and provide the listed
`PredictorArn`.

###### Important

Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

## Contents

**CreationTime**

When the model training task was created.

Type: Timestamp

Required: No

**DatasetGroupArn**

The Amazon Resource Name (ARN) of the dataset group that contains the data used to train
the predictor.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

Required: No

**IsAutoPredictor**

Whether AutoPredictor was used to create the predictor.

Type: Boolean

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

**PredictorArn**

The ARN of the predictor.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

Required: No

**PredictorName**

The name of the predictor.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z][a-zA-Z0-9_]*`

Required: No

**ReferencePredictorSummary**

A summary of the reference predictor used if the predictor was retrained or
upgraded.

Type: [ReferencePredictorSummary](API_ReferencePredictorSummary.md "API_ReferencePredictorSummary.md") object

Required: No

**Status**

The status of the predictor. States include:

- `ACTIVE`
- `CREATE_PENDING`, `CREATE_IN_PROGRESS`,
  `CREATE_FAILED`
- `DELETE_PENDING`, `DELETE_IN_PROGRESS`,
  `DELETE_FAILED`
- `CREATE_STOPPING`, `CREATE_STOPPED`

###### Note

The `Status` of the predictor must be `ACTIVE` before you can use
the predictor to create a forecast.

Type: String

Length Constraints: Maximum length of 256.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/PredictorSummary.md "../../../goto/SdkForCpp/forecast-2018-06-26/PredictorSummary.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/PredictorSummary.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/PredictorSummary.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/PredictorSummary.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/PredictorSummary.md")
