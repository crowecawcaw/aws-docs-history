# Container Contract

Outputs

The container can analyze the data available in the
`*dataset_source*` path and write reports to the path in
`*output_path*.` The container code can write any reports
that suit your needs.

If you use the following structure and contract, certain output files are
treated specially by SageMaker AI in the visualization and API . This applies only
to tabular datasets.

Output Files for Tabular Datasets

| File Name                         | Description                                                                                                                                                                                                                           |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`statistics.json`**             | This file is expected to have columnar statistics for<br>each feature in the dataset that is analyzed. The schema<br>for this file is available in the next section.                                                                  |
| **`constraints.json`**            | This file is expected to have the constraints on the<br>features observed. The schema for this file is available<br>in the next section.                                                                                              |
| **`constraints_violations.json`** | This file is expected to have the list of violations<br>found in this current set of data as compared to the<br>baseline statistics and constraints file specified in<br>the `baseline_constaints` and<br>`baseline_statistics` path. |

In addition, if the `publish_cloudwatch_metrics` value is
`"Enabled"` container code can emit Amazon CloudWatch metrics in this
location: `/opt/ml/output/metrics/cloudwatch`. The schema for
these files is described in the following sections.

###### Topics

- [Schema for Statistics
  (statistics.json file)](model-monitor-byoc-statistics.md "model-monitor-byoc-statistics.md")
- [Schema for Constraints
  (constraints.json file)](model-monitor-byoc-constraints.md "model-monitor-byoc-constraints.md")
