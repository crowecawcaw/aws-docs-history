# Use `PutRecordBatch` with an AWS SDK or CLI

The following code examples show how to use `PutRecordBatch`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in
context in the following code example:

- [Put records to Firehose](example_firehose_Scenario_PutRecords_section.md "example_firehose_Scenario_PutRecords_section.md")

CLI

**AWS CLI**

**To write multiple records to a stream**

The following `put-record-batch` example writes three records to a stream. The data is encoded in Base64 format.

```
`aws firehose put-record-batch \
 --delivery-stream-name `my-stream` \
 --records `file://records.json``

```

Contents of `myfile.json`:

```
[
    {"Data": "Rmlyc3QgdGhpbmc="},
    {"Data": "U2Vjb25kIHRoaW5n"},
    {"Data": "VGhpcmQgdGhpbmc="}
]
```

Output:

```
{
    "FailedPutCount": 0,
    "Encrypted": false,
    "RequestResponses": [
        {
            "RecordId": "9D2OJ6t2EqCTZTXwGzeSv/EVHxRoRCw89xd+o3+sXg8DhYOaWKPSmZy/CGlRVEys1u1xbeKh6VofEYKkoeiDrcjrxhQp9iF7sUW7pujiMEQ5LzlrzCkGosxQn+3boDnURDEaD42V7GiixpOyLJkYZcae1i7HzlCEoy9LJhMr8EjDSi4Om/9Vc2uhwwuAtGE0XKpxJ2WD7ZRWtAnYlKAnvgSPRgg7zOWL"
        },
        {
            "RecordId": "jFirejqxCLlK5xjH/UNmlMVcjktEN76I7916X9PaZ+PVaOSXDfU1WGOqEZhxq2js7xcZ552eoeDxsuTU1MSq9nZTbVfb6cQTIXnm/GsuF37Uhg67GKmR5z90l6XKJ+/+pDloFv7Hh9a3oUS6wYm3DcNRLTHHAimANp1PhkQvWpvLRfzbuCUkBphR2QVzhP9OiHLbzGwy8/DfH8sqWEUYASNJKS8GXP5s"
        },
        {
            "RecordId": "oy0amQ40o5Y2YV4vxzufdcMOOw6n3EPr3tpPJGoYVNKH4APPVqNcbUgefo1stEFRg4hTLrf2k6eliHu/9+YJ5R3iiedHkdsfkIqX0XTySSutvgFYTjNY1TSrK0pM2sWxpjqqnk3+2UX1MV5z88xGro3cQm/DTBt3qBlmTj7Xq8SKVbO1S7YvMTpWkMKA86f8JfmT8BMKoMb4XZS/sOkQLe+qh0sYKXWl"
        }
    ]
}
```

For more information, see [Sending Data to an Amazon Kinesis Data Firehose Delivery Stream](basic-write.md "basic-write.md") in the _Amazon Kinesis Data Firehose Developer Guide_.

- For API details, see
  [PutRecordBatch](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/firehose/put-record-batch.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/firehose/put-record-batch.html")
  in _AWS CLI Command Reference_.

Java

**SDK for Java 2.x**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/firehose#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/firehose#code-examples").

```
    /**
     * Puts a batch of records to an Amazon Kinesis Data Firehose delivery stream.
     *
     * @param records           a list of maps representing the records to be sent
     * @param batchSize         the maximum number of records to include in each batch
     * @param deliveryStreamName the name of the Kinesis Data Firehose delivery stream
     * @throws IllegalArgumentException if the input parameters are invalid (null or empty)
     * @throws RuntimeException         if there is an error putting the record batch
     */
    public static void putRecordBatch(List<Map<String, Object>> records, int batchSize, String deliveryStreamName) {
        if (records == null || records.isEmpty() || deliveryStreamName == null || deliveryStreamName.isEmpty()) {
            throw new IllegalArgumentException("Invalid input: records or delivery stream name cannot be null/empty");
        }
        ObjectMapper objectMapper = new ObjectMapper();

        try {
            for (int i = 0; i < records.size(); i += batchSize) {
                List<Map<String, Object>> batch = records.subList(i, Math.min(i + batchSize, records.size()));

                List<Record> batchRecords = batch.stream().map(record -> {
                    try {
                        String jsonRecord = objectMapper.writeValueAsString(record);
                        return Record.builder()
                            .data(SdkBytes.fromByteArray(jsonRecord.getBytes(StandardCharsets.UTF_8)))
                            .build();
                    } catch (Exception e) {
                        throw new RuntimeException("Error creating Firehose record", e);
                    }
                }).collect(Collectors.toList());

                PutRecordBatchRequest request = PutRecordBatchRequest.builder()
                    .deliveryStreamName(deliveryStreamName)
                    .records(batchRecords)
                    .build();

                PutRecordBatchResponse response = getFirehoseClient().putRecordBatch(request);

                if (response.failedPutCount() > 0) {
                    response.requestResponses().stream()
                        .filter(r -> r.errorCode() != null)
                        .forEach(r -> System.err.println("Failed record: " + r.errorMessage()));
                }
                System.out.println("Batch sent with size: " + batchRecords.size());
            }
        } catch (Exception e) {
            throw new RuntimeException("Failed to put record batch: " + e.getMessage(), e);
        }
    }


```

- For API details, see
  [PutRecordBatch](../../../goto/SdkForJavaV2/firehose-2015-08-04/PutRecordBatch.md "../../../goto/SdkForJavaV2/firehose-2015-08-04/PutRecordBatch.md")
  in _AWS SDK for Java 2.x API Reference_.

Python

**SDK for Python (Boto3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/firehose#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/firehose#code-examples").

```
class FirehoseClient:
    """
    AWS Firehose client to send records and monitor metrics.

    Attributes:
        config (object): Configuration object with delivery stream name and region.
        delivery_stream_name (str): Name of the Firehose delivery stream.
        region (str): AWS region for Firehose and CloudWatch clients.
        firehose (boto3.client): Boto3 Firehose client.
        cloudwatch (boto3.client): Boto3 CloudWatch client.
    """

    def __init__(self, config):
        """
        Initialize the FirehoseClient.

        Args:
            config (object): Configuration object with delivery stream name and region.
        """
        self.config = config
        self.delivery_stream_name = config.delivery_stream_name
        self.region = config.region
        self.firehose = boto3.client("firehose", region_name=self.region)
        self.cloudwatch = boto3.client("cloudwatch", region_name=self.region)


    @backoff.on_exception(
        backoff.expo, Exception, max_tries=5, jitter=backoff.full_jitter
    )
    def put_record_batch(self, data: list, batch_size: int = 500):
        """
        Put records in batches to Firehose with backoff and retry.

        Args:
            data (list): List of data records to be sent to Firehose.
            batch_size (int): Number of records to send in each batch. Default is 500.

        This method attempts to send records in batches to the Firehose delivery stream.
        It retries with exponential backoff in case of exceptions.
        """
        for i in range(0, len(data), batch_size):
            batch = data[i : i + batch_size]
            record_dicts = [{"Data": json.dumps(record)} for record in batch]
            try:
                response = self.firehose.put_record_batch(
                    DeliveryStreamName=self.delivery_stream_name, Records=record_dicts
                )
                self._log_batch_response(response, len(batch))
            except Exception as e:
                logger.info(f"Failed to send batch of {len(batch)} records. Error: {e}")



```

- For API details, see
  [PutRecordBatch](../../../goto/boto3/firehose-2015-08-04/PutRecordBatch.md "../../../goto/boto3/firehose-2015-08-04/PutRecordBatch.md")
  in _AWS SDK for Python (Boto3) API Reference_.

Rust

**SDK for Rust**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/firehose#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/firehose#code-examples").

```
async fn put_record_batch(
    client: &Client,
    stream: &str,
    data: Vec<Record>,
) -> Result<PutRecordBatchOutput, SdkError<PutRecordBatchError>> {
    client
        .put_record_batch()
        .delivery_stream_name(stream)
        .set_records(Some(data))
        .send()
        .await
}


```

- For API details, see
  [PutRecordBatch](https://docs.rs/aws-sdk-firehose/latest/aws_sdk_firehose/client/struct.Client.html#method.put_record_batch "https://docs.rs/aws-sdk-firehose/latest/aws_sdk_firehose/client/struct.Client.html#method.put_record_batch")
  in _AWS SDK for Rust API reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using Firehose with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
