

# Run a PySpark job in AWS Glue 5.0
<a name="run-pyspark-job"></a>

Download the PySpark script . This AWS Glue PySpark script runs Spark SQL by joining the shared federated table in account A and S3 based table in account B to analyze the data and identify the total orders placed per market.

Create and run an AWS Glue job that joins the shared federated table in account A and Amazon S3 based table in account B:

1. On the AWS Glue console, in the navigation pane, choose **ETL jobs**.

1. Choose **Create job**, then choose **Script editor**.

1. For **Engine**, choose **Spark** and for **Options**, choose **Start fresh**.

1. Upload your PySpark script that contains the Spark SQL join query.

1. On the **Job details** tab:

   1. Provide the job name. 

   1. Choose {{`Glue-execution-role`}} for the IAM role.

   1. For **Glue version**, select **Glue 5.0**.

   1. Under **Advanced properties**, for **Job parameters**, choose **Add new parameter** and add the following parameters:
      + `--datalake-formats = iceberg`
      + `--enable-lakeformation-fine-grained-access = true`

1. Save the job and choose **Run** to execute it.

1. Review the job run details from the **Output logs**.

## Clean up the resources
<a name="clean-up"></a>

To avoid incurring costs on your AWS accounts, delete the following resources that you created:
+ Lake Formation permissions, catalog link container, database, and tables in account B
+ AWS Glue job in account B
+ Federated catalog, database, and table resources in account A
+ Redshift Serverless namespace in account A
+ Amazon S3 buckets that you created as part of data transfer in both accounts
+ Athena query results bucket in account B
+ IAM roles for the lakehouse architecture setup