Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Using COPY to load data into SUPER columns

In the following sections, you can learn about different ways to use the COPY command
to load JSON data into Amazon Redshift. For information about the data format parameters that Amazon Redshift
uses to parse JSON in COPY commands, read the [JSON format for COPY](copy-parameters-data-format.md#copy-json "copy-parameters-data-format.md#copy-json")
parameter description in [Data format parameters](copy-parameters-data-format.md "copy-parameters-data-format.md").

###### Topics

- [Copying data from JSON and Avro](#copy_json-from-JSON "#copy_json-from-JSON")
- [Copying data from text and CSV](#copy_json-from-text-csv "#copy_json-from-text-csv")
- [Copying data from columnar-format
  Parquet and ORC](#copy_json-from-parquet-orc "#copy_json-from-parquet-orc")

## Copying data from JSON and Avro

Amazon Redshift provides the following methods to ingest a JSON document using COPY, even with a JSON
structure that is fully or partially unknown:

- Store the data deriving from a JSON document into a single SUPER data column
  using the `noshred` option. This method is useful when the schema
  isn't known or is expected to change. Thus, this method makes it easier to
  store the entire tuple in a single SUPER column.
- Shred the JSON document into multiple Amazon Redshift columns using the `auto` or `jsonpaths` option. Attributes can be Amazon Redshift
  scalars or SUPER values.
  You can use these options with the JSON or Avro formats. For more information on JSON options such as `noshred`, `auto`, and `jsonpaths`, see
  [JSON format for COPY](copy-parameters-data-format.md#copy-json "copy-parameters-data-format.md#copy-json").

The maximum size for a JSON object in Amazon Redshift is 4 MB, which applies before any shredding or parsing.

### Method 1: Copying a JSON document into a single SUPER

data column using `noshred`

You can copy entire JSON documents into single SUPER data columns using the `noshred`
option in the COPY command. Consider the following example:

1. Create a table with a single
   SUPER data column.

```
CREATE TABLE region_nations_noshred (rdata SUPER);
```

2. Copy the data from Amazon S3 into the single SUPER data column. To ingest the JSON source
   data into a single SUPER data column, specify the `noshred` option in the
   FORMAT JSON clause.

```
COPY region_nations_noshred FROM 's3://redshift-downloads/semistructured/tpch-nested/data/json/region_nation'
REGION 'us-east-1' IAM_ROLE 'arn:aws:iam::xxxxxxxxxxxx:role/Redshift-S3'
FORMAT JSON 'noshred';
```

After COPY has successfully ingested the JSON, your table has a `rdata`
SUPER data column that contains the data of the entire JSON object. The ingested data
maintains all the properties of the JSON hierarchy. However, the leaves are converted
to Amazon Redshift scalar types for efficient query processing. 3. Use the following query to retrieve the original JSON string.

```
SELECT rdata FROM region_nations_noshred;
```

When Amazon Redshift generates a SUPER data column, it becomes accessible using JDBC as a
string through JSON serialization. For more information, see [Serializing complex nested JSON](serializing-complex-JSON.md "serializing-complex-JSON.md").

### Method 2: Copying a JSON document into multiple

SUPER data columns

You can shred a JSON document into multiple columns that can be either SUPER data
columns or Amazon Redshift scalar types. Amazon Redshift spreads different portions of the JSON object
to different columns. Consider the following example:

1. Create a table with multiple columns to hold the shredded JSON.

```
CREATE TABLE region_nations
(
 r_regionkey smallint
 ,r_name varchar
 ,r_comment varchar
 ,r_nations super
 );
```

2. To copy JSON into the `region_nations` table,
   specify the AUTO option in the FORMAT JSON clause to split the JSON
   value across multiple columns. COPY matches the top-level JSON
   attributes with column names and allows nested values to be
   ingested as SUPER values, such as JSON arrays and objects.

```
COPY region_nations FROM 's3://redshift-downloads/semistructured/tpch-nested/data/json/region_nation'
REGION 'us-east-1' IAM_ROLE 'arn:aws:iam::xxxxxxxxxxxx:role/Redshift-S3'
FORMAT JSON 'auto';
```

When the JSON attribute names are in mixed upper and lower cases, specify the `auto ignorecase` option in
the FORMAT JSON clause. For more information about the COPY command, see
[Load from JSON data using the
'auto ignorecase' option](r_COPY_command_examples.md#copy-from-json-examples-using-auto-ignorecase "r_COPY_command_examples.md#copy-from-json-examples-using-auto-ignorecase").

In some cases, there is a mismatch between column names and JSON attributes or the
attribute to load is nested more than a level deep. If so, use a
`jsonpaths` file to manually map JSON attributes to Amazon Redshift
columns. Consider the following example:

1. Create a table with multiple columns to hold the shredded JSON.

```
CREATE TABLE region_nations
(
 r_regionkey smallint
 ,r_name varchar
 ,r_comment varchar
 ,r_nations super
 );
```

2. In this case, the column names don't match
   the JSON attributes. You can create a `jsonpaths` file that maps the paths of
   attributes to the table columns by their position in the `jsonpaths`
   array, like the following:

```
{"jsonpaths": [
       "$.r_regionkey",
       "$.r_name",
       "$.r_comment",
       "$.r_nations
    ]
}
```

3. Use the location of the `jsonpaths` file as the argument to the FORMAT
   JSON option in COPY.

```
COPY nations FROM 's3://redshift-downloads/semistructured/tpch-nested/data/json/region_nation'
REGION 'us-east-1' IAM_ROLE 'arn:aws:iam::xxxxxxxxxxxx:role/Redshift-S3'
FORMAT JSON 's3://redshift-downloads/semistructured/tpch-nested/data/jsonpaths/nations_jsonpaths.json';
```

4. Use the following query to access the table that shows data spread to multiple columns.
   The SUPER data columns are printed using the JSON format.

```
SELECT r_regionkey,r_name,r_comment,r_nations[0].n_nationkey FROM region_nations ORDER BY 1,2,3 LIMIT 1;
```

`jsonpaths` files map fields in the JSON document to table columns.
You can extract additional columns, such as distribution and sort keys, while still loading the complete
document as a SUPER column. The following query loads the complete document to the `nations` column.
The `name` column is the sort key and the `regionkey` column is the distribution key.
Consider the following example:

1. Create a table with multiple columns to hold the shredded JSON.

```
CREATE TABLE nations_sorted (
    regionkey smallint,
    name varchar,
    nations super
) DISTKEY(regionkey) SORTKEY(name);
```

2. Map the root jsonpath "$" to the root of the document as follows:

```
{"jsonpaths": [
       "$.r_regionkey",
       "$.r_name",
       "$"
    ]
}
```

3. Use the location of the `jsonpaths` file as the argument to the FORMAT
   JSON option in COPY.

```
COPY nations_sorted FROM 's3://redshift-downloads/semistructured/tpch-nested/data/json/region_nation'
REGION 'us-east-1' IAM_ROLE 'arn:aws:iam::xxxxxxxxxxxx:role/Redshift-S3'
FORMAT JSON 's3://redshift-downloads/semistructured/tpch-nested/data/jsonpaths/nations_sorted_jsonpaths.json';
```

For more information on using `jsonpaths`, see
[COPY from JSON format](copy-usage_notes-copy-from-json.md "copy-usage_notes-copy-from-json.md").

## Copying data from text and CSV

Amazon Redshift represents SUPER columns in text and CSV formats as serialized JSON. Valid JSON formatting is required
for SUPER columns to load with the correct type information. Unquote objects, arrays, numbers, booleans, and null
values. Wrap string values in double quotes. SUPER columns use standard escaping rules for text and CSV formats.

When copying from CSV, delimiters are escaped according to the CSV standard. Consider the following example:

```
CREATE TABLE region_nations
(
 r_regionkey smallint
 ,r_name varchar
 ,r_comment varchar
 ,r_nations super
 );

 COPY region_nations FROM 's3://redshift-downloads/semistructured/tpch-nested/data/csv/region_nation'
REGION 'us-east-1' IAM_ROLE 'arn:aws:iam::xxxxxxxxxxxx:role/Redshift-S3'
FORMAT CSV;
```

When copying from text, if the chosen delimiter might also appear in a SUPER field,
use the ESCAPE option during COPY and UNLOAD. Consider the following example:

```
CREATE TABLE region_nations
(
 r_regionkey smallint
 ,r_name varchar
 ,r_comment varchar
 ,r_nations super
 );

COPY region_nations FROM 's3://redshift-downloads/semistructured/tpch-nested/data/text/region_nation'
REGION 'us-east-1' IAM_ROLE 'arn:aws:iam::xxxxxxxxxxxx:role/Redshift-S3'
DELIMITER ','
ESCAPE;
```

## Copying data from columnar-format

Parquet and ORC

If your semi-structured or nested data is already available in either Apache Parquet
or Apache ORC format, you can use the COPY command to ingest data into Amazon Redshift.

The Amazon Redshift table structure should match the number of columns and the column
data types of the Parquet or ORC files. By specifying SERIALIZETOJSON in the COPY
command, you can load any column type in the file that aligns with a SUPER column in
the table as SUPER. This includes structure and array types.

The following example uses a Parquet format:

```
COPY region_nations FROM 's3://redshift-downloads/semistructured/tpch-nested/data/parquet/region_nation'
REGION 'us-east-1' IAM_ROLE 'arn:aws:iam::xxxxxxxxxxxx:role/Redshift-S3'
FORMAT PARQUET SERIALIZETOJSON;
```

The following example uses an ORC format.

```
COPY region_nations FROM 's3://redshift-downloads/semistructured/tpch-nested/data/orc/region_nation'
IAM_ROLE 'arn:aws:iam::xxxxxxxxxxxx:role/Redshift-S3'
FORMAT ORC SERIALIZETOJSON;
```

When the attributes of the date or time data types are in ORC, Amazon Redshift converts them to varchar upon encoding them in SUPER.
