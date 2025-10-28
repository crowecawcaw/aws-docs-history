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

````
{
    "version": 0,
    "features":
    [
        {
            "name": "string",
            "inferred_type": "Integral" | "Fractional" |
| "String" | "Unknown", "completeness": number, "num_constraints": { "is_non_negative": boolean }, "string_constraints": { "domains": [ "list of", "observed values", "for small cardinality" ] }, "monitoringConfigOverrides": {} } ], "monitoring_config": { "evaluate_constraints": "Enabled", "emit_metrics": "Enabled", "datatype_check_threshold": 0.1, "domain_content_threshold": 0.1, "distribution_constraints": { "perform_comparison": "Enabled", "comparison_threshold": 0.1, "comparison_method": "Simple"||"Robust", "categorical_comparison_threshold": 0.1, "categorical_drift_method": "LInfinity"||"ChiSquared" } } } ``` The `monitoring_config` object contains options for monitoring job for the feature. The following table describes each option. Monitoring Constraints
| Constraint | Description |
| --- | --- |
| `evaluate_constraints` | When `Enabled`, evaluates whether the current dataset being analyzed satisfies the constraints specified in the constraints.json file taken as a baseline. Valid values: `Enabled` or `Disabled` Default: `Enabled` |
| `emit_metrics` | When `Enabled`, emits CloudWatch metrics for the data contained in the file. Valid values: `Enabled` or `Disabled` Default: `Enabled` |
| `datatype_check_threshold` | If the threshold is above the value of the specified `datatype_check_threshold`, this causes a failure that is treated as a violation in the violation report. If the data types in the current execution are not the same as in the baseline dataset, this threshold is used to evaluate if it needs to be flagged as a violation. During the baseline step, the generated constraints suggest the inferred data type for each column. The `datatype_check_threshold` parameter can be tuned to adjust the threshold on when it is flagged as a violation. Valid values: float Default: 0.1 |
| `domain_content_threshold` | If there are more unknown values for a String field in the current dataset than in the baseline dataset, this threshold can be used to dictate if it needs to be flagged as a violation. Valid values: float Default: 0.1 |
| `distribution_constraints` | `perform_comparison` When `Enabled`, this flag instructs the code to perform a distribution comparison between the baseline distribution and the distribution observed for the current dataset.Valid values: `Enabled` or `Disabled` Default: `Enabled` |
| `comparison_threshold` If the threshold is above the value set for the `comparison_threshold`, this causes a failure that is treated as a violation in the violation report. The distance is calculated by getting the maximum absolute difference between the cumulative distribution functions of two distributions. Valid values: floatDefault: 0.1 | | `comparison_method` Whether to calculate `linf_simple` or `linf_robust`. The `linf_simple` is based on the maximum absolute difference between the cumulative distribution functions of two distributions. Calculating `linf_robust` is based on `linf_simple`, but is used when there are not enough samples. The `linf_robust` formula is based on the [Two-sample Kolmogorov–Smirnov test](https://en.m.wikipedia.org/wiki/Kolmogorov%E2%80%93Smirnov_test "https://en.m.wikipedia.org/wiki/Kolmogorov%E2%80%93Smirnov_test").Valid values: `linf_simple` or `linf_robust` |
| `categorical_comparison_threshold`Optional. Sets a threshold for categorical features. If the value in the dataset exceeds the threshold that you set, a violation is recorded in the violation report.Valid values: floatDefault: The value assigned to the `comparison_threshold` parameter | | `categorical_drift_method`Optional. For categorical features, specifies the computation method used to detect distribution drift. If you don't set this parameter, the K-S (LInfinity) test is used. Valid Values: `LInfinity` or `ChiSquared`Default: `LInfinity` |
````
