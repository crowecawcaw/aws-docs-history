

# Using user-defined functions with Lake Formation fine-grained access control

With Amazon EMR release `emr-7.14.0` and later, or `emr-spark-8.2.0` and later, Lake Formation-enabled EMR Serverless applications can run Lake Formation-governed AWS Glue user-defined functions (UDFs). Spark loads a declared governed UDF in both the system profile and the user profile. A governed UDF that your query calls runs in the user profile on data that Lake Formation has already filtered. A governed UDF that a Lake Formation row-level security (RLS) policy or a Data Catalog view calls runs in the system profile.

To use governed UDFs, a data lake administrator grants permissions in Lake Formation, and you declare the UDFs in the Spark property `spark.aws.lakeformation.artifacts` for your application, job run, [interactive workload](interactive-workloads.html) (including Livy endpoints), or Spark Connect session.

## How governed user-defined functions work
<a name="emr-serverless-lf-udf-how-it-works"></a>

1. A data lake administrator [creates a Lake Formation-governed UDF](https://docs.aws.amazon.com/lake-formation/latest/dg/governing-user-defined-functions.html#governing-udfs-create) in the [AWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/populate-data-catalog.html). The administrator stores the UDF's JAR files in an Amazon S3 location that is registered with Lake Formation.

1. In Lake Formation, the data lake administrator [grants](https://docs.aws.amazon.com/lake-formation/latest/dg/governing-user-defined-functions.html#governing-udfs-permissions) the job runtime role `EXECUTE` on the UDF, and grants the UDF `SELECT` on each table that it can read. A new governed UDF has `SELECT` on all tables in its catalog by default. Revoke that grant to limit the UDF to specific tables.

1. You declare the UDFs that a workload uses in the Spark property `spark.aws.lakeformation.artifacts`.

1. EMR Serverless verifies with Lake Formation that the job runtime role has `EXECUTE` on each declared UDF. If any check fails, the job run or session fails.

1. The system driver downloads the UDF JAR files with temporary credentials from Lake Formation, verifies that each JAR has not changed since the UDF was created or last updated, and loads them in the system profile. The UDFs are also available in the user profile. If a JAR has changed, the job run or session fails.

1. During the job run or session, for each table that the job runtime role reads with fine-grained access control, Lake Formation allows access only if every declared UDF has `SELECT` on that table.

## Prerequisites
<a name="emr-serverless-lf-udf-prerequisites"></a>
+ A Lake Formation-enabled EMR Serverless application with release `emr-7.14.0` or later, or `emr-spark-8.2.0` or later. For more information, see [Enabling Lake Formation in Amazon EMR](emr-serverless-lf-enable.md#emr-serverless-lf-enable-config).
+ Lake Formation-governed UDFs registered in the AWS Glue Data Catalog in the same AWS Region as your application. Governed UDFs are Hive UDF or GenericUDF classes, packaged in JAR files compiled for Java 17 or lower and stored in an Amazon S3 location that is registered with Lake Formation.
+ In Lake Formation, the job runtime role has `EXECUTE` on each UDF, and each UDF has `SELECT` on every table that the workload reads with fine-grained access control. This applies whether or not the workload calls the UDF.

## Job runtime role IAM permissions
<a name="emr-serverless-lf-udf-permissions"></a>

In addition to the permissions in [Job runtime role IAM permissions](emr-serverless-lf-enable.md#emr-serverless-lf-enable-permissions), add the following actions to the job runtime role. Scope `glue:GetUserDefinedFunction` to your catalog, database, and UDF ARNs. `lakeformation:GetTemporaryGlueFunctionCredentials` supports only `"Resource": "*"`.


| Action | Purpose | 
| --- | --- | 
| glue:GetUserDefinedFunction | Reads UDF metadata, such as the Amazon S3 locations of the JAR files | 
| lakeformation:GetTemporaryGlueFunctionCredentials | Gets temporary credentials to download the UDF JAR files from Amazon S3 | 

The following example policy grants these permissions for one UDF. It also includes `lakeformation:GetDataAccess`, which Lake Formation already requires and which also supports only `"Resource": "*"`. Your Lake Formation permissions, not the IAM policy, determine which data is returned. For more information, see [Underlying data access control](https://docs.aws.amazon.com/lake-formation/latest/dg/access-control-underlying-data.html) in the *AWS Lake Formation Developer Guide*.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "GovernedUdfMetadata",
      "Effect": "Allow",
      "Action": "glue:GetUserDefinedFunction",
      "Resource": [
        "arn:aws:glue:{{us-east-1}}:{{123456789012}}:catalog",
        "arn:aws:glue:{{us-east-1}}:{{123456789012}}:database/{{my_db}}",
        "arn:aws:glue:{{us-east-1}}:{{123456789012}}:userDefinedFunction/{{my_db}}/{{my_udf}}"
      ]
    },
    {
      "Sid": "LakeFormationDataAccess",
      "Effect": "Allow",
      "Action": [
        "lakeformation:GetDataAccess",
        "lakeformation:GetTemporaryGlueFunctionCredentials"
      ],
      "Resource": "*"
    }
  ]
}
```

Replace {{my\_db}} and {{my\_udf}} with the names of your AWS Glue database and user-defined function.

**Note**  
IAM permissions and Lake Formation permissions are separate. The job runtime role also needs the `EXECUTE` permission on each UDF in Lake Formation.

## Declaring user-defined functions
<a name="emr-serverless-lf-udf-declare"></a>

Set the Spark property `spark.aws.lakeformation.artifacts` to a comma-separated list of UDF ARNs in the following format.

```
arn:aws:glue:{{region}}:{{account-id}}:userDefinedFunction/{{database-name}}/{{function-name}}
```

You can set the property in the `spark-defaults` classification of an application, job run, or session, or with `--conf` in the `sparkSubmitParameters` of a job run.

EMR Serverless validates the list when you submit the request:
+ Each value must be a valid AWS Glue user-defined function ARN.
+ All ARNs must be in the same AWS Region and partition as the application.
+ You can declare up to 10 UDFs.
+ The list can't contain duplicate ARNs.

**Note**  
Set the property in the application, job run, or session configuration. Setting it in your code, for example with `SparkSession.builder.config(...)`, has no effect, because EMR Serverless authorizes the UDFs before your code starts.

### Application level
<a name="emr-serverless-lf-udf-declare-application"></a>

Set the property in the runtime configuration when you create or update the application. All job runs and sessions on the application use these UDFs by default.

```bash
aws emr-serverless create-application \
    --release-label emr-7.14.0 \
    --type "SPARK" \
    --runtime-configuration '[{
     "classification": "spark-defaults",
     "properties": {
      "spark.emr-serverless.lakeformation.enabled": "true",
      "spark.aws.lakeformation.artifacts": "arn:aws:glue:us-east-1:111122223333:userDefinedFunction/my_db/my_udf"
      }
    }]'
```

### Job run level
<a name="emr-serverless-lf-udf-declare-job-run"></a>

Set the property when you start a job run, either in the configuration overrides or in `sparkSubmitParameters`. The job run value takes precedence over the application value of this property.

The following example sets the property in the configuration overrides.

```bash
aws emr-serverless start-job-run \
    --application-id APPLICATION_ID \
    --execution-role-arn EXECUTION_ROLE_ARN \
    --job-driver '{
        "sparkSubmit": {
            "entryPoint": "s3://amzn-s3-demo-bucket/scripts/my_job.py"
        }
    }' \
    --configuration-overrides '{
        "applicationConfiguration": [{
            "classification": "spark-defaults",
            "properties": {
                "spark.aws.lakeformation.artifacts": "arn:aws:glue:us-east-1:111122223333:userDefinedFunction/my_db/my_udf,arn:aws:glue:us-east-1:111122223333:userDefinedFunction/my_db/my_other_udf"
            }
        }]
    }'
```

The following example sets the property in `sparkSubmitParameters`, which accepts longer values than a property in a configuration classification. Use this form for longer lists of UDFs. For the limits, see [SparkSubmit](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_SparkSubmit.html) and [Configuration](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_Configuration.html) in the [*Amazon EMR Serverless API Reference*](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/Welcome.html).

```bash
aws emr-serverless start-job-run \
    --application-id APPLICATION_ID \
    --execution-role-arn EXECUTION_ROLE_ARN \
    --job-driver '{
        "sparkSubmit": {
            "entryPoint": "s3://amzn-s3-demo-bucket/scripts/my_job.py",
            "sparkSubmitParameters": "--conf spark.aws.lakeformation.artifacts=arn:aws:glue:us-east-1:111122223333:userDefinedFunction/my_db/my_udf,arn:aws:glue:us-east-1:111122223333:userDefinedFunction/my_db/my_other_udf"
        }
    }'
```

### Spark Connect sessions
<a name="emr-serverless-lf-udf-declare-spark-connect"></a>

Set the property in the configuration overrides when you start the session. For more information, see [Fine-grained access control with AWS Lake Formation for Spark Connect sessions](spark-connect.md#spark-connect-fgac).

```bash
aws emr-serverless start-session \
    --application-id APPLICATION_ID \
    --execution-role-arn EXECUTION_ROLE_ARN \
    --configuration-overrides '{
        "runtimeConfiguration": [{
            "classification": "spark-defaults",
            "properties": {
                "spark.aws.lakeformation.artifacts": "arn:aws:glue:us-east-1:111122223333:userDefinedFunction/my_db/my_udf"
            }
        }]
    }'
```

## Security considerations
<a name="emr-serverless-lf-udf-security"></a>
+ **Granting permissions on a UDF is a decision to trust its code.** A declared UDF is loaded in the system profile of your job run or session. When a Lake Formation RLS policy or a Data Catalog view calls it, its code runs in the system profile, can read data before Lake Formation filters are applied, uses the privileged data access credentials of the system profile, and can call AWS services as the job runtime role. In Lake Formation, a data lake administrator should grant `EXECUTE` and `SELECT` only to UDFs whose code they have reviewed and trust with unfiltered access to that data.
+ **Grant permissions narrowly.** Grant `EXECUTE` to specific job runtime roles instead of to whole accounts. A new governed UDF has `SELECT` on all tables in its catalog by default. Revoke that grant, and then grant the UDF `SELECT` only on the tables that it needs.
+ **Give each governed UDF its own artifact location.** Lake Formation credentials cover the whole Amazon S3 artifact location of a UDF, so UDFs that share a location can read each other's JAR files. If a Lake Formation RLS policy or a Data Catalog view calls a governed UDF, every job run or session that reads that table must declare the UDF, or it fails.
+ **Revoking permissions isn't immediate.** When you revoke a UDF's `SELECT` on a table, the change applies to new data access requests. Temporary credentials that Lake Formation already issued remain valid until they expire. When you revoke `EXECUTE` from the job runtime role, a running job run or session continues until its current authorization expires. This takes at most 1 hour. To stop access sooner, cancel the job runs and sessions that declare the UDF.
+ **Protect the Amazon S3 locations of your UDF JAR files.** Lake Formation records the last-modified time of each JAR file when you create or update the UDF. If the Amazon S3 object has a newer last-modified time, even if its content is the same, job runs and sessions that declare the UDF fail before the code loads. Restrict write access to these locations. To publish a new version, upload it under a new file name and update the UDF.
+ **System profile logs can include output from your UDFs.** EMR Serverless restricts access to system profile logs. For more information, see [Considerations and limitations](emr-serverless-lf-enable-considerations.md).