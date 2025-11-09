# Schema for Constraints

(constraints.json file)

A constraints.json file is used to express the constraints that a
dataset must satisfy. Amazon SageMaker Model Monitor containers can use the constraints.json file
to evaluate datasets against. Prebuilt containers provide the ability to
generate the constraints.json file automatically for a baseline dataset.
If you bring your own container, you can provide it with similar
abilities or you can create the constraints.json file in some other way.
Here is the schema for the constraint file that the prebuilt container
uses. Bring your own containers can adopt the same format or enhance it
as required.

```
{
    "version": 0,
    "features":
    [
        {
            "name": "string",
            "inferred_type": "Integral" | "Fractional" |
                    | "String" | "Unknown",
            "completeness": number,
            "num_constraints":
            {
                "is_non_negative": boolean
            },
            "string_constraints":
            {
                "domains":
                [
                    "list of",
                    "observed values",
                    "for small cardinality"
                ]
            },
            "monitoringConfigOverrides":
            {}
        }
    ],
    "monitoring_config":
    {
        "evaluate_constraints": "Enabled",
        "emit_metrics": "Enabled",
        "datatype_check_threshold": 0.1,
        "domain_content_threshold": 0.1,
        "distribution_constraints":
        {
            "perform_comparison": "Enabled",
            "comparison_threshold": 0.1,
            "comparison_method": "Simple"||"Robust",
            "categorical_comparison_threshold": 0.1,
            "categorical_drift_method": "LInfinity"||"ChiSquared"
        }
    }
}
```

The `monitoring_config` object contains options for monitoring
job for the feature. The following table describes each option.

Monitoring Constraints

| Constraint                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `evaluate_constraints`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | When `Enabled`, evaluates whether the<br>current dataset being analyzed satisfies the<br>constraints specified in the constraints.json file<br>taken as a baseline.<br>Valid values: `Enabled` or<br>`Disabled`<br>Default: `Enabled`                                                                                                                                                                                                                                                                                                                                                                                               |
| `emit_metrics`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | When `Enabled`, emits CloudWatch metrics for<br>the data contained in the file.<br>Valid values: `Enabled` or<br>`Disabled`<br>Default: `Enabled`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `datatype_check_threshold`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | If the threshold is above the value of the<br>specified `datatype_check_threshold`,<br>this causes a failure that is treated as a violation<br>in the violation report. If the data types in the<br>current execution are not the same as in the<br>baseline dataset, this threshold is used to evaluate<br>if it needs to be flagged as a violation.<br>During the baseline step, the generated<br>constraints suggest the inferred data type for each<br>column. The `datatype_check_threshold`<br>parameter can be tuned to adjust the threshold on<br>when it is flagged as a violation.<br>Valid values: float<br>Default: 0.1 |
| `domain_content_threshold`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | If there are more unknown values for a String<br>field in the current dataset than in the baseline<br>dataset, this threshold can be used to dictate if it<br>needs to be flagged as a violation.<br>Valid values: float<br>Default: 0.1                                                                                                                                                                                                                                                                                                                                                                                            |
| `distribution_constraints`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | `perform_comparison`<br>When `Enabled`, this flag instructs the<br>code to perform a distribution comparison between<br>the baseline distribution and the distribution<br>observed for the current dataset.Valid<br>values: `Enabled` or<br>`Disabled`<br>Default:<br>`Enabled`                                                                                                                                                                                                                                                                                                                                                     |
| `comparison_threshold`<br>If the threshold is above the value set for the<br>`comparison_threshold`, this causes a<br>failure that is treated as a violation in the<br>violation report. The distance is calculated by<br>getting the maximum absolute difference between the<br>cumulative distribution functions of two<br>distributions. Valid values:<br>floatDefault: 0.1                                                                                                                                                                                                                                    |
| `comparison_method`<br>Whether to calculate `linf_simple` or<br>`linf_robust`. The<br>`linf_simple` is based on the maximum<br>absolute difference between the cumulative distribution<br>functions of two distributions. Calculating<br>`linf_robust` is based on<br>`linf_simple`, but is used when there are<br>not enough samples. The `linf_robust` formula<br>is based on the [Two-sample Kolmogorov–Smirnov<br>test](https://en.m.wikipedia.org/wiki/Kolmogorov%E2%80%93Smirnov_test "https://en.m.wikipedia.org/wiki/Kolmogorov%E2%80%93Smirnov_test").Valid values:<br>`linf_simple` or<br>`linf_robust` |
| `categorical_comparison_threshold`Optional.<br>Sets a threshold for categorical features. If the value<br>in the dataset exceeds the threshold that you set, a<br>violation is recorded in the violation<br>report.Valid values:<br>floatDefault: The value assigned to the<br>`comparison_threshold`<br>parameter                                                                                                                                                                                                                                                                                                |
| `categorical_drift_method`Optional. For<br>categorical features, specifies the computation method<br>used to detect distribution drift. If you don't set this<br>parameter, the K-S (LInfinity) test is used.<br>Valid Values: `LInfinity` or<br>`ChiSquared`Default:<br>`LInfinity`                                                                                                                                                                                                                                                                                                                              |
