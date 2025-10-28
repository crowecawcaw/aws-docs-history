# CREATE PUMP

A pump is an Amazon Kinesis Data Analytics Repository Object (an extension of the SQL standard) that provides a continuously running INSERT INTO stream SELECT ... FROM query functionality, thereby enabling the results of a query to be continuously entered into a named stream.

You need to specify a column list for both the query and the named stream (these imply a set of source-target pairs).
The column lists need to match in terms of datatype, or the SQL validator will reject them.
(These need not list all columns in the target stream; you can set up a pump for one column.)

For more information, see [SELECT statement](sql-reference-select.md "sql-reference-select.md").

The following code first creates and sets a schema, then creates two streams in this schema:

- "OrderDataWithCreateTime" which will serve as the origin stream for the pump.
- "OrderData" which will serve as the destination stream for the pump.

```
CREATE OR REPLACE STREAM "OrderDataWithCreateTime" (
"key_order" VARCHAR(20),
"key_user" VARCHAR(20),
"key_billing_country" VARCHAR(20),
"key_product" VARCHAR(20),
"quantity" VARCHAR(20),
"eur" VARCHAR(20),
"usd" VARCHAR(20))
DESCRIPTION 'Creates origin stream for pump';

CREATE OR REPLACE STREAM "OrderData" (
"key_order" VARCHAR(20),
"key_user" VARCHAR(20),
"country" VARCHAR(20),
"key_product" VARCHAR(20),
"quantity" VARCHAR(20),
"eur" INTEGER,
"usd" INTEGER)
DESCRIPTION 'Creates destination stream for pump';

```

The following code uses these two streams to create a pump. Data is selected from "OrderDataWithCreateTime"
and inserted into "OrderData".

```
CREATE OR REPLACE PUMP "200-ConditionedOrdersPump" AS
INSERT INTO "OrderData" (
"key_order", "key_user", "country",
"key_product", "quantity", "eur", "usd")
//note that this list matches that of the query
SELECT STREAM
"key_order", "key_user", "key_billing_country",
"key_product", "quantity", "eur", "usd"
//note that this list matches that of the insert statement
FROM "OrderDataWithCreateTime";

```

For more detail, see the topic [In-Application Streams and Pumps](../dev/streams-pumps.md "../dev/streams-pumps.md") in the _Amazon Managed Service for Apache Flink Developer Guide_.

## Syntax

```
 CREATE [ OR REPLACE ] PUMP <qualified-pump-name>
                       [ DESCRIPTION '<string-literal>' ] AS <streaming-insert>

```

where streaming-insert is an insert statement such as:

```
INSERT INTO ''stream-name'' SELECT "columns" FROM <source stream>
```
