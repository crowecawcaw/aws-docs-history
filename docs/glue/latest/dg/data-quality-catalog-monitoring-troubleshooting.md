

# Troubleshooting data quality monitoring at the catalog and database level

Use this topic to find out why a data quality evaluation configuration doesn't evaluate a table, why its evaluation runs fail, or why a request to create or update a configuration fails.

**Contents**
+ [Resolving missing evaluation runs for a table](#data-quality-catalog-monitoring-trouble-no-runs)
+ [Resolving failed evaluation runs](#data-quality-catalog-monitoring-trouble-failed-runs)
+ [Resolving errors when you create or update a configuration](#data-quality-catalog-monitoring-trouble-api-errors)

## Resolving missing evaluation runs for a table
<a name="data-quality-catalog-monitoring-trouble-no-runs"></a>

Evaluation configurations work in the background. If AWS Glue Data Quality can't evaluate a table before an evaluation run starts, for example because the role lacks a permission, no run appears for that table. If you don't see runs or results for a table, check the following causes in order.

1. **The evaluation hasn't started yet** – A `ONCE` evaluation starts about a minute after you create the configuration, and evaluations for new tables and metadata changes typically start within a few minutes. When your account is near its quota of concurrent data quality evaluation runs, evaluations wait until capacity is available.

1. **The configuration isn't set to evaluate now** – Call `GetDataQualityEvaluationConfig` and check that `PauseRuns` is `false`, that the triggers match what you expect, and, for a `SCHEDULE` trigger, that the current time is between `StartAt` and `EndAt`. Schedule expressions use UTC.

1. **The table isn't in scope** – Check that the table is in the configuration's catalog and database and that its name matches `TableNamePattern`. Also check whether a more specific configuration applies to the table. A table-level or database-level configuration takes precedence over a broader one, even when it is paused or uses different triggers. For more information, see [When configurations overlap](data-quality-catalog-monitoring.md#data-quality-catalog-monitoring-precedence).

1. **The table was evaluated less than an hour ago** – Each table is evaluated at most once an hour across all of your configurations. A trigger that fires within an hour of the table's previous automatic evaluation skips the table.

1. **The table type isn't supported** – Configurations skip tables that use a JDBC connection, views other than Amazon Athena views, and multi-dialect views. For more information, see [Supported tables](data-quality-catalog-monitoring.md#data-quality-catalog-monitoring-supported-tables).

1. **The trigger doesn't apply to this change** – The `METADATA_CHANGE` trigger responds to changes to the table in the AWS Glue Data Catalog. Writing files to Amazon S3 without updating the table, and adding partitions, don't trigger an evaluation.

1. **The role can't be assumed or lacks permissions** – Permissions can change after you create the configuration. Check that the role's trust policy still allows AWS Glue to assume it, and that its permissions policy includes the actions in [Permissions policy for the configuration role](data-quality-authorization.md#data-quality-authorization-evaluation-configs-permissions). In particular, check `glue:SearchTables`, `glue:GetTable`, `glue:StartDataQualityRulesetEvaluationRun`, and `iam:PassRole` on the role itself. If you use Lake Formation, check that the role has the `DESCRIBE` permission on the table.

1. **The ruleset no longer exists** – If you deleted the ruleset that the configuration's `RulesetName` refers to, recreate it or update the configuration to use another ruleset.

To see the calls that AWS Glue makes on your behalf, look in AWS CloudTrail for events from the configuration's role, such as `AssumeRole`, `SearchTables`, `GetTable`, and `StartDataQualityRulesetEvaluationRun`, and check them for `AccessDenied` errors. When AWS Glue finds the tables in scope and starts their evaluation runs, the role session name begins with `glue-dq-autorun-`.

## Resolving failed evaluation runs
<a name="data-quality-catalog-monitoring-trouble-failed-runs"></a>

When an evaluation run starts but fails, it appears with the `FAILED` status in the list of evaluation runs for the table. To see why, call `GetDataQualityRulesetEvaluationRun` and read `ErrorString`. Common causes include the following:
+ **A rule references a column that the table doesn't have** – A ruleset in a catalog-level or database-level configuration runs against every table in scope. Use rules that apply to any table, or move table-specific rules to a table-level configuration.
+ **The preprocessing query doesn't work for every table** – A `PreProcessingQuery` in a broad configuration must be valid for each table in scope. Use the `{{DATABASE_NAME}}` and `{{TABLE_NAME}}` placeholders, and filter only on columns that every table has.
+ **The role can't read the data** – Check that the role can read the table's data location in Amazon S3, and decrypt it if it uses an AWS KMS key.
+ **Lake Formation denies access to the data** – If the error says `FULL SELECT privileges required on the table`, grant the role the `SELECT` permission on the table without column or data filters. If it says `Insufficient Lake Formation permissions. Verify the data lake settings`, allow external engines to access data with full table access in the Lake Formation data lake settings.

## Resolving errors when you create or update a configuration
<a name="data-quality-catalog-monitoring-trouble-api-errors"></a>

AWS Glue validates a configuration when you create or update it. The following table lists common errors and how to resolve them.


| Error message | Resolution | 
| --- | --- | 
| Unable to assume role for arn: {{role-arn}} with aws:SourceArn {{source-arn}} | Update the role's trust policy to allow glue.amazonaws.com to assume it, with conditions that match your account and the catalog and table ARNs. For an example, see [Trust policy for the configuration role](data-quality-authorization.md#data-quality-authorization-evaluation-configs-trust). | 
| Data quality evaluation configuration role {{role-arn}} is not allowed to describe the {{target}} | Add glue:GetCatalog, glue:GetDatabase, or glue:GetTable to the role's permissions policy, depending on the configuration's level. | 
| ... does not have the Lake Formation DESCRIBE permission on the {{target}} | Grant the DESCRIBE permission in Lake Formation on the catalog, database, or table. The message names the principal that needs it: the configuration's role or the caller. | 
| User: {{caller-arn}} is not authorized to perform: iam:PassRole | Allow the caller to pass the configuration's role to AWS Glue. For more information, see [Permissions to manage evaluation configurations](data-quality-authorization.md#data-quality-authorization-evaluation-configs-caller). | 
| CatalogId must be in the calling account or Cross-account pass role is not allowed. | Create the configuration in the account that owns the catalog, with a role from the same account. | 
| Cannot find Data Quality Ruleset in account {{account-id}} with name {{name}} | Create the ruleset with CreateDataQualityRuleset in the same account and Region before you create the configuration, or check the ruleset name. | 
| ScheduleExpression can run at most hourly, so minutes must be a single value | Use a single value in the minutes field of the cron expression, such as cron(0 \* \* \* ? \*). For rate expressions, use at least one hour. | 
| ScheduleExpression has no future run times | Choose an expression and a StartAt and EndAt window that include at least one future run. | 
| PauseRuns can only be set when Triggers include SCHEDULE or METADATA\_CHANGE | A configuration with only the ONCE trigger can't be paused. To stop it, delete it. | 
| Role is required unless the Update only sets PauseRuns | Include the role in the update request. | 
| Specify either RulesetName or ManagedRulesetName, not both | Choose a built-in ruleset or your own ruleset. | 
| RowLevelResults requires a RulesetName ... | Built-in rulesets contain only analyzers, which don't produce rule results or row-level results. Remove these run options, or use your own ruleset. | 
| Data quality evaluation configuration count ({{count}}) has reached the limit of {{limit}} | Delete configurations that you no longer need, or combine them by using database-level or catalog-level configurations. | 