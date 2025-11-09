After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# Preprocessing Data Using a Lambda Function

###### Note

After September 12, 2023, you will not able to create new applications using Kinesis Data Firehose as a source if you do not already use Kinesis Data Analytics for SQL. For more information, see [Limits](limits.md "limits.md").

If the data in your stream needs format conversion, transformation, enrichment, or
filtering, you can preprocess the data using an AWS Lambda function. You can do this
before your application SQL code executes or before your application creates a schema
from your data stream.

Using a Lambda function for preprocessing records is useful in the following
scenarios:

- Transforming records from other formats (such as KPL or GZIP) into formats
  that Kinesis Data Analytics can analyze. Kinesis Data Analytics currently supports JSON or CSV data
  formats.
- Expanding data into a format that is more accessible for operations such as
  aggregation or anomaly detection. For instance, if several data values are
  stored together in a string, you can expand the data into separate
  columns.
- Data enrichment with other Amazon services, such as extrapolation or error
  correction.
- Applying complex string transformation to record fields.
- Data filtering for cleaning up the data.

## Using a Lambda Function for Preprocessing

Records

When creating your Kinesis Data Analytics application, you enable Lambda preprocessing in the
**Connect to a Source** page.

###### To use a Lambda function to preprocess records in a Kinesis Data Analytics application

1. Sign in to the AWS Management Console and open the Managed Service for Apache Flink console at
   [https://console.aws.amazon.com/kinesisanalytics](https://console.aws.amazon.com/kinesisanalytics "https://console.aws.amazon.com/kinesisanalytics").
2. On the **Connect to a Source** page for your application,
   choose **Enabled** in the **Record pre-processing
   with AWS Lambda** section.
3. To use a Lambda function that you have already created, choose the function
   in the **Lambda function** drop-down list.
4. To create a new Lambda function from one of the Lambda preprocessing
   templates, choose the template from the drop-down list. Then choose
   **View <template name> in Lambda** to edit the
   function.
5. To create a new Lambda function, choose **Create new**.
   For information about creating a Lambda function, see [Create a
   HelloWorld Lambda Function and Explore the Console](../../../lambda/latest/dg/getting-started-create-function.md "../../../lambda/latest/dg/getting-started-create-function.md") in the
   _AWS Lambda Developer Guide_.
6. Choose the version of the Lambda function to use. To use the latest
   version, choose **$LATEST**.

When you choose or create a Lambda function for record preprocessing, the records
are preprocessed before your application SQL code executes or your application
generates a schema from the records.

## Lambda Preprocessing

Permissions

To use Lambda preprocessing, the application's IAM role requires the following
permissions policy:

```
     {
       "Sid": "UseLambdaFunction",
       "Effect": "Allow",
       "Action": [
           "lambda:InvokeFunction",
           "lambda:GetFunctionConfiguration"
       ],
       "Resource": "<FunctionARN>"
   }

```

## Lambda Preprocessing Metrics

You can use Amazon CloudWatch to monitor the number of Lambda invocations, bytes processed,
successes and failures, and so on. For information about CloudWatch metrics that are
emitted by Kinesis Data Analytics Lambda preprocessing, see [Amazon Kinesis Analytics
Metrics](../../../AmazonCloudWatch/latest/monitoring/aka-metricscollected.md "../../../AmazonCloudWatch/latest/monitoring/aka-metricscollected.md").

## Using AWS Lambda with the Kinesis

Producer Library

The [Kinesis Producer Library](../../../streams/latest/dev/developing-producers-with-kpl.md "../../../streams/latest/dev/developing-producers-with-kpl.md") (KPL) aggregates small user-formatted records
into larger records up to 1 MB to make better use of Amazon Kinesis Data Streams throughput. The Kinesis
Client Library (KCL) for Java supports deaggregating these records. However, you
must use a special module to deaggregate the records when you use AWS Lambda as the
consumer of your streams.

To get the necessary project code and instructions, see the [Kinesis Producer Library
Deaggregation Modules for AWS Lambda](https://github.com/awslabs/kinesis-deaggregation "https://github.com/awslabs/kinesis-deaggregation") on GitHub. You can use the
components in this project to process KPL serialized data within AWS Lambda in Java,
Node.js, and Python. You can also use these components as part of a [multi-lang KCL application](https://github.com/awslabs/amazon-kinesis-client/blob/master/amazon-kinesis-client-multilang/src/main/java/software/amazon/kinesis/multilang/package-info.java "https://github.com/awslabs/amazon-kinesis-client/blob/master/amazon-kinesis-client-multilang/src/main/java/software/amazon/kinesis/multilang/package-info.java").

## Data Preprocessing Event Input

Data Model/Record Response Model

To preprocess records, your Lambda function must be compliant with the required
event input data and record response models.

### Event Input Data

Model

Kinesis Data Analytics continuously reads data from your Kinesis data stream or Firehose delivery
stream. For each batch of records it retrieves, the service manages how each
batch gets passed to your Lambda function. Your function receives a list of
records as input. Within your function, you iterate through the list and apply
your business logic to accomplish your preprocessing requirements (such as data
format conversion or enrichment).

The input model to your preprocessing function varies slightly, depending on
whether the data was received from a Kinesis data stream or a Firehose delivery
stream.

If the source is a Firehose delivery stream, the event input data model is as
follows:

**Kinesis Data Firehose Request Data
Model**

| Field            | Description                                                   |
| ---------------- | ------------------------------------------------------------- | ----------- | ---- | ------- | ------- | ---- | ---------- | ----------------------- | ---- | ------------------------------- | --- | ----- | ----------- | ---- | ------- | ------- | ---- | ----------------------------- | -------------------------------------------------- | --- | ---- | ------ | --------------------------------------- | --- |
| `invocationId`   | The Lambda invocation Id (random GUID).                       |
| `applicationArn` | Kinesis Data Analytics application Amazon Resource Name (ARN) |
| `streamArn`      | Delivery stream ARN                                           |
| records<br>      | Field                                                         | Description | <br> | --<br>• | --<br>• | <br> | `recordId` | record ID (random GUID) | <br> | `kinesisFirehoseRecordMetadata` |     | Field | Description | <br> | --<br>• | --<br>• | <br> | `approximateArrivalTimestamp` | Delivery stream record approximate arrival<br>time |     | <br> | `data` | Base64-encoded source record<br>payload |     |

The following example shows input from a Firehose delivery stream:

```
{
   "invocationId":"00540a87-5050-496a-84e4-e7d92bbaf5e2",
   "applicationArn":"arn:aws:kinesisanalytics:us-east-1:12345678911:application/lambda-test",
   "streamArn":"arn:aws:firehose:us-east-1:AAAAAAAAAAAA:deliverystream/lambda-test",
   "records":[
      {
         "recordId":"49572672223665514422805246926656954630972486059535892482",
         "data":"aGVsbG8gd29ybGQ=",
         "kinesisFirehoseRecordMetadata":{
            "approximateArrivalTimestamp":1520280173
         }
      }
   ]
}

```

If the source is a Kinesis data stream, the event input data model is as
follows:

**Kinesis Streams Request Data Model**

| Field            | Description                             |
| ---------------- | --------------------------------------- | ----------- | ---- | ------- | ------- | ---- | ---------- | -------------------------------------------------------- | ---- | ----------------------------- | --- | ----- | ----------- | ---- | ------- | ------- | ---- | ---------------- | ------------------------------------------------- | ---- | -------------- | ----------------------------------------------- | ---- | --------- | ------------------------------------------- | ---- | ----------------------------- | -------------------------------------------------- | --- | ---- | ---- | --------------------------------------- | --- |
| `invocationId`   | The Lambda invocation Id (random GUID). |
| `applicationArn` | Kinesis Data Analytics application ARN  |
| `streamArn`      | Delivery stream ARN                     |
| records<br>      | Field                                   | Description | <br> | --<br>• | --<br>• | <br> | `recordId` | record ID based off of Kinesis record<br>sequence number | <br> | `kinesisStreamRecordMetadata` |     | Field | Description | <br> | --<br>• | --<br>• | <br> | `sequenceNumber` | Sequence number from the Kinesis stream<br>record | <br> | `partitionKey` | Partition key from the Kinesis stream<br>record | <br> | `shardId` | `ShardId` from the Kinesis<br>stream record | <br> | `approximateArrivalTimestamp` | Delivery stream record approximate arrival<br>time |     | <br> | data | Base64-encoded source record<br>payload |     |

The following example shows input from a Kinesis data stream:

```

{
  "invocationId": "00540a87-5050-496a-84e4-e7d92bbaf5e2",
  "applicationArn": "arn:aws:kinesisanalytics:us-east-1:12345678911:application/lambda-test",
  "streamArn": "arn:aws:kinesis:us-east-1:AAAAAAAAAAAA:stream/lambda-test",
  "records": [
    {
      "recordId": "49572672223665514422805246926656954630972486059535892482",
      "data": "aGVsbG8gd29ybGQ=",
      "kinesisStreamRecordMetadata":{
            "shardId" :"shardId-000000000003",
            "partitionKey":"7400791606",
            "sequenceNumber":"49572672223665514422805246926656954630972486059535892482",
            "approximateArrivalTimestamp":1520280173
         }
    }
  ]
}

```

### Record Response

Model

All records returned from your Lambda preprocessing function (with record IDs)
that are sent to the Lambda function must be returned. They must contain the
following parameters, or Kinesis Data Analytics rejects them and treats it as a data
preprocessing failure. The data payload part of the record can be transformed to
accomplish preprocessing requirements.

**Response Data Model**

|             |       |             |      |         |         |      |            |                                                                                                                                                                                                                                                                                                 |
| ----------- | ----- | ----------- | ---- | ------- | ------- | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- |
| records<br> | Field | Description | <br> | --<br>• | --<br>• | <br> | `recordId` | The record ID is passed from Kinesis Data Analytics to<br>Lambda during the invocation. The transformed<br>record must contain the same record ID. Any<br>mismatch between the ID of the original record and<br>the ID of the transformed record is treated as a<br>data preprocessing failure. | <br> | `result` | The status of the data transformation of<br>the record. The possible values are:<br>• `Ok`: The record was transformed<br>successfully. Kinesis Data Analytics ingests the record for SQL<br>processing.<br>• `Dropped`: The record was dropped<br>intentionally by your processing logic. Kinesis Data Analytics<br>drops the record from SQL processing. The data<br>payload field is optional for a<br>`Dropped` record.<br>• `ProcessingFailed`: The record<br>could not be transformed. Kinesis Data Analytics considers it<br>unsuccessfully processed by your Lambda function<br>and writes an error to the error stream. For more<br>information about the error stream, see [Error Handling](error-handling.md "error-handling.md"). The data payload field<br>is optional for a `ProcessingFailed`<br>record. | <br> | `data` | The transformed data payload, after<br>base64-encoding. Each data payload can contain<br>multiple JSON documents if the application<br>ingestion data format is JSON. Or each can contain<br>multiple CSV rows (with a row delimiter specified<br>in each row) if the application ingestion data<br>format is CSV. The Kinesis Data Analytics service successfully<br>parses and processes data with either multiple<br>JSON documents or CSV rows within the same data<br>payload. |     |

The following example shows output from a Lambda function:

```
{
  "records": [
    {
      "recordId": "49572672223665514422805246926656954630972486059535892482",
      "result": "Ok",
      "data": "SEVMTE8gV09STEQ="
    }
  ]
}

```

## Common Data Preprocessing

Failures

The following are common reasons why preprocessing can fail.

- Not all records (with record IDs) in a batch that are sent to the Lambda
  function are returned back to the Kinesis Data Analytics service.
- The response is missing either the record ID, status, or data payload
  field. The data payload field is optional for a `Dropped` or
  `ProcessingFailed` record.
- The Lambda function timeouts are not sufficient to preprocess the
  data.
- The Lambda function response exceeds the response limits imposed by the
  AWS Lambda service.

For data preprocessing failures, Kinesis Data Analytics continues to retry Lambda invocations on the
same set of records until successful. You can monitor the following CloudWatch metrics to
gain insight into failures.

- Kinesis Data Analytics application `MillisBehindLatest`: Indicates how far
  behind an application is reading from the streaming source.
- Kinesis Data Analytics application `InputPreprocessing` CloudWatch metrics: Indicates
  the number of successes and failures, among other statistics. For more
  information, see [Amazon
  Kinesis Analytics Metrics](../../../AmazonCloudWatch/latest/monitoring/aka-metricscollected.md "../../../AmazonCloudWatch/latest/monitoring/aka-metricscollected.md").
- AWS Lambda function CloudWatch metrics and logs.
