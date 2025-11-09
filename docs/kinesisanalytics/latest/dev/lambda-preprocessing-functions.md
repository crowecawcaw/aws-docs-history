After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# Creating Lambda Functions for

Preprocessing

Your Amazon Kinesis Data Analytics application can use Lambda functions for preprocessing records as
they are ingested into the application. Kinesis Data Analytics provides the following templates on
the console to use as a starting point for preprocessing your data.

###### Topics

- [Creating a Preprocessing
  Lambda Function in Node.js](#lambda-preprocessing-functions-nodejs "#lambda-preprocessing-functions-nodejs")
- [Creating a Preprocessing
  Lambda Function in Python](#lambda-preprocessing-functions-python "#lambda-preprocessing-functions-python")
- [Creating a Preprocessing
  Lambda Function in Java](#lambda-preprocessing-functions-java "#lambda-preprocessing-functions-java")
- [Creating a Preprocessing
  Lambda Function in .NET](#lambda-preprocessing-functions-net "#lambda-preprocessing-functions-net")

## Creating a Preprocessing

Lambda Function in Node.js

The following templates for creating preprocessing Lambda function in Node.js
are available on the Kinesis Data Analytics console:

| Lambda Blueprint                                | Language and version | Description                                                                                                                                                                                                              |
| ----------------------------------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| General Kinesis Data Analytics Input Processing | Node.js 6.10         | A Kinesis Data Analytics record preprocessor that receives JSON or CSV<br>records as input and then returns them with a processing<br>status. Use this processor as a starting point for custom<br>transformation logic. |
| Compressed Input Processing                     | Node.js 6.10         | A Kinesis Data Analytics record processor that receives compressed (GZIP or<br>Deflate compressed) JSON or CSV records as input and returns<br>decompressed records with a processing status.                            |

## Creating a Preprocessing

Lambda Function in Python

The following templates for creating preprocessing Lambda function in Python
are available on the console:

| Lambda Blueprint                           | Language and version | Description                                                                                                                                                                                                              |
| ------------------------------------------ | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| General Kinesis Analytics Input Processing | Python 2.7           | A Kinesis Data Analytics record preprocessor that receives JSON or CSV<br>records as input and then returns them with a processing<br>status. Use this processor as a starting point for custom<br>transformation logic. |
| KPL Input Processing                       | Python 2.7           | A Kinesis Data Analytics record processor that receives Kinesis Producer<br>Library (KPL) aggregates of JSON or CSV records as input and<br>returns disaggregated records with a processing status.                      |

## Creating a Preprocessing

Lambda Function in Java

To create a Lambda function in Java for preprocessing records, use the [Java events](https://github.com/aws/aws-lambda-java-libs/tree/master/aws-lambda-java-events/src/main/java/com/amazonaws/services/lambda/runtime/events "https://github.com/aws/aws-lambda-java-libs/tree/master/aws-lambda-java-events/src/main/java/com/amazonaws/services/lambda/runtime/events") classes.

The following code demonstrates a sample Lambda function that preprocesses
records using Java:

```
public class LambdaFunctionHandler implements
        RequestHandler<KinesisAnalyticsStreamsInputPreprocessingEvent, KinesisAnalyticsInputPreprocessingResponse> {

    @Override
    public KinesisAnalyticsInputPreprocessingResponse handleRequest(
            KinesisAnalyticsStreamsInputPreprocessingEvent event, Context context) {
        context.getLogger().log("InvocatonId is : " + event.invocationId);
        context.getLogger().log("StreamArn is : " + event.streamArn);
        context.getLogger().log("ApplicationArn is : " + event.applicationArn);

        List<KinesisAnalyticsInputPreprocessingResponse.Record> records = new ArrayList<KinesisAnalyticsInputPreprocessingResponse.Record>();
        KinesisAnalyticsInputPreprocessingResponse response = new KinesisAnalyticsInputPreprocessingResponse(records);

        event.records.stream().forEach(record -> {
            context.getLogger().log("recordId is : " + record.recordId);
            context.getLogger().log("record aat is :" + record.kinesisStreamRecordMetadata.approximateArrivalTimestamp);
             // Add your record.data pre-processing logic here.
            // response.records.add(new Record(record.recordId, KinesisAnalyticsInputPreprocessingResult.Ok, <preprocessedrecordData>));
        });
        return response;
    }

}

```

## Creating a Preprocessing

Lambda Function in .NET

To create a Lambda function in .NET for preprocessing records, use the [.NET events](https://github.com/aws/aws-lambda-dotnet/tree/master/Libraries/src/Amazon.Lambda.KinesisAnalyticsEvents "https://github.com/aws/aws-lambda-dotnet/tree/master/Libraries/src/Amazon.Lambda.KinesisAnalyticsEvents") classes.

The following code demonstrates a sample Lambda function that preprocesses
records using C#:

```
public class Function
    {
        public KinesisAnalyticsInputPreprocessingResponse FunctionHandler(KinesisAnalyticsStreamsInputPreprocessingEvent evnt, ILambdaContext context)
        {
            context.Logger.LogLine($"InvocationId: {evnt.InvocationId}");
            context.Logger.LogLine($"StreamArn: {evnt.StreamArn}");
            context.Logger.LogLine($"ApplicationArn: {evnt.ApplicationArn}");

            var response = new KinesisAnalyticsInputPreprocessingResponse
            {
                Records = new List<KinesisAnalyticsInputPreprocessingResponse.Record>()
            };

            foreach (var record in evnt.Records)
            {
                context.Logger.LogLine($"\tRecordId: {record.RecordId}");
                context.Logger.LogLine($"\tShardId: {record.RecordMetadata.ShardId}");
                context.Logger.LogLine($"\tPartitionKey: {record.RecordMetadata.PartitionKey}");
                context.Logger.LogLine($"\tRecord ApproximateArrivalTime: {record.RecordMetadata.ApproximateArrivalTimestamp}");
                context.Logger.LogLine($"\tData: {record.DecodeData()}");

                // Add your record preprocessig logic here.

                var preprocessedRecord = new KinesisAnalyticsInputPreprocessingResponse.Record
                {
                    RecordId = record.RecordId,
                    Result = KinesisAnalyticsInputPreprocessingResponse.OK
                };
                preprocessedRecord.EncodeData(record.DecodeData().ToUpperInvariant());
                response.Records.Add(preprocessedRecord);
            }
            return response;
        }
    }
```

For more information about creating Lambda functions for preprocessing and
destinations in .NET, see [`Amazon.Lambda.KinesisAnalyticsEvents`](https://github.com/aws/aws-lambda-dotnet/tree/master/Libraries/src/Amazon.Lambda.KinesisAnalyticsEvents "https://github.com/aws/aws-lambda-dotnet/tree/master/Libraries/src/Amazon.Lambda.KinesisAnalyticsEvents").
