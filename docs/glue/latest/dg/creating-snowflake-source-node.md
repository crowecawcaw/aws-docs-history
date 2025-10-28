# Creating a Snowflake source node

## Permissions needed

AWS Glue Studio jobs using Snowflake data sources require additional permissions. For more information on how to
add permissions to ETL jobs, see
[Review IAM permissions needed for ETL jobs](../ug/setting-up.md#getting-started-min-privs-job "../ug/setting-up.md#getting-started-min-privs-job").

`SNOWFLAKE` AWS Glue connections use an AWS Secrets Manager secret to provide credential information.
Your job and data preview roles in AWS Glue Studio must have permission to read this secret.

## Adding a Snowflake data source

**Prerequisites**:

- An AWS Secrets Manager secret for your Snowflake credentials
- A Snowflake type AWS Glue Data Catalog connection

###### To add a **Data Source – Snowflake** node:

1. Choose the connection for your Snowflake data source.
   This assumes that the connection already exists and you can select from existing connections. If you need to create a
   connection, choose **Create Snowflake connection**. For more information, see
   [Overview of using connectors and connections](../ug/connectors-chapter.md#using-connectors-overview "../ug/connectors-chapter.md#using-connectors-overview") .

Once you have chosen a connection, you can view the connection properties by clicking **View properties**.
Information about the connection are visible, including URL, security groups, subnet, availability zone, description, and
created (UTC) and last updated (UTC) timestamps. 2. Choose a Snowflake source option:

    * **Choose a single table** – this is the table that contains the data you want to access from a
     single Snowflake table.
    * **Enter custom query**  – allows you to access a dataset from multiple Snowflake
     tables based on your custom query.

3. If you chose a single table, enter the name of a Snowflake schema.

Or, choose **Enter custom query**. Choose this option to access a custom dataset from multiple
Snowflake tables. When you choose this option, enter the Snowflake query. 4. In **Performance and security** options (optional),

    * **Enable query pushdown** – choose if you want to offload work to the Snowflake instance.

5. In **Custom Snowflake properties** (optional), enter parameters and values as needed.
