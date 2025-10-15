# Running ETL jobs on Amazon S3 tables with
 AWS Glue

AWS Glue is a serverless data integration service that makes it easy for analytics users to
 discover, prepare, move, and integrate data from multiple sources. You can use AWS Glue jobs to
 run extract, transform, and load (ETL) pipelines to load data into your data lakes. For more
 information about AWS Glue, see [What is AWS Glue?](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html "https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html") in the *AWS Glue
 Developer Guide*.

An AWS Glue job encapsulates a script that connects to your source data, processes it, and
 then writes it out to your data target. Typically, a job runs extract, transform, and load
 (ETL) scripts. Jobs can run scripts designed for Apache Spark runtime
 environments. You can monitor job runs to understand runtime metrics such as completion
 status, duration, and start time.

You can use AWS Glue jobs to process data in your S3 tables by connecting to your tables
 through the integration with AWS analytics services, or, connect directly using the
 Amazon S3 Tables Iceberg REST endpoint or the Amazon S3 Tables Catalog for Apache Iceberg. This guide covers the basic steps to get
 started using AWS Glue with S3 Tables, including:

###### Topics

* [Step 1 – Prerequisites](#glue-etl-prereqs "#glue-etl-prereqs")
* [Step 2 – Create a script to connect to
 table buckets](#glue-etl-script "#glue-etl-script")
* [Step 3 – Create a AWS Glue job that queries tables](#glue-etl-job "#glue-etl-job")
Choose your access method based on your specific AWS Glue ETL job requirements:


* **AWS analytics services integration (Recommended)** – 
 Recommended when you need centralized metadata management across multiple AWS analytics services, 
 need to leverage existing AWS Glue Data Catalog permissions and fine-grained access control with Lake Formation, or are building production ETL pipelines that integrate with other AWS services like Athena or Amazon EMR.
* **Amazon S3 Tables Iceberg REST endpoint** – 
 Recommended when you need to connect to S3 tables from third-party query engines that support Apache Iceberg, 
 build custom ETL applications that need direct REST API access, or when you require control over catalog operations without dependencies on AWS Glue Data Catalog.
* **Amazon S3 Tables Catalog for Apache Iceberg** – 
 Use only for legacy applications or specific programmatic scenarios that require the Java client library. 
 This method is not recommended for new AWS Glue ETL job implementations due to additional `JAR` 
 dependency management and complexity.
###### Note

S3 Tables is supported on [AWS Glue version 5.0 or higher](https://docs.aws.amazon.com/glue/latest/dg/release-notes.html "https://docs.aws.amazon.com/glue/latest/dg/release-notes.html").


## Step 1 – Prerequisites


Before you can query tables from a AWS Glue job you must configure an IAM role that
 AWS Glue can use to run the job. Choose your method of access to see specific prerequisites for that method.



AWS analytics services integration (Recommended)
Prerequisites required to use the S3 Tables AWS analytics integration to run AWS Glue jobs.



* [Integrate your table buckets with
 AWS analytics services](s3-tables-integrating-aws.md "s3-tables-integrating-aws.md").
* [Create an IAM role for AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/create-an-iam-role.html "https://docs.aws.amazon.com/glue/latest/dg/create-an-iam-role.html").




	+ Attach the `AmazonS3TablesFullAccess` managed policy to the
	 role.
	+ Attach the `AmazonS3FullAccess` managed policy to the
	 role.


Amazon S3 Tables Iceberg REST endpoint
Prerequisites to use the Amazon S3 Tables Iceberg REST endpoint to run AWS Glue ETL jobs.



* [Create an IAM role for AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/create-an-iam-role.html "https://docs.aws.amazon.com/glue/latest/dg/create-an-iam-role.html").




	+ Attach the `AmazonS3TablesFullAccess` managed policy to the
	 role.
	+ Attach the `AmazonS3FullAccess` managed policy to the
	 role.


Amazon S3 Tables Catalog for Apache Iceberg
Prerequisites use the Amazon S3 Tables Catalog for Apache Iceberg to run AWS Glue ETL jobs.



* [Create an IAM role for AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/create-an-iam-role.html "https://docs.aws.amazon.com/glue/latest/dg/create-an-iam-role.html").




	+ Attach the `AmazonS3TablesFullAccess` managed policy to the
	 role.
	+ Attach the `AmazonS3FullAccess` managed policy to the
	 role.
	+ To use the Amazon S3 Tables Catalog for Apache Iceberg you need to download
	 the client catalog JAR and upload it to an S3 bucket.
	
	
	###### **Downloading the catalog
	 JAR**
	
	
		1. Check for the latest version on [Maven Central](https://mvnrepository.com/artifact/software.amazon.s3tables/s3-tables-catalog-for-iceberg-runtime "https://mvnrepository.com/artifact/software.amazon.s3tables/s3-tables-catalog-for-iceberg-runtime"). You can download the JAR from
		 Maven central using your browser, or using the following command. Make
		 sure to replace the `version number` with the
		 latest version.
		
		
		
		```
		wget https://repo1.maven.org/maven2/software/amazon/s3tables/s3-tables-catalog-for-iceberg-runtime/`0.1.5`/s3-tables-catalog-for-iceberg-runtime-`0.1.5.jar`                       
		```
		2. Upload the downloaded JAR to an S3 bucket that your
		 AWS Glue IAM role can access. You can use the following AWS CLI command to
		 upload the JAR. Make sure to replace the
		 `version number` with the latest version,
		 and the `bucket name` and
		 `path` with your own.
		
		
		
		```
		aws s3 cp s3-tables-catalog-for-iceberg-runtime-`0.1.5`.jar s3://`amzn-s3-demo-bucket``/jars/`
		```



## Step 2 – Create a script to connect to
 table buckets


To access your table data when you run an AWS Glue ETL job, you configure a
 Spark session for Apache Iceberg that connects to your
 S3 table bucket. You can modify an existing script to connect to your table bucket or
 create a new script. For more information on creating AWS Glue scripts, see [Tutorial: Writing an AWS Glue for Spark script](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-intro-tutorial.html "https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-intro-tutorial.html") in the *AWS Glue
 Developer Guide*.


You can configure the session to connect to your table buckets through the any of the
 following S3 Tables access methods:



* S3 Tables AWS analytics services integration (Recommended)
* Amazon S3 Tables Iceberg REST endpoint
* Amazon S3 Tables Catalog for Apache Iceberg

Choose from the following access methods to view setup instructions and configuration
 examples.



AWS analytics services integration (Recommended)
As a prerequisites to query tables with Spark on AWS Glue
 using the AWS analytics services integration, you must [Integrate your table buckets with
 AWS analytics services](s3-tables-integrating-aws.md "s3-tables-integrating-aws.md")


You can configure the connection to your table bucket through a
 Spark session in a job or with AWS Glue Studio magics in an
 interactive session. To use the following examples, replace the
 `placeholder values` with the information for
 your own table bucket.




**Using a PySpark script**

Use the following code snippet in a PySpark
 script to configure a AWS Glue job to connect to your table bucket
 using the integration.



```
spark = SparkSession.builder.appName("SparkIcebergSQL") \
    .config("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions") \
    .config("spark.sql.defaultCatalog","s3tables") \
    .config("spark.sql.catalog.s3tables", "org.apache.iceberg.spark.SparkCatalog") \
    .config("spark.sql.catalog.s3tables.catalog-impl", "org.apache.iceberg.aws.glue.GlueCatalog") \
    .config("spark.sql.catalog.s3tables.glue.id", "`111122223333`:s3tablescatalog/`amzn-s3-demo-table-bucket`") \
    .config("spark.sql.catalog.s3tables.warehouse", "s3://`amzn-s3-demo-table-bucket`/warehouse/") \
    .getOrCreate()                                    
```


**Using an interactive AWS Glue
 session**

If you are using an interactive notebook session with AWS Glue
 5.0, specify the same configurations using the
 `%%configure` magic in a cell prior to code
 execution.



```
%%configure
{"conf": "spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions --conf spark.sql.defaultCatalog=s3tables --conf spark.sql.catalog.s3tables=org.apache.iceberg.spark.SparkCatalog --conf spark.sql.catalog.s3tables.catalog-impl=org.apache.iceberg.aws.glue.GlueCatalog --conf spark.sql.catalog.s3tables.glue.id=`111122223333`:s3tablescatalog/`amzn-s3-demo-table-bucket` --conf spark.sql.catalog.s3tables.warehouse=s3://`amzn-s3-demo-table-bucket`/warehouse/"}
```




Amazon S3 Tables Iceberg REST endpoint
You can configure the connection to your table bucket through a
 Spark session in a job or with AWS Glue Studio magics in an
 interactive session. To use the following examples, replace the
 `placeholder values` with the information for
 your own table bucket.




**Using a PySpark script**
Use the following code snippet in a PySpark script
 to configure a AWS Glue job to connect to your table bucket using the
 endpoint. 



```
spark = SparkSession.builder.appName("glue-s3-tables-rest") \
    .config("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions") \
    .config("spark.sql.defaultCatalog", "s3_rest_catalog") \
    .config("spark.sql.catalog.s3_rest_catalog", "org.apache.iceberg.spark.SparkCatalog") \
    .config("spark.sql.catalog.s3_rest_catalog.type", "rest") \
    .config("spark.sql.catalog.s3_rest_catalog.uri", "https://s3tables.`Region`.amazonaws.com/iceberg") \
    .config("spark.sql.catalog.s3_rest_catalog.warehouse", "arn:aws:s3tables:`Region`:`111122223333`:bucket/`amzn-s3-demo-table-bucket`") \
    .config("spark.sql.catalog.s3_rest_catalog.rest.sigv4-enabled", "true") \
    .config("spark.sql.catalog.s3_rest_catalog.rest.signing-name", "s3tables") \
    .config("spark.sql.catalog.s3_rest_catalog.rest.signing-region", "`Region`") \
    .config('spark.sql.catalog.s3_rest_catalog.io-impl','org.apache.iceberg.aws.s3.S3FileIO') \
    .config('spark.sql.catalog.s3_rest_catalog.rest-metrics-reporting-enabled','false') \
    .getOrCreate()                                    
```


**Using an interactive AWS Glue
 session**
If you are using an interactive notebook session with AWS Glue 5.0,
 specify the same configurations using the `%%configure`
 magic in a cell prior to code execution. Replace the placeholder
 values with the information for your own table bucket.



```
%%configure
{"conf": "spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions --conf spark.sql.defaultCatalog=s3_rest_catalog --conf spark.sql.catalog.s3_rest_catalog=org.apache.iceberg.spark.SparkCatalog --conf spark.sql.catalog.s3_rest_catalog.type=rest --conf spark.sql.catalog.s3_rest_catalog.uri=https://s3tables.`Region`.amazonaws.com/iceberg --conf spark.sql.catalog.s3_rest_catalog.warehouse=arn:aws:s3tables:`Region`:`111122223333`:bucket/`amzn-s3-demo-table-bucket` --conf spark.sql.catalog.s3_rest_catalog.rest.sigv4-enabled=true --conf spark.sql.catalog.s3_rest_catalog.rest.signing-name=s3tables --conf spark.sql.catalog.s3_rest_catalog.rest.signing-region=`Region` --conf spark.sql.catalog.s3_rest_catalog.io-impl=org.apache.iceberg.aws.s3.S3FileIO --conf spark.sql.catalog.s3_rest_catalog.rest-metrics-reporting-enabled=false"}
```




Amazon S3 Tables Catalog for Apache Iceberg
As a prerequisite to connecting to tables using the
 Amazon S3 Tables Catalog for Apache Iceberg you must first download the latest catalog jar and
 upload it to an S3 bucket. Then, when you create your job, you add the
 the path to the client catalog JAR as a special parameter. For more information on job parameters
 in AWS Glue, see [Special parameters used in AWS Glue jobs](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html "https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html") in the
 *AWS Glue Developer Guide*.


You can configure the connection to your table bucket through a
 Spark session in a job or with AWS Glue Studio magics in an
 interactive session. To use the following examples, replace the
 `placeholder values` with the information for
 your own table bucket.




**Using a PySpark script**

Use the following code snippet in a PySpark script
 to configure a AWS Glue job to connect to your table bucket using the
 JAR. Replace the placeholder values with the
 information for your own table bucket.



```
spark = SparkSession.builder.appName("glue-s3-tables") \
    .config("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions") \
    .config("spark.sql.defaultCatalog", "s3tablesbucket") \
    .config("spark.sql.catalog.s3tablesbucket", "org.apache.iceberg.spark.SparkCatalog") \
    .config("spark.sql.catalog.s3tablesbucket.catalog-impl", "software.amazon.s3tables.iceberg.S3TablesCatalog") \
    .config("spark.sql.catalog.s3tablesbucket.warehouse", "arn:aws:s3tables:`Region`:111122223333:bucket/`amzn-s3-demo-table-bucket`") \
    .getOrCreate()                                
```

**Using an interactive AWS Glue
 session**

If you are using an interactive notebook session with AWS Glue 5.0,
 specify the same configurations using the `%%configure`
 magic in a cell prior to code execution. Replace the placeholder
 values with the information for your own table bucket.



```
%%configure
{"conf": "spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions --conf spark.sql.defaultCatalog=s3tablesbucket --conf spark.sql.catalog.s3tablesbucket=org.apache.iceberg.spark.SparkCatalog --conf spark.sql.catalog.s3tablesbucket.catalog-impl=software.amazon.s3tables.iceberg.S3TablesCatalog --conf spark.sql.catalog.s3tablesbucket.warehouse=arn:aws:s3tables:`Region`:111122223333:bucket/`amzn-s3-demo-table-bucket`", "extra-jars": "s3://`amzn-s3-demo-bucket`/jars/s3-tables-catalog-for-iceberg-runtime-`0.1.5`.jar"}
```




### Sample scripts


The following example PySpark scripts can be used to test querying
 S3 tables with an AWS Glue job. These scripts connect to your table bucket and runs
 queries to: create a new namespace, create a sample table, insert data into the
 table, and return the table data. To use the scripts, replace the
 `placeholder values` with the information for you own
 table bucket.


Choose from the following scripts based on your S3 Tables access method.



S3 Tables integration with AWS analytics services

```
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SparkIcebergSQL") \
    .config("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions") \
    .config("spark.sql.defaultCatalog","s3tables")
    .config("spark.sql.catalog.s3tables", "org.apache.iceberg.spark.SparkCatalog") \
    .config("spark.sql.catalog.s3tables.catalog-impl", "org.apache.iceberg.aws.glue.GlueCatalog") \
    .config("spark.sql.catalog.s3tables.glue.id", "`111122223333`:s3tablescatalog/`amzn-s3-demo-table-bucket`") \
    .config("spark.sql.catalog.s3tables.warehouse", "s3://`amzn-s3-demo-table-bucket`/bucket/`amzn-s3-demo-table-bucket`") \
    .getOrCreate()

namespace = "`new_namespace`"
table = "`new_table`"

spark.sql("SHOW DATABASES").show()

spark.sql(f"DESCRIBE NAMESPACE {namespace}").show()

spark.sql(f"""
    CREATE TABLE IF NOT EXISTS {namespace}.{table} (
       id INT,
       name STRING,
       value INT
    )
""")

spark.sql(f"""
    INSERT INTO {namespace}.{table}
    VALUES 
       (1, 'ABC', 100),
       (2, 'XYZ', 200)
""")

spark.sql(f"SELECT * FROM {namespace}.{table} LIMIT 10").show()
```


Amazon S3 Tables Iceberg REST endpoint

```
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("glue-s3-tables-rest") \
    .config("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions") \
    .config("spark.sql.defaultCatalog", "s3_rest_catalog") \
    .config("spark.sql.catalog.s3_rest_catalog", "org.apache.iceberg.spark.SparkCatalog") \
    .config("spark.sql.catalog.s3_rest_catalog.type", "rest") \
    .config("spark.sql.catalog.s3_rest_catalog.uri", "https://s3tables.`Region`.amazonaws.com/iceberg") \
    .config("spark.sql.catalog.s3_rest_catalog.warehouse", "arn:aws:s3tables:`Region`:`111122223333`:bucket/`amzn-s3-demo-table-bucket`") \
    .config("spark.sql.catalog.s3_rest_catalog.rest.sigv4-enabled", "true") \
    .config("spark.sql.catalog.s3_rest_catalog.rest.signing-name", "s3tables") \
    .config("spark.sql.catalog.s3_rest_catalog.rest.signing-region", "`Region`") \
    .config('spark.sql.catalog.s3_rest_catalog.io-impl','org.apache.iceberg.aws.s3.S3FileIO') \
    .config('spark.sql.catalog.s3_rest_catalog.rest-metrics-reporting-enabled','false') \
    .getOrCreate()

namespace = "`s3_tables_rest_namespace`"
table = "`new_table_s3_rest`"

spark.sql("SHOW DATABASES").show()

spark.sql(f"DESCRIBE NAMESPACE {namespace}").show()

spark.sql(f"""
    CREATE TABLE IF NOT EXISTS {namespace}.{table} (
       id INT,
       name STRING,
       value INT
    )
""")

spark.sql(f"""
    INSERT INTO {namespace}.{table}
    VALUES 
       (1, 'ABC', 100),
       (2, 'XYZ', 200)
""")

spark.sql(f"SELECT * FROM {namespace}.{table} LIMIT 10").show()

            
```


Amazon S3 Tables Catalog for Apache Iceberg

```
from pyspark.sql import SparkSession

#Spark session configurations
spark = SparkSession.builder.appName("glue-s3-tables") \
    .config("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions") \
    .config("spark.sql.defaultCatalog", "s3tablesbucket") \
    .config("spark.sql.catalog.s3tablesbucket", "org.apache.iceberg.spark.SparkCatalog") \
    .config("spark.sql.catalog.s3tablesbucket.catalog-impl", "software.amazon.s3tables.iceberg.S3TablesCatalog") \
    .config("spark.sql.catalog.s3tablesbucket.warehouse", "arn:aws:s3tables:`Region`:`111122223333`:bucket/`amzn-s3-demo-table-bucket`") \
    .getOrCreate()

#Script
namespace = "`new_namespace`"
table = "`new_table`"

spark.sql(f"CREATE NAMESPACE IF NOT EXISTS s3tablesbucket.{namespace}")
spark.sql(f"DESCRIBE NAMESPACE {namespace}").show()

spark.sql(f"""
    CREATE TABLE IF NOT EXISTS {namespace}.{table} (
       id INT,
       name STRING,
       value INT
    )
""")

spark.sql(f"""
    INSERT INTO {namespace}.{table}
    VALUES 
       (1, 'ABC', 100),
       (2, 'XYZ', 200)
""")

spark.sql(f"SELECT * FROM {namespace}.{table} LIMIT 10").show()
```



## Step 3 – Create a AWS Glue job that queries tables


The following procedures show how to setup AWS Glue jobs that connect to your S3 table
 buckets. You can do this using the AWS CLI or using the console with AWS Glue Studio script editor.
 For more information, see [Authoring jobs in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/author-job-glue.html "https://docs.aws.amazon.com/glue/latest/dg/author-job-glue.html") in the
 *AWS Glue User Guide*.


The following procedure shows how to use the AWS Glue Studio script editor to create an
 ETL job that queries your S3 tables.


###### Prerequisites


* [Step 1 – Prerequisites](#glue-etl-prereqs "#glue-etl-prereqs")
* [Step 2 – Create a script to connect to
 table buckets](#glue-etl-script "#glue-etl-script")
1. Open the AWS Glue console at
 [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/ "https://console.aws.amazon.com/glue/").
2. From the Navigation pane, choose **ETL jobs**.
3. Choose **Script editor**, then choose
 **Upload script** and upload the
 PySpark script you created to query S3 tables.
4. Select the **Job details** tab and enter the
 following for **Basic properties**.




	* For **Name**, enter a name for the
	 job.
	* For **IAM Role**, select the role you created
	 for AWS Glue.
5. (Optional) If you are using the Amazon S3 Tables Catalog for Apache Iceberg access method,
 expand **Advanced properties** and for
 **Dependent JARs path**, enter the S3 URI of the
 client catalog jar your uploaded to an S3 bucket as a prerequisite. For
 example,
 s3://`amzn-s3-demo-bucket1`/`jars`/s3-tables-catalog-for-iceberg-runtime-`0.1.5`.jar
6. Choose **Save** to create the job.
7. Choose **Run** start the job, and review the job
 status under the **Runs** tab.

The following procedure shows how to use the AWS CLI to create an ETL job that
 queries your S3 tables. To use the commands replace the `placeholder
 values` with your own.


###### Prerequisites


* [Step 1 – Prerequisites](#glue-etl-prereqs "#glue-etl-prereqs")
* [Step 2 – Create a script to connect to
 table buckets](#glue-etl-script "#glue-etl-script") and
 upload it to an S3 bucket.
1. Create an AWS Glue job.



```
aws glue create-job \
--name `etl-tables-job` \
--role arn:aws:iam::`111122223333`:role/`AWSGlueServiceRole` \
--command '{
    "Name": "glueetl",
    "ScriptLocation": "s3://`amzn-s3-demo-bucket1``/scripts/glue-etl-query.py`",
    "PythonVersion": "3"
}' \
--default-arguments '{
    "--job-language": "python",
    "--class": "GlueApp"
}' \
--glue-version "5.0"
```

###### Note

(Optional) If you are using the Amazon S3 Tables Catalog for Apache Iceberg access method, add the client catalog JAR to the `--default-arguments` using the `--extra-jars` parameter. Replace the `input placeholders` with your own when you add the parameter.


```

                            "--extra-jars": "s3://`amzn-s3-demo-bucket`/`jar-path`/s3-tables-catalog-for-iceberg-runtime-`0.1.5`.jar" 
```
2. Start your job.



```
aws glue start-job-run \
--job-name `etl-tables-job`
```
3. To review you job status, copy the run ID from the previous command
 and enter it into the following command.



```
aws glue get-job-run --job-name `etl-tables-job` \
--run-id `jr_ec9a8a302e71f8483060f87b6c309601ea9ee9c1ffc2db56706dfcceb3d0e1ad`
```
