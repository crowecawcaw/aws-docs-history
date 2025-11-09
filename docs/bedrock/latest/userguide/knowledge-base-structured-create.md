# Create a knowledge base by connecting to a structured data store

To connect a knowledge base to a structured data store, you specify the following components:

- ###### Query engine configuration

The configuration for the compute service that will execute the generated SQL querries. The query
engine is used to convert natural language user queries into SQL queries that can be used
to extract data from your data store. You can choose Amazon Redshift as your query engine. When
choosing this configuration, you must specify:

    + The compute connnection metadata such as the cluster ID or the workgroup ARN depending on
     the chosen query engine.
    + The authentication method for using the query engine, which can be using an IAM service role with the appropriate
     permissions, a query engine database user, or an AWS Secrets Manager secret that is linked to your database credentials.

- ###### Storage configuration

The configuration for the data store containing your data. You can connect to Amazon Redshift
Provisioned or Amazon Redshift Serverless and use Amazon Redshift or AWS Glue Data Catalog as your data store.

- ###### (Optional) Query configurations

You can use optional query configurations for improving the accuracy of SQL generation:

    + **Maximum query time** – The amount of time after which the query times out.
    + **Descriptions** – Provides metadata or supplementary information about tables or columns. You can include descriptions of the tables or columns, usage notes, or any additional attributes. The descriptions you add can improve SQL query generation by providing extra context and information about the structure of the tables or columns.
    + **Inclusions and Exclusions** – Specifies a set of tables or columns to be included or excluded
     for SQL generation. This field is crucial if you want to limit the scope of SQL queries to a defined subset of available tables or
     columns. This option can help optimize the generation process by reducing unnecessary table or column references.


    If you specify inclusions, all other tables and columns are ignored. If you specify exclusions, the tables and columns you specify
     are ignored.


    ###### Note

    Inclusions and exclusions aren't a substitute for guardrails and is only intended for improving model accuracy.
    + **Curated queries** – A set of predefined question and answer examples. Questions are written as
     natural language queries (NLQ) and answers are the corresponding SQL query. These examples help the SQL generation process by providing
     examples of the kinds of queries that should be generated. They serve as reference points to improve the accuracy and relevance of generative
     SQL outputs.

Expand the section that corresponds to your use case:

To connect to a structured data store using the AWS Management Console, do the following:

1. Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at
   [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock").
2. In the left navigation pane, choose **Knowledge bases**.
3. In the **Knowledge bases** section, choose **Create** and then select **Knowledge base with structured data store**.
4. Set up the following details for the knowledge base:
   1. (Optional) Change the default name and provide a description for your knowledge base.
   2. Select the query engine to use for retrieving data from your data store.
   3. Choose an IAM service role with the proper permissions to create and manage this knowledge base. You can let Amazon Bedrock create the service role or choose a custom role that you have created. For more information about creating a custom role, see [Set up your query engine and permissions
      for creating a knowledge base with structured data store](knowledge-base-prereq-structured.md "knowledge-base-prereq-structured.md").
   4. (Optional) Add tags to associate with your knowledge base. For more information, see [Tagging Amazon Bedrock resources](tagging.md "tagging.md").
   5. Choose **Next**.

5. Configure your query engine:
   1. Select the service in which you created a cluster or workgroup. Then choose the cluster or workgroup to use.
   2. Select the authentication method and provide the necessary fields.
   3. Select the data store in which to store your metadata. Then, choose or enter the name of the database.
   4. (Optional) Modify the query configurations as necessary. Refer to the beginning of this topic for more information about different configurations.
   5. Choose **Next**.

6. Review your knowledge base configurations and edit any sections as necessary. Confirm to create your knowledge base.
   To connect to a structured data store using the Amazon Bedrock API, send a [CreateKnowledgeBase](../APIReference/API_agent_CreateKnowledgeBase.md "../APIReference/API_agent_CreateKnowledgeBase.md") request with an [Agents for Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt") with the following general request body:

```
{
    "name": "string",
    "roleArn": "string",
    "knowledgeBaseConfiguration": {
        "type": "SQL",
        "sqlKnowledgeBaseConfiguration": SqlKnowledgeBaseConfiguration
    },
    "description": "string",
    "clientToken": "string",
    "tags": {
        "string": "string"
    }
}
```

The following fields are required.

| Field                      | Basic description                                                                                                                                                                                     |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Name                       | A name for the knowledge base                                                                                                                                                                         |
| roleArn                    | A [knowledge base service role](kb-permissions.md "kb-permissions.md")<br>with the proper permissions. You can use the console to automatically create<br>a service role with the proper permissions. |
| knowledgeBaseConfiguration | Contains configurations for the knowledge base. For a structured database, specify `SQL` as the `type` and include the `sqlKnowledgeBaseConfiguration` field.                                         |

The following fields are optional.

| Field       | Use                                                                                                                                                                                                         |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| description | To include a description for the knowledge base.                                                                                                                                                            |
| clientToken | To ensure the API request completes only once. For more information, see [Ensuring idempotency](../../../ec2/latest/devguide/ec2-api-idempotency.md "../../../ec2/latest/devguide/ec2-api-idempotency.md"). |
| tags        | To associate tags with the flow. For more information, see [Tagging Amazon Bedrock resources](tagging.md "tagging.md").                                                                                     |

The `SQLKnowledgeBaseConfiguration` depends on the query engine that you use. For Amazon Redshift, specify the `type` field as `REDSHIFT` and include the `redshiftConfiguration` field, which maps to a [RedshiftConfiguration](../APIReference/API_agent_RedshiftConfiguration.md "../APIReference/API_agent_RedshiftConfiguration.md"). For the [RedshiftConfiguration](../APIReference/API_agent_RedshiftConfiguration.md "../APIReference/API_agent_RedshiftConfiguration.md"), you configure the following fields:

You can configure the following types of query engine:

If your Amazon Redshift databases are provisioned on dedicated compute nodes, the value of the `queryEngineConfiguration` field should be a [RedshiftQueryEngineConfiguration](../APIReference/API_agent_RedshiftQueryEngineConfiguration.md "../APIReference/API_agent_RedshiftQueryEngineConfiguration.md") in the following format:

```
{
    "type": "PROVISIONED",
    "provisionedConfiguration": {
        "clusterIdentifier": "string",
        "authConfiguration": RedshiftProvisionedAuthConfiguration
    },
}
```

Specify the ID of the cluster in the `clusterIdentifier` field. The [RedshiftProvisionedAuthConfiguration](../APIReference/API_agent_RedshiftProvisionedAuthConfiguration.md "../APIReference/API_agent_RedshiftProvisionedAuthConfiguration.md") depends on the type of authorization you're using. Select the tab that matches your authorization method:

IAM role
If you authorize with your IAM role, you need to specify
only `IAM` as the type in the
[RedshiftProvisionedAuthConfiguration](../APIReference/API_agent_RedshiftProvisionedAuthConfiguration.md "../APIReference/API_agent_RedshiftProvisionedAuthConfiguration.md") with no additional fields.

```
{
    "type": "IAM"
}
```

Temporary credentials user name
If you authorize with the database user name, specify the
`type` as `USERNAME` and specify the
user name in the `databaseUser` field in the
`RedshiftProvisionedAuthConfig`:

```
{
    "type": "USERNAME",
    "databaseUser": "string"
}
```

AWS Secrets Manager
If you authorize with AWS Secrets Manager, specify the
`type` as `USERNAME_PASSWORD` and
specify the ARN of the secret in the
`usernamePasswordSecretArn` field in the
`RedshiftProvisionedAuthConfig`:

```
{
    "type": "USERNAME_PASSWORD",
    "usernamePasswordSecretArn": "string"
}
```

If you're using Amazon Redshift Serverless, the value of the `queryConfiguration`field should be a [RedshiftQueryEngineConfiguration](../APIReference/API_agent_RedshiftQueryEngineConfiguration.md "../APIReference/API_agent_RedshiftQueryEngineConfiguration.md") in the following format:

```
{
    "type": "SERVERLESS",
    "serverlessConfiguration": {
        "workgroupArn": "string",
        "authConfiguration":
    }
}
```

Specify the ARN of your workgroup in the `workgroupArn` field. The [RedshiftServerlessAuthConfiguration](../APIReference/API_agent_RedshiftServerlessAuthConfiguration.md "../APIReference/API_agent_RedshiftServerlessAuthConfiguration.md") depends on the type of authorization you're using. Select the tab that matches your authorization method:

IAM role
If you authorize with your IAM role, you need to specify
only `IAM` as the type in the
`RedshiftServerlessAuthConfiguration` with no
additional fields.

```
{
    "type": "IAM"
}
```

AWS Secrets Manager
If you authorize with AWS Secrets Manager, specify the
`type` as `USERNAME_PASSWORD` and
specify the ARN of the secret in the
`usernamePasswordSecretArn` field in the
`RedshiftServerlessAuthConfiguration`:

```
{
    "type": "USERNAME_PASSWORD",
    "usernamePasswordSecretArn": "string"
}
```

This field maps to an array containing a single [RedshiftQueryEngineStorageConfiguration](../APIReference/API_agent_RedshiftQueryEngineStorageConfiguration.md "../APIReference/API_agent_RedshiftQueryEngineStorageConfiguration.md"), whose format depends on where your data is stored.

If your data is stored in AWS Glue Data Catalog, the
`RedshiftQueryEngineStorageConfiguration` should be in the
following format:

```
{
    "type": "AWS_DATA_CATALOG",
    "awsDataCatalogConfiguration": {
        "tableNames": ["string"]
    }
}
```

Add the name of each table that you want to connect your knowledge base to in the array that `tableNames` maps to.

###### Note

Enter table names in the pattern described in [Cross-database queries](../../../redshift/latest/dg/cross-database-overview.md "../../../redshift/latest/dg/cross-database-overview.md") (`${databaseName}.${tableName}`). You can include all tables by specifying `${databaseName.*}`.

If your data is stored in an Amazon Redshift database, the `RedshiftQueryEngineStorageConfiguration` should be in the following format:

```
{
    "type": "string",
    "redshiftConfiguration": {
        "databaseName": "string"
    }
}
```

Specify the name of your Amazon Redshift database in the `databaseName` field.

###### Note

Enter table names in the pattern described in [Cross-database queries](../../../redshift/latest/dg/cross-database-overview.md "../../../redshift/latest/dg/cross-database-overview.md") (`${databaseName}.${tableName}`). You can include all tables by specifying `${databaseName.*}`.

If your database is mounted through Amazon SageMaker AI Lakehouse, the database name is in the format `${db}@${schema}`.

This field maps to the following [QueryGenerationConfiguration](../APIReference/API_agent_QueryGenerationConfiguration.md "../APIReference/API_agent_QueryGenerationConfiguration.md") that you can use to configure how your data is queried:

```
{
    "executionTimeoutSeconds": number,
    "generationContext": {
        "tables": [
            {
                "name": "string",
                "description": "string",
                "inclusion": "string",
                "columns": [
                    {
                        "name": "string",
                        "description": "string",
                        "inclusion": "string"
                    },
                    ...
                ]
            },
            ...
        ],
        "curatedQueries": [
            {
                "naturalLanguage": "string",
                "sql": "string"
            },
            ...
        ]
    }
}
```

If you want the query to time out, specify the timeout duration in seconds in the `executionTimeoutSeconds` field.

The `generationContext` field maps to a [QueryGenerationContext](../APIReference/API_agent_QueryGenerationContext.md "../APIReference/API_agent_QueryGenerationContext.md") object in
which you can configure as many of the following options as you need.

###### Important

If you include a generation context, the query engine makes a best effort attempt to apply it when generating SQL. The generation context is non-deterministic and is only intended for improving model accuracy. To ensure accuracy, verify the generated SQL queries.

For information about generation contexts that you can include, expand the following sections:

To improve the accuracy of SQL generation for querying the database, you can provide a description for the table or column that provides more context than a short table or column name. You can do the following:

- To add a description for a table, include a [QueryGenerationTable](../APIReference/API_agent_QueryGenerationTable.md "../APIReference/API_agent_QueryGenerationTable.md") object in the `tables` array. In that object, specify the name of the table in the `name` field and a description in the `description` field, as in the following example:

```
{
    "name": "database.schema.tableA",
    "description": "Description for Table A"
}
```

- To add a description for a column, include a [QueryGenerationTable](../APIReference/API_agent_QueryGenerationTable.md "../APIReference/API_agent_QueryGenerationTable.md") object in the `tables` array. In that object, specify the name of the table in the `name` field and include the `columns` field, which maps to an array of [QueryGenerationColumn](../APIReference/API_agent_QueryGenerationColumn.md "../APIReference/API_agent_QueryGenerationColumn.md"). In a `QueryGenerationColumn` object, include the name of the column in the `name` field and a description in the `description` field, as in the following example:

```
{
    "name": "database.schema.tableA",
    "columns": [
        {
            "name": "Column A",
            "description": "Description for Column A"
        }
    ]
}
```

- You can add a description for both a table and a column in it,
  as in the following example:

```
{
    "name": "database.schema.tableA",
    "description": "Description for Table A",
    "columns": [
        {
            "name": "columnA",
            "description": "Description for Column A"
        }
    ]
}
```

###### Note

Enter table and column names in the pattern described in [Cross-database queries](../../../redshift/latest/dg/cross-database-overview.md "../../../redshift/latest/dg/cross-database-overview.md"). If your database is in AWS Glue Data Catalog, the format is `awsdatacatalog.gluedatabase.table`.
You can suggest tables or columns to include or exclude when generating SQL
by using the `inclusion` field in the [QueryGenerationTable](../APIReference/API_agent_QueryGenerationTable.md "../APIReference/API_agent_QueryGenerationTable.md") and
[QueryGenerationColumn](../APIReference/API_agent_QueryGenerationColumn.md "../APIReference/API_agent_QueryGenerationColumn.md") objects. You can specify one of the following values in the
`inclusion` field:

- INCLUDE – Only the tables or columns that you specify are included as context when generating SQL.
- EXCLUDE – The tables or columns that you specify are excluded as context when generating SQL.
  You can specify whether to include or exclude tables or columns in the following ways:

- To include or exclude a table, include a [QueryGenerationTable](../APIReference/API_agent_QueryGenerationTable.md "../APIReference/API_agent_QueryGenerationTable.md") object in the `tables` array. In that object, specify the name of the table in the `name` field and whether to include or exclude it in the `inclusion` field, as in the following example:

```
{
    "name": "database.schema.tableA",
    "inclusion": "EXCLUDE"
}
```

The query engine doesn't add `Table A` in the additional context for generating SQL.

- To include or exclude a column, include a [QueryGenerationTable](../APIReference/API_agent_QueryGenerationTable.md "../APIReference/API_agent_QueryGenerationTable.md") object in the `tables` array. In that object, specify the name of the table in the `name` field and include the `columns` field, which maps to an array of [QueryGenerationColumn](../APIReference/API_agent_QueryGenerationColumn.md "../APIReference/API_agent_QueryGenerationColumn.md"). In a `QueryGenerationColumn` object, include the name of the column in the `name` field and whether to include or exclude it in the `inclusion` field, as in the following example:

```
{
    "name": "database.schema.tableA",
    "columns": [
        {
            "name": "database.schema.tableA.columnA",
            "inclusion": "EXCLUDE"
        }
    ]
}
```

The SQL generation ignores `Column A` in `Table A` in the context when generating SQL.

- You can combine tables and columns when specifying inclusions or exclusions, as in the following example:

```
{
    "name": "database.schema.tableA",
    "inclusion": "INCLUDE",
    "columns": [
        {
            "name": "database.schema.tableA.columnA",
            "inclusion": "EXCLUDE"
        }
    ]
}
```

SQL generation includes `Table A`, but excludes `Column A` within it when adding context for generating SQL.

###### Important

Table and column exclusions aren't substitutes for guardrails. These table and column inclusions and exclusions are used as additional context for model to consider when generating SQL.

To improve a query engine's accuracy in converting user queries into
SQL queries, you can provide it examples in the `curatedQueries`
field in the [QueryGenerationContext](../APIReference/API_agent_QueryGenerationContext.md "../APIReference/API_agent_QueryGenerationContext.md") object, which maps to an array of
[CuratedQuery](../APIReference/API_agent_CuratedQuery.md "../APIReference/API_agent_CuratedQuery.md") objects. Each object contains the following fields:

- naturalLanguage – An example of a query in natural language.
- sql – The SQL query that corresponds to the natural language query.
