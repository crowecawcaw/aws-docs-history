# Creating a Snowflake target node

## Permissions needed

AWS Glue Studio jobs using Snowflake data sources require additional permissions. For more information on how to
add permissions to ETL jobs, see
[Review IAM permissions needed for ETL jobs](../ug/setting-up.md#getting-started-min-privs-job "../ug/setting-up.md#getting-started-min-privs-job").

`SNOWFLAKE` AWS Glue connections use an AWS Secrets Manager secret to provide credential information.
Your job and data preview roles in AWS Glue Studio must have permission to read this secret.

## Adding a Snowflake data target

###### To create a Snowflake target node:

1.  Choose an existing Snowflake table as the target, or enter a new table name.
2.  When you use the **Data target - Snowflake** target node, you can choose from the following options:
    - **APPEND** – If a table already exists, dump all the new data into the table as an insert.
      If the table doesn't exist, create it and then insert all new data.
    - **MERGE** – AWS Glue will update or append data to your target table
      based on the conditions you specify.

    Choose options:

        + **Choose keys and simple actions** – choose the columns to be used as
         matching keys between the source data and your target data set.


        Specify the following options when matched:




        	- Update record in your target data set with data from source.
        	- Delete record in your target data set.
        Specify the following options when not matched:




        	- Insert source data as a new row into your target data set.
        	- Do nothing.
        + **Enter custom MERGE statement** – You can then choose **Validate
         Merge statement** to verify that the statement is valid or invalid.

    - **TRUNCATE** – If a table already exists, truncate the table data by first clearing the
      contents of the target table. If truncate is successful, then insert all data. If the table doesn't exist, create the
      table and insert all data. If truncate is not successful, the operation will fail.
    - **DROP** – If a table already exists, delete the table metadata and data. If deletion is successful,
      then insert all data. If the table doesn't exist, create the table and insert all data. If drop is not successful,
      the operation will fail.
