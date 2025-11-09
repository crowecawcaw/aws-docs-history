Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Create a Studio notebook with Kinesis Data Streams

This tutorial describes how to create a Studio notebook that uses a Kinesis data stream as a source.

###### This tutorial contains the following sections:

- [Complete the prerequisites](#example-notebook-streams-setup "#example-notebook-streams-setup")
- [Create an AWS Glue table](#example-notebook-streams-glue "#example-notebook-streams-glue")
- [Create a Studio notebook with Kinesis Data Streams](#example-notebook-streams-create "#example-notebook-streams-create")
- [Send data to your Kinesis data stream](#example-notebook-streams-send "#example-notebook-streams-send")
- [Test your Studio notebook](#example-notebook-streams-test "#example-notebook-streams-test")

## Complete the prerequisites

Before you create a Studio notebook, create a Kinesis data stream
(`ExampleInputStream`). Your
application uses this stream for the application source.

You can create this stream using either the Amazon Kinesis console or the following
AWS CLI command. For console instructions, see [Creating and Updating Data
Streams](../../../kinesis/latest/dev/amazon-kinesis-streams.md "../../../kinesis/latest/dev/amazon-kinesis-streams.md") in the _Amazon Kinesis Data Streams Developer Guide_. Name the stream
`ExampleInputStream` and set the **Number of open shards** to `1`.

To create the stream (`ExampleInputStream`) using the AWS CLI, use the
following Amazon Kinesis `create-stream` AWS CLI command.

```
$ aws kinesis create-stream \
--stream-name ExampleInputStream \
--shard-count 1 \
--region us-east-1 \
--profile adminuser
```

## Create an AWS Glue table

Your Studio notebook uses an [AWS Glue](../../../glue/latest/dg/what-is-glue.md "../../../glue/latest/dg/what-is-glue.md") database for metadata about
your Kinesis Data Streams data source.

###### Note

You can either manually create the database first or you can let Managed Service for Apache Flink create it for you when
you create the notebook. Similarly, you can either manually create the table as
described in this section, or you can use the create table connector code for Managed Service for Apache Flink
in your notebook within Apache Zeppelin to create your table via a DDL statement.
You can then check in AWS Glue to make sure the table was correctly created.

###### Create a Table

1. Sign in to the AWS Management Console and open the AWS Glue console at
   [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/ "https://console.aws.amazon.com/glue/").
2. If you don't already have a AWS Glue database, choose **Databases** from the left navigation bar. Choose
   **Add Database**. In the **Add database** window, enter `default` for
   **Database name**. Choose **Create**.
3. In the left navigation bar, choose **Tables**. In the **Tables** page, choose
   **Add tables**, **Add table manually**.
4. In the **Set up your table's properties** page, enter `stock` for the
   **Table name**. Make sure you select the database you created previously. Choose **Next**.
5. In the **Add a data store** page, choose **Kinesis**. For the **Stream name**,
   enter `ExampleInputStream`. For **Kinesis source URL**, choose
   enter `https://kinesis.us-east-1.amazonaws.com`. If you copy and paste the **Kinesis source URL**,
   be sure to delete any leading or trailing spaces. Choose **Next**.
6. In the **Classification** page, choose **JSON**. Choose **Next**.
7. In the **Define a Schema** page, choose Add Column to add a column. Add columns with the following properties:

| Column name | Data type |
| ----------- | --------- |
| `ticker`    | `string`  |
| `price`     | `double`  |

Choose **Next**. 8. On the next page, verify your settings, and choose **Finish**. 9. Choose your newly created table from the list of tables. 10. Choose **Edit table** and add a property with the key
`managed-flink.proctime` and the value
`proctime`. 11. Choose **Apply**.

## Create a Studio notebook with Kinesis Data Streams

Now that you have created the resources your application uses, you create your Studio notebook.

###### To create your application, you can use either the AWS Management Console or the AWS CLI.

- [Create a Studio notebook using the AWS Management Console](#example-notebook-create-streams-console "#example-notebook-create-streams-console")
- [Create a Studio notebook using the AWS CLI](#example-notebook-msk-create-api "#example-notebook-msk-create-api")

### Create a Studio notebook using the AWS Management Console

1. Open the Managed Service for Apache Flink console at
   [https://console.aws.amazon.com/managed-flink/home?region=us-east-1#/applications/dashboard](https://console.aws.amazon.com/managed-flink/home?region=us-east-1#/applications/dashboard "https://console.aws.amazon.com/managed-flink/home?region=us-east-1#/applications/dashboard").
2. In the **Managed Service for Apache Flink applications** page, choose the
   **Studio** tab. Choose **Create
   Studio notebook**.

###### Note

You can also create a Studio notebook from the Amazon MSK or Kinesis Data Streams consoles by selecting
your input Amazon MSK cluster or Kinesis data stream, and choosing
**Process data in real time**. 3. In the **Create Studio notebook** page, provide the following information:

    * Enter `MyNotebook` for the name of the notebook.
    * Choose **default** for **AWS Glue database**.

Choose **Create Studio notebook**. 4. In the **MyNotebook** page, choose **Run**. Wait for the
**Status** to show **Running**.
Charges apply when the notebook is running.

### Create a Studio notebook using the AWS CLI

To create your Studio notebook using the AWS CLI, do the following:

1. Verify your account ID. You need this value to create your application.
2. Create the role `arn:aws:iam::`AccountID`:role/ZeppelinRole` and add the following permissions to the auto-created role by console.

`"kinesis:GetShardIterator",`

`"kinesis:GetRecords",`

`"kinesis:ListShards"` 3. Create a file called `create.json` with the following contents.
Replace the placeholder values with your information.

```
{
    "ApplicationName": "MyNotebook",
    "RuntimeEnvironment": "ZEPPELIN-FLINK-3_0",
    "ApplicationMode": "INTERACTIVE",
    "ServiceExecutionRole": "arn:aws:iam::`AccountID`:role/ZeppelinRole",
    "ApplicationConfiguration": {
        "ApplicationSnapshotConfiguration": {
            "SnapshotsEnabled": false
        },
        "ZeppelinApplicationConfiguration": {
            "CatalogConfiguration": {
                "GlueDataCatalogConfiguration": {
                    "DatabaseARN": "arn:aws:glue:us-east-1:`AccountID`:database/default"
                }
            }
        }
    }
}

```

4. Run the following command to create your application:

```
aws kinesisanalyticsv2 create-application --cli-input-json file://create.json

```

5. When the command completes, you see output that shows the details for your new Studio notebook.
   The following is an example of the output.

```
{
    "ApplicationDetail": {
        "ApplicationARN": "arn:aws:kinesisanalyticsus-east-1:012345678901:application/MyNotebook",
        "ApplicationName": "MyNotebook",
        "RuntimeEnvironment": "ZEPPELIN-FLINK-3_0",
        "ApplicationMode": "INTERACTIVE",
        "ServiceExecutionRole": "arn:aws:iam::012345678901:role/ZeppelinRole",
...

```

6. Run the following command to start your application. Replace the sample value with your account ID.

```
aws kinesisanalyticsv2 start-application --application-arn arn:aws:kinesisanalyticsus-east-1:`012345678901`:application/MyNotebook\

```

## Send data to your Kinesis data stream

To send test data to your Kinesis data stream, do the following:

1. Open the [Kinesis Data Generator](https://awslabs.github.io/amazon-kinesis-data-generator/web/help.html "https://awslabs.github.io/amazon-kinesis-data-generator/web/help.html").
2. Choose **Create a Cognito User with CloudFormation**.
3. The AWS CloudFormation console opens with the Kinesis Data Generator template. Choose **Next**.
4. In the **Specify stack details** page, enter a username and password for your
   Cognito user. Choose **Next**.
5. In the **Configure stack options** page, choose **Next**.
6. In the **Review Kinesis-Data-Generator-Cognito-User** page, choose the
   **I acknowledge that AWS CloudFormation might create IAM resources.** checkbox.
   Choose **Create Stack**.
7. Wait for the AWS CloudFormation stack to finish being created. After the stack is complete,
   open the **Kinesis-Data-Generator-Cognito-User** stack in the AWS CloudFormation console,
   and choose the **Outputs** tab. Open the URL listed for the
   **KinesisDataGeneratorUrl** output value.
8. In the **Amazon Kinesis Data Generator** page, log in with the credentials
   you created in step 4.
9. On the next page, provide the following values:

|                            |                      |
| -------------------------- | -------------------- |
| **Region**                 | `us-east-1`          |
| **Stream/Firehose stream** | `ExampleInputStream` |
| **Records per second**     | `1`                  |

For **Record Template**, paste the following code:

```
{
    "ticker": "{{random.arrayElement(
        ["AMZN","MSFT","GOOG"]
    )}}",
    "price": {{random.number(
        {
            "min":10,
            "max":150
        }
    )}}
}

```

10. Choose **Send data**.
11. The generator will send data to your Kinesis data stream.

Leave the generator running while you complete the next section.

## Test your Studio notebook

In this section, you use your Studio notebook to query data from your Kinesis data
stream.

1. Open the Managed Service for Apache Flink console at
   [https://console.aws.amazon.com/managed-flink/home?region=us-east-1#/applications/dashboard](https://console.aws.amazon.com/managed-flink/home?region=us-east-1#/applications/dashboard "https://console.aws.amazon.com/managed-flink/home?region=us-east-1#/applications/dashboard").
2. On the **Managed Service for Apache Flink applications** page, choose the **Studio notebook**
   tab. Choose **MyNotebook**.
3. In the **MyNotebook** page, choose **Open in Apache Zeppelin**.

The Apache Zeppelin interface opens in a new tab. 4. In the **Welcome to Zeppelin!** page, choose **Zeppelin Note**. 5. In the **Zeppelin Note** page, enter the following query into a new note:

```
%flink.ssql(type=update)
select * from stock
```

Choose the run icon.

After a short time, the note displays data from the Kinesis data stream.

To open the Apache Flink Dashboard for your application to view operational aspects, choose **FLINK JOB**.
For more information about the Flink Dashboard, see [Apache Flink Dashboard](how-dashboard.md "how-dashboard.md")
in the [Managed Service for Apache Flink Developer Guide](../../../index.md "../../../index.md").

For more examples of Flink Streaming SQL queries, see
[Queries](https://nightlies.apache.org/flink/flink-docs-release-1.15/dev/table/sql/queries.html "https://nightlies.apache.org/flink/flink-docs-release-1.15/dev/table/sql/queries.html")
in the [Apache Flink documentation](https://nightlies.apache.org/flink/flink-docs-release-1.15/ "https://nightlies.apache.org/flink/flink-docs-release-1.15/").
