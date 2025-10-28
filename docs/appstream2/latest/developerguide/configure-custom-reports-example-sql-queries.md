# Working with Athena Queries

This section provides SQL queries that you can run in Athena to analyze the usage reports data in your Amazon S3 bucket.

To create a consolidated report of all sessions in a given month, run the following query:

```
SELECT *
FROM "appstream-usage"."sessions"
WHERE year='`four-digit-year`'
AND month='`two-digit-month`'
```

You can also perform join operations between the **applications** and **sessions** tables in your query. For example, to view the distinct users who launched each application in a given month, run the following query:

```
SELECT DISTINCT apps.application_name, sessions.user_id
FROM "appstream-usage"."applications" apps
   INNER JOIN "appstream-usage"."sessions" sessions ON (apps.user_session_id = sessions.user_session_id AND sessions.year='`four-digit-year`' AND sessions.month='`two-digit-month`')
WHERE apps.year='`four-digit-year`'
  AND apps.month='`two-digit-month`'
ORDER BY 1, 2
```

Athena query results are stored as .csv files in an Amazon S3 bucket in your account that is named `aws-athena-query-results-`account-id-without-hyphens`-`region-code``. For ease in locating query results, choose **Save as** and provide a name for your query before you run it. You can also choose the download icon in the **Athena Results** pane to download the results of the query as a .csv file.

To enhance performance and reduce costs, Athena uses partitioning to reduce the amount
of data scanned in queries. For more information, see [Partitioning Data](../../../athena/latest/ug/partitions.md "../../../athena/latest/ug/partitions.md"). Usage reports
are partitioned in your Amazon S3 buckets by year, month, and day. You can restrict your
queries to certain date range partitions using the **year**, **month**, and **day** fields as
conditions in your queries. For example, the following query ingests only the sessions
reports for the week of May 19, 2019.

```
SELECT SUBSTRING(session_start_time, 1, 10) AS report_date,
    COUNT(DISTINCT user_session_id) AS num_sessions
FROM "appstream-usage"."sessions"
WHERE year='2019'
   AND month='05'
   AND day BETWEEN '19' and '25'
GROUP BY 1
ORDER BY 1
```

In contrast, the following query produces identical results, but because it isn't restricted to any partitions, it ingests all sessions reports stored in your Amazon S3 bucket.

```
SELECT SUBSTRING(session_start_time, 1, 10) AS report_date,
    COUNT(DISTINCT user_session_id) AS num_sessions
FROM "appstream-usage"."sessions"
WHERE session_end_time BETWEEN '2019-05-19' AND '2019-05-26'
GROUP BY 1
ORDER BY 1
```

If a session spans more than one day, the session and application records appear in the sessions and applications reports, respectively, corresponding to the day in which the session ended. For this reason, if you need to find records that relate to all sessions that were active during a given date range, consider expanding the partition set of your query by the maximum session length you have configured for your fleets.

For example, to view all sessions that were active for a given fleet during a calendar month, where the fleet had a maximum session duration of 100 hours, run the following query to expand your partition set by five days.

```
SELECT *
FROM "appstream-usage"."sessions"
WHERE fleet_name = '`fleet_name`'
   AND session_start_time BETWEEN '2019-05-01' AND '2019-06-01'
   AND year='2019'
   AND (month='05' OR (month='06' AND day<='05'))
ORDER BY session_start_time
```

The AWS CloudFormation template that created the AWS Glue crawlers also created and saved several sample queries in your Athena account that you can use to analyze your usage data. These sample queries include the following:

- Aggregated monthly session report
- Average session length per stack
- Number of sessions per day
- Total streaming hours per user

###### Note

On-demand usage charges are rounded up to the next hour for each session.

- Distinct users per app
  To use any of these queries, perform the following steps.

1. Open the Athena console at
   [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/ "https://console.aws.amazon.com/athena/").
2. Choose **Saved Queries**. The five queries noted before this procedure should
   display. The name of each query begins with "AS2." For example,
   "AS2_users_per_app_curr_mo."
3. To run a query, choose the query name rather than the option next to the name.
4. The text of the query appears in the query pane. Choose **Run query**.
   To view these queries in a separate AWS CloudFormation template, see [athena-sample-queries-appstream-usage-data_template.yml](../../../code-samples/latest/catalog/cloudformation-appstream2-athena-sample-queries-appstream-usage-data_template.md "../../../code-samples/latest/catalog/cloudformation-appstream2-athena-sample-queries-appstream-usage-data_template.md") in the _AWS Code Sample Catalog._
