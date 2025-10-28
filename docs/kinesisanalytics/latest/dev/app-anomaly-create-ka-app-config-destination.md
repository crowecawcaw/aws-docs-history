After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# Step 3: Configure

Application Output

After completing [Step 2: Create an Application](app-anom-score-create-app.md "app-anom-score-create-app.md"), you have application
code that is reading heart rate data from a streaming source and assigning an
anomaly score to each.

You can now send the application results from the in-application stream to an
external destination, which is another Kinesis data stream
(`OutputStreamTestingAnomalyScores`). You can analyze the anomaly
scores and determine which heart rate is anomalous. You can then extend this
application further to generate alerts.

Follow these steps to configure application output:

1. Open the Amazon Kinesis Data Analytics console. In the SQL editor, choose either
   **Destination** or **Add a
   destination** in the application dashboard.
2. On the **Connect to destination** page, choose the
   `OutputStreamTestingAnomalyScores` stream that you created in
   the preceding section.

Now you have an external destination, where Amazon Kinesis Data Analytics persists any records
your application writes to the in-application stream
`DESTINATION_SQL_STREAM`. 3. You can optionally configure AWS Lambda to monitor the
`OutputStreamTestingAnomalyScores` stream and send you
alerts. For instructions, see [Preprocessing Data Using a Lambda Function](lambda-preprocessing.md "lambda-preprocessing.md"). If you don't set alerts, you can
review the records that Kinesis Data Analytics writes to the external destination, which is
the Kinesis data stream `OutputStreamTestingAnomalyScores`, as
described in [Step 4: Verify Output](app-anomaly-verify-output.md "app-anomaly-verify-output.md").

###### Next Step

[Step 4: Verify Output](app-anomaly-verify-output.md "app-anomaly-verify-output.md")
