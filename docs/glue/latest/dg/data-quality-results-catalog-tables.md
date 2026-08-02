# Writing data quality results to Data Catalog tables

You can configure AWS Glue Data Quality evaluation runs to automatically write results to Apache Iceberg
tables in the AWS Glue Data Catalog. After you enable results output, you can query your data quality
results directly using , build dashboards with visualization tools, and maintain a
centralized history of data quality outcomes across your account.

You can write the following types of data quality results to Data Catalog tables:

- **Rule results** – The pass or fail outcome for each
  rule in your ruleset, including the evaluated metrics and failure reasons
- **Profiling results** – Statistics gathered by
  analyzers, including scalar values (such as mean and standard deviation) and distribution
  data (histograms and value distributions)
- **Row-level results** – Per-record evaluation
  outcomes that identify which specific rows in your dataset passed or failed each
  rule
- **Observation results** – Anomaly detection
  predictions, including expected values, prediction bounds, and whether the actual value was
  flagged as an anomaly

## Prerequisites

To write data quality results to Data Catalog tables, the IAM role you use for the evaluation
run must have the following permissions:

- Permission to create and update databases and tables in the AWS Glue Data Catalog
- Permission to write to the Amazon S3 location where Iceberg table data is stored

The evaluation run uses the IAM role you specify to write to the results tables. This
is the same role that has access to the source data table.

## Configuring results output

You configure data quality results output using the `--additional-run-options`
parameter of the `StartDataQualityRulesetEvaluationRun` API or the
`additional_options` parameter in AWS Glue ETL jobs. By default, AWS Glue Data Quality does not
write results to Data Catalog tables. You must explicitly enable each result type that you want
to write.

Each result type has its own configuration block with a shared
`CatalogTableConfig` structure. If you do not provide a
`CatalogTableConfig`, AWS Glue Data Quality derives default values automatically, including
the table name and Amazon S3 path.

The `CatalogTableConfig` structure contains the following fields:

- **DatabaseName** (optional) – The name of the
  catalog database for the target table. If not specified, a default database is
  created.
- **TableName** (optional) – The name of the target
  table. If not specified, a default table name is used.
- **S3Location** (optional) – The Amazon S3 location
  where table data is stored. Format:
  `s3://`amzn-s3-demo-bucket`/`prefix`/`.
  If not specified, results are stored in a default location.
- **CatalogId** (optional) – The ID of the
  AWS Glue Data Catalog in which to create the table. If not specified, the AWS account ID is used
  by default.

**Example: Configure rule results and profiling results**

```
aws glue start-data-quality-ruleset-evaluation-run \
  --data-source '{
    "GlueTable": {
      "DatabaseName": "my_database",
      "TableName": "my_table"
    }
  }' \
  --role "arn:aws:iam::123456789012:role/GlueServiceRole" \
  --ruleset-names '["my_ruleset"]' \
  --additional-run-options '{
    "DataQualityRuleResults": {
      "WriteDataQualityRuleResultsEnabled": true,
      "CatalogTableConfig": {
        "DatabaseName": "quality_results",
        "TableName": "rule_results"
      }
    },
    "ProfilingResults": {
      "WriteProfilingResultsEnabled": true,
      "CatalogTableConfig": {
        "DatabaseName": "quality_results",
        "TableName": "profiles"
      }
    }
  }'
```

**Example: Configure row-level results**

For row-level results, you can also specify the type of records to include and a
maximum number of rows to write.

```
aws glue start-data-quality-ruleset-evaluation-run \
  --data-source '{
    "GlueTable": {
      "DatabaseName": "my_database",
      "TableName": "my_table"
    }
  }' \
  --role "arn:aws:iam::123456789012:role/GlueServiceRole" \
  --ruleset-names '["my_ruleset"]' \
  --additional-run-options '{
    "RowLevelResults": {
      "MaxRowsToWrite": 5000,
      "ResultType": "FAILED_ONLY",
      "CatalogTableConfig": {
        "DatabaseName": "quality_results",
        "TableName": "row_level_results"
      }
    }
  }'
```

The `ResultType` parameter accepts the following values:

- `FAILED_ONLY` – Write only rows that failed at least one data
  quality rule.
- `PASSED_ONLY` – Write only rows that passed all data quality
  rules.
- `ALL` – Write all rows with their evaluation results.

**Example – Configure in AWS Glue ETL jobs**

In AWS Glue ETL jobs, you configure results output using the
`additional_options` parameter with dot-notation keys:

```
result = EvaluateDataQuality.process_rows(
    frame=dynamic_frame,
    ruleset=ruleset,
    publishing_options={
        "dataQualityEvaluationContext": "my_context",
        "enableDataQualityResultsPublishing": True
    },
    additional_options={
        "observations.scope": "ALL",
        "dataQualityResultsPublishing.strategy": "BEST_EFFORT",
        "dataQualityResultsPublishing.resultsFormat.profilingResults.writeProfilingResultsEnabled": "true",
        "dataQualityResultsPublishing.resultsFormat.profilingResults.catalogTableConfig.databaseName": "my_db",
        "dataQualityResultsPublishing.resultsFormat.profilingResults.catalogTableConfig.tableName": "profiling_results",
        "dataQualityResultsPublishing.resultsFormat.profilingResults.catalogTableConfig.s3Location": "s3://amzn-s3-demo-bucket/profiling/",
        "dataQualityResultsPublishing.resultsFormat.profilingResults.catalogTableConfig.catalogId": "123456789012"
    }
)
```

**Example – Configure observation results**

You can configure observation results the same way as other result types. Observation
results require anomaly detection to be enabled (`ObservationScope: ALL`):

```
aws glue start-data-quality-ruleset-evaluation-run \
  --data-source '{
    "GlueTable": {
      "DatabaseName": "my_database",
      "TableName": "my_table"
    }
  }' \
  --role "arn:aws:iam::123456789012:role/GlueServiceRole" \
  --ruleset-names '["my_ruleset"]' \
  --additional-run-options '{
    "ObservationScope": "ALL",
    "ObservationResults": {
      "WriteObservationResultsEnabled": true,
      "CatalogTableConfig": {
        "DatabaseName": "quality_results",
        "TableName": "observation_results"
      }
    }
  }'
```

## Table schemas

AWS Glue Data Quality writes each result type to a separate Iceberg table. The rule results, profiling
results (including the separate distribution results table), and observation results tables
are partitioned by `catalog_id`, `database_name`,
`table_name`, and `day(stored_on)` to enable efficient querying.
You can filter on `stored_on` directly for time-based queries and Iceberg
handles partition pruning automatically.

### Rule results table

The rule results table stores the pass or fail outcome for each rule evaluated during a
data quality run.

| Column                      | Type                | Description                                                 |
| --------------------------- | ------------------- | ----------------------------------------------------------- |
| `dq_result_id`              | STRING              | Unique identifier for the data quality result.              |
| `rule_name`                 | STRING              | Name of the rule (for example, `Rule_1`).                   |
| `rule_description`          | STRING              | The DQDL expression for the rule.                           |
| `rule_result`               | STRING              | The evaluation result: `PASS` or `FAIL`.                    |
| `evaluation_message`        | STRING              | A message describing the reason for failure, if applicable. |
| `evaluated_metrics`         | MAP<STRING, DOUBLE> | The metrics evaluated by the rule.                          |
| `catalog_id`                | STRING              | The catalog ID of the source table.                         |
| `database_name`             | STRING              | The database name of the source table.                      |
| `table_name`                | STRING              | The name of the source table.                               |
| `ruleset_evaluation_run_id` | STRING              | The ID of the evaluation run.                               |
| `started_on`                | TIMESTAMP           | When the evaluation started.                                |
| `completed_on`              | TIMESTAMP           | When the evaluation completed.                              |
| `evaluated_rule`            | STRING              | The evaluated rule expression after operand resolution.     |
| `ruleset_name`              | STRING              | Name of the ruleset that produced this result.              |

### Profiling results table

The following table describes the columns in the profiling results table. This table
stores scalar statistics gathered by analyzers and rules (such as `Mean`,
`StandardDeviation`, and `Completeness`). AWS Glue Data Quality stores
distribution statistics in a separate distribution results table.

| Column                      | Type                | Description                                                                              |
| --------------------------- | ------------------- | ---------------------------------------------------------------------------------------- |
| `profile_id`                | STRING              | Unique identifier for the data quality profile.                                          |
| `statistic_id`              | STRING              | Unique identifier for the statistic.                                                     |
| `statistic_name`            | STRING              | Name of the statistic (for example, `Mean`,<br>`Completeness`)                           |
| `evaluation_level`          | STRING              | The level at which the statistic is evaluated: `Dataset`,<br>`Column`, or `Multicolumn`. |
| `statistics_value`          | DOUBLE              | The scalar value of the statistic.                                                       |
| `statistic_properties`      | MAP<STRING, STRING> | Additional properties of the statistic.                                                  |
| `columns_referenced`        | ARRAY<STRING>       | The columns referenced by the statistic.                                                 |
| `referenced_datasets`       | ARRAY<STRING>       | Referenced datasets for the statistic.                                                   |
| `column_name`               | STRING              | The target column name.                                                                  |
| `dq_result_id`              | STRING              | Data quality result identifier.                                                          |
| `started_on`                | TIMESTAMP           | When the evaluation started.                                                             |
| `completed_on`              | TIMESTAMP           | When the evaluation completed.                                                           |
| `stored_on`                 | TIMESTAMP           | When the record was written to the table.                                                |
| `catalog_id`                | STRING              | Catalog ID of the source table.                                                          |
| `database_name`             | STRING              | Database name of the source table.                                                       |
| `table_name`                | STRING              | Name of the source table.                                                                |
| `region`                    | STRING              | AWS Region.                                                                              |
| `account_id`                | STRING              | AWS account ID.                                                                          |
| `ruleset_evaluation_run_id` | STRING              | The ID of the evaluation run.                                                            |

### Distribution results table

The following table describes the columns in the distribution results table.
Distribution results are stored separately from scalar profiling statistics, with one row
per bin or category. You can configure this table within the
`ProfilingResults.DistributionResults` block.

| Column                      | Type      | Description                                                                                                                                                 |
| --------------------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `statistic_id`              | STRING    | Unique identifier for the distribution statistic.                                                                                                           |
| `column_name`               | STRING    | The source column (for example, "age" or "department").                                                                                                     |
| `data_type`                 | STRING    | The data type of the column (for example, "LongType",<br>"StringType").                                                                                     |
| `num_bins`                  | INT       | Number of bins used for the distribution.                                                                                                                   |
| `bin_index`                 | INT       | 0-based position of the bin.                                                                                                                                |
| `bin_label`                 | STRING    | For categorical columns: the distinct value. NULL for numeric<br>columns.                                                                                   |
| `bin_lower_bound`           | STRING    | For numeric columns: the lower edge of the bin. NULL for categorical<br>columns.                                                                            |
| `bin_upper_bound`           | STRING    | For numeric columns: the upper edge of the bin. NULL for categorical<br>columns.                                                                            |
| `bin_count`                 | BIGINT    | Frequency count for this bin.                                                                                                                               |
| `null_count`                | INT       | Number of NULL values excluded from the distribution. Same value on every<br>row for a given statistic within a run. NULL when no nulls are present.        |
| `tail_count`                | INT       | Aggregate frequency of categorical values beyond the top 20. Same value on<br>every row for a given statistic within a run. NULL for numeric<br>histograms. |
| `profile_id`                | STRING    | Profile identifier.                                                                                                                                         |
| `dq_result_id`              | STRING    | Data quality result identifier.                                                                                                                             |
| `ruleset_evaluation_run_id` | STRING    | Evaluation run identifier.                                                                                                                                  |
| `started_on`                | TIMESTAMP | When the evaluation started.                                                                                                                                |
| `completed_on`              | TIMESTAMP | When the evaluation completed.                                                                                                                              |
| `stored_on`                 | TIMESTAMP | When the record was written to the table.                                                                                                                   |
| `catalog_id`                | STRING    | Catalog ID of the source table.                                                                                                                             |
| `database_name`             | STRING    | Database name of the source table.                                                                                                                          |
| `table_name`                | STRING    | Name of the source table.                                                                                                                                   |
| `region`                    | STRING    | AWS Region.                                                                                                                                                 |
| `account_id`                | STRING    | AWS account ID.                                                                                                                                             |

### Row-level results table

The following table describes the columns in the row-level results table. You can use
this table to identify the specific records that failed your data quality rules.

| Column                           | Type          | Description                                                             |
| -------------------------------- | ------------- | ----------------------------------------------------------------------- |
| _Source columns_                 | _Varies_      | All columns from the original source data.                              |
| `data_quality_rules_pass`        | ARRAY<STRING> | Rules that passed for this record.                                      |
| `data_quality_rules_fail`        | ARRAY<STRING> | Rules that failed for this record.                                      |
| `data_quality_rules_skip`        | ARRAY<STRING> | Rules that were skipped for this record.                                |
| `data_quality_evaluation_result` | STRING        | The overall evaluation result for this record: `Passed` or<br>`Failed`. |
| `dq_result_id`                   | STRING        | Unique identifier for the data quality result.                          |
| `ruleset_evaluation_run_id`      | STRING        | The ID of the evaluation run.                                           |
| `started_on`                     | TIMESTAMP     | When the evaluation started.                                            |
| `completed_on`                   | TIMESTAMP     | When the evaluation completed.                                          |
| `stored_on`                      | TIMESTAMP     | When the record was written to the table.                               |
| `catalog_id`                     | STRING        | Catalog ID of the source table.                                         |
| `database_name`                  | STRING        | Database name of the source table.                                      |
| `table_name`                     | STRING        | Name of the source table.                                               |
| `region`                         | STRING        | AWS Region.                                                             |
| `account_id`                     | STRING        | AWS account ID.                                                         |

### Observation results table

The observation results table stores anomaly detection predictions for each statistic on
every evaluation run. The table includes all prediction outcomes: anomalies, normal
values, and skipped predictions. This lets you render continuous trend charts with
prediction bands.

| Column                      | Type      | Description                                                                                      |
| --------------------------- | --------- | ------------------------------------------------------------------------------------------------ |
| `statistic_id`              | STRING    | Identifier for the statistic being monitored.                                                    |
| `statistic_name`            | STRING    | Name of the monitored statistic.                                                                 |
| `prediction_outcome`        | STRING    | The anomaly detection result: `ANOMALY`,<br>`NOT_ANOMALY`, or `SKIPPED`.                         |
| `expected_value`            | DOUBLE    | The predicted expected value. NULL when prediction is skipped.                                   |
| `lower_bound`               | DOUBLE    | The lower bound of the predicted range. NULL when prediction is<br>skipped.                      |
| `upper_bound`               | DOUBLE    | The upper bound of the predicted range. NULL when prediction is<br>skipped.                      |
| `observation_message`       | STRING    | A description of the anomaly, if detected.                                                       |
| `training_input`            | STRING    | Whether this data point is included in the anomaly detection model:<br>`INCLUDED` or `EXCLUDED`. |
| `ruleset_evaluation_run_id` | STRING    | The ID of the evaluation run.                                                                    |
| `recorded_on`               | TIMESTAMP | When the observation was recorded.                                                               |
| `stored_on`                 | TIMESTAMP | When the record was written to the table.                                                        |
| `actual_value`              | DOUBLE    | The actual observed value for the statistic.                                                     |
| `training_status`           | STRING    | Status of the anomaly detection model training (for example,<br>`PENDING`, `COMPLETED`).         |
| `recommended_rules`         | STRING    | Rules recommended based on the anomaly detection prediction.                                     |
| `modified_rules`            | STRING    | Rules modified with updated thresholds based on predictions.                                     |
| `catalog_id`                | STRING    | Catalog ID of the source table.                                                                  |
| `database_name`             | STRING    | Database name of the source table.                                                               |
| `table_name`                | STRING    | Name of the source table.                                                                        |

###### Note

The observation results table uses an append-only write model. When you exclude a data
point using the `BatchPutDataQualityStatisticAnnotation` API, a new row is
appended with `training_input` set to `EXCLUDED`. To query the
latest state of each observation, use the `stored_on` timestamp to identify
the most recent row for each statistic and run combination.

###### Note

This table also stores distribution overflow observations, generated when more than
2% of values fall outside frozen bin boundaries. These rows have
`statistic_name = 'Distribution'` and `prediction_outcome` is
NULL. The `observation_message` field contains the overflow
description.

## Querying results with

After your data quality evaluation completes, you can query the results tables directly
using . The following examples demonstrate common query patterns.

**Example: Find failed rules for a specific run**

```
SELECT rule_name, rule_description, evaluation_message, evaluated_metrics
FROM quality_results.rule_results
WHERE ruleset_evaluation_run_id = 'dqr-12345678'
  AND rule_result = 'FAIL'
ORDER BY rule_name;
```

**Example: View profiling statistics over time**

```
SELECT stored_on, statistics_value
FROM quality_results.profiles
WHERE database_name = 'my_database'
  AND table_name = 'my_table'
  AND statistic_name = 'Mean'
  AND columns_referenced = ARRAY['salary']
ORDER BY stored_on;
```

**Example – Identify rows that failed a specific rule**

```
SELECT *
FROM quality_results.row_level_results
WHERE data_quality_evaluation_result = 'Failed'
  AND contains(data_quality_rules_fail, 'IsComplete "email"');
```

**Example – View a numeric histogram**

```
SELECT bin_index, bin_lower_bound, bin_upper_bound, bin_count
FROM quality_results.distributions
WHERE column_name = 'salary'
  AND ruleset_evaluation_run_id = 'dqrun-abc123'
ORDER BY bin_index;
```

**Example – View a categorical value distribution**

```
SELECT bin_label, bin_count
FROM quality_results.distributions
WHERE column_name = 'department'
  AND ruleset_evaluation_run_id = 'dqrun-abc123'
ORDER BY bin_count DESC;
```

**Example – Track category frequency over time**

```
SELECT started_on, bin_count
FROM quality_results.distributions
WHERE column_name = 'status' AND bin_label = 'active'
ORDER BY started_on;
```

**Example: View anomaly detection trends with prediction
bands**

```
SELECT o.recorded_on,
       p.statistics_value AS actual_value,
       o.expected_value,
       o.lower_bound,
       o.upper_bound,
       o.prediction_outcome
FROM quality_results.profiles p
JOIN quality_results.observation_results o
  ON p.statistic_id = o.statistic_id
  AND p.ruleset_evaluation_run_id = o.ruleset_evaluation_run_id
WHERE p.database_name = 'my_database'
  AND p.table_name = 'my_table'
  AND p.statistic_name = 'RowCount'
  AND p.stored_on >= DATE '2025-03-01'
ORDER BY p.stored_on;
```

**Example – Query latest observation state after
annotations**

Because the observation results table uses an append-only model, exclusion annotations
add new rows. Use a deduplication query to get the latest state for each observation:

```
SELECT statistic_id, statistic_name, prediction_outcome,
       expected_value, lower_bound, upper_bound, training_input, stored_on
FROM (
  SELECT *, ROW_NUMBER() OVER (
    PARTITION BY statistic_id, ruleset_evaluation_run_id
    ORDER BY stored_on DESC
  ) AS rn
  FROM quality_results.observation_results
  WHERE database_name = 'my_database'
    AND table_name = 'my_table'
)
WHERE rn = 1
ORDER BY stored_on;
```

## Considerations

Keep the following considerations in mind when writing data quality results to Data Catalog
tables:

- AWS Glue Data Quality stores results in Apache Iceberg format, which supports efficient time-travel
  queries and partition pruning.
- A single results table can store results from multiple source tables. Use the
  `catalog_id`, `database_name`, and `table_name`
  partition columns to filter results for a specific source.
- AWS Glue Data Quality writes observation results asynchronously after the evaluation run completes.
  There might be a brief delay before observations appear in the table.
- For distribution statistics in the distribution results table, each bin or category is
  stored as a separate row. For example, a histogram with 20 bins generates 20 rows in the
  table for that statistic.
