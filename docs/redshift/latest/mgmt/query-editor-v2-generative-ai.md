Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Interacting with Amazon Q generative SQL

###### Note

Amazon Q generative SQL support is only available in the following AWS Regions:

- US East (N. Virginia) Region (us-east-1)
- US East (Ohio) Region (us-east-2)
- US West (Oregon) Region (us-west-2)
- Asia Pacific (Mumbai) Region (ap-south-1)
- Asia Pacific (Seoul) Region (ap-northeast-2)
- Asia Pacific (Singapore) Region (ap-southeast-1)
- Asia Pacific (Sydney) Region (ap-southeast-2)
- Asia Pacific (Tokyo) Region (ap-northeast-1)
- Canada (Central) Region (ca-central-1)
- Europe (Frankfurt) Region (eu-central-1)
- Europe (Ireland) Region (eu-west-1)
- Europe (London) Region (eu-west-2)
- Europe (Paris) Region (eu-west-3)
- South America (São Paulo) Region (sa-east-1)
  For information about where your data is processed, see
  [Cross region inference in Amazon Q Developer](../../../amazonq/latest/qdeveloper-ug/cross-region-inference.md "../../../amazonq/latest/qdeveloper-ug/cross-region-inference.md")
  in the _Amazon Q Developer User Guide_.

You can interact with Amazon Q generative SQL capability in Amazon Redshift query editor v2. It's a coding assistant that
generates SQL statements based on your prompts and database schema. This coding assistant
is available while you're authoring a notebook in query editor v2.
The SQL generated is for the database your notebook is connected to.

When interacting with Amazon Q generative SQL, ask specific questions, iterate when you have complex requests, and verify the answers for accuracy.

When providing analysis requests in natural language, be as specific as possible to help
the coding assistant understand exactly what you need. Instead of asking "find top venues
that sold the most tickets," provide more details like "find names/ids of top three venues
that sold the most tickets in 2008." Use consistent and specific names of objects in your database when you know them.
Such as the schema, table, and column names as defined in your database instead of referring to
the same object in different ways, which can confuse the assistant.

Break down complex requests into multiple simple statements that are easier for the
assistant to interpret. Iteratively ask follow-up questions to get more detailed analysis
from the assistant. For example, first ask "which state has the most venues?" Then based on
the response, ask "which is the most popular venue from this state?".

Review the generated SQL before running it to ensure accuracy. If the generated SQL query
has errors or does not match your intent, provide instructions to the assistant on how to
correct it instead of rephrasing the entire request. For example, if the query is missing a
predicate clause on year, ask "Provide venues from year 2008."

Submit text of errors you receive from running generated SQL as prompts back to the Amazon Q generative SQL.
It learns from these errors to produce better SQL.

Add your schema to the SQL search path to signal that schema should be used.
For example, add the tickit schema when the data is in the tickit schema rather than the public schema.

```
set search_path to '$user', tickit;
```

## Considerations when interacting with Amazon Q generative SQL

Consider the following when working in the chat panel.

- The query editor v2 administrator for your account must have turned on the chat capability in the **Generative SQL settings** page.
- To use Amazon Q generative SQL, you need permission `sqlworkbench:GetQSqlRecommendations` in your IAM policy,
  in addition to other permissions specified in the AWS managed policy for query editor v2.
  For more information about AWS managed policies, see [Accessing the query editor v2](query-editor-v2-getting-started.md#query-editor-v2-configure "query-editor-v2-getting-started.md#query-editor-v2-configure").
- Your questions must be written in English.
- Your questions must be in reference to the connected database in your cluster or workgroup.
  To avoid empty state errors, there should be at least one table and some data in the database.
- Your questions must be in reference to data that is stored in the connected database. It cannot reference an external schema.
  For more information on the supported schemas, see
  [Create schema](../dg/r_CREATE_EXTERNAL_SCHEMA.md "../dg/r_CREATE_EXTERNAL_SCHEMA.md") in the _Amazon Redshift Database Developer Guide_.
- Any questions that result in SQL that changes the connected database might result in a warning.
- Generative AI technology is new and there can be mistakes, sometimes called hallucinations, in
  the responses. Test and review all code for errors and vulnerabilities before
  using it in your environment or workload.
- You can improve recommendations by sharing the SQL queries run by other users in your account.
  Your account administrator can run the following SQL commands

to allow access to the account's query history.

```
GRANT ROLE SYS:MONITOR to "IAMR:`role-name`";
GRANT ROLE SYS:MONITOR to "IAM:`user-name`";
GRANT ROLE SYS:MONITOR to "`database-username`";
```

For more information about `SYS:MONITOR`, see
[Amazon Redshift system-defined roles](../dg/r_roles-default.md "../dg/r_roles-default.md") in the _Amazon Redshift Database Developer Guide_.

- Your data is secure and private. Your data is not shared across accounts. Your queries, data, and database schemas are not used to train a generative AI foundation model (FM).
  Your input is used as contextual prompts to the FM to answer only your queries.

## Custom context

The query editor v2 administrator can specify a _custom context_ to tailor the generated SQL to your environment.
A custom context provides domain knowledge and preferences to provide fine-grained control over SQL generation.
A custom context is defined in a JSON file which can be uploaded by the query editor v2 administrator to Amazon Q generative SQL.

The JSON keys used to personalize generated SQL for a data warehouse are follows.

All table references need to follow the three-part notation `database.schema.table`.

**Resources**
A resource specifies the scope or portion of a data asset to which the custom context is applied.

**ResourceId**
Specifies a unique identifier of the resource.

For an Amazon Redshift cluster, specify the `cluster id`.
For an Redshift Serverless workgroup specify the `workgroup name`.

**ResourceType**
Valid value: `REDSHIFT_WAREHOUSE`.

**TablesToInclude**
Specifies a set of tables that are considered for SQL generation.
This field is crucial when you want to limit the scope of SQL queries to a defined subset of available tables.
It can help optimize the generation process by reducing unnecessary table references.
You can pair this field with `TablesToExclude` for finer control over query generation.

**TablesToExclude**
Specifies the set of tables that are excluded from SQL generation.
Use this when certain tables are irrelevant or should not be considered in the query generation process.

**TableAnnotations**
Provides metadata or supplementary information about the tables in use.
These annotations can include table descriptions, usage notes, or any additional attributes that help Amazon Q generative SQL better understand the context or structure of the table.
This is valuable for enhancing the accuracy of SQL generation by adding clarity to the table definitions.

**ColumnsToInclude**
Defines which columns from the specified tables are included when generating SQL queries.
This field helps Amazon Q generative SQL focus on the relevant columns and improves performance by narrowing down the scope of data retrieval.
It ensures the Amazon Q generative SQL only pulls data that’s needed for the given query context.

**ColumnsToExclude**
Specifies the columns that are omitted from consideration in SQL generation.
This can be used when certain columns contain irrelevant or redundant data that should not be considered by Amazon Q generative SQL.
By managing the inclusion and exclusion of columns, you can refine the results and maintain control over the data retrieved.

**ColumnAnnotations**
Similar to `TableAnnotations`, this field provides metadata or annotations specific to individual columns.
These annotations can offer insight into column definitions or special handling instructions.
This information is beneficial in guiding the SQL generation process and ensuring that columns are used appropriately in queries.

**CuratedQueries**
A set of predefined question and answer examples, where the question is written in natural language (NLQ) and the answer is the corresponding SQL query.
These examples help Amazon Q generative SQL understand the kinds of queries it is expected to generate.
They serve as reference points to improve the accuracy and relevance of Amazon Q generative SQL outputs.

**CustomDocuments**
Additional pieces of information or hints provided to Amazon Q generative SQL, such as definitions, domain-specific knowledge, or explanations.
For example, if your business unit uses a unique way to calculate a value, for example "in manufacturing division total sales is price \* revenue" this can be documented here.
These documents enhance the Amazon Q generative SQL ability to interpret the natural language inputs by providing additional context.

**AdditionalTables**
Specifies any additional tables that should be considered for SQL generation but are not part of the data stored in the data warehouse.
This allows the Amazon Q generative SQL to integrate external data sources into its SQL generation logic, broadening its capacity to handle complex data environments.

**AppendToPrompt**
Additional instructions or guidelines provided to Amazon Q generative SQL to guide the SQL generation process.
This can include specific directives on how to structure the query, preferences for certain SQL constructs,
or any other high-level instruction that enhances the quality of the Amazon Q generative SQL output.

The following example custom context shows you the format of the JSON file and defines the following:

- Defines a custom context for the Amazon Redshift data warehouse for cluster `mycluster`.
- Defines specific tables and columns to include and to exclude to help optimize the SQL generation process.
- Defines annotations for the tables and columns called out to include.
- Defines sample curated queries for Amazon Q generative SQL to use.
- Defines custom documents and guardrails to use when generating SQL.
- Defines the DDL for additional tables to use when generating SQL.

```
{
    "resources": [
        {
            "ResourceId": "mycluster",
            "ResourceType": "REDSHIFT_WAREHOUSE",
            "TablesToInclude": [
                "database.schema.table1",
                "database.schema.table2"
            ],
            "TablesToExclude": [
                "database.schema.table3",
                "database.schema.table4"
            ],
            "ColumnsToInclude": {
                "database.schema.table1": [
                    "col1",
                    "col2"
                ],
                "database.schema.table2": [
                    "col1",
                    "col2"
                ]
            },
            "ColumnsToExclude": {
                "database.schema.table5": [
                    "col1",
                    "col2"
                ],
                "database.schema.table6": [
                    "col1",
                    "col2"
                ]
            },
            "TableAnnotations": {
                "database.schema.table1": "table1 refers to Q3 sales",
                "database.schema.table2": "table2 refers to Q4 sales"
            },
            "ColumnAnnotations": {
                "database.schema.table1": {
                    "col1": "col1 refers to Q3 sale total",
                    "col2": "col2 refers to sale location"
                },
                "database.schema.table2": {
                    "col1": "col2 refers to Q4 sale total",
                    "col2": "col2 refers to sale location"
                }
            },
            "CuratedQueries": [
                {
                    "Question": "what is the sales data for Q3",
                    "Answer": "SELECT * FROM table1"
                },
                {
                    "Question": "what is the sales data for Q4",
                    "Answer": "SELECT * FROM table2"
                }
            ],
            "CustomDocuments": [
                "in manufacturing division total sales is price * revenue",
                "in research division total sales is price * revenue"
            ],
            "AdditionalTables": {
                "database.schema.table8": "create table database.schema.table8(col1 int)",
                "database.schema.table9": "create table database.schema.table9(col1 int)"
            },
            "AppendToPrompt": "Apply these guardrails: Queries should never return the secretId field of a user."
        }
    ]
}
```
