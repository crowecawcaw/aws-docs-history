# Using the XML format in AWS Glue

AWS Glue retrieves data from sources and writes data to targets stored and transported in various data formats.
If your data is stored or transported in the XML data format, this document introduces you available features
for using your data in AWS Glue.

AWS Glue supports using the XML format. This format represents highly configurable, rigidly defined data
structures that aren't row or column based. XML is highly standardized. For an introduction to the format by the
standard authority, see [XML Essentials](https://www.w3.org/standards/xml/core "https://www.w3.org/standards/xml/core").

You can use AWS Glue to read XML files from Amazon S3, as well as `bzip` and `gzip` archives containing
XML files. You configure compression behavior on the [S3 connection parameters](aws-glue-programming-etl-connect-s3-home.md#aws-glue-programming-etl-connect-s3 "aws-glue-programming-etl-connect-s3-home.md#aws-glue-programming-etl-connect-s3") instead of in the configuration discussed on this
page.

The following table shows which common AWS Glue features support the XML format option.

| Read      | Write       | Streaming read | Group small files | Job bookmarks |
| --------- | ----------- | -------------- | ----------------- | ------------- |
| Supported | Unsupported | Unsupported    | Supported         | Supported     |

## Example: Read XML from S3

The XML reader takes an XML tag name. It examines elements with that tag within its input to infer a
schema and populates a DynamicFrame with corresponding values. The AWS Glue XML functionality behaves
similarly to the [XML Data Source for Apache Spark](https://github.com/databricks/spark-xml "https://github.com/databricks/spark-xml"). You might be able to
gain insight around basic behavior by comparing this reader to that project's documentation.

**Prerequisites:** You will need the S3 paths (`s3path`) to the
XML files or folders that you want to read, and some information about your XML file. You will also need the
tag for the XML element you want to read, `xmlTag`.

**Configuration:** In your function options, specify
`format="xml"`. In your `connection_options`, use the `paths` key to
specify `s3path`. You can further configure how the reader interacts with S3 in the
`connection_options`. For details, see Connection types and options for ETL in AWS Glue: [S3 connection parameters](aws-glue-programming-etl-connect-s3-home.md#aws-glue-programming-etl-connect-s3 "aws-glue-programming-etl-connect-s3-home.md#aws-glue-programming-etl-connect-s3"). In your `format_options`, use the
`rowTag` key to specify `xmlTag`. You can further configure how the reader interprets XML
files in your `format_options`. For details, see [XML Configuration Reference](#aws-glue-programming-etl-format-xml-reference "#aws-glue-programming-etl-format-xml-reference").

The following
AWS Glue ETL script shows the process of reading XML files or folders from S3.

Python
For this example, use the [create_dynamic_frame.from_options](aws-glue-api-crawler-pyspark-extensions-glue-context.md#aws-glue-api-crawler-pyspark-extensions-glue-context-create_dynamic_frame_from_options "aws-glue-api-crawler-pyspark-extensions-glue-context.md#aws-glue-api-crawler-pyspark-extensions-glue-context-create_dynamic_frame_from_options") method.

```
# Example: Read XML from S3
# Set the rowTag option to configure the reader.

from awsglue.context import GlueContext
from pyspark.context import SparkContext

sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)

dynamicFrame = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": ["s3://`s3path`"]},
    format="xml",
    format_options={"rowTag": "`xmlTag`"},
)

```

You can also use DataFrames in a script (`pyspark.sql.DataFrame`).

```
dataFrame = spark.read\
    .format("xml")\
    .option("rowTag", "`xmlTag`")\
    .load("s3://`s3path`")
```

Scala
For this example, use the [getSourceWithFormat](glue-etl-scala-apis-glue-gluecontext.md#glue-etl-scala-apis-glue-gluecontext-defs-getSourceWithFormat "glue-etl-scala-apis-glue-gluecontext.md#glue-etl-scala-apis-glue-gluecontext-defs-getSourceWithFormat") operation.

```
// Example: Read XML from S3
// Set the rowTag option to configure the reader.

import com.amazonaws.services.glue.util.JsonOptions
import com.amazonaws.services.glue.GlueContext
import org.apache.spark.sql.SparkSession

val glueContext = new GlueContext(SparkContext.getOrCreate())
val sparkSession: SparkSession = glueContext.getSparkSession

object GlueApp {
  def main(sysArgs: Array[String]): Unit = {
    val dynamicFrame = glueContext.getSourceWithFormat(
      formatOptions=JsonOptions("""{"rowTag": "`xmlTag`"}"""),
      connectionType="s3",
      format="xml",
      options=JsonOptions("""{"paths": ["s3://`s3path`"], "recurse": true}""")
    ).getDynamicFrame()
}

```

You can also use DataFrames in a script (`org.apache.spark.sql.DataFrame`).

```
val dataFrame = spark.read
  .option("rowTag", "`xmlTag`")
  .format("xml")
  .load("s3://`s3path`“)

```

## XML configuration reference

You can use the following `format_options` wherever AWS Glue libraries specify `format="xml"`:

- `rowTag` – Specifies the XML tag in the file to treat as a row. Row tags cannot
  be self-closing.
  - **Type:** Text, **Required**

- `encoding` – Specifies the character encoding. It can be the name or alias of a
  [Charset](https://docs.oracle.com/javase/8/docs/api/java/nio/charset/Charset.html "https://docs.oracle.com/javase/8/docs/api/java/nio/charset/Charset.html")
  supported by our runtime environment. We don't make specific guarantees around encoding support, but
  major encodings should work.
  - **Type:** Text, **Default:**
    `"UTF-8"`

- `excludeAttribute` – Specifies whether you want to exclude attributes in
  elements or not.
  - **Type:** Boolean, **Default:**
    `false`

- `treatEmptyValuesAsNulls` – Specifies whether to treat white space as a null
  value.
  - **Type:** Boolean, **Default:**
    `false`

- `attributePrefix` – A prefix for attributes to differentiate them from child
  element text. This prefix is used for field names.
  - **Type:** Text, **Default:**
    `"_"`

- `valueTag` – The tag used for a value when there are attributes in the element
  that have no child.
  - **Type:** Text, **Default:**
    `"_VALUE"`

- `ignoreSurroundingSpaces` – Specifies whether the white space that surrounds
  values should be ignored.
  - **Type:** Boolean, **Default:**
    `false`

- `withSchema` – Contains the expected schema, in situations where you want to
  override the inferred schema. If you don't use this option, AWS Glue infers the schema
  from the XML data.
  - **Type:** Text, **Default:** Not
    applicable
  - The value should be a JSON object that represents a
    `StructType`.

## Manually specify the XML schema

**Manual XML schema example**

This is an example of using the `withSchema` format option to specify the schema for XML
data.

```
from awsglue.gluetypes import *

schema = StructType([
  Field("id", IntegerType()),
  Field("name", StringType()),
  Field("nested", StructType([
    Field("x", IntegerType()),
    Field("y", StringType()),
    Field("z", ChoiceType([IntegerType(), StringType()]))
  ]))
])

datasource0 = create_dynamic_frame_from_options(
    connection_type,
    connection_options={"paths": ["s3://xml_bucket/someprefix"]},
    format="xml",
    format_options={"withSchema": json.dumps(schema.jsonValue())},
    transformation_ctx = ""
)
```
