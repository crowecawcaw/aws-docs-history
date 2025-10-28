# Using Delta Lake OSS with EMR Serverless

## Amazon EMR versions 6.9.0 and higher

###### Note

Amazon EMR 7.0.0 and higher uses Delta Lake 3.0.0, which renames the `delta-core.jar`
file to `delta-spark.jar`. If you use Amazon EMR 7.0.0 or higher, make sure to
specify `delta-spark.jar` in your configurations.

Amazon EMR 6.9.0 and higher includes Delta Lake, so you no longer have to package Delta Lake
yourself or provide the `--packages` flag with your EMR Serverless jobs.

1. When you submit EMR Serverless jobs, make sure that you have the following configuration properties and include
   the following parameters in the `sparkSubmitParameters` field.

```
--conf spark.jars=/usr/share/aws/delta/lib/delta-core.jar,/usr/share/aws/delta/lib/delta-storage.jar
    --conf spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension
    --conf spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog
```

2. Create a local `delta_sample.py` to test creating and reading a Delta table.

```
# delta_sample.py
    from pyspark.sql import SparkSession

    import uuid

    url = "s3://`amzn-s3-demo-bucket`/delta-lake/output/%s/" % str(uuid.uuid4())
    spark = SparkSession.builder.appName("DeltaSample").getOrCreate()

    ## creates a Delta table and outputs to target S3 bucket
    spark.range(5).write.format("delta").save(url)

    ## reads a Delta table and outputs to target S3 bucket
    spark.read.format("delta").load(url).show
```

3. Using the AWS CLI, upload the `delta_sample.py` file to your
   Amazon S3 bucket. Then use the `start-job-run` command to submit a job to an existing EMR Serverless
   application.

```
aws s3 cp delta_sample.py s3://`amzn-s3-demo-bucket`/code/

    aws emr-serverless start-job-run \
        --application-id `application-id` \
        --execution-role-arn `job-role-arn` \
        --name emr-delta \
        --job-driver '{
            "sparkSubmit": {
                "entryPoint": "s3://`amzn-s3-demo-bucket`/code/delta_sample.py",
                "sparkSubmitParameters": "--conf spark.jars=/usr/share/aws/delta/lib/delta-core.jar,/usr/share/aws/delta/lib/delta-storage.jar --conf spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension --conf spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog"
            }
        }'
```

To use Python libraries with Delta Lake, add the `delta-core` library by [packaging it as a dependency](using-python-libraries.md "using-python-libraries.md") or by [using it as a custom image](using-custom-images.md "using-custom-images.md").

Alternatively, you can use the `SparkContext.addPyFile` to add the Python libraries from the `delta-core` JAR file:

```
import glob
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.addPyFile(glob.glob("/usr/share/aws/delta/lib/delta-core_*.jar")[0])
```

## Amazon EMR versions 6.8.0 and lower

If you're using Amazon EMR 6.8.0 or lower, follow these steps to use Delta Lake OSS with your EMR Serverless applications.

1. To build an open source version of [Delta
   Lake](https://delta.io/ "https://delta.io/") that’s compatible with the version of Spark on your
   Amazon EMR Serverless application, navigate to the [Delta GitHub](https://github.com/delta-io/delta "https://github.com/delta-io/delta") and follow the
   instructions.
2. Upload the Delta Lake libraries to an Amazon S3 bucket in your AWS account.
3. When you submit EMR Serverless jobs in the application configuration, include the
   Delta Lake JAR files that are now in your bucket.

```
--conf spark.jars=s3://`amzn-s3-demo-bucket`/jars/delta-core_2.12-1.1.0.jar
```

4. To ensure that you can read to and write from a Delta table, run a sample PySpark
   test.

```
from pyspark import SparkConf, SparkContext
    from pyspark.sql import HiveContext, SparkSession

    import uuid

    conf = SparkConf()
    sc = SparkContext(conf=conf)
    sqlContext = HiveContext(sc)

    url = "s3://`amzn-s3-demo-bucket`/delta-lake/output/1.0.1/%s/" % str(uuid.uuid4())

    ## creates a Delta table and outputs to target S3 bucket
    session.range(5).write.format("delta").save(url)

    ## reads a Delta table and outputs to target S3 bucket
    session.read.format("delta").load(url).show
```
