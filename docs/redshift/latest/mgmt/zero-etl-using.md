Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Querying replicated

data in Amazon Redshift

After you add data to your source, it's replicated in near real time to the Amazon Redshift data
warehouse, and it's ready for querying. For information about integration metrics and table
statistics, see [Metrics for zero-ETL integrations](zero-etl-using.md "zero-etl-using.md").

###### Note

As a database is the same as a schema in MySQL, MySQL database level maps to Amazon Redshift schema
level. Note this mapping difference when you query data replicated from Aurora MySQL or
RDS for MySQL.

###### To query replicated data

1. Navigate to the Amazon Redshift console and choose **Query editor
   v2**.
2. Connect to your Amazon Redshift Serverless workgroup or Amazon Redshift provisioned cluster and choose your
   database from the dropdown list.
3. Use a SELECT statement to select all replicated data from the schema and table that
   you created in the source. For case sensitivity, use double quotes (" ") for schema,
   table, and column names. For example:

```
SELECT * FROM "`schema_name`"."`table_name`";
```

You can also query the data using the Amazon Redshift Data API.

## Querying replicated data with materialized

views

You can create materialized views in your local Amazon Redshift database to transform data
replicated through zero-ETL integrations.
Connect
to your local database and use cross-database queries to access the destination databases.
You can use either fully qualified object names with the three-part notation
(destination-database-name.schema-name.table-name) or create an external schema referencing
the destination database-schema pair and use the two-part notation
(external-schema-name.table-name). For more information on cross-database queries, see
[Querying
data across databases](../dg/cross-database-overview.md "../dg/cross-database-overview.md").

Use the following example to create and insert sample data into the
`sales_zetl` and `event_zetl` tables
from the source `tickit_zetl`. The tables are replicated into the
Amazon Redshift database `zetl_int_db`.

```
CREATE TABLE sales_zetl (
        salesid integer NOT NULL primary key,
        eventid integer NOT NULL,
        pricepaid decimal(8, 2)
);

CREATE TABLE event_zetl (
        eventid integer NOT NULL PRIMARY KEY,
        eventname varchar(200)
);

INSERT INTO sales_zetl VALUES(1, 1, 3.33);
INSERT INTO sales_zetl VALUES(2, 2, 4.44);
INSERT INTO sales_zetl VALUES(3, 2, 5.55);

INSERT INTO event_zetl VALUES(1, "Event 1");
INSERT INTO event_zetl VALUES(2, "Event 2");
```

You can create a materialized view to get total sales per event using the three-part
notation:

```
--three part notation zetl-database-name.schema-name.table-name
CREATE MATERIALIZED VIEW mv_transformed_sales_per_event_3p
AUTO REFRESH YES
AS
(SELECT eventname, sum(pricepaid) as total_price
FROM  zetl_int_db.tickit_zetl.sales_zetl S, zetl_int_db.tickit_zetl.event_zetl E
WHERE S.eventid = E.eventid
GROUP BY 1);
```

You can create a materialized view to get total sales per event using the two-part
notation:

```
--two part notation external-schema-name.table-name notation
CREATE EXTERNAL schema ext_tickit_zetl
FROM REDSHIFT
DATABASE zetl_int_db
SCHEMA tickit_zetl;

CREATE MATERIALIZED VIEW mv_transformed_sales_per_event_2p
AUTO REFRESH YES
AS
(
    SELECT eventname, sum(pricepaid) as total_price
    FROM  ext_tickit_zetl.sales_zetl S, ext_tickit_zetl.event_zetl E
    WHERE S.eventid = E.eventid
    GROUP BY 1
);
```

To view the materialized views you created, use the following example.

```
`SELECT * FROM mv_transformed_sales_per_event_3p;`

`+-----------+-------------+
| eventname | total_price |
+-----------+-------------+
| Event 1 | 3.33 |
| Event 2 | 9.99 |
+-----------+-------------+`

`SELECT * FROM mv_transformed_sales_per_event_2p;`

`+-----------+-------------+
| eventname | total_price |
+-----------+-------------+
| Event 1 | 3.33 |
| Event 2 | 9.99 |
+-----------+-------------+`
```

## Querying replicated data from DynamoDB

When you replicate data from Amazon DynamoDB to a Amazon Redshift database, it is stored in a
materialized view in a column of SUPER data type.

For this example, the following data is stored in DynamoDB.

```
{
    "key1": {
        "S": "key_1"
    },
    "key2": {
        "N": 0
    },
    "payload": {
        "L": [
            {
                "S": "sale1"
            },
            {
                "S": "sale2"
            },
        ]
    },
}
```

The Amazon Redshift materialized view is defined as the following.

```
CREATE MATERIALIZED VIEW mv_sales
                    BACKUP NO
                    AUTO REFRESH YES
                    AS
                    SELECT "value"."payload"."L"[0]."S"::VARCHAR AS first_payload
                    FROM public.sales;
```

To view the data in the materialized view run an SQL command.

```
SELECT first_payload FROM mv_sales;
```
