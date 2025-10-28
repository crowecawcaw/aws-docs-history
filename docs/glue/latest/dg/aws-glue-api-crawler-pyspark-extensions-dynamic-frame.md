# DynamicFrame class

One of the major abstractions in Apache Spark is the SparkSQL `DataFrame`, which
is similar to the `DataFrame` construct found in R and Pandas. A
`DataFrame` is similar to a table and supports functional-style
(map/reduce/filter/etc.) operations and SQL operations (select, project, aggregate).

`DataFrames` are powerful and widely used, but they have limitations with respect
to extract, transform, and load (ETL) operations. Most significantly, they require a schema to
be specified before any data is loaded. SparkSQL addresses this by making two passes over the
data—the first to infer the schema, and the second to load the data. However, this
inference is limited and doesn't address the realities of messy data. For example, the same
field might be of a different type in different records. Apache Spark often gives up and reports the
type as `string` using the original field text. This might not be correct, and you
might want finer control over how schema discrepancies are resolved. And for large datasets, an
additional pass over the source data might be prohibitively expensive.

To address these limitations, AWS Glue introduces the `DynamicFrame`. A
`DynamicFrame` is similar to a `DataFrame`, except that each record is
self-describing, so no schema is required initially. Instead, AWS Glue computes a schema on-the-fly
when required, and explicitly encodes schema inconsistencies using a choice (or union) type. You
can resolve these inconsistencies to make your datasets compatible with data stores that require
a fixed schema.

Similarly, a `DynamicRecord` represents a logical record within a `DynamicFrame`. It is
like a row in a Spark `DataFrame`, except that it is self-describing and can be used for data that does
not conform to a fixed schema. When using AWS Glue with PySpark, you do not typically manipulate independent
`DynamicRecords`. Rather, you will transform the dataset together through its `DynamicFrame`.

You can convert `DynamicFrames` to and from `DataFrames` after you
resolve any schema inconsistencies.

##  — construction —

- [\_\_init\_\_](#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-__init__ "#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-__init__")
- [fromDF](#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-fromDF "#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-fromDF")
- [toDF](#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-toDF "#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-toDF")

## \_\_init\_\_

###### `__init__(jdf, glue_ctx, name)`

- `jdf` – A reference to the data frame in the Java Virtual Machine (JVM).
- `glue_ctx` – A [GlueContext class](aws-glue-api-crawler-pyspark-extensions-glue-context.md "aws-glue-api-crawler-pyspark-extensions-glue-context.md") object.
- `name` – An optional name string, empty by default.

## fromDF

###### `fromDF(dataframe, glue_ctx, name)`

Converts a `DataFrame` to a `DynamicFrame` by converting `DataFrame`
fields to `DynamicRecord` fields. Returns the new `DynamicFrame`.

A `DynamicRecord` represents a logical record in a `DynamicFrame`.
It is similar to a row in a Spark `DataFrame`, except that it
is self-describing and can be used for data that does not conform to a fixed schema.

This function expects columns with duplicated names in your `DataFrame`
to have already been resolved.

- `dataframe` – The Apache Spark SQL `DataFrame` to convert
  (required).
- `glue_ctx` – The [GlueContext class](aws-glue-api-crawler-pyspark-extensions-glue-context.md "aws-glue-api-crawler-pyspark-extensions-glue-context.md") object that
  specifies the context for this transform (required).
- `name` – The name of the resulting `DynamicFrame`
  (optional since AWS Glue 3.0).

## toDF

###### `toDF(options)`

Converts a `DynamicFrame` to an Apache Spark `DataFrame` by
converting `DynamicRecords` into `DataFrame` fields. Returns the
new `DataFrame`.

A `DynamicRecord` represents a logical record in a `DynamicFrame`.
It is similar to a row in a Spark `DataFrame`, except that it
is self-describing and can be used for data that does not conform to a fixed schema.

- `options` – A list of `ResolveOption` objects that specify how to resolve choice types during the conversion.
  This parameter is used to handle schema inconsistencies, not for format options like CSV parsing.

For CSV parsing and other format options, specify these in the `from_options` method when creating the DynamicFrame,
not in the `toDF` method.

Here's an example of the correct way to handle CSV format options:

```
from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame
from pyspark.context import SparkContext

sc = SparkContext()
glueContext = GlueContext(sc)

# Correct: Specify format options in from_options
csv_dyf = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": ["s3://my-bucket/path/to/csv/"]},
    format="csv",
    format_options={
        "withHeader": True,
        "separator": ",",
        "inferSchema": True
    }
)

# Convert to DataFrame (no format options needed here)
csv_df = csv_dyf.toDF()
```

The `options` parameter in `toDF` is specifically for resolving choice types.
Specify the target type if you choose the `Project` and `Cast` action type. Examples include the
following.

```
>>>toDF([ResolveOption("a.b.c", "KeepAsStruct")])
>>>toDF([ResolveOption("a.b.c", "Project", DoubleType())])

```

##  — information —

- [count](#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-count "#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-count")
- [schema](#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-schema "#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-schema")
- [printSchema](#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-printSchema "#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-printSchema")
- [show](#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-show "#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-show")
- [repartition](#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-repartition "#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-repartition")
- [coalesce](#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-coalesce "#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-coalesce")

## count

`count( )` – Returns the number of rows in the underlying
`DataFrame`.

## schema

`schema( )` – Returns the schema of this `DynamicFrame`, or if
that is not available, the schema of the underlying `DataFrame`.

For more information about the `DynamicFrame` types that make up this schema, see [PySpark extension types](aws-glue-api-crawler-pyspark-extensions-types.md "aws-glue-api-crawler-pyspark-extensions-types.md").

## printSchema

`printSchema( )` – Prints the schema of the underlying
`DataFrame`.

## show

`show(num_rows)` – Prints a specified number of rows from the underlying
`DataFrame`.

## repartition

`repartition(numPartitions)` – Returns a new `DynamicFrame`
with `numPartitions` partitions.

## coalesce

`coalesce(numPartitions)` – Returns a new `DynamicFrame` with
`numPartitions` partitions.

##  — transforms —

- [apply_mapping](#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-apply_mapping "#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-apply_mapping")
- [drop_fields](#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-drop_fields "#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-drop_fields")
- [filter](#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-filter "#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-filter")
- [join](#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-join "#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-join")
- [map](#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-map "#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-map")
- [mergeDynamicFrame](#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-merge "#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-merge")
- [relationalize](#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-relationalize "#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-relationalize")
- [rename_field](#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-rename_field "#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-rename_field")
- [resolveChoice](#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-resolveChoice "#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-resolveChoice")
- [select_fields](#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-select_fields "#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-select_fields")
- [spigot](#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-spigot "#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-spigot")
- [split_fields](#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-split_fields "#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-split_fields")
- [split_rows](#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-split_rows "#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-split_rows")
- [unbox](#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-unbox "#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-unbox")
- [union](#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-union "#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-union")
- [unnest](#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-unnest "#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-unnest")
- [unnest_ddb_json](#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-unnest_ddb_json "#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-unnest_ddb_json")
- [write](#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-write "#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-write")

## apply_mapping

###### `apply_mapping(mappings, transformation_ctx="", info="", stageThreshold=0,

totalThreshold=0)`

Applies a declarative mapping to a `DynamicFrame` and returns a new
`DynamicFrame` with those mappings applied to the fields that you specify.
Unspecified fields are omitted from the new `DynamicFrame`.

- `mappings` – A list of mapping tuples (required). Each consists of:
  (source column, source type, target column, target type).

If the source column has a dot "`.`" in the name, you must place
backticks "````" around it. For example, to map `this.old.name` (string) to`thisNewName`, you would use the following tuple:

```
("`this.old.name`", "string", "thisNewName", "string")
```

- `transformation_ctx` – A unique string that is used to identify state
  information (optional).
- `info` – A string to be associated with error reporting for this
  transformation (optional).
- `stageThreshold` – The number of errors encountered during this
  transformation at which the process should error out (optional). The default is zero,
  which indicates that the process should not error out.
- `totalThreshold` – The number of errors encountered up to and
  including this transformation at which the process should error out (optional). The
  default is zero, which indicates that the process should not error out.

### Example: Use apply_mapping to rename fields and change field types

The following code example shows how to use the `apply_mapping` method to rename selected fields and change field types.

###### Note

To access the dataset that is used in this example, see [Code example: Joining
and relationalizing data](aws-glue-programming-python-samples-legislators.md "aws-glue-programming-python-samples-legislators.md") and follow the instructions in [Step 1:
Crawl the data in the Amazon S3 bucket](aws-glue-programming-python-samples-legislators.md#aws-glue-programming-python-samples-legislators-crawling "aws-glue-programming-python-samples-legislators.md#aws-glue-programming-python-samples-legislators-crawling").

```
# Example: Use apply_mapping to reshape source data into
# the desired column names and types as a new DynamicFrame

from pyspark.context import SparkContext
from awsglue.context import GlueContext

# Create GlueContext
sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)

# Create a DynamicFrame and view its schema
persons = glueContext.create_dynamic_frame.from_catalog(
    database="legislators", table_name="persons_json"
)
print("Schema for the persons DynamicFrame:")
persons.printSchema()

# Select and rename fields, change field type
print("Schema for the persons_mapped DynamicFrame, created with apply_mapping:")
persons_mapped = persons.apply_mapping(
    [
        ("family_name", "String", "last_name", "String"),
        ("name", "String", "first_name", "String"),
        ("birth_date", "String", "date_of_birth", "Date"),
    ]
)
persons_mapped.printSchema()


```

````
Schema for the persons DynamicFrame:
root
|-- family_name: string
|-- name: string
|-- links: array
|    |-- element: struct
|    |    |-- note: string
|    |    |-- url: string
|-- gender: string |-- image: string |-- identifiers: array
|    |-- element: struct
|    |    |-- scheme: string
|    |    |-- identifier: string
|-- other_names: array |    |-- element: struct
|    |    |-- lang: string
|    |    |-- note: string
|    |    |-- name: string
|-- sort_name: string |-- images: array |    |-- element: struct
|    |    |-- url: string
|-- given_name: string |-- birth_date: string |-- id: string
|-- contact_details: array |    |-- element: struct
|    |    |-- type: string
|    |    |-- value: string
|-- death_date: string Schema for the persons_mapped DynamicFrame, created with apply_mapping: root |-- last_name: string |-- first_name: string
|-- date_of_birth: date ``` ## drop\_fields ###### `drop_fields(paths, transformation_ctx="", info="", stageThreshold=0, totalThreshold=0)` Calls the [FlatMap class](aws-glue-api-crawler-pyspark-transforms-flat-map.md "aws-glue-api-crawler-pyspark-transforms-flat-map.md") transform to remove fields from a `DynamicFrame`. Returns a new `DynamicFrame` with the specified fields dropped. <br>• `paths` – A list of strings. Each contains the full path to a field node that you want to drop. You can use dot notation to specify nested fields. For example, if field `first` is a child of field `name` in the tree, you specify `"name.first"` for the path. If a field node has a literal `.` in the name, you must enclose the name in backticks (```). <br>• `transformation_ctx` – A unique string that is used to identify state information (optional). <br>• `info` – A string to be associated with error reporting for this transformation (optional). <br>• `stageThreshold` – The number of errors encountered during this transformation at which the process should error out (optional). The default is zero, which indicates that the process should not error out. <br>• `totalThreshold` – The number of errors encountered up to and including this transformation at which the process should error out (optional). The default is zero, which indicates that the process should not error out. ### Example: Use drop\_fields to remove fields from a `DynamicFrame` This code example uses the `drop_fields` method to remove selected top-level and nested fields from a `DynamicFrame`. **Example dataset** The example uses the following dataset that is represented by the `EXAMPLE-FRIENDS-DATA` table in the code: ``` {"name": "Sally", "age": 23, "location": {"state": "WY", "county": "Fremont"}, "friends": []} {"name": "Varun", "age": 34, "location": {"state": "NE", "county": "Douglas"}, "friends": [{"name": "Arjun", "age": 3}]} {"name": "George", "age": 52, "location": {"state": "NY"}, "friends": [{"name": "Fred"}, {"name": "Amy", "age": 15}]} {"name": "Haruki", "age": 21, "location": {"state": "AK", "county": "Denali"}} {"name": "Sheila", "age": 63, "friends": [{"name": "Nancy", "age": 22}]} ``` **Example code** ``` # Example: Use drop_fields to remove top-level and nested fields from a DynamicFrame. # Replace MY-EXAMPLE-DATABASE with your Glue Data Catalog database name. # Replace EXAMPLE-FRIENDS-DATA with your table name. from pyspark.context import SparkContext from awsglue.context import GlueContext # Create GlueContext sc = SparkContext.getOrCreate() glueContext = GlueContext(sc) # Create a DynamicFrame from Glue Data Catalog glue_source_database = "`MY-EXAMPLE-DATABASE`" glue_source_table = "`EXAMPLE-FRIENDS-DATA`" friends = glueContext.create_dynamic_frame.from_catalog( database=glue_source_database, table_name=glue_source_table ) print("Schema for friends DynamicFrame before calling drop_fields:") friends.printSchema() # Remove location.county, remove friends.age, remove age friends = friends.drop_fields(paths=["age", "location.county", "friends.age"]) print("Schema for friends DynamicFrame after removing age, county, and friend age:") friends.printSchema() ``` ``` Schema for friends DynamicFrame before calling drop_fields: root |-- name: string |-- age: int
|-- location: struct |    |-- state: string
|    |-- county: string |-- friends: array
|    |-- element: struct
|    |    |-- name: string
|    |    |-- age: int Schema for friends DynamicFrame after removing age, county, and friend age: root
|-- name: string |-- location: struct |    |-- state: string
|-- friends: array |    |-- element: struct
|    |    |-- name: string ``` ## filter ###### `filter(f, transformation_ctx="", info="", stageThreshold=0, totalThreshold=0)` Returns a new `DynamicFrame` that contains all `DynamicRecords` within the input `DynamicFrame` that satisfy the specified predicate function `f`. <br>• `f` – The predicate function to apply to the `DynamicFrame`. The function must take a `DynamicRecord` as an argument and return True if the `DynamicRecord` meets the filter requirements, or False if not (required). A `DynamicRecord` represents a logical record in a `DynamicFrame`. It's similar to a row in a Spark `DataFrame`, except that it is self-describing and can be used for data that doesn't conform to a fixed schema. <br>• `transformation_ctx` – A unique string that is used to identify state information (optional). <br>• `info` – A string to be associated with error reporting for this transformation (optional). <br>• `stageThreshold` – The number of errors encountered during this transformation at which the process should error out (optional). The default is zero, which indicates that the process should not error out. <br>• `totalThreshold` – The number of errors encountered up to and including this transformation at which the process should error out (optional). The default is zero, which indicates that the process should not error out. ### Example: Use filter to get a filtered selection of fields This example uses the `filter` method to create a new `DynamicFrame` that includes a filtered selection of another `DynamicFrame`'s fields. Like the `map` method, `filter` takes a function as an argument that gets applied to each record in the original `DynamicFrame`. The function takes a record as an input and returns a Boolean value. If the return value is true, the record gets included in the resulting `DynamicFrame`. If it's false, the record is left out. ###### Note To access the dataset that is used in this example, see [Code example: Data preparation using ResolveChoice, Lambda, and ApplyMapping](aws-glue-programming-python-samples-medicaid.md "aws-glue-programming-python-samples-medicaid.md") and follow the instructions in [Step 1: Crawl the data in the Amazon S3 bucket](aws-glue-programming-python-samples-medicaid.md#aws-glue-programming-python-samples-medicaid-crawling "aws-glue-programming-python-samples-medicaid.md#aws-glue-programming-python-samples-medicaid-crawling"). ``` # Example: Use filter to create a new DynamicFrame # with a filtered selection of records from pyspark.context import SparkContext from awsglue.context import GlueContext # Create GlueContext sc = SparkContext.getOrCreate() glueContext = GlueContext(sc) # Create DynamicFrame from Glue Data Catalog medicare = glueContext.create_dynamic_frame.from_options( "s3", { "paths": [ "s3://awsglue-datasets/examples/medicare/Medicare_Hospital_Provider.csv" ] }, "csv", {"withHeader": True}, ) # Create filtered DynamicFrame with custom lambda # to filter records by Provider State and Provider City sac_or_mon = medicare.filter( f=lambda x: x["Provider State"] in ["CA", "AL"] and x["Provider City"] in ["SACRAMENTO", "MONTGOMERY"] ) # Compare record counts print("Unfiltered record count: ", medicare.count()) print("Filtered record count:  ", sac_or_mon.count()) ``` ``` Unfiltered record count:  163065 Filtered record count:   564 ``` ## join ###### `join(paths1, paths2, frame2, transformation_ctx="", info="", stageThreshold=0, totalThreshold=0)` Performs an equality join with another `DynamicFrame` and returns the resulting `DynamicFrame`. <br>• `paths1` – A list of the keys in this frame to join. <br>• `paths2` – A list of the keys in the other frame to join. <br>• `frame2` – The other `DynamicFrame` to join. <br>• `transformation_ctx` – A unique string that is used to identify state information (optional). <br>• `info` – A string to be associated with error reporting for this transformation (optional). <br>• `stageThreshold` – The number of errors encountered during this transformation at which the process should error out (optional). The default is zero, which indicates that the process should not error out. <br>• `totalThreshold` – The number of errors encountered up to and including this transformation at which the process should error out (optional). The default is zero, which indicates that the process should not error out. ### Example: Use join to combine `DynamicFrames` This example uses the `join` method to perform a join on three `DynamicFrames`. AWS Glue performs the join based on the field keys that you provide. The resulting `DynamicFrame` contains rows from the two original frames where the specified keys match. Note that the `join` transform keeps all fields intact. This means that the fields that you specify to match appear in the resulting DynamicFrame, even if they're redundant and contain the same keys. In this example, we use `drop_fields` to remove these redundant keys after the join. ###### Note To access the dataset that is used in this example, see [Code example: Joining and relationalizing data](aws-glue-programming-python-samples-legislators.md "aws-glue-programming-python-samples-legislators.md") and follow the instructions in [Step 1: Crawl the data in the Amazon S3 bucket](aws-glue-programming-python-samples-legislators.md#aws-glue-programming-python-samples-legislators-crawling "aws-glue-programming-python-samples-legislators.md#aws-glue-programming-python-samples-legislators-crawling"). ``` # Example: Use join to combine data from three DynamicFrames from pyspark.context import SparkContext from awsglue.context import GlueContext # Create GlueContext sc = SparkContext.getOrCreate() glueContext = GlueContext(sc) # Load DynamicFrames from Glue Data Catalog persons = glueContext.create_dynamic_frame.from_catalog( database="legislators", table_name="persons_json" ) memberships = glueContext.create_dynamic_frame.from_catalog( database="legislators", table_name="memberships_json" ) orgs = glueContext.create_dynamic_frame.from_catalog( database="legislators", table_name="organizations_json" ) print("Schema for the persons DynamicFrame:") persons.printSchema() print("Schema for the memberships DynamicFrame:") memberships.printSchema() print("Schema for the orgs DynamicFrame:") orgs.printSchema() # Join persons and memberships by ID persons_memberships = persons.join( paths1=["id"], paths2=["person_id"], frame2=memberships ) # Rename and drop fields from orgs # to prevent field name collisions with persons_memberships orgs = ( orgs.drop_fields(["other_names", "identifiers"]) .rename_field("id", "org_id") .rename_field("name", "org_name") ) # Create final join of all three DynamicFrames legislators_combined = orgs.join( paths1=["org_id"], paths2=["organization_id"], frame2=persons_memberships ).drop_fields(["person_id", "org_id"]) # Inspect the schema for the joined data print("Schema for the new legislators_combined DynamicFrame:") legislators_combined.printSchema() ``` ``` Schema for the persons DynamicFrame: root
|-- family_name: string |-- name: string |-- links: array
|    |-- element: struct
|    |    |-- note: string
|    |    |-- url: string
|-- gender: string |-- image: string |-- identifiers: array
|    |-- element: struct
|    |    |-- scheme: string
|    |    |-- identifier: string
|-- other_names: array |    |-- element: struct
|    |    |-- lang: string
|    |    |-- note: string
|    |    |-- name: string
|-- sort_name: string |-- images: array |    |-- element: struct
|    |    |-- url: string
|-- given_name: string |-- birth_date: string |-- id: string
|-- contact_details: array |    |-- element: struct
|    |    |-- type: string
|    |    |-- value: string
|-- death_date: string Schema for the memberships DynamicFrame: root |-- area_id: string |-- on_behalf_of_id: string
|-- organization_id: string |-- role: string |-- person_id: string
|-- legislative_period_id: string |-- start_date: string |-- end_date: string Schema for the orgs DynamicFrame: root
|-- identifiers: array |    |-- element: struct
|    |    |-- scheme: string
|    |    |-- identifier: string
|-- other_names: array |    |-- element: struct
|    |    |-- lang: string
|    |    |-- note: string
|    |    |-- name: string
|-- id: string |-- classification: string |-- name: string
|-- links: array |    |-- element: struct
|    |    |-- note: string
|    |    |-- url: string
|-- image: string |-- seats: int |-- type: string Schema for the new legislators_combined DynamicFrame: root
|-- role: string |-- seats: int |-- org_name: string
|-- links: array |    |-- element: struct
|    |    |-- note: string
|    |    |-- url: string
|-- type: string |-- sort_name: string |-- area_id: string
|-- images: array |    |-- element: struct
|    |    |-- url: string
|-- on_behalf_of_id: string |-- other_names: array |    |-- element: struct
|    |    |-- note: string
|    |    |-- name: string
|    |    |-- lang: string
|-- contact_details: array |    |-- element: struct
|    |    |-- type: string
|    |    |-- value: string
|-- name: string |-- birth_date: string |-- organization_id: string
|-- gender: string |-- classification: string |-- legislative_period_id: string
|-- identifiers: array |    |-- element: struct
|    |    |-- scheme: string
|    |    |-- identifier: string
|-- image: string |-- given_name: string |-- start_date: string
|-- family_name: string |-- id: string |-- death_date: string
|-- end_date: string ``` ## map ###### `map(f, transformation_ctx="", info="", stageThreshold=0, totalThreshold=0)` Returns a new `DynamicFrame` that results from applying the specified mapping function to all records in the original `DynamicFrame`. <br>• `f` – The mapping function to apply to all records in the `DynamicFrame`. The function must take a `DynamicRecord` as an argument and return a new `DynamicRecord` (required). A `DynamicRecord` represents a logical record in a `DynamicFrame`. It's similar to a row in an Apache Spark `DataFrame`, except that it is self-describing and can be used for data that doesn't conform to a fixed schema. <br>• `transformation_ctx` – A unique string that is used to identify state information (optional). <br>• `info` – A string that is associated with errors in the transformation (optional). <br>• `stageThreshold` – The maximum number of errors that can occur in the transformation before it errors out (optional). The default is zero. <br>• `totalThreshold` – The maximum number of errors that can occur overall before processing errors out (optional). The default is zero. ### Example: Use map to apply a function to every record in a `DynamicFrame` This example shows how to use the `map` method to apply a function to every record of a `DynamicFrame`. Specifically, this example applies a function called `MergeAddress` to each record in order to merge several address fields into a single `struct` type. ###### Note To access the dataset that is used in this example, see [Code example: Data preparation using ResolveChoice, Lambda, and ApplyMapping](aws-glue-programming-python-samples-medicaid.md "aws-glue-programming-python-samples-medicaid.md") and follow the instructions in [Step 1: Crawl the data in the Amazon S3 bucket](aws-glue-programming-python-samples-medicaid.md#aws-glue-programming-python-samples-medicaid-crawling "aws-glue-programming-python-samples-medicaid.md#aws-glue-programming-python-samples-medicaid-crawling"). ``` # Example: Use map to combine fields in all records # of a DynamicFrame from pyspark.context import SparkContext from awsglue.context import GlueContext # Create GlueContext sc = SparkContext.getOrCreate() glueContext = GlueContext(sc) # Create a DynamicFrame and view its schema medicare = glueContext.create_dynamic_frame.from_options( "s3", {"paths": ["s3://awsglue-datasets/examples/medicare/Medicare_Hospital_Provider.csv"]}, "csv", {"withHeader": True}) print("Schema for medicare DynamicFrame:") medicare.printSchema() # Define a function to supply to the map transform # that merges address fields into a single field def MergeAddress(rec): rec["Address"] = {} rec["Address"]["Street"] = rec["Provider Street Address"] rec["Address"]["City"] = rec["Provider City"] rec["Address"]["State"] = rec["Provider State"] rec["Address"]["Zip.Code"] = rec["Provider Zip Code"] rec["Address"]["Array"] = [rec["Provider Street Address"], rec["Provider City"], rec["Provider State"], rec["Provider Zip Code"]] del rec["Provider Street Address"] del rec["Provider City"] del rec["Provider State"] del rec["Provider Zip Code"] return rec # Use map to apply MergeAddress to every record mapped_medicare = medicare.map(f = MergeAddress) print("Schema for mapped_medicare DynamicFrame:") mapped_medicare.printSchema() ``` ``` Schema for medicare DynamicFrame: root |-- DRG Definition: string |-- Provider Id: string
|-- Provider Name: string |-- Provider Street Address: string |-- Provider City: string
|-- Provider State: string |-- Provider Zip Code: string |-- Hospital Referral Region Description: string
|-- Total Discharges: string |-- Average Covered Charges: string |-- Average Total Payments: string
|-- Average Medicare Payments: string Schema for mapped_medicare DynamicFrame: root |-- Average Total Payments: string |-- Average Covered Charges: string
|-- DRG Definition: string |-- Average Medicare Payments: string |-- Hospital Referral Region Description: string
|-- Address: struct |    |-- Zip.Code: string
|    |-- City: string |    |-- Array: array
|    |    |-- element: string
|    |-- State: string |    |-- Street: string
|-- Provider Id: string |-- Total Discharges: string |-- Provider Name: string ``` ## mergeDynamicFrame ###### `mergeDynamicFrame(stage_dynamic_frame, primary_keys, transformation_ctx = "", options = {}, info = "", stageThreshold = 0, totalThreshold = 0)` Merges this `DynamicFrame` with a staging `DynamicFrame` based on the specified primary keys to identify records. Duplicate records (records with the same primary keys) are not deduplicated. If there is no matching record in the staging frame, all records (including duplicates) are retained from the source. If the staging frame has matching records, the records from the staging frame overwrite the records in the source in AWS Glue. <br>• `stage_dynamic_frame` – The staging `DynamicFrame` to merge. <br>• `primary_keys` – The list of primary key fields to match records from the source and staging dynamic frames. <br>• `transformation_ctx` – A unique string that is used to retrieve metadata about the current transformation (optional). <br>• `options` – A string of JSON name-value pairs that provide additional information for this transformation. This argument is not currently used. <br>• `info` – A `String`. Any string to be associated with errors in this transformation. <br>• `stageThreshold` – A `Long`. The number of errors in the given transformation for which the processing needs to error out. <br>• `totalThreshold` – A `Long`. The total number of errors up to and including this transformation for which the processing needs to error out. This method returns a new `DynamicFrame` that is obtained by merging this `DynamicFrame` with the staging `DynamicFrame`. The returned `DynamicFrame` contains record A in these cases: <br>• If `A` exists in both the source frame and the staging frame, then `A` in the staging frame is returned. <br>• If `A` is in the source table and `A.primaryKeys` is not in the `stagingDynamicFrame`, `A` is not updated in the staging table. The source frame and staging frame don't need to have the same schema. ### Example: Use mergeDynamicFrame to merge two `DynamicFrames` based on a primary key The following code example shows how to use the `mergeDynamicFrame` method to merge a `DynamicFrame` with a "staging" `DynamicFrame`, based on the primary key `id`. **Example dataset** The example uses two `DynamicFrames` from a `DynamicFrameCollection` called `split_rows_collection`. The following is the list of keys in `split_rows_collection`. ``` dict_keys(['high', 'low']) ``` **Example code** ``` # Example: Use mergeDynamicFrame to merge DynamicFrames # based on a set of specified primary keys from pyspark.context import SparkContext from awsglue.context import GlueContext from awsglue.transforms import SelectFromCollection # Inspect the original DynamicFrames frame_low = SelectFromCollection.apply(dfc=split_rows_collection, key="low") print("Inspect the DynamicFrame that contains rows where ID < 10") frame_low.toDF().show() frame_high = SelectFromCollection.apply(dfc=split_rows_collection, key="high") print("Inspect the DynamicFrame that contains rows where ID > 10") frame_high.toDF().show() # Merge the DynamicFrames based on the "id" primary key merged_high_low = frame_high.mergeDynamicFrame( stage_dynamic_frame=frame_low, primary_keys=["id"] ) # View the results where the ID is 1 or 20 print("Inspect the merged DynamicFrame that contains the combined rows") merged_high_low.toDF().where("id = 1 or id= 20").orderBy("id").show() ``` ``` Inspect the DynamicFrame that contains rows where ID < 10 +---+-----+------------------------+-------------------------+
| id|index|contact_details.val.type|contact_details.val.value| +---+-----+------------------------+-------------------------+
|  1|    0|                     fax|             202-225-3307|
|  1|    1|                   phone|             202-225-5731|
|  2|    0|                     fax|             202-225-3307|
|  2|    1|                   phone|             202-225-5731|
|  3|    0|                     fax|             202-225-3307|
|  3|    1|                   phone|             202-225-5731|
|  4|    0|                     fax|             202-225-3307|
|  4|    1|                   phone|             202-225-5731|
|  5|    0|                     fax|             202-225-3307|
|  5|    1|                   phone|             202-225-5731|
|  6|    0|                     fax|             202-225-3307|
|  6|    1|                   phone|             202-225-5731|
|  7|    0|                     fax|             202-225-3307|
|  7|    1|                   phone|             202-225-5731|
|  8|    0|                     fax|             202-225-3307|
|  8|    1|                   phone|             202-225-5731|
|  9|    0|                     fax|             202-225-3307|
|  9|    1|                   phone|             202-225-5731|
| 10|    0|                     fax|             202-225-6328|
| 10|    1|                   phone|             202-225-4576| +---+-----+------------------------+-------------------------+ only showing top 20 rows Inspect the DynamicFrame that contains rows where ID > 10 +---+-----+------------------------+-------------------------+
| id|index|contact_details.val.type|contact_details.val.value| +---+-----+------------------------+-------------------------+
| 11|    0|                     fax|             202-225-6328|
| 11|    1|                   phone|             202-225-4576|
| 11|    2|                 twitter|           RepTrentFranks|
| 12|    0|                     fax|             202-225-6328|
| 12|    1|                   phone|             202-225-4576|
| 12|    2|                 twitter|           RepTrentFranks|
| 13|    0|                     fax|             202-225-6328|
| 13|    1|                   phone|             202-225-4576|
| 13|    2|                 twitter|           RepTrentFranks|
| 14|    0|                     fax|             202-225-6328|
| 14|    1|                   phone|             202-225-4576|
| 14|    2|                 twitter|           RepTrentFranks|
| 15|    0|                     fax|             202-225-6328|
| 15|    1|                   phone|             202-225-4576|
| 15|    2|                 twitter|           RepTrentFranks|
| 16|    0|                     fax|             202-225-6328|
| 16|    1|                   phone|             202-225-4576|
| 16|    2|                 twitter|           RepTrentFranks|
| 17|    0|                     fax|             202-225-6328|
| 17|    1|                   phone|             202-225-4576| +---+-----+------------------------+-------------------------+ only showing top 20 rows Inspect the merged DynamicFrame that contains the combined rows +---+-----+------------------------+-------------------------+
| id|index|contact_details.val.type|contact_details.val.value| +---+-----+------------------------+-------------------------+
|  1|    0|                     fax|             202-225-3307|
|  1|    1|                   phone|             202-225-5731|
| 20|    0|                     fax|             202-225-5604|
| 20|    1|                   phone|             202-225-6536|
| 20|    2|                 twitter|                USRepLong| +---+-----+------------------------+-------------------------+ ``` ## relationalize ###### `relationalize(root_table_name, staging_path, options, transformation_ctx="", info="", stageThreshold=0, totalThreshold=0)` Converts a `DynamicFrame` into a form that fits within a relational database. Relationalizing a `DynamicFrame` is especially useful when you want to move data from a NoSQL environment like DynamoDB into a relational database like MySQL. The transform generates a list of frames by unnesting nested columns and pivoting array columns. You can join the pivoted array columns to the root table by using the join key that is generated during the unnest phase. <br>• `root_table_name` – The name for the root table. <br>• `staging_path` – The path where the method can store partitions of pivoted tables in CSV format (optional). Pivoted tables are read back from this path. <br>• `options` – A dictionary of optional parameters. <br>• `transformation_ctx` – A unique string that is used to identify state information (optional). <br>• `info` – A string to be associated with error reporting for this transformation (optional). <br>• `stageThreshold` – The number of errors encountered during this transformation at which the process should error out (optional). The default is zero, which indicates that the process should not error out. <br>• `totalThreshold` – The number of errors encountered up to and including this transformation at which the process should error out (optional). The default is zero, which indicates that the process should not error out. ### Example: Use relationalize to flatten a nested schema in a `DynamicFrame` This code example uses the `relationalize` method to flatten a nested schema into a form that fits into a relational database. **Example dataset** The example uses a `DynamicFrame` called `legislators_combined` with the following schema. `legislators_combined` has multiple nested fields such as `links`, `images`, and `contact_details`, which will be flattened by the `relationalize` transform. ``` root
|-- role: string |-- seats: int |-- org_name: string |-- links: array |    |-- element: struct
|    |    |-- note: string |    |    |-- url: string
|-- type: string |-- sort_name: string |-- area_id: string |-- images: array |    |-- element: struct
|    |    |-- url: string |-- on_behalf_of_id: string |-- other_names: array
|    |-- element: struct |    |    |-- note: string
|    |    |-- name: string |    |    |-- lang: string
|-- contact_details: array |    |-- element: struct |    |    |-- type: string
|    |    |-- value: string |-- name: string |-- birth_date: string
|-- organization_id: string |-- gender: string |-- classification: string |-- legislative_period_id: string |-- identifiers: array
|    |-- element: struct |    |    |-- scheme: string
|    |    |-- identifier: string |-- image: string |-- given_name: string
|-- start_date: string |-- family_name: string |-- id: string |-- death_date: string |-- end_date: string ``` **Example code** ``` # Example: Use relationalize to flatten # a nested schema into a format that fits # into a relational database. # Replace DOC-EXAMPLE-S3-BUCKET/tmpDir with your own location. from pyspark.context import SparkContext from awsglue.context import GlueContext # Create GlueContext sc = SparkContext.getOrCreate() glueContext = GlueContext(sc) # Apply relationalize and inspect new tables legislators_relationalized = legislators_combined.relationalize( "l_root", "`s3://DOC-EXAMPLE-BUCKET/tmpDir`" ) legislators_relationalized.keys() # Compare the schema of the contact_details # nested field to the new relationalized table that # represents it legislators_combined.select_fields("contact_details").printSchema() legislators_relationalized.select("l_root_contact_details").toDF().where( "id = 10 or id = 75" ).orderBy(["id", "index"]).show() ``` The following output lets you compare the schema of the nested field called `contact_details` to the table that the `relationalize` transform created. Notice that the table records link back to the main table using a foreign key called `id` and an `index` column that represents the positions of the array. ``` dict_keys(['l_root', 'l_root_images', 'l_root_links', 'l_root_other_names', 'l_root_contact_details', 'l_root_identifiers']) root
|-- contact_details: array |    |-- element: struct |    |    |-- type: string
|    |    |-- value: string +---+-----+------------------------+-------------------------+
| id|index|contact_details.val.type|contact_details.val.value| +---+-----+------------------------+-------------------------+
| 10|    0|                     fax|             202-225-4160|
| 10|    1|                   phone|             202-225-3436|
| 75|    0|                     fax|             202-225-6791|
| 75|    1|                   phone|             202-225-2861|
| 75|    2|                 twitter|               RepSamFarr| +---+-----+------------------------+-------------------------+ ``` ## rename\_field ###### `rename_field(oldName, newName, transformation_ctx="", info="", stageThreshold=0, totalThreshold=0)` Renames a field in this `DynamicFrame` and returns a new `DynamicFrame` with the field renamed. <br>• `oldName` – The full path to the node you want to rename. If the old name has dots in it, `RenameField` doesn't work unless you place backticks around it (```). For example, to replace `this.old.name` with `thisNewName`, you would call rename\_field as follows. ``` newDyF = oldDyF.rename_field("`this.old.name`", "thisNewName") ``` <br>• `newName` – The new name, as a full path. <br>• `transformation_ctx` – A unique string that is used to identify state information (optional). <br>• `info` – A string to be associated with error reporting for this transformation (optional). <br>• `stageThreshold` – The number of errors encountered during this transformation at which the process should error out (optional). The default is zero, which indicates that the process should not error out. <br>• `totalThreshold` – The number of errors encountered up to and including this transformation at which the process should error out (optional). The default is zero, which indicates that the process should not error out. ### Example: Use rename\_field to rename fields in a `DynamicFrame` This code example uses the `rename_field` method to rename fields in a `DynamicFrame`. Notice that the example uses method chaining to rename multiple fields at the same time. ###### Note To access the dataset that is used in this example, see [Code example: Joining and relationalizing data](aws-glue-programming-python-samples-legislators.md "aws-glue-programming-python-samples-legislators.md") and follow the instructions in [Step 1: Crawl the data in the Amazon S3 bucket](aws-glue-programming-python-samples-legislators.md#aws-glue-programming-python-samples-legislators-crawling "aws-glue-programming-python-samples-legislators.md#aws-glue-programming-python-samples-legislators-crawling"). **Example code** ``` # Example: Use rename_field to rename fields # in a DynamicFrame from pyspark.context import SparkContext from awsglue.context import GlueContext # Create GlueContext sc = SparkContext.getOrCreate() glueContext = GlueContext(sc) # Inspect the original orgs schema orgs = glueContext.create_dynamic_frame.from_catalog( database="legislators", table_name="organizations_json" ) print("Original orgs schema: ") orgs.printSchema() # Rename fields and view the new schema orgs = orgs.rename_field("id", "org_id").rename_field("name", "org_name") print("New orgs schema with renamed fields: ") orgs.printSchema() ``` ``` Original orgs schema: root
|-- identifiers: array |    |-- element: struct |    |    |-- scheme: string
|    |    |-- identifier: string |-- other_names: array |    |-- element: struct
|    |    |-- lang: string |    |    |-- note: string
|    |    |-- name: string |-- id: string |-- classification: string
|-- name: string |-- links: array |    |-- element: struct |    |    |-- note: string
|    |    |-- url: string |-- image: string |-- seats: int
|-- type: string New orgs schema with renamed fields: root |-- identifiers: array |    |-- element: struct |    |    |-- scheme: string
|    |    |-- identifier: string |-- other_names: array |    |-- element: struct
|    |    |-- lang: string |    |    |-- note: string
|    |    |-- name: string |-- classification: string |-- org_id: string
|-- org_name: string |-- links: array |    |-- element: struct |    |    |-- note: string
|    |    |-- url: string |-- image: string |-- seats: int
|-- type: string ``` ## resolveChoice ###### `resolveChoice(specs = None, choice = "" , database = None , table_name = None , transformation_ctx="", info="", stageThreshold=0, totalThreshold=0, catalog_id = None)` Resolves a choice type within this `DynamicFrame` and returns the new `DynamicFrame`. <br>• `specs` – A list of specific ambiguities to resolve, each in the form of a tuple: `(field_path, action)`. There are two ways to use `resolveChoice`. The first is to use the `specs` argument to specify a sequence of specific fields and how to resolve them. The other mode for `resolveChoice` is to use the `choice` argument to specify a single resolution for all `ChoiceTypes`. Values for `specs` are specified as tuples made up of `(field_path, action)` pairs. The `field_path` value identifies a specific ambiguous element, and the `action` value identifies the corresponding resolution. The following are the possible actions: + `cast:`type`` – Attempts to cast all values to the specified type. For example: `cast:int`. + `make_cols` – Converts each distinct type to a column with the name ``columnName`_`type``. It resolves a potential ambiguity by flattening the data. For example, if `columnA` could be an `int` or a `string`, the resolution would be to produce two columns named `columnA_int` and `columnA_string` in the resulting `DynamicFrame`. + `make_struct` – Resolves a potential ambiguity by using a `struct` to represent the data. For example, if data in a column could be an `int` or a `string`, the `make_struct` action produces a column of structures in the resulting `DynamicFrame`. Each structure contains both an `int` and a `string`. + `project:`type`` – Resolves a potential ambiguity by projecting all the data to one of the possible data types. For example, if data in a column could be an `int` or a `string`, using a `project:string` action produces a column in the resulting `DynamicFrame` where all the `int` values have been converted to strings. If the `field_path` identifies an array, place empty square brackets after the name of the array to avoid ambiguity. For example, suppose you are working with data structured as follows: ``` "myList": [ { "price": 100.00 }, { "price": "$100.00" } ] ``` You can select the numeric rather than the string version of the price by setting the `field_path` to `"myList[].price"`, and setting the `action` to `"cast:double"`. ###### Note You can only use one of the `specs` and `choice` parameters. If the `specs` parameter is not `None`, then the `choice` parameter must be an empty string. Conversely, if the `choice` is not an empty string, then the `specs` parameter must be `None`. <br>• `choice` – Specifies a single resolution for all `ChoiceTypes`. You can use this in cases where the complete list of `ChoiceTypes` is unknown before runtime. In addition to the actions listed previously for `specs`, this argument also supports the following action: + `match_catalog` – Attempts to cast each `ChoiceType` to the corresponding type in the specified Data Catalog table. <br>• `database` – The Data Catalog database to use with the `match_catalog` action. <br>• `table_name` – The Data Catalog table to use with the `match_catalog` action. <br>• `transformation_ctx` – A unique string that is used to identify state information (optional). <br>• `info` – A string to be associated with error reporting for this transformation (optional). <br>• `stageThreshold` – The number of errors encountered during this transformation at which the process should error out (optional). The default is zero, which indicates that the process should not error out. <br>• `totalThreshold` – The number of errors encountered up to and including this transformation at which the process should error out (optional).The default is zero, which indicates that the process should not error out. <br>• `catalog_id` – The catalog ID of the Data Catalog being accessed (the account ID of the Data Catalog). When set to `None` (default value), it uses the catalog ID of the calling account. ### Example: Use resolveChoice to handle a column that contains multiple types This code example uses the `resolveChoice` method to specify how to handle a `DynamicFrame` column that contains values of multiple types. The example demonstrates two common ways to handle a column with different types: <br>• Cast the column to a single data type. <br>• Retain all types in separate columns. **Example dataset** ###### Note To access the dataset that is used in this example, see [Code example: Data preparation using ResolveChoice, Lambda, and ApplyMapping](aws-glue-programming-python-samples-medicaid.md "aws-glue-programming-python-samples-medicaid.md") and follow the instructions in [Step 1: Crawl the data in the Amazon S3 bucket](aws-glue-programming-python-samples-medicaid.md#aws-glue-programming-python-samples-medicaid-crawling "aws-glue-programming-python-samples-medicaid.md#aws-glue-programming-python-samples-medicaid-crawling"). The example uses a `DynamicFrame` called `medicare` with the following schema: ``` root |-- drg definition: string |-- provider id: choice |    |-- long
|    |-- string |-- provider name: string |-- provider street address: string |-- provider city: string
|-- provider state: string |-- provider zip code: long |-- hospital referral region description: string |-- total discharges: long |-- average covered charges: string
|-- average total payments: string |-- average medicare payments: string ``` **Example code** ``` # Example: Use resolveChoice to handle # a column that contains multiple types from pyspark.context import SparkContext from awsglue.context import GlueContext # Create GlueContext sc = SparkContext.getOrCreate() glueContext = GlueContext(sc) # Load the input data and inspect the "provider id" column medicare = glueContext.create_dynamic_frame.from_catalog( database="payments", table_name="medicare_hospital_provider_csv" ) print("Inspect the provider id column:") medicare.toDF().select("provider id").show() # Cast provider id to type long medicare_resolved_long = medicare.resolveChoice(specs=[("provider id", "cast:long")]) print("Schema after casting provider id to type long:") medicare_resolved_long.printSchema() medicare_resolved_long.toDF().select("provider id").show() # Create separate columns # for each provider id type medicare_resolved_cols = medicare.resolveChoice(choice="make_cols") print("Schema after creating separate columns for each type:") medicare_resolved_cols.printSchema() medicare_resolved_cols.toDF().select("provider id_long", "provider id_string").show() ``` ``` Inspect the 'provider id' column: +-----------+ |provider id| +-----------+ |   [10001,]|
|   [10005,]| |   [10006,]| |   [10011,]|
|   [10016,]| |   [10023,]| |   [10029,]|
|   [10033,]| |   [10039,]| |   [10040,]|
|   [10046,]| |   [10055,]| |   [10056,]|
|   [10078,]| |   [10083,]| |   [10085,]|
|   [10090,]| |   [10092,]| |   [10100,]|
|   [10103,]| +-----------+ only showing top 20 rows Schema after casting 'provider id' to type long: root |-- drg definition: string |-- provider id: long |-- provider name: string
|-- provider street address: string |-- provider city: string |-- provider state: string |-- provider zip code: long |-- hospital referral region description: string
|-- total discharges: long |-- average covered charges: string |-- average total payments: string |-- average medicare payments: string +-----------+ |provider id| +-----------+
|      10001| |      10005| |      10006|
|      10011| |      10016| |      10023|
|      10029| |      10033| |      10039|
|      10040| |      10046| |      10055|
|      10056| |      10078| |      10083|
|      10085| |      10090| |      10092|
|      10100| |      10103| +-----------+ only showing top 20 rows Schema after creating separate columns for each type: root |-- drg definition: string
|-- provider id_string: string |-- provider id_long: long |-- provider name: string |-- provider street address: string |-- provider city: string
|-- provider state: string |-- provider zip code: long |-- hospital referral region description: string |-- total discharges: long |-- average covered charges: string
|-- average total payments: string |-- average medicare payments: string +----------------+------------------+ |provider id_long|provider id_string| +----------------+------------------+
|           10001|              null| |           10005|              null|
|           10006|              null| |           10011|              null|
|           10016|              null| |           10023|              null|
|           10029|              null| |           10033|              null|
|           10039|              null| |           10040|              null|
|           10046|              null| |           10055|              null|
|           10056|              null| |           10078|              null|
|           10083|              null| |           10085|              null|
|           10090|              null| |           10092|              null|
|           10100|              null| |           10103|              null| +----------------+------------------+ only showing top 20 rows ``` ## select\_fields ###### `select_fields(paths, transformation_ctx="", info="", stageThreshold=0, totalThreshold=0)` Returns a new `DynamicFrame` that contains the selected fields. <br>• `paths` – A list of strings. Each string is a path to a top-level node that you want to select. <br>• `transformation_ctx` – A unique string that is used to identify state information (optional). <br>• `info` – A string to be associated with error reporting for this transformation (optional). <br>• `stageThreshold` – The number of errors encountered during this transformation at which the process should error out (optional). The default is zero, which indicates that the process should not error out. <br>• `totalThreshold` – The number of errors encountered up to and including this transformation at which the process should error out (optional). The default is zero, which indicates that the process should not error out. ### Example: Use select\_fields to create a new `DynamicFrame` with chosen fields The following code example shows how to use the `select_fields` method to create a new `DynamicFrame` with a chosen list of fields from an existing `DynamicFrame`. ###### Note To access the dataset that is used in this example, see [Code example: Joining and relationalizing data](aws-glue-programming-python-samples-legislators.md "aws-glue-programming-python-samples-legislators.md") and follow the instructions in [Step 1: Crawl the data in the Amazon S3 bucket](aws-glue-programming-python-samples-legislators.md#aws-glue-programming-python-samples-legislators-crawling "aws-glue-programming-python-samples-legislators.md#aws-glue-programming-python-samples-legislators-crawling"). ``` # Example: Use select_fields to select specific fields from a DynamicFrame from pyspark.context import SparkContext from awsglue.context import GlueContext # Create GlueContext sc = SparkContext.getOrCreate() glueContext = GlueContext(sc) # Create a DynamicFrame and view its schema persons = glueContext.create_dynamic_frame.from_catalog( database="legislators", table_name="persons_json" ) print("Schema for the persons DynamicFrame:") persons.printSchema() # Create a new DynamicFrame with chosen fields names = persons.select_fields(paths=["family_name", "given_name"]) print("Schema for the names DynamicFrame, created with select_fields:") names.printSchema() names.toDF().show() ``` ``` Schema for the persons DynamicFrame: root
|-- family_name: string |-- name: string |-- links: array |    |-- element: struct
|    |    |-- note: string |    |    |-- url: string
|-- gender: string |-- image: string |-- identifiers: array |    |-- element: struct
|    |    |-- scheme: string |    |    |-- identifier: string
|-- other_names: array |    |-- element: struct |    |    |-- lang: string
|    |    |-- note: string |    |    |-- name: string
|-- sort_name: string |-- images: array |    |-- element: struct |    |    |-- url: string
|-- given_name: string |-- birth_date: string |-- id: string |-- contact_details: array |    |-- element: struct
|    |    |-- type: string |    |    |-- value: string
|-- death_date: string Schema for the names DynamicFrame: root |-- family_name: string |-- given_name: string +-----------+----------+ |family_name|given_name| +-----------+----------+
|    Collins|   Michael| |   Huizenga|      Bill|
|    Clawson|    Curtis| |    Solomon|    Gerald|
|     Rigell|    Edward| |      Crapo|   Michael|
|      Hutto|      Earl| |      Ertel|     Allen|
|     Minish|    Joseph| |    Andrews|    Robert|
|     Walden|      Greg| |      Kazen|   Abraham|
|     Turner|   Michael| |      Kolbe|     James|
|  Lowenthal|      Alan| |    Capuano|   Michael|
|   Schrader|      Kurt| |     Nadler|   Jerrold|
|     Graves|       Tom| |   McMillan|      John| +-----------+----------+ only showing top 20 rows ``` ## simplify\_ddb\_json **`simplify_ddb_json(): DynamicFrame`** Simplifies nested columns in a `DynamicFrame` that are specifically in the DynamoDB JSON structure, and returns a new simplified `DynamicFrame`. If there’re multiple types or Map type in a List type, the elements in the List will not be simplified. Note that this is a specific type of transform that behaves differently from the regular `unnest` transform and requires the data to already be in the DynamoDB JSON structure. For more information, see [DynamoDB JSON](../../../amazondynamodb/latest/developerguide/DataExport.md#DataExport.Output.Data "../../../amazondynamodb/latest/developerguide/DataExport.md#DataExport.Output.Data"). For example, the schema of a reading an export with the DynamoDB JSON structure might look like the following: ``` root
|-- Item: struct |    |-- parentMap: struct |    |    |-- M: struct
|    |    |    |-- childMap: struct
|    |    |    |    |-- M: struct
|    |    |    |    |    |-- appName: struct
|    |    |    |    |    |    |-- S: string
|    |    |    |    |    |-- packageName: struct
|    |    |    |    |    |    |-- S: string
|    |    |    |    |    |-- updatedAt: struct
|    |    |    |    |    |    |-- N: string
|    |-- strings: struct |    |    |-- SS: array |    |    |    |-- element: string
|    |-- numbers: struct |    |    |-- NS: array |    |    |    |-- element: string
|    |-- binaries: struct |    |    |-- BS: array |    |    |    |-- element: string
|    |-- isDDBJson: struct |    |    |-- BOOL: boolean |    |-- nullValue: struct
|    |    |-- NULL: boolean ``` The `simplify_ddb_json()` transform would convert this to: ``` root |-- parentMap: struct |    |-- childMap: struct |    |    |-- appName: string
|    |    |-- packageName: string |    |    |-- updatedAt: string |-- strings: array
|    |-- element: string |-- numbers: array |    |-- element: string |-- binaries: array |    |-- element: string
|-- isDDBJson: boolean |-- nullValue: null ``` ### Example: Use simplify\_ddb\_json to invoke a DynamoDB JSON simplify This code example uses the `simplify_ddb_json` method to use the AWS Glue DynamoDB export connector, invoke a DynamoDB JSON simplify, and print the number of partitions. **Example code** ``` from pyspark.context import SparkContext from awsglue.context import GlueContext sc = SparkContext() glueContext = GlueContext(sc) dynamicFrame = glueContext.create_dynamic_frame.from_options( connection_type = "dynamodb", connection_options = { 'dynamodb.export': 'ddb', 'dynamodb.tableArn': '<table arn>', 'dynamodb.s3.bucket': '<bucket name>', 'dynamodb.s3.prefix': '<bucket prefix>', 'dynamodb.s3.bucketOwner': '<account_id of bucket>' } ) simplified = dynamicFrame.simplify_ddb_json() print(simplified.getNumPartitions()) ``` ## spigot ###### `spigot(path, options={})` Writes sample records to a specified destination to help you verify the transformations performed by your job. <br>• `path` – The path of the destination to write to (required). <br>• `options` – Key-value pairs that specify options (optional). The `"topk"` option specifies that the first `k` records should be written. The `"prob"` option specifies the probability (as a decimal) of choosing any given record. You can use it in selecting records to write. <br>• `transformation_ctx` – A unique string that is used to identify state information (optional). ### Example: Use spigot to write sample fields from a `DynamicFrame` to Amazon S3 This code example uses the `spigot` method to write sample records to an Amazon S3 bucket after applying the `select_fields` transform. **Example dataset** ###### Note To access the dataset that is used in this example, see [Code example: Joining and relationalizing data](aws-glue-programming-python-samples-legislators.md "aws-glue-programming-python-samples-legislators.md") and follow the instructions in [Step 1: Crawl the data in the Amazon S3 bucket](aws-glue-programming-python-samples-legislators.md#aws-glue-programming-python-samples-legislators-crawling "aws-glue-programming-python-samples-legislators.md#aws-glue-programming-python-samples-legislators-crawling"). The example uses a `DynamicFrame` called `persons` with the following schema: ``` root |-- family_name: string |-- name: string |-- links: array |    |-- element: struct
|    |    |-- note: string |    |    |-- url: string |-- gender: string
|-- image: string |-- identifiers: array |    |-- element: struct |    |    |-- scheme: string
|    |    |-- identifier: string |-- other_names: array |    |-- element: struct |    |    |-- lang: string
|    |    |-- note: string |    |    |-- name: string |-- sort_name: string
|-- images: array |    |-- element: struct |    |    |-- url: string |-- given_name: string
|-- birth_date: string |-- id: string |-- contact_details: array |    |-- element: struct |    |    |-- type: string
|    |    |-- value: string |-- death_date: string ``` **Example code** ``` # Example: Use spigot to write sample records # to a destination during a transformation # from pyspark.context import SparkContext. # Replace DOC-EXAMPLE-BUCKET with your own location. from pyspark.context import SparkContext from awsglue.context import GlueContext # Create GlueContext sc = SparkContext.getOrCreate() glueContext = GlueContext(sc) # Load table data into a DynamicFrame persons = glueContext.create_dynamic_frame.from_catalog( database="legislators", table_name="persons_json" ) # Perform the select_fields on the DynamicFrame persons = persons.select_fields(paths=["family_name", "given_name", "birth_date"]) # Use spigot to write a sample of the transformed data # (the first 10 records) spigot_output = persons.spigot( path="`s3://DOC-EXAMPLE-BUCKET`", options={"topk": 10} ) # Example: Use spigot to write sample records # to a destination during a transformation # from pyspark.context import SparkContext. # Replace DOC-EXAMPLE-BUCKET with your own location. from pyspark.context import SparkContext from awsglue.context import GlueContext # Create GlueContext sc = SparkContext.getOrCreate() glueContext = GlueContext(sc) # Load table data into a DynamicFrame persons = glueContext.create_dynamic_frame.from_catalog( database="legislators", table_name="persons_json" ) # Perform the select_fields on the DynamicFrame persons = persons.select_fields(paths=["family_name", "given_name", "birth_date"]) # Use spigot to write a sample of the transformed data # (the first 10 records) spigot_output = persons.spigot( path="`s3://DOC-EXAMPLE-BUCKET`", options={"topk": 10} ) ``` The following is an example of the data that `spigot` writes to Amazon S3. Because the example code specified `options={"topk": 10}`, the sample data contains the first 10 records. ``` {"family_name":"Collins","given_name":"Michael","birth_date":"1944-10-15"} {"family_name":"Huizenga","given_name":"Bill","birth_date":"1969-01-31"} {"family_name":"Clawson","given_name":"Curtis","birth_date":"1959-09-28"} {"family_name":"Solomon","given_name":"Gerald","birth_date":"1930-08-14"} {"family_name":"Rigell","given_name":"Edward","birth_date":"1960-05-28"} {"family_name":"Crapo","given_name":"Michael","birth_date":"1951-05-20"} {"family_name":"Hutto","given_name":"Earl","birth_date":"1926-05-12"} {"family_name":"Ertel","given_name":"Allen","birth_date":"1937-11-07"} {"family_name":"Minish","given_name":"Joseph","birth_date":"1916-09-01"} {"family_name":"Andrews","given_name":"Robert","birth_date":"1957-08-04"} ``` ## split\_fields ###### `split_fields(paths, name1, name2, transformation_ctx="", info="", stageThreshold=0, totalThreshold=0)` Returns a new `DynamicFrameCollection` that contains two `DynamicFrames`. The first `DynamicFrame` contains all the nodes that have been split off, and the second contains the nodes that remain. <br>• `paths` – A list of strings, each of which is a full path to a node that you want to split into a new `DynamicFrame`. <br>• `name1` – A name string for the `DynamicFrame` that is split off. <br>• `name2` – A name string for the `DynamicFrame` that remains after the specified nodes have been split off. <br>• `transformation_ctx` – A unique string that is used to identify state information (optional). <br>• `info` – A string to be associated with error reporting for this transformation (optional). <br>• `stageThreshold` – The number of errors encountered during this transformation at which the process should error out (optional). The default is zero, which indicates that the process should not error out. <br>• `totalThreshold` – The number of errors encountered up to and including this transformation at which the process should error out (optional). The default is zero, which indicates that the process should not error out. ### Example: Use split\_fields to split selected fields into a separate `DynamicFrame` This code example uses the `split_fields` method to split a list of specified fields into a separate `DynamicFrame`. **Example dataset** The example uses a `DynamicFrame` called `l_root_contact_details` that is from a collection named `legislators_relationalized`. `l_root_contact_details` has the following schema and entries. ``` root |-- id: long |-- index: int |-- contact_details.val.type: string
|-- contact_details.val.value: string +---+-----+------------------------+-------------------------+ | id|index|contact_details.val.type|contact_details.val.value| +---+-----+------------------------+-------------------------+ |  1|    0|                   phone|             202-225-5265|
|  1|    1|                 twitter|              kathyhochul| |  2|    0|                   phone|             202-225-3252|
|  2|    1|                 twitter|            repjackyrosen| |  3|    0|                     fax|             202-225-1314|
|  3|    1|                   phone|             202-225-3772| ... ``` **Example code** ``` # Example: Use split_fields to split selected # fields into a separate DynamicFrame from pyspark.context import SparkContext from awsglue.context import GlueContext # Create GlueContext sc = SparkContext.getOrCreate() glueContext = GlueContext(sc) # Load the input DynamicFrame and inspect its schema frame_to_split = legislators_relationalized.select("l_root_contact_details") print("Inspect the input DynamicFrame schema:") frame_to_split.printSchema() # Split id and index fields into a separate DynamicFrame split_fields_collection = frame_to_split.split_fields(["id", "index"], "left", "right") # Inspect the resulting DynamicFrames print("Inspect the schemas of the DynamicFrames created with split_fields:") split_fields_collection.select("left").printSchema() split_fields_collection.select("right").printSchema() ``` ``` Inspect the input DynamicFrame's schema: root |-- id: long |-- index: int
|-- contact_details.val.type: string |-- contact_details.val.value: string Inspect the schemas of the DynamicFrames created with split_fields: root |-- id: long |-- index: int root |-- contact_details.val.type: string |-- contact_details.val.value: string ``` ## split\_rows ###### `split_rows(comparison_dict, name1, name2, transformation_ctx="", info="", stageThreshold=0, totalThreshold=0)` Splits one or more rows in a `DynamicFrame` off into a new `DynamicFrame`. The method returns a new `DynamicFrameCollection` that contains two `DynamicFrames`. The first `DynamicFrame` contains all the rows that have been split off, and the second contains the rows that remain. <br>• `comparison_dict` – A dictionary where the key is a path to a column, and the value is another dictionary for mapping comparators to values that the column values are compared to. For example, `{"age": {">": 10, "<": 20}}` splits off all rows whose value in the age column is greater than 10 and less than 20. <br>• `name1` – A name string for the `DynamicFrame` that is split off. <br>• `name2` – A name string for the `DynamicFrame` that remains after the specified nodes have been split off. <br>• `transformation_ctx` – A unique string that is used to identify state information (optional). <br>• `info` – A string to be associated with error reporting for this transformation (optional). <br>• `stageThreshold` – The number of errors encountered during this transformation at which the process should error out (optional). The default is zero, which indicates that the process should not error out. <br>• `totalThreshold` – The number of errors encountered up to and including this transformation at which the process should error out (optional). The default is zero, which indicates that the process should not error out. ### Example: Use split\_rows to split rows in a `DynamicFrame` This code example uses the `split_rows` method to split rows in a `DynamicFrame` based on the `id` field value. **Example dataset** The example uses a `DynamicFrame` called `l_root_contact_details` that is selected from a collection named `legislators_relationalized`. `l_root_contact_details` has the following schema and entries. ``` root |-- id: long
|-- index: int |-- contact_details.val.type: string |-- contact_details.val.value: string +---+-----+------------------------+-------------------------+ | id|index|contact_details.val.type|contact_details.val.value| +---+-----+------------------------+-------------------------+
|  1|    0|                   phone|             202-225-5265| |  1|    1|                 twitter|              kathyhochul|
|  2|    0|                   phone|             202-225-3252| |  2|    1|                 twitter|            repjackyrosen|
|  3|    0|                     fax|             202-225-1314| |  3|    1|                   phone|             202-225-3772|
|  3|    2|                 twitter|          MikeRossUpdates| |  4|    0|                     fax|             202-225-1314|
|  4|    1|                   phone|             202-225-3772| |  4|    2|                 twitter|          MikeRossUpdates|
|  5|    0|                     fax|             202-225-1314| |  5|    1|                   phone|             202-225-3772|
|  5|    2|                 twitter|          MikeRossUpdates| |  6|    0|                     fax|             202-225-1314|
|  6|    1|                   phone|             202-225-3772| |  6|    2|                 twitter|          MikeRossUpdates|
|  7|    0|                     fax|             202-225-1314| |  7|    1|                   phone|             202-225-3772|
|  7|    2|                 twitter|          MikeRossUpdates| |  8|    0|                     fax|             202-225-1314| +---+-----+------------------------+-------------------------+ ``` **Example code** ``` # Example: Use split_rows to split up # rows in a DynamicFrame based on value from pyspark.context import SparkContext from awsglue.context import GlueContext # Create GlueContext sc = SparkContext.getOrCreate() glueContext = GlueContext(sc) # Retrieve the DynamicFrame to split frame_to_split = legislators_relationalized.select("l_root_contact_details") # Split up rows by ID split_rows_collection = frame_to_split.split_rows({"id": {">": 10}}, "high", "low") # Inspect the resulting DynamicFrames print("Inspect the DynamicFrame that contains IDs < 10") split_rows_collection.select("low").toDF().show() print("Inspect the DynamicFrame that contains IDs > 10") split_rows_collection.select("high").toDF().show() ``` ``` Inspect the DynamicFrame that contains IDs < 10 +---+-----+------------------------+-------------------------+
| id|index|contact_details.val.type|contact_details.val.value| +---+-----+------------------------+-------------------------+ |  1|    0|                   phone|             202-225-5265|
|  1|    1|                 twitter|              kathyhochul| |  2|    0|                   phone|             202-225-3252|
|  2|    1|                 twitter|            repjackyrosen| |  3|    0|                     fax|             202-225-1314|
|  3|    1|                   phone|             202-225-3772| |  3|    2|                 twitter|          MikeRossUpdates|
|  4|    0|                     fax|             202-225-1314| |  4|    1|                   phone|             202-225-3772|
|  4|    2|                 twitter|          MikeRossUpdates| |  5|    0|                     fax|             202-225-1314|
|  5|    1|                   phone|             202-225-3772| |  5|    2|                 twitter|          MikeRossUpdates|
|  6|    0|                     fax|             202-225-1314| |  6|    1|                   phone|             202-225-3772|
|  6|    2|                 twitter|          MikeRossUpdates| |  7|    0|                     fax|             202-225-1314|
|  7|    1|                   phone|             202-225-3772| |  7|    2|                 twitter|          MikeRossUpdates|
|  8|    0|                     fax|             202-225-1314| +---+-----+------------------------+-------------------------+ only showing top 20 rows Inspect the DynamicFrame that contains IDs > 10 +---+-----+------------------------+-------------------------+ | id|index|contact_details.val.type|contact_details.val.value| +---+-----+------------------------+-------------------------+
| 11|    0|                   phone|             202-225-5476| | 11|    1|                 twitter|            RepDavidYoung|
| 12|    0|                   phone|             202-225-4035| | 12|    1|                 twitter|           RepStephMurphy|
| 13|    0|                     fax|             202-226-0774| | 13|    1|                   phone|             202-225-6335|
| 14|    0|                     fax|             202-226-0774| | 14|    1|                   phone|             202-225-6335|
| 15|    0|                     fax|             202-226-0774| | 15|    1|                   phone|             202-225-6335|
| 16|    0|                     fax|             202-226-0774| | 16|    1|                   phone|             202-225-6335|
| 17|    0|                     fax|             202-226-0774| | 17|    1|                   phone|             202-225-6335|
| 18|    0|                     fax|             202-226-0774| | 18|    1|                   phone|             202-225-6335|
| 19|    0|                     fax|             202-226-0774| | 19|    1|                   phone|             202-225-6335|
| 20|    0|                     fax|             202-226-0774| | 20|    1|                   phone|             202-225-6335| +---+-----+------------------------+-------------------------+ only showing top 20 rows ``` ## unbox ###### `unbox(path, format, transformation_ctx="", info="", stageThreshold=0, totalThreshold=0, **options)` Unboxes (reformats) a string field in a `DynamicFrame` and returns a new `DynamicFrame` that contains the unboxed `DynamicRecords`. A `DynamicRecord` represents a logical record in a `DynamicFrame`. It's similar to a row in an Apache Spark `DataFrame`, except that it is self-describing and can be used for data that doesn't conform to a fixed schema. <br>• `path` – A full path to the string node you want to unbox. <br>• `format` – A format specification (optional). You use this for an Amazon S3 or AWS Glue connection that supports multiple formats. For the formats that are supported, see [Data format options for inputs and outputs in AWS Glue for Spark](aws-glue-programming-etl-format.md "aws-glue-programming-etl-format.md"). <br>• `transformation_ctx` – A unique string that is used to identify state information (optional). <br>• `info` – A string to be associated with error reporting for this transformation (optional). <br>• `stageThreshold` – The number of errors encountered during this transformation at which the process should error out (optional). The default is zero, which indicates that the process should not error out. <br>• `totalThreshold` – The number of errors encountered up to and including this transformation at which the process should error out (optional). The default is zero, which indicates that the process should not error out. <br>• `options` – One or more of the following: + `separator` – A string that contains the separator character. + `escaper` – A string that contains the escape character. + `skipFirst` – A Boolean value that indicates whether to skip the first instance. + `withSchema` – A string containing a JSON representation of the node's schema. The format of a schema's JSON representation is defined by the output of `StructType.json()`. + `withHeader` – A Boolean value that indicates whether a header is included. ### Example: Use unbox to unbox a string field into a struct This code example uses the `unbox` method to *unbox*, or reformat, a string field in a `DynamicFrame` into a field of type struct. **Example dataset** The example uses a `DynamicFrame` called `mapped_with_string` with the following schema and entries. Notice the field named `AddressString`. This is the field that the example unboxes into a struct. ``` root
|-- Average Total Payments: string |-- AddressString: string |-- Average Covered Charges: string |-- DRG Definition: string |-- Average Medicare Payments: string |-- Hospital Referral Region Description: string |-- Address: struct
|    |-- Zip.Code: string |    |-- City: string |    |-- Array: array |    |    |-- element: string
|    |-- State: string |    |-- Street: string |-- Provider Id: string |-- Total Discharges: string |-- Provider Name: string +----------------------+--------------------+-----------------------+--------------------+-------------------------+------------------------------------+--------------------+-----------+----------------+--------------------+
|Average Total Payments|       AddressString|Average Covered Charges|      DRG Definition|Average Medicare Payments|Hospital Referral Region Description|             Address|Provider Id|Total Discharges|       Provider Name| +----------------------+--------------------+-----------------------+--------------------+-------------------------+------------------------------------+--------------------+-----------+----------------+--------------------+
|              $5777.24|{"Street": "1108 ...|              $32963.07|039 - EXTRACRANIA...|                 $4763.73|                         AL - Dothan|[36301, DOTHAN, [...|      10001|              91|SOUTHEAST ALABAMA...|
|              $5787.57|{"Street": "2505 ...|              $15131.85|039 - EXTRACRANIA...|                 $4976.71|                     AL - Birmingham|[35957, BOAZ, [25...|      10005|              14|MARSHALL MEDICAL ...|
|              $5434.95|{"Street": "205 M...|              $37560.37|039 - EXTRACRANIA...|                 $4453.79|                     AL - Birmingham|[35631, FLORENCE,...|      10006|              24|ELIZA COFFEE MEMO...|
|              $5417.56|{"Street": "50 ME...|              $13998.28|039 - EXTRACRANIA...|                 $4129.16|                     AL - Birmingham|[35235, BIRMINGHA...|      10011|              25|   ST VINCENT'S EAST| ... ``` **Example code** ``` # Example: Use unbox to unbox a string field # into a struct in a DynamicFrame from pyspark.context import SparkContext from awsglue.context import GlueContext # Create GlueContext sc = SparkContext.getOrCreate() glueContext = GlueContext(sc) unboxed = mapped_with_string.unbox("AddressString", "json") unboxed.printSchema() unboxed.toDF().show() ``` ``` root
|-- Average Total Payments: string |-- AddressString: struct |    |-- Street: string |    |-- City: string |    |-- State: string |    |-- Zip.Code: string |    |-- Array: array
|    |    |-- element: string |-- Average Covered Charges: string |-- DRG Definition: string |-- Average Medicare Payments: string |-- Hospital Referral Region Description: string |-- Address: struct |    |-- Zip.Code: string |    |-- City: string
|    |-- Array: array |    |    |-- element: string |    |-- State: string |    |-- Street: string |-- Provider Id: string |-- Total Discharges: string
|-- Provider Name: string +----------------------+--------------------+-----------------------+--------------------+-------------------------+------------------------------------+--------------------+-----------+----------------+--------------------+
|Average Total Payments|       AddressString|Average Covered Charges|      DRG Definition|Average Medicare Payments|Hospital Referral Region Description|             Address|Provider Id|Total Discharges|       Provider Name| +----------------------+--------------------+-----------------------+--------------------+-------------------------+------------------------------------+--------------------+-----------+----------------+--------------------+
|              $5777.24|[1108 ROSS CLARK ...|              $32963.07|039 - EXTRACRANIA...|                 $4763.73|                         AL - Dothan|[36301, DOTHAN, [...|      10001|              91|SOUTHEAST ALABAMA...|
|              $5787.57|[2505 U S HIGHWAY...|              $15131.85|039 - EXTRACRANIA...|                 $4976.71|                     AL - Birmingham|[35957, BOAZ, [25...|      10005|              14|MARSHALL MEDICAL ...|
|              $5434.95|[205 MARENGO STRE...|              $37560.37|039 - EXTRACRANIA...|                 $4453.79|                     AL - Birmingham|[35631, FLORENCE,...|      10006|              24|ELIZA COFFEE MEMO...|
|              $5417.56|[50 MEDICAL PARK ...|              $13998.28|039 - EXTRACRANIA...|                 $4129.16|                     AL - Birmingham|[35235, BIRMINGHA...|      10011|              25|   ST VINCENT'S EAST|
|              $5658.33|[1000 FIRST STREE...|              $31633.27|039 - EXTRACRANIA...|                 $4851.44|                     AL - Birmingham|[35007, ALABASTER...|      10016|              18|SHELBY BAPTIST ME...|
|              $6653.80|[2105 EAST SOUTH ...|              $16920.79|039 - EXTRACRANIA...|                 $5374.14|                     AL - Montgomery|[36116, MONTGOMER...|      10023|              67|BAPTIST MEDICAL C...|
|              $5834.74|[2000 PEPPERELL P...|              $11977.13|039 - EXTRACRANIA...|                 $4761.41|                     AL - Birmingham|[36801, OPELIKA, ...|      10029|              51|EAST ALABAMA MEDI...|
|              $8031.12|[619 SOUTH 19TH S...|              $35841.09|039 - EXTRACRANIA...|                 $5858.50|                     AL - Birmingham|[35233, BIRMINGHA...|      10033|              32|UNIVERSITY OF ALA...|
|              $6113.38|[101 SIVLEY RD, H...|              $28523.39|039 - EXTRACRANIA...|                 $5228.40|                     AL - Huntsville|[35801, HUNTSVILL...|      10039|             135| HUNTSVILLE HOSPITAL|
|              $5541.05|[1007 GOODYEAR AV...|              $75233.38|039 - EXTRACRANIA...|                 $4386.94|                     AL - Birmingham|[35903, GADSDEN, ...|      10040|              34|GADSDEN REGIONAL ...|
|              $5461.57|[600 SOUTH THIRD ...|              $67327.92|039 - EXTRACRANIA...|                 $4493.57|                     AL - Birmingham|[35901, GADSDEN, ...|      10046|              14|RIVERVIEW REGIONA...|
|              $5356.28|[4370 WEST MAIN S...|              $39607.28|039 - EXTRACRANIA...|                 $4408.20|                         AL - Dothan|[36305, DOTHAN, [...|      10055|              45|    FLOWERS HOSPITAL|
|              $5374.65|[810 ST VINCENT'S...|              $22862.23|039 - EXTRACRANIA...|                 $4186.02|                     AL - Birmingham|[35205, BIRMINGHA...|      10056|              43|ST VINCENT'S BIRM...|
|              $5366.23|[400 EAST 10TH ST...|              $31110.85|039 - EXTRACRANIA...|                 $4376.23|                     AL - Birmingham|[36207, ANNISTON,...|      10078|              21|NORTHEAST ALABAMA...|
|              $5282.93|[1613 NORTH MCKEN...|              $25411.33|039 - EXTRACRANIA...|                 $4383.73|                         AL - Mobile|[36535, FOLEY, [1...|      10083|              15|SOUTH BALDWIN REG...|
|              $5676.55|[1201 7TH STREET ...|               $9234.51|039 - EXTRACRANIA...|                 $4509.11|                     AL - Huntsville|[35609, DECATUR, ...|      10085|              27|DECATUR GENERAL H...|
|              $5930.11|[6801 AIRPORT BOU...|              $15895.85|039 - EXTRACRANIA...|                 $3972.85|                         AL - Mobile|[36608, MOBILE, [...|      10090|              27| PROVIDENCE HOSPITAL|
|              $6192.54|[809 UNIVERSITY B...|              $19721.16|039 - EXTRACRANIA...|                 $5179.38|                     AL - Tuscaloosa|[35401, TUSCALOOS...|      10092|              31|D C H REGIONAL ME...|
|              $4968.00|[750 MORPHY AVENU...|              $10710.88|039 - EXTRACRANIA...|                 $3898.88|                         AL - Mobile|[36532, FAIRHOPE,...|      10100|              18|     THOMAS HOSPITAL|
|              $5996.00|[701 PRINCETON AV...|              $51343.75|039 - EXTRACRANIA...|                 $4962.45|                     AL - Birmingham|[35211, BIRMINGHA...|      10103|              33|BAPTIST MEDICAL C...| +----------------------+--------------------+-----------------------+--------------------+-------------------------+------------------------------------+--------------------+-----------+----------------+--------------------+ only showing top 20 rows ``` ## union ###### `union(frame1, frame2, transformation_ctx = "", info = "", stageThreshold = 0, totalThreshold = 0)` Union two DynamicFrames. Returns DynamicFrame containing all records from both input DynamicFrames. This transform may return different results from the union of two DataFrames with equivalent data. If you need the Spark DataFrame union behavior, consider using `toDF`. <br>• `frame1` – First DynamicFrame to union. <br>• `frame2` – Second DynamicFrame to union. <br>• `transformation_ctx` – (optional) A unique string that is used to identify stats / state information <br>• `info` – (optional) Any string to be associated with errors in the transformation <br>• `stageThreshold` – (optional) Max number of errors in the transformation until processing will error out <br>• `totalThreshold` – (optional) Max number of errors total until processing will error out. ## unnest ###### `unnest(transformation_ctx="", info="", stageThreshold=0, totalThreshold=0)` Unnests nested objects in a `DynamicFrame`, which makes them top-level objects, and returns a new unnested `DynamicFrame`. <br>• `transformation_ctx` – A unique string that is used to identify state information (optional). <br>• `info` – A string to be associated with error reporting for this transformation (optional). <br>• `stageThreshold` – The number of errors encountered during this transformation at which the process should error out (optional). The default is zero, which indicates that the process should not error out. <br>• `totalThreshold` – The number of errors encountered up to and including this transformation at which the process should error out (optional). The default is zero, which indicates that the process should not error out. ### Example: Use unnest to turn nested fields into top-level fields This code example uses the `unnest` method to flatten all of the nested fields in a `DynamicFrame` into top-level fields. **Example dataset** The example uses a `DynamicFrame` called `mapped_medicare` with the following schema. Notice that the `Address` field is the only field that contains nested data. ``` root
|-- Average Total Payments: string |-- Average Covered Charges: string |-- DRG Definition: string |-- Average Medicare Payments: string |-- Hospital Referral Region Description: string |-- Address: struct |    |-- Zip.Code: string |    |-- City: string |    |-- Array: array
|    |    |-- element: string |    |-- State: string |    |-- Street: string |-- Provider Id: string |-- Total Discharges: string |-- Provider Name: string ``` **Example code** ``` # Example: Use unnest to unnest nested # objects in a DynamicFrame from pyspark.context import SparkContext from awsglue.context import GlueContext # Create GlueContext sc = SparkContext.getOrCreate() glueContext = GlueContext(sc) # Unnest all nested fields unnested = mapped_medicare.unnest() unnested.printSchema() ``` ``` root |-- Average Total Payments: string
|-- Average Covered Charges: string |-- DRG Definition: string |-- Average Medicare Payments: string |-- Hospital Referral Region Description: string |-- Address.Zip.Code: string |-- Address.City: string |-- Address.Array: array |    |-- element: string |-- Address.State: string |-- Address.Street: string
|-- Provider Id: string |-- Total Discharges: string |-- Provider Name: string ``` ## unnest\_ddb\_json Unnests nested columns in a `DynamicFrame` that are specifically in the DynamoDB JSON structure, and returns a new unnested `DynamicFrame`. Columns that are of an array of struct types will not be unnested. Note that this is a specific type of unnesting transform that behaves differently from the regular `unnest` transform and requires the data to already be in the DynamoDB JSON structure. For more information, see [DynamoDB JSON](../../../amazondynamodb/latest/developerguide/DataExport.md#DataExport.Output.Data "../../../amazondynamodb/latest/developerguide/DataExport.md#DataExport.Output.Data"). ###### `unnest_ddb_json(transformation_ctx="", info="", stageThreshold=0, totalThreshold=0)` <br>• `transformation_ctx` – A unique string that is used to identify state information (optional). <br>• `info` – A string to be associated with error reporting for this transformation (optional). <br>• `stageThreshold` – The number of errors encountered during this transformation at which the process should error out (optional: zero by default, indicating that the process should not error out). <br>• `totalThreshold` – The number of errors encountered up to and including this transformation at which the process should error out (optional: zero by default, indicating that the process should not error out). For example, the schema of a reading an export with the DynamoDB JSON structure might look like the following: ``` root |-- Item: struct |    |-- ColA: struct |    |    |-- S: string |    |-- ColB: struct
|    |    |-- S: string |    |-- ColC: struct |    |    |-- N: string |    |-- ColD: struct |    |    |-- L: array
|    |    |    |-- element: null ``` The `unnest_ddb_json()` transform would convert this to: ``` root |-- ColA: string |-- ColB: string |-- ColC: string |-- ColD: array |    |-- element: null ``` The following code example shows how to use the AWS Glue DynamoDB export connector, invoke a DynamoDB JSON unnest, and print the number of partitions: ``` import sys from pyspark.context import SparkContext from awsglue.context import GlueContext from awsglue.job import Job from awsglue.utils import getResolvedOptions args = getResolvedOptions(sys.argv, ["JOB_NAME"]) glue_context= GlueContext(SparkContext.getOrCreate()) job = Job(glue_context) job.init(args["JOB_NAME"], args) dynamicFrame = glue_context.create_dynamic_frame.from_options( connection_type="dynamodb", connection_options={ "dynamodb.export": "ddb", "dynamodb.tableArn": "<test_source>", "dynamodb.s3.bucket": "<bucket name>", "dynamodb.s3.prefix": "<bucket prefix>", "dynamodb.s3.bucketOwner": "<account_id>", } ) unnested = dynamicFrame.unnest_ddb_json() print(unnested.getNumPartitions()) job.commit() ``` ## write ###### `write(connection_type, connection_options, format, format_options, accumulator_size)` Gets a [DataSink(object)](aws-glue-api-crawler-pyspark-extensions-types.md#aws-glue-api-crawler-pyspark-extensions-types-awsglue-data-sink "aws-glue-api-crawler-pyspark-extensions-types.md#aws-glue-api-crawler-pyspark-extensions-types-awsglue-data-sink") of the specified connection type from the [GlueContext class](aws-glue-api-crawler-pyspark-extensions-glue-context.md "aws-glue-api-crawler-pyspark-extensions-glue-context.md") of this `DynamicFrame`, and uses it to format and write the contents of this `DynamicFrame`. Returns the new `DynamicFrame` formatted and written as specified. <br>• `connection_type` – The connection type to use. Valid values include `s3`, `mysql`, `postgresql`, `redshift`, `sqlserver`, and `oracle`. <br>• `connection_options` – The connection option to use (optional). For a `connection_type` of `s3`, an Amazon S3 path is defined. ``` connection_options = {"path": "`s3://aws-glue-target/temp`"} ``` For JDBC connections, several properties must be defined. Note that the database name must be part of the URL. It can optionally be included in the connection options. ###### Warning Storing passwords in your script is not recommended. Consider using `boto3` to retrieve them from AWS Secrets Manager or the AWS Glue Data Catalog. ``` connection_options = {"url": "`jdbc-url/database`", "user": "`username`", "password": `passwordVariable`,"dbtable": "`table-name`", "redshiftTmpDir": "`s3-tempdir-path`"} ``` <br>• `format` – A format specification (optional). This is used for an Amazon Simple Storage Service (Amazon S3) or an AWS Glue connection that supports multiple formats. See [Data format options for inputs and outputs in AWS Glue for Spark](aws-glue-programming-etl-format.md "aws-glue-programming-etl-format.md") for the formats that are supported. <br>• `format_options` – Format options for the specified format. See [Data format options for inputs and outputs in AWS Glue for Spark](aws-glue-programming-etl-format.md "aws-glue-programming-etl-format.md") for the formats that are supported. <br>• `accumulator_size` – The accumulable size to use, in bytes (optional). ##  — errors — <br>• [assertErrorThreshold](#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-assertErrorThreshold "#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-assertErrorThreshold") <br>• [errorsAsDynamicFrame](#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-errorsAsDynamicFrame "#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-errorsAsDynamicFrame") <br>• [errorsCount](#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-errorsCount "#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-errorsCount") <br>• [stageErrorsCount](#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-stageErrorsCount "#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-stageErrorsCount") ## assertErrorThreshold `assertErrorThreshold( )` – An assert for errors in the transformations that created this `DynamicFrame`. Returns an `Exception` from the underlying `DataFrame`. ## errorsAsDynamicFrame `errorsAsDynamicFrame( )` – Returns a `DynamicFrame` that has error records nested inside. ### Example: Use errorsAsDynamicFrame to view error records The following code example shows how to use the `errorsAsDynamicFrame` method to view an error record for a `DynamicFrame`. **Example dataset** The example uses the following dataset that you can upload to Amazon S3 as JSON. Notice that the second record is malformed. Malformed data typically breaks file parsing when you use SparkSQL. However, `DynamicFrame` recognizes malformation issues and turns malformed lines into error records that you can handle individually. ``` {"id": 1, "name": "george", "surname": "washington", "height": 178} {"id": 2, "name": "benjamin", "surname": "franklin", {"id": 3, "name": "alexander", "surname": "hamilton", "height": 171} {"id": 4, "name": "john", "surname": "jay", "height": 190} ``` **Example code** ``` # Example: Use errorsAsDynamicFrame to view error records. # Replace s3://DOC-EXAMPLE-S3-BUCKET/error_data.json with your location. from pyspark.context import SparkContext from awsglue.context import GlueContext # Create GlueContext sc = SparkContext.getOrCreate() glueContext = GlueContext(sc) # Create errors DynamicFrame, view schema errors = glueContext.create_dynamic_frame.from_options( "s3", {"paths": ["`s3://DOC-EXAMPLE-S3-BUCKET/error_data.json`"]}, "json" ) print("Schema of errors DynamicFrame:") errors.printSchema() # Show that errors only contains valid entries from the dataset print("errors contains only valid records from the input dataset (2 of 4 records)") errors.toDF().show() # View errors print("Errors count:", str(errors.errorsCount())) print("Errors:") errors.errorsAsDynamicFrame().toDF().show() # View error fields and error data error_record = errors.errorsAsDynamicFrame().toDF().head() error_fields = error_record["error"] print("Error fields: ") print(error_fields.asDict().keys()) print("\nError record data:") for key in error_fields.asDict().keys(): print("\n", key, ": ", str(error_fields[key])) ``` ``` Schema of errors DynamicFrame: root |-- id: int
|-- name: string |-- surname: string |-- height: int errors contains only valid records from the input dataset (2 of 4 records) +---+------+----------+------+ | id|  name|   surname|height| +---+------+----------+------+ |  1|george|washington|   178|
|  4|  john|       jay|   190| +---+------+----------+------+ Errors count: 1 Errors: +--------------------+ |               error| +--------------------+ |[[  File "/tmp/20...| +--------------------+ Error fields: dict_keys(['callsite', 'msg', 'stackTrace', 'input', 'bytesread', 'source', 'dynamicRecord']) Error record data: callsite :  Row(site='  File "/tmp/2060612586885849088", line 549, in <module>\n    sys.exit(main())\n  File "/tmp/2060612586885849088", line 523, in main\n    response = handler(content)\n  File "/tmp/2060612586885849088", line 197, in execute_request\n    result = node.execute()\n  File "/tmp/2060612586885849088", line 103, in execute\n    exec(code, global_dict)\n  File "<stdin>", line 10, in <module>\n  File "/opt/amazon/lib/python3.6/site-packages/awsglue/dynamicframe.py", line 625, in from_options\n    format_options, transformation_ctx, push_down_predicate, **kwargs)\n  File "/opt/amazon/lib/python3.6/site-packages/awsglue/context.py", line 233, in create_dynamic_frame_from_options\n    source.setFormat(format, **format_options)\n', info='') msg :  error in jackson reader stackTrace :  com.fasterxml.jackson.core.JsonParseException: Unexpected character ('{' (code 123)): was expecting either valid name character (for unquoted name) or double-quote (for quoted) to start field name at [Source: com.amazonaws.services.glue.readers.BufferedStream@73492578; line: 3, column: 2] at com.fasterxml.jackson.core.JsonParser._constructError(JsonParser.java:1581) at com.fasterxml.jackson.core.base.ParserMinimalBase._reportError(ParserMinimalBase.java:533) at com.fasterxml.jackson.core.base.ParserMinimalBase._reportUnexpectedChar(ParserMinimalBase.java:462) at com.fasterxml.jackson.core.json.UTF8StreamJsonParser._handleOddName(UTF8StreamJsonParser.java:2012) at com.fasterxml.jackson.core.json.UTF8StreamJsonParser._parseName(UTF8StreamJsonParser.java:1650) at com.fasterxml.jackson.core.json.UTF8StreamJsonParser.nextToken(UTF8StreamJsonParser.java:740) at com.amazonaws.services.glue.readers.JacksonReader$$anonfun$hasNextGoodToken$1.apply(JacksonReader.scala:57) at com.amazonaws.services.glue.readers.JacksonReader$$anonfun$hasNextGoodToken$1.apply(JacksonReader.scala:57) at scala.collection.Iterator$$anon$9.next(Iterator.scala:162) at scala.collection.Iterator$$anon$16.hasNext(Iterator.scala:599) at scala.collection.Iterator$$anon$16.hasNext(Iterator.scala:598) at scala.collection.Iterator$class.foreach(Iterator.scala:891) at scala.collection.AbstractIterator.foreach(Iterator.scala:1334) at com.amazonaws.services.glue.readers.JacksonReader$$anonfun$1.apply(JacksonReader.scala:120) at com.amazonaws.services.glue.readers.JacksonReader$$anonfun$1.apply(JacksonReader.scala:116) at com.amazonaws.services.glue.DynamicRecordBuilder.handleErr(DynamicRecordBuilder.scala:209) at com.amazonaws.services.glue.DynamicRecordBuilder.handleErrorWithException(DynamicRecordBuilder.scala:202) at com.amazonaws.services.glue.readers.JacksonReader.nextFailSafe(JacksonReader.scala:116) at com.amazonaws.services.glue.readers.JacksonReader.next(JacksonReader.scala:109) at com.amazonaws.services.glue.readers.JSONReader.next(JSONReader.scala:247) at com.amazonaws.services.glue.hadoop.TapeHadoopRecordReaderSplittable.nextKeyValue(TapeHadoopRecordReaderSplittable.scala:103) at org.apache.spark.rdd.NewHadoopRDD$$anon$1.hasNext(NewHadoopRDD.scala:230) at org.apache.spark.InterruptibleIterator.hasNext(InterruptibleIterator.scala:37) at scala.collection.Iterator$$anon$11.hasNext(Iterator.scala:409) at scala.collection.Iterator$$anon$11.hasNext(Iterator.scala:409) at scala.collection.Iterator$$anon$13.hasNext(Iterator.scala:462) at scala.collection.Iterator$$anon$11.hasNext(Iterator.scala:409) at scala.collection.Iterator$$anon$11.hasNext(Iterator.scala:409) at scala.collection.Iterator$$anon$13.hasNext(Iterator.scala:462) at scala.collection.Iterator$$anon$11.hasNext(Iterator.scala:409) at scala.collection.Iterator$$anon$11.hasNext(Iterator.scala:409) at org.apache.spark.sql.execution.SparkPlan$$anonfun$2.apply(SparkPlan.scala:255) at org.apache.spark.sql.execution.SparkPlan$$anonfun$2.apply(SparkPlan.scala:247) at org.apache.spark.rdd.RDD$$anonfun$mapPartitionsInternal$1$$anonfun$apply$24.apply(RDD.scala:836) at org.apache.spark.rdd.RDD$$anonfun$mapPartitionsInternal$1$$anonfun$apply$24.apply(RDD.scala:836) at org.apache.spark.rdd.MapPartitionsRDD.compute(MapPartitionsRDD.scala:52) at org.apache.spark.rdd.RDD.computeOrReadCheckpoint(RDD.scala:324) at org.apache.spark.rdd.RDD.iterator(RDD.scala:288) at org.apache.spark.rdd.MapPartitionsRDD.compute(MapPartitionsRDD.scala:52) at org.apache.spark.rdd.RDD.computeOrReadCheckpoint(RDD.scala:324) at org.apache.spark.rdd.RDD.iterator(RDD.scala:288) at org.apache.spark.scheduler.ResultTask.runTask(ResultTask.scala:90) at org.apache.spark.scheduler.Task.run(Task.scala:121) at org.apache.spark.executor.Executor$TaskRunner$$anonfun$10.apply(Executor.scala:408) at org.apache.spark.util.Utils$.tryWithSafeFinally(Utils.scala:1360) at org.apache.spark.executor.Executor$TaskRunner.run(Executor.scala:414) at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) at java.lang.Thread.run(Thread.java:750) input : bytesread :  252 source : dynamicRecord :  Row(id=2, name='benjamin', surname='franklin') ``` ## Comprehensive DynamicFrame examples The following examples demonstrate various ways to create and work with DynamicFrames beyond basic Glue catalog scenarios. ### Loading from PostgreSQL with SQL SELECT query This example shows how to load data from a PostgreSQL database using a custom SQL SELECT query: ``` from awsglue.context import GlueContext from pyspark.context import SparkContext sc = SparkContext() glueContext = GlueContext(sc) # Load specific data from PostgreSQL with custom query postgres_dyf = glueContext.create_dynamic_frame.from_options( connection_type="postgresql", connection_options={ "url": "jdbc:postgresql://your-postgres-host:5432/your-database", "user": "your-username", "password": "your-password", "dbtable": "(SELECT customer_id, customer_name, email FROM customers WHERE active = true) AS filtered_customers" } ) ``` ### Loading specific columns to avoid full table scans This example demonstrates how to load only specific columns from a large database table: ``` from awsglue.context import GlueContext from pyspark.context import SparkContext sc = SparkContext() glueContext = GlueContext(sc) # Load only specific columns from a large table selected_columns_dyf = glueContext.create_dynamic_frame.from_options( connection_type="mysql", connection_options={ "url": "jdbc:mysql://your-mysql-host:3306/your-database", "user": "your-username", "password": "your-password", "dbtable": "(SELECT order_id, customer_id FROM large_orders_table) AS selected_data" } ) # Alternative approach using column selection in query efficient_load_dyf = glueContext.create_dynamic_frame.from_options( connection_type="postgresql", connection_options={ "url": "jdbc:postgresql://your-postgres-host:5432/your-database", "user": "your-username", "password": "your-password", "query": "SELECT product_id, product_name FROM products WHERE category = 'electronics'" } ) ``` ### Row-level filtering via JDBC connections This example shows how to use row-level filtering to load only specific rows from a database table: ``` from awsglue.context import GlueContext from pyspark.context import SparkContext sc = SparkContext() glueContext = GlueContext(sc) # Load filtered rows using WHERE clause filtered_rows_dyf = glueContext.create_dynamic_frame.from_options( connection_type="postgresql", connection_options={ "url": "jdbc:postgresql://your-postgres-host:5432/your-database", "user": "your-username", "password": "your-password", "dbtable": "(SELECT * FROM transactions WHERE transaction_date >= '2024-01-01' AND amount > 100) AS recent_large_transactions" } ) # Using partitionColumn for parallel loading with filtering partitioned_load_dyf = glueContext.create_dynamic_frame.from_options( connection_type="mysql", connection_options={ "url": "jdbc:mysql://your-mysql-host:3306/your-database", "user": "your-username", "password": "your-password", "dbtable": "sales_data", "partitionColumn": "sale_date", "lowerBound": "2024-01-01", "upperBound": "2024-12-31", "numPartitions": "10" } ) ``` ### Creating DynamicFrame from in-memory Python data This example demonstrates how to create a DynamicFrame from Python lists, tuples, or dictionaries: ``` from awsglue.context import GlueContext from awsglue.dynamicframe import DynamicFrame from pyspark.context import SparkContext from pyspark.sql import Row sc = SparkContext() glueContext = GlueContext(sc) # Method 1: From list of tuples data_tuples = [ ("John", "Doe", 30, "Engineer"), ("Jane", "Smith", 25, "Designer"), ("Bob", "Johnson", 35, "Manager") ] # Convert to RDD of Rows rdd = sc.parallelize([Row(first_name=row[0], last_name=row[1], age=row[2], job=row[3]) for row in data_tuples]) df = glueContext.spark_session.createDataFrame(rdd) dyf_from_tuples = DynamicFrame.fromDF(df, glueContext, "employees_from_tuples") # Method 2: From list of dictionaries data_dicts = [ {"product_id": 1, "product_name": "Laptop", "price": 999.99, "category": "Electronics"}, {"product_id": 2, "product_name": "Book", "price": 19.99, "category": "Education"}, {"product_id": 3, "product_name": "Chair", "price": 149.99, "category": "Furniture"} ] df_from_dicts = glueContext.spark_session.createDataFrame(data_dicts) dyf_from_dicts = DynamicFrame.fromDF(df_from_dicts, glueContext, "products_from_dicts") # Method 3: From nested data structures nested_data = [ { "customer_id": 1, "customer_info": { "name": "Alice Brown", "email": "alice@example.com" }, "orders": [ {"order_id": 101, "amount": 250.00}, {"order_id": 102, "amount": 175.50} ] } ] df_nested = glueContext.spark_session.createDataFrame(nested_data) dyf_nested = DynamicFrame.fromDF(df_nested, glueContext, "customers_with_orders") ``` ### Performance optimization for large datasets When working with large datasets, consider these performance optimization techniques: ``` # Use partitioning for parallel reads large_table_dyf = glueContext.create_dynamic_frame.from_options( connection_type="postgresql", connection_options={ "url": "jdbc:postgresql://your-postgres-host:5432/your-database", "user": "your-username", "password": "your-password", "dbtable": "large_table", "partitionColumn": "id", "lowerBound": "1", "upperBound": "1000000", "numPartitions": "20" } ) # Use pushdown predicates to filter at source filtered_dyf = glueContext.create_dynamic_frame.from_options( connection_type="mysql", connection_options={ "url": "jdbc:mysql://your-mysql-host:3306/your-database", "user": "your-username", "password": "your-password", "dbtable": "transactions" }, push_down_predicate="transaction_date >= '2024-01-01'" ) ``` ## errorsCount `errorsCount( )` – Returns the total number of errors in a `DynamicFrame`. ## stageErrorsCount `stageErrorsCount` – Returns the number of errors that occurred in the process of generating this `DynamicFrame`.
````
