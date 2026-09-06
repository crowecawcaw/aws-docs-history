

# Schema for Constraints (constraints.json file)
<a name="model-monitor-byoc-constraints"></a>

**Note**  
Amazon SageMaker Model Monitor is no longer open to new customers. Existing customers can continue to use the service as normal. AWS continues to invest in security and availability improvements for Model Monitor, but we do not plan to introduce new features. For more information, see [Amazon SageMaker Model Monitor availability change](model-monitor-availability-change.md). 

A constraints.json file is used to express the constraints that a dataset must satisfy. Amazon SageMaker Model Monitor containers can use the constraints.json file to evaluate datasets against. Prebuilt containers provide the ability to generate the constraints.json file automatically for a baseline dataset. If you bring your own container, you can provide it with similar abilities or you can create the constraints.json file in some other way. Here is the schema for the constraint file that the prebuilt container uses. Bring your own containers can adopt the same format or enhance it as required.

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

The `monitoring_config` object contains options for monitoring job for the feature. The following table describes each option.

Monitoring Constraints



- **`evaluate_constraints`**
  - When `Enabled`, evaluates whether the current dataset being analyzed satisfies the constraints specified in the constraints.json file taken as a baseline. <br />Valid values: `Enabled` or `Disabled`<br />Default: `Enabled`

- **`emit_metrics`**
  - When `Enabled`, emits CloudWatch metrics for the data contained in the file.<br />Valid values: `Enabled` or `Disabled`<br />Default: `Enabled`

- **`datatype_check_threshold`**
  - If the threshold is above the value of the specified `datatype_check_threshold`, this causes a failure that is treated as a violation in the violation report. If the data types in the current execution are not the same as in the baseline dataset, this threshold is used to evaluate if it needs to be flagged as a violation.<br />During the baseline step, the generated constraints suggest the inferred data type for each column. The `datatype_check_threshold` parameter can be tuned to adjust the threshold on when it is flagged as a violation.<br />Valid values: float<br />Default: 0.1

- **`domain_content_threshold`**
  - If there are more unknown values for a String field in the current dataset than in the baseline dataset, this threshold can be used to dictate if it needs to be flagged as a violation.<br />Valid values: float<br />Default: 0.1

- **`distribution_constraints`**
  - perform\_comparisonWhen `Enabled`, this flag instructs the code to perform a distribution comparison between the baseline distribution and the distribution observed for the current dataset.<br />Valid values: `Enabled` or `Disabled` <br />Default: `Enabled`
  - comparison\_thresholdIf the threshold is above the value set for the `comparison_threshold`, this causes a failure that is treated as a violation in the violation report. The distance is calculated by getting the maximum absolute difference between the cumulative distribution functions of two distributions. <br />Valid values: float<br />Default: 0.1
  - comparison\_methodWhether to calculate `linf_simple` or `linf_robust`. The `linf_simple` is based on the maximum absolute difference between the cumulative distribution functions of two distributions. Calculating `linf_robust` is based on `linf_simple`, but is used when there are not enough samples. The `linf_robust` formula is based on the [Two-sample Kolmogorov–Smirnov test](https://en.m.wikipedia.org/wiki/Kolmogorov%E2%80%93Smirnov_test).<br />Valid values: `linf_simple` or `linf_robust`
  - categorical\_comparison\_thresholdOptional. Sets a threshold for categorical features. If the value in the dataset exceeds the threshold that you set, a violation is recorded in the violation report.<br />Valid values: float<br />Default: The value assigned to the `comparison_threshold` parameter
  - categorical\_drift\_methodOptional. For categorical features, specifies the computation method used to detect distribution drift. If you don't set this parameter, the K-S (LInfinity) test is used. <br />Valid Values: `LInfinity` or `ChiSquared`<br />Default: `LInfinity`

