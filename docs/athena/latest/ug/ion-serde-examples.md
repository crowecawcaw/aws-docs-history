# Path extractor examples

The following path extractor examples show how to flatten and rename fields or extract
data as Amazon Ion text.

## Flatten and rename

fields

The following example shows a set of search paths that flatten and rename fields.
The example uses search paths to do the following:

- Map the `nickname` column to the `alias`
  field
- Map the `name` column to the `name` subfield located
  in the `identification` struct.

Following is the example Amazon Ion document.

```
-- Example Amazon Ion Document
{
    identification: {
        name: "John Smith",
        driver_license: "XXXX"
    },

    alias: "Johnny"
}
```

The following is the example `CREATE TABLE` statement that defines the
path extractors.

```
-- Example DDL Query
CREATE EXTERNAL TABLE example_schema2 (
    name STRING,
    nickname STRING
)
ROW FORMAT SERDE
 'com.amazon.ionhiveserde.IonHiveSerDe'
WITH SERDEPROPERTIES (
 'ion.nickname.path_extractor' = '(alias)',
 'ion.name.path_extractor' = '(identification name)'
 )
STORED AS ION
LOCATION 's3://amzn-s3-demo-bucket/path_extraction2/'
```

The following example shows the extracted data.

```
-- Extracted Table
| name         |   nickname   |
|--------------|--------------|
| "John Smith" |  "Johnny"    |
```

For more information about search paths and additional search path examples, see
the [Ion Java Path
Extraction](https://github.com/amzn/ion-java-path-extraction "https://github.com/amzn/ion-java-path-extraction") page on GitHub.

## Extract flight

data to text format

The following example `CREATE TABLE` query uses `WITH
 SERDEPROPERTIES` to add path extractors to extract flight data and specify
the output encoding as Amazon Ion text. The example uses the `STORED AS
 ION` syntax.

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
WITH SERDEPROPERTIES (
 'ion.encoding' = 'TEXT',
 'ion.yr.path_extractor'='(year)',
 'ion.quarter.path_extractor'='(results quarter)',
 'ion.month.path_extractor'='(date month)')
STORED AS ION
LOCATION 's3://amzn-s3-demo-bucket/'
```
