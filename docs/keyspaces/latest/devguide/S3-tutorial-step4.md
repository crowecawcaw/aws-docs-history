# Step 4: (Optional) Create a trigger to schedule the export job

To run the export job created in the previous step on a regular basis, you can create a scheduled trigger. For more information, see
[AWS Glue triggers](../../../glue/latest/dg/about-triggers.md "../../../glue/latest/dg/about-triggers.md") in the AWS Glue Developer Guide.

###### Schedule a AWS Glue job

1. The following AWS CLI command is an
   example of a simple trigger with the name `KeyspacesExportWeeklyTrigger`
   that runs the AWS Glue job with the name
   `AmazonKeyspacesExportToS3-cfn-setup-cfn-glue` once per week on Monday at 12:00 UTC.

```
aws glue create-trigger \
  --name KeyspacesExportWeeklyTrigger \
  --type SCHEDULED \
  --schedule "cron(0 12 ? * MON *)" \
  --start-on-creation \
  --actions '[{
     "JobName": "AmazonKeyspacesExportToS3-cfn-setup-cfn-glue"
  }]'
```

    * To override any of the default settings of the scheduled job, you can pass them as arguments.
     In this example we override the keyspace name, the table name, the number
     of workers, and the worker type by passing them as arguments. The following command is an
     example of this.



    ```
    aws glue create-trigger \
      --name KeyspacesExportWeeklyTrigger \
      --type SCHEDULED \
      --schedule "cron(0 12 ? * MON *)" \
      --start-on-creation \
      --actions '[{
         "JobName": "AmazonKeyspacesExportToS3-cfn-setup-cfn-glue",
         "Arguments": {
           "--number-of-workers": "8",
           "--worker-type": "G.2X"},
           "--table_name": "`my_table`",
           "--keyspace_name": "`my_keyspace`"
      }]'
    ```

2. To confirm that the trigger has been created, use the following command.

```
aws glue list-triggers
```

The output of the command should look similar to this.

```
`{
 "TriggerNames": [
 "KeyspacesExportWeeklyTrigger"
 ]
}`
```

To clean up the AWS resources created in this tutorial, proceed to [Step 5: (Optional) Cleanup](S3-tutorial-step5.md "S3-tutorial-step5.md").
