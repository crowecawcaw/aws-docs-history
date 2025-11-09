# Schema for Violations

(constraint_violations.json file)

The violations file is generated as the output of a
`MonitoringExecution`, which lists the results of evaluating the
constraints (specified in the constraints.json file) against the current dataset
that was analyzed. The Amazon SageMaker Model Monitor prebuilt container provides the following violation
checks.

```
{
    "violations": [{
      "feature_name" : "string",
      "constraint_check_type" :
              "data_type_check",
            | "completeness_check",
            | "baseline_drift_check",
            | "missing_column_check",
            | "extra_column_check",
            | "categorical_values_check"
      "description" : "string"
    }]
}
```

Types of Violations Monitored

| Violation Check Type       | Description                                                                                                                                                                                                                                                                                                                                                                    |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `data_type_check`          | If the data types in the current execution are not the same<br>as in the baseline dataset, this violation is flagged.<br>During the baseline step, the generated constraints suggest<br>the inferred data type for each column. The<br>`monitoring_config.datatype_check_threshold`<br>parameter can be tuned to adjust the threshold on when it is<br>flagged as a violation. |
| `completeness_check`       | If the completeness (% of non-null items) observed in the<br>current execution exceeds the threshold specified in<br>completeness threshold specified per feature, this violation is<br>flagged.<br>During the baseline step, the generated constraints suggest a<br>completeness value.                                                                                       |
| `baseline_drift_check`     | If the calculated distribution distance between the current<br>and the baseline datasets is more than the threshold specified<br>in `monitoring_config.comparison_threshold`, this<br>violation is flagged.                                                                                                                                                                    |
| `missing_column_check`     | If the number of columns in the current dataset is less<br>than the number in the baseline dataset, this violation is<br>flagged.                                                                                                                                                                                                                                              |
| `extra_column_check`       | If the number of columns in the current dataset is more<br>than the number in the baseline, this violation is<br>flagged.                                                                                                                                                                                                                                                      |
| `categorical_values_check` | If there are more unknown values in the current dataset<br>than in the baseline dataset, this violation is flagged. This<br>value is dictated by the threshold in<br>`monitoring_config.domain_content_threshold`.                                                                                                                                                             |
