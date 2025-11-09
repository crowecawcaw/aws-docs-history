# Create Amazon Ion tables

To create a table in Athena from data stored in Amazon Ion format, you can use one of the
following techniques in a CREATE TABLE statement:

- Specify `STORED AS ION`. In this usage, you do not have to specify the
  Amazon Ion Hive SerDe explicitly. This choice is the more straightforward
  option.
- Specify the Amazon Ion class paths in the `ROW FORMAT SERDE`,
  `INPUTFORMAT`, and `OUTPUTFORMAT` fields.
  You can also use `CREATE TABLE AS SELECT` (CTAS) statements to create Amazon
  Ion tables in Athena. For information, see [Use CTAS and
  INSERT INTO to create Amazon Ion tables](ion-serde-using-ctas-and-insert-into-to-create-ion-tables.md "ion-serde-using-ctas-and-insert-into-to-create-ion-tables.md").

## Specify STORED AS ION

The following example `CREATE TABLE` statement uses `STORED AS
 ION` before the `LOCATION` clause to create a table based on flight
data in Amazon Ion format. The `LOCATION` clause specifies the bucket or
folder where the input files in Ion format are located. All files in the specified
location are scanned.

```
CREATE EXTERNAL TABLE flights_ion (
    yr INT,
    quarter INT,
    month INT,
    dayofmonth INT,
    dayofweek INT,
    flightdate STRING,
    uniquecarrier STRING,
    airlineid INT,
)
STORED AS ION
LOCATION 's3://amzn-s3-demo-bucket/'
```

## Specify the Amazon Ion class

paths

Instead of using the `STORED AS ION` syntax, you can explicitly specify the
Ion class path values for the `ROW FORMAT SERDE`, `INPUTFORMAT`,
and `OUTPUTFORMAT` clauses as follows.

| Parameter               | Ion class path                                      |
| ----------------------- | --------------------------------------------------- |
| `ROW FORMAT SERDE`      | `'com.amazon.ionhiveserde.IonHiveSerDe'`            |
| `STORED AS INPUTFORMAT` | `'com.amazon.ionhiveserde.formats.IonInputFormat'`  |
| `OUTPUTFORMAT`          | `'com.amazon.ionhiveserde.formats.IonOutputFormat'` |

The following DDL query uses this technique to create the same external table as in
the previous example.

```
CREATE EXTERNAL TABLE flights_ion (
    yr INT,
    quarter INT,
    month INT,
    dayofmonth INT,
    dayofweek INT,
    flightdate STRING,
    uniquecarrier STRING,
    airlineid INT,
)
ROW FORMAT SERDE
 'com.amazon.ionhiveserde.IonHiveSerDe'
STORED AS INPUTFORMAT
 'com.amazon.ionhiveserde.formats.IonInputFormat'
OUTPUTFORMAT
 'com.amazon.ionhiveserde.formats.IonOutputFormat'
LOCATION 's3://amzn-s3-demo-bucket/'
```

For information about the SerDe properties for `CREATE TABLE` statements in
Athena, see [Amazon Ion SerDe property
reference](ion-serde-using-ion-serde-properties.md "ion-serde-using-ion-serde-properties.md").
