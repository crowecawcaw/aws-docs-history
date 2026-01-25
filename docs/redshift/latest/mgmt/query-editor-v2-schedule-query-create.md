Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Creating a query schedule with

query editor v2

You can create a schedule to run a SQL statement with Amazon Redshift query editor v2. You create a
schedule to run your SQL statement at the time intervals that match your business needs.
When it's time for the scheduled query to run, the query is started by Amazon EventBridge and
uses the Amazon Redshift Data API.

###### To create a schedule to run a SQL statement

1. On the **Editor**

![Editor](images/qev2-align-left.png)
view, choose
![Schedule](images/qev2-calendar.png)

**Schedule** to create a schedule to run a SQL
statement. 2. When you define the schedule, you provide the following information.

    * The IAM role that assumes the required permissions to run the query.
     This IAM role is also attached to your cluster or workgroup.
    * The authentication values for either AWS Secrets Manager or temporary
     credentials to authorize access your cluster or workgroup. These
     authentication methods are supported by the Data API. For more
     information, see [Authenticating a
     scheduled query](query-editor-v2-schedule-query-authentication.md "query-editor-v2-schedule-query-authentication.md").
    * The cluster or workgroup where your database resides.
    * The name of the database that contains the data to be queried.
    * The name of the scheduled query and its description. The query editor v2
     prefixes the scheduled query name you provide with "QS2-". The query
     editor v1 prefixes its scheduled query names with "QS-".
    * The SQL statement to be run on the schedule.
    * The schedule frequency and repeat options or a cron formatted value
     that defines the schedule. For more information, see [Cron Expressions](../../../AmazonCloudWatch/latest/events/ScheduledEvents.md#CronExpressions "../../../AmazonCloudWatch/latest/events/ScheduledEvents.md#CronExpressions") in the
     *Amazon CloudWatch Events User Guide*.
    * Optionally, you can enable standard Amazon SNS notifications to monitor the
     scheduled query. You might need to confirm the email address you provide
     to the Amazon SNS notification. Check your email for a link to confirm the
     email address for the Amazon SNS notification. For more information, see
     [Email
     notifications](../../../sns/latest/dg/sns-email-notifications.md "../../../sns/latest/dg/sns-email-notifications.md") in the *Amazon Simple Notification Service Developer Guide*. If
     your query is being run but you don't see messages published in your SNS
     topic, see  [My rule runs, but I don't see any messages published into my Amazon SNS
     topic](../../../eventbridge/latest/userguide/eventbridge-troubleshooting.md#eb-no-messages-published-sns "../../../eventbridge/latest/userguide/eventbridge-troubleshooting.md#eb-no-messages-published-sns") in the *Amazon EventBridge User Guide*.

3. Choose **Schedule query** to save and activate the schedule
   and add the schedule to the list of queries in the **Scheduled
   queries** view.
   The **Scheduled queries**

![Scheduled queries](images/qev2-calendar.png)
view lists all the scheduled queries for your clusters and
workgroups. With this view, you can display schedule query details, activate or
deactivate the schedule, edit the schedule, and delete the scheduled query. When you
view query details, you can also view the history of running the query with the
schedule.

###### Note

A schedule query run is only available in the **Schedule
history** list for 24 hours. Queries that run on a schedule don't
appear in the **Query history** view of query editor v2.

## Demo of scheduling a

query

For a demo of scheduling a query, watch the following video.
