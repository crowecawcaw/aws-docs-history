# AWS Glue PySpark transforms reference

AWS Glue provides the following built-in transforms that you can use in PySpark ETL operations. Your data passes from transform to transform in
a data structure called a _DynamicFrame_, which is an extension to an Apache
Spark SQL `DataFrame`. The `DynamicFrame` contains your data, and you
reference its schema to process your data.

Most of these transforms also exist
as methods of the `DynamicFrame` class. For more information, see [DynamicFrame transforms](aws-glue-api-crawler-pyspark-extensions-dynamic-frame.md#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-_transforms "aws-glue-api-crawler-pyspark-extensions-dynamic-frame.md#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-_transforms") .

- [GlueTransform base class](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md")
- [ApplyMapping class](aws-glue-api-crawler-pyspark-transforms-ApplyMapping.md "aws-glue-api-crawler-pyspark-transforms-ApplyMapping.md")
- [DropFields class](aws-glue-api-crawler-pyspark-transforms-DropFields.md "aws-glue-api-crawler-pyspark-transforms-DropFields.md")
- [DropNullFields class](aws-glue-api-crawler-pyspark-transforms-DropNullFields.md "aws-glue-api-crawler-pyspark-transforms-DropNullFields.md")
- [ErrorsAsDynamicFrame class](aws-glue-api-crawler-pyspark-transforms-ErrorsAsDynamicFrame.md "aws-glue-api-crawler-pyspark-transforms-ErrorsAsDynamicFrame.md")
- [EvaluateDataQuality class](aws-glue-api-crawler-pyspark-transforms-EvaluateDataQuality.md "aws-glue-api-crawler-pyspark-transforms-EvaluateDataQuality.md")
- [FillMissingValues class](aws-glue-api-crawler-pyspark-transforms-fillmissingvalues.md "aws-glue-api-crawler-pyspark-transforms-fillmissingvalues.md")
- [Filter class](aws-glue-api-crawler-pyspark-transforms-filter.md "aws-glue-api-crawler-pyspark-transforms-filter.md")
- [FindIncrementalMatches class](aws-glue-api-crawler-pyspark-transforms-findincrementalmatches.md "aws-glue-api-crawler-pyspark-transforms-findincrementalmatches.md")
- [FindMatches class](aws-glue-api-crawler-pyspark-transforms-findmatches.md "aws-glue-api-crawler-pyspark-transforms-findmatches.md")
- [FlatMap class](aws-glue-api-crawler-pyspark-transforms-flat-map.md "aws-glue-api-crawler-pyspark-transforms-flat-map.md")
- [Join class](aws-glue-api-crawler-pyspark-transforms-join.md "aws-glue-api-crawler-pyspark-transforms-join.md")
- [Map class](aws-glue-api-crawler-pyspark-transforms-map.md "aws-glue-api-crawler-pyspark-transforms-map.md")
- [MapToCollection class](aws-glue-api-crawler-pyspark-transforms-MapToCollection.md "aws-glue-api-crawler-pyspark-transforms-MapToCollection.md")
- [mergeDynamicFrame](aws-glue-api-crawler-pyspark-extensions-dynamic-frame.md#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-merge "aws-glue-api-crawler-pyspark-extensions-dynamic-frame.md#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-merge")
- [Relationalize class](aws-glue-api-crawler-pyspark-transforms-Relationalize.md "aws-glue-api-crawler-pyspark-transforms-Relationalize.md")
- [RenameField class](aws-glue-api-crawler-pyspark-transforms-RenameField.md "aws-glue-api-crawler-pyspark-transforms-RenameField.md")
- [ResolveChoice class](aws-glue-api-crawler-pyspark-transforms-ResolveChoice.md "aws-glue-api-crawler-pyspark-transforms-ResolveChoice.md")
- [SelectFields class](aws-glue-api-crawler-pyspark-transforms-SelectFields.md "aws-glue-api-crawler-pyspark-transforms-SelectFields.md")
- [SelectFromCollection class](aws-glue-api-crawler-pyspark-transforms-SelectFromCollection.md "aws-glue-api-crawler-pyspark-transforms-SelectFromCollection.md")
- [Simplify_ddb_json class](aws-glue-api-crawler-pyspark-transforms-simplify-ddb-json.md "aws-glue-api-crawler-pyspark-transforms-simplify-ddb-json.md")
- [Spigot class](aws-glue-api-crawler-pyspark-transforms-spigot.md "aws-glue-api-crawler-pyspark-transforms-spigot.md")
- [SplitFields class](aws-glue-api-crawler-pyspark-transforms-SplitFields.md "aws-glue-api-crawler-pyspark-transforms-SplitFields.md")
- [SplitRows class](aws-glue-api-crawler-pyspark-transforms-SplitRows.md "aws-glue-api-crawler-pyspark-transforms-SplitRows.md")
- [Unbox class](aws-glue-api-crawler-pyspark-transforms-Unbox.md "aws-glue-api-crawler-pyspark-transforms-Unbox.md")
- [UnnestFrame class](aws-glue-api-crawler-pyspark-transforms-UnnestFrame.md "aws-glue-api-crawler-pyspark-transforms-UnnestFrame.md")

## Data integration transforms

For AWS Glue 4.0 and above, create or update job arguments with `key: --enable-glue-di-transforms, value: true`.

Example job script:

```
from pyspark.context import SparkContext

from awsgluedi.transforms import *
sc = SparkContext()

input_df = spark.createDataFrame(
    [(5,), (0,), (-1,), (2,), (None,)],
    ["source_column"],
)

try:
    df_output = math_functions.IsEven.apply(
        data_frame=input_df,
        spark_context=sc,
        source_column="source_column",
        target_column="target_column",
        value=None,
        true_string="Even",
        false_string="Not even",
    )
    df_output.show()
except:
    print("Unexpected Error happened ")
    raise
```

Example Sessions using Notebooks

```
%idle_timeout 2880
%glue_version 4.0
%worker_type G.1X
%number_of_workers 5
%region eu-west-1
```

```
%%configure
{
    "--enable-glue-di-transforms": "true"
}
```

```
from pyspark.context import SparkContext
from awsgluedi.transforms import *

sc = SparkContext()

input_df = spark.createDataFrame(
    [(5,), (0,), (-1,), (2,), (None,)],
    ["source_column"],
)

try:
    df_output = math_functions.IsEven.apply(
        data_frame=input_df,
        spark_context=sc,
        source_column="source_column",
        target_column="target_column",
        value=None,
        true_string="Even",
        false_string="Not even",
    )
    df_output.show()
except:
    print("Unexpected Error happened ")
    raise
```

Example Sessions using AWS CLI

```
aws glue create-session --default-arguments "--enable-glue-di-transforms=true"
```

DI transforms:

- [FlagDuplicatesInColumn class](aws-glue-api-pyspark-transforms-FlagDuplicatesInColumn.md "aws-glue-api-pyspark-transforms-FlagDuplicatesInColumn.md")
- [FormatPhoneNumber class](aws-glue-api-pyspark-transforms-FormatPhoneNumber.md "aws-glue-api-pyspark-transforms-FormatPhoneNumber.md")
- [FormatCase class](aws-glue-api-pyspark-transforms-FormatCase.md "aws-glue-api-pyspark-transforms-FormatCase.md")
- [FillWithMode class](aws-glue-api-pyspark-transforms-FillWithMode.md "aws-glue-api-pyspark-transforms-FillWithMode.md")
- [FlagDuplicateRows class](aws-glue-api-pyspark-transforms-FlagDuplicateRows.md "aws-glue-api-pyspark-transforms-FlagDuplicateRows.md")
- [RemoveDuplicates class](aws-glue-api-pyspark-transforms-RemoveDuplicates.md "aws-glue-api-pyspark-transforms-RemoveDuplicates.md")
- [MonthName class](aws-glue-api-pyspark-transforms-MonthName.md "aws-glue-api-pyspark-transforms-MonthName.md")
- [IsEven class](aws-glue-api-pyspark-transforms-IsEven.md "aws-glue-api-pyspark-transforms-IsEven.md")
- [CryptographicHash class](aws-glue-api-pyspark-transforms-CryptographicHash.md "aws-glue-api-pyspark-transforms-CryptographicHash.md")
- [Decrypt class](aws-glue-api-pyspark-transforms-Decrypt.md "aws-glue-api-pyspark-transforms-Decrypt.md")
- [Encrypt class](aws-glue-api-pyspark-transforms-Encrypt.md "aws-glue-api-pyspark-transforms-Encrypt.md")
- [IntToIp class](aws-glue-api-pyspark-transforms-IntToIp.md "aws-glue-api-pyspark-transforms-IntToIp.md")
- [IpToInt class](aws-glue-api-pyspark-transforms-IpToInt.md "aws-glue-api-pyspark-transforms-IpToInt.md")

### Maven: Bundle the plugin with your Spark applications

You can bundle the transforms dependency with your Spark applications and Spark distributions (version 3.3)
by adding the plugin dependency in your Maven `pom.xml` while developing your Spark applications locally.

```
<repositories>
   ...
    <repository>
        <id>aws-glue-etl-artifacts</id>
        <url>https://aws-glue-etl-artifacts.s3.amazonaws.com/release/ </url>
    </repository>
</repositories>
...
<dependency>
    <groupId>com.amazonaws</groupId>
    <artifactId>AWSGlueTransforms</artifactId>
    <version>4.0.0</version>
</dependency>
```

You can alternatively download the binaries from AWS Glue Maven artifacts directly and include them in your Spark
application as follows.

```
#!/bin/bash
sudo wget -v https://aws-glue-etl-artifacts.s3.amazonaws.com/release/com/amazonaws/AWSGlueTransforms/4.0.0/AWSGlueTransforms-4.0.0.jar -P /usr/lib/spark/jars/
```
