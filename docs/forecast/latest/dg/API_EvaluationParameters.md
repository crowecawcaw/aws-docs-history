Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# EvaluationParameters

Parameters that define how to split a dataset into training data and testing data, and the
number of iterations to perform. These parameters are specified in the predefined algorithms
but you can override them in the [CreatePredictor](API_CreatePredictor.md "API_CreatePredictor.md") request.

## Contents

**BackTestWindowOffset**

The point from the end of the dataset where you want to split the data for model training
and testing (evaluation). Specify the value as the number of data points. The default is the
value of the forecast horizon. `BackTestWindowOffset` can be used to mimic a past
virtual forecast start date. This value must be greater than or equal to the forecast horizon
and less than half of the TARGET_TIME_SERIES dataset length.

`ForecastHorizon` <= `BackTestWindowOffset` < 1/2 \*
TARGET_TIME_SERIES dataset length

Type: Integer

Required: No

**NumberOfBacktestWindows**

The number of times to split the input data. The default is 1. Valid values are 1 through 5.

Type: Integer

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/EvaluationParameters.md "../../../goto/SdkForCpp/forecast-2018-06-26/EvaluationParameters.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/EvaluationParameters.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/EvaluationParameters.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/EvaluationParameters.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/EvaluationParameters.md")
