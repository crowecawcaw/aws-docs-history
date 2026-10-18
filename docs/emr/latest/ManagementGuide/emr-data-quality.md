

# Amazon EMR Data Quality
<a name="emr-data-quality"></a>

Amazon EMR Data Quality, powered by [AWS Glue Data Quality](https://docs.aws.amazon.com/glue/latest/dg/glue-data-quality.html), lets you measure and monitor the quality of the data that your Amazon EMR Spark workloads read and write without leaving the Spark application. Amazon EMR Data Quality uses the same open-source [Deequ](https://github.com/awslabs/deequ) engine as AWS Glue Data Quality. Starting with the [AWS runtime for Apache Spark (`emr-spark-8.1.0`)](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark810-release.html) on Amazon EMR, you can evaluate data quality directly inside your Amazon EMR Spark applications by adding the `EvaluateDataQuality` transform to your Spark script. The transform runs a declarative ruleset against your DataFrame and returns the per-rule outcome in-process, so your application can act on the result (for example, aborting a downstream write when a rule fails). Each evaluation is also published to AWS Glue Data Quality, so you can review the history of your runs and alert on them alongside runs from AWS Glue ETL and the AWS Glue Data Catalog.

Using Amazon EMR Data Quality requires a Spark application and a ruleset written in Data Quality Definition Language (DQDL). No other programming is required beyond your existing Spark workflow.

Amazon EMR Data Quality is available on all three Amazon EMR deployment modes: Amazon EMR on EC2, [Amazon EMR on EKS](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-data-quality.html), and [Amazon EMR Serverless](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/emr-serverless-data-quality.html). It is supported for Apache Spark only.

**Topics**
+ [How Data Quality works](#emr-dq-how-it-works)
+ [Concepts and terminology](#emr-dq-concepts)
+ [Where to validate in your pipeline](#emr-dq-validation-stages)
+ [Limits](#emr-dq-limits)
+ [Getting started with Amazon EMR Data Quality](emr-dq-getting-started.md)
+ [Key capabilities](emr-dq-key-capabilities.md)
+ [Working with results](emr-dq-working-with-results.md)
+ [Monitoring and alerting](emr-dq-monitoring.md)
+ [Troubleshooting](emr-dq-troubleshooting.md)

## How Data Quality works
<a name="emr-dq-how-it-works"></a>

Amazon EMR Data Quality is a Spark transform. You pass it a DataFrame and a DQDL ruleset; it evaluates the rules and returns a DataFrame of outcomes. Each evaluation is also published to AWS Glue Data Quality so you can query the result later through the APIs or the AWS Glue console. AWS Glue ETL and the AWS Glue Data Catalog publish to the same store, so you can compare Amazon EMR runs with runs from either of those engines.

You define your data quality expectations as a declarative ruleset written in [Data Quality Definition Language (DQDL) reference](https://docs.aws.amazon.com/glue/latest/dg/dqdl.html). A ruleset is a set of rules that describe expected properties of a dataset. For example, the following ruleset checks that a table has more than 100 rows, that its `customer_id` column is complete and unique, and that the `country` column is drawn from a fixed set of values.

```
Rules = [
    RowCount > 100,
    IsComplete "customer_id",
    IsUnique "customer_id",
    ColumnValues "country" in ["US", "CA", "MX"]
]
```

At runtime, the `EvaluateDataQuality` transform reads your DataFrame, evaluates each rule with the same Deequ engine used by AWS Glue Data Quality and the AWS Glue Data Catalog, and returns the outcome (`Passed`, `Failed`, or `Error`) for every rule. Failed rules include the observed value so you can triage them without re-running the application. The result is a Spark DataFrame your application can branch on, log, or persist.

Data Quality also publishes each evaluation to the AWS Glue Data Quality service. From there you can:
+ Query historical results with the AWS Glue Data Quality APIs (`GetDataQualityResultV2`, `ListDataQualityResultsV2`, `BatchGetDataQualityResultV2`), the AWS CLI, or the AWS Glue console.
+ View the run in the AWS Glue console under the AWS Glue Data Catalog table it validated when your application sets `publishToDataCatalogTarget`. The run appears on the *Data quality* tab of the specified database and table, alongside AWS Glue ETL runs that target the same table.
+ Enable anomaly detection over the time series of statistics produced by each run.

Because results can be published to the same store used by AWS Glue Data Quality, you can correlate runs across compute engines. Runs that share an `EvaluationContext` (a string identifier that you pass to the transform) appear as a single logical dataset in the console and in anomaly-detection training, regardless of whether they came from an Amazon EMR Spark application or a AWS Glue ETL job.

## Concepts and terminology
<a name="emr-dq-concepts"></a>

The following terms appear throughout this chapter and in the AWS Glue Data Quality APIs and console.

Rule  
A single declarative assertion about a dataset, written in DQDL. For example, `RowCount > 1000` or `IsUnique "order_id"`. Each rule evaluates to `Passed`, `Failed`, or `Error`.

Ruleset  
A named collection of rules that are evaluated together in a single call to `EvaluateDataQuality`.

Analyzer  
A statistic that is computed for a dataset without asserting a pass or fail outcome, for example `Mean "order_total"`. Analyzers seed rule thresholds and train the anomaly-detection model. See [Analyzers](emr-dq-key-capabilities.md#emr-dq-analyzers).

Data quality score  
The percentage of rules in a ruleset that passed on a given run, computed as `rules passed / (rules passed + rules failed)`. Rules that error and observations do not contribute to the score. The score is returned by the AWS Glue Data Quality APIs and, when your application sets `publishToDataCatalogTarget`, surfaces in the AWS Glue console on the *Data quality* tab of the attributed catalog table.

Observation  
A value flagged by anomaly detection as outside its predicted range. Observations do not reduce the data quality score. See [Anomaly detection](emr-dq-key-capabilities.md#emr-dq-anomaly-detection).

`EvaluationContext`  
A string identifier that groups runs of the same logical dataset across compute engines. Runs that share an `EvaluationContext` feed the same anomaly-detection model and appear together in the AWS Glue console. See [Comparing runs across Amazon EMR and AWS Glue](emr-dq-working-with-results.md#emr-dq-compare-runs).

Publishing  
The step that writes the result of an `EvaluateDataQuality` run to the AWS Glue Data Quality service so it can be read later through the AWS Glue Data Quality APIs and the AWS Glue console. Publishing is enabled by default and controlled by the `enableDataQualityResultsPublishing` key in `publishing_options`. Each publish is keyed by `EvaluationContext`, the identifier that anomaly detection and cross-engine comparison use to group runs. When the application also sets `publishToDataCatalogTarget`, the run is attributed to a catalog table and appears in the *Data quality* tab of that table in the AWS Glue console.

DQDL  
Data Quality Definition Language, the declarative language used to author Data Quality rulesets. See [Rule evaluation and DQDL](emr-dq-key-capabilities.md#emr-dq-rule-evaluation).

## Where to validate in your pipeline
<a name="emr-dq-validation-stages"></a>

You can invoke `EvaluateDataQuality` anywhere in a Spark script. The three common patterns are:
+ **Pre-validation.** Evaluate the raw input immediately after reading. Use this to fail fast on upstream problems (missing files, schema drift, empty tables) before spending compute on the rest of the application.
+ **Inline validation.** Evaluate an intermediate DataFrame between transformations. Use this to check the output of a specific step (for example, after a join or aggregation).
+ **Post-validation.** Evaluate the final DataFrame before writing to your sink. Use this to gate a downstream publish on the result: branch on the `Outcome` column and abort the write if any rule failed.

The following PySpark snippet gates a write on the result of a post-validation evaluation.

```
results = EvaluateDataQuality.apply(
    frame=final_df,
    ruleset=ruleset,
    publishing_options={
        "dataQualityEvaluationContext": "orders_daily",
        "enableDataQualityResultsPublishing": True,
    },
)

failed = results.filter("Outcome in ('Failed', 'Error')").count()
if failed > 0:
    raise RuntimeError(f"{failed} data quality rules failed or errored; aborting write")

final_df.write.mode("overwrite").parquet("s3://{{amzn-s3-demo-bucket}}/orders_curated/")
```

## Limits
<a name="emr-dq-limits"></a>
+ A single ruleset can contain up to **2,000 rules**.
+ The serialized DQDL source of a ruleset must be no larger than **65 KB**.
+ Data Quality collects statistics when you create a rule or analyzer. There is no cost associated with storing these statistics. However, there is a limit of **100,000 statistics per account**, and these statistics will be retained for a maximum of **two years**.
+ Data Quality is supported for Apache Spark applications on Amazon EMR only. It does not run on Hive, Trino, Flink, or other non-Spark engines supported by Amazon EMR.