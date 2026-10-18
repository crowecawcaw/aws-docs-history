

# Key capabilities
<a name="emr-dq-key-capabilities"></a>

The capabilities below are available to any Amazon EMR Spark application that uses the `EvaluateDataQuality` transform. All of them behave the same on Amazon EMR as on AWS Glue; the sections that follow summarize each one and link to the detailed reference in the *AWS Glue Developer Guide*.

## Rule evaluation and DQDL
<a name="emr-dq-rule-evaluation"></a>

You author rulesets in DQDL, the declarative language that Amazon EMR Data Quality uses to describe data quality expectations. The transform supports more than 30 built-in rule types spanning completeness, uniqueness, value constraints, aggregations, freshness, schema shape, and pattern matching, and lets you combine them with boolean operators, thresholds, and `with` clauses that filter the rows a rule applies to. The grammar is identical on Amazon EMR and on AWS Glue.

For the full rule catalog, parameter reference, and worked examples, see [Data Quality Definition Language (DQDL) reference](https://docs.aws.amazon.com/glue/latest/dg/dqdl.html) in the *AWS Glue Developer Guide*.

## Analyzers
<a name="emr-dq-analyzers"></a>

*Analyzers* compute statistics about your dataset without asserting a pass/fail outcome. They are useful for exploring a new dataset, for seeding thresholds on a rule, and for training the anomaly-detection model. You declare them in the `Analyzers` block of a ruleset.

```
Rules = [
    RowCount > 1000
]

Analyzers = [
    RowCount,
    Completeness "customer_id",
    Uniqueness "customer_id",
    DistinctValuesCount "country",
    Mean "order_total"
]
```

Each analyzer value is written to the results store as a time series, keyed by the `EvaluationContext`, and is available to the anomaly-detection model. The same set of analyzers is supported on Amazon EMR and on AWS Glue.

For the full analyzer catalog and parameter reference, see [Analyzers](https://docs.aws.amazon.com/glue/latest/dg/dqdl-anomalydetection.html#dqdl-analyzers) in the *AWS Glue Developer Guide*.

## Anomaly detection
<a name="emr-dq-anomaly-detection"></a>

Anomaly detection learns the trend and seasonality of a statistic from its own history and flags runs where the observed value falls outside the expected range, without you having to re-tune thresholds by hand. Every time your Amazon EMR Spark application runs Data Quality with publishing enabled, the values of each rule metric and each analyzer statistic are appended to a per-statistic time series, keyed by `EvaluationContext`. The model trains on that time series, predicts the expected range for the next run, and emits an *observation* when the observed value falls outside that range.

To enable anomaly detection on an Amazon EMR run, set `observations.scope` to `ALL` in `additional_options`, and keep `enableDataQualityResultsPublishing` set to `true`. The `observations.scope` option tells the transform which analyzers in your ruleset produce observations; `ALL` scores every published statistic.

For the detection algorithm, mode selection, feedback workflow, and recommendation types, see [Anomaly detection](https://docs.aws.amazon.com/glue/latest/dg/data-quality-anomaly-detection.html) in the *AWS Glue Developer Guide*. The anomaly-detection engine and algorithm are shared between Amazon EMR Data Quality and AWS Glue Data Quality. For Amazon EMR runs, the time series of statistics and the anomaly observations are visible in the AWS Glue console on the *Data quality* tab of the AWS Glue Data Catalog table only when your application sets `publishToDataCatalogTarget`. Without catalog attribution, retrieve the statistic time series through `ListDataQualityStatistics` and the anomaly observations through `ListDataQualityStatisticAnnotations`.

## Dynamic rules
<a name="emr-dq-dynamic-rules"></a>

*Dynamic rules* compare the current value of a statistic to the history of that statistic for previous runs of the same `EvaluationContext`. This lets you write rules such as "row count should be within 10 percent of last run" without hard-coding a threshold. Unlike anomaly detection, which learns expected ranges from history automatically, dynamic rules require you to define the comparison logic explicitly in your ruleset. Dynamic rules require that publishing was enabled on prior runs so that the history exists.

```
Rules = [
    RowCount between last(1) * 0.9 and last(1) * 1.1,
    Mean "order_total" between avg(last(7)) - 2 * std(last(7))
                          and avg(last(7)) + 2 * std(last(7))
]
```

For the full dynamic-rule syntax and supported functions, see [Dynamic rules](https://docs.aws.amazon.com/glue/latest/dg/dqdl.html#dqdl-dynamic-rules) in the *AWS Glue Developer Guide*.