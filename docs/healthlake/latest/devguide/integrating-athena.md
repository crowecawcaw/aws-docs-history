

# Setting up Amazon Athena

Amazon Athena queries the HealthLake tables in place with standard SQL, with no export. For how the tables are organized, see [Understanding the analytics tables](integrating-analytics.md#integrating-analytics-tables).

**Note**  
HealthLake supports FHIR R4 `read` interaction on your HealthLake data in Athena. For more information, see [Reading a FHIR resource](managing-fhir-resources-read.md).

Before you begin, complete Steps 1 and 2 in [Getting started with HealthLake analytics](integrating-analytics-getting-started.md). Grant Lake Formation permissions to the IAM user or role that runs your Athena queries.

In the commands in this topic, replace {{us-east-1}} with the AWS Region of your data store.

## Step 1: Give the principal Athena permissions
<a name="getting-started-athena-user"></a>

Give the IAM user or role Athena permissions. To get started, add the `AmazonAthenaFullAccess` AWS managed policy. AWS managed policies might not grant least-privilege permissions, because all AWS customers can use them. Grant only the permissions required to perform a task, including permission to read and write the Amazon S3 location where Athena stores query results. For more information, see [Apply least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies) in the *IAM User Guide*.

------
#### [ Console ]

**To attach the policy (console)**

1. Open the [IAM console](https://console.aws.amazon.com/iam).

1. Choose **Users** or **Roles**, and then choose the principal that runs queries.

1. Choose **Add permissions**, and then choose **Attach policies**.

1. Select **AmazonAthenaFullAccess**, and then choose **Add permissions**.

------
#### [ AWS CLI ]

**To attach the policy (AWS CLI)**
+ Attach the `AmazonAthenaFullAccess` policy to the role that runs your queries.

  ```bash
  aws iam attach-role-policy --role-name {{role-name}} --policy-arn arn:aws:iam::aws:policy/AmazonAthenaFullAccess
  ```

  For an IAM user, use `attach-user-policy` with `--user-name` instead.

Replace {{role-name}} with the role that runs your queries.

------

**Result:** The principal can run Athena queries.

## Step 2: Create a workgroup that uses engine version 3
<a name="integrating-athena-workgroup"></a>

A workgroup can set the query result location for every query and override client settings. This step configures the workgroup, so you don't set a query result location for each user.

**Important**  
To query a HealthLake data store in Athena, you must use **Athena engine version 3**.

For more information, see [Manage workgroups](https://docs.aws.amazon.com/athena/latest/ug/workgroups-create-update-delete.html) and [Use workgroups to control query access and costs](https://docs.aws.amazon.com/athena/latest/ug/workgroups-manage-queries-control-costs.html) in the *Athena User Guide*.

For more information about setting a query result location, see [Specifying a query result location using the Athena console](https://docs.aws.amazon.com/athena/latest/ug/querying.html#query-results-specify-location-console) in the *Amazon Athena User Guide*.

------
#### [ Console ]

**To create a workgroup (console)**

1. Open the [Athena console](https://console.aws.amazon.com/athena).

1. In the navigation pane, choose **Workgroups**, and then choose **Create workgroup**.

1. Enter a name for the workgroup.

1. For the engine version, choose **Athena engine version 3** manually.

1. Under the query result configuration, enter the Amazon S3 location for results. Use an Amazon S3 location in the same AWS Region.

1. Choose **Create workgroup**.

------
#### [ AWS CLI ]

**To create a workgroup (AWS CLI)**

1. If you don't already have a bucket for query results, create one.

   ```bash
   aws s3 mb s3://{{amzn-s3-demo-bucket}} --region {{us-east-1}}
   ```

1. Create a workgroup that uses Athena engine version 3 and stores results in your bucket.

   ```bash
   aws athena create-work-group \
       --region {{us-east-1}} \
       --name healthlake \
       --configuration '{
           "ResultConfiguration": {"OutputLocation": "s3://{{amzn-s3-demo-bucket}}/athena-results/"},
           "EnforceWorkGroupConfiguration": true,
           "EngineVersion": {"SelectedEngineVersion": "Athena engine version 3"}
       }'
   ```

1. Verify the engine version.

   ```bash
   aws athena get-work-group --region {{us-east-1}} --work-group healthlake --query "WorkGroup.Configuration.EngineVersion.EffectiveEngineVersion"
   ```

   The output is `"Athena engine version 3"`.

Replace {{amzn-s3-demo-bucket}} with your bucket for query results, in the same AWS Region as Athena.

------

**Result:** The workgroup `healthlake` uses engine version 3 and stores results in your bucket. Record the workgroup name. You use it in Step 3.

## Step 3: Run a test query
<a name="integrating-athena-query-sql"></a>

Run a query in the `healthlake` workgroup that you created in Step 2.

------
#### [ Console ]

**To run a test query (console)**

1. In the Athena query editor, choose the `healthlake` workgroup.

1. Choose the resource link database for your data store.

1. Run a test query.

   ```SQL
   SELECT COUNT(*) FROM patient;
   ```

------
#### [ AWS CLI ]

**To run a test query (AWS CLI)**

1. Start the query in the `healthlake` workgroup.

   ```bash
   aws athena start-query-execution \
       --region {{us-east-1}} \
       --work-group healthlake \
       --query-execution-context Database={{resource-link-name}},Catalog=AwsDataCatalog \
       --query-string "SELECT COUNT(*) FROM patient"
   ```

   The command returns a `QueryExecutionId`.

1. Check the query status until it's `SUCCEEDED`.

   ```bash
   aws athena get-query-execution --region {{us-east-1}} --query-execution-id {{query-execution-id}} --query QueryExecution.Status.State
   ```

1. Get the query results.

   ```bash
   aws athena get-query-results --region {{us-east-1}} --query-execution-id {{query-execution-id}}
   ```

Replace {{resource-link-name}} with the resource link name from Step 1 in [Getting started with HealthLake analytics](integrating-analytics-getting-started.md). Replace {{query-execution-id}} with the ID that `start-query-execution` returns.

------

**Result:** The query returns the number of rows in the patient table, including earlier versions of each resource.

For more queries, see [Example queries for HealthLake data](integrating-analytics-example-queries.md).

## More information about SQL in Athena
<a name="integrating-athena-more-info"></a>

For more information about SQL in Athena, see the following topics in the *Athena User Guide*:
+ [Query arrays with complex types and nested structures](https://docs.aws.amazon.com/athena/latest/ug/rows-and-structs.html)
+ [Querying JSON](https://docs.aws.amazon.com/athena/latest/ug/querying-JSON.html)
+ [DML queries, functions, and operators](https://docs.aws.amazon.com/athena/latest/ug/dml-queries-functions-operators.html)
+ [Data types in Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/data-types.html)
+ [SQL reference for Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/ddl-sql-reference.html)
+ [Query Apache Iceberg tables](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg.html)
+ [Extracting data from JSON](https://docs.aws.amazon.com/athena/latest/ug/extracting-data-from-JSON.html)