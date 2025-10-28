Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Create a table

After you create your new database, create tables to hold your data. Specify the
column information when you create the table.

For example, to create a table named `DEMO`, run the following
command.

```
CREATE TABLE Demo (
  PersonID int,
  City varchar (255)
);
```

By default, new database objects, such as tables, are created in the default schema
named `public` created during data warehouse creation. You can use another schema to
create database objects. For more information about schemas, see [Managing database security](../dg/r_Database_objects.md "../dg/r_Database_objects.md") in the
_Amazon Redshift Database Developer Guide_.

You can also create a table using the `schema_name.object_name` notation to
create the table in the `SALES` schema.

```
CREATE TABLE SALES.DEMO (
  PersonID int,
  City varchar (255)
);
```

To view and inspect schemas and their tables, you can use the Amazon Redshift query editor v2 . Or
you can see the list of tables in schemas using system views. For more information, see
[Query the system tables and views](t_querying_redshift_system_tables.md "t_querying_redshift_system_tables.md").

The `encoding`, `distkey`, and `sortkey` columns are
used by Amazon Redshift for parallel processing. For more information about designing tables
that incorporate these elements, see [Amazon Redshift best practices for designing tables](../dg/c_designing-tables-best-practices.md "../dg/c_designing-tables-best-practices.md").

## Insert data rows into a table

After you create a table, insert rows of data into that table.

###### Note

The [INSERT](../dg/r_INSERT_30.md "../dg/r_INSERT_30.md") command inserts
rows into a table. For standard bulk loads, use the [COPY](../dg/r_COPY.md "../dg/r_COPY.md") command. For more information,
see [Use a COPY command
to load data](../dg/c_best-practices-use-copy.md "../dg/c_best-practices-use-copy.md").

For example, to insert values into the `DEMO` table, run the following
command.

```
INSERT INTO DEMO VALUES (781, 'San Jose'), (990, 'Palo Alto');
```

To insert data into a table that's in a specific schema, run the following command.

```
INSERT INTO SALES.DEMO VALUES (781, 'San Jose'), (990, 'Palo Alto');
```

## Select data from a table

After you create a table and populate it with data, use a SELECT statement to
display the data contained in the table. The SELECT \* statement returns all the
column names and row values for all of the data in a table. Using SELECT is a good
way to verify that recently added data was correctly inserted into the table.

To view the data that you entered in the `DEMO` table, run
the following command.

```
SELECT * from DEMO;
```

The result should look like the following.

```
 personid |   city
----------+-----------
      781 | San Jose
      990 | Palo Alto
(2 rows)
```

For more information about using the SELECT statement to query tables, see [SELECT](../dg/r_SELECT_synopsis.md "../dg/r_SELECT_synopsis.md").
