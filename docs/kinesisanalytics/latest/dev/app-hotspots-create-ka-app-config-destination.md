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

the Application Output

At this point in the [Hotspots
example](app-hotspots-detection.md "app-hotspots-detection.md"), you have Amazon Kinesis Data Analytics application code discovering significant
hotspots from a streaming source and assigning a heat score to each.

You can now send the application result from the in-application stream to an
external destination, which is another Kinesis data stream
(`ExampleOutputStream`). You can then analyze the hotspot scores and
determine what an appropriate threshold is for hotspot heat. You can extend this
application further to generate alerts.

###### To configure the application output

1. Open the Kinesis Data Analytics console at [https://console.aws.amazon.com/kinesisanalytics](https://console.aws.amazon.com/kinesisanalytics "https://console.aws.amazon.com/kinesisanalytics").
2. In the SQL editor, choose either **Destination** or
   **Add a destination** in the application dashboard.
3. On the **Add a destination** page, choose
   **Select from your streams**. Then choose the
   `ExampleOutputStream` stream that you created in the
   preceding section.

Now you have an external destination, where Amazon Kinesis Data Analytics persists any
records, your application writes to the in-application stream
`DESTINATION_SQL_STREAM`. 4. You can optionally configure AWS Lambda to monitor the
`ExampleOutputStream` stream and send you alerts. For
more information, see [Using a Lambda Function as Output](how-it-works-output-lambda.md "how-it-works-output-lambda.md"). You can also review the
records that Kinesis Data Analytics writes to the external destination, which is the Kinesis
stream `ExampleOutputStream`, as described in [Step 4: Verify the Application
Output](app-hotspots-verify-output.md "app-hotspots-verify-output.md").

###### Next Step

[Step 4: Verify the Application
Output](app-hotspots-verify-output.md "app-hotspots-verify-output.md")
