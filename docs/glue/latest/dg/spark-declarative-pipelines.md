# Spark Declarative Pipelines

Spark Declarative Pipelines (SDP) is a declarative framework for building batch and
streaming data pipelines in AWS Glue 6.0. With SDP, you define what your data should look
like using SQL or Python, and the framework automatically determines the execution plan,
resolves dependencies between datasets, and runs independent branches in parallel.

SDP simplifies pipeline development by eliminating imperative boilerplate code for
reading, writing, catalog registration, and execution ordering. You focus on business
transformations while the framework handles the pipeline infrastructure.

SDP is available in AWS Glue version 6.0 and later.

## SDP concepts

A pipeline consists of a YAML manifest file
(`spark-pipeline.yml`) and one or more SQL or Python transformation
files. SDP automatically:

- Resolves dependencies by inferring the DAG from table references
- Determines execution order without manual orchestration
- Runs independent branches in parallel for maximum throughput
- Manages incremental state for streaming tables through checkpoints
- Registers output tables in the catalog upon materialization

### Dataset types

Three dataset types are available in SDP:

Streaming table

Processes only new data since the last run. Maintains state across
job executions using checkpoints. Use streaming tables for ingestion,
event streams, IoT data, change data capture, and append-only
sources.

Materialized view

Fully recomputes the dataset on every run. The output always reflects
the current state of source data. Use materialized views for
aggregations, joins, summary analytics, and reports.

Temporary view

Session-scoped and not persisted or cataloged. Use temporary views
for intermediate transformations and staging logic.

###### Important

Materialized views always perform a full recompute in the current version.
They do not support incremental refresh. Use streaming tables for incremental
workloads.

## Prerequisites

To use SDP, you need the following:

- AWS Glue version 6.0
- An Amazon S3 location for pipeline storage (checkpoints, metadata)
- For Data Catalog integration (optional): set
  `--enable-glue-datacatalog` to `true`. Alternatively,
  you can configure catalog settings directly through Spark configuration.
- For persistent table storage: either set
  `spark.sql.warehouse.dir` to an Amazon S3 path, or set the
  `database:` field in the pipeline YAML and ensure the AWS Glue
  database has a `LocationUri` configured to an Amazon S3 path
- For cross-run incremental processing with streaming tables: use Iceberg
  tables (Hive-managed streaming tables do not support cross-run incremental
  processing)

###### Important

If you use the `database:` field in your pipeline YAML, the
corresponding AWS Glue database must have its `LocationUri` set to an
Amazon S3 path. Databases created through the console often have an empty
`LocationUri`. Create or update the database with an explicit Amazon S3
location:

```
aws glue create-database --database-input '{
  "Name":"my_pipeline_db",
  "LocationUri":"s3://my-bucket/warehouse/my_pipeline_db"
}'
```

## Creating a pipeline

To create an SDP pipeline, complete the following steps.

### Step 1: Create the pipeline YAML

Create a file named `spark-pipeline.yml`:

```
name: my_analytics_pipeline
catalog: spark_catalog
database: analytics_db
storage: s3://my-bucket/pipeline-storage/
libraries:
  - glob:
      include: transformations/**
configuration:
  spark.sql.shuffle.partitions: "4"
```

The following table describes the pipeline YAML fields.

| Field           | Required | Description                                                                                     |
| --------------- | -------- | ----------------------------------------------------------------------------------------------- |
| `name`          | Yes      | A name for your pipeline.                                                                       |
| `catalog`       | No       | The catalog to use. Defaults to<br>`spark_catalog`.                                             |
| `database`      | No       | The target database for output tables. The database must exist<br>and have a `LocationUri` set. |
| `storage`       | Yes      | An Amazon S3 path for pipeline checkpoints and metadata.                                        |
| `libraries`     | Yes      | Glob patterns for transformation files to include.                                              |
| `configuration` | No       | Spark configuration properties.                                                                 |

### Step 2: Write transformations

Create transformation files in a `transformations/`
directory. You can use SQL, Python, or both in the same pipeline.

**SQL example**
(`transformations/silver.sql`):

```
CREATE MATERIALIZED VIEW silver_sales AS
SELECT *, UPPER(region) as clean_region
FROM bronze_sales
WHERE amount > 0;

CREATE MATERIALIZED VIEW gold_summary AS
SELECT clean_region, COUNT(*) as order_count, SUM(amount) as total_revenue
FROM silver_sales
GROUP BY clean_region;
```

**Python example**
(`transformations/bronze.py`):

```
from pyspark import pipelines as dp
from pyspark.sql import DataFrame, SparkSession

spark = SparkSession.active()

@dp.materialized_view(comment="Raw sales data from S3")
def bronze_sales() -> DataFrame:
    return spark.read.format("csv").option("header", "true") \
        .option("inferSchema", "true") \
        .load("s3://source-bucket/raw-data/sales/")
```

**Python streaming table example**
(`transformations/events.py`):

```
from pyspark import pipelines as dp
from pyspark.sql import DataFrame, SparkSession

spark = SparkSession.active()

dp.create_streaming_table(
    "streaming_events",
    comment="Incremental event ingestion",
    schema="event_id STRING, event_type STRING, timestamp LONG, payload STRING"
)

@dp.append_flow(target="streaming_events")
def ingest_events() -> DataFrame:
    return (
        spark.readStream.format("json")
        .schema("event_id STRING, event_type STRING, timestamp LONG, payload STRING")
        .load("s3://source-bucket/events/")
    )
```

###### Note

For streaming tables in Python, use
`dp.create_streaming_table()` combined with
`@dp.append_flow(target=...)`. The
`@dp.streaming_table` decorator is not available.

### Step 3: Upload to Amazon S3

Upload your pipeline files to Amazon S3 as either:

- A `.zip` file containing
  `spark-pipeline.yml` and the
  `transformations/` directory
- An Amazon S3 prefix (directory) containing the same structure

### Step 4: Create and run the AWS Glue job

Create a AWS Glue job with the following parameters:

- `--enable-spark-declarative-pipeline`:
  `true` (required — activates SDP mode)
- `ScriptLocation`: pipeline definition zip or an Amazon S3 prefix
  (required for SDP pipeline)
- `--enable-glue-datacatalog`: `true`
  (optional — registers tables in Data Catalog)

The following example creates an SDP job using the AWS CLI:

```
aws glue create-job \
  --name my-sdp-pipeline \
  --role arn:aws:iam::123456789012:role/MyGlueRole \
  --glue-version 6.0 \
  --worker-type G.1X --number-of-workers 2 \
  --command '{"Name":"glueetl","ScriptLocation":"s3://my-bucket/pipelines/my_pipeline.zip"}' \
  --default-arguments '{
      "--enable-spark-declarative-pipeline": "true",
      "--enable-glue-datacatalog": "true"
  }'
```

## Running pipelines

You run SDP pipelines using `StartJobRun`. You can control execution
behavior with job arguments passed at run time.

### Run modes

Pass the following arguments to `StartJobRun` to control pipeline execution:

`--conf spark.glue.sdp.jobMode`

Controls the execution mode:

- `RUN` (default) — Executes the pipeline normally.
- `VALIDATE` — Performs a dry run that checks YAML syntax,
  dependency resolution, and SQL/Python compilation without writing any data.

`--conf spark.glue.sdp.runMode`

Controls which datasets are refreshed:

`--refresh`

Runs all datasets. Materialized views fully recompute. Streaming tables
process only new data since the last checkpoint.

`--refresh <dataset_name>`

Runs only the specified dataset. For streaming tables, this processes
new data incrementally. For materialized views, this performs a full
recompute of that view only.

`--full-refresh`

Resets and recomputes all datasets. For streaming tables, this resets
checkpoints and reprocesses all data from scratch.

`--full-refresh-all`

Drops all tables and reprocesses the entire pipeline from
scratch.

## Using Iceberg tables with SDP

For streaming tables that require cross-run incremental processing, use Apache
Iceberg. Hive-managed streaming tables store metadata locally and do not persist
across job runs.

To configure Iceberg, add the following to your
`spark-pipeline.yml` configuration section:

```
configuration:
  spark.sql.catalog.spark_catalog: "org.apache.iceberg.spark.SparkSessionCatalog"
  spark.sql.catalog.spark_catalog.type: "hadoop"
  spark.sql.catalog.spark_catalog.warehouse: "s3://my-bucket/iceberg-warehouse"
```

With Iceberg configured, you get the following benefits:

- Streaming tables maintain checkpoint state in Amazon S3 across job runs
- Each run creates new data files and Iceberg snapshots
- Subsequent runs resume from the last committed offset
- Full table history is preserved through Iceberg's snapshot mechanism

## Considerations and limitations

Consider the following when you use SDP:

- **Materialized views always fully
  recompute** — Incremental refresh is not supported. Use streaming
  tables for incremental workloads.
- **Streaming table Python API** — Use
  `dp.create_streaming_table()` with
  `@dp.append_flow(target=...)`. The
  `@dp.streaming_table` decorator is not available in the current
  version.
- **Cross-run incremental processing requires
  Iceberg** — Streaming tables with Hive or AWS Glue managed catalog do
  not support incremental processing across job runs. Use Iceberg tables for
  persistent incremental state.
- **Database LocationUri required** — If you
  specify a `database:` in your pipeline YAML, the AWS Glue database
  must have its `LocationUri` set to an Amazon S3 path. Without it, the
  pipeline fails.
- **Data quality expectations** — Inline data
  quality annotations are not supported in the current SDP framework.
- **Avoid `withColumn` in downstream query
  functions** — When a downstream dataset (such as a materialized view)
  reads from an upstream pipeline dataset using `spark.table(...)` and
  applies `.withColumn(...)`, SDP might fail to detect the dependency
  between the datasets on the second and subsequent runs. This causes the
  downstream to read stale data from the previous run (one-run lag). To avoid this
  issue, express derived columns inside `.select(...)` instead of using
  `.withColumn(...)`. Also avoid any operation that forces plan
  resolution (such as `.schema` or `.collect`) inside query
  functions.
- **No migration tooling** — Automated
  migration from other pipeline frameworks is not supported. Migrate tables
  incrementally — SDP can read from existing catalog tables.
- **Scheduling** — SDP jobs use the same
  scheduling mechanisms as other AWS Glue jobs (AWS Glue Triggers, Amazon
  EventBridge, Apache Airflow).

## Migrating from imperative scripts to SDP

You can migrate existing imperative Spark scripts to SDP incrementally:

1. Start with one table — convert a single
   `spark.sql(...).write.saveAsTable(...)` call into a
   `CREATE MATERIALIZED VIEW` SQL statement.
2. Add tables incrementally — SDP handles mixed dependencies. SDP tables
   can read from existing catalog tables that are not part of the
   pipeline.
3. Run both patterns in parallel during transition — SDP jobs and imperative
   jobs can coexist.

SDP can reference any table accessible through the SparkSession, including
existing Data Catalog tables, external tables, and cross-database references.
