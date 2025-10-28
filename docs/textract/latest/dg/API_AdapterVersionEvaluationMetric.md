# AdapterVersionEvaluationMetric

Contains information on the metrics used to evalute the peformance of a given adapter version. Includes data for
baseline model performance and individual adapter version perfromance.

## Contents

**AdapterVersion**

The F1 score, precision, and recall metrics for the baseline model.

Type: [EvaluationMetric](API_EvaluationMetric.md "API_EvaluationMetric.md") object

Required: No

**Baseline**

The F1 score, precision, and recall metrics for the baseline model.

Type: [EvaluationMetric](API_EvaluationMetric.md "API_EvaluationMetric.md") object

Required: No

**FeatureType**

Indicates the feature type being analyzed by a given adapter version.

Type: String

Valid Values: `TABLES | FORMS | QUERIES | SIGNATURES | LAYOUT`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/textract-2018-06-27/AdapterVersionEvaluationMetric.md "../../../goto/SdkForCpp/textract-2018-06-27/AdapterVersionEvaluationMetric.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/textract-2018-06-27/AdapterVersionEvaluationMetric.md "../../../goto/SdkForJavaV2/textract-2018-06-27/AdapterVersionEvaluationMetric.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/textract-2018-06-27/AdapterVersionEvaluationMetric.md "../../../goto/SdkForRubyV3/textract-2018-06-27/AdapterVersionEvaluationMetric.md")
