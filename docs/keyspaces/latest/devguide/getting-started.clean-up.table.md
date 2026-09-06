

# Delete a table in Amazon Keyspaces
<a name="getting-started.clean-up.table"></a>

To avoid being charged for tables and data that you don't need, delete all the tables that you're not using. When you delete a table, the table and its data are deleted and you stop accruing charges for them. However, the keyspace remains. When you delete a keyspace, the keyspace and all its tables are deleted and you stop accruing charges for them.

You can delete a table using the console, CQL, or the AWS CLI. When you delete a table, the table and all its data are deleted.

## Using the console
<a name="getting-started.clean-up.table.con"></a>

The following procedure deletes a table and all its data using the AWS Management Console.

**To delete a table using the console**

1. Sign in to the AWS Management Console, and open the Amazon Keyspaces console at [https://console.aws.amazon.com/keyspaces/home](https://console.aws.amazon.com/keyspaces/home).

1. In the navigation pane, choose **Tables**.

1. Choose the box to the left of the name of each table that you want to delete.

1. Choose **Delete**.

1. On the **Delete table** screen, enter **Delete** in the box. Then, choose **Delete table**.

1. To verify that the table was deleted, choose **Tables** in the navigation pane, and confirm that the `book_awards` table is no longer listed.

## Using CQL
<a name="getting-started.clean-up.table.cql"></a>

The following procedure deletes a table and all its data using CQL.

**To delete a table using CQL**

1. Open AWS CloudShell and connect to Amazon Keyspaces using the following command. Make sure to update {{us-east-1}} with your own Region. 

   ```
   cqlsh-expansion cassandra.{{us-east-1}}.amazonaws.com 9142 --ssl
   ```

1. Delete your table by entering the following statement.

   ```
   DROP TABLE IF EXISTS catalog.book_awards ;
   ```

1. Verify that your table was deleted.

   ```
   SELECT * FROM system_schema.tables WHERE keyspace_name = 'catalog' ;
   ```

   The output should look like this. Note that this might take some time, so re-run the statement after a minute if you don't see this result.

   ```
   keyspace_name | table_name | bloom_filter_fp_chance | caching | cdc | comment | compaction | compression | crc_check_chance | dclocal_read_repair_chance | default_time_to_live | extensions | flags | gc_grace_seconds | id | max_index_interval | memtable_flush_period_in_ms | min_index_interval | read_repair_chance | speculative_retry
   ---------------+------------+------------------------+---------+-----+---------+------------+-------------+------------------+----------------------------+----------------------+------------+-------+------------------+----+--------------------+-----------------------------+--------------------+--------------------+-------------------
   
   (0 rows)
   ```

## Using the AWS CLI
<a name="getting-started.clean-up.table.cli"></a>

The following procedure deletes a table and all its data using the AWS CLI.

**To delete a table using the AWS CLI**

1. Open CloudShell 

1. Delete your table with the following statement.

   ```
   aws keyspaces delete-table --keyspace-name 'catalog' --table-name 'book_awards'
   ```

1. To verify that your table was deleted, you can list all tables in a keyspace.

   ```
   aws keyspaces list-tables --keyspace-name 'catalog'
   ```

   You should see the following output. Note that this asynchronous operation can take some time. Re-run the command again after a short while to confirm that the table has been deleted.

   ```
   {
       "tables": []
   }
   ```