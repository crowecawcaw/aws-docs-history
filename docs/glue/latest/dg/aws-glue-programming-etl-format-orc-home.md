# Using the ORC format in AWS Glue

AWS Glue retrieves data from sources and writes data to targets stored and transported in various data formats. If your data is
stored or transported in the ORC data format, this document introduces you available features for using your
data in AWS Glue.

AWS Glue supports using the ORC format. This format is a performance-oriented, column-based data format. For
an introduction to the format by the standard authority see, [Apache Orc](https://orc.apache.org/docs/ "https://orc.apache.org/docs/").

You can use AWS Glue to read ORC files from Amazon S3 and from streaming sources as well as write ORC files to Amazon S3.
You can read and write `bzip` and `gzip` archives containing ORC files from S3. You
configure compression behavior on the [S3 connection parameters](aws-glue-programming-etl-connect-s3-home.md#aws-glue-programming-etl-connect-s3 "aws-glue-programming-etl-connect-s3-home.md#aws-glue-programming-etl-connect-s3") instead of in the configuration discussed on this
page.

The following table shows which common AWS Glue operations support the ORC format
option.

| Read      | Write     | Streaming read | Group small files | Job bookmarks |
| --------- | --------- | -------------- | ----------------- | ------------- |
| Supported | Supported | Supported      | Unsupported       | Supported\*   |

\*Supported in AWS Glue version 1.0+

## Example: Read ORC files or folders from S3

**Prerequisites:** You will need the S3 paths (`s3path`) to the
ORC files or folders that you want to read.

**Configuration:** In your function options, specify
`format="orc"`. In your `connection_options`, use the `paths` key to
specify your `s3path`. You can configure how the reader interacts with S3 in the
`connection_options`. For details, see Connection types and options for ETL in AWS Glue: [Amazon S3 connection option reference](aws-glue-programming-etl-connect-s3-home.md#aws-glue-programming-etl-connect-s3 "aws-glue-programming-etl-connect-s3-home.md#aws-glue-programming-etl-connect-s3").

The following AWS Glue ETL script shows the process of reading ORC files or folders from S3:

Python
For this example, use the [create_dynamic_frame.from_options](aws-glue-api-crawler-pyspark-extensions-glue-context.md#aws-glue-api-crawler-pyspark-extensions-glue-context-create_dynamic_frame_from_options "aws-glue-api-crawler-pyspark-extensions-glue-context.md#aws-glue-api-crawler-pyspark-extensions-glue-context-create_dynamic_frame_from_options") method.

```
from pyspark.context import SparkContext
from awsglue.context import GlueContext

sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)

dynamicFrame = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": ["s3://`s3path`"]},
    format="orc"
)
```

You can also use DataFrames in a script (`pyspark.sql.DataFrame`).

```
dataFrame = spark.read\
    .orc("s3://`s3path`")
```

Scala
For this example, use the [getSourceWithFormat](glue-etl-scala-apis-glue-gluecontext.md#glue-etl-scala-apis-glue-gluecontext-defs-getSourceWithFormat "glue-etl-scala-apis-glue-gluecontext.md#glue-etl-scala-apis-glue-gluecontext-defs-getSourceWithFormat") operation.

```
import com.amazonaws.services.glue.util.JsonOptions
import com.amazonaws.services.glue.GlueContext
import org.apache.spark.sql.SparkContext

object GlueApp {
  def main(sysArgs: Array[String]): Unit = {
    val spark: SparkContext = new SparkContext()
    val glueContext: GlueContext = new GlueContext(spark)

    val dynamicFrame = glueContext.getSourceWithFormat(
      connectionType="s3",
      format="orc",
      options=JsonOptions("""{"paths": ["s3://`s3path`"]}""")
    ).getDynamicFrame()
  }
}
```

You can also use DataFrames in a script (`pyspark.sql.DataFrame`).

```
val dataFrame = spark.read
    .orc("s3://`s3path`")
```

## Example: Write ORC files and folders to S3

**Prerequisites:** You will need an initialized DataFrame
(`dataFrame`) or DynamicFrame (`dynamicFrame`). You will also need your expected S3
output path, `s3path`.

**Configuration:**
In your function options, specify `format="orc"`. In your connection options, use the `paths` key to specify `s3path`.
You can further alter how the writer interacts with S3 in the
`connection_options`. For details, see Data format options for ETL inputs and outputs in AWS Glue: [Amazon S3 connection option reference](aws-glue-programming-etl-connect-s3-home.md#aws-glue-programming-etl-connect-s3 "aws-glue-programming-etl-connect-s3-home.md#aws-glue-programming-etl-connect-s3").
The following code example shows the process:

Python
For this example, use the [write_dynamic_frame.from_options](aws-glue-api-crawler-pyspark-extensions-glue-context.md#aws-glue-api-crawler-pyspark-extensions-glue-context-write_dynamic_frame_from_options "aws-glue-api-crawler-pyspark-extensions-glue-context.md#aws-glue-api-crawler-pyspark-extensions-glue-context-write_dynamic_frame_from_options") method.

```
from pyspark.context import SparkContext
from awsglue.context import GlueContext

sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)

glueContext.write_dynamic_frame.from_options(
    frame=`dynamicFrame`,
    connection_type="s3",
    format="orc",
    connection_options={
        "path": "s3://`s3path`"
    }
)
```

You can also use DataFrames in a script (`pyspark.sql.DataFrame`).

```
df.write.orc("s3://`s3path`/")
```

Scala
For this example, use the [getSinkWithFormat](glue-etl-scala-apis-glue-gluecontext.md#glue-etl-scala-apis-glue-gluecontext-defs-getSinkWithFormat "glue-etl-scala-apis-glue-gluecontext.md#glue-etl-scala-apis-glue-gluecontext-defs-getSinkWithFormat")
method.

```
import com.amazonaws.services.glue.util.JsonOptions
import com.amazonaws.services.glue.{DynamicFrame, GlueContext}
import org.apache.spark.SparkContext

object GlueApp {
  def main(sysArgs: Array[String]): Unit = {
    val spark: SparkContext = new SparkContext()
    val glueContext: GlueContext = new GlueContext(spark)

    glueContext.getSinkWithFormat(
      connectionType="s3",
      options=JsonOptions("""{"path": "s3://`s3path`"}"""),
      format="orc"
    ).writeDynamicFrame(`dynamicFrame`)
  }
}
```

You can also use DataFrames in a script (`pyspark.sql.DataFrame`).

```
df.write.orc("s3://`s3path`/")
```

## ORC configuration reference

There are no `format_options` values for `format="orc"`. However,
any options that are accepted by the underlying SparkSQL code can be passed to it by way of
the `connection_options` map parameter.
