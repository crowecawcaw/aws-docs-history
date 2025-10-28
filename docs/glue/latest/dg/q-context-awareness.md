# Using context awareness with Amazon Q Data Integration in AWS Glue

You can now create data processing jobs more efficiently with query based context-aware and PySpark DataFrame code generation in
Amazon Q Data Integration. For example, you can use this prompt to generate PySpark code: “create a job to load sales data from
Redshift table ‘analytics.salesorder’ using connection ‘erp_conn’, filter order_amount below 50 dollars, and save to Amazon S3 in parquet
format.”

Amazon Q will generate the script based on your prompt and setup data integration workflow setup with the details provided from your
question, such as connection configurations, schema details, database/table names, and column specifications for transformations.
Sensitive information, such as connection option passwords, continue to be redacted.

If required information is not provided from your prompt, Amazon Q will put placeholders, which you have to update the generated code
with the appropriate values before running the code.

The following are examples on how to use context awareness.

## Example: interactions

Prompt: `Create an AWS Glue spark job that reads a file s3://amzn-s3-demo-bucket-input-bucket-name/input-filename.csv and 
 saves it into the parquet file under directory s3://amzn-s3-demo-bucket-output-bucket-name/output-s3-prefix/`

```
import sys
from awsglue.transforms import *
from pyspark.context import SparkContext
from pyspark.sql import SparkSession

sc = SparkContext.getOrCreate()
spark = SparkSession.builder.getOrCreate()

# Script generated for node S3DataSource
S3DataSource_dsource1 = spark.read.format("csv").load(
    "s3://amzn-s3-demo-bucket-input-bucket-name/input-filename.csv"
)

# Script generated for node S3DataSink
S3DataSource_dsource1.write.format("parquet").mode("append").save(
    "s3://amzn-s3-demo-bucket-output-bucket-name/output-s3-prefix/"
)
```

![An example of asking Amazon Q data integration in AWS Glue for a generated ETL script.](/images/glue/latest/dg/images/context-awareness-lakehouse-example.gif)

Prompt: `write an ETL script to read from a Lakehouse table my-table in database my-database and write it to a RDS MySQL table 
 my-target-table`

For fields where you did not provide information (for example, the connectionName required is for MySQL data sink and default
with a placehoder <connection-name> in the generated code), a placeholder is kept for you to fill in the required
information before run the script.

Generated script:

```
import sys
from awsglue.transforms import *
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from connectivity.adapter import CatalogConnectionHelper

sc = SparkContext.getOrCreate()
spark = SparkSession.builder.getOrCreate()

# Script generated for node S3DataSource
S3DataSource_dsource1 = spark.read.format("parquet").load(
    "s3://amzn-lakehouse-demo-bucket/my-database/my-table"
)

# Script generated for node ConnectionV2DataSink
ConnectionV2DataSink_dsink1_additional_options = {"dbtable": "my-target-table"}
CatalogConnectionHelper(spark).write(
    S3DataSource_dsource1,
    "mysql",
    "<connection-name>",
    ConnectionV2DataSink_dsink1_additional_options,
)

```

![An example of asking Amazon Q data integration in AWS Glue for a generated ETL script.](/images/glue/latest/dg/images/context-awareness-example-interactions.gif)

The following example demonstrates how you can ask AWS Glue to create a AWS Glue script to complete a full ETL workflow with the following
prompt: `Create a AWS Glue ETL Script read from two AWS Glue Data Catalog tables venue and event in my database 
 glue_db_4fthqih3vvk1if, join the results on the field venueid, filter on venue state with condition as venuestate=='DC' 
 after joining the results and write output to an Amazon S3 S3 location s3://amz-s3-demo-bucket/output/ in CSV format`.

The workflow contains reading from different data sources (two AWS Glue Data Catalog tables), and a couple of transforms after the
reading by join the result from two readings, filter based on some condition and write the transformed output to an Amazon S3
destination in CSV format.

The generated job will fill in the detailed information to the data source, transform and sink operation with corresponding
information extracted from user question as below.

```

import sys
from awsglue.transforms import *
from pyspark.context import SparkContext
from pyspark.sql import SparkSession

sc = SparkContext.getOrCreate()
spark = SparkSession.builder.getOrCreate()

# Script generated for node CatalogDataSource
CatalogDataSource_dsource1 = spark.sql("select * from `glue_db_4fthqih3vvk1if`.`venue`")

# Script generated for node CatalogDataSource
CatalogDataSource_dsource2 = spark.sql("select * from `glue_db_4fthqih3vvk1if`.`event`")

# Script generated for node JoinTransform
JoinTransform_transform1 = CatalogDataSource_dsource1.join(
    CatalogDataSource_dsource2,
    (CatalogDataSource_dsource1["venueid"] == CatalogDataSource_dsource2["venueid"]),
    "inner",
)

# Script generated for node FilterTransform
FilterTransform_transform2 = JoinTransform_transform1.filter("venuestate=='DC'")

# Script generated for node S3DataSink
FilterTransform_transform2.write.format("csv").mode("append").save(
    "s3://amz-s3-demo-bucket/output//output/"
)
```

![An example of asking Amazon Q data integration in AWS Glue for a generated ETL script.](/images/glue/latest/dg/images/context-awareness-complex-example.gif)

##

Limitations

- Context carryover:
  - The context-awareness feature only carries over context from the previous user query within the same conversation.
    It does not retain context beyond the immediate preceding query.

- Support for node configurations:
  - Currently, context-awareness supports only a subset of required configurations for various nodes.
  - Support for optional fields is planned in upcoming releases.

- Availability:
  - Context-awareness and DataFrame support are available in Q Chat and SageMaker Unified Studio notebooks.
    However, these features are not yet available in AWS Glue Studio notebooks.
