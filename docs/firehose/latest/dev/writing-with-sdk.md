

# Send data with AWS SDK
<a name="writing-with-sdk"></a>

You can use the [Amazon Data Firehose API](https://docs.aws.amazon.com/firehose/latest/APIReference/) to send data to a Firehose stream using the [AWS SDK for Java](https://aws.amazon.com/sdk-for-java/), [.NET](https://aws.amazon.com/sdk-for-net/), [Node.js](https://aws.amazon.com/sdk-for-javascript/), [Python](https://aws.amazon.com/sdk-for-python/), or [Ruby](https://aws.amazon.com/sdk-for-ruby/). If you are new to Amazon Data Firehose, take some time to become familiar with the concepts and terminology presented in [What is Amazon Data Firehose?](what-is-this-service.md). For more information, see [Start Developing with Amazon Web Services](http://aws.amazon.com/developers/getting-started/).

These examples do not represent production-ready code, in that they do not check for all possible exceptions, or account for all possible security or performance considerations. 

The Amazon Data Firehose API offers two operations for sending data to your Firehose stream: [PutRecord](https://docs.aws.amazon.com/firehose/latest/APIReference/API_PutRecord.html) and [PutRecordBatch](https://docs.aws.amazon.com/firehose/latest/APIReference/API_PutRecordBatch.html). `PutRecord()` sends one data record within one call and `PutRecordBatch()` can send multiple data records within one call. 

## Single write operations using PutRecord
<a name="putrecord"></a>

Putting data requires only the Firehose stream name and a byte buffer (<=1000 KB). Because Amazon Data Firehose batches multiple records before loading the file into Amazon S3, you may want to add a record separator. To put data one record at a time into a Firehose stream, use the following code:

```
PutRecordRequest putRecordRequest = new PutRecordRequest();
putRecordRequest.setDeliveryStreamName(deliveryStreamName);

String data = line + "\n";

Record record = new Record().withData(ByteBuffer.wrap(data.getBytes()));
putRecordRequest.setRecord(record);

// Put record into the DeliveryStream
firehoseClient.putRecord(putRecordRequest);
```

For more code context, see the sample code included in the AWS SDK. For information about request and response syntax, see the relevant topic in [Firehose API Operations](https://docs.aws.amazon.com/firehose/latest/APIReference/API_Operations.html).

## Batch write operations using PutRecordBatch
<a name="putrecordbatch"></a>

Putting data requires only the Firehose stream name and a list of records. Because Amazon Data Firehose batches multiple records before loading the file into Amazon S3, you may want to add a record separator. To put data records in batches into a Firehose stream, use the following code:

```
PutRecordBatchRequest putRecordBatchRequest = new PutRecordBatchRequest();
putRecordBatchRequest.setDeliveryStreamName(deliveryStreamName);
putRecordBatchRequest.setRecords(recordList);

// Put Record Batch records. Max No.Of Records we can put in a
// single put record batch request is 500
firehoseClient.putRecordBatch(putRecordBatchRequest);

recordList.clear();
```

For more code context, see the sample code included in the AWS SDK. For information about request and response syntax, see the relevant topic in [Firehose API Operations](https://docs.aws.amazon.com/firehose/latest/APIReference/API_Operations.html).