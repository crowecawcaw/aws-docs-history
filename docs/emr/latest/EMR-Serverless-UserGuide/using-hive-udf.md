# Using Hive user-defined functions with

EMR Serverless

Hive user-defined functions (UDFs) let you create custom functions to process records or
groups of records. In this tutorial, you'll use a sample UDF with a pre-existing
Amazon EMR Serverless application to run a job that outputs a query result. To learn how to
set up an application, refer to [Getting started with Amazon EMR Serverless](getting-started.md "getting-started.md").

###### To use a UDF with EMR Serverless

1. Navigate to the [GitHub](https://github.com/jeromebanks/brickhouse "https://github.com/jeromebanks/brickhouse")
   for a sample UDF. Clone the repo and switch to the git branch that you want to use.
   Update the `maven-compiler-plugin` in the `pom.xml` file of the repository
   to have a source. Also update the target java version configuration to `1.8`.
   Run `mvn package -DskipTests` to create the JAR file that contains your
   sample UDFs.
2. After you create the JAR file, upload it to your S3 bucket with the following
   command.

```
aws s3 cp brickhouse-0.8.2-JS.jar s3://`amzn-s3-demo-bucket`/jars/
```

3. Create an example file to use one of the sample UDF functions. Save this query as
   `udf_example.q` and upload it to your S3 bucket.

```
add jar s3://`amzn-s3-demo-bucket`/jars/brickhouse-0.8.2-JS.jar;
CREATE TEMPORARY FUNCTION from_json AS 'brickhouse.udf.json.FromJsonUDF';
select from_json('{"key1":[0,1,2], "key2":[3,4,5,6], "key3":[7,8,9]}', map("", array(cast(0 as int))));
select from_json('{"key1":[0,1,2], "key2":[3,4,5,6], "key3":[7,8,9]}', map("", array(cast(0 as int))))["key1"][2];
```

4. Submit the following Hive job.

```
aws emr-serverless start-job-run \
  --application-id `application-id` \
  --execution-role-arn `job-role-arn` \
  --job-driver '{
    "hive": {
        "query": "s3://`amzn-s3-demo-bucket`/queries/udf_example.q",
        "parameters": "--hiveconf hive.exec.scratchdir=s3://`amzn-s3-demo-bucket`/emr-serverless-hive/scratch --hiveconf hive.metastore.warehouse.dir=s3://'$BUCKET'/emr-serverless-hive/warehouse"
    }
}' --configuration-overrides '{
    "applicationConfiguration": [{
        "classification": "hive-site",
        "properties": {
            "hive.driver.cores": "2",
            "hive.driver.memory": "6G"
        }
    }],
    "monitoringConfiguration": {
        "s3MonitoringConfiguration": {
            "logUri": "s3://`amzn-s3-demo-bucket`/logs/"
        }
    }
}'
```

5. Use the `get-job-run` command to check your job’s state. Wait for the
   state to change to `SUCCESS`.

```
aws emr-serverless get-job-run --application-id `application-id` --job-run-id `job-id`
```

6. Download the output files with the following command.

```
aws s3 cp --recursive s3://`amzn-s3-demo-bucket`/logs/applications/`application-id`/jobs/`job-id`/HIVE_DRIVER/ .
```

The `stdout.gz` file resembles the following.

```
{"key1":[0,1,2],"key2":[3,4,5,6],"key3":[7,8,9]}
2
```
