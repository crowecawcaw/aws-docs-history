# Enable Data Quality Validation

You can enable data quality checks by providing both source and target cluster IDs in your prompt. The system runs your existing application on the source cluster to collect baseline metadata for comparison.

**Note: Only Spark write operations can be tracked for data quality.**

```
Upgrade my pyspark application <local-path>/pyspark-example-24/ from EMR version 6.0.0 to 7.12.0. Use EMR-EC2 Cluster <source-cluster-id> for source version run
and <target-cluster-id> for target version run. Use s3 path s3://<please fill in your staging bucket path> to store updated application artifacts
and s3://<please fill in your staging bucket path>/metadata for storing metadata. Enable data quality checks.
```

## Data Quality Workflow Differences

The workflow follows the same steps as the standard upgrade process with these additional steps in the order above:

- **[After Step 3: Plan Review and Customization]**
  - **Build with Current Configuration**: Build the application with current configuration for source cluster submission.
  - **Validate on Source EMR Cluster**: Run original application on source Spark version and collect output metadata for baseline comparison.

- **[After Step 7: Summary for the upgrade] Data Quality Summary**: Data quality comparison report between versions and analysis.

### Data quality mismatch capability currently includes:

- **Schema Checks**: Detects changes in column structure: missing or newly added columns, data type differences, and nullability changes.
- **Value Checks** _(numeric and string columns only)_
  - Compares min, max, and mean (mean only for numeric columns).
  - For strings, min and max are based on lexicographical order.

- **Aggregated Statistical Checks**: Compares total row counts between source and target outputs.

## Data Quality Validation: Scope and Limitations

Data Quality Validation supports EMR-EC2 step using spark-submit command with Spark version >= 3.0 and the EMR cluster cannot have StepConcurrencyLevel > 1. The Data Quality Validation evaluates statistics at the Spark query plan's data sink nodes (Data source/Transforms's metadata are not captured) and covers common Spark write operations including file writes, database inserts, table creation, and various data source outputs.
