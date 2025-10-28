After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# Example: Creating Simple Alerts

In this Kinesis Data Analytics application, the query runs continuously on the
in-application stream that is created over the demo stream. For more information, see
[Continuous Queries](continuous-queries-concepts.md "continuous-queries-concepts.md").

If any rows show a stock price change that is greater than 1 percent, those rows are
inserted into another in-application stream. In the exercise, you can configure the
application output to persist the results to an external destination. You can then
further investigate the results. For example, you can use an AWS Lambda function to
process records and send you alerts.

###### To create a simple alerts application

1. Create the analytics application as described in the Kinesis Data Analytics [Getting Started](get-started-exercise.md "get-started-exercise.md")
   exercise.
2. In the SQL editor in Kinesis Data Analytics, replace the application code with the following:

```
CREATE OR REPLACE STREAM "DESTINATION_SQL_STREAM"
           (ticker_symbol VARCHAR(4),
            sector        VARCHAR(12),
            change        DOUBLE,
            price         DOUBLE);

CREATE OR REPLACE PUMP "STREAM_PUMP" AS
   INSERT INTO "DESTINATION_SQL_STREAM"
      SELECT STREAM ticker_symbol, sector, change, price
      FROM   "SOURCE_SQL_STREAM_001"
      WHERE  (ABS(Change / (Price - Change)) * 100) > 1;
```

The `SELECT` statement in the application code filters rows in the
`SOURCE_SQL_STREAM_001` for stock price changes greater than 1
percent. It then inserts those rows into another in-application stream
`DESTINATION_SQL_STREAM` using a pump. For more information about
the coding pattern that explains using pumps to insert rows into in-application
streams, see [Application Code](how-it-works-app-code.md "how-it-works-app-code.md"). 3. Choose **Save and run SQL**. 4. Add a destination. To do this, either choose the
**Destination** tab in the SQL editor or choose
**Add a destination** on the application details
page.

    1. In the SQL editor, choose the **Destination** tab,
     and then choose **Connect to a destination**.


    On the **Connect to destination** page, choose
     **Create New**.
    2. Choose **Go to Kinesis Streams**.
    3. On the Amazon Kinesis Data Streams console, create a new Kinesis stream (for example,
     `gs-destination`) with one shard. Wait until the stream
     status is **ACTIVE**.
    4. Return to the Kinesis Data Analytics console. On the **Connect to
     destination** page, choose the stream that you created.


    If the stream does not appear, refresh the page.
    5. Choose **Save and continue**.Now you have an external destination, a Kinesis data stream, where Kinesis Data Analytics persists

your application output in the `DESTINATION_SQL_STREAM`
in-application stream. 5. Configure AWS Lambda to monitor the Kinesis stream you created and invoke a Lambda
function.

For instructions, see [Preprocessing Data Using a Lambda Function](lambda-preprocessing.md "lambda-preprocessing.md").
