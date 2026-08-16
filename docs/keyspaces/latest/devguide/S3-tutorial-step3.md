# Step 3: (Optional) Create a trigger to schedule the export job

To run the export job on a regular basis, you can create a scheduled trigger using the AWS CLI. For more information, see
[AWS Glue triggers](../../../glue/latest/dg/about-triggers.md "../../../glue/latest/dg/about-triggers.md") in the AWS Glue Developer Guide.

###### To schedule the AWS Glue export job

1. To find the job name and parameters from a previous run, use the `--json` flag
   to output the run details including the arguments used.

```
`$` `./keyspaces-bulk-cli runs export --json`
```

The output includes the job name, worker configuration, and all arguments from each run:

```
`[
 {
 "JobName": "AmazonKeyspacesExportToS3-aksglue",
 "RunId": "jr_2d827b0637a36b25f32f03b83e107cf8...",
 "State": "SUCCEEDED",
 "Started": "2025-01-30T14:54:22.480000-04:00",
 "Duration": 127,
 "Workers": 2,
 "WorkerType": "G.2X",
 "Arguments": {
 "--KEYSPACE_NAME": "catalog",
 "--DRIVER_CONF": "keyspaces-application.conf",
 "--TABLE_NAME": "book_awards",
 "--S3_URI": "s3://amazon-keyspaces-bulk-cli-aksglue-111122223333",
 "--FORMAT": "parquet"
 }
 }
]`
```

Use the `JobName`, `Workers`, `WorkerType`, and
`Arguments` values from the output in the next step to create the trigger. 2. The following AWS CLI command creates a trigger with the name `KeyspacesExportWeeklyTrigger`
that runs the AWS Glue export job once per week on Monday at 12:00 UTC. Use the values from the
JSON output of the previous step for the job name, worker configuration, and arguments.

```
aws glue create-trigger \
  --name KeyspacesExportWeeklyTrigger \
  --type SCHEDULED \
  --schedule "cron(0 12 ? * MON *)" \
  --start-on-creation \
  --actions '[{
     "JobName": "AmazonKeyspacesExportToS3-`aksglue`",
     "NumberOfWorkers": `2`,
     "WorkerType": "`G.2X`",
     "Arguments": {
       "--KEYSPACE_NAME": "`catalog`",
       "--DRIVER_CONF": "keyspaces-application.conf",
       "--TABLE_NAME": "`book_awards`",
       "--S3_URI": "s3://amazon-keyspaces-bulk-cli-`aksglue`-`YOURACCOUNTID`",
       "--FORMAT": "`parquet`"
     }
  }]'
```

    * To override specific parameters for the scheduled job, change the values
     in the `Arguments` block. The following example schedules an export
     of a different table with more workers.



    ```
    aws glue create-trigger \
      --name KeyspacesExportWeeklyTrigger \
      --type SCHEDULED \
      --schedule "cron(0 12 ? * MON *)" \
      --start-on-creation \
      --actions '[{
         "JobName": "AmazonKeyspacesExportToS3-`aksglue`",
         "NumberOfWorkers": `8`,
         "WorkerType": "`G.2X`",
         "Arguments": {
           "--KEYSPACE_NAME": "`my_keyspace`",
           "--DRIVER_CONF": "keyspaces-application.conf",
           "--TABLE_NAME": "`my_table`",
           "--S3_URI": "s3://amazon-keyspaces-bulk-cli-`aksglue`-`YOURACCOUNTID`",
           "--FORMAT": "`parquet`"
         }
      }]'
    ```

3. To confirm that the trigger was created, use the following command.

```
`$` `aws glue list-triggers`
```

The output of the command looks similar to the following:

```
`{
 "TriggerNames": [
 "KeyspacesExportWeeklyTrigger"
 ]
}`
```

To clean up the AWS resources created in this tutorial, proceed to [Step 4: (Optional) Cleanup](S3-tutorial-step4.md "S3-tutorial-step4.md").
