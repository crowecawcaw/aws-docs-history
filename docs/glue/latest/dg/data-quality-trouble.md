# Troubleshooting AWS Glue Data Quality errors

If you encounter errors in AWS Glue Data Quality, use the following solutions to help you find the source of the problems and fix them.

###### Contents

- [Error: missing AWS Glue Data Quality module](data-quality-trouble.md#data-quality-trouble-error-1 "data-quality-trouble.md#data-quality-trouble-error-1")
- [Error: insufficient AWS Lake Formation permissions](data-quality-trouble.md#data-quality-trouble-error-2 "data-quality-trouble.md#data-quality-trouble-error-2")
- [Error: rulesets are not uniquely named](data-quality-trouble.md#data-quality-trouble-error-3 "data-quality-trouble.md#data-quality-trouble-error-3")
- [Error: tables with special characters](data-quality-trouble.md#data-quality-trouble-error-4 "data-quality-trouble.md#data-quality-trouble-error-4")
- [Error: overflow error with a large ruleset](data-quality-trouble.md#data-quality-trouble-error-5 "data-quality-trouble.md#data-quality-trouble-error-5")
- [Error: overall rule status is failed](data-quality-trouble.md#data-quality-trouble-error-6 "data-quality-trouble.md#data-quality-trouble-error-6")
- [AnalysisException: Unable to verify existence of default database](data-quality-trouble.md#data-quality-trouble-error-7 "data-quality-trouble.md#data-quality-trouble-error-7")
- [Error Message: Provided key map not suitable for given data frames](data-quality-trouble.md#data-quality-trouble-error-8 "data-quality-trouble.md#data-quality-trouble-error-8")
- [Exception in User Class:
  java.lang.RuntimeException : Failed to fetch data. Check the logs in CloudWatch to get more details](data-quality-trouble.md#data-quality-trouble-error-9 "data-quality-trouble.md#data-quality-trouble-error-9")
- [LAUNCH ERROR: Error downloading from S3 for bucket](data-quality-trouble.md#data-quality-trouble-error-10 "data-quality-trouble.md#data-quality-trouble-error-10")
- [InvalidInputException (status: 400): DataQuality rules cannot be parsed](data-quality-trouble.md#data-quality-trouble-error-11 "data-quality-trouble.md#data-quality-trouble-error-11")
- [Error: Eventbridge is not triggering Glue DQ jobs based on the schedule I setup](data-quality-trouble.md#data-quality-trouble-error-12 "data-quality-trouble.md#data-quality-trouble-error-12")
- [CustomSQL errors](data-quality-trouble.md#data-quality-trouble-error-13 "data-quality-trouble.md#data-quality-trouble-error-13")
- [Dynamic Rules](data-quality-trouble.md#data-quality-trouble-error-14 "data-quality-trouble.md#data-quality-trouble-error-14")
- [Exception in User Class: org.apache.spark.sql.AnalysisException:
  org.apache.hadoop.hive.ql.metadata.HiveException](data-quality-trouble.md#data-quality-trouble-error-15 "data-quality-trouble.md#data-quality-trouble-error-15")
- [UNCLASSIFIED_ERROR; IllegalArgumentException: Parsing Error: No rules or analyzers
  provided., no viable alternative at input](data-quality-trouble.md#data-quality-trouble-error-16 "data-quality-trouble.md#data-quality-trouble-error-16")

## Error: missing AWS Glue Data Quality module

**Error message**: No module named 'awsgluedq'.

**Resolution**: This error occurs when you run AWS Glue Data Quality in an unsupported version. AWS Glue Data Quality is supported only in Glue version 3.0 and later.

## Error: insufficient AWS Lake Formation permissions

**Error message**: Exception in User Class:
`com.amazonaws.services.glue.model.AccessDeniedException`:
Insufficient Lake Formation permission(s) on impact_sdg_involvement (Service: AWS Glue; Status Code: 400; Error Code:
AccessDeniedException; Request ID: 465ae693-b7ba-4df0-a4e4-6b17xxxxxxxx; Proxy: null).

**Resolution**: You must provide sufficient permissions in AWS Lake Formation.

## Error: rulesets are not uniquely named

**Error message**: Exception in User Class: ...services.glue.model.AlreadyExistsException: Another ruleset with the same name already exists.

**Resolution**: Rulesets are global and must be unique.

## Error: tables with special characters

**Error message**: Exception in User Class: org.apache.spark.sql.AnalysisException: cannot resolve ''C'' given input columns: [primary.data\_end\_time, primary.data\_start\_time, primary.end\_time, primary.last\_updated, primary.message, primary.process\_date, primary.rowhash, primary.run\_by, primary.run\_id, primary.start\_time, primary.status]; line 1 pos 44;.

**Resolution**: There is a current limitation that AWS Glue Data Quality cannot be executed on tables that have special characters such as ".".

## Error: overflow error with a large ruleset

**Error message**: Exception in User Class: java.lang.StackOverflowError.

**Resolution**: If you have a large ruleset of greater than 2K rules, you may encounter this issue. Break your rules into multiple rulesets.

## Error: overall rule status is failed

**Error condition**: My Ruleset is successful, but my overall rule status is failed.

**Resolution**: This error most likely occurred because you chose
the option to publish metrics to Amazon CloudWatch while publishing. If your dataset is in a VPC, your VPC may not allow
AWS Glue to publish metrics to Amazon CloudWatch. In this case, you >must set up an endpoint for your VPC to access Amazon CloudWatch.

## AnalysisException: Unable to verify existence of default database

**Error condition**: AnalysisException: Unable to verify existence of default database:
com.amazonaws.services.glue.model.AccessDeniedException: Insufficient Lake Formation permission(s) on default (Service:
AWS Glue;
Status Code: 400; Error Code: AccessDeniedException; Request ID: XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX; Proxy: null)

**Resolution**: In AWS Glue job’s catalog integration, AWS Glue
always tries to check whether default database exists or not using AWS Glue `GetDatabase API`.
When the `DESCRIBE` Lake Formation permission is not granted, or `GetDatabase IAM` permission is granted,
then the job fails when verifying existence of the default database.

To resolve:

1. Add the `DESCRIBE` permission in Lake Formation for the default database.
2. Configure the IAM role attached to the AWS Glue job as Database Creator in Lake Formation.
   This will automatically create a default database and grant required Lake Formation permissions for the role.
3. Disable `--enable-data-catalog` option. (It is shown as **Use Data Catalog as the Hive
   metastore** in AWS Glue Studio).

If you do not need Spark SQL Data Catalog integration in the job, you can disable it.

## Error Message: Provided key map not suitable for given data frames

**Error condition**: Provided key map not suitable for given data frames.

**Resolution**: You are using **DataSetMatch** ruletype and the join keys have duplicates.
Your join keys must be unique and must not be NULL. In cases where you can’t have join keys that are unique, consider using other
ruletypes such as **AggregateMatch** to match on summary data.

## Exception in User Class:

java.lang.RuntimeException : Failed to fetch data. Check the logs in CloudWatch to get more details

**Error condition**: Exception in User Class:
java.lang.RuntimeException : Failed to fetch data. Check the logs in CloudWatch to get more details.

**Resolution**: This happens when you are creating DQ rules on an
Amazon S3-based table that compares against Amazon RDS or Amazon Redshift. In these cases,
AWS Glue cannot load the connection. Instead, try to set up DQ rule on the Amazon Redshift or Amazon RDS dataset.
This is a known bug.

## LAUNCH ERROR: Error downloading from S3 for bucket

**Error condition**: LAUNCH ERROR: Error downloading from S3 for bucket:
`aws-glue-ml-data-quality-assets-us-east-1, key: 
 jars/aws-glue-ml-data-quality-etl.jar.Access Denied (Service: Amazon S3; Status Code: 403; Please refer logs for details)` .

**Resolution**: The permissions in the role passed to AWS Glue Data Quality
must permit reading from the preceding
Amazon S3 location. This IAM policy should be attached to the role:

```
{
  "Sid": "allowS3",
  "Effect": "Allow",
  "Action": "s3:GetObject",
  "Resource": "arn:aws:s3:::aws-glue-ml-data-quality-assets-<region>/*"
}

```

Refer to [Data Quality authorization](data-quality-authorization.md "data-quality-authorization.md")
for detailed permissions. These libraries are required to evaluate data quality for your datasets.

## InvalidInputException (status: 400): DataQuality rules cannot be parsed

**Error condition**: InvalidInputException (status: 400): DataQuality rules cannot be parsed.

**Resolution**: There are many possibilities for this error. One
possibility is that your rules may have single quotes. Verify that they are in double quotes. For example:

```
Rules = [
ColumnValues "tipo_vinculo" in ["CODO", "DOCO", "COCO", "DODO"] AND "categoria" = 'ES"
    AND "cod_bandera" = 'CEP'

```

Change this to:

```
Rules = [
(ColumnValues "tipovinculo" in [ "CODO", "DOCO", "COCO", "DODO"]) AND (ColumnValues "categoria" = "ES")
    AND (ColumnValues "codbandera" = "CEP")
]

```

## Error: Eventbridge is not triggering Glue DQ jobs based on the schedule I setup

**Error condition**: Eventbridge is not triggering AWS Glue Data Quality jobs based on the schedule I setup.

**Resolution**: The role triggering the job may not have the
right permissions. Make sure that the role that you are using to start the jobs has the permissions mentioned in [IAM setup required for scheduling evaluation runs](data-quality-authorization.md#data-quality-iam-setup-evaluation-runs "data-quality-authorization.md#data-quality-iam-setup-evaluation-runs") .

## CustomSQL errors

**Error condition**: `The output from CustomSQL must contain at least one column that matches the 
 input dataset for AWS Glue Data Quality to provide row level results. The SQL query is a valid query but no columns from the SQL result are 
 present in the Input Dataset. Ensure that matching columns are returned from the SQL`.

**Resolution**: The SQL query is valid but verify
that you’re selecting only columns from the primary table. Selecting
aggregate functions like sum, count on the columns from the primary can result in this error.

**Error condition**: `There was a problem when executing your SQL statement: cannot resolve "Col"`.

**Resolution**: This column is not present in the primary table.

**Error condition**: `The columns that are returned from the SQL statement should only belong to the primary table. 
 "In this case, some columns ( Col ) belong to reference table"`.

**Resolution**: In SQL queries when you’re joining the primary
table with other reference tables, verify
that your select statement has only column names from your primary table to
generate row level results for the primary table.

## Dynamic Rules

**Error condition**`: Dynamic
 rules require job context, and cannot be evaluated in interactive session or data
 preview.`.

**Cause:** This error message might
appear in your data preview results, or in other interactive sessions, when dynamic DQ rules
are present in your ruleset. Dynamic rules reference historical metrics associated with a
particular job name and evaluation context, so they can't be evaluated in interactive sessions.

**Resolution**: Running your AWS Glue job will produce historical metrics, which can be
referenced in later job runs for the same job.

**Error condition**:

- `[RuleType] rule only supports simple atomic operands in thresholds.`.
- `Function last not yet implemented for [RuleType] rule.`

**Resolution**: Dynamic rules are generally supported for all DQDL ruletypes in numeric expressions (see [DQDL Reference](dqdl.md "dqdl.md")).
However, some rules that produce multiple metrics, ColumnValues and ColumnLength, are not yet supported.

**Error condition**: `Binary expression operands must resolve to a single number.`.

**Cause**: Dynamic rules support binary expressions, like
`RowCount > avg(last(5)) * 0.9`.
Here, the binary expression is `avg(last(5)) * 0.9`. This rule is valid because both
operands `avg(last(5))` and `0.9` resolve to a single number. An
incorrect example is `RowCount > last(5) * 0.9`, because `last(5)` will
produce a list that can't be meaningfully compared to the current row count.

**Resolution**: Use aggregation functions to reduce a list-valued operand to a single number.

**Error condition**:

- `Rule threshold results in list, and a single value is expected. Use aggregation functions to produce a single value. 
Valid example: sum(last(10)), avg(last(10)).`
- `Rule threshold results in empty list, and a single value is expected.`

**Cause**: Dynamic rules can be used to compare some feature
of your dataset with its historical values. The last function allows for the retrieval of
multiple historical values, if a positive integer argument is provided. For example,
`last(5)` will retrieve the last five most recent values observed in job runs for your rule.

**Resolution**: An aggregation function must be used to reduce these values to a single number to make a
meaningful comparison with the value observed in the current job run.

Valid examples:

- `RowCount >= avg(last(5))`
- `RowCount > last(1)`
- `RowCount < last()`

Invalid example: `RowCount > last(5)`.

**Error condition**:

- `Function index used in threshold requires positive integer argument.`
- `Index argument must be an integer. Valid syntax example: `RowCount > index(last(10, 2))`, which means 
`RowCount` must be greater than third most recent execution from last 10 job runs.`

**Resolution**: When authoring dynamic rules, you can use the `index` aggregation function
to select one historical value from a list. For example, `RowCount > index(last(5)`, 1) will check whether the row
count observed in the current job is strictly greater than the second most recent row count observed for your job.
`index` is zero-indexed.

**Error condition**: `IllegalArgumentException: Parsing Error: Rule Type: DetectAnomalies is not valid`.

**Resolution**: Anomaly detection is only available in AWS Glue 4.0.

**Error condition**: `IllegalArgumentException: Parsing Error: Unexpected condition for rule of type ... 
 no viable alternative at input ...`.

Note: `...` is dynamic. Example: `IllegalArgumentException: Parsing Error: Unexpected condition for rule of type RowCount with 
 number return type, line 4:19 no viable alternative at input '>last'`.

**Resolution**: Anomaly detection is only available in AWS Glue 4.0.

## Exception in User Class: org.apache.spark.sql.AnalysisException:

org.apache.hadoop.hive.ql.metadata.HiveException

**Error condition**`: Exception in User Class: org.apache.spark.sql.AnalysisException: 
 org.apache.hadoop.hive.ql.metadata.HiveException: Unable to fetch table mailpiece_submitted. 
 StorageDescriptor#InputFormat cannot be null for table: mailpiece_submitted (Service: null; Status Code: 0; Error Code: 
 null; Request ID: null; Proxy: null)`

**Cause:** You are using Apache Iceberg in AWS Glue Data Catalog and the Input Format attribute in
AWS Glue Data Catalog is empty.

**Resolution**: This issue occurs when you are using CustomSQL ruletype in your DQ rule.
One way to fix this is to use “primary“ or add catalog name `glue_catalog.` to `<database>.<table>
 in Custom ruletype` .

## UNCLASSIFIED_ERROR; IllegalArgumentException: Parsing Error: No rules or analyzers

provided., no viable alternative at input

**Error condition**`: UNCLASSIFIED_ERROR; IllegalArgumentException: Parsing Error: No rules or 
 analyzers provided., no viable alternative at input`

**Resolution**: DQDL is not parsable. There are a few instances where this can occur. If you are
using composite rules, makes sure they have right parenthesis.

```
(RowCount >= avg(last(10)) * 0.6) and (RowCount <= avg(last(10)) * 1.4) instead of
      RowCount >= avg(last(10)) * 0.6 and RowCount <= avg(last(10)) * 1.4
```
