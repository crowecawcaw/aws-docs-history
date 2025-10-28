# Create a crawler schedule

You can create a schedule for the crawler using the AWS Glue console or AWS CLI.

AWS Management Console

1. Sign in to the AWS Management Console, and open the AWS Glue console at
   [https://console.aws.amazon.com/glue/](<https://console.aws.amazon.com/glue\ "https://console.aws.amazon.com/glue">).
2. Choose **Crawlers** in the navigation
   pane.
3. Follow steps 1-3 in the [Configuring a crawler](define-crawler.md "define-crawler.md")
   section.
4. In [Step 4: Set output and scheduling](define-crawler-set-output-and-scheduling.md "define-crawler-set-output-and-scheduling.md"), choose a **Crawler schedule** to set the frequency of the run.
   You can choose the crawler to run hourly, daily, weekly, monthly or define custom schedule using cron expressions.

A cron expression is a string representing a schedule pattern,
consisting of 6 fields separated by spaces: \* \* \* \* \* <minute>
<hour> <day of month> <month> <day of week> <year>

For example, to run a task every day at midnight, the cron
expression is: 0 0 \* \* ? \*

For more information, see [Cron expressions](monitor-data-warehouse-schedule.md#CronExpressions "monitor-data-warehouse-schedule.md#CronExpressions"). 5. Review the crawler settings you configured, and create the crawler to run on a schedule.

AWS CLI

```
aws glue create-crawler
 --name `myCrawler` \
 --role `AWSGlueServiceRole-myCrawler`  \
 --targets '{"S3Targets":[{Path=`"s3://amzn-s3-demo-bucket/"`}]}' \
 --schedule `cron(15 12 * * ? *)`
```

For more information about using cron to schedule jobs and crawlers, see [Time-based schedules for jobs and crawlers](monitor-data-warehouse-schedule.md "monitor-data-warehouse-schedule.md").
