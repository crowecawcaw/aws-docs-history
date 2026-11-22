

# Getting started with AWS Glue Data Quality for the Data Catalog

 This getting started section provides instructions to help you get started with AWS Glue Data Quality on the AWS Glue console. You'll learn how to complete essential tasks such as generating data quality rule recommendations and evaluating a ruleset against your data. 

**Topics**
+ [Prerequisites](#data-quality-prereqs)
+ [Step-by-step example](#data-quality-step-by-step-example)
+ [Generating rule recommendations](#data-quality-get-recommendations)
+ [Monitoring rule recommendations](#data-quality-monitor-recommendations)
+ [Editing recommended rulesets](#data-quality-edit-ruleset)
+ [Creating a new ruleset](#data-quality-create-ruleset)
+ [Running a ruleset to evaluate data quality](#data-quality-run-data-quality-task)
+ [Viewing the data quality score and results](#data-quality-view-results)
+ [Using preprocessing queries](#data-quality-preprocessing-queries)
+ [Supported source types](#data-quality-get-started-supported-source-types)
+ [Related topics](#data-quality-get-started-related)

## Prerequisites
<a name="data-quality-prereqs"></a>

 Before you use AWS Glue Data Quality, you should be familiar with using the Data Catalog and crawlers in AWS Glue. With AWS Glue Data Quality, you can evaluate quality for tables in a Data Catalog database. You also need the following: 
+  A table in the Data Catalog to evaluate your data quality ruleset against. 
+  An IAM role for AWS Glue that you supply when you generate rule recommendations or run a data quality task. This role must have permission to access resources that various AWS Glue Data Quality processes require to run on your behalf. These resources include AWS Glue, Amazon S3, and CloudWatch. To view example policies that include the minimum permissions for AWS Glue Data Quality, see [Example IAM policies](data-quality-authorization.md#data-quality-authorization-example-policy). 

   To learn more about IAM roles for AWS Glue, see [Create an IAM policy for the AWS Glue service](https://docs.aws.amazon.com/glue/latest/dg/create-service-policy.html) and [Create an IAM role for the AWS Glue service](https://docs.aws.amazon.com/glue/latest/dg/create-an-iam-role.html). You can also view a list of all AWS Glue permissions that are specific to data quality in [Authorization for AWS Glue Data Quality actions](https://docs.aws.amazon.com/glue/latest/dg/data-quality-authorization.html). 
+  A database with at least one table that contains a variety of data. The table used in this tutorial is named `yyz-tickets`, with the table `tickets`. This data is a collection of publicly available information from the City of Toronto for parking citations. If you create your own table, make sure that it's populated with a variety of valid data to get the best set of recommended rules. 

## Step-by-step example
<a name="data-quality-step-by-step-example"></a>

 For a step-by-step example with sample datasets, see the [AWS Glue Data Quality blog post](https://aws.amazon.com/blogs/big-data/getting-started-with-aws-glue-data-quality-from-the-aws-glue-data-catalog/). 

## Generating rule recommendations
<a name="data-quality-get-recommendations"></a>

 Rule recommendations make it easy to get started with data quality without writing code. With AWS Glue Data Quality, you can analyze your data, identify rules, and create a ruleset that you can evaluate in a data quality task. Recommendation runs are automatically deleted after 90 days.

**To generate data quality rule recommendations**

1.  Open the AWS Glue console at [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/). 

1.  Choose **Tables** in the navigation pane. Then choose the table that you want to generate data quality rule recommendations for. 

1.  On the table details page, select the **Data quality** tab to access AWS Glue Data Quality rules and settings for your table. 

1.  On the **Data quality** tab, choose **Add rules and monitor data quality**. 

1.  On the **Ruleset builder** page, an alert at the top of the page will prompt you to start a recommendation task if there are no rule recommendation runs. 

1.  Choose **Recommend rules** to open the modal and input your parameters for the recommendation task. 

1.  Choose an IAM role with access to AWS Glue. This role must have permission to access resources that various AWS Glue Data Quality processes require to run on your behalf. 

1.  After the fields are completed according to your preferences, choose **Recommend rules** to start the recommendation task run. If recommendation runs are in progress or completed, you can manage your runs in this alert. You might need to refresh the alert to view the status change. Completed and in-progress recommendation task runs appear in the **Run history** page that lists all recommendation runs for the past 90 days. 

### Recommendation modes
<a name="data-quality-recommendation-modes"></a>

When you start a recommendation run, you can choose one of the following modes:
+ `BASIC` analyzes table statistics to recommend rules. This mode is the default.
+ `ADVANCED` uses Amazon Bedrock to recommend rules from table metadata and a random sample of the table rows. This additional context can produce rules based on values and relationships that table statistics do not describe.

**Automatic Amazon Bedrock enhancement**  
In supported AWS Regions, `BASIC` recommendation runs automatically attempt to enhance the statistical ruleset with Amazon Bedrock. AWS Glue Data Quality sends the ruleset and column metadata for enhancement. You do not need to enable this step or grant Amazon Bedrock permissions.  
The recommendation role must allow `glue:StartDataQualityRuleRecommendationRun`. If enhancement fails or is unavailable, the run returns the original statistical ruleset.

**Athena resources and charges**  
`ADVANCED` uses Athena to access table data for the recommendation run. If the `glue-dataquality-sampling` Athena workgroup does not exist, AWS Glue creates it in your account. You can view this workgroup in the Athena console. An `ADVANCED` run incurs charges for Athena usage.

**Choosing a recommendation mode**  
Choose `BASIC` or `ADVANCED` based on your priorities:
+ If you need recommendations based on table statistics and support in all AWS Glue Data Quality Regions, choose `BASIC`.
+ If you want dynamic recommendations with more context about your data, choose `ADVANCED`.

**Availability and limitations**  
You can use `ADVANCED` in the following AWS Regions:
+ `ap-northeast-1`
+ `ap-northeast-3`
+ `ap-southeast-2`
+ `ap-southeast-4`
+ `ca-central-1`
+ `eu-central-1`
+ `eu-central-2`
+ `eu-north-1`
+ `eu-south-1`
+ `eu-south-2`
+ `eu-west-1`
+ `eu-west-2`
+ `eu-west-3`
+ `us-east-1`
+ `us-east-2`
+ `us-west-1`
+ `us-west-2`

**Note**  
`ADVANCED` uses a generative model and can return different rules for the same table, so we recommend that you review the rules after each run.

**Note**  
An `ADVANCED` run does not support `PreProcessingQuery`, `NumberOfWorkers`, `Timeout`, or `AdditionalRunOptions`.

The following AWS CLI command starts an `ADVANCED` recommendation run:

```
aws glue start-data-quality-rule-recommendation-run \
  --data-source '{"DataQualityGlueTable":{"DatabaseName":"mydatabase","TableName":"mytable"}}' \
  --role "arn:aws:iam::111122223333:role/GlueDataQualityRole" \
  --recommendation-mode ADVANCED
```

For more information about data processing and storage, see [Data protection for advanced data quality rule recommendations](data-protection-advanced-dq-recommendations.md).

For more information about the required recommendation role permissions, see [Minimum permissions to get advanced data quality rule recommendations](data-quality-authorization.md#example-policy-get-advanced-dq-rule-recommendations).

### What the recommended rules mean
<a name="data-quality-recommend-rules"></a>

Review and edit the generated rules before you use them in a data quality evaluation.

 AWS Glue Data Quality generates rules based on the data from each column of the input table. It uses the rules to identify potential boundaries where data can be filtered to maintain quality requirements. The following list of generated rules includes examples that are useful for understanding what the rules mean and what they might do when applied to your data. 

 For a full list of the generated Data Quality Definition Language (DQDL) rule types, see [DQDL rule type reference](https://docs.aws.amazon.com/glue/latest/dg/dqdl.html#dqdl-rule-types). 
+  `IsComplete "SET_FINE_AMOUNT"` –The `IsComplete` rule verifies that the column is filled in for any given row. Use this rule to tag columns as non-optional in data. 
+  `Uniqueness "TICKET_NUMBER" > 0.95` – The `Uniqueness` rule verifies that the data within the column meets some threshold of uniqueness. In this example, the data that populates any given row for `"TICKET_NUMBER"` was determined to be at most 95% identical in content to all other rows, which suggests this rule. 
+  `ColumnValues "PROVINCE" in ["ON", "QC", "AB", "NY",...]` – The `ColumnValues` rule defines valid values for the column, based on existing column contents. In this example, the data for each row is a 2-letter license code plate for a state or province. 
+  `ColumnLength "INFRACTION_DESCRIPTION" between 15 and 31` – The `ColumnLength` rule enforces a length restriction on a column's data. This rule is generated from the sample data based on the minimum and maximum recorded lengths for a column of strings. 

## Monitoring rule recommendations
<a name="data-quality-monitor-recommendations"></a>

 When data quality rule recommendations are running, the **Add rules and monitor data quality** page displays information and additional actions that you can take in the top bar. 

 When rule recommendations are in progress, you can choose **Stop run** before the recommendation task is complete. While the task is in progress, you will see the status, **in progress**, and the date and time when the run started. 

 When the rule recommendations are complete, the rule recommendation bar displays the number of rules recommended, the status of the last recommendation run, and the date and timestamp when it finished. 

 You can add the recommended rules by choosing **Insert Rule Recommendation**. To view previously recommended rules, select a specific date. To run a new recommendation, choose **More actions**, and then choose ** Recommended rules**. 

 Set default settings by choosing **Manage user settings**. You can set the default path for Amazon S3 to store rulesets or to set up a default role to run the Data Catalog. 

## Editing recommended rulesets
<a name="data-quality-edit-ruleset"></a>

Because AWS Glue Data Quality generates rules based on existing data that you have available, you might see some unexpected or undesirable rules in the automated suggestions. In order to get the most out of the recommended rulesets, you need to evaluate and modify them. For this step of the tutorial, you take the rules generated in the previous step and adjust them to enforce more restrictive qualities on some data. You also relax other rules to ensure that correct, unique data can be added later. 

**Edit a suggested ruleset**

1.  In the AWS Glue console, choose **Data Catalog**, and then choose **Databases tables** in the navigation pane. Choose the table `tickets`. 

1. On the table details page, choose the **Data quality** tab to access AWS Glue Data Quality rules and settings for the table.

1.  In the **Rulesets** section, select the ruleset generated in [Generating rule recommendations](#data-quality-get-recommendations). 

1.  Choose **Actions**, and then choose **Edit** in the console window. The ruleset editor loads in the console. It includes an editing pane for your rules and a quick reference for DQDL. 

1. Remove line `2` of the script. This relaxes the requirement that the database size is constrained within a certain number of rows. After the edit, your file should contain the following on lines 1–3:

   ```
   Rules = [
       IsComplete "TAG_NUMBER_MASKED",
       ColumnLength "TAG_NUMBER_MASKED" between 6 and 9,
   ```

1. Remove line `25` of the script. This relaxes the requirement that 96% of recorded provinces are `ON`. After the edit, your file should contain the following from line `24` to the end of the ruleset:

   ```
   ColumnValues "PROVINCE" in ["ON", "QC", "AB", "NY", "AZ", "NS", "BC", "MI", "PQ", "MB", "PA", "FL", "SK", "NJ", "OH", "NB", "IL", "MA", "CA",
       "VA", "TX", "NF", "MD", "PE", "CT", "NC", "GA", "IN", "OR", "MN", "TN", "WI", "KY", "MO", "WA", "NH", "SC", "CO", "OK", "VT", "RI", "ME", "AL",
       "YT", "IA", "DE", "AR", "LA", "XX", "WV", "MT", "KS", "NT", "DC", "NV", "NE", "UT", "MS", "NM", "ID", "SD", "ND", "AK", "NU", "GO", "WY", "HI"],
   ColumnLength "PROVINCE" = 2
   ]
   ```

1. Change line `14` to the following:

   ```
   IsComplete "TIME_OF_INFRACTION",
   ```

    This *strengthens* the requirement on the column by limiting the database to only tickets that contain a recorded time of infraction. You should always consider tickets without a recorded time of infraction to be invalid data in this dataset. This is different than situations where partitioning or transformation might be more appropriate for further data use or inspection to determine a quality rule.

1. Choose **Update Ruleset**at the bottom of the console page.

## Creating a new ruleset
<a name="data-quality-create-ruleset"></a>

 A ruleset is a group of data quality rules that you evaluate against your data. In the AWS Glue console, you can author custom rulesets using Data Quality Definition Language (DQDL). 

**To create a data quality ruleset**

1.  In the AWS Glue console, choose **Data Catalog**, choose **Databases**, and then choose **Tables** in the navigation pane. Select the table `tickets`. 

1. Open the **Data quality** tab.

1.  In the **Rulesets** section, choose **Create ruleset**. The DQDL editor launches in the console. It has a text area for direct editing, and a quick reference for DQDL rules and the table schema. 

1.  Start adding rules to the text area of the DQDL editor. You can either write rules directly from this tutorial, or use the **DQDL rule builder** feature of the data quality rules editor. 
**Note**  
 Select a rule type from the list, and select the plus sign to insert example syntax into the editor pane. 
Exchange the placeholder column names with your own column names. Column names from the table are available in the **Schema** tab. 
 Update the expression parameter as you see fit. For a full list of expressions that DQDL supports, see [Expressions](dqdl.md#dqdl-syntax-rule-expressions). 

    As an example, the following rules are constraints for data validation of the `ticket_number` column in the `tickets` table. To add the following rules, use the DQDL rule builder or directly edit your ruleset: 

   ```
   IsComplete "ticket_number",
   IsUnique "ticket_number",
   ColumnValues "ticket_number" > 9000000000
   ```

1. Provide a name for your new ruleset in the **Ruleset name** field.

1. Choose **Save ruleset**.

### Evaluating data quality across multiple datasets
<a name="data-quality-create-ruleset-referential-integrity"></a>

 You can set up data quality rules across multiple datasets using ReferentialIntegrity and DatasetMatch rulesets. ReferentialIntegrity checks to see if data in the primary dataset is present in other datasets. 

To add a reference dataset, choose the **Schema** tab and then choose **Update reference tables**. You will be prompted to select a database and a table. You can add the table and then set up data quality rules. Rule types like AggregateMatch, RowCountMatch, ReferentialIntegrity, SchemaMatch, and DatasetMatch support the ability to perform data quality checks across multiple datasets. 

## Running a ruleset to evaluate data quality
<a name="data-quality-run-data-quality-task"></a>

 When you run a data quality task, AWS Glue Data Quality evaluates a ruleset against your data and calculates a data quality score. This score represents the percentage of data quality rules that passed for the input. 

**To run a data quality task**

1. In the AWS Glue console, choose **Data Catalog**, choose **Databases**, and then choose **Tables** in the navigation pane. Select the table `tickets`.

1. Choose the **Data quality** tab.

1. In the **Rulesets** list, select the ruleset that you want to evaluate against the table. For this step, we recommend using a ruleset that you've written or modified already rather than generated rules. Choose **Run**. 

1.  In the modal, choose your IAM role. This role must have permission to access resources that various AWS Glue Data Quality processes require to run on your behalf. You can save the IAM role as the default or modify it by going to the **Default Setting** page. 

1.  Under **Data quality actions**, choose whether you want to **Publish metrics to Amazon CloudWatch**. When this option is selected, AWS Glue Data Quality publishes metrics that indicate the number of rules that passed and the number of rules that failed. To take action on metrics stored this way, you can use CloudWatch alarms. Key metrics are also published to Amazon EventBridge for you to set up alerts. For more information, see [Setting up alerts, deployments, and scheduling](https://docs.aws.amazon.com/glue/latest/dg/data-quality-alerts.html). 

1.  In **Run Frequency**, choose run on demand or schedule the ruleset. When you schedule a ruleset, you're prompted for a task name. The schedule will be created in Amazon EventBridge. You can edit your schedule in Amazon EventBridge. 

1.  To save the data quality results in Amazon S3, select a **Data quality results location**. The IAM role that you previously selected for this task must have write access to this location. 

1.  Under **Additional Configurations**, enter the **Requested number of workers** that you want AWS Glue to allocate for your data quality task. 

1.  You can optionally set up a filter at the data source. This helps you reduce the data that you're reading. You can also use a filter to run incremental validations by selecting partition information and passing them as parameters via API calls. To improve performance, you can provide a partition predicate. 

1.  Choose **Run**. You should see your new task in the **Data quality task runs** list. When the **Run status** column for the task shows as **Completed**, you can view the quality score results. You might need to refresh your console window for the status to update correctly. 

1.  To view the column for the data quality result details, choose the “\+” icon to expand the ruleset. The results show you the rules that passed and failed in the evaluation, and what triggered the rule failure. 

## Viewing the data quality score and results
<a name="data-quality-view-results"></a>

**To see the latest run on all created rulesets**

1.  In the AWS Glue console, choose **Tables** in the navigation pane. Then choose the table that you want to run a data quality task for. 

1.  Choose the **Data quality** tab. 

1.  The **Data quality snapshot** shows a general trend of runs over time. The last 10 runs over all rulesets are displayed by default. To filter by ruleset, select the desired one from the dropdown list. If there are less than 10 runs, all the completed runs that are available are displayed. 

1.  In the **Data quality** table, each ruleset with its latest run (if there is one) is shown, along with the score. Expanding the ruleset displays the rules that are in that ruleset, along with the rule results for that run. 



**To see the latest run on a particular ruleset**

1.  In the AWS Glue console, choose **Tables** in the navigation pane. Then choose the table that you want to run a data quality task for. 

1.  Choose the **Data quality** tab. 

1.  In the **Data quality **table, choose on a specific ruleset. 

1.  On the **Ruleset details** page, choose the **Run history** tab. 

    All of the evaluation runs for this particular ruleset are listed in the table within this tab. You can see the history of the scores and the status of the runs. 

1.  To see more information about a particular run, choose the **Run ID** to go to the **Evaluation run details** page. On this page, you can see specifics about the run and more details about the status of individual rule results. 

## Using preprocessing queries
<a name="data-quality-preprocessing-queries"></a>

 AWS Glue Data Quality supports preprocessing queries that allow you to transform your data before running data quality checks. This feature enables you to: 
+ Create derived columns for data quality validation.
+ Filter data based on specific conditions.
+ Perform calculations or transformations for quality checks.
+ Validate relationships between columns.

**Note**  
 This feature is only supported in APIs and is not supported via the console. 

### Using preprocessing queries with the CLI and SDK
<a name="data-quality-preprocessing-queries-cli-sdk"></a>

#### Recommendation runs
<a name="data-quality-preprocessing-queries-recommendation-runs"></a>

 The following examples show how to use preprocessing queries with recommendation runs. 

 **AWS CLI:** 

```
aws glue start-data-quality-rule-recommendation-run \
  --data-source '{"DataQualityGlueTable": { \
    "DatabaseName": "mydatabase", \
    "TableName": "mytable", \
    "PreProcessingQuery": "SELECT sepal_length, sepal_width, petal_length, petal_width, class, (sepal_length + sepal_width) as sepal_total FROM `mydatabase.mytable`" \
  }}' \
  --role "arn:aws:iam::123456789012:role/GlueDataQualityRole" \
  --created-ruleset-name "my-ruleset-with-preprocessing"
```

 **Java SDK:** 

```
StartDataQualityRuleRecommendationRunRequest request = new StartDataQualityRuleRecommendationRunRequest()
    .withDataSource(new DataSource()
        .withDataQualityGlueTable(new DataQualityGlueTable()
            .withDatabaseName("mydatabase")
            .withTableName("mytable")
            .withPreProcessingQuery("SELECT sepal_length, sepal_width, " + 
                "(sepal_length + sepal_width) as sepal_total " +
                "FROM `mydatabase.mytable`")))
    .withRole("arn:aws:iam::123456789012:role/GlueDataQualityRole")
    .withCreatedRulesetName("my-ruleset-with-preprocessing");

glueClient.startDataQualityRuleRecommendationRun(request);
```

#### Ruleset evaluation runs
<a name="data-quality-preprocessing-queries-evaluation-runs"></a>

 The following examples show how to use preprocessing queries with ruleset evaluation runs. 

 **AWS CLI:** 

```
aws glue start-data-quality-ruleset-evaluation-run \
  --data-source '{"DataQualityGlueTable": { \
    "DatabaseName": "mydatabase", \
    "TableName": "mytable", \
    "PreProcessingQuery": "SELECT order_id, amount, (tax + shipping) as total_fees FROM `mydatabase.mytable`" \
  }}' \
  --role "arn:aws:iam::123456789012:role/GlueDataQualityRole" \
  --ruleset-names '["my-ruleset"]'
```

 **Java SDK:** 

```
StartDataQualityRulesetEvaluationRunRequest request = new StartDataQualityRulesetEvaluationRunRequest()
    .withDataSource(new DataSource()
        .withDataQualityGlueTable(new DataQualityGlueTable()
            .withDatabaseName("mydatabase")
            .withTableName("mytable")
            .withPreProcessingQuery("SELECT order_id, amount, " +
                "(tax + shipping) as total_fees " +
                "FROM `mydatabase.mytable`")))
    .withRole("arn:aws:iam::123456789012:role/GlueDataQualityRole")
    .withRulesetNames(Arrays.asList("my-ruleset"));

glueClient.startDataQualityRulesetEvaluationRun(request);
```

### Considerations when authoring preprocessing queries
<a name="data-quality-preprocessing-queries-considerations"></a>

 When writing a preprocessing query: 
+ The table reference must be formatted as ``databaseName.tableName`` using backticks.
+ The query must be a valid SELECT statement.
+ Column names in the query output will be used for data quality rules.

 The following example shows a preprocessing query: 

```
SELECT 
    sepal_length, 
    sepal_width, 
    petal_length, 
    petal_width, 
    class,
    (sepal_length + sepal_width) as sepal_total 
FROM `mydatabase.mytable`
```

### Limitations
<a name="data-quality-preprocessing-queries-limitations"></a>
+ The query must reference the table using backticks and the full ``databaseName.tableName`` format.
+ Maximum query length is 51,200 characters.
+ The query must return at least one row of data.
+ All columns referenced in your ruleset must be present in the query output.

## Supported source types
<a name="data-quality-get-started-supported-source-types"></a>

 The following tables show which sources and table formats you can evaluate with AWS Glue Data Quality, and which AWS Lake Formation permission setups each one works with. Sources that aren't listed aren't supported. 


**Supported sources and table formats**  

| Source or table format | Supported | Where you can start runs | 
| --- | --- | --- | 
| Parquet, ORC, Avro, CSV, JSON, TSV | Yes | AWS Glue console, API/AWS CLI, Amazon SageMaker Unified Studio | 
| Apache Iceberg, Apache Hudi, Delta Lake | Yes | AWS Glue console, API/AWS CLI, Amazon SageMaker Unified Studio | 
| Amazon S3 Tables | Yes | API/AWS CLI, Amazon SageMaker Unified Studio | 
| Amazon Athena views | Yes | AWS Glue console, API/AWS CLI, Amazon SageMaker Unified Studio | 
| Amazon Redshift managed storage (RMS) catalogs | Yes | API/AWS CLI, Amazon SageMaker Unified Studio | 
| Amazon Redshift namespaces registered in the Data Catalog | Yes | API/AWS CLI, Amazon SageMaker Unified Studio | 
| Amazon Redshift through a REDSHIFT connection | Yes | AWS Glue console, API/AWS CLI | 
| JDBC connections to MySQL, MariaDB, PostgreSQL, Microsoft SQL Server, or Oracle databases, including Amazon RDS and Aurora | Yes | AWS Glue console, API/AWS CLI | 
| Amazon DocumentDB and MongoDB through a MONGODB connection | Yes | AWS Glue console, API/AWS CLI | 
| DynamoDB tables cataloged by a crawler | Yes | AWS Glue console, API/AWS CLI | 
| Federated catalogs for sources other than Amazon Redshift (for example, Snowflake, BigQuery, Amazon RDS, DynamoDB, or a remote Iceberg REST catalog) | No | For a database that a supported JDBC connection can reach, use a JDBC connection. Otherwise, evaluate the data in an AWS Glue ETL job, or copy the data to Amazon S3 | 
| Snowflake through a JDBC connection | No | Evaluate the data in an AWS Glue ETL job that uses a SNOWFLAKE connection, or copy the data to Amazon S3 | 
| Connections other than JDBC, REDSHIFT, and MONGODB (for example, SNOWFLAKE, BIGQUERY, or SALESFORCE) | No | Evaluate the data in an AWS Glue ETL job, or copy the data to Amazon S3 | 
| Streaming tables, Delta Lake symlink tables, protected multi-dialect Data Catalog views | No | Copy the data to Amazon S3 | 

 A source that you reach through an unsupported federated catalog or connection can often still be evaluated another way. If a supported JDBC connection can reach the database, as with Amazon RDS, create a table in your default Data Catalog that reads the same table through a JDBC connection, and evaluate that table. For other sources, such as Snowflake, evaluate the data in an AWS Glue ETL job instead: read the data with the source's connection and apply the `EvaluateDataQuality` transform. For example, read a Snowflake table through a `SNOWFLAKE` connection. You can't evaluate a Data Catalog table that reads Snowflake through a JDBC connection, even though a crawler can create that table. For more information, see [Evaluating data quality with AWS Glue Studio](data-quality-gs-studio.md) and [Snowflake connections](aws-glue-programming-etl-connect-snowflake-home.md). You can also copy the data to Amazon S3 and evaluate the resulting table. 

 To evaluate a Amazon DocumentDB or MongoDB table through a `MONGODB` connection, set up the connection as follows: 
+ Include the database and collection in the connection URL, for example `mongodb://{{host}}:27017/{{database}}.{{collection}}`. AWS Glue Data Quality reads the collection that the connection URL names, so use a separate connection for each collection that you evaluate. If the user is defined in a different database, also add `authSource` to the URL, for example `?authSource=admin`.
+ Store the user name and password in the connection. AWS Glue Data Quality doesn't read MongoDB credentials from an AWS Secrets Manager secret.


**Supported AWS Lake Formation permission setups**  

| Permission setup | Amazon S3-based sources (table formats, Amazon S3 Tables, Amazon Athena views) | Amazon Redshift catalogs (RMS catalogs and registered namespaces) | 
| --- | --- | --- | 
| AWS Lake Formation, full table access | Yes | Yes | 
| AWS Lake Formation, column permissions or data filters | No | Yes | 
| AWS Lake Formation, cross-account full table access | Yes | No | 
| No AWS Lake Formation (IAM only) | Yes | No | 

 AWS Lake Formation doesn't apply to sources that you read through a `REDSHIFT`, JDBC, or `MONGODB` connection, or to DynamoDB tables. Some setups for Amazon S3-based sources need additional permissions: 
+ With AWS Lake Formation, grant the data quality IAM role `SELECT` on the whole table.
+ For cross-account Apache Iceberg tables, create a resource link in the account that runs AWS Glue Data Quality. You can't reference the producer account's catalog ID directly.
+ For cross-account Apache Hudi, Delta Lake, and Amazon S3 Tables, the producer account must also grant the data quality IAM role direct access to the underlying data location, for example with an Amazon S3 bucket policy or an Amazon S3 table bucket policy.
+ Store Amazon Athena views in the account that runs AWS Glue Data Quality. For more information, see [Amazon Athena view support](#data-quality-athena-view-support).

### Amazon Redshift support
<a name="data-quality-redshift-support"></a>

 You can evaluate data in Amazon Redshift with AWS Glue Data Quality. How you set it up depends on how your Amazon Redshift data is available to AWS Glue: 


**Ways to evaluate Amazon Redshift data**  

| If your Amazon Redshift data is | Evaluate it through | Access control | Where you can start runs | 
| --- | --- | --- | --- | 
| In Amazon Redshift managed storage (RMS) catalogs in the Data Catalog | The RMS catalog tables | AWS Lake Formation (full table access, column permissions, or data filters) | API/AWS CLI, Amazon SageMaker Unified Studio | 
| In a provisioned cluster or Serverless namespace registered in the Data Catalog | The federated catalog for the namespace | AWS Lake Formation (full table access, column permissions, or data filters) | API/AWS CLI, Amazon SageMaker Unified Studio | 
| In a provisioned cluster or Serverless namespace that isn't registered in the Data Catalog | A Data Catalog table that uses a REDSHIFT connection | The connection's credentials | AWS Glue console, API/AWS CLI | 

For RMS catalogs and registered namespaces, keep the following in mind:
+ The Amazon Redshift database user that the data quality IAM role maps to (`IAMR:{{role-name}}`) must have `USAGE` on the schema and `SELECT` on the table. Alternatively, tag the role with `RedshiftDbUser` or `RedshiftDbRoles` to map it to a database user or role that has these privileges.
+ For registered namespaces, also allow the data quality IAM role `redshift-serverless:GetCredentials` and the Amazon Redshift Data API actions (`redshift-data:BatchExecuteStatement`, `redshift-data:DescribeStatement`, and `redshift-data:GetStatementResult`).
+ You can't evaluate columns of type `SUPER`.
+ Cross-account access and setups without AWS Lake Formation aren't supported.

### Amazon Athena view support
<a name="data-quality-athena-view-support"></a>

 AWS Glue Data Quality supports rule recommendation and evaluation runs for Amazon Athena views created using `CREATE VIEW` and stored in the Data Catalog of the account that runs AWS Glue Data Quality. Nested views are supported. To evaluate data in another account, create the view in your account and reference the other account's tables through resource links. 

 AWS Glue Data Quality evaluates an Amazon Athena view using the permissions of the IAM role that you provide for the data quality run. Grant this role access to the view and to every underlying table, partition, data location, and encryption key that the view references. For cross-account views, configure the required AWS Glue, AWS Lake Formation, Amazon S3, and AWS KMS permissions in each participating account. If you use resource links, configure them in the account that runs AWS Glue Data Quality. 

Consider the following limitations:
+  Protected multi-dialect Data Catalog views are not supported. 
+  An Amazon Athena view dependency chain can be up to 100 levels deep, including the selected view. AWS Glue Data Quality resolves the nested views required to build the selected view. It then runs the recommendation or evaluation once against the data returned by the selected view, rather than separately against each underlying view. 
+  Each physical table referenced by a view must use a source type that AWS Glue Data Quality supports. 
+  The view query must use SQL syntax and functions that are compatible with the AWS Glue Spark SQL runtime. 
+  Catalog partition predicates are not supported for view sources. 

## Related topics
<a name="data-quality-get-started-related"></a>
+ [DQDL rule type reference](dqdl-rule-types.md)
+ [Data Quality Definition Language (DQDL) reference](dqdl.md)