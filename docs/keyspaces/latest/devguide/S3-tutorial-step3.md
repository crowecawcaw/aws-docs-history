# Step 3: Run the AWS Glue job to export the Amazon Keyspaces table to the Amazon S3 bucket from the

AWS CLI

In this step, you use the AWS CLI to run the AWS Glue job created in the previous step to export an Amazon Keyspaces table to your bucket in Amazon S3.

###### Run the export job from the AWS CLI

1. In the following example, the AWS CLI command runs the job created in the previous step.

```
aws glue start-job-run --job-name `AmazonKeyspacesExportToS3-cfn-setup-cfn-glue`
```

    * You can override any of the AWS Glue job parameters including the
     default arguments in the AWS CLI command. To override any default arguments of the job, for example keyspace or
     table name, you can pass them as arguments. For a full list of arguments,
     see [start-job-run](../../../cli/latest/reference/glue/start-job-run.md "../../../cli/latest/reference/glue/start-job-run.md") in the AWS Glue Command Line Reference.


    The following command runs the AWS Glue export job, but overrides the number of AWS Glue workers,
     worker type, and the table name.



    ```
    aws glue start-job-run --job-name AmazonKeyspacesExportToS3-cfn-setup-cfn-glue \
                        --number-of-workers 8 --worker-type G.2X \
                        --arguments '{"--TABLE_NAME":"`my_table`"}'
    ```

2. Confirm that your table has been exported to your Amazon S3 bucket. Based on the size of the table, this can take some time.
   When the export job is finished, you can see the following folders in the bucket using the example command.

```
aws s3 ls s3://s3-keyspaces
```

The output shows the following structure in your bucket.

```
 `PRE conf/
 PRE export/
 PRE jars/
 PRE scripts/
 PRE spark-logs/`
```

Your files will be located in the following folder structure under `export`, data/time values will show
your own values.

```
`\------- export
 \----- keyspace_name
 \----- table_name
 \----- snapshot
 \----- year=2025
 \----- month=01
 \----- day=02
 \----- hour=09
 \----- minute=22
 \--- YOUR DATA HERE`
```

To schedule the AWS Glue job you just ran manually, proceed to [Step 4: (Optional) Create a trigger to schedule the export job](S3-tutorial-step4.md "S3-tutorial-step4.md").
