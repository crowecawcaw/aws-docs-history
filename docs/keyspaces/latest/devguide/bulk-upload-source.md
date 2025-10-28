# Step 1: Create the source CSV file and a target table for the data upload

For this tutorial, we use a comma-separated values (CSV) file with the
name `keyspaces_sample_table.csv` as the source file for the
data migration. The provided sample file contains a few rows of data for a table with the name `book_awards`.

1.  Create the source file. You can choose one of the following options:
    - Download the sample CSV file (`keyspaces_sample_table.csv`) contained in the
      following archive file [samplemigration.zip](samples/samplemigration.md "samples/samplemigration.md").
      Unzip the archive and take note of the path to `keyspaces_sample_table.csv`.
    - To populate a CSV file with your own data stored in an Apache Cassandra
      database, you can populate the source CSV file by using the `cqlsh`
      `COPY TO` statement as shown in the following example.

    ```
    cqlsh localhost 9042 -u "`username`" -p "`password`" --execute "COPY `mykeyspace.mytable` TO 'keyspaces_sample_table.csv' WITH HEADER=true";
    ```

    Make sure the CSV file you create meets the following
    requirements:

        + The first row contains the column names.
        + The column names in the source CSV file match the column names in the target table.
        + The data is delimited with a comma.
        + All data values are valid Amazon Keyspaces data types. See [Data types](cql.md#cql.data-types "cql.md#cql.data-types").

2.  Create the target keyspace and table in Amazon Keyspaces.
    1. Connect to Amazon Keyspaces using `cqlsh`, replacing the service endpoint, user name, and
       password in the following example with your own values.

    ```
    cqlsh cassandra.`us-east-1`.amazonaws.com 9142 -u "`111122223333`" -p "`wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`" --ssl
    ```

    2. Create a new keyspace with the name `catalog` as shown in the following
       example.

    ```
    CREATE KEYSPACE `catalog` WITH REPLICATION = {'class': 'SingleRegionStrategy'};
    ```

    3. When the new keyspace is available, use the following code to create the target table `book_awards`.

    ````
    CREATE TABLE "`catalog.book_awards`" (
       year int,
       award text,
       rank int,
       category text,
       book_title text,
       author text,
       publisher text,
       PRIMARY KEY ((year, award), category, rank)
       );
    ```If Apache Cassandra is your original data source, a simple way to create the
    Amazon Keyspaces target table with matching headers is to generate the `CREATE
    TABLE` statement from the source table, as shown in the following
    statement.
    ````

```
cqlsh localhost 9042  -u "username" -p "password" --execute "DESCRIBE TABLE `mykeyspace.mytable`;"
```

Then create the target table in Amazon Keyspaces with the column names and data types matching the description from the Cassandra source table.
