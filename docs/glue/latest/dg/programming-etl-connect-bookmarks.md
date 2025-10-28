# Using job bookmarks

AWS Glue for Spark uses job bookmarks to track data that has already been processed. For a summary
of the job bookmarks feature and what it supports, see [Tracking processed data using job bookmarks](monitor-continuations.md "monitor-continuations.md"). When programming
a AWS Glue job with bookmarks, you have access to flexibility unavailable in visual jobs.

- When reading from JDBC, you can specify the column(s) to use as bookmark keys in your AWS Glue script.
- You can chose which `transformation_ctx` to apply to each method call.
  _Always call `job.init` in the beginning of the script and the `job.commit` in
  the end of the script with appropriately configured parameters_. These two functions initialize the
  bookmark service and update the state change to the service. Bookmarks won’t work without calling them.

## Specify bookmark keys

For JDBC workflows, the bookmark keeps track of which rows your job has read by comparing the values of key fields
to a bookmarked value. This is not necessary or applicable for Amazon S3 workflows.
When writing a AWS Glue script without the visual editor, you can specify which column to track with bookmarks. You can also
specify multiple columns. Gaps in the sequence of values are permitted when specifying user-defined bookmark keys.

###### Warning

If user-defined bookmarks keys are used, they must each be strictly monotonically increasing or
decreasing. When selecting additional fields for a compound key, fields for concepts like "minor
versions" or "revision numbers" do not meet this criteria, since their values are reused throughout your
dataset.

You can specify `jobBookmarkKeys` and `jobBookmarkKeysSortOrder` in
the following ways:

- `create_dynamic_frame.from_catalog` — Use
  `additional_options`.
- `create_dynamic_frame.from_options` — Use
  `connection_options`.

## Transformation context

Many of the AWS Glue PySpark dynamic frame methods include an optional parameter named
`transformation_ctx`, which is a unique identifier for the ETL operator
instance. The `transformation_ctx` parameter is used to identify state
information within a job bookmark for the given operator. Specifically, AWS Glue uses
`transformation_ctx` to index the key to the bookmark state.

###### Warning

The `transformation_ctx` serves as the key to search the bookmark state for a specific
source in your script. For the bookmark to work properly, you should always keep the source and the
associated `transformation_ctx` consistent. Changing the source property or renaming the
`transformation_ctx` may make the previous bookmark invalid and the time stamp based
filtering may not yield the correct result.

For job bookmarks to work properly, enable the job bookmark parameter and set the
`transformation_ctx` parameter. If you don't pass in the
`transformation_ctx` parameter, then job bookmarks are not enabled for a
dynamic frame or a table used in the method. For example, if you have an ETL job that reads
and joins two Amazon S3 sources, you might choose to pass the `transformation_ctx`
parameter only to those methods that you want to enable bookmarks. If you reset the job
bookmark for a job, it resets all transformations that are associated with the job
regardless of the `transformation_ctx` used.

For more information about the `DynamicFrameReader` class, see [DynamicFrameReader class](aws-glue-api-crawler-pyspark-extensions-dynamic-frame-reader.md "aws-glue-api-crawler-pyspark-extensions-dynamic-frame-reader.md"). For more
information about PySpark extensions, see [AWS Glue PySpark extensions reference](aws-glue-programming-python-extensions.md "aws-glue-programming-python-extensions.md").

## Examples

The following is an example of a generated script for an Amazon S3 data source. The portions
of the script that are required for using job bookmarks are shown in italics. For
more information about these elements see the [GlueContext class](aws-glue-api-crawler-pyspark-extensions-glue-context.md "aws-glue-api-crawler-pyspark-extensions-glue-context.md") API, and the [DynamicFrameWriter class](aws-glue-api-crawler-pyspark-extensions-dynamic-frame-writer.md "aws-glue-api-crawler-pyspark-extensions-dynamic-frame-writer.md") API.

```
# Sample Script
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session*job = Job(glueContext)
job.init(args['JOB\_NAME'], args)*

datasource0 = glueContext.create_dynamic_frame.from_catalog(
    database = "database",
    table_name = "relatedqueries_csv",
    *transformation\_ctx = "datasource0"*
)

applymapping1 = ApplyMapping.apply(
    frame = datasource0,
    mappings = [("col0", "string", "name", "string"), ("col1", "string", "number", "string")],
    *transformation\_ctx = "applymapping1"*
)

datasink2 = glueContext.write_dynamic_frame.from_options(
    frame = applymapping1,
    connection_type = "s3",
    connection_options = {"path": "s3://input_path"},
    format = "json",
    *transformation\_ctx = "datasink2"*
)

*job.commit()*
```

The following is an example of a generated script for a JDBC source. The source table is
an employee table with the `empno` column as the primary key. Although by default
the job uses a sequential primary key as the bookmark key if no bookmark key is specified,
because `empno` is not necessarily sequential—there could be gaps in the
values—it does not qualify as a default bookmark key. Therefore, the script explicitly
designates `empno` as the bookmark key. That portion of the code is shown in italics.

```
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

datasource0 = glueContext.create_dynamic_frame.from_catalog(
    database = "hr",
    table_name = "emp",
    transformation_ctx = "datasource0",
    *additional\_options = {"jobBookmarkKeys":["empno"],"jobBookmarkKeysSortOrder":"asc"}*
)

applymapping1 = ApplyMapping.apply(
    frame = datasource0,
    mappings = [("ename", "string", "ename", "string"), ("hrly_rate", "decimal(38,0)", "hrly_rate", "decimal(38,0)"), ("comm", "decimal(7,2)", "comm", "decimal(7,2)"), ("hiredate", "timestamp", "hiredate", "timestamp"), ("empno", "decimal(5,0)", "empno", "decimal(5,0)"), ("mgr", "decimal(5,0)", "mgr", "decimal(5,0)"), ("photo", "string", "photo", "string"), ("job", "string", "job", "string"), ("deptno", "decimal(3,0)", "deptno", "decimal(3,0)"), ("ssn", "decimal(9,0)", "ssn", "decimal(9,0)"), ("sal", "decimal(7,2)", "sal", "decimal(7,2)")],
    transformation_ctx = "applymapping1"
)

datasink2 = glueContext.write_dynamic_frame.from_options(
    frame = applymapping1,
    connection_type = "s3",
    connection_options = {"path": "s3://hr/employees"},
    format = "csv",
    transformation_ctx = "datasink2"
)

job.commit()
```
