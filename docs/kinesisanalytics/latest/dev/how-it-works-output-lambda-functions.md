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

Application Destinations

Your Kinesis Data Analytics application can use AWS Lambda functions as an output. Kinesis Data Analytics provides
templates for creating Lambda functions to use as a destination for your
applications. Use these templates as a starting point for post-processing output
from your application.

###### Topics

- [Creating a Lambda Function
  Destination in Node.js](#how-it-works-lambda-dest-nodejs "#how-it-works-lambda-dest-nodejs")
- [Creating a Lambda Function
  Destination in Python](#how-it-works-lambda-dest-python "#how-it-works-lambda-dest-python")
- [Creating a Lambda Function
  Destination in Java](#how-it-works-lambda-dest-java "#how-it-works-lambda-dest-java")
- [Creating a Lambda Function Destination
  in .NET](#how-it-works-lambda-net "#how-it-works-lambda-net")

## Creating a Lambda Function

Destination in Node.js

The following template for creating a destination Lambda function in Node.js is
available on the console:

| Lambda as Output Blueprint | Language and Version | Description                                                                                  |
| -------------------------- | -------------------- | -------------------------------------------------------------------------------------------- |
| `kinesis-analytics-output` | Node.js 12.x         | Deliver output records from a Kinesis Data Analytics application to a custom<br>destination. |

## Creating a Lambda Function

Destination in Python

The following templates for creating a destination Lambda function in Python
are available on the console:

| Lambda as Output Blueprint     | Language and Version | Description                                                                             |
| ------------------------------ | -------------------- | --------------------------------------------------------------------------------------- |
| `kinesis-analytics-output-sns` | Python 2.7           | Deliver output records from a Kinesis Data Analytics application to<br>Amazon SNS.      |
| `kinesis-analytics-output-ddb` | Python 2.7           | Deliver output records from a Kinesis Data Analytics application to<br>Amazon DynamoDB. |

## Creating a Lambda Function

Destination in Java

To create a destination Lambda function in Java, use the [Java events](https://github.com/aws/aws-lambda-java-libs/tree/master/aws-lambda-java-events/src/main/java/com/amazonaws/services/lambda/runtime/events "https://github.com/aws/aws-lambda-java-libs/tree/master/aws-lambda-java-events/src/main/java/com/amazonaws/services/lambda/runtime/events") classes.

The following code demonstrates a sample destination Lambda function using
Java:

```
public class LambdaFunctionHandler
        implements RequestHandler<KinesisAnalyticsOutputDeliveryEvent, KinesisAnalyticsOutputDeliveryResponse> {

    @Override
    public KinesisAnalyticsOutputDeliveryResponse handleRequest(KinesisAnalyticsOutputDeliveryEvent event,
            Context context) {
        context.getLogger().log("InvocatonId is : " + event.invocationId);
        context.getLogger().log("ApplicationArn is : " + event.applicationArn);

        List<KinesisAnalyticsOutputDeliveryResponse.Record> records = new ArrayList<KinesisAnalyticsOutputDeliveryResponse.Record>();
        KinesisAnalyticsOutputDeliveryResponse response = new KinesisAnalyticsOutputDeliveryResponse(records);

        event.records.stream().forEach(record -> {
            context.getLogger().log("recordId is : " + record.recordId);
            context.getLogger().log("record retryHint is :" + record.lambdaDeliveryRecordMetadata.retryHint);
            // Add logic here to transform and send the record to final destination of your choice.
            response.records.add(new Record(record.recordId, KinesisAnalyticsOutputDeliveryResponse.Result.Ok));
        });
        return response;
    }

}

```

## Creating a Lambda Function Destination

in .NET

To create a destination Lambda function in .NET, use the [.NET events](https://github.com/aws/aws-lambda-dotnet/tree/master/Libraries/src/Amazon.Lambda.KinesisAnalyticsEvents "https://github.com/aws/aws-lambda-dotnet/tree/master/Libraries/src/Amazon.Lambda.KinesisAnalyticsEvents") classes.

The following code demonstrates a sample destination Lambda function using
C#:

```
public class Function
    {
        public KinesisAnalyticsOutputDeliveryResponse FunctionHandler(KinesisAnalyticsOutputDeliveryEvent evnt, ILambdaContext context)
        {
            context.Logger.LogLine($"InvocationId: {evnt.InvocationId}");
            context.Logger.LogLine($"ApplicationArn: {evnt.ApplicationArn}");

            var response = new KinesisAnalyticsOutputDeliveryResponse
            {
                Records = new List<KinesisAnalyticsOutputDeliveryResponse.Record>()
            };

            foreach (var record in evnt.Records)
            {
                context.Logger.LogLine($"\tRecordId: {record.RecordId}");
                context.Logger.LogLine($"\tRetryHint: {record.RecordMetadata.RetryHint}");
                context.Logger.LogLine($"\tData: {record.DecodeData()}");

                // Add logic here to send to the record to final destination of your choice.

                var deliveredRecord = new KinesisAnalyticsOutputDeliveryResponse.Record
                {
                    RecordId = record.RecordId,
                    Result = KinesisAnalyticsOutputDeliveryResponse.OK
                };
                response.Records.Add(deliveredRecord);
            }
            return response;
        }
    }
```

For more information about creating Lambda functions for pre-processing and
destinations in .NET, see [`Amazon.Lambda.KinesisAnalyticsEvents`](https://github.com/aws/aws-lambda-dotnet/tree/master/Libraries/src/Amazon.Lambda.KinesisAnalyticsEvents "https://github.com/aws/aws-lambda-dotnet/tree/master/Libraries/src/Amazon.Lambda.KinesisAnalyticsEvents").
