Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# HyperParameterTuningJobConfig

Configuration information for a hyperparameter tuning job. You specify this object in
the [CreatePredictor](API_CreatePredictor.md "API_CreatePredictor.md") request.

A _hyperparameter_ is a parameter that governs the model training process. You set
hyperparameters before training starts, unlike model parameters, which are determined during
training. The values of the hyperparameters effect which values are chosen for the model parameters.

In a _hyperparameter tuning job_, Amazon Forecast chooses the set of hyperparameter
values that optimize a specified metric. Forecast accomplishes this by running many training jobs
over a range of hyperparameter values. The optimum set of values depends on the
algorithm, the training data, and the specified metric objective.

## Contents

**ParameterRanges**

Specifies the ranges of valid values for the hyperparameters.

Type: [ParameterRanges](API_ParameterRanges.md "API_ParameterRanges.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/HyperParameterTuningJobConfig.md "../../../goto/SdkForCpp/forecast-2018-06-26/HyperParameterTuningJobConfig.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/HyperParameterTuningJobConfig.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/HyperParameterTuningJobConfig.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/HyperParameterTuningJobConfig.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/HyperParameterTuningJobConfig.md")
