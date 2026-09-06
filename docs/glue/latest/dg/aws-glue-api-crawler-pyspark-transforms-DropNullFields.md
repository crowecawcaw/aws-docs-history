

# DropNullFields class
<a name="aws-glue-api-crawler-pyspark-transforms-DropNullFields"></a>

Drops all null fields in a `DynamicFrame` whose type is `NullType`. These are fields with missing or null values in every record in the `DynamicFrame` dataset.

## Example
<a name="pyspark-DropNullFields-examples"></a>

This example uses `DropNullFields` to create a new `DynamicFrame` where fields of type `NullType` have been dropped. In order to demonstrate `DropNullFields`, we add a new column named `empty_column` with type null to the already-loaded `persons` dataset.

**Note**  
To access the dataset that is used in this example, see [Code example: Joining and relationalizing data](aws-glue-programming-python-samples-legislators.md) and follow the instructions in [Step 1: Crawl the data in the Amazon S3 bucket](aws-glue-programming-python-samples-legislators.md#aws-glue-programming-python-samples-legislators-crawling).

```
# Example: Use DropNullFields to create a new DynamicFrame without NullType fields

from pyspark.context import SparkContext
from awsglue.context import GlueContext
from pyspark.sql.functions import lit
from pyspark.sql.types import NullType
from awsglue.dynamicframe import DynamicFrame
from awsglue.transforms import DropNullFields

# Create GlueContext
sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)

# Create DynamicFrame
persons = glueContext.create_dynamic_frame.from_catalog(
    database="legislators", table_name="persons_json"
)
print("Schema for the persons DynamicFrame:")
persons.printSchema()

# Add new column "empty_column" with NullType
persons_with_nulls = persons.toDF().withColumn("empty_column", lit(None).cast(NullType()))
persons_with_nulls_dyf = DynamicFrame.fromDF(persons_with_nulls, glueContext, "persons_with_nulls")
print("Schema for the persons_with_nulls_dyf DynamicFrame:")
persons_with_nulls_dyf.printSchema()

# Remove the NullType field
persons_no_nulls = DropNullFields.apply(persons_with_nulls_dyf)
print("Schema for the persons_no_nulls DynamicFrame:")
persons_no_nulls.printSchema()
```

### Output
<a name="drop_null_fields-example-output"></a>

```
Schema for the persons DynamicFrame:
root
|-- family_name: string
|-- name: string
|-- links: array
|    |-- element: struct
|    |    |-- note: string
|    |    |-- url: string
|-- gender: string
|-- image: string
|-- identifiers: array
|    |-- element: struct
|    |    |-- scheme: string
|    |    |-- identifier: string
|-- other_names: array
|    |-- element: struct
|    |    |-- lang: string
|    |    |-- note: string
|    |    |-- name: string
|-- sort_name: string
|-- images: array
|    |-- element: struct
|    |    |-- url: string
|-- given_name: string
|-- birth_date: string
|-- id: string
|-- contact_details: array
|    |-- element: struct
|    |    |-- type: string
|    |    |-- value: string
|-- death_date: string

Schema for the persons_with_nulls_dyf DynamicFrame:
root
|-- family_name: string
|-- name: string
|-- links: array
|    |-- element: struct
|    |    |-- note: string
|    |    |-- url: string
|-- gender: string
|-- image: string
|-- identifiers: array
|    |-- element: struct
|    |    |-- scheme: string
|    |    |-- identifier: string
|-- other_names: array
|    |-- element: struct
|    |    |-- lang: string
|    |    |-- note: string
|    |    |-- name: string
|-- sort_name: string
|-- images: array
|    |-- element: struct
|    |    |-- url: string
|-- given_name: string
|-- birth_date: string
|-- id: string
|-- contact_details: array
|    |-- element: struct
|    |    |-- type: string
|    |    |-- value: string
|-- death_date: string
|-- empty_column: null

null_fields ['empty_column']
Schema for the persons_no_nulls DynamicFrame:
root
|-- family_name: string
|-- name: string
|-- links: array
|    |-- element: struct
|    |    |-- note: string
|    |    |-- url: string
|-- gender: string
|-- image: string
|-- identifiers: array
|    |-- element: struct
|    |    |-- scheme: string
|    |    |-- identifier: string
|-- other_names: array
|    |-- element: struct
|    |    |-- lang: string
|    |    |-- note: string
|    |    |-- name: string
|-- sort_name: string
|-- images: array
|    |-- element: struct
|    |    |-- url: string
|-- given_name: string
|-- birth_date: string
|-- id: string
|-- contact_details: array
|    |-- element: struct
|    |    |-- type: string
|    |    |-- value: string
|-- death_date: string
```

## Methods
<a name="aws-glue-api-crawler-pyspark-transforms-DropNullFields-_methods"></a>
+ [\_\_call\_\_](#aws-glue-api-crawler-pyspark-transforms-DropNullFields-__call__)
+ [apply](#aws-glue-api-crawler-pyspark-transforms-DropNullFields-apply)
+ [name](#aws-glue-api-crawler-pyspark-transforms-DropNullFields-name)
+ [describeArgs](#aws-glue-api-crawler-pyspark-transforms-DropNullFields-describeArgs)
+ [describeReturn](#aws-glue-api-crawler-pyspark-transforms-DropNullFields-describeReturn)
+ [describeTransform](#aws-glue-api-crawler-pyspark-transforms-DropNullFields-describeTransform)
+ [describeErrors](#aws-glue-api-crawler-pyspark-transforms-DropNullFields-describeErrors)
+ [Describe](#aws-glue-api-crawler-pyspark-transforms-DropNullFields-describe)

## \_\_call\_\_(frame, transformation\_ctx = "", info = "", stageThreshold = 0, totalThreshold = 0)
<a name="aws-glue-api-crawler-pyspark-transforms-DropNullFields-__call__"></a>

Drops all null fields in a `DynamicFrame` whose type is `NullType`. These are fields with missing or null values in every record in the `DynamicFrame` dataset.
+ `frame` – The `DynamicFrame` to drop null fields in (required).
+ `transformation_ctx` – A unique string that is used to identify state information (optional).
+ `info` – A string associated with errors in the transformation (optional).
+ `stageThreshold` – The maximum number of errors that can occur in the transformation before it errors out (optional). The default is zero.
+ `totalThreshold` – The maximum number of errors that can occur overall before processing errors out (optional). The default is zero.

Returns a new `DynamicFrame` with no null fields.

## apply(cls, \*args, \*\*kwargs)
<a name="aws-glue-api-crawler-pyspark-transforms-DropNullFields-apply"></a>
+ `cls` – cls

## name(cls)
<a name="aws-glue-api-crawler-pyspark-transforms-DropNullFields-name"></a>
+ `cls` – cls

## describeArgs(cls)
<a name="aws-glue-api-crawler-pyspark-transforms-DropNullFields-describeArgs"></a>
+ `cls` – cls

## describeReturn(cls)
<a name="aws-glue-api-crawler-pyspark-transforms-DropNullFields-describeReturn"></a>
+ `cls` – cls

## describeTransform(cls)
<a name="aws-glue-api-crawler-pyspark-transforms-DropNullFields-describeTransform"></a>
+ `cls` – cls

## describeErrors(cls)
<a name="aws-glue-api-crawler-pyspark-transforms-DropNullFields-describeErrors"></a>
+ `cls` – cls

## describe(cls)
<a name="aws-glue-api-crawler-pyspark-transforms-DropNullFields-describe"></a>
+ `cls` – cls