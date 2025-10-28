# Managing the schedule for column statistics generation

You can manage the scheduling operations such as updating, starting, stopping, and
deleting schedules for the column statistics generation in AWS Glue. You can use AWS Glue
console, AWS CLI, or [AWS Glue column statistics API operations](aws-glue-api-crawler-column-statistics.md "aws-glue-api-crawler-column-statistics.md") to perform these tasks.

###### Topics

- [Updating the column statistics generation
  schedule](#update-column-stats-shedule "#update-column-stats-shedule")
- [Stopping the schedule for column statistics generation](#stop-column-stats-schedule "#stop-column-stats-schedule")
- [Resuming the schedule for column statistics generation](#resume-column-stats-schedule "#resume-column-stats-schedule")
- [Deleting column statistics generation schedule](#delete-column-stats-schedule "#delete-column-stats-schedule")

## Updating the column statistics generation

schedule

You can update the schedule to trigger the column statistics generation task after it
has been created. You can use the AWS Glue console, AWS CLI, or run the
[UpdateColumnStatisticsTaskSettings](aws-glue-api-crawler-column-statistics.md#aws-glue-api-crawler-column-statistics-UpdateColumnStatisticsTaskSettings "aws-glue-api-crawler-column-statistics.md#aws-glue-api-crawler-column-statistics-UpdateColumnStatisticsTaskSettings") operation to update the
schedule for a table. You can modify the parameters of an existing schedule, such as the
schedule type (on-demand, or scheduled) and other optional parameters.

AWS Management Console###### To update the settings for a column statistics generation task

1. Sign in to the AWS Glue console at [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/ "https://console.aws.amazon.com/glue/").
2. Choose the table that you want to update from the tables list.
3. In the lower section of the table details page, choose **Column statistics**.
4. Under **Actions**, choose **Edit** to update the schedule.
5. Make the desired changes to the schedule, and choose **Save**.

AWS CLI
If you are not using AWS Glue's statistics generation feature in
the console, you can manually update the schedule using the `update-column-statistics-task-settings`
command. The following example shows how to update column statistics
using AWS CLI.

```
aws glue update-column-statistics-task-settings \
 --database-name '`database_name`' \
 --table-name '`table_name`' \
 --role arn:aws:iam::`123456789012`:role/`stats_role` \
 --schedule '`cron(0 0-5 16 * * ?)`' \
 --column-name-list '`col-1`' \
 --sample-size '`20.0`' \
 --catalog-id '`123456789012`'\
 --security-configuration '`test-security`'
```

## Stopping the schedule for column statistics generation

If you no longer need the incremental statistics, you can stop the scheduled generation to save resources and costs.
Pausing the schedule doesn't impact the previously generated statistics. You can resume the schedule at your convenience.

AWS Management Console###### To stop the schedule for a column statistics generation task

1. On AWS Glue console, choose **Tables** under Data Catalog.
2. Select a table with column statistics.
3. On the **Table details** page, choose **Column statistics**.
4. Under **Actions**, choose **Scheduled generation**, **Pause**.
5. Choose **Pause** to confirm.

AWS CLI
To stop a column statistics task run schedule using the AWS CLI, you can use the following command:

```
aws glue stop-column-statistics-task-run-schedule \
 --database-name ''`database_name`' \
 --table-name '`table_name`'

```

Replace the `database_name` and the `table_name` with the actual names of the database and table for which you want to stop the column statistics task run schedule.

## Resuming the schedule for column statistics generation

If you've paused the statistics generation schedule, AWS Glue allows you to resume
the schedule at your convenience. You can resume the schedule using the AWS Glue
console, AWS CLI, or the [StartColumnStatisticsTaskRunSchedule](aws-glue-api-crawler-column-statistics.md#aws-glue-api-crawler-column-statistics-StartColumnStatisticsTaskRunSchedule "aws-glue-api-crawler-column-statistics.md#aws-glue-api-crawler-column-statistics-StartColumnStatisticsTaskRunSchedule") operation.

AWS Management Console###### To resume the schedule for column statistics generation

1. On AWS Glue console, choose **Tables** under Data Catalog.
2. Select a table with column statistics.
3. On the **Table details** page, choose **Column statistics**.
4. Under **Actions**, choose **Scheduled generation**, and choose **Resume**.
5. Choose **Resume**to confirm.

AWS CLI
Replace the `database_name` and the `table_name` with the actual names of the database and table for which you want to stop the column statistics task run schedule.

```
aws glue start-column-statistics-task-run-schedule \
 --database-name '`database_name`' \
 --table-name '`table_name`'
```

## Deleting column statistics generation schedule

While maintaining up-to-date statistics is generally recommended for optimal query performance, there are specific use cases where removing the automatic generation schedule might be beneficial.

- If the data remains relatively static, the existing column statistics may remain accurate for an extended period,
  reducing the need for frequent updates. Deleting the schedule can prevent unnecessary resource consumption and overhead associated with regenerating statistics on unchanging data.
- When manual control over statistics generation is preferred. By deleting the automatic
  schedule, administrators can selectively update column statistics at
  specific intervals or after significant data changes, aligning the process
  with their maintenance strategies and resource allocation needs.

AWS Management Console###### To delete the schedule for column statistics generation

1. On AWS Glue console, choose **Tables** under Data Catalog.
2. Select a table with column statistics.
3. On the **Table details** page, choose **Column statistics**.
4. Under **Actions**, choose **Scheduled generation**, **Delete**.
5. Choose **Delete**to confirm.

AWS CLI
Replace the `database_name` and the `table_name` with the actual names of the database and table for which you want to stop the column statistics task run schedule.

You can delete column statistics schedule using the [DeleteColumnStatisticsTaskSettings](aws-glue-api-crawler-column-statistics.md#aws-glue-api-crawler-column-statistics-DeleteColumnStatisticsTaskSettings "aws-glue-api-crawler-column-statistics.md#aws-glue-api-crawler-column-statistics-DeleteColumnStatisticsTaskSettings") API operation or
AWS CLI. The following example shows how to delete the schedule for
generating column statistics using AWS Command Line Interface (AWS CLI).

```
aws glue delete-column-statistics-task-settings \
    --database-name '`database_name`' \
    --table-name '`table_name`'

```
