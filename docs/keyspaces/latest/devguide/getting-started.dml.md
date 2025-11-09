# Read data from a table using the CQL `SELECT` statement in Amazon Keyspaces

In the [Inserting and loading data into
an Amazon Keyspaces table](getting-started.dml.md "getting-started.dml.md") section, you used the
`SELECT` statement to verify that you had successfully added data to your
table. In this section, you refine your use of `SELECT` to display specific
columns, and only rows that meet specific criteria.

The general form of the `SELECT` statement is as follows.

```
SELECT `column_list` FROM `table_name` [WHERE `condition` [ALLOW FILTERING]] ;
```

###### Topics

- [Select all the data in your
  table](#getting-started.dml.read.all "#getting-started.dml.read.all")
- [Select a subset of
  columns](#getting-started.dml.read.columns "#getting-started.dml.read.columns")
- [Select a subset of rows](#getting-started.dml.read.rows "#getting-started.dml.read.rows")

## Select all the data in your

table

The simplest form of the `SELECT` statement returns all the data in your table.

###### Important

In a production environment, it's typically not a best practice to run this
command, because it returns all the data in your table.

###### To select all your table's data

1. Open AWS CloudShell and connect to Amazon Keyspaces using the following command. Make sure to update `us-east-1`
   with your own Region.

```
cqlsh-expansion cassandra.`us-east-1`.amazonaws.com 9142 --ssl
```

2. Run the following query.

```
SELECT * FROM catalog.book_awards ;
```

Using the wild-card character ( `*` ) for the
`column_list` selects all columns. The output of the statement looks like the following example.

```
 `year | award | category | rank | author | book_title | publisher
------+------------------+-------------+------+--------------------+-----------------------+---------------
 2020 | Wolf | Non-Fiction | 1 | Wang Xiulan | History of Ideas | AnyPublisher
 2020 | Wolf | Non-Fiction | 2 | Ana Carolina Silva | Science Today | SomePublisher
 2020 | Wolf | Non-Fiction | 3 | Shirley Rodriguez | The Future of Sea Ice | AnyPublisher
 2020 | Kwesi Manu Prize | Fiction | 1 | Akua Mansa | Where did you go? | SomePublisher
 2020 | Kwesi Manu Prize | Fiction | 2 | John Stiles | Yesterday | Example Books
 2020 | Kwesi Manu Prize | Fiction | 3 | Nikki Wolf | Moving to the Chateau | AnyPublisher
 2020 | Richard Roe | Fiction | 1 | Alejandro Rosalez | Long Summer | SomePublisher
 2020 | Richard Roe | Fiction | 2 | Arnav Desai | The Key | Example Books
 2020 | Richard Roe | Fiction | 3 | Mateo Jackson | Inside the Whale | AnyPublisher`
```

## Select a subset of

columns

###### To query for a subset of columns

1. Open AWS CloudShell and connect to Amazon Keyspaces using the following command. Make sure to update `us-east-1`
   with your own Region.

```
cqlsh-expansion cassandra.`us-east-1`.amazonaws.com 9142 --ssl
```

2. To retrieve only the `award`, `category`, and
   `year` columns, run the following query.

```
SELECT award, category, year FROM catalog.book_awards ;
```

The output contains only the specified columns in the order listed in the
`SELECT` statement.

```
 `award | category | year
------------------+-------------+------
 Wolf | Non-Fiction | 2020
 Wolf | Non-Fiction | 2020
 Wolf | Non-Fiction | 2020
 Kwesi Manu Prize | Fiction | 2020
 Kwesi Manu Prize | Fiction | 2020
 Kwesi Manu Prize | Fiction | 2020
 Richard Roe | Fiction | 2020
 Richard Roe | Fiction | 2020
 Richard Roe | Fiction | 2020`
```

## Select a subset of rows

When querying a large dataset, you might only want records that meet certain
criteria. To do this, you can append a `WHERE` clause to the end of our
`SELECT` statement.

###### To query for a subset of rows

1. Open AWS CloudShell and connect to Amazon Keyspaces using the following command. Make sure to update `us-east-1`
   with your own Region.

```
cqlsh-expansion cassandra.`us-east-1`.amazonaws.com 9142 --ssl
```

2. To retrieve only the records for the awards of a given year, run the following query.

```
SELECT * FROM catalog.book_awards WHERE year=2020 AND award='Wolf' ;
```

The preceding `SELECT` statement returns the following output.

```
 `year | award | category | rank | author | book_title | publisher
------+-------+-------------+------+--------------------+-----------------------+---------------
 2020 | Wolf | Non-Fiction | 1 | Wang Xiulan | History of Ideas | AnyPublisher
 2020 | Wolf | Non-Fiction | 2 | Ana Carolina Silva | Science Today | SomePublisher
 2020 | Wolf | Non-Fiction | 3 | Shirley Rodriguez | The Future of Sea Ice | AnyPublisher`
```

### Understanding the `WHERE`

clause

The `WHERE` clause is used to filter the data and return only the data that
meets the specified criteria. The specified criteria can be a simple condition or a compound
condition.

###### How to use conditions in a `WHERE` clause

- A simple condition – A single column.

```
WHERE column_name=value
```

You can use a simple condition in a `WHERE` clause if any of
the following conditions are met:

    + The column is the only partition key column of the table.
    + You add `ALLOW FILTERING` after the condition in the `WHERE`
     clause.


    Be aware that using `ALLOW FILTERING` can result in inconsistent performance,
     especially with large, and multi-partitioned tables.

- A compound condition – Multiple simple conditions connected by
  `AND`.

```
WHERE column_name1=value1 AND column_name2=value2 AND column_name3=value3...
```

You can use compound conditions in a `WHERE` clause if any of
the following conditions are met:

    + The columns you can use in the `WHERE` clause need to include either all or a subset of the columns in the
     table's partition key.
     If you want to use only a subset of the columns in the `WHERE` clause, you must include a contiguous set of partition
     key columns from left to right, beginning with the partition key's leading column. For example, if the partition
     key columns are `year`, `month`, and `award` then you can use the following columns in the
     `WHERE` clause:




    	- `year`
    	- `year` AND `month`
    	- `year` AND `month` AND `award`
    + You add `ALLOW FILTERING` after the compound condition
     in the `WHERE` clause, as in the following example.



    ```
    SELECT * FROM my_table WHERE col1=5 AND col2='Bob' ALLOW FILTERING ;
    ```

    Be aware that using `ALLOW FILTERING` can result in inconsistent performance,
     especially with large, and multi-partitioned tables.

### Try it

Create your own CQL queries to find the following from your
`book_awards` table:

- Find the winners of the 2020 Wolf awards and display the book titles and authors, ordered by rank.
- Show the first prize winners for all awards in 2020 and display the book titles and award names.
