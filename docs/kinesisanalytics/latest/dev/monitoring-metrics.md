After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# Metrics and Dimensions

The `AWS/KinesisAnalytics` namespace includes the following metrics.

| Metric                                    | Description                                                                                                                                                                                                                                       |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| `Bytes`                                   | The number of bytes read (per input stream) or written (per output stream). Levels: Per input stream and per output stream                                                                                                                        |
| `KPUs`                                    | The number of Kinesis Processing Units that are used to run your stream processing application. The average number of KPUs used each hour determines the billing for your application. Levels: Application-level                                  |
| `MillisBehindLatest`                      | Indicates how far behind from the current time an application is reading from the streaming source. Levels: Application-level                                                                                                                     |
| `Records`                                 | The number of records read (per input stream) or written (per output stream). Levels: Per input stream and per output stream                                                                                                                      |
| `Success`                                 | 1 for each successful delivery attempt to the destination configured for your application; 0 for every failed delivery attempt. The average value of this metric indicates how many successful deliveries are performed. Levels: Per destination. |
| `InputProcessing.Duration`                | The time taken for each AWS Lambda function invocation performed by . Levels: Per input stream                                                                                                                                                    |
| `InputProcessing.OkRecords`               | The number of records returned by a Lambda function that were marked with `Ok` status. Levels: Per input stream                                                                                                                                   |
| `InputProcessing.OkBytes`                 | The sum of bytes of the records returned by a Lambda function that were marked with `Ok` status. Levels: Per input stream                                                                                                                         |
| `InputProcessing.DroppedRecords`          | The number of records returned by a Lambda function that were marked with `Dropped` status. Levels: Per input stream                                                                                                                              |
| `InputProcessing.ProcessingFailedRecords` | The number of records returned by a Lambda function that were marked with `ProcessingFailed` status. Levels: Per input stream                                                                                                                     |
| `InputProcessing.Success`                 | The number of successful Lambda invocations by . Levels: Per input stream                                                                                                                                                                         |
| `LambdaDelivery.OkRecords`                | The number of records returned by a Lambda function that were marked with `Ok` status. Levels: Per Lambda destination                                                                                                                             |
| `LambdaDelivery.DeliveryFailedRecords`    | The number of records returned by a Lambda function that were marked with `DeliveryFailed` status. Levels: Per Lambda destination                                                                                                                 |
| `LambdaDelivery.Duration`                 | The time taken for each Lambda function invocation performed by . Levels: Per Lambda destination                                                                                                                                                  | provides metrics for the following dimensions. |
| Dimension                                 | Description                                                                                                                                                                                                                                       |
| ---                                       | ---                                                                                                                                                                                                                                               |
| `Flow`                                    | Per input stream: Input Per output stream: Output                                                                                                                                                                                                 |
| `Id`                                      | Per input stream: Input Id Per output stream: Output Id                                                                                                                                                                                           |
