# Getting started with

AWS Glue Data Quality for the Data Catalog

This
getting
started
section
provides instructions to help you get started with AWS Glue Data Quality on the
AWS Glue console. You'll learn how to complete essential tasks such as
generating data quality rule recommendations and evaluating a ruleset against your data.

###### Topics

- [Prerequisites](#data-quality-prereqs "#data-quality-prereqs")
- [Step-by-step example](#data-quality-step-by-step-example "#data-quality-step-by-step-example")
- [Generating rule recommendations](#data-quality-get-recommendations "#data-quality-get-recommendations")
- [Monitoring rule recommendations](#data-quality-monitor-recommendations "#data-quality-monitor-recommendations")
- [Editing recommended rulesets](#data-quality-edit-ruleset "#data-quality-edit-ruleset")
- [Creating a new ruleset](#data-quality-create-ruleset "#data-quality-create-ruleset")
- [Running a ruleset to evaluate data quality](#data-quality-run-data-quality-task "#data-quality-run-data-quality-task")
- [Viewing the data quality score and results](#data-quality-view-results "#data-quality-view-results")
- [Supported source types](#data-quality-get-started-supported-source-types "#data-quality-get-started-supported-source-types")
- [Related topics](#data-quality-get-started-related "#data-quality-get-started-related")

## Prerequisites

Before you use AWS Glue Data Quality, you should be familiar with using
the
Data Catalog and crawlers in AWS Glue.
With
AWS Glue Data Quality,
you can
evaluate
quality for tables in a
Data Catalog
database. You also need the following:

- A table in
  the
  Data Catalog to evaluate your data quality
  ruleset against.
- An IAM role for AWS Glue that you supply when you generate rule recommendations or run a data quality task.
  This role must have permission to access resources that various AWS Glue Data Quality processes require to run on your behalf.
  These resources include AWS Glue, Amazon S3, and CloudWatch. To view example policies that include the minimum permissions for
  AWS Glue Data Quality, see [Example IAM policies](data-quality-authorization.md#data-quality-authorization-example-policy "data-quality-authorization.md#data-quality-authorization-example-policy").

To learn more about IAM roles for AWS Glue, see [Create an IAM policy for the
AWS Glue service](create-service-policy.md "create-service-policy.md") and [Create an IAM role for the
AWS Glue service](create-an-iam-role.md "create-an-iam-role.md"). You can also view a list of all
AWS Glue permissions that are specific to data quality in [Authorization for
AWS Glue Data Quality
actions](data-quality-authorization.md "data-quality-authorization.md").

- A database with at least one table
  that
  contains
  a variety of data. The table used in this tutorial is named
  `yyz-tickets`, with the table `tickets`. This data is
  a collection of publicly available information from the City of Toronto for
  parking citations. If you create your own table, make sure
  that
  it's populated with a variety of valid data to get the
  best
  set of
  recommended rules.

## Step-by-step example

For a step-by-step example with sample datasets, see
the
[AWS Glue Data Quality
blog
post](https://aws.amazon.com/blogs/big-data/getting-started-with-aws-glue-data-quality-from-the-aws-glue-data-catalog/ "https://aws.amazon.com/blogs/big-data/getting-started-with-aws-glue-data-quality-from-the-aws-glue-data-catalog/").

## Generating rule recommendations

Rule recommendations make it easy to get started with data quality without writing
code. With
AWS Glue Data Quality,
you can
analyze your
data,
identify
rules, and
create a
ruleset that you can evaluate in a data quality task. Recommendation runs are automatically deleted after 90 days.

###### To generate data quality rule

recommendations

1. Open the AWS Glue console at [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/ "https://console.aws.amazon.com/glue/").
2. Choose **Tables** in the navigation pane. Then choose the table that you want to generate data quality rule recommendations for.
3. On the table details page, select the **Data quality** tab to access AWS Glue Data Quality rules and settings for your table.
4. On
   the **Data quality** tab, choose **Add rules and
   monitor data quality**.
5. On the **Ruleset builder** page, an alert at the top of the page will prompt you to start a recommendation task if there
   are no rule recommendation runs.
6. Choose **Recommend rules** to open the modal and input your parameters for the recommendation task.
7. Choose an
   IAM
   role
   with access to AWS Glue. This role must have permission to access resources that
   various AWS Glue Data Quality processes require to run on your behalf.
8. After
   the fields are completed according to your preferences, choose
   **Recommend rules** to start the recommendation task run.
   If recommendation runs are in progress or completed, you can manage your runs in
   this alert. You
   might
   need to refresh the alert to view the status change. Completed and in-progress
   recommendation task runs appear in the **Run history** page
   that lists all recommendation runs for the past 90 days.

### What the recommended rules mean

AWS Glue Data Quality generates rules based on the data from each column of the input
table.
It
uses
the
rules
to identify potential boundaries where data can be filtered to maintain quality
requirements.
The following
list of generated rules
includes
examples that are useful for understanding what the rules mean and what they might
do when applied to your data.

For a full list of
the generated
Data Quality Definition Language
(DQDL)
rule types, see [DQDL rule type
reference](dqdl.md#dqdl-rule-types "dqdl.md#dqdl-rule-types").

- `IsComplete "SET_FINE_AMOUNT"`
  –The
  `IsComplete` rule verifies that the column is filled in for
  any given row.
  Use
  this
  rule
  to
  tag columns as non-optional in data.
- `Uniqueness "TICKET_NUMBER" > 0.95`
  –
  The `Uniqueness` rule verifies that the data within the column
  meets some threshold of uniqueness. In this example, the data
  that
  populates
  any given row for `"TICKET_NUMBER"` was determined to be at most
  95% identical in content to all other rows,
  which
  suggests
  this rule.
- `ColumnValues "PROVINCE" in ["ON", "QC", "AB", "NY",...]`
  –
  The `ColumnValues` rule defines valid values for the column,
  based on
  existing
  column contents. In this example, the data for each row is a 2-letter
  license code plate for a state or province.
- `ColumnLength "INFRACTION_DESCRIPTION" between 15 and 31`
  –
  The `ColumnLength` rule enforces a length restriction on a
  column's data. This rule is generated from the sample data based on the
  minimum and maximum recorded lengths for a column of strings.

## Monitoring rule recommendations

When data quality rule recommendations are running, the **Add rules and
monitor data quality** page displays information and additional actions
that
you can take in the top bar.

When rule recommendations are in progress, you can choose **Stop
run** before the recommendation task is complete. While the task is in
progress, you will see the status,
**in
progress**, and the date and time when the run started.

When the
rule recommendations are complete, the rule recommendation bar
displays the number of rules recommended, the status of the last recommendation run, and
the date and timestamp when it finished.

You can add the recommended rules by choosing
**Insert Rule Recommendation**. To view previously recommended
rules,
select a specific date. To run a new recommendation, choose
**More actions**,
and
then
choose
**Recommended rules**.

Set default settings by choosing **Manage user settings**. You can
set the default path for Amazon S3 to store rulesets or to set
up a default role to run
the
Data Catalog.

## Editing recommended rulesets

Because
AWS Glue Data Quality generates rules based on
existing
data that
you have available, you
might
see some unexpected or undesirable rules in the automated suggestions. In order to get
the most out of
the
recommended rulesets,
you
need to evaluate and modify them. For this step of the tutorial,
you
take the rules generated in the previous step and adjust them to enforce more
restrictive qualities on some data.
You
also
relax other
rules
to ensure that correct, unique data can be added later.

###### Edit a suggested ruleset

1. In the AWS Glue console, choose
   **Data
   Catalog**, and then choose **Databases
   tables**
   in the navigation pane.
   Choose
   the table `tickets`.
2. On the table details page,
   choose
   the **Data quality** tab to access AWS Glue Data Quality rules and settings
   for the table.
3. In the **Rulesets** section, select the ruleset generated in
   [Generating rule recommendations](#data-quality-get-recommendations "#data-quality-get-recommendations").
4. Choose
   **Actions**,
   and then choose
   **Edit**
   in the console window. The ruleset editor loads in the
   console.
   It
   includes an editing pane for your rules and a quick reference for DQDL.
5. Remove line `2` of the
   script.
   This
   relaxes
   the requirement that the database size
   is
   constrained within a certain number of rows. After the
   edit,
   your file should contain the following on lines
   1–3:

```
Rules = [
    IsComplete "TAG_NUMBER_MASKED",
    ColumnLength "TAG_NUMBER_MASKED" between 6 and 9,
```

6. Remove line `25` of the
   script.
   This
   relaxes
   the requirement that 96% of recorded provinces are
   `ON`. After the
   edit,
   your file should contain the following from line `24` to the end of
   the ruleset:

```
ColumnValues "PROVINCE" in ["ON", "QC", "AB", "NY", "AZ", "NS", "BC", "MI", "PQ", "MB", "PA", "FL", "SK", "NJ", "OH", "NB", "IL", "MA", "CA",
    "VA", "TX", "NF", "MD", "PE", "CT", "NC", "GA", "IN", "OR", "MN", "TN", "WI", "KY", "MO", "WA", "NH", "SC", "CO", "OK", "VT", "RI", "ME", "AL",
    "YT", "IA", "DE", "AR", "LA", "XX", "WV", "MT", "KS", "NT", "DC", "NV", "NE", "UT", "MS", "NM", "ID", "SD", "ND", "AK", "NU", "GO", "WY", "HI"],
ColumnLength "PROVINCE" = 2
]
```

7. Change line `14` to the following:

```
IsComplete "TIME_OF_INFRACTION",
```

This _strengthens_ the requirement on the
column
by limiting the database to only tickets
that
contain
a recorded time of infraction.
You
should always consider
tickets without a recorded time of infraction
to
be
invalid
data in this
dataset.
This is
different than situations where partitioning or transformation might be more
appropriate for further data use or inspection to determine a quality
rule. 8. Choose
**Update
Ruleset**at the bottom of the console
page.

## Creating a new ruleset

A ruleset is a group of data quality rules that you evaluate against your data. In the AWS Glue console, you can author custom
rulesets using Data Quality Definition Language (DQDL).

###### To create a data quality ruleset

1. In the AWS Glue console, choose
   **Data
   Catalog**, choose **Databases**, and then choose
   **Tables**
   in the navigation pane. Select the table `tickets`.
2. Open the **Data quality** tab.
3. In the **Rulesets** section, choose
   **Create ruleset**. The DQDL editor launches in the
   console.
   It
   has
   a text area for direct
   editing,
   and a quick reference for DQDL rules and the table schema.
4. Start adding rules to the text area of the DQDL editor. You can either write
   rules directly from this tutorial, or use the **DQDL rule
   builder** feature of the
   data
   quality rules editor.

###### Note

###### How to use the DQDL rule builder

    1. Select a rule type from the list, and select the
     plus sign to insert example syntax into the editor
     pane.
    2. Exchange the placeholder column names with your
     own column names. Column names from the table are available in the
     **Schema** tab.
    3. Update the expression parameter as you see fit.
     For a full list of expressions that DQDL supports, see
     [Expressions](dqdl.md#dqdl-syntax-rule-expressions "dqdl.md#dqdl-syntax-rule-expressions").

As an
example,
the
following rules are constraints for data validation of the
`ticket_number` column in the `tickets`
table.
To add the
following rules,
use
the
DQDL rule builder or directly edit your
ruleset:

```
IsComplete "ticket_number",
IsUnique "ticket_number",
ColumnValues "ticket_number" > 9000000000
```

5. Provide a name for your new ruleset in the **Ruleset name** field.
6. Choose
   **Save ruleset**.

### Evaluating data quality across multiple datasets

You can set
up
data
quality
rules across multiple datasets using
ReferentialIntegrity
and
DatasetMatch rulesets.
ReferentialIntegrity
checks to see if data in the primary dataset is present in other datasets.

To add a reference dataset,
choose
the **Schema** tab and
then
choose **Update reference tables**. You will be
prompted to select a database and
a
table. You can add the table and then set
up
data quality
rules. Rule
types like AggregateMatch, RowCountMatch, ReferentialIntegrity,
SchemaMatch, and DatasetMatch support the ability to perform
data
quality
checks across multiple
datasets.

## Running a ruleset to evaluate data quality

When you run a data quality task, AWS Glue Data Quality evaluates a ruleset against your data and
calculates a data quality score. This score represents the percentage of data quality
rules that passed for the input.

###### To run a data quality task

1. In the AWS Glue console, choose
   **Data
   Catalog**, choose **Databases**, and then choose
   **Tables**
   in the navigation pane. Select the table `tickets`.
2. Choose
   the **Data quality** tab.
3. In the **Rulesets** list, select the ruleset that you want to
   evaluate against the table. For this step, we recommend using a ruleset
   that
   you've written or modified already rather than generated
   rules. Choose **Run**.
4. In the modal, choose your IAM role. This role must have permission to
   access resources that various AWS Glue Data Quality processes require to run on your behalf.
   You can save the IAM role as
   the
   default or modify
   it
   by going to the
   **Default
   Setting** page.
5. Under **Data quality actions**, choose whether you want to
   **Publish metrics to Amazon CloudWatch**. When
   this
   option is selected, AWS Glue Data Quality publishes metrics that indicate
   the number of rules that passed and the number of rules that failed.
   To take
   action on
   metrics
   stored this
   way, you
   can
   use
   CloudWatch alarms. Key metrics are also published to Amazon EventBridge for
   you to set
   up alerts. For more information, see [Setting
   up alerts, deployments, and
   scheduling](data-quality-alerts.md "data-quality-alerts.md").
6. In **Run Frequency**, choose run on demand or schedule the
   ruleset. When you schedule a ruleset,
   you're
   prompted for a task name. The schedule will be created in
   Amazon EventBridge. You can edit your schedule in
   Amazon EventBridge.
7. To save the data quality results in Amazon S3, select a
   **Data quality results location**. The
   IAM
   role
   that you previously selected for this task must have write access to this
   location.
8. Under
   **Additional
   Configurations**, enter the **Requested
   number of workers** that you want AWS Glue to allocate for your data
   quality task.
9. You can optionally set
   up a filter at the data source. This helps you reduce the data
   that
   you're
   reading.
   You
   can also use a
   filter
   to run incremental validations by selecting partition information and passing
   them as parameters via API calls.
   To improve
   performance,
   you
   can
   provide
   a
   partition
   predicate.
10. Choose **Run**. You should see your new task in the
    **Data quality task runs** list. When the **Run
    status** column for the task shows
    as
    **Completed**, you can view the quality
    score results. You
    might
    need to refresh your console window for the status to update correctly.
11. To view
    the column for the data quality result details,
    choose
    the “+” icon to expand the
    ruleset.
    The results show you
    the
    rules that
    passed and failed in the evaluation, and what triggered
    the
    rule
    failure.

## Viewing the data quality score and results

###### To see the latest run on all created rulesets

1. In the AWS Glue console, choose **Tables** in the navigation pane.
   Then choose the table that you want to run a data quality task for.
2. Choose the **Data quality** tab.
3. The **Data quality snapshot** shows a general trend of runs
   over time. The last
   10
   runs over all rulesets are displayed by default. To filter by ruleset, select
   the desired one from the
   dropdown
   list. If there are less than 10 runs, all the completed runs
   that are available are displayed.
4. In the **Data quality** table, each ruleset with
   its
   latest run
   (if
   there is
   one)
   is shown, along with the score. Expanding the ruleset displays the rules that
   are in that ruleset, along with the
   rule
   results for that run.

###### To see the latest run on a particular ruleset

1. In the AWS Glue console, choose **Tables** in the navigation pane.
   Then choose the table that you want to run a data quality task for.
2. Choose the **Data quality** tab.
3. In the **Data quality** table, choose on a specific ruleset.
4. On
   the **Ruleset details** page, choose the **Run
   history** tab.

All of the evaluation runs for this particular ruleset are listed in the table within this tab.
You can see the history of the scores and the status of the runs. 5. To see more information about a particular run, choose the **Run
ID** to go to the **Evaluation run details** page.
On this
page,
you can see specifics about the run and more details about the status of
individual rule results.

## Supported source types

| Table type support by AWS Lake Formation configuration | Table Type     | AWS Lake Formation - All Table Access | AWS Lake Formation Enabled with Columns | AWS Lake Formation Enabled with Data Filters | Cross-Account AWS Lake Formation Support - All Table Access | AWS Lake Formation Disabled                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------------------------------------ | -------------- | ------------------------------------- | --------------------------------------- | -------------------------------------------- | ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Parquet                                                | Supported      | Not Supported                         | Not Supported                           | Supported                                    | Supported                                                   |
| ORC                                                    | Supported      | Not Supported                         | Not Supported                           | Supported                                    | Supported                                                   |
| CSV, JSON, TSV                                         | Supported      | Not Supported                         | Not Supported                           | Supported                                    | Supported                                                   |
| Avro                                                   | Supported      | Not Supported                         | Not Supported                           | Supported                                    | Supported                                                   |
| JSON                                                   | Supported      | Not Supported                         | Not Supported                           | Supported                                    | Supported                                                   |
| Iceberg                                                | Supported      | Not Supported                         | Not Supported                           | Supported                                    | Supported                                                   |
| HUDI                                                   | Not Supported  | Not Supported                         | Not Supported                           | Not Supported                                | Supported                                                   |
| Delta                                                  | Not Supported  | Not Supported                         | Not Supported                           | Not Supported                                | Supported                                                   |
| RMS                                                    | Supported\*    | Supported\*                           | Supported\*                             | Not Supported                                | Not Supported                                               |
| Amazon S3 Tables                                       | Supported\*    | Not Supported                         | Not Supported                           | Not applicable                               | Supported                                                   |
| Amazon RDS and Aurora                                  | Not applicable | Not applicable                        | Not applicable                          | Not applicable                               | Not Supported                                               |
| JDBC                                                   | Not applicable | Not applicable                        | Not applicable                          | Not applicable                               | Supported                                                   | \* Amazon S3 tables and SageMaker Lakehouse support in AWS Glue Console is not supported. Currently, Amazon S3 table and SageMaker Lakehouse Data Catalog Recommendation Runs and Data Catalog Data Quality Evaluation runs are only supported via the CLI. ### Other known limitations <br>• Delta Lake Symlink Tables: Not supported for AWS Glue Data Quality recommendation runs or Data Catalog Data Quality evaluation runs. <br>• Amazon S3 Table Asset publishing in SageMaker Unified Studio: Currently, publishing Amazon S3 Tables as Assets in SageMaker Unified Studio is unavailable; visualizing Amazon S3 Table Data Quality runs is unavailable from SageMaker Unified Studio as a result. ## Related topics <br>• [DQDL rule type reference](dqdl-rule-types.md "dqdl-rule-types.md") <br>• [Data Quality Definition Language (DQDL) reference](dqdl.md "dqdl.md") |
