# Run a PySpark job in AWS Glue 5.0

Download the PySpark script . This AWS Glue PySpark script runs Spark SQL by joining the
shared federated table in account A and S3 based table in account B to analyze the data and
identify the total orders placed per market.

Create and run an AWS Glue job that joins the shared federated table in account A and Amazon S3
based table in account B:

1. On the AWS Glue console, in the navigation pane, choose **ETL jobs**.
2. Choose **Create job**, then choose **Script editor**.
3. For **Engine**, choose **Spark** and for **Options**, choose **Start fresh**.
4. Upload your PySpark script that contains the Spark SQL join query.
5. On the **Job details** tab:
   1. Provide the job name.
   2. Choose `Glue-execution-role` for the IAM
      role.
   3. For **Glue version**, select **Glue 5.0**.
   4. Under **Advanced properties**, for **Job
      parameters**, choose **Add new parameter** and add the following
      parameters:
      - `--datalake-formats = iceberg`
      - `--enable-lakeformation-fine-grained-access = true`

6. Save the job and choose **Run** to execute it.
7. Review the job run details from the **Output logs**.

## Clean up the resources

To avoid incurring costs on your AWS accounts, delete the following resources that you
created:

- Lake Formation permissions, catalog link container, database, and tables in account B
- AWS Glue job in account B
- Federated catalog, database, and table resources in account A
- Redshift Serverless namespace in account A
- Amazon S3 buckets that you created as part of data transfer in both accounts
- Athena query results bucket in account B
- IAM roles for the lakehouse architecture setup
