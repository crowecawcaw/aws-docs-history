# Differences between a relational (SQL) database

and DynamoDB when creating a table

Tables are the fundamental data structures in relational databases and in Amazon DynamoDB. A
relational database management system (RDBMS) requires you to define the table's schema
when you create it. In contrast, DynamoDB tables are schemaless—other than the
primary key, you do not need to define any extra attributes or data types when you
create a table.

The following section compares how you would create a table with SQL to how you would
create it with DynamoDB.

###### Topics

- [Creating a table with SQL](#SQLtoNoSQL.CreateTable.SQL "#SQLtoNoSQL.CreateTable.SQL")
- [Creating a table with
  DynamoDB](#SQLtoNoSQL.CreateTable.DynamoDB "#SQLtoNoSQL.CreateTable.DynamoDB")

## Creating a table with SQL

With SQL you would use the `CREATE TABLE` statement to create a table,
as shown in the following example.

```
CREATE TABLE Music (
    Artist VARCHAR(20) NOT NULL,
    SongTitle VARCHAR(30) NOT NULL,
    AlbumTitle VARCHAR(25),
    Year INT,
    Price FLOAT,
    Genre VARCHAR(10),
    Tags TEXT,
    PRIMARY KEY(Artist, SongTitle)
);
```

The primary key for this table consists of _Artist_ and
_SongTitle_.

You must define all of the table's columns and data types, and the table's primary
key. (You can use the `ALTER TABLE` statement to change these definitions
later, if necessary.)

Many SQL implementations let you define storage specifications for your table, as
part of the `CREATE TABLE` statement. Unless you indicate otherwise, the
table is created with default storage settings. In a production environment, a
database administrator can help determine the optimal storage parameters.

## Creating a table with

DynamoDB

Use the `CreateTable` operation to create a provisioned mode table,
specifying parameters as shown following:

```
{
    TableName : "Music",
    KeySchema: [
        {
            AttributeName: "Artist",
            KeyType: "HASH" //Partition key
        },
        {
            AttributeName: "SongTitle",
            KeyType: "RANGE" //Sort key
        }
    ],
    AttributeDefinitions: [
        {
            AttributeName: "Artist",
            AttributeType: "S"
        },
        {
            AttributeName: "SongTitle",
            AttributeType: "S"
        }
    ],
    ProvisionedThroughput: {       // Only specified if using provisioned mode
        ReadCapacityUnits: 1,
        WriteCapacityUnits: 1
    }
}
```

The primary key for this table consists of _Artist_ (partition
key) and _SongTitle_ (sort key).

You must provide the following parameters to `CreateTable`:

- `TableName` – Name of the table.
- `KeySchema` – Attributes that are used for the primary
  key. For more information, see [Tables, items, and
  attributes](HowItWorks.md#HowItWorks.CoreComponents.TablesItemsAttributes "HowItWorks.md#HowItWorks.CoreComponents.TablesItemsAttributes") and
  [Primary key](HowItWorks.md#HowItWorks.CoreComponents.PrimaryKey "HowItWorks.md#HowItWorks.CoreComponents.PrimaryKey").
- `AttributeDefinitions` – Data types for the key schema
  attributes.
- `ProvisionedThroughput (for provisioned tables)` – Number
  of reads and writes per second that you need for this table. DynamoDB reserves
  sufficient storage and system resources so that your throughput requirements
  are always met. You can use the `UpdateTable` operation to change
  these later, if necessary. You do not need to specify a table's storage
  requirements because storage allocation is managed entirely by DynamoDB.
