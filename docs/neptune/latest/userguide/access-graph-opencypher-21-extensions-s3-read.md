

# neptune.read()
<a name="access-graph-opencypher-21-extensions-s3-read"></a>

 Neptune supports a `CALL` procedure `neptune.read` to read data from Amazon S3 and then run an openCypher query (read, insert, update) using the data. The procedure yields each row in the file as a declared result variable row. It uses the IAM credentials of the caller to access the data in Amazon S3. See [Managing permissions for neptune.read()](access-graph-opencypher-21-extensions-s3-read-permissions.md) to set up the permissions. The AWS region of the Amazon S3 bucket must be in the same region where instance is located. Currently, cross-region reads are not supported. 

 **Syntax** 

```
CALL neptune.read(
  {
    source: "string",
    format: "parquet/csv",
    concurrency: 10
  }
)
YIELD row
...
```

**Inputs**
+  **source** (required) - Amazon S3 URI to a **single** object. Amazon S3 prefix to multiple objects is not supported. 
+  **format** (required) - `parquet` and `csv` are supported. 
  +  More details on the supported Parquet format can be found in [Supported Parquet column types](access-graph-opencypher-21-extensions-s3-read-parquet.md#access-graph-opencypher-21-extensions-s3-read-parquet-column-types). 
  +  For more information on the supported csv format, see [Gremlin load data format](bulk-load-tutorial-format-gremlin.md). 
+  **concurrency** (optional) - Type: 0 or greater integer. Default: 0. Specifies the number of threads to be used for reading the file. If the value is 0, the maximum number of threads allowed by the resource will be used. For Parquet, it is recommended to be set to a number of row groups. 

**Outputs**

 The neptune.read returns: 
+  **row** - type:Map 
  +  Each row in the file, where the keys are the columns and the values are the data found in each column. 
  +  You can access each column's data like a property access (`row.col`). 

## Best practices for neptune.read()
<a name="access-graph-opencypher-21-extensions-s3-read-best-practices"></a>

Neptune S3 read operations can be memory-intensive. Please use instance types well-suited for production workloads as outlined in [Choosing instance types for Amazon Neptune](instance-types.md).

Memory usage and performance of `neptune.read()` requests are affected by a variety of factors like file size, number of columns, number of rows, and file format. Depending on structure, small files (e.g., CSV files 100MB or under, Parquet files 20MB or under) may work reliably on most production-suited instance types, whereas larger files may require substantial memory that smaller instance types cannot provide.

When testing this feature, it is recommended to start with small files and scale gradually to ensure your read workload can be accommodated by your instance size. If you notice `neptune.read()` requests leading to out-of-memory exceptions or instance restarts, consider splitting your files into smaller chunks, reducing file complexity, or upgrading to larger instance types.