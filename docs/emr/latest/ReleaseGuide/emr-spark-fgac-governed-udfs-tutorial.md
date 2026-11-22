

# Tutorial: Create and run your first governed UDF

In this tutorial, you create a Hive UDF that changes text to uppercase. You register it as a governed UDF, call it from a query, and then call it from an RLS policy. The examples use EMR Serverless. The table after the steps shows the changes for other platforms.

Before you start, make sure that you have these resources:
+ An Amazon S3 location that you registered with Lake Formation.
+ A Data Catalog database `sales_db` with a table `customers` that has the columns `id` and `name`.
+ A job runtime role with the permissions in [Permissions for governed UDFs](emr-spark-fgac-governed-udfs.md#emr-spark-fgac-governed-udfs-permissions). The role also needs read access to the script location and `s3:PutObject` on the log location.
+ An EMR Serverless application and a job runtime role for Lake Formation. For the setup, see [Using Lake Formation with EMR Serverless for fine-grained access control](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/emr-serverless-lf-enable.html) in the *EMR Serverless User Guide*.
+ The `IAMAllowedPrincipals` group has no permissions on `sales_db` or `customers`.
+ The job runtime role has the Lake Formation `SELECT` permission on `customers`.

## Step 1: Build the custom code artifact
<a name="emr-spark-fgac-governed-udfs-tutorial-build"></a>

1. Create a Maven project with the coordinates `com.example:my-upper:1.0` and the packaging `jar`. Create the class `com.example.MyUpper` in `src/main/java/com/example/`.

   ```java
   package com.example;
   
   import java.util.Locale;
   import org.apache.hadoop.hive.ql.exec.UDF;
   
   public final class MyUpper extends UDF {
       public String evaluate(String s) {
           return s == null ? null : s.toUpperCase(Locale.ROOT);
       }
   }
   ```

1. Add `hive-exec` as a `provided` dependency, and compile for Java 8.

   ```xml
   <properties>
     <maven.compiler.release>8</maven.compiler.release>
   </properties>
   <dependencies>
     <dependency>
       <groupId>org.apache.hive</groupId>
       <artifactId>hive-exec</artifactId>
       <version>2.3.10</version>
       <classifier>core</classifier>
       <scope>provided</scope>
     </dependency>
   </dependencies>
   ```

1. Build the JAR, and check the class file version with these shell commands.

   ```bash
   mvn -q clean package
   javap -v -cp target/my-upper-1.0.jar com.example.MyUpper | grep major
      major version: 52
   ```

   Version 52 is Java 8. Version 61 is Java 17.

## Step 2: Register the governed UDF
<a name="emr-spark-fgac-governed-udfs-tutorial-register"></a>

1. Use the AWS CLI to upload the JAR to a prefix for this governed UDF only, in the registered Amazon S3 location.

   ```bash
   aws s3 cp target/my-upper-1.0.jar s3://{{amzn-s3-demo-bucket}}/udfs/my_upper/my-upper-1.0.jar
   ```

1. Create the JSON file `udf-input.json` with this content.

   ```json
   {
     "FunctionName": "my_upper",
     "ClassName": "com.example.MyUpper",
     "OwnerName": "{{data_admin}}",
     "OwnerType": "USER",
     "ResourceUris": [
       { "ResourceType": "JAR", "Uri": "s3://{{amzn-s3-demo-bucket}}/udfs/my_upper/my-upper-1.0.jar" }
     ],
     "ArtifactLocation": "s3://{{amzn-s3-demo-bucket}}/udfs/my_upper/",
     "GovernanceMode": "LAKE_FORMATION"
   }
   ```

1. Use the AWS CLI to create the governed UDF in the Data Catalog.

   ```bash
   aws glue create-user-defined-function \
     --database-name sales_db \
     --function-input file://udf-input.json
   ```

1. Use the AWS CLI to grant `EXECUTE` on the governed UDF to the job runtime role.

   ```bash
   aws lakeformation grant-permissions \
     --principal DataLakePrincipalIdentifier=arn:aws:iam::{{111122223333}}:role/{{JobRuntimeRole}} \
     --resource '{"UserDefinedFunction":{"CatalogId":"{{111122223333}}","DatabaseName":"sales_db","Name":"my_upper"}}' \
     --permissions EXECUTE
   ```

## Step 3: Call the governed UDF from a query
<a name="emr-spark-fgac-governed-udfs-tutorial-run"></a>

1. Create the Python script `query.py` with this code, and upload it to Amazon S3.

   ```python
   from pyspark.sql import SparkSession
   
   spark = SparkSession.builder.getOrCreate()
   spark.sql("SELECT id, sales_db.my_upper(name) AS uname FROM sales_db.customers").show()
   ```

1. Use the AWS CLI to start the job run, and declare the governed UDF.

   ```bash
   aws emr-serverless start-job-run \
     --application-id {{application-id}} \
     --execution-role-arn arn:aws:iam::{{111122223333}}:role/{{JobRuntimeRole}} \
     --job-driver '{
       "sparkSubmit": {
         "entryPoint": "s3://{{amzn-s3-demo-bucket}}/scripts/query.py",
         "sparkSubmitParameters": "--conf spark.aws.lakeformation.artifacts=arn:aws:glue:{{region}}:{{111122223333}}:userDefinedFunction/sales_db/my_upper"
       }
     }' \
     --configuration-overrides '{"monitoringConfiguration":{"s3MonitoringConfiguration":{"logUri":"s3://{{amzn-s3-demo-bucket}}/logs/"}}}'
   ```

1. Examine the driver output. Download `applications/{{application-id}}/jobs/{{job-run-id}}/SPARK_DRIVER/stdout.gz` from the log location. The `uname` column shows the names in uppercase.

## Step 4: Call the governed UDF from an RLS policy
<a name="emr-spark-fgac-governed-udfs-tutorial-rls"></a>

1. Use the AWS CLI to create an RLS policy that calls the governed UDF.

   ```bash
   aws lakeformation create-rls-policy \
     --name customers_alice_only \
     --attachment-columns '[{"name":"name","type":"string"}]' \
     --filter-expression "sales_db.my_upper(name) = 'ALICE'"
   ```

1. Use the AWS CLI to attach the policy to the table for the job runtime role.

   ```bash
   aws lakeformation attach-rls-policy \
     --name customers_alice_only \
     --resource '{"Table":{"CatalogId":"{{111122223333}}","DatabaseName":"sales_db","Name":"customers"}}' \
     --principal '{"DataLakePrincipalIdentifier":"arn:aws:iam::{{111122223333}}:role/{{JobRuntimeRole}}"}'
   ```

1. Use the AWS CLI to grant `SELECT` on the table to the governed UDF.

   ```bash
   aws lakeformation grant-permissions \
     --principal DataLakePrincipalIdentifier=arn:aws:glue:{{region}}:{{111122223333}}:userDefinedFunction/sales_db/my_upper \
     --resource '{"Table":{"CatalogId":"{{111122223333}}","DatabaseName":"sales_db","Name":"customers"}}' \
     --permissions SELECT
   ```

1. Run the job from step 3 again, with the same declaration.

1. Examine the output. The output shows only the rows where `sales_db.my_upper(name)` is `ALICE`.

You created a governed UDF and called it from a query and from an RLS policy. The query call ran in user space. The policy call ran in system space.

If the job does not declare the governed UDF, the job fails. The `stateDetails` of the job run shows `Driver was shut down due to a security validation exception.` The driver log `SPARK_DRIVER/stderr.gz` shows `Multi Dialect View sales_db.customers SQL contains unsupported operations`.

## Changes for other platforms
<a name="emr-spark-fgac-governed-udfs-tutorial-platforms"></a>


**Tutorial changes by platform**  

| Platform | Changes | 
| --- | --- | 
| Amazon EMR on EC2 | Before step 3, the cluster administrator sets UdfEnabled to true and adds the UDF ARN to ApprovedUdfArns in the security configuration. In step 3, add a step that runs spark-submit --conf spark.aws.lakeformation.artifacts={{arn}} query.py. | 
| AWS Glue ETL | In step 3, create a AWS Glue 6.1 job with the job parameters --enable-lakeformation-fine-grained-access true and --lakeformation-artifacts {{arn}}. Compile the classes for Java 17 or lower. | 