# Endpoint requests for time series data

A SageMaker Clarify processing job serializes data into arbitrary JSON structures
(with MIME type: `application/json`). To do this, you must provide a template
string to the analysis configuration `content_template` parameter.
This is used by the SageMaker Clarify processing job to construct the JSON query provided
to your model. `content_template` contains a record or multiple
records from your dataset. You must also provide a template string for
`record_template`, which is used to construct the JSON structure
of each record. These records are then inserted into `content_template`.
For more information
about `content_type` or `dataset_type`, see [Analysis Configuration Files](clarify-processing-job-configure-analysis.md "clarify-processing-job-configure-analysis.md").

###### Note

Because `content_template` and `record_template`
are string parameters, any double quote characters (") that are part of the
JSON serialized structure should be noted as an escaped character in your
configuration. For example, if you want to escape a double quote in Python,
you could enter the following value for `content_template`:

```
'$record'
```

The following table shows examples of serialized JSON request payloads and
the corresponding `content_template` and `record_template`
parameters required to construct them.

| Use case                                                              | Endpoint request payload (string representation)                                                                                                                                                                                                          | content_template            | record_template                                                                                                             |
| --------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Single record at a time                                               | `{"target": [1, 2, 3],"start": "2024-01-01 01:00:00"}`                                                                                                                                                                                                    | `'$record'`                 | `'{"start": $start_time, "target": $target_time_series}'`                                                                   |
| Single record with `$related_time_series` and<br>`$static_covariates` | `{"target": [1, 2, 3],"start": "2024-01-01 01:00:00","dynamic_feat": [[1.0, 2.0, 3.0],[1.0, 2.0, 3.0],"cat": [0,1]}`                                                                                                                                      | `'$record'`                 | `'{"start": $start_time, "target": $target_time_series, "dynamic_feat": $related_time_series, "cat": $static_covariates}'`  |
| Multi-records                                                         | `{"instances": [{"target": [1, 2, 3],"start": "2024-01-01 01:00:00"}, {"target": [1, 2, 3],"start": "2024-01-01 02:00:00"}]}`                                                                                                                             | `'{"instances": $records}'` | `'{"start": $start_time, "target": $target_time_series}'`                                                                   |
| Multi-records with `$related_time_series` and<br>`$static_covariates` | `{"instances": [{"target": [1, 2, 3],"start": "2024-01-01 01:00:00","dynamic_feat": [[1.0, 2.0, 3.0],[1.0, 2.0, 3.0],"cat": [0,1]}, {"target": [1, 2, 3],"start": "2024-01-01 02:00:00","dynamic_feat": [[1.0, 2.0, 3.0],[1.0, 2.0, 3.0],"cat": [0,1]}]}` | `'{"instances": $records}'` | `''{"start": $start_time, "target": $target_time_series, "dynamic_feat": $related_time_series, "cat": $static_covariates}'` |
