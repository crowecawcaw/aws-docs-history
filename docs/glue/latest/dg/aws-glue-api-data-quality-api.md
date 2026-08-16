# Data Quality API

The Data Quality API describes the data quality data types, and includes
the API for creating, deleting, or updating data quality rulesets, runs and evaluations.

## Data types

- [DataSource structure](#aws-glue-api-data-quality-api-DataSource "#aws-glue-api-data-quality-api-DataSource")
- [DataQualityRulesetListDetails structure](#aws-glue-api-data-quality-api-DataQualityRulesetListDetails "#aws-glue-api-data-quality-api-DataQualityRulesetListDetails")
- [DataQualityTargetTable structure](#aws-glue-api-data-quality-api-DataQualityTargetTable "#aws-glue-api-data-quality-api-DataQualityTargetTable")
- [DataQualityRulesetEvaluationRunDescription structure](#aws-glue-api-data-quality-api-DataQualityRulesetEvaluationRunDescription "#aws-glue-api-data-quality-api-DataQualityRulesetEvaluationRunDescription")
- [DataQualityRulesetEvaluationRunFilter structure](#aws-glue-api-data-quality-api-DataQualityRulesetEvaluationRunFilter "#aws-glue-api-data-quality-api-DataQualityRulesetEvaluationRunFilter")
- [DataQualityEvaluationRunAdditionalRunOptions structure](#aws-glue-api-data-quality-api-DataQualityEvaluationRunAdditionalRunOptions "#aws-glue-api-data-quality-api-DataQualityEvaluationRunAdditionalRunOptions")
- [DataQualityRuleRecommendationRunDescription structure](#aws-glue-api-data-quality-api-DataQualityRuleRecommendationRunDescription "#aws-glue-api-data-quality-api-DataQualityRuleRecommendationRunDescription")
- [DataQualityRuleRecommendationRunFilter structure](#aws-glue-api-data-quality-api-DataQualityRuleRecommendationRunFilter "#aws-glue-api-data-quality-api-DataQualityRuleRecommendationRunFilter")
- [DataQualityResult structure](#aws-glue-api-data-quality-api-DataQualityResult "#aws-glue-api-data-quality-api-DataQualityResult")
- [DataQualityAnalyzerResult structure](#aws-glue-api-data-quality-api-DataQualityAnalyzerResult "#aws-glue-api-data-quality-api-DataQualityAnalyzerResult")
- [DataQualityObservation structure](#aws-glue-api-data-quality-api-DataQualityObservation "#aws-glue-api-data-quality-api-DataQualityObservation")
- [MetricBasedObservation structure](#aws-glue-api-data-quality-api-MetricBasedObservation "#aws-glue-api-data-quality-api-MetricBasedObservation")
- [DataQualityMetricValues structure](#aws-glue-api-data-quality-api-DataQualityMetricValues "#aws-glue-api-data-quality-api-DataQualityMetricValues")
- [DataQualityRuleResult structure](#aws-glue-api-data-quality-api-DataQualityRuleResult "#aws-glue-api-data-quality-api-DataQualityRuleResult")
- [DataQualityResultDescription structure](#aws-glue-api-data-quality-api-DataQualityResultDescription "#aws-glue-api-data-quality-api-DataQualityResultDescription")
- [DataQualityResultFilterCriteria structure](#aws-glue-api-data-quality-api-DataQualityResultFilterCriteria "#aws-glue-api-data-quality-api-DataQualityResultFilterCriteria")
- [DataQualityRulesetFilterCriteria structure](#aws-glue-api-data-quality-api-DataQualityRulesetFilterCriteria "#aws-glue-api-data-quality-api-DataQualityRulesetFilterCriteria")
- [DataQualityAggregatedMetrics structure](#aws-glue-api-data-quality-api-DataQualityAggregatedMetrics "#aws-glue-api-data-quality-api-DataQualityAggregatedMetrics")
- [StatisticAnnotation structure](#aws-glue-api-data-quality-api-StatisticAnnotation "#aws-glue-api-data-quality-api-StatisticAnnotation")
- [TimestampedInclusionAnnotation structure](#aws-glue-api-data-quality-api-TimestampedInclusionAnnotation "#aws-glue-api-data-quality-api-TimestampedInclusionAnnotation")
- [AnnotationError structure](#aws-glue-api-data-quality-api-AnnotationError "#aws-glue-api-data-quality-api-AnnotationError")
- [DatapointInclusionAnnotation structure](#aws-glue-api-data-quality-api-DatapointInclusionAnnotation "#aws-glue-api-data-quality-api-DatapointInclusionAnnotation")
- [StatisticSummaryList list](#aws-glue-api-data-quality-api-StatisticSummaryList "#aws-glue-api-data-quality-api-StatisticSummaryList")
- [StatisticSummary structure](#aws-glue-api-data-quality-api-StatisticSummary "#aws-glue-api-data-quality-api-StatisticSummary")
- [RunIdentifier structure](#aws-glue-api-data-quality-api-RunIdentifier "#aws-glue-api-data-quality-api-RunIdentifier")
- [StatisticModelResult structure](#aws-glue-api-data-quality-api-StatisticModelResult "#aws-glue-api-data-quality-api-StatisticModelResult")
- [DataQualityGlueTable structure](#aws-glue-api-data-quality-api-DataQualityGlueTable "#aws-glue-api-data-quality-api-DataQualityGlueTable")
- [DataQualityRuleRecommendationRunAdditionalRunOptions structure](#aws-glue-api-data-quality-api-DataQualityRuleRecommendationRunAdditionalRunOptions "#aws-glue-api-data-quality-api-DataQualityRuleRecommendationRunAdditionalRunOptions")
- [DataQualityRuleResultsOptions structure](#aws-glue-api-data-quality-api-DataQualityRuleResultsOptions "#aws-glue-api-data-quality-api-DataQualityRuleResultsOptions")
- [DistributionData structure](#aws-glue-api-data-quality-api-DistributionData "#aws-glue-api-data-quality-api-DistributionData")
- [ObservationResultsOptions structure](#aws-glue-api-data-quality-api-ObservationResultsOptions "#aws-glue-api-data-quality-api-ObservationResultsOptions")
- [ProfilingResultsOptions structure](#aws-glue-api-data-quality-api-ProfilingResultsOptions "#aws-glue-api-data-quality-api-ProfilingResultsOptions")
- [RowLevelResultsOptions structure](#aws-glue-api-data-quality-api-RowLevelResultsOptions "#aws-glue-api-data-quality-api-RowLevelResultsOptions")
- [CatalogTableConfigOptions structure](#aws-glue-api-data-quality-api-CatalogTableConfigOptions "#aws-glue-api-data-quality-api-CatalogTableConfigOptions")
- [DistributionResultsOptions structure](#aws-glue-api-data-quality-api-DistributionResultsOptions "#aws-glue-api-data-quality-api-DistributionResultsOptions")

## DataSource structure

A data source (an AWS Glue table) for which you want data quality
results.

###### Fields

- `GlueTable` – A [GlueTable](aws-glue-api-machine-learning-api.md#aws-glue-api-machine-learning-api-GlueTable "aws-glue-api-machine-learning-api.md#aws-glue-api-machine-learning-api-GlueTable") object.

An AWS Glue table.

- `DataQualityGlueTable` – A [DataQualityGlueTable](#aws-glue-api-data-quality-api-DataQualityGlueTable "#aws-glue-api-data-quality-api-DataQualityGlueTable") object.

An AWS Glue table for Data Quality Operations.

## DataQualityRulesetListDetails structure

Describes a data quality ruleset returned by `GetDataQualityRuleset`.

###### Fields

- `Name` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the data quality ruleset.

- `Description` – Description string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

A description of the data quality ruleset.

- `CreatedOn` – Timestamp.

The date and time the data quality ruleset was created.

- `LastModifiedOn` – Timestamp.

The date and time the data quality ruleset was last modified.

- `TargetTable` – A [DataQualityTargetTable](#aws-glue-api-data-quality-api-DataQualityTargetTable "#aws-glue-api-data-quality-api-DataQualityTargetTable") object.

An object representing an AWS Glue table.

- `RecommendationRunId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

When a ruleset was created from a recommendation run, this run ID is generated
to link the two together.

- `RuleCount` – Number (integer).

The number of rules in the ruleset.

## DataQualityTargetTable structure

An object representing an AWS Glue table.

###### Fields

- `TableName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the AWS Glue table.

- `DatabaseName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the database where the AWS Glue table exists.

- `CatalogId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The catalog id where the AWS Glue table exists.

## DataQualityRulesetEvaluationRunDescription structure

Describes the result of a data quality ruleset evaluation run.

###### Fields

- `RunId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The unique run identifier associated with this run.

- `Status` – UTF-8 string (valid values: `RUNNING` | `FINISHED` | `FAILED` | `PENDING_EXECUTION` | `TIMED_OUT` | `CANCELING` | `CANCELED` | `RECEIVED_BY_TASKRUNNER`).

The status for this run.

- `StartedOn` – Timestamp.

The date and time when the run started.

- `DataSource` – A [DataSource](#aws-glue-api-data-quality-api-DataSource "#aws-glue-api-data-quality-api-DataSource") object.

The data source (an AWS Glue table) associated with the run.

## DataQualityRulesetEvaluationRunFilter structure

The filter criteria.

###### Fields

- `DataSource` – _Required:_ A [DataSource](#aws-glue-api-data-quality-api-DataSource "#aws-glue-api-data-quality-api-DataSource") object.

Filter based on a data source (an AWS Glue table) associated
with the run.

- `StartedBefore` – Timestamp.

Filter results by runs that started before this time.

- `StartedAfter` – Timestamp.

Filter results by runs that started after this time.

- `RulesetName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Filter results by the name of the ruleset.

## DataQualityEvaluationRunAdditionalRunOptions structure

Additional run options you can specify for an evaluation run.

###### Fields

- `CloudWatchMetricsEnabled` – Boolean.

Whether or not to enable CloudWatch metrics.

- `ResultsS3Prefix` – UTF-8 string.

Prefix for Amazon S3 to store results.

- `CompositeRuleEvaluationMethod` – UTF-8 string (valid values: `COLUMN` | `ROW`).

Set the evaluation method for composite rules in the ruleset to ROW/COLUMN

- `CustomLogGroupPrefix` – UTF-8 string.

A custom prefix for the CloudWatch log group names. When specified, evaluation
run logs are written to `<CustomLogGroupPrefix>/error`
and `<CustomLogGroupPrefix>/output` instead of the default
`/aws-glue/data-quality/error` and `/aws-glue/data-quality/output`
log groups.

- `RowLevelResults` – A [RowLevelResultsOptions](#aws-glue-api-data-quality-api-RowLevelResultsOptions "#aws-glue-api-data-quality-api-RowLevelResultsOptions") object.

The configuration for writing row-level evaluation results to a AWS Glue Data Catalog table.

- `ProfilingResults` – A [ProfilingResultsOptions](#aws-glue-api-data-quality-api-ProfilingResultsOptions "#aws-glue-api-data-quality-api-ProfilingResultsOptions") object.

The configuration for writing profiling results to a AWS Glue Data Catalog table.

- `ObservationScope` – UTF-8 string (valid values: `ALL` | `NONE`).

The scope of the observation for the evaluation run. Specifies whether
anomaly detection is enabled or disabled.

- `ObservationMode` – UTF-8 string (valid values: `SCHEDULED` | `FIXED`).

The observation mode for the evaluation run. Specifies how anomaly detection
bounds are calculated.

- `DataQualityRuleResults` – A [DataQualityRuleResultsOptions](#aws-glue-api-data-quality-api-DataQualityRuleResultsOptions "#aws-glue-api-data-quality-api-DataQualityRuleResultsOptions") object.

The configuration for writing rule results to a AWS Glue Data Catalog table.

- `ObservationResults` – An [ObservationResultsOptions](#aws-glue-api-data-quality-api-ObservationResultsOptions "#aws-glue-api-data-quality-api-ObservationResultsOptions") object.

The configuration for writing observation results to a AWS Glue Data Catalog table.

## DataQualityRuleRecommendationRunDescription structure

Describes the result of a data quality rule recommendation run.

###### Fields

- `RunId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The unique run identifier associated with this run.

- `Status` – UTF-8 string (valid values: `RUNNING` | `FINISHED` | `FAILED` | `PENDING_EXECUTION` | `TIMED_OUT` | `CANCELING` | `CANCELED` | `RECEIVED_BY_TASKRUNNER`).

The status for this run.

- `StartedOn` – Timestamp.

The date and time when this run started.

- `DataSource` – A [DataSource](#aws-glue-api-data-quality-api-DataSource "#aws-glue-api-data-quality-api-DataSource") object.

The data source (AWS Glue table) associated with the recommendation
run.

- `CreatedRulesetName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the ruleset that was created by the recommendation run.

## DataQualityRuleRecommendationRunFilter structure

A filter for listing data quality recommendation runs.

###### Fields

- `DataSource` – _Required:_ A [DataSource](#aws-glue-api-data-quality-api-DataSource "#aws-glue-api-data-quality-api-DataSource") object.

Filter based on a specified data source (AWS Glue table).

- `StartedBefore` – Timestamp.

Filter based on time for results started before provided time.

- `StartedAfter` – Timestamp.

Filter based on time for results started after provided time.

## DataQualityResult structure

Describes a data quality result.

###### Fields

- `ResultId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

A unique result ID for the data quality result.

- `ProfileId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The Profile ID for the data quality result.

- `Score` – Number (double), not more than 1.0.

An aggregate data quality score. Represents the ratio of rules that passed
to the total number of rules.

- `DataSource` – A [DataSource](#aws-glue-api-data-quality-api-DataSource "#aws-glue-api-data-quality-api-DataSource") object.

The table associated with the data quality result, if any.

- `RulesetName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the ruleset associated with the data quality result.

- `EvaluationContext` – UTF-8 string.

In the context of a job in AWS Glue Studio, each node in the canvas
is typically assigned some sort of name and data quality nodes will have names.
In the case of multiple nodes, the `evaluationContext` can differentiate
the nodes.

- `StartedOn` – Timestamp.

The date and time when this data quality run started.

- `CompletedOn` – Timestamp.

The date and time when this data quality run completed.

- `JobName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The job name associated with the data quality result, if any.

- `JobRunId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The job run ID associated with the data quality result, if any.

- `RulesetEvaluationRunId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The unique run ID for the ruleset evaluation for this data quality result.

- `RuleResults` – An array of [DataQualityRuleResult](#aws-glue-api-data-quality-api-DataQualityRuleResult "#aws-glue-api-data-quality-api-DataQualityRuleResult") objects, not more than 2000 structures.

A list of `DataQualityRuleResult` objects representing
the results for each rule.

- `AnalyzerResults` – An array of [DataQualityAnalyzerResult](#aws-glue-api-data-quality-api-DataQualityAnalyzerResult "#aws-glue-api-data-quality-api-DataQualityAnalyzerResult") objects, not more than 2000 structures.

A list of `DataQualityAnalyzerResult` objects representing
the results for each analyzer.

- `Observations` – An array of [DataQualityObservation](#aws-glue-api-data-quality-api-DataQualityObservation "#aws-glue-api-data-quality-api-DataQualityObservation") objects, not more than 50 structures.

A list of `DataQualityObservation` objects representing
the observations generated after evaluating the rules and analyzers.

- `AggregatedMetrics` – A [DataQualityAggregatedMetrics](#aws-glue-api-data-quality-api-DataQualityAggregatedMetrics "#aws-glue-api-data-quality-api-DataQualityAggregatedMetrics") object.

A summary of `DataQualityAggregatedMetrics` objects showing
the total counts of processed rows and rules, including their pass/fail statistics
based on row-level results.

## DataQualityAnalyzerResult structure

Describes the result of the evaluation of a data quality analyzer.

###### Fields

- `Name` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the data quality analyzer.

- `Description` – UTF-8 string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

A description of the data quality analyzer.

- `EvaluationMessage` – UTF-8 string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

An evaluation message.

- `EvaluatedMetrics` – A map array of key-value pairs.

Each key is a UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Each value is a Number (double).

A map of metrics associated with the evaluation of the analyzer.

- `EvaluatedDistributions` – A map array of key-value pairs.

Each key is a UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Each value is a A [DistributionData](#aws-glue-api-data-quality-api-DistributionData "#aws-glue-api-data-quality-api-DistributionData") object.

A map of distribution metrics associated with the evaluation of the analyzer.

## DataQualityObservation structure

Describes the observation generated after evaluating the rules and analyzers.

###### Fields

- `Description` – UTF-8 string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

A description of the data quality observation.

- `MetricBasedObservation` – A [MetricBasedObservation](#aws-glue-api-data-quality-api-MetricBasedObservation "#aws-glue-api-data-quality-api-MetricBasedObservation") object.

An object of type `MetricBasedObservation` representing
the observation that is based on evaluated data quality metrics.

## MetricBasedObservation structure

Describes the metric based observation generated based on evaluated
data quality metrics.

###### Fields

- `MetricName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the data quality metric used for generating the observation.

- `StatisticId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The Statistic ID.

- `MetricValues` – A [DataQualityMetricValues](#aws-glue-api-data-quality-api-DataQualityMetricValues "#aws-glue-api-data-quality-api-DataQualityMetricValues") object.

An object of type `DataQualityMetricValues` representing
the analysis of the data quality metric value.

- `NewRules` – An array of UTF-8 strings.

A list of new data quality rules generated as part of the observation based
on the data quality metric value.

## DataQualityMetricValues structure

Describes the data quality metric value according to the analysis of historical
data.

###### Fields

- `ActualValue` – Number (double).

The actual value of the data quality metric.

- `ExpectedValue` – Number (double).

The expected value of the data quality metric according to the analysis
of historical data.

- `LowerLimit` – Number (double).

The lower limit of the data quality metric value according to the analysis
of historical data.

- `UpperLimit` – Number (double).

The upper limit of the data quality metric value according to the analysis
of historical data.

## DataQualityRuleResult structure

Describes the result of the evaluation of a data quality rule.

###### Fields

- `Name` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the data quality rule.

- `Description` – UTF-8 string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

A description of the data quality rule.

- `EvaluationMessage` – UTF-8 string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

An evaluation message.

- `Result` – UTF-8 string (valid values: `PASS` | `FAIL` | `ERROR`).

A pass or fail status for the rule.

- `EvaluatedMetrics` – A map array of key-value pairs.

Each key is a UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Each value is a Number (double).

A map of metrics associated with the evaluation of the rule.

- `EvaluatedRule` – UTF-8 string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

The evaluated rule.

- `RuleMetrics` – A map array of key-value pairs.

Each key is a UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Each value is a Number (double).

A map containing metrics associated with the evaluation of the rule based
on row-level results.

- `Labels` – A map array of key-value pairs.

Each key is a UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Each value is a UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

A map containing labels assigned to the data quality rule.

## DataQualityResultDescription structure

Describes a data quality result.

###### Fields

- `ResultId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The unique result ID for this data quality result.

- `DataSource` – A [DataSource](#aws-glue-api-data-quality-api-DataSource "#aws-glue-api-data-quality-api-DataSource") object.

The table name associated with the data quality result.

- `JobName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The job name associated with the data quality result.

- `JobRunId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The job run ID associated with the data quality result.

- `StartedOn` – Timestamp.

The time that the run started for this data quality result.

## DataQualityResultFilterCriteria structure

Criteria used to return data quality results.

###### Fields

- `DataSource` – A [DataSource](#aws-glue-api-data-quality-api-DataSource "#aws-glue-api-data-quality-api-DataSource") object.

Filter results by the specified data source. For example, retrieving
all results for an AWS Glue table.

- `JobName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Filter results by the specified job name.

- `JobRunId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Filter results by the specified job run ID.

- `StartedAfter` – Timestamp.

Filter results by runs that started after this time.

- `StartedBefore` – Timestamp.

Filter results by runs that started before this time.

## DataQualityRulesetFilterCriteria structure

The criteria used to filter data quality rulesets.

###### Fields

- `Name` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the ruleset filter criteria.

- `Description` – Description string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

The description of the ruleset filter criteria.

- `CreatedBefore` – Timestamp.

Filter on rulesets created before this date.

- `CreatedAfter` – Timestamp.

Filter on rulesets created after this date.

- `LastModifiedBefore` – Timestamp.

Filter on rulesets last modified before this date.

- `LastModifiedAfter` – Timestamp.

Filter on rulesets last modified after this date.

- `TargetTable` – A [DataQualityTargetTable](#aws-glue-api-data-quality-api-DataQualityTargetTable "#aws-glue-api-data-quality-api-DataQualityTargetTable") object.

The name and database name of the target table.

## DataQualityAggregatedMetrics structure

A summary of metrics showing the total counts of processed rows and rules,
including their pass/fail statistics based on row-level results.

###### Fields

- `TotalRowsProcessed` – Number (double).

The total number of rows that were processed during the data quality evaluation.

- `TotalRowsPassed` – Number (double).

The total number of rows that passed all applicable data quality rules.

- `TotalRowsFailed` – Number (double).

The total number of rows that failed one or more data quality rules.

- `TotalRulesProcessed` – Number (double).

The total number of data quality rules that were evaluated.

- `TotalRulesPassed` – Number (double).

The total number of data quality rules that passed their evaluation criteria.

- `TotalRulesFailed` – Number (double).

The total number of data quality rules that failed their evaluation criteria.

## StatisticAnnotation structure

A Statistic Annotation.

###### Fields

- `ProfileId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The Profile ID.

- `StatisticId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The Statistic ID.

- `StatisticRecordedOn` – Timestamp.

The timestamp when the annotated statistic was recorded.

- `InclusionAnnotation` – A [TimestampedInclusionAnnotation](#aws-glue-api-data-quality-api-TimestampedInclusionAnnotation "#aws-glue-api-data-quality-api-TimestampedInclusionAnnotation") object.

The inclusion annotation applied to the statistic.

## TimestampedInclusionAnnotation structure

A timestamped inclusion annotation.

###### Fields

- `Value` – UTF-8 string (valid values: `INCLUDE` | `EXCLUDE`).

The inclusion annotation value.

- `LastModifiedOn` – Timestamp.

The timestamp when the inclusion annotation was last modified.

## AnnotationError structure

A failed annotation.

###### Fields

- `ProfileId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The Profile ID for the failed annotation.

- `StatisticId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The Statistic ID for the failed annotation.

- `FailureReason` – Description string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

The reason why the annotation failed.

## DatapointInclusionAnnotation structure

An Inclusion Annotation.

###### Fields

- `ProfileId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the data quality profile the statistic belongs to.

- `StatisticId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The Statistic ID.

- `InclusionAnnotation` – UTF-8 string (valid values: `INCLUDE` | `EXCLUDE`).

The inclusion annotation value to apply to the statistic.

## StatisticSummaryList list

A list of `StatisticSummary`.

An array of [StatisticSummary](#aws-glue-api-data-quality-api-StatisticSummary "#aws-glue-api-data-quality-api-StatisticSummary") objects.

A list of `StatisticSummary`.

## StatisticSummary structure

Summary information about a statistic.

###### Fields

- `StatisticId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The Statistic ID.

- `ProfileId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The Profile ID.

- `RunIdentifier` – A [RunIdentifier](#aws-glue-api-data-quality-api-RunIdentifier "#aws-glue-api-data-quality-api-RunIdentifier") object.

The Run Identifier

- `StatisticName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Custom string pattern #21](aws-glue-api-common.md#regex_21 "aws-glue-api-common.md#regex_21").

The name of the statistic.

- `DoubleValue` – Number (double).

The value of the statistic.

- `DistributionValue` – A [DistributionData](#aws-glue-api-data-quality-api-DistributionData "#aws-glue-api-data-quality-api-DistributionData") object.

The distribution value for the statistic.

- `EvaluationLevel` – UTF-8 string (valid values: `Dataset="DATASET"` | `Column="COLUMN"` | `Multicolumn="MULTICOLUMN"`).

The evaluation level of the statistic. Possible values: `Dataset`,
`Column`, `Multicolumn`.

- `ColumnsReferenced` – An array of UTF-8 strings.

The list of columns referenced by the statistic.

- `ReferencedDatasets` – An array of UTF-8 strings.

The list of datasets referenced by the statistic.

- `StatisticProperties` – A map array of key-value pairs.

Each key is a UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Each value is a Description string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

A `StatisticPropertiesMap`, which contains a `NameString`
and `DescriptionString`

- `RecordedOn` – Timestamp.

The timestamp when the statistic was recorded.

- `InclusionAnnotation` – A [TimestampedInclusionAnnotation](#aws-glue-api-data-quality-api-TimestampedInclusionAnnotation "#aws-glue-api-data-quality-api-TimestampedInclusionAnnotation") object.

The inclusion annotation for the statistic.

## RunIdentifier structure

A run identifier.

###### Fields

- `RunId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The Run ID.

- `JobRunId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The Job Run ID.

## StatisticModelResult structure

The statistic model result.

###### Fields

- `LowerBound` – Number (double).

The lower bound.

- `UpperBound` – Number (double).

The upper bound.

- `PredictedValue` – Number (double).

The predicted value.

- `ActualValue` – Number (double).

The actual value.

- `Date` – Timestamp.

The date.

- `InclusionAnnotation` – UTF-8 string (valid values: `INCLUDE` | `EXCLUDE`).

The inclusion annotation.

## DataQualityGlueTable structure

The database and table in the AWS Glue Data Catalog that is used for
input or output data for Data Quality Operations.

###### Fields

- `DatabaseName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

A database name in the AWS Glue Data Catalog.

- `TableName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

A table name in the AWS Glue Data Catalog.

- `CatalogId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

A unique identifier for the AWS Glue Data Catalog.

- `ConnectionName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the connection to the AWS Glue Data Catalog.

- `AdditionalOptions` – A map array of key-value pairs, not less than 1 or more than 10 pairs.

Each key is a UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Each value is a Description string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

Additional options for the table. Currently there are two keys supported:

    + `pushDownPredicate`: to filter on partitions without having
     to list and read all the files in your dataset.
    + `catalogPartitionPredicate`: to use server-side partition
     pruning using partition indexes in the AWS Glue Data Catalog.

- `PreProcessingQuery` – UTF-8 string, not more than 51200 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

SQL Query of SparkSQL format that can be used to pre-process the data for
the table in AWS Glue Data Catalog, before running the Data Quality Operation.

## DataQualityRuleRecommendationRunAdditionalRunOptions structure

Additional run options you can specify for a recommendation run.

###### Fields

- `CustomLogGroupPrefix` – UTF-8 string.

A custom prefix for the CloudWatch log group names. When specified, recommendation
run logs are written to `<CustomLogGroupPrefix>/error`
and `<CustomLogGroupPrefix>/output` instead of the default
`/aws-glue/data-quality/error` and `/aws-glue/data-quality/output`
log groups.

## DataQualityRuleResultsOptions structure

The configuration for writing data quality rule results.

###### Fields

- `WriteDataQualityRuleResultsEnabled` – Boolean.

Set to true to write data quality rule results.

- `CatalogTableConfig` – A [CatalogTableConfigOptions](#aws-glue-api-data-quality-api-CatalogTableConfigOptions "#aws-glue-api-data-quality-api-CatalogTableConfigOptions") object.

The AWS Glue Data Catalog table configuration for storing the rule
results.

## DistributionData structure

The distribution data for a statistic.

###### Fields

- `BinEdges` – An array of UTF-8 strings.

The bin edge values for the distribution.

- `Count` – An array of signed 32-bit integers.

The frequency count for each bin in the distribution.

- `DataType` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The data type of the column for the distribution.

## ObservationResultsOptions structure

The configuration for writing observation results.

###### Fields

- `WriteObservationResultsEnabled` – Boolean.

Set to true to write observation results.

- `CatalogTableConfig` – A [CatalogTableConfigOptions](#aws-glue-api-data-quality-api-CatalogTableConfigOptions "#aws-glue-api-data-quality-api-CatalogTableConfigOptions") object.

The AWS Glue Data Catalog table configuration for storing the observation
results.

## ProfilingResultsOptions structure

The configuration for writing profiling results.

###### Fields

- `WriteProfilingResultsEnabled` – Boolean.

Set to true to write profiling results.

- `CatalogTableConfig` – A [CatalogTableConfigOptions](#aws-glue-api-data-quality-api-CatalogTableConfigOptions "#aws-glue-api-data-quality-api-CatalogTableConfigOptions") object.

The AWS Glue Data Catalog table configuration for storing the profiling
results.

- `DistributionResults` – A [DistributionResultsOptions](#aws-glue-api-data-quality-api-DistributionResultsOptions "#aws-glue-api-data-quality-api-DistributionResultsOptions") object.

The configuration for writing distribution results.

## RowLevelResultsOptions structure

The configuration for writing row-level evaluation results.

###### Fields

- `MaxRowsToWrite` – Number (integer).

The maximum number of rows to write in the results.

- `ResultType` – UTF-8 string (valid values: `ALL` | `PASSED_ONLY` | `FAILED_ONLY`).

The result type to include in the row-level results output.

- `CatalogTableConfig` – A [CatalogTableConfigOptions](#aws-glue-api-data-quality-api-CatalogTableConfigOptions "#aws-glue-api-data-quality-api-CatalogTableConfigOptions") object.

The AWS Glue Data Catalog table configuration for storing the results.

## CatalogTableConfigOptions structure

The configuration for a AWS Glue Data Catalog table used to store
data quality results.

###### Fields

- `DatabaseName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the database in the AWS Glue Data Catalog.

- `TableName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the table in the AWS Glue Data Catalog.

- `S3Location` – UTF-8 string.

The Amazon S3 location for storing the results.

- `CatalogId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

A unique identifier for the AWS Glue Data Catalog.

## DistributionResultsOptions structure

The configuration for writing distribution results.

###### Fields

- `WriteDistributionResultsEnabled` – Boolean.

Set to true to write distribution results.

- `CatalogTableConfig` – A [CatalogTableConfigOptions](#aws-glue-api-data-quality-api-CatalogTableConfigOptions "#aws-glue-api-data-quality-api-CatalogTableConfigOptions") object.

The AWS Glue Data Catalog table configuration for storing the distribution
results.

## Operations

- [StartDataQualityRulesetEvaluationRun action (Python: start\_data\_quality\_ruleset\_evaluation\_run)](#aws-glue-api-data-quality-api-StartDataQualityRulesetEvaluationRun "#aws-glue-api-data-quality-api-StartDataQualityRulesetEvaluationRun")
- [CancelDataQualityRulesetEvaluationRun action (Python: cancel\_data\_quality\_ruleset\_evaluation\_run)](#aws-glue-api-data-quality-api-CancelDataQualityRulesetEvaluationRun "#aws-glue-api-data-quality-api-CancelDataQualityRulesetEvaluationRun")
- [GetDataQualityRulesetEvaluationRun action (Python: get\_data\_quality\_ruleset\_evaluation\_run)](#aws-glue-api-data-quality-api-GetDataQualityRulesetEvaluationRun "#aws-glue-api-data-quality-api-GetDataQualityRulesetEvaluationRun")
- [ListDataQualityRulesetEvaluationRuns action (Python: list\_data\_quality\_ruleset\_evaluation\_runs)](#aws-glue-api-data-quality-api-ListDataQualityRulesetEvaluationRuns "#aws-glue-api-data-quality-api-ListDataQualityRulesetEvaluationRuns")
- [StartDataQualityRuleRecommendationRun action (Python: start\_data\_quality\_rule\_recommendation\_run)](#aws-glue-api-data-quality-api-StartDataQualityRuleRecommendationRun "#aws-glue-api-data-quality-api-StartDataQualityRuleRecommendationRun")
- [CancelDataQualityRuleRecommendationRun action (Python: cancel\_data\_quality\_rule\_recommendation\_run)](#aws-glue-api-data-quality-api-CancelDataQualityRuleRecommendationRun "#aws-glue-api-data-quality-api-CancelDataQualityRuleRecommendationRun")
- [GetDataQualityRuleRecommendationRun action (Python: get\_data\_quality\_rule\_recommendation\_run)](#aws-glue-api-data-quality-api-GetDataQualityRuleRecommendationRun "#aws-glue-api-data-quality-api-GetDataQualityRuleRecommendationRun")
- [ListDataQualityRuleRecommendationRuns action (Python: list\_data\_quality\_rule\_recommendation\_runs)](#aws-glue-api-data-quality-api-ListDataQualityRuleRecommendationRuns "#aws-glue-api-data-quality-api-ListDataQualityRuleRecommendationRuns")
- [GetDataQualityResult action (Python: get\_data\_quality\_result)](#aws-glue-api-data-quality-api-GetDataQualityResult "#aws-glue-api-data-quality-api-GetDataQualityResult")
- [BatchGetDataQualityResult action (Python: batch\_get\_data\_quality\_result)](#aws-glue-api-data-quality-api-BatchGetDataQualityResult "#aws-glue-api-data-quality-api-BatchGetDataQualityResult")
- [ListDataQualityResults action (Python: list\_data\_quality\_results)](#aws-glue-api-data-quality-api-ListDataQualityResults "#aws-glue-api-data-quality-api-ListDataQualityResults")
- [CreateDataQualityRuleset action (Python: create\_data\_quality\_ruleset)](#aws-glue-api-data-quality-api-CreateDataQualityRuleset "#aws-glue-api-data-quality-api-CreateDataQualityRuleset")
- [DeleteDataQualityRuleset action (Python: delete\_data\_quality\_ruleset)](#aws-glue-api-data-quality-api-DeleteDataQualityRuleset "#aws-glue-api-data-quality-api-DeleteDataQualityRuleset")
- [GetDataQualityRuleset action (Python: get\_data\_quality\_ruleset)](#aws-glue-api-data-quality-api-GetDataQualityRuleset "#aws-glue-api-data-quality-api-GetDataQualityRuleset")
- [ListDataQualityRulesets action (Python: list\_data\_quality\_rulesets)](#aws-glue-api-data-quality-api-ListDataQualityRulesets "#aws-glue-api-data-quality-api-ListDataQualityRulesets")
- [UpdateDataQualityRuleset action (Python: update\_data\_quality\_ruleset)](#aws-glue-api-data-quality-api-UpdateDataQualityRuleset "#aws-glue-api-data-quality-api-UpdateDataQualityRuleset")
- [ListDataQualityStatistics action (Python: list\_data\_quality\_statistics)](#aws-glue-api-data-quality-api-ListDataQualityStatistics "#aws-glue-api-data-quality-api-ListDataQualityStatistics")
- [TimestampFilter structure](#aws-glue-api-data-quality-api-TimestampFilter "#aws-glue-api-data-quality-api-TimestampFilter")
- [CreateDataQualityRulesetRequest structure](#aws-glue-api-data-quality-api-CreateDataQualityRulesetRequest "#aws-glue-api-data-quality-api-CreateDataQualityRulesetRequest")
- [GetDataQualityRulesetResponse structure](#aws-glue-api-data-quality-api-GetDataQualityRulesetResponse "#aws-glue-api-data-quality-api-GetDataQualityRulesetResponse")
- [GetDataQualityResultResponse structure](#aws-glue-api-data-quality-api-GetDataQualityResultResponse "#aws-glue-api-data-quality-api-GetDataQualityResultResponse")
- [StartDataQualityRuleRecommendationRunRequest structure](#aws-glue-api-data-quality-api-StartDataQualityRuleRecommendationRunRequest "#aws-glue-api-data-quality-api-StartDataQualityRuleRecommendationRunRequest")
- [GetDataQualityRuleRecommendationRunResponse structure](#aws-glue-api-data-quality-api-GetDataQualityRuleRecommendationRunResponse "#aws-glue-api-data-quality-api-GetDataQualityRuleRecommendationRunResponse")
- [BatchPutDataQualityStatisticAnnotation action (Python: batch\_put\_data\_quality\_statistic\_annotation)](#aws-glue-api-data-quality-api-BatchPutDataQualityStatisticAnnotation "#aws-glue-api-data-quality-api-BatchPutDataQualityStatisticAnnotation")
- [GetDataQualityModel action (Python: get\_data\_quality\_model)](#aws-glue-api-data-quality-api-GetDataQualityModel "#aws-glue-api-data-quality-api-GetDataQualityModel")
- [GetDataQualityModelResult action (Python: get\_data\_quality\_model\_result)](#aws-glue-api-data-quality-api-GetDataQualityModelResult "#aws-glue-api-data-quality-api-GetDataQualityModelResult")
- [ListDataQualityStatisticAnnotations action (Python: list\_data\_quality\_statistic\_annotations)](#aws-glue-api-data-quality-api-ListDataQualityStatisticAnnotations "#aws-glue-api-data-quality-api-ListDataQualityStatisticAnnotations")
- [PutDataQualityProfileAnnotation action (Python: put\_data\_quality\_profile\_annotation)](#aws-glue-api-data-quality-api-PutDataQualityProfileAnnotation "#aws-glue-api-data-quality-api-PutDataQualityProfileAnnotation")

## StartDataQualityRulesetEvaluationRun action (Python: start\_data\_quality\_ruleset\_evaluation\_run)

Once you have a ruleset definition (either recommended or your own), you
call this operation to evaluate the ruleset against a data source (AWS Glue table). The evaluation computes results which you can retrieve with the `GetDataQualityResult`
API.

###### Request

- `DataSource` – _Required:_ A [DataSource](#aws-glue-api-data-quality-api-DataSource "#aws-glue-api-data-quality-api-DataSource") object.

The data source (AWS Glue table) associated with this run.

- `Role` – _Required:_ UTF-8 string.

An IAM role supplied to encrypt the results of the run.

- `NumberOfWorkers` – Number (integer).

The number of `G.1X` workers to be used in the run. The default
is 5.

- `Timeout` – Number (integer), at least 1.

The timeout for a run in minutes. This is the maximum time that a run can consume
resources before it is terminated and enters `TIMEOUT` status.
The default is 2,880 minutes (48 hours).

- `ClientToken` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Used for idempotency and is recommended to be set to a random ID (such as
a UUID) to avoid creating or starting multiple instances of the same resource.

- `AdditionalRunOptions` – A [DataQualityEvaluationRunAdditionalRunOptions](#aws-glue-api-data-quality-api-DataQualityEvaluationRunAdditionalRunOptions "#aws-glue-api-data-quality-api-DataQualityEvaluationRunAdditionalRunOptions") object.

Additional run options you can specify for an evaluation run.

- `RulesetNames` – _Required:_ An array of UTF-8 strings, not less than 1 or more than 10 strings.

A list of ruleset names.

- `AdditionalDataSources` – A map array of key-value pairs.

Each key is a UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Each value is a A [DataSource](#aws-glue-api-data-quality-api-DataSource "#aws-glue-api-data-quality-api-DataSource") object.

A map of reference strings to additional data sources you can specify for
an evaluation run.

###### Response

- `RunId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The unique run identifier associated with this run.

###### Errors

- `InvalidInputException`
- `EntityNotFoundException`
- `OperationTimeoutException`
- `InternalServiceException`
- `ConflictException`

## CancelDataQualityRulesetEvaluationRun action (Python: cancel\_data\_quality\_ruleset\_evaluation\_run)

Cancels a run where a ruleset is being evaluated against a data source.

###### Request

- `RunId` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The unique run identifier associated with this run.

###### Response

- _No Response parameters._

###### Errors

- `EntityNotFoundException`
- `InvalidInputException`
- `OperationTimeoutException`
- `InternalServiceException`

## GetDataQualityRulesetEvaluationRun action (Python: get\_data\_quality\_ruleset\_evaluation\_run)

Retrieves a specific run where a ruleset is evaluated against a data source.

###### Request

- `RunId` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The unique run identifier associated with this run.

###### Response

- `RunId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The unique run identifier associated with this run.

- `DataSource` – A [DataSource](#aws-glue-api-data-quality-api-DataSource "#aws-glue-api-data-quality-api-DataSource") object.

The data source (an AWS Glue table) associated with this evaluation
run.

- `Role` – UTF-8 string.

An IAM role supplied to encrypt the results of the run.

- `NumberOfWorkers` – Number (integer).

The number of `G.1X` workers to be used in the run. The default
is 5.

- `Timeout` – Number (integer), at least 1.

The timeout for a run in minutes. This is the maximum time that a run can consume
resources before it is terminated and enters `TIMEOUT` status.
The default is 2,880 minutes (48 hours).

- `AdditionalRunOptions` – A [DataQualityEvaluationRunAdditionalRunOptions](#aws-glue-api-data-quality-api-DataQualityEvaluationRunAdditionalRunOptions "#aws-glue-api-data-quality-api-DataQualityEvaluationRunAdditionalRunOptions") object.

Additional run options you can specify for an evaluation run.

- `Status` – UTF-8 string (valid values: `RUNNING` | `FINISHED` | `FAILED` | `PENDING_EXECUTION` | `TIMED_OUT` | `CANCELING` | `CANCELED` | `RECEIVED_BY_TASKRUNNER`).

The status for this run.

- `ErrorString` – UTF-8 string.

The error strings that are associated with the run.

- `StartedOn` – Timestamp.

The date and time when this run started.

- `LastModifiedOn` – Timestamp.

A timestamp. The last point in time when this data quality rule recommendation
run was modified.

- `CompletedOn` – Timestamp.

The date and time when this run was completed.

- `ExecutionTime` – Number (integer).

The amount of time (in seconds) that the run consumed resources.

- `RulesetNames` – An array of UTF-8 strings, not less than 1 or more than 10 strings.

A list of ruleset names for the run. Currently, this parameter takes only
one Ruleset name.

- `ResultIds` – An array of UTF-8 strings, not less than 1 or more than 10 strings.

A list of result IDs for the data quality results for the run.

- `AdditionalDataSources` – A map array of key-value pairs.

Each key is a UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Each value is a A [DataSource](#aws-glue-api-data-quality-api-DataSource "#aws-glue-api-data-quality-api-DataSource") object.

A map of reference strings to additional data sources you can specify for
an evaluation run.

###### Errors

- `EntityNotFoundException`
- `InvalidInputException`
- `OperationTimeoutException`
- `InternalServiceException`

## ListDataQualityRulesetEvaluationRuns action (Python: list\_data\_quality\_ruleset\_evaluation\_runs)

Lists all the runs meeting the filter criteria, where a ruleset is evaluated
against a data source.

###### Request

- `Filter` – A [DataQualityRulesetEvaluationRunFilter](#aws-glue-api-data-quality-api-DataQualityRulesetEvaluationRunFilter "#aws-glue-api-data-quality-api-DataQualityRulesetEvaluationRunFilter") object.

The filter criteria.

- `NextToken` – UTF-8 string.

A paginated token to offset the results.

- `MaxResults` – Number (integer), not less than 1 or more than 1000.

The maximum number of results to return.

###### Response

- `Runs` – An array of [DataQualityRulesetEvaluationRunDescription](#aws-glue-api-data-quality-api-DataQualityRulesetEvaluationRunDescription "#aws-glue-api-data-quality-api-DataQualityRulesetEvaluationRunDescription") objects.

A list of `DataQualityRulesetEvaluationRunDescription`
objects representing data quality ruleset runs.

- `NextToken` – UTF-8 string.

A pagination token, if more results are available.

###### Errors

- `InvalidInputException`
- `OperationTimeoutException`
- `InternalServiceException`

## StartDataQualityRuleRecommendationRun action (Python: start\_data\_quality\_rule\_recommendation\_run)

Starts a recommendation run that is used to generate rules when you don't
know what rules to write. AWS Glue Data Quality analyzes the data and
comes up with recommendations for a potential ruleset. You can then triage the
ruleset and modify the generated ruleset to your liking.

Recommendation runs are automatically deleted after 90 days.

###### Request

The request of the Data Quality rule recommendation request.

- `DataSource` – _Required:_ A [DataSource](#aws-glue-api-data-quality-api-DataSource "#aws-glue-api-data-quality-api-DataSource") object.

The data source (AWS Glue table) associated with this run.

- `Role` – _Required:_ UTF-8 string.

An IAM role supplied to encrypt the results of the run.

- `NumberOfWorkers` – Number (integer).

The number of `G.1X` workers to be used in the run. The default
is 5.

- `Timeout` – Number (integer), at least 1.

The timeout for a run in minutes. This is the maximum time that a run can consume
resources before it is terminated and enters `TIMEOUT` status.
The default is 2,880 minutes (48 hours).

- `CreatedRulesetName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

A name for the ruleset.

- `DataQualitySecurityConfiguration` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the security configuration created with the data quality encryption
option.

- `ClientToken` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Used for idempotency and is recommended to be set to a random ID (such as
a UUID) to avoid creating or starting multiple instances of the same resource.

- `AdditionalRunOptions` – A [DataQualityRuleRecommendationRunAdditionalRunOptions](#aws-glue-api-data-quality-api-DataQualityRuleRecommendationRunAdditionalRunOptions "#aws-glue-api-data-quality-api-DataQualityRuleRecommendationRunAdditionalRunOptions") object.

Additional run options you can specify for a recommendation run.

###### Response

- `RunId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The unique run identifier associated with this run.

###### Errors

- `InvalidInputException`
- `OperationTimeoutException`
- `InternalServiceException`
- `ConflictException`

## CancelDataQualityRuleRecommendationRun action (Python: cancel\_data\_quality\_rule\_recommendation\_run)

Cancels the specified recommendation run that was being used to generate
rules.

###### Request

- `RunId` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The unique run identifier associated with this run.

###### Response

- _No Response parameters._

###### Errors

- `EntityNotFoundException`
- `InvalidInputException`
- `OperationTimeoutException`
- `InternalServiceException`

## GetDataQualityRuleRecommendationRun action (Python: get\_data\_quality\_rule\_recommendation\_run)

Gets the specified recommendation run that was used to generate rules.

###### Request

- `RunId` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The unique run identifier associated with this run.

###### Response

The response for the Data Quality rule recommendation run.

- `RunId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The unique run identifier associated with this run.

- `DataSource` – A [DataSource](#aws-glue-api-data-quality-api-DataSource "#aws-glue-api-data-quality-api-DataSource") object.

The data source (an AWS Glue table) associated with this run.

- `Role` – UTF-8 string.

An IAM role supplied to encrypt the results of the run.

- `NumberOfWorkers` – Number (integer).

The number of `G.1X` workers to be used in the run. The default
is 5.

- `Timeout` – Number (integer), at least 1.

The timeout for a run in minutes. This is the maximum time that a run can consume
resources before it is terminated and enters `TIMEOUT` status.
The default is 2,880 minutes (48 hours).

- `Status` – UTF-8 string (valid values: `RUNNING` | `FINISHED` | `FAILED` | `PENDING_EXECUTION` | `TIMED_OUT` | `CANCELING` | `CANCELED` | `RECEIVED_BY_TASKRUNNER`).

The status for this run.

- `ErrorString` – UTF-8 string.

The error strings that are associated with the run.

- `StartedOn` – Timestamp.

The date and time when this run started.

- `LastModifiedOn` – Timestamp.

A timestamp. The last point in time when this data quality rule recommendation
run was modified.

- `CompletedOn` – Timestamp.

The date and time when this run was completed.

- `ExecutionTime` – Number (integer).

The amount of time (in seconds) that the run consumed resources.

- `RecommendedRuleset` – UTF-8 string, not less than 1 or more than 65536 bytes long.

When a start rule recommendation run completes, it creates a recommended
ruleset (a set of rules). This member has those rules in Data Quality Definition
Language (DQDL) format.

- `CreatedRulesetName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the ruleset that was created by the run.

- `DataQualitySecurityConfiguration` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the security configuration created with the data quality encryption
option.

- `AdditionalRunOptions` – A [DataQualityRuleRecommendationRunAdditionalRunOptions](#aws-glue-api-data-quality-api-DataQualityRuleRecommendationRunAdditionalRunOptions "#aws-glue-api-data-quality-api-DataQualityRuleRecommendationRunAdditionalRunOptions") object.

Additional run options you can specify for a recommendation run.

###### Errors

- `EntityNotFoundException`
- `InvalidInputException`
- `OperationTimeoutException`
- `InternalServiceException`

## ListDataQualityRuleRecommendationRuns action (Python: list\_data\_quality\_rule\_recommendation\_runs)

Lists the recommendation runs meeting the filter criteria.

###### Request

- `Filter` – A [DataQualityRuleRecommendationRunFilter](#aws-glue-api-data-quality-api-DataQualityRuleRecommendationRunFilter "#aws-glue-api-data-quality-api-DataQualityRuleRecommendationRunFilter") object.

The filter criteria.

- `NextToken` – UTF-8 string.

A paginated token to offset the results.

- `MaxResults` – Number (integer), not less than 1 or more than 1000.

The maximum number of results to return.

- `Tags` – A map array of key-value pairs, not more than 50 pairs.

Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

Each value is a UTF-8 string, not more than 256 bytes long.

A list of key-value pair tags to filter recommendation runs.

###### Response

- `Runs` – An array of [DataQualityRuleRecommendationRunDescription](#aws-glue-api-data-quality-api-DataQualityRuleRecommendationRunDescription "#aws-glue-api-data-quality-api-DataQualityRuleRecommendationRunDescription") objects.

A list of `DataQualityRuleRecommendationRunDescription`
objects.

- `NextToken` – UTF-8 string.

A pagination token, if more results are available.

###### Errors

- `InvalidInputException`
- `OperationTimeoutException`
- `InternalServiceException`

## GetDataQualityResult action (Python: get\_data\_quality\_result)

Retrieves the result of a data quality rule evaluation.

###### Request

- `ResultId` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

A unique result ID for the data quality result.

###### Response

The response for the data quality result.

- `ResultId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

A unique result ID for the data quality result.

- `ProfileId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The Profile ID for the data quality result.

- `Score` – Number (double), not more than 1.0.

An aggregate data quality score. Represents the ratio of rules that passed
to the total number of rules.

- `DataSource` – A [DataSource](#aws-glue-api-data-quality-api-DataSource "#aws-glue-api-data-quality-api-DataSource") object.

The table associated with the data quality result, if any.

- `RulesetName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the ruleset associated with the data quality result.

- `EvaluationContext` – UTF-8 string.

In the context of a job in AWS Glue Studio, each node in the canvas
is typically assigned some sort of name and data quality nodes will have names.
In the case of multiple nodes, the `evaluationContext` can differentiate
the nodes.

- `StartedOn` – Timestamp.

The date and time when the run for this data quality result started.

- `CompletedOn` – Timestamp.

The date and time when the run for this data quality result was completed.

- `JobName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The job name associated with the data quality result, if any.

- `JobRunId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The job run ID associated with the data quality result, if any.

- `RulesetEvaluationRunId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The unique run ID associated with the ruleset evaluation.

- `RuleResults` – An array of [DataQualityRuleResult](#aws-glue-api-data-quality-api-DataQualityRuleResult "#aws-glue-api-data-quality-api-DataQualityRuleResult") objects, not more than 2000 structures.

A list of `DataQualityRuleResult` objects representing
the results for each rule.

- `AnalyzerResults` – An array of [DataQualityAnalyzerResult](#aws-glue-api-data-quality-api-DataQualityAnalyzerResult "#aws-glue-api-data-quality-api-DataQualityAnalyzerResult") objects, not more than 2000 structures.

A list of `DataQualityAnalyzerResult` objects representing
the results for each analyzer.

- `Observations` – An array of [DataQualityObservation](#aws-glue-api-data-quality-api-DataQualityObservation "#aws-glue-api-data-quality-api-DataQualityObservation") objects, not more than 50 structures.

A list of `DataQualityObservation` objects representing
the observations generated after evaluating the rules and analyzers.

- `AggregatedMetrics` – A [DataQualityAggregatedMetrics](#aws-glue-api-data-quality-api-DataQualityAggregatedMetrics "#aws-glue-api-data-quality-api-DataQualityAggregatedMetrics") object.

A summary of `DataQualityAggregatedMetrics` objects showing
the total counts of processed rows and rules, including their pass/fail statistics
based on row-level results.

###### Errors

- `InvalidInputException`
- `OperationTimeoutException`
- `InternalServiceException`
- `EntityNotFoundException`

## BatchGetDataQualityResult action (Python: batch\_get\_data\_quality\_result)

Retrieves a list of data quality results for the specified result IDs.

###### Request

- `ResultIds` – _Required:_ An array of UTF-8 strings, not less than 1 or more than 100 strings.

A list of unique result IDs for the data quality results.

###### Response

- `Results` – _Required:_ An array of [DataQualityResult](#aws-glue-api-data-quality-api-DataQualityResult "#aws-glue-api-data-quality-api-DataQualityResult") objects.

A list of `DataQualityResult` objects representing the
data quality results.

- `ResultsNotFound` – An array of UTF-8 strings, not less than 1 or more than 100 strings.

A list of result IDs for which results were not found.

###### Errors

- `InvalidInputException`
- `OperationTimeoutException`
- `InternalServiceException`

## ListDataQualityResults action (Python: list\_data\_quality\_results)

Returns all data quality execution results for your account.

###### Request

- `Filter` – A [DataQualityResultFilterCriteria](#aws-glue-api-data-quality-api-DataQualityResultFilterCriteria "#aws-glue-api-data-quality-api-DataQualityResultFilterCriteria") object.

The filter criteria.

- `NextToken` – UTF-8 string.

A paginated token to offset the results.

- `MaxResults` – Number (integer), not less than 1 or more than 1000.

The maximum number of results to return.

###### Response

- `Results` – _Required:_ An array of [DataQualityResultDescription](#aws-glue-api-data-quality-api-DataQualityResultDescription "#aws-glue-api-data-quality-api-DataQualityResultDescription") objects.

A list of `DataQualityResultDescription` objects.

- `NextToken` – UTF-8 string.

A pagination token, if more results are available.

###### Errors

- `InvalidInputException`
- `OperationTimeoutException`
- `InternalServiceException`

## CreateDataQualityRuleset action (Python: create\_data\_quality\_ruleset)

Creates a data quality ruleset with DQDL rules applied to a specified AWS Glue table.

You create the ruleset using the Data Quality Definition Language (DQDL).
For more information, see the AWS Glue developer guide.

###### Request

A request to create a data quality ruleset.

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

A unique name for the data quality ruleset.

- `Description` – Description string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

A description of the data quality ruleset.

- `Ruleset` – _Required:_ UTF-8 string, not less than 1 or more than 65536 bytes long.

A Data Quality Definition Language (DQDL) ruleset. For more information,
see the AWS Glue developer guide.

- `Tags` – A map array of key-value pairs, not more than 50 pairs.

Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

Each value is a UTF-8 string, not more than 256 bytes long.

A list of tags applied to the data quality ruleset.

- `TargetTable` – A [DataQualityTargetTable](#aws-glue-api-data-quality-api-DataQualityTargetTable "#aws-glue-api-data-quality-api-DataQualityTargetTable") object.

A target table associated with the data quality ruleset.

- `RecommendationRunId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

A unique run ID for the recommendation run.

- `DataQualitySecurityConfiguration` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the security configuration created with the data quality encryption
option.

- `ClientToken` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Used for idempotency and is recommended to be set to a random ID (such as
a UUID) to avoid creating or starting multiple instances of the same resource.

###### Response

- `Name` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

A unique name for the data quality ruleset.

###### Errors

- `InvalidInputException`
- `AlreadyExistsException`
- `OperationTimeoutException`
- `InternalServiceException`
- `ResourceNumberLimitExceededException`

## DeleteDataQualityRuleset action (Python: delete\_data\_quality\_ruleset)

Deletes a data quality ruleset.

###### Request

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

A name for the data quality ruleset.

###### Response

- _No Response parameters._

###### Errors

- `EntityNotFoundException`
- `InvalidInputException`
- `OperationTimeoutException`
- `InternalServiceException`

## GetDataQualityRuleset action (Python: get\_data\_quality\_ruleset)

Returns an existing ruleset by identifier or name.

###### Request

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the ruleset.

###### Response

Returns the data quality ruleset response.

- `Name` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the ruleset.

- `Description` – Description string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

A description of the ruleset.

- `Ruleset` – UTF-8 string, not less than 1 or more than 65536 bytes long.

A Data Quality Definition Language (DQDL) ruleset. For more information,
see the AWS Glue developer guide.

- `TargetTable` – A [DataQualityTargetTable](#aws-glue-api-data-quality-api-DataQualityTargetTable "#aws-glue-api-data-quality-api-DataQualityTargetTable") object.

The name and database name of the target table.

- `CreatedOn` – Timestamp.

A timestamp. The time and date that this data quality ruleset was created.

- `LastModifiedOn` – Timestamp.

A timestamp. The last point in time when this data quality ruleset was modified.

- `RecommendationRunId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

When a ruleset was created from a recommendation run, this run ID is generated
to link the two together.

- `DataQualitySecurityConfiguration` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the security configuration created with the data quality encryption
option.

###### Errors

- `EntityNotFoundException`
- `InvalidInputException`
- `OperationTimeoutException`
- `InternalServiceException`

## ListDataQualityRulesets action (Python: list\_data\_quality\_rulesets)

Returns a paginated list of rulesets for the specified list of AWS Glue tables.

###### Request

- `NextToken` – UTF-8 string.

A paginated token to offset the results.

- `MaxResults` – Number (integer), not less than 1 or more than 1000.

The maximum number of results to return.

- `Filter` – A [DataQualityRulesetFilterCriteria](#aws-glue-api-data-quality-api-DataQualityRulesetFilterCriteria "#aws-glue-api-data-quality-api-DataQualityRulesetFilterCriteria") object.

The filter criteria.

- `Tags` – A map array of key-value pairs, not more than 50 pairs.

Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

Each value is a UTF-8 string, not more than 256 bytes long.

A list of key-value pair tags.

###### Response

- `Rulesets` – An array of [DataQualityRulesetListDetails](#aws-glue-api-data-quality-api-DataQualityRulesetListDetails "#aws-glue-api-data-quality-api-DataQualityRulesetListDetails") objects.

A paginated list of rulesets for the specified list of AWS Glue tables.

- `NextToken` – UTF-8 string.

A pagination token, if more results are available.

###### Errors

- `EntityNotFoundException`
- `InvalidInputException`
- `OperationTimeoutException`
- `InternalServiceException`

## UpdateDataQualityRuleset action (Python: update\_data\_quality\_ruleset)

Updates the specified data quality ruleset.

###### Request

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the data quality ruleset.

- `Description` – Description string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

A description of the ruleset.

- `Ruleset` – UTF-8 string, not less than 1 or more than 65536 bytes long.

A Data Quality Definition Language (DQDL) ruleset. For more information,
see the AWS Glue developer guide.

###### Response

- `Name` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the data quality ruleset.

- `Description` – Description string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

A description of the ruleset.

- `Ruleset` – UTF-8 string, not less than 1 or more than 65536 bytes long.

A Data Quality Definition Language (DQDL) ruleset. For more information,
see the AWS Glue developer guide.

###### Errors

- `EntityNotFoundException`
- `AlreadyExistsException`
- `IdempotentParameterMismatchException`
- `InvalidInputException`
- `OperationTimeoutException`
- `InternalServiceException`
- `ResourceNumberLimitExceededException`

## ListDataQualityStatistics action (Python: list\_data\_quality\_statistics)

Retrieves a list of data quality statistics.

###### Request

- `StatisticId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The Statistic ID.

- `ProfileId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The Profile ID.

- `TimestampFilter` – A [TimestampFilter](#aws-glue-api-data-quality-api-TimestampFilter "#aws-glue-api-data-quality-api-TimestampFilter") object.

A timestamp filter.

- `MaxResults` – Number (integer), not less than 1 or more than 1000.

The maximum number of results to return in this request.

- `NextToken` – UTF-8 string.

A pagination token to request the next page of results.

###### Response

- `Statistics` – An array of [StatisticSummary](#aws-glue-api-data-quality-api-StatisticSummary "#aws-glue-api-data-quality-api-StatisticSummary") objects.

A `StatisticSummaryList`.

- `NextToken` – UTF-8 string.

A pagination token to request the next page of results.

###### Errors

- `EntityNotFoundException`
- `InvalidInputException`
- `InternalServiceException`

## TimestampFilter structure

A timestamp filter.

###### Fields

- `RecordedBefore` – Timestamp.

The timestamp before which statistics should be included in the results.

- `RecordedAfter` – Timestamp.

The timestamp after which statistics should be included in the results.

## CreateDataQualityRulesetRequest structure

A request to create a data quality ruleset.

###### Fields

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

A unique name for the data quality ruleset.

- `Description` – Description string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

A description of the data quality ruleset.

- `Ruleset` – _Required:_ UTF-8 string, not less than 1 or more than 65536 bytes long.

A Data Quality Definition Language (DQDL) ruleset. For more information,
see the AWS Glue developer guide.

- `Tags` – A map array of key-value pairs, not more than 50 pairs.

Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

Each value is a UTF-8 string, not more than 256 bytes long.

A list of tags applied to the data quality ruleset.

- `TargetTable` – A [DataQualityTargetTable](#aws-glue-api-data-quality-api-DataQualityTargetTable "#aws-glue-api-data-quality-api-DataQualityTargetTable") object.

A target table associated with the data quality ruleset.

- `RecommendationRunId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

A unique run ID for the recommendation run.

- `DataQualitySecurityConfiguration` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the security configuration created with the data quality encryption
option.

- `ClientToken` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Used for idempotency and is recommended to be set to a random ID (such as
a UUID) to avoid creating or starting multiple instances of the same resource.

## GetDataQualityRulesetResponse structure

Returns the data quality ruleset response.

###### Fields

- `Name` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the ruleset.

- `Description` – Description string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

A description of the ruleset.

- `Ruleset` – UTF-8 string, not less than 1 or more than 65536 bytes long.

A Data Quality Definition Language (DQDL) ruleset. For more information,
see the AWS Glue developer guide.

- `TargetTable` – A [DataQualityTargetTable](#aws-glue-api-data-quality-api-DataQualityTargetTable "#aws-glue-api-data-quality-api-DataQualityTargetTable") object.

The name and database name of the target table.

- `CreatedOn` – Timestamp.

A timestamp. The time and date that this data quality ruleset was created.

- `LastModifiedOn` – Timestamp.

A timestamp. The last point in time when this data quality ruleset was modified.

- `RecommendationRunId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

When a ruleset was created from a recommendation run, this run ID is generated
to link the two together.

- `DataQualitySecurityConfiguration` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the security configuration created with the data quality encryption
option.

## GetDataQualityResultResponse structure

The response for the data quality result.

###### Fields

- `ResultId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

A unique result ID for the data quality result.

- `ProfileId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The Profile ID for the data quality result.

- `Score` – Number (double), not more than 1.0.

An aggregate data quality score. Represents the ratio of rules that passed
to the total number of rules.

- `DataSource` – A [DataSource](#aws-glue-api-data-quality-api-DataSource "#aws-glue-api-data-quality-api-DataSource") object.

The table associated with the data quality result, if any.

- `RulesetName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the ruleset associated with the data quality result.

- `EvaluationContext` – UTF-8 string.

In the context of a job in AWS Glue Studio, each node in the canvas
is typically assigned some sort of name and data quality nodes will have names.
In the case of multiple nodes, the `evaluationContext` can differentiate
the nodes.

- `StartedOn` – Timestamp.

The date and time when the run for this data quality result started.

- `CompletedOn` – Timestamp.

The date and time when the run for this data quality result was completed.

- `JobName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The job name associated with the data quality result, if any.

- `JobRunId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The job run ID associated with the data quality result, if any.

- `RulesetEvaluationRunId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The unique run ID associated with the ruleset evaluation.

- `RuleResults` – An array of [DataQualityRuleResult](#aws-glue-api-data-quality-api-DataQualityRuleResult "#aws-glue-api-data-quality-api-DataQualityRuleResult") objects, not more than 2000 structures.

A list of `DataQualityRuleResult` objects representing
the results for each rule.

- `AnalyzerResults` – An array of [DataQualityAnalyzerResult](#aws-glue-api-data-quality-api-DataQualityAnalyzerResult "#aws-glue-api-data-quality-api-DataQualityAnalyzerResult") objects, not more than 2000 structures.

A list of `DataQualityAnalyzerResult` objects representing
the results for each analyzer.

- `Observations` – An array of [DataQualityObservation](#aws-glue-api-data-quality-api-DataQualityObservation "#aws-glue-api-data-quality-api-DataQualityObservation") objects, not more than 50 structures.

A list of `DataQualityObservation` objects representing
the observations generated after evaluating the rules and analyzers.

- `AggregatedMetrics` – A [DataQualityAggregatedMetrics](#aws-glue-api-data-quality-api-DataQualityAggregatedMetrics "#aws-glue-api-data-quality-api-DataQualityAggregatedMetrics") object.

A summary of `DataQualityAggregatedMetrics` objects showing
the total counts of processed rows and rules, including their pass/fail statistics
based on row-level results.

## StartDataQualityRuleRecommendationRunRequest structure

The request of the Data Quality rule recommendation request.

###### Fields

- `DataSource` – _Required:_ A [DataSource](#aws-glue-api-data-quality-api-DataSource "#aws-glue-api-data-quality-api-DataSource") object.

The data source (AWS Glue table) associated with this run.

- `Role` – _Required:_ UTF-8 string.

An IAM role supplied to encrypt the results of the run.

- `NumberOfWorkers` – Number (integer).

The number of `G.1X` workers to be used in the run. The default
is 5.

- `Timeout` – Number (integer), at least 1.

The timeout for a run in minutes. This is the maximum time that a run can consume
resources before it is terminated and enters `TIMEOUT` status.
The default is 2,880 minutes (48 hours).

- `CreatedRulesetName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

A name for the ruleset.

- `DataQualitySecurityConfiguration` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the security configuration created with the data quality encryption
option.

- `ClientToken` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Used for idempotency and is recommended to be set to a random ID (such as
a UUID) to avoid creating or starting multiple instances of the same resource.

- `AdditionalRunOptions` – A [DataQualityRuleRecommendationRunAdditionalRunOptions](#aws-glue-api-data-quality-api-DataQualityRuleRecommendationRunAdditionalRunOptions "#aws-glue-api-data-quality-api-DataQualityRuleRecommendationRunAdditionalRunOptions") object.

Additional run options you can specify for a recommendation run.

## GetDataQualityRuleRecommendationRunResponse structure

The response for the Data Quality rule recommendation run.

###### Fields

- `RunId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The unique run identifier associated with this run.

- `DataSource` – A [DataSource](#aws-glue-api-data-quality-api-DataSource "#aws-glue-api-data-quality-api-DataSource") object.

The data source (an AWS Glue table) associated with this run.

- `Role` – UTF-8 string.

An IAM role supplied to encrypt the results of the run.

- `NumberOfWorkers` – Number (integer).

The number of `G.1X` workers to be used in the run. The default
is 5.

- `Timeout` – Number (integer), at least 1.

The timeout for a run in minutes. This is the maximum time that a run can consume
resources before it is terminated and enters `TIMEOUT` status.
The default is 2,880 minutes (48 hours).

- `Status` – UTF-8 string (valid values: `RUNNING` | `FINISHED` | `FAILED` | `PENDING_EXECUTION` | `TIMED_OUT` | `CANCELING` | `CANCELED` | `RECEIVED_BY_TASKRUNNER`).

The status for this run.

- `ErrorString` – UTF-8 string.

The error strings that are associated with the run.

- `StartedOn` – Timestamp.

The date and time when this run started.

- `LastModifiedOn` – Timestamp.

A timestamp. The last point in time when this data quality rule recommendation
run was modified.

- `CompletedOn` – Timestamp.

The date and time when this run was completed.

- `ExecutionTime` – Number (integer).

The amount of time (in seconds) that the run consumed resources.

- `RecommendedRuleset` – UTF-8 string, not less than 1 or more than 65536 bytes long.

When a start rule recommendation run completes, it creates a recommended
ruleset (a set of rules). This member has those rules in Data Quality Definition
Language (DQDL) format.

- `CreatedRulesetName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the ruleset that was created by the run.

- `DataQualitySecurityConfiguration` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the security configuration created with the data quality encryption
option.

- `AdditionalRunOptions` – A [DataQualityRuleRecommendationRunAdditionalRunOptions](#aws-glue-api-data-quality-api-DataQualityRuleRecommendationRunAdditionalRunOptions "#aws-glue-api-data-quality-api-DataQualityRuleRecommendationRunAdditionalRunOptions") object.

Additional run options you can specify for a recommendation run.

## BatchPutDataQualityStatisticAnnotation action (Python: batch\_put\_data\_quality\_statistic\_annotation)

Annotate datapoints over time for a specific data quality statistic.
The API requires both profileID and statisticID as part of the InclusionAnnotation
input. The API only works for a single statisticId across multiple profiles.

###### Request

- `InclusionAnnotations` – _Required:_ An array of [DatapointInclusionAnnotation](#aws-glue-api-data-quality-api-DatapointInclusionAnnotation "#aws-glue-api-data-quality-api-DatapointInclusionAnnotation") objects.

A list of `DatapointInclusionAnnotation`'s. The InclusionAnnotations
must contain a profileId and statisticId. If there are multiple InclusionAnnotations,
the list must refer to a single statisticId across multiple profileIds.

- `ClientToken` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Client Token.

###### Response

- `FailedInclusionAnnotations` – An array of [AnnotationError](#aws-glue-api-data-quality-api-AnnotationError "#aws-glue-api-data-quality-api-AnnotationError") objects.

A list of `AnnotationError`'s.

###### Errors

- `EntityNotFoundException`
- `InvalidInputException`
- `InternalServiceException`
- `ResourceNumberLimitExceededException`

## GetDataQualityModel action (Python: get\_data\_quality\_model)

Retrieve the training status of the model along with more information
(CompletedOn, StartedOn, FailureReason).

###### Request

- `StatisticId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The Statistic ID.

- `ProfileId` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The Profile ID.

###### Response

- `Status` – UTF-8 string (valid values: `RUNNING` | `SUCCEEDED` | `FAILED`).

The training status of the data quality model.

- `StartedOn` – Timestamp.

The timestamp when the data quality model training started.

- `CompletedOn` – Timestamp.

The timestamp when the data quality model training completed.

- `FailureReason` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The training failure reason.

###### Errors

- `EntityNotFoundException`
- `InvalidInputException`
- `OperationTimeoutException`
- `InternalServiceException`

## GetDataQualityModelResult action (Python: get\_data\_quality\_model\_result)

Retrieve a statistic's predictions for a given Profile ID.

###### Request

- `StatisticId` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The Statistic ID.

- `ProfileId` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The Profile ID.

###### Response

- `CompletedOn` – Timestamp.

The timestamp when the data quality model training completed.

- `Model` – An array of [StatisticModelResult](#aws-glue-api-data-quality-api-StatisticModelResult "#aws-glue-api-data-quality-api-StatisticModelResult") objects.

A list of `StatisticModelResult`

###### Errors

- `EntityNotFoundException`
- `InvalidInputException`
- `OperationTimeoutException`
- `InternalServiceException`

## ListDataQualityStatisticAnnotations action (Python: list\_data\_quality\_statistic\_annotations)

Retrieve annotations for a data quality statistic.

###### Request

- `StatisticId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The Statistic ID.

- `ProfileId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The Profile ID.

- `TimestampFilter` – A [TimestampFilter](#aws-glue-api-data-quality-api-TimestampFilter "#aws-glue-api-data-quality-api-TimestampFilter") object.

A timestamp filter.

- `MaxResults` – Number (integer), not less than 1 or more than 1000.

The maximum number of results to return in this request.

- `NextToken` – UTF-8 string.

A pagination token to retrieve the next set of results.

###### Response

- `Annotations` – An array of [StatisticAnnotation](#aws-glue-api-data-quality-api-StatisticAnnotation "#aws-glue-api-data-quality-api-StatisticAnnotation") objects.

A list of `StatisticAnnotation` applied to the Statistic

- `NextToken` – UTF-8 string.

A pagination token to retrieve the next set of results.

###### Errors

- `InvalidInputException`
- `InternalServiceException`

## PutDataQualityProfileAnnotation action (Python: put\_data\_quality\_profile\_annotation)

Annotate all datapoints for a Profile.

###### Request

- `ProfileId` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the data quality monitoring profile to annotate.

- `InclusionAnnotation` – _Required:_ UTF-8 string (valid values: `INCLUDE` | `EXCLUDE`).

The inclusion annotation value to apply to the profile.

###### Response

- _No Response parameters._

###### Errors

- `EntityNotFoundException`
- `InvalidInputException`
- `InternalServiceException`
