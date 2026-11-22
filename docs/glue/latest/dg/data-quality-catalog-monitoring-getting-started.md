

# Getting started with data quality monitoring at the catalog and database level

Data quality monitoring at the catalog and database level evaluates every table in a AWS Glue Data Catalog catalog or database from a single data quality evaluation configuration, including tables that you add later. To learn how configurations choose tables, triggers, and rulesets, see [Data quality monitoring at the catalog and database level](data-quality-catalog-monitoring.md).

In this topic, you create an IAM role, create a configuration for a database with the AWS CLI, and then find its results. Each CLI command has a matching operation in the AWS SDKs. In the examples, replace the values in {{italics}} with your own, and replace `111122223333` with your account ID.

**Contents**
+ [Prerequisites](#data-quality-catalog-monitoring-gs-prereqs)
+ [Step 1: Create an IAM role for the configuration](#data-quality-catalog-monitoring-gs-role)
+ [Step 2: Create a data quality evaluation configuration](#data-quality-catalog-monitoring-gs-create)
+ [Step 3: View the results](#data-quality-catalog-monitoring-gs-results)
+ [More configuration examples](#data-quality-catalog-monitoring-gs-examples)
  + [Evaluate a whole catalog on a schedule](#data-quality-catalog-monitoring-gs-example-catalog-schedule)
  + [Evaluate tables that match a name pattern](#data-quality-catalog-monitoring-gs-example-pattern)
  + [Evaluate a table with your own rules](#data-quality-catalog-monitoring-gs-example-custom)
  + [Evaluate recent data only](#data-quality-catalog-monitoring-gs-example-preprocessing)
  + [Evaluate tables in Amazon S3 Tables](#data-quality-catalog-monitoring-gs-example-s3tables)
+ [Managing evaluation configurations](#data-quality-catalog-monitoring-gs-manage)
  + [List configurations](#data-quality-catalog-monitoring-gs-list)
  + [Update a configuration](#data-quality-catalog-monitoring-gs-update)
  + [Pause and resume a configuration](#data-quality-catalog-monitoring-gs-pause)
  + [Delete a configuration](#data-quality-catalog-monitoring-gs-delete)
+ [Example: Manage configurations with the AWS SDK for Python (Boto3)](#data-quality-catalog-monitoring-gs-python)

## Prerequisites
<a name="data-quality-catalog-monitoring-gs-prereqs"></a>

Before you begin, make sure that you have the following:
+ One or more tables in the AWS Glue Data Catalog with data in Amazon S3 or Amazon S3 Tables.
+ The latest version of the AWS CLI or the AWS SDK that you use, so that it includes the data quality evaluation configuration operations.
+ Permissions to manage evaluation configurations, to pass the configuration's IAM role, and, if you use Lake Formation, the Lake Formation permissions on the catalog, database, or table. For more information about these permissions, see [Permissions to manage evaluation configurations](data-quality-authorization.md#data-quality-authorization-evaluation-configs-caller).

## Step 1: Create an IAM role for the configuration
<a name="data-quality-catalog-monitoring-gs-role"></a>

AWS Glue Data Quality assumes the configuration's role to find the tables in scope, start an evaluation run for each table, and read the table's data during the run. The role needs a trust policy that allows AWS Glue to assume it, and a permissions policy for these tasks.

**To create the configuration role**

1. Open a terminal where the AWS CLI is configured for the account that owns your tables.

1. Save the trust policy from [Trust policy for the configuration role](data-quality-authorization.md#data-quality-authorization-evaluation-configs-trust) as `trust-policy.json`, replacing the Region and account ID with your own.

1. Save the permissions policy from [Permissions policy for the configuration role](data-quality-authorization.md#data-quality-authorization-evaluation-configs-permissions) as `permissions-policy.json`, replacing the Region, account ID, role name, and Amazon S3 bucket with your own.

1. Create the role. The examples in this topic use the role name `DataQualityEvaluationConfigRole`. If you choose another name, replace it in the commands and policies.

   ```bash
   aws iam create-role \
     --role-name {{DataQualityEvaluationConfigRole}} \
     --assume-role-policy-document file://trust-policy.json
   ```

1. Attach the permissions policy to the role. Replace `DataQualityEvaluationConfigPolicy` with a name for the policy.

   ```bash
   aws iam put-role-policy \
     --role-name {{DataQualityEvaluationConfigRole}} \
     --policy-name {{DataQualityEvaluationConfigPolicy}} \
     --policy-document file://permissions-policy.json
   ```

1. If you use Lake Formation, grant the role the Lake Formation permissions in [Permissions policy for the configuration role](data-quality-authorization.md#data-quality-authorization-evaluation-configs-permissions). The configuration evaluates only the tables that its role can describe.

## Step 2: Create a data quality evaluation configuration
<a name="data-quality-catalog-monitoring-gs-create"></a>

The following command creates a configuration at the database level that gathers baseline statistics for every table in a database. It uses the default settings: the `SIMPLE` built-in ruleset and the `ONCE` trigger.

```bash
aws glue create-data-quality-evaluation-config \
  --name {{my-database-config}} \
  --level DATABASE \
  --data-source '{
    "GlueTables": {
      "CatalogId": "111122223333",
      "DatabaseName": "{{my_database}}"
    }
  }' \
  --role {{DataQualityEvaluationConfigRole}}
```

The response returns the name of the configuration.

```json
{
    "Name": "my-database-config",
    "EvaluationRunMode": "EVALUATION_CONFIG"
}
```

When you create a configuration, AWS Glue checks that the catalog, database, or table exists, that your role can be assumed and can describe it, and that the ruleset, if you specify one, exists. About a minute later, the `ONCE` trigger starts an evaluation run for each table in the database. Because this configuration includes `ONCE`, tables that you add to the database later are each evaluated once when they are created.

To confirm the settings that the configuration uses, call `get-data-quality-evaluation-config`.

```bash
aws glue get-data-quality-evaluation-config --name {{my-database-config}}
```

```json
{
    "Name": "my-database-config",
    "EvaluationRunMode": "EVALUATION_CONFIG",
    "CreatedOn": "2026-11-16T17:02:11.512000+00:00",
    "LastModifiedOn": "2026-11-16T17:02:11.512000+00:00",
    "Level": "DATABASE",
    "DataSource": {
        "GlueTables": {
            "CatalogId": "111122223333",
            "DatabaseName": "my_database"
        }
    },
    "ManagedRulesetName": "SIMPLE",
    "Triggers": [
        "ONCE"
    ],
    "PauseRuns": false,
    "Role": "arn:aws:iam::111122223333:role/DataQualityEvaluationConfigRole"
}
```

AWS Glue returns the role as a full ARN, even if you specified a role name.

## Step 3: View the results
<a name="data-quality-catalog-monitoring-gs-results"></a>

Each evaluation stores its results with the table. To list the results that your configuration produced for a table, filter `list-data-quality-results` on the table, the evaluation run mode, and the configuration name.

```bash
aws glue list-data-quality-results \
  --filter '{
    "DataSource": {
      "GlueTable": {
        "DatabaseName": "{{my_database}}",
        "TableName": "{{my_table}}"
      }
    },
    "EvaluationRunMode": "EVALUATION_CONFIG",
    "DataQualityEvaluationConfig": "{{my-database-config}}"
  }'
```

Each result in the response includes `EvaluationRunMode` and `DataQualityEvaluationConfig`, so you can tell results from your configurations apart from results of runs that you started yourself.

```json
{
    "Results": [
        {
            "ResultId": "dqresult-a1b2c3d4e5f6EXAMPLE",
            "DataSource": {
                "GlueTable": {
                    "DatabaseName": "my_database",
                    "TableName": "my_table",
                    "CatalogId": "111122223333"
                }
            },
            "StartedOn": "2026-11-16T17:04:38.204000+00:00",
            "EvaluationRunMode": "EVALUATION_CONFIG",
            "DataQualityEvaluationConfig": "my-database-config"
        }
    ]
}
```

A built-in ruleset gathers statistics rather than evaluating rules. To view the statistics, get the result's profile ID and list its statistics. In the second command, replace {{profile-id}} with the profile ID that the first command returns.

```bash
aws glue get-data-quality-result \
  --result-id {{dqresult-a1b2c3d4e5f6EXAMPLE}} \
  --query ProfileId --output text

aws glue list-data-quality-statistics \
  --profile-id {{profile-id}}
```

You can also see each run in the list of evaluation runs for the table, including runs that failed.

```bash
aws glue list-data-quality-ruleset-evaluation-runs \
  --filter '{
    "DataSource": {
      "GlueTable": {
        "DatabaseName": "{{my_database}}",
        "TableName": "{{my_table}}"
      }
    }
  }'
```

If no results appear after a few minutes, see [Troubleshooting data quality monitoring at the catalog and database level](data-quality-catalog-monitoring-troubleshooting.md).

## More configuration examples
<a name="data-quality-catalog-monitoring-gs-examples"></a>

The following examples show configurations for other levels, triggers, and rulesets. Replace the values in {{italics}} with your own, and replace `111122223333` with your account ID.

### Evaluate a whole catalog on a schedule
<a name="data-quality-catalog-monitoring-gs-example-catalog-schedule"></a>

The following configuration profiles every table in the account's default catalog every 24 hours, starting on December 1, 2026. A rate expression, such as `rate(24 hours)`, runs at a fixed interval. Because new tables are always evaluated, tables that you add to the catalog are also profiled when they are created.

```bash
aws glue create-data-quality-evaluation-config \
  --name {{my-catalog-config}} \
  --level CATALOG \
  --data-source '{"GlueTables": {"CatalogId": "111122223333"}}' \
  --managed-ruleset-name SIMPLE \
  --triggers SCHEDULE \
  --schedule-expression "rate(24 hours)" \
  --start-at {{2026-12-01T00:00:00Z}} \
  --role {{DataQualityEvaluationConfigRole}}
```

To run at a specific time of day instead, use a cron expression. For example, `cron(0 6 * * ? *)` runs every day at 6:00 AM UTC.

### Evaluate tables that match a name pattern
<a name="data-quality-catalog-monitoring-gs-example-pattern"></a>

The following configuration evaluates only the tables in a database whose names start with a prefix, every 12 hours, and whenever their metadata changes. It uses the `ADVANCED` built-in ruleset, which gathers more statistics for anomaly detection to learn from.

```bash
aws glue create-data-quality-evaluation-config \
  --name {{my-pattern-config}} \
  --level DATABASE \
  --data-source '{
    "GlueTables": {
      "CatalogId": "111122223333",
      "DatabaseName": "{{my_other_database}}",
      "TableNamePattern": "{{my_prefix_}}*"
    }
  }' \
  --managed-ruleset-name ADVANCED \
  --triggers SCHEDULE METADATA_CHANGE \
  --schedule-expression "rate(12 hours)" \
  --role {{DataQualityEvaluationConfigRole}}
```

### Evaluate a table with your own rules
<a name="data-quality-catalog-monitoring-gs-example-custom"></a>

To hold a table to specific standards, create a ruleset with `create-data-quality-ruleset`, and then create a table-level configuration that uses it. For a `TABLE` configuration, set `TableNamePattern` to the table name. This configuration takes precedence over the database configuration from Step 2 for this table. It runs at the start of every hour.

```bash
aws glue create-data-quality-ruleset \
  --name {{my-ruleset}} \
  --ruleset 'Rules = [
    RowCount > 0,
    IsComplete "{{id_column}}",
    IsUnique "{{id_column}}"
  ]'

aws glue create-data-quality-evaluation-config \
  --name {{my-table-config}} \
  --level TABLE \
  --data-source '{
    "GlueTables": {
      "CatalogId": "111122223333",
      "DatabaseName": "{{my_database}}",
      "TableNamePattern": "{{my_table}}"
    }
  }' \
  --ruleset-name {{my-ruleset}} \
  --triggers SCHEDULE \
  --schedule-expression "cron(0 * * * ? *)" \
  --role {{DataQualityEvaluationConfigRole}}
```

### Evaluate recent data only
<a name="data-quality-catalog-monitoring-gs-example-preprocessing"></a>

To evaluate a subset of each table, add a `PreProcessingQuery` to the data source. In catalog-level and database-level configurations, use the `{{DATABASE_NAME}}` and `{{TABLE_NAME}}` placeholders so that the query reads each table in scope. The following configuration evaluates the last seven days of data in each table of a database every day at 2:00 AM UTC. Each table in scope must have the column that the query filters on.

```bash
aws glue create-data-quality-evaluation-config \
  --name {{my-recent-data-config}} \
  --level DATABASE \
  --data-source '{
    "GlueTables": {
      "CatalogId": "111122223333",
      "DatabaseName": "{{my_database}}",
      "PreProcessingQuery": "SELECT * FROM `{{DATABASE_NAME}}.{{TABLE_NAME}}` WHERE {{date_column}} >= date_sub(current_date(), 7)"
    }
  }' \
  --triggers SCHEDULE \
  --schedule-expression "cron(0 2 * * ? *)" \
  --role {{DataQualityEvaluationConfigRole}}
```

### Evaluate tables in Amazon S3 Tables
<a name="data-quality-catalog-monitoring-gs-example-s3tables"></a>

For Amazon S3 Tables, set `CatalogId` to the Amazon S3 Tables catalog for your table bucket, and `DatabaseName` to the namespace. The following configuration profiles every table in a namespace every Monday at 3:00 AM UTC. You and the role also need Amazon S3 Tables permissions. For more information about these permissions, see [Permissions to manage evaluation configurations](data-quality-authorization.md#data-quality-authorization-evaluation-configs-caller) and [Permissions policy for the configuration role](data-quality-authorization.md#data-quality-authorization-evaluation-configs-permissions).

```bash
aws glue create-data-quality-evaluation-config \
  --name {{my-s3-tables-config}} \
  --level DATABASE \
  --data-source '{
    "GlueTables": {
      "CatalogId": "111122223333:s3tablescatalog/{{amzn-s3-demo-table-bucket}}",
      "DatabaseName": "{{my_namespace}}"
    }
  }' \
  --triggers SCHEDULE \
  --schedule-expression "cron(0 3 ? * MON *)" \
  --role {{DataQualityEvaluationConfigRole}}
```

## Managing evaluation configurations
<a name="data-quality-catalog-monitoring-gs-manage"></a>

### List configurations
<a name="data-quality-catalog-monitoring-gs-list"></a>

To list the configurations in your account and Region, call `list-data-quality-evaluation-configs`. You can filter by level.

```bash
aws glue list-data-quality-evaluation-configs --level DATABASE
```

### Update a configuration
<a name="data-quality-catalog-monitoring-gs-update"></a>

Call `update-data-quality-evaluation-config` with the configuration name, the role, and the settings to change. Settings that you don't specify keep their current values. The following command changes the configuration from Step 2 to the `ADVANCED` ruleset and adds a schedule that runs every 24 hours.

```bash
aws glue update-data-quality-evaluation-config \
  --name {{my-database-config}} \
  --managed-ruleset-name ADVANCED \
  --triggers ONCE SCHEDULE \
  --schedule-expression "rate(24 hours)" \
  --role {{DataQualityEvaluationConfigRole}}
```

Keep the following in mind when you update a configuration:
+ You must specify the role in every update, except an update that only sets `PauseRuns`.
+ You can't change the name, the level, or the catalog of a configuration. You can change the database and the table name pattern within the same level. To change the level or catalog, create a new configuration.
+ A list of triggers replaces the current list. If the new list doesn't include `SCHEDULE`, the schedule expression and time window are removed.
+ `DataSource`, `AdditionalRunOptions`, and `AdditionalDataSources` replace their current values as a whole. If you specify a `DataSource` without a `PreProcessingQuery`, the configuration no longer uses a preprocessing query.
+ Specifying `RulesetName` replaces a built-in ruleset, and specifying `ManagedRulesetName` replaces your own ruleset.
+ Keeping `ONCE` in the triggers doesn't evaluate the tables again. Adding `ONCE` to a configuration that didn't have it evaluates every table in scope one more time.
+ Evaluation runs that have already started aren't affected. Evaluations that haven't started yet use the updated settings.
+ To add or remove tags, use `tag-resource` and `untag-resource` with the configuration's ARN.

### Pause and resume a configuration
<a name="data-quality-catalog-monitoring-gs-pause"></a>

To pause a configuration that uses the `SCHEDULE` or `METADATA_CHANGE` trigger, set `PauseRuns` to `true`. While it is paused, the configuration evaluates nothing, including new tables. In the AWS CLI, `PauseRuns` is a Boolean flag: `--pause-runs` sets it to `true`, and `--no-pause-runs` sets it to `false`. The CLI doesn't accept a value after the flag.

```bash
aws glue update-data-quality-evaluation-config \
  --name {{my-database-config}} \
  --pause-runs
```

To resume, set `PauseRuns` to `false`. The configuration continues with its existing triggers, and evaluations that were missed while it was paused aren't run later.

```bash
aws glue update-data-quality-evaluation-config \
  --name {{my-database-config}} \
  --no-pause-runs
```

### Delete a configuration
<a name="data-quality-catalog-monitoring-gs-delete"></a>

Deleting a configuration stops all future evaluations from it. Evaluation runs that have already started finish, and existing results remain with each table. The built-in rulesets that AWS Glue created in your account aren't deleted, because other configurations can use them.

```bash
aws glue delete-data-quality-evaluation-config --name {{my-database-config}}
```

## Example: Manage configurations with the AWS SDK for Python (Boto3)
<a name="data-quality-catalog-monitoring-gs-python"></a>

The following Python example creates a configuration at the database level, waits for its evaluations to produce results, and prints the results for one table. Replace the configuration, database, table, and role names, and the account ID, with your own values.

```python
import logging
import time

import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)
glue = boto3.client("glue")

try:
    glue.create_data_quality_evaluation_config(
        Name="my-database-config",
        Level="DATABASE",
        DataSource={
            "GlueTables": {
                "CatalogId": "111122223333",
                "DatabaseName": "my_database",
            }
        },
        ManagedRulesetName="SIMPLE",
        Triggers=["ONCE"],
        Role="DataQualityEvaluationConfigRole",
    )
except ClientError as err:
    logger.error(
        "Couldn't create the data quality evaluation configuration. Here's why: %s: %s",
        err.response["Error"]["Code"], err.response["Error"]["Message"])
    raise

result_filter = {
    "DataSource": {"GlueTable": {"DatabaseName": "my_database", "TableName": "my_table"}},
    "EvaluationRunMode": "EVALUATION_CONFIG",
    "DataQualityEvaluationConfig": "my-database-config",
}

results = []
for _ in range(30):
    results = glue.list_data_quality_results(Filter=result_filter)["Results"]
    if results:
        break
    time.sleep(60)

for summary in results:
    result = glue.get_data_quality_result(ResultId=summary["ResultId"])
    statistics = glue.list_data_quality_statistics(ProfileId=result["ProfileId"])
    for statistic in statistics["Statistics"]:
        print(statistic["StatisticName"], statistic.get("ColumnsReferenced"), statistic.get("DoubleValue"))
```