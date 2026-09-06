

# Step 2: Run the export job
<a name="S3-tutorial-step2"></a>

In this step, you run the AWS Glue export job created in the previous step. After you start the export, you can monitor the job progress with the `status` and `logs` commands.

**To run and monitor the export job**

1. Run the export command. Specify the keyspace, table, and the Amazon S3 bucket to export to. Use the bucket that was created by the bootstrap command in the previous step. Replace {{YOURACCOUNTID}} with your AWS account ID.

   ```
   $ ./keyspaces-bulk-cli export --keyspace {{catalog}} --table {{book_awards}} \
       --s3-uri s3://amazon-keyspaces-bulk-cli-{{aksglue}}-{{YOURACCOUNTID}}
   ```
   + You can override additional parameters when running the export. The following command increases the number of AWS Glue workers. Start with the default of 2 workers and increase as needed based on table size and export duration. Monitor the job with the `status` command and scale up if the export takes longer than expected.

     ```
     $ ./keyspaces-bulk-cli export --keyspace {{catalog}} --table {{book_awards}} \
         --s3-uri s3://amazon-keyspaces-bulk-cli-{{aksglue}}-{{YOURACCOUNTID}} --workers {{8}}
     ```

1. Monitor the status of the export job. You can check the current run status and view logs.

   ```
   $ ./keyspaces-bulk-cli status export
   ```

   The output shows the job run details. Wait until the `State` field shows `SUCCEEDED`:

   ```
            Job Run: jr_6f8de24d7131da54...
   ┏━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
   ┃ Field          ┃ Value                                      ┃
   ┡━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
   │ Job Name       │ AmazonKeyspacesExportToS3-aksglue          │
   │ State          │ SUCCEEDED                                  │
   │ Started        │ 2025-01-30 14:54:22                        │
   │ Completed      │ 2025-01-30 14:56:45                        │
   │ Execution Time │ 143s                                       │
   │ Workers        │ 2                                          │
   │ Worker Type    │ G.2X                                       │
   └────────────────┴────────────────────────────────────────────┘
   ```

   To view the logs for the running or completed job, use the following command.

   ```
   $ ./keyspaces-bulk-cli logs export
   ```

   To view only error logs, use the following command.

   ```
   $ ./keyspaces-bulk-cli logs export --log-type error
   ```

1. Confirm that the export completed by listing the Amazon S3 bucket contents. Based on the size of the table, the export can take some time. When the export job finishes, you can see the following folders in the bucket. Replace {{YOURACCOUNTID}} with your AWS account ID.

   ```
   $ aws s3 ls s3://amazon-keyspaces-bulk-cli-{{aksglue}}-{{YOURACCOUNTID}}
   ```

   The output shows the following structure in your bucket:

   ```
                              PRE conf/
                              PRE export/
                              PRE jars/
                              PRE scripts/
                              PRE spark-logs/
   ```

   Your exported data files are in the following folder structure (date and time values reflect your own export run):

   ```
   \------- export
               \----- catalog
                   \----- book_awards
                      \----- snapshot
                          \----- year=2025
                              \----- month=01
                                 \----- day=30
                                     \----- hour=14
                                         \----- minute=54
                                             \--- part-00000-*.snappy.parquet
   ```

To schedule the AWS Glue job you just ran manually, proceed to [Step 3: (Optional) Create a trigger to schedule the export job](S3-tutorial-step3.md).