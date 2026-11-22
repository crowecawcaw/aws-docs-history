

# Data quality monitoring at the catalog and database level

With data quality monitoring at the catalog and database level, you define data quality checks once for a catalog or a database in the AWS Glue Data Catalog, or for a single table. AWS Glue Data Quality then evaluates every table in scope, including tables that you add later, on the cadence that you choose. Quality issues surface as your data changes, without per-table setup or manual runs, so you can catch bad data before it reaches downstream consumers.

You set up monitoring by creating a *data quality evaluation configuration* at the catalog or database level. For a table that needs different checks, you can also create a configuration at the table level. A configuration describes which tables to evaluate, what to evaluate them with, and when to evaluate them. You can use a built-in ruleset that AWS Glue provides to gather baseline statistics for every column, or provide your own Data Quality Definition Language (DQDL) ruleset to hold every table to the same quality standards.

You can use data quality monitoring at the catalog and database level to:
+ Gather baseline statistics, such as row counts, completeness, and value ranges, for every table in a database or catalog from a single configuration.
+ Cover new tables automatically as producers add them, without anyone remembering to set up checks.
+ Apply an organization-wide quality standard, such as "every table has at least one row and its key columns are at least 99% complete", to every table in scope.
+ Monitor a critical table more often, or with stricter rules, than the rest of its database.
+ Build a history of statistics that AWS Glue Data Quality anomaly detection uses to flag unexpected changes in your data.

Evaluation configurations evaluate data at rest, after it lands in your tables. They don't block or stop the jobs that write your data. To check data before it is loaded, use [Data quality for AWS Glue ETL jobs](glue-data-quality.md#glue-data-quality-for-etl).

You can create and manage evaluation configurations with the AWS Glue API, the AWS CLI, and the AWS SDKs. To set up your first configuration, see [Getting started with data quality monitoring at the catalog and database level](data-quality-catalog-monitoring-getting-started.md).

**Contents**
+ [How evaluation configurations work](#data-quality-catalog-monitoring-how-it-works)
  + [Levels and scope](#data-quality-catalog-monitoring-scope)
  + [When configurations overlap](#data-quality-catalog-monitoring-precedence)
  + [Triggers](#data-quality-catalog-monitoring-triggers)
  + [Rulesets](#data-quality-catalog-monitoring-rulesets)
    + [Built-in rulesets](#data-quality-catalog-monitoring-managed-rulesets)
    + [Your own rulesets](#data-quality-catalog-monitoring-custom-rulesets)
  + [Results](#data-quality-catalog-monitoring-results)
  + [Pausing a configuration](#data-quality-catalog-monitoring-pause)
+ [Supported tables](#data-quality-catalog-monitoring-supported-tables)
+ [Considerations and quotas](#data-quality-catalog-monitoring-considerations)
+ [Getting started with data quality monitoring at the catalog and database level](data-quality-catalog-monitoring-getting-started.md)
  + [Prerequisites](data-quality-catalog-monitoring-getting-started.md#data-quality-catalog-monitoring-gs-prereqs)
  + [Step 1: Create an IAM role for the configuration](data-quality-catalog-monitoring-getting-started.md#data-quality-catalog-monitoring-gs-role)
  + [Step 2: Create a data quality evaluation configuration](data-quality-catalog-monitoring-getting-started.md#data-quality-catalog-monitoring-gs-create)
  + [Step 3: View the results](data-quality-catalog-monitoring-getting-started.md#data-quality-catalog-monitoring-gs-results)
  + [More configuration examples](data-quality-catalog-monitoring-getting-started.md#data-quality-catalog-monitoring-gs-examples)
    + [Evaluate a whole catalog on a schedule](data-quality-catalog-monitoring-getting-started.md#data-quality-catalog-monitoring-gs-example-catalog-schedule)
    + [Evaluate tables that match a name pattern](data-quality-catalog-monitoring-getting-started.md#data-quality-catalog-monitoring-gs-example-pattern)
    + [Evaluate a table with your own rules](data-quality-catalog-monitoring-getting-started.md#data-quality-catalog-monitoring-gs-example-custom)
    + [Evaluate recent data only](data-quality-catalog-monitoring-getting-started.md#data-quality-catalog-monitoring-gs-example-preprocessing)
    + [Evaluate tables in Amazon S3 Tables](data-quality-catalog-monitoring-getting-started.md#data-quality-catalog-monitoring-gs-example-s3tables)
  + [Managing evaluation configurations](data-quality-catalog-monitoring-getting-started.md#data-quality-catalog-monitoring-gs-manage)
    + [List configurations](data-quality-catalog-monitoring-getting-started.md#data-quality-catalog-monitoring-gs-list)
    + [Update a configuration](data-quality-catalog-monitoring-getting-started.md#data-quality-catalog-monitoring-gs-update)
    + [Pause and resume a configuration](data-quality-catalog-monitoring-getting-started.md#data-quality-catalog-monitoring-gs-pause)
    + [Delete a configuration](data-quality-catalog-monitoring-getting-started.md#data-quality-catalog-monitoring-gs-delete)
  + [Example: Manage configurations with the AWS SDK for Python (Boto3)](data-quality-catalog-monitoring-getting-started.md#data-quality-catalog-monitoring-gs-python)
+ [Troubleshooting data quality monitoring at the catalog and database level](data-quality-catalog-monitoring-troubleshooting.md)
  + [Resolving missing evaluation runs for a table](data-quality-catalog-monitoring-troubleshooting.md#data-quality-catalog-monitoring-trouble-no-runs)
  + [Resolving failed evaluation runs](data-quality-catalog-monitoring-troubleshooting.md#data-quality-catalog-monitoring-trouble-failed-runs)
  + [Resolving errors when you create or update a configuration](data-quality-catalog-monitoring-troubleshooting.md#data-quality-catalog-monitoring-trouble-api-errors)

## How evaluation configurations work
<a name="data-quality-catalog-monitoring-how-it-works"></a>

An evaluation configuration combines the following settings:
+ **Scope** – The level that the configuration applies to (a catalog, a database, or a single table) and, optionally, a table name pattern that narrows the tables in scope.
+ **Ruleset** – What to evaluate each table with: a built-in ruleset (`SIMPLE` or `ADVANCED`) or a DQDL ruleset that you create.
+ **Triggers** – When to evaluate tables: once, on a schedule, when table metadata changes, or a combination of these.
+ **IAM role** – The role that AWS Glue Data Quality assumes to find the tables in scope and evaluate them.
+ **Run settings** (optional) – The same settings that you use for an on-demand evaluation run, such as the number of workers, the timeout, a preprocessing query, and options for publishing results and anomaly detection.

When a trigger fires, AWS Glue Data Quality finds the tables in scope and starts a data quality evaluation run for each one, using your role and run settings. Each run works like a run that you start with `StartDataQualityRulesetEvaluationRun`. Runs appear in your list of evaluation runs, count toward the same quotas, and store their results with each table.

### Levels and scope
<a name="data-quality-catalog-monitoring-scope"></a>

Each configuration applies to one level of the AWS Glue Data Catalog hierarchy. You identify the catalog, database, or table with the `GlueTables` data source. The following table describes each level.


| Level | Data source | Tables in scope | 
| --- | --- | --- | 
| CATALOG | CatalogId, and optionally TableNamePattern | Every table in every database of the catalog whose name matches the pattern | 
| DATABASE | CatalogId and DatabaseName, and optionally TableNamePattern | Every table in the database whose name matches the pattern | 
| TABLE | CatalogId, DatabaseName, and TableNamePattern set to the table name | The named table | 

`TableNamePattern` is a glob pattern, such as `orders_*`, that must match the whole table name. Matching isn't case sensitive. If you omit the pattern, every table at the selected level is in scope.

For tables in Amazon S3 Tables, set `CatalogId` to the Amazon S3 Tables catalog and `DatabaseName` to the namespace. For example, use `{{111122223333}}:s3tablescatalog/{{amzn-s3-demo-table-bucket}}` for a single table bucket, or `{{111122223333}}:s3tablescatalog` for every table bucket in the account.

The scope is evaluated each time a trigger fires, so tables that you add later are included automatically, and tables that you delete are no longer evaluated.

### When configurations overlap
<a name="data-quality-catalog-monitoring-precedence"></a>

A table can be in scope of configurations at more than one level. For example, a catalog-level configuration and a table-level configuration can both include the same table. When this happens, the most specific configuration applies:
+ A table-level configuration takes precedence over database-level and catalog-level configurations for that table.
+ A database-level configuration takes precedence over a catalog-level configuration for the tables that it includes.

The less specific configuration continues to evaluate all other tables in its scope. For example, you can evaluate every table in a catalog daily with the `SIMPLE` ruleset, and evaluate one critical table hourly with your own rules. The table-level configuration replaces the catalog-level configuration for that table only.

Precedence depends only on scope. A more specific configuration applies to its tables even when it is paused or uses different triggers. If a database-level configuration has a `TableNamePattern` that doesn't match a table, it doesn't include that table, and the catalog-level configuration still applies.

Avoid creating configurations at the same level with overlapping scopes. If two configurations at the same level include the same table, each table is still evaluated at most once an hour, and either configuration might start that evaluation.

### Triggers
<a name="data-quality-catalog-monitoring-triggers"></a>

Triggers control when a configuration evaluates the tables in scope. You can choose one or more of the following triggers. If you don't specify triggers, the default is `ONCE`.

ONCE  
Evaluates every table in scope one time, starting about a minute after you create the configuration. Tables that you add to the database or catalog later are each evaluated once when they are created. Updating the configuration doesn't evaluate the tables again.

SCHEDULE  
Evaluates every table in scope on a schedule that you define with `ScheduleExpression`. You can use a cron expression, such as `cron(0 6 * * ? *)` for 6:00 AM every day, or a rate expression, such as `rate(12 hours)`. Schedules use Coordinated Universal Time (UTC) and can run at most once an hour. Use `StartAt` and `EndAt` to limit the schedule to a time window.

METADATA\_CHANGE  
Evaluates a table when its metadata in the AWS Glue Data Catalog changes. Metadata changes include:  
+ Schema changes, such as added or removed columns, whether you make them directly or a crawler makes them.
+ Table property updates, which can include row count parameters that some engines write.
+ Storage format changes, such as from JSON to Parquet.
+ Apache Iceberg commits. Each commit updates the table's metadata location, so every commit counts as a metadata change.
Writing new files to Amazon S3 without updating the table, and adding or changing partitions, don't count as metadata changes. If your Iceberg tables are written to frequently, consider a `SCHEDULE` trigger instead to control cost.

Keep the following in mind when you choose triggers:
+ **New tables** – When a table is created in a database or catalog that a configuration applies to, the configuration evaluates the new table, whichever triggers you choose. For a `SCHEDULE`-only configuration, this happens only between `StartAt` and `EndAt`.
+ **Hourly limit** – Each table is evaluated at most once an hour. This limit applies across all of your configurations and triggers. If a trigger fires less than an hour after a configuration last evaluated a table, AWS Glue Data Quality skips that table until the next trigger. Evaluation runs that you start yourself aren't affected.

### Rulesets
<a name="data-quality-catalog-monitoring-rulesets"></a>

Each configuration evaluates tables with one ruleset. Specify either `ManagedRulesetName` for a built-in ruleset or `RulesetName` for a ruleset that you create. If you specify neither, the configuration uses the `SIMPLE` built-in ruleset.

#### Built-in rulesets
<a name="data-quality-catalog-monitoring-managed-rulesets"></a>

Built-in rulesets contain analyzers that gather statistics about every table and column, without rules that pass or fail. These statistics give you a baseline profile of each table and feed anomaly detection. The following table lists the built-in rulesets and the statistics that each one gathers.


| Ruleset | Statistics | 
| --- | --- | 
| SIMPLE (default) | `RowCount` and `ColumnCount` for each table, and `Completeness`, minimum and maximum values, `ColumnLength`, `Mean`, `Sum`, and `StandardDeviation` for each column, where the column type supports the statistic.<br />These analyzers don't need to shuffle data, so `SIMPLE` is the lowest-cost option. | 
| ADVANCED | Every statistic in `SIMPLE`, plus `Uniqueness`, `Entropy`, `DistinctValuesCount`, and `Distribution` for each column.<br />These additional analyzers shuffle data, so they cost more, especially on columns with many distinct values. | 

The first time a configuration uses a built-in ruleset, AWS Glue creates it in your account as a data quality ruleset named `SIMPLE-DataQualityEvaluationConfigManagedRuleset` or `ADVANCED-DataQualityEvaluationConfigManagedRuleset`. All configurations in the account share it. Don't edit these rulesets. AWS Glue restores their definitions before each evaluation.

Because built-in rulesets contain only analyzers, they don't produce rule results or row-level results. To use the `DataQualityRuleResults` or `RowLevelResults` run options, use your own ruleset.

For more information about these statistics, see [DQDL rule type reference](dqdl-rule-types.md) and [Distribution Analyzer](dqdl.md#dqdl-analyzers-distribution).

#### Your own rulesets
<a name="data-quality-catalog-monitoring-custom-rulesets"></a>

To evaluate tables against your own standards, create a DQDL ruleset with the `CreateDataQualityRuleset` API and specify its name in `RulesetName`. Your ruleset can contain rules, analyzers, or both. Rules produce a data quality score and pass or fail results. Analyzers gather statistics that feed anomaly detection.

A ruleset in a catalog-level or database-level configuration runs against tables with different schemas. A rule that references a column that doesn't exist in a table fails for that table. For broad configurations, use rules that apply to any table, such as `RowCount > 0`, `ColumnCount > 0`, or rules on columns that all of your tables share. Put table-specific rules in table-level configurations.

The configuration evaluates the current definition of your ruleset each time it runs. If you delete the ruleset, the configuration stops evaluating tables until you update it with a ruleset that exists.

### Results
<a name="data-quality-catalog-monitoring-results"></a>

Each evaluation stores its results with the table in the AWS Glue Data Catalog, the same as results from evaluation runs that you start yourself. To find results from your configurations, use the following fields in the AWS Glue API:
+ `EvaluationRunMode` – How the evaluation run that produced the result started. The value is `EVALUATION_CONFIG` for runs that a configuration started and `ON_DEMAND` for runs that you started with `StartDataQualityRulesetEvaluationRun`.
+ `DataQualityEvaluationConfig` – The name of the configuration that started the run.

`GetDataQualityResult`, `BatchGetDataQualityResult`, and `ListDataQualityResults` return both fields, and you can filter `ListDataQualityResults` on either field. Results from AWS Glue ETL jobs and other sources that don't use evaluation runs don't include `EvaluationRunMode`.

Because each evaluation is an evaluation run, the rest of AWS Glue Data Quality works with these results as usual:
+ Statistics are available through `ListDataQualityStatistics`.
+ Anomaly detection learns from the statistics of each table and flags values that drift outside their expected range after at least three evaluations. Anomaly detection is on by default. To turn it off, set `ObservationScope` to `NONE` in the configuration's `AdditionalRunOptions`. For more information, see [Anomaly detection in AWS Glue Data Quality](data-quality-anomaly-detection.md).
+ Amazon EventBridge receives an event when each run's results are available. For more information, see [Setting up alerts and notifications in Amazon EventBridge integration](data-quality-alerts.md#data-quality-alerts-eventbridge).
+ You can write results to Amazon S3 or to AWS Glue Data Catalog tables by setting the same `AdditionalRunOptions` that you use for on-demand runs. For more information, see [Writing data quality results to Data Catalog tables](data-quality-results-catalog-tables.md).

If you use Lake Formation, results for a table are governed by your table permissions.

### Pausing a configuration
<a name="data-quality-catalog-monitoring-pause"></a>

To stop a configuration temporarily without deleting it, call `UpdateDataQualityEvaluationConfig` with `PauseRuns` set to `true`. While a configuration is paused, it evaluates nothing, including tables that you add to the catalog or database. To resume, set `PauseRuns` to `false`. The configuration continues with its existing triggers. Evaluations that were missed while the configuration was paused aren't run later.

You can pause only configurations that include the `SCHEDULE` or `METADATA_CHANGE` trigger. If a configuration is paused when its `ONCE` evaluation is due, that evaluation is skipped and doesn't run when you resume.

## Supported tables
<a name="data-quality-catalog-monitoring-supported-tables"></a>

Evaluation configurations evaluate native AWS Glue Data Catalog tables, including:
+ Apache Hive tables on Amazon S3
+ Apache Iceberg tables on Amazon S3 and in Amazon S3 Tables
+ Amazon Athena views

Configurations skip the following tables in their scope:
+ Tables in federated catalogs that connect over JDBC, such as Snowflake, Google BigQuery, or Amazon Redshift through federation
+ Tables that use a JDBC connection
+ Tables that are multi-dialect Data Catalog views, or views other than Amazon Athena views

## Considerations and quotas
<a name="data-quality-catalog-monitoring-considerations"></a>

Consider the following before you create evaluation configurations:
+ **Quotas** – You can create up to 1,000 evaluation configurations in each AWS account and Region. Configuration names must be unique within your account in each Region.
+ **Concurrent runs** – Evaluation runs that configurations start count toward your account's quota of concurrent data quality evaluation runs. Configurations start new runs only while capacity remains under that quota, so you keep room for runs that you start yourself. When many tables are waiting, for example after you add 1,000 tables to a database, AWS Glue Data Quality evaluates them as capacity becomes available, starting with the most recently updated tables.
+ **Statistics** – Statistics that configurations gather count toward your account's quota of stored statistics. For more information, see [Limits](glue-data-quality.md#data-quality-limits).
+ **Cost** – There is no charge for evaluation configurations. Each evaluation run is billed at standard AWS Glue Data Quality DPU-hour pricing. To control cost, limit the tables in scope with `TableNamePattern`, use a `PreProcessingQuery` to evaluate a subset of each table, choose the `SIMPLE` ruleset for broad configurations, and choose triggers that match how often your data changes. For pricing, see [AWS Glue pricing](https://aws.amazon.com/glue/pricing).
+ **Preprocessing queries** – A `PreProcessingQuery` in a catalog-level or database-level configuration runs against many tables. Use the `{{DATABASE_NAME}}` and `{{TABLE_NAME}}` placeholders, which AWS Glue Data Quality replaces with each table's database and table name. For more information, see [Using preprocessing queries](data-quality-getting-started.md#data-quality-preprocessing-queries).
+ **Timing** – Evaluations start asynchronously. A `ONCE` evaluation starts about a minute after you create the configuration, and evaluations for new tables and metadata changes typically start within a few minutes of the change. Runs can start later when your account is near its concurrent run quota.
+ **Lake Formation** – If you use Lake Formation, the configuration's role evaluates only the tables that it has the `DESCRIBE` permission on. Tables that the role can't describe are skipped. For tables whose data Lake Formation manages, such as Amazon S3 Tables, the evaluation run also reads the data through Lake Formation, so the role needs the `SELECT` permission on each table, without column or data filters. Without it, the table's evaluation runs fail.
+ **Catalogs** – Each configuration applies to one catalog in your account. To monitor more than one catalog, create a configuration for each catalog.