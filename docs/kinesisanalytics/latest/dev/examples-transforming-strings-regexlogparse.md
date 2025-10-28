After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# Example: Parsing Log

Strings Based on Regular Expressions (REGEX_LOG_PARSE Function)

This example uses the `REGEX_LOG_PARSE` function to transform a string in
Amazon Kinesis Data Analytics. `REGEX_LOG_PARSE` parses a string based on default Java regular
expression patterns. For more information, see [REGEX_LOG_PARSE](../sqlref/sql-reference-regex-log-parse.md "../sqlref/sql-reference-regex-log-parse.md") in
the _Amazon Managed Service for Apache Flink SQL Reference_.

In this example, you write the following records to an Amazon Kinesis stream:

```
{"LOGENTRY": "203.0.113.24 - - [25/Mar/2018:15:25:37 -0700] \"GET /index.php HTTP/1.1\" 200 125 \"-\" \"Mozilla/5.0 [en] Gecko/20100101 Firefox/52.0\""}
{"LOGENTRY": "203.0.113.24 - - [25/Mar/2018:15:25:37 -0700] \"GET /index.php HTTP/1.1\" 200 125 \"-\" \"Mozilla/5.0 [en] Gecko/20100101 Firefox/52.0\""}
{"LOGENTRY": "203.0.113.24 - - [25/Mar/2018:15:25:37 -0700] \"GET /index.php HTTP/1.1\" 200 125 \"-\" \"Mozilla/5.0 [en] Gecko/20100101 Firefox/52.0\""}
...
```

You then create an Kinesis Data Analytics application on the console, with the Kinesis
data stream as the streaming source. The discovery process reads sample records on the
streaming source and infers an in-application schema with one column (LOGENTRY), as
shown following.

![Console screenshot showing in-application schema with LOGENTRY column.](images/ex_regex_log_parse_0.png)
Then, you use the application code with the `REGEX_LOG_PARSE` function to
parse the log string to retrieve the data elements. You insert the resulting data into
another in-application stream, as shown in the following screenshot:

![Console screenshot showing the resulting data table with ROWTIME, LOGENTRY, MATCH1, and MATCH2 columns.](images/ex_regex_log_parse_1.png)

###### Topics

- [Step 1: Create a
  Kinesis Data Stream](#examples-transforming-strings-regexlogparse-1 "#examples-transforming-strings-regexlogparse-1")
- [Step 2: Create the
  Kinesis Data Analytics Application](#examples-transforming-strings-regexlogparse-2 "#examples-transforming-strings-regexlogparse-2")

## Step 1: Create a

Kinesis Data Stream

Create an Amazon Kinesis data stream and populate the log records as follows:

1. Sign in to the AWS Management Console and open the Kinesis console at
   [https://console.aws.amazon.com/kinesis](https://console.aws.amazon.com/kinesis "https://console.aws.amazon.com/kinesis").
2. Choose **Data Streams** in the navigation pane.
3. Choose **Create Kinesis stream**, and create a stream
   with one shard. For more information, see [Create a Stream](../../../streams/latest/dev/learning-kinesis-module-one-create-stream.md "../../../streams/latest/dev/learning-kinesis-module-one-create-stream.md") in the _Amazon Kinesis Data Streams Developer
   Guide_.
4. Run the following Python code to populate sample log records. This simple
   code continuously writes the same log record to the stream.

```

import json
import boto3

STREAM_NAME = "ExampleInputStream"


def get_data():
    return {
        "LOGENTRY": "203.0.113.24 - - [25/Mar/2018:15:25:37 -0700] "
        '"GET /index.php HTTP/1.1" 200 125 "-" '
        '"Mozilla/5.0 [en] Gecko/20100101 Firefox/52.0"'
    }


def generate(stream_name, kinesis_client):
    while True:
        data = get_data()
        print(data)
        kinesis_client.put_record(
            StreamName=stream_name, Data=json.dumps(data), PartitionKey="partitionkey"
        )


if __name__ == "__main__":
    generate(STREAM_NAME, boto3.client("kinesis"))

```

## Step 2: Create the

Kinesis Data Analytics Application

Next, create an Kinesis Data Analytics application as follows:

1. Open the Managed Service for Apache Flink console at
   [https://console.aws.amazon.com/kinesisanalytics](https://console.aws.amazon.com/kinesisanalytics "https://console.aws.amazon.com/kinesisanalytics").
2. Choose **Create application**, and specify an application
   name.
3. On the application details page, choose **Connect streaming
   data**.
4. On the **Connect to source** page, do the
   following:
   1. Choose the stream that you created in the preceding section.
   2. Choose the option to create an IAM role.
   3. Choose **Discover schema**. Wait for the console
      to show the inferred schema and samples records used to infer the
      schema for the in-application stream created. The inferred schema
      has only one column.
   4. Choose **Save and continue**.

5. On the application details page, choose **Go to SQL
   editor**. To start the application, choose **Yes, start
   application** in the dialog box that appears.
6. In the SQL editor, write the application code, and verify the results as
   follows:
   1. Copy the following application code and paste it into the
      editor.

   ```
   CREATE OR REPLACE STREAM "DESTINATION_SQL_STREAM" (logentry VARCHAR(24), match1 VARCHAR(24), match2 VARCHAR(24));

   CREATE OR REPLACE PUMP "STREAM_PUMP" AS INSERT INTO "DESTINATION_SQL_STREAM"
       SELECT STREAM T.LOGENTRY, T.REC.COLUMN1, T.REC.COLUMN2
       FROM
            (SELECT STREAM LOGENTRY,
                REGEX_LOG_PARSE(LOGENTRY, '(\w.+) (\d.+) (\w.+) (\w.+)') AS REC
                FROM SOURCE_SQL_STREAM_001) AS T;
   ```

   2. Choose **Save and run SQL**. On the
      **Real-time analytics** tab, you can see all
      the in-application streams that the application created and verify
      the data.
