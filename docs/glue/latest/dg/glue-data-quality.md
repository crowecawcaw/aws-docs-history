# AWS Glue Data Quality

AWS Glue Data Quality allows you to measure and monitor the quality of your data so that you can make
good business decisions. Built on top of the open-source DeeQu framework, AWS Glue Data Quality provides a
managed, serverless experience. AWS Glue Data Quality works with Data Quality Definition Language (DQDL),
which is a domain specific language that you use to define data quality rules. To learn more
about DQDL and supported rule types, see [Data Quality Definition Language (DQDL) reference](dqdl.md "dqdl.md").

For additional product details and pricing, see the service page for [AWS Glue Data Quality](https://aws.amazon.com/glue/features/data-quality "https://aws.amazon.com/glue/features/data-quality").

## Benefits and key features

Benefits and key features of AWS Glue Data Quality include:

- **Serverless** – There is no installation, patching or maintenance.
- **Get started quickly** – AWS Glue Data Quality quickly analyzes your data and creates data quality rules for you.
  You can get started with two clicks: “Create Data Quality Rules → Recommend rules”.
- **Detect data quality issues** – Use machine learning (ML) to detect anomalies and
  hard-to-detect data quality issues.
- **Improvise your rules** – with 25+ out-of-the-box DQ rules to start from, you can create rules
  that suit your specific needs.
- **Evaluate quality and make confident business decisions** – Once you evaluate the rules,
  you get a Data Quality score that provides an overview of the health of your data.
  Use Data Quality score to make confident business decisions.
- **Zero in on bad data** – AWS Glue Data Quality helps you identify the exact records that caused your
  quality scores to go down. Easily identify them, quarantine and fix them.
- **Pay as you go** – There are no annual licenses you need to use AWS Glue Data Quality.
- **No lock-in** – AWS Glue Data Quality is built on open source DeeQu, allowing you to keep the rules you are
  authoring in an open language.
- **Data quality checks** – You can enforce data quality checks on Data Catalog
  and AWS Glue ETL pipelines allowing you to manage data quality at rest and in transit.
- **ML-based data quality detection** – Use machine learning (ML) to detect anomalies and
  hard-to-detect data quality issues.
- **Open language to express rules** – ensures that data quality rules are authored
  consistently and simply. Business users can easily express data quality rules in a straightforward language
  that they can understand. For engineers, this language provides the flexibility to generate code,
  implement consistent version control, and automate deployments.

## How it works

There are two entry points for AWS Glue Data Quality: the AWS Glue Data Catalog and AWS Glue ETL jobs. This
section provides an overview of the use cases and AWS Glue features that each entry point
supports.

### Data

quality for the AWS Glue Data Catalog

AWS Glue Data Quality evaluates objects that are stored in the AWS Glue Data Catalog It offers non-coders an easy way to set up data
quality rules. These personas include data stewards and business analysts.

You might choose this option for the following use cases:

- You want to perform data quality tasks on data sets that you've already
  cataloged in the AWS Glue Data Catalog.
- You work on data governance and need to identify or evaluate data quality
  issues in your data lake on an ongoing basis.

You can manage data quality for the Data Catalog using the following interfaces:

- The AWS Glue management console
- AWS Glue APIs

To get started with AWS Glue Data Quality for the AWS Glue Data Catalog see [Getting started with
AWS Glue Data Quality for the Data Catalog](data-quality-getting-started.md "data-quality-getting-started.md").

### Data quality for AWS Glue ETL jobs

AWS Glue Data Quality for AWS Glue ETL jobs lets you perform _proactive_ data quality tasks. Proactive tasks help you identify and
filter out bad data _before_ you load a data set
into your data lake.

You might choose data quality for ETL jobs for the following use cases:

- You want to incorporate data quality tasks into your ETL jobs
- You want to write code that defines data quality tasks in ETL
  scripts
- You want to manage the quality of data that flows in your visual data
  pipelines

You can manage data quality for ETL jobs using the following interfaces:

- AWS Glue Studio, AWS Glue Studio notebooks, and AWS Glue interactive sessions
- AWS Glue libraries for ETL scripting
- AWS Glue APIs

To get started with data quality for ETL jobs, see [Tutorial: Getting started with
Data Quality](../ug/gs-data-quality-chapter.md "../ug/gs-data-quality-chapter.md") in the _AWS Glue Studio User
Guide_.

### Comparing data quality for the Data Catalog

to data quality for ETL jobs

This table provides an overview of features that each entry point for AWS Glue Data Quality
supports.

| Feature                                             | Data quality for the Data Catalog                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Data quality for ETL jobs                                                                          |
| --------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| Data sources                                        | Amazon S3, Amazon Redshift, JDBC sources compatible with the Data Catalog, and<br>transactional data lake formats such as Apache Iceberg, Apache Hudi, and Delta Lake.<br>AWS Lake Formation managed OTF formats are also supported with some limitations. Amazon Athena views<br>that are cataloged in AWS Glue Data Catalog are not supported. Please see<br>[Supported source types](data-quality-getting-started.md#data-quality-get-started-supported-source-types "data-quality-getting-started.md#data-quality-get-started-supported-source-types"). | All data sources supported by AWS Glue, including custom connectors<br>and third-party connectors. |
| Data Quality rule recommendations                   | Supported                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Not supported                                                                                      |
| Author and run DQDL rules                           | Supported                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Supported                                                                                          |
| Auto scaling                                        | Not supported                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Supported                                                                                          |
| AWS Glue Flex support                               | Not supported                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Supported                                                                                          |
| Scheduling                                          | Supported when evaluating Data Quality rules and via Step Functions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Supported when using Step Functions and workflows.                                                 |
| Identifying records that failed data quality checks | Not supported                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Supported                                                                                          |
| Integration with Amazon Eventbridge                 | Supported                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Supported                                                                                          |
| Integration with AWS Cloudwatch                     | Supported                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Supported                                                                                          |
| Writing data quality results to Amazon S3           | Supported                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Supported                                                                                          |
| Incremental data quality                            | Supported via pushdown predicates                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Supported via AWS Glue bookmarks                                                                   |
| AWS CloudFormation support                          | Supported                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Supported                                                                                          |
| ML-based anomaly detection                          | Not supported                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Supported                                                                                          |
| Dynamic rules                                       | Not supported                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Supported                                                                                          |

## Considerations

Consider the following items before you use AWS Glue Data Quality:

- Data quality rules can't evaluate nested or list-type data sources. See
  [Flatten nested structs](transforms-flatten.md "transforms-flatten.md").

## Terminology

The following list defines terms that are related to AWS Glue Data Quality.

**Data Quality Definition Language (DQDL)**

A domain-specific language that you can use to write AWS Glue Data Quality rules.

To learn more about DQDL, see the [Data Quality Definition Language (DQDL) reference](dqdl.md "dqdl.md") guide.

**data quality**

Describes how well a dataset serves its specific purpose. AWS Glue Data Quality
evaluates rules against a dataset to measure data quality. Each rule checks
for particular characteristics like data freshness or integrity. To quantify
data quality, you can use a _data quality
score_.

**data quality score**

The percentage of data quality rules that pass (result in true) when you
evaluate a ruleset with AWS Glue Data Quality.

**rule**

A DQDL expression that checks your data for a specific characteristic and
returns a Boolean value. For more information, see [Rule structure](dqdl.md#dqdl-syntax-rule-structure "dqdl.md#dqdl-syntax-rule-structure").

**analyzer**

A DQDL expression that gathers data statistics. An analyzer gathers data statistics that can be used by
ML algorithms to detect anomalies and hard-to-detect data quality issues over time.

**ruleset**

An AWS Glue resource that comprises a set of data quality rules. A ruleset
must be associated with a table in the AWS Glue Data Catalog. When you save a ruleset,
AWS Glue assigns an Amazon Resource Name (ARN) to the ruleset.

**data quality score**

The percentage of data quality rules that pass (result in true) when you evaluate a ruleset with
AWS Glue Data Quality.

**observation**

An unconfirmed insight generated by AWS Glue by analyzing data
statistics gathered from rules and analyzers over time.

## Limits

AWS Glue Data Quality service limits:

- You can have 2,000 rules in a ruleset. If your rulesets are larger, we recommend splitting into multiple rulesets.
- The size of the ruleset is 65KB. If your rulesets are larger, we recommend splitting into multiple rulesets.
- AWS Glue Data Quality collects statistics when you create a rule or analyzer. There is no cost associated with storing
  these statistics. However, there is a limit of 100,000 statistics per account, and these statistics will be
  retained for a maximum of two years.

## Release notes for AWS Glue Data Quality

This topic describes features introduced in AWS Glue Data Quality.

### General availability: new features

The following new features are available with the general availability of AWS Glue Data Quality:

- The ability to identify which records failed data quality checks is now supported in AWS Glue Studio
- New data quality ruletypes such as validating referential integrity of data between two data sets, comparing data between two datasets, and data type checks
- Improved user experience in the AWS Glue Data Catalog
- Support for Apache Iceberg, Apache Hudi and Delta Lake
- Support for Amazon Redshift
- Simplified notification with Amazon EventBridge
- AWS CloudFormation support for creating rulesets
- Performance improvements: caching option in ETL and AWS Glue Studio for faster performance when evaluating data quality

### Nov 27, 2023 (Preview)

- ML-powered anomaly detection capabilities are now available in AWS Glue ETL and AWS Glue Studio.
  With this, you can now detect anomalies and hard-to-detect data quality issues
- [Dynamic Rules allows you to provide dynamic thresholds (ex: `RowCount>
avg(last(10))`)](dqdl.md#dqdl-dynamic-rules "dqdl.md#dqdl-dynamic-rules")

### Mar 12, 2024

- DQDL improvements
  - [Support for Keywords like NULL, BLANKS, WHITESPACES_ONLY](dqdl.md#dqdl-keywords-null-empty-whitespaces_only "dqdl.md#dqdl-keywords-null-empty-whitespaces_only")
  - [Options to specify how AWS Glue Data Quality must handle Composite rules](dqdl.md#dqdl-syntax-rule-composition "dqdl.md#dqdl-syntax-rule-composition")
  - [ColumnValues rule type will not allow NULL values to pass during comparisons](dqdl.md#dqdl-keywords-null-empty-whitespaces_only "dqdl.md#dqdl-keywords-null-empty-whitespaces_only")
  - [Support for NOT operator in DQDL](dqdl.md#dqdl-syntax-rule-expressions "dqdl.md#dqdl-syntax-rule-expressions")

### June 26, 2024

- DQDL improvements
  - DQDL now supports [where clause](dqdl.md#dqdl-filtering-data-in-dqdl "dqdl.md#dqdl-filtering-data-in-dqdl")  
    so that you can filter data before applying DQ rules

### August 7, 2024

- Anomaly Detection and Dynamic Rules are now generally available

### Nov 22, 2024

- [Complex composite rules allows you to author more complex business rules with nested support](dqdl.md#dqdl-syntax-rule-composition "dqdl.md#dqdl-syntax-rule-composition")
- New rule types for managing data quality for your files
  - [FileFreshness](dqdl-rule-types-FileFreshness.md "dqdl-rule-types-FileFreshness.md")
  - [FileSize](dqdl-rule-types-FileSize.md "dqdl-rule-types-FileSize.md")
  - [FileUniqueness](dqdl-rule-types-FileUniqueness.md "dqdl-rule-types-FileUniqueness.md")
  - [FileMatch](dqdl-rule-types-FileMatch.md "dqdl-rule-types-FileMatch.md")

- Default data quality checks in Visual ETL jobs

### Dec 6, 2024

- AWS Glue Data Quality now supports Amazon SageMaker AI LakeHouse tables and AWS Lake Formation managed
  Iceberg, Delta and HUDI tables in AWS Glue ETL 5.0.

### Jul 7, 2025

- AWS Glue Data Quality; now supports Amazon S3 Tables, RMS, Lakehouse and AWS Lake Formation managed Iceberg tables in
  AWS Glue Data Catalog.

### Nov 21, 2025

- AWS Glue Data Quality now supports rule labeling for enhanced reporting. You can organize and analyze data quality results more effectively by querying results by specific labels to identify failing rules within particular categories, count rule outcomes by team or domain, and create focused reports for different stakeholders. For more information, see [Labels](dqdl.md#dqdl-labels "dqdl.md#dqdl-labels").
- AWS Glue Data Quality now supports Constants in DQDL, allowing you to define constant values and reference them throughout your script. This helps prevent issues related to query size limits when working with large SQL statements. For more information, see [Constants](dqdl.md#dqdl-constants "dqdl.md#dqdl-constants").
