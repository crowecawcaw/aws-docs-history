# Add tags when creating a new table

You can use the Amazon Keyspaces console, CQL or the AWS CLI to add tags to new tables when you create
them.

Console

###### Add a tag when creating a new table using the (console)

1. Sign in to the AWS Management Console, and open the Amazon Keyspaces console at [https://console.aws.amazon.com/keyspaces/home](https://console.aws.amazon.com/keyspaces/home "https://console.aws.amazon.com/keyspaces/home").
2. In the navigation pane, choose **Tables**, and then choose
   **Create table**.
3. On the **Create table** page in the **Table details** section, select a keyspace and provide a name for the
   table.
4. In the **Schema** section, create the schema for your table.
5. In the **Table settings** section, choose **Customize
   settings**.
6. Continue to the **Table tags – _optional_** section, and choose **Add new
   tag** to create new tags.
7. Choose **Create table**.

Cassandra Query Language (CQL)

###### Add tags when creating a new table using CQL

- The following example creates a new table with tags.

```
CREATE TABLE `mytable(...)` WITH TAGS = `{'key1':'val1', 'key2':'val2'}`;
```

CLI

###### Add tags when creating a new table using the AWS CLI

- The following example shows how to create a new table with tags. The command creates a table
  _myTable_ in an already existing keyspace _myKeyspace_.
  Note that the command has been broken
  up into different lines to help with readability.

```
aws keyspaces create-table --keyspace-name 'myKeyspace' --table-name 'myTable'
            --schema-definition 'allColumns=[{name=id,type=int},{name=name,type=text},{name=date,type=timestamp}],partitionKeys=[{name=id}]'
            --tags 'key=key1,value=val1' 'key=key2,value=val2'
```
