

# Learn Data Streams basics using an AWS SDK
<a name="example_kinesis_Scenario_GettingStarted_section"></a>

The following code examples show how to:
+ Create a stream and wait for it to become ACTIVE.
+ List streams and verify creation.
+ Describe stream summary to get metadata.
+ List shards in the stream.
+ Batch put records using PutRecords.
+ Get a shard iterator and read records.
+ Add tags to the stream.
+ List tags for the stream.
+ Remove tags from the stream.
+ Register an enhanced fan-out consumer.
+ Deregister the consumer.
+ Clean up all resources.

------
#### [ Python ]

**SDK for Python (Boto3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/kinesis#code-examples). 
Run the Kinesis Data Streams basics scenario.  

```
def run_scenario(kinesis_wrapper):
    """
    Runs the Kinesis Data Streams basics scenario.

    :param kinesis_wrapper: A KinesisWrapper instance.
    """
    stream_name = f"sdk-example-stream-{int(time.time())}"
    consumer_name = "sdk-example-consumer"
    consumer_arn = None
    stream_arn = None

    print(DASHES)
    print("Welcome to the Amazon Kinesis Data Streams Scenario.")
    print(
        "This scenario demonstrates advanced stream management, batch data\n"
        "ingestion, shard inspection, tagging, and enhanced fan-out consumers."
    )
    print(DASHES)

    try:
        # --- Setup: Create stream ---
        print("\nSetting up resources...")
        print(f"Creating Kinesis stream: {stream_name}")
        kinesis_wrapper.kinesis_client.create_stream(
            StreamName=stream_name, ShardCount=1
        )
        print("Waiting for stream to become ACTIVE...")
        summary = kinesis_wrapper.wait_for_stream_active(stream_name)
        stream_arn = summary.get("StreamARN", "")
        print("Stream is now ACTIVE.")
        print(DASHES)

        # --- Step 1: List Streams ---
        print("\nStep 1: Listing streams in your account...")
        streams = kinesis_wrapper.list_streams()
        for s in streams:
            mode = s.get("StreamModeDetails", dict()).get("StreamMode", "N/A")
            print(
                f"  Stream: {s.get('StreamName')} "
                f"(Status: {s.get('StreamStatus')}, Mode: {mode})"
            )
        found = any(s.get("StreamName") == stream_name for s in streams)
        print(
            f"Found {len(streams)} stream(s). "
            f"Our scenario stream is {'present' if found else 'NOT found'}."
        )
        print(DASHES)

        # --- Step 2: Describe Stream Summary ---
        print("\nStep 2: Describing stream summary...")
        summary = kinesis_wrapper.describe_stream_summary(stream_name)
        print(f"  Stream Name: {summary.get('StreamName')}")
        print(f"  Stream ARN: {summary.get('StreamARN')}")
        print(f"  Status: {summary.get('StreamStatus')}")
        print(f"  Retention Period: {summary.get('RetentionPeriodHours')} hours")
        print(f"  Open Shard Count: {summary.get('OpenShardCount')}")
        print(f"  Encryption: {summary.get('EncryptionType', 'NONE')}")
        mode = summary.get("StreamModeDetails", dict()).get("StreamMode", "N/A")
        print(f"  Stream Mode: {mode}")
        stream_arn = summary.get("StreamARN", stream_arn)
        print(DASHES)

        # --- Step 3: List Shards ---
        print("\nStep 3: Listing shards in the stream...")
        shards = kinesis_wrapper.list_shards(stream_name)
        first_shard_id = None
        for shard in shards:
            shard_id = shard.get("ShardId", "")
            if first_shard_id is None:
                first_shard_id = shard_id
            hash_range = shard.get("HashKeyRange", dict())
            seq_range = shard.get("SequenceNumberRange", dict())
            print(f"  Shard ID: {shard_id}")
            print(
                f"    Hash Key Range: {hash_range.get('StartingHashKey')} - "
                f"{hash_range.get('EndingHashKey')}"
            )
            print(
                f"    Starting Sequence Number: "
                f"{seq_range.get('StartingSequenceNumber')}"
            )
        print(f"Found {len(shards)} shard(s).")
        print(DASHES)

        # --- Step 4: PutRecords ---
        print("\nStep 4: Putting 5 records into the stream using PutRecords...")
        sensor_data = [
            {
                "sensor_id": "sensor-001",
                "temperature": 72.5,
                "timestamp": "2024-01-15T10:00:00Z",
            },
            {
                "sensor_id": "sensor-002",
                "temperature": 68.3,
                "timestamp": "2024-01-15T10:00:01Z",
            },
            {
                "sensor_id": "sensor-001",
                "temperature": 73.1,
                "timestamp": "2024-01-15T10:00:02Z",
            },
            {
                "sensor_id": "sensor-003",
                "temperature": 75.8,
                "timestamp": "2024-01-15T10:00:03Z",
            },
            {
                "sensor_id": "sensor-002",
                "temperature": 67.9,
                "timestamp": "2024-01-15T10:00:04Z",
            },
        ]
        records = [
            {
                "Data": json.dumps(data).encode("utf-8"),
                "PartitionKey": data["sensor_id"],
            }
            for data in sensor_data
        ]
        put_response = kinesis_wrapper.put_records(stream_name, records)
        for idx, rec in enumerate(put_response.get("Records", list()), 1):
            if rec.get("ErrorCode"):
                print(
                    f"  Record {idx}: FAILED - {rec.get('ErrorCode')}: "
                    f"{rec.get('ErrorMessage')}"
                )
            else:
                print(
                    f"  Record {idx}: ShardId={rec.get('ShardId')}, "
                    f"SequenceNumber={rec.get('SequenceNumber')}"
                )
        failed = put_response.get("FailedRecordCount", 0)
        print(f"Successfully put 5 record(s) with {failed} failures.")
        print(DASHES)

        # --- Step 5: GetShardIterator and read records ---
        print("\nStep 5: Getting shard iterator (TRIM_HORIZON) and reading records...")
        shard_iterator = kinesis_wrapper.get_shard_iterator(
            stream_name, first_shard_id, "TRIM_HORIZON"
        )
        print(f"  Obtained shard iterator for {first_shard_id}.")
        print("  Reading records from the stream...")
        get_response = kinesis_wrapper.kinesis_client.get_records(
            ShardIterator=shard_iterator, Limit=10
        )
        data_records = get_response.get("Records", list())
        for idx, rec in enumerate(data_records, 1):
            payload = rec.get("Data", b"").decode("utf-8")
            print(f"  Record {idx}: {payload}")
        print(f"Read {len(data_records)} record(s) from the stream.")
        print(DASHES)

        # --- Step 6: Add Tags ---
        print("\nStep 6: Adding tags to the stream...")
        tags = {
            "Project": "kinesis-demo",
            "Environment": "development",
            "CostCenter": "12345",
        }
        kinesis_wrapper.add_tags_to_stream(stream_name, tags)
        for key, value in tags.items():
            print(f"  Added tag: {key} = {value}")
        print("Tags added successfully.")
        print(DASHES)

        # --- Step 7: List Tags ---
        print("\nStep 7: Listing tags for the stream...")
        tag_list, has_more_tags = kinesis_wrapper.list_tags_for_stream(stream_name)
        for tag in tag_list:
            print(f"  Tag: {tag.get('Key')} = {tag.get('Value')}")
        print(f"Found {len(tag_list)} tag(s). HasMoreTags: {has_more_tags}")
        print(DASHES)

        # --- Step 8: Remove Tags ---
        print("\nStep 8: Removing the CostCenter tag from the stream...")
        kinesis_wrapper.remove_tags_from_stream(stream_name, ["CostCenter"])
        print("Tag removed successfully.")
        print("Verifying remaining tags...")
        remaining_tags, _ = kinesis_wrapper.list_tags_for_stream(stream_name)
        for tag in remaining_tags:
            print(f"  Tag: {tag.get('Key')} = {tag.get('Value')}")
        print(f"Confirmed: {len(remaining_tags)} tag(s) remaining after removal.")
        print(DASHES)

        # --- Step 9: Register Consumer ---
        print("\nStep 9: Registering an enhanced fan-out consumer...")
        consumer = kinesis_wrapper.register_stream_consumer(stream_arn, consumer_name)
        consumer_arn = consumer.get("ConsumerARN", "")
        print(f"  Consumer Name: {consumer.get('ConsumerName')}")
        print(f"  Consumer ARN: {consumer_arn}")
        print(f"  Status: {consumer.get('ConsumerStatus')}")
        print("Waiting for consumer to become ACTIVE...")
        desc = kinesis_wrapper.wait_for_consumer_active(stream_arn, consumer_name)
        print(f"  Consumer status: {desc.get('ConsumerStatus')}")
        print("Enhanced fan-out consumer registered successfully.")
        print(DASHES)

        # --- Step 10: Deregister Consumer ---
        print("\nStep 10: Deregistering the enhanced fan-out consumer...")
        kinesis_wrapper.deregister_stream_consumer(consumer_arn)
        print(f"Consumer '{consumer_name}' deregistered successfully.")
        print("Enhanced fan-out charges will stop for this consumer.")
        consumer_arn = None
        print(DASHES)

    finally:
        # --- Cleanup ---
        print(DASHES)
        print("Cleaning up resources...")

        # Deregister consumer if still registered
        if consumer_arn:
            print("Ensuring consumer is deregistered...")
            try:
                kinesis_wrapper.deregister_stream_consumer(consumer_arn)
                print("  Consumer deregistered during cleanup.")
            except ClientError as err:
                if err.response["Error"]["Code"] == "ResourceNotFoundException":
                    print("  Consumer already deregistered.")
                else:
                    logger.error("Error deregistering consumer: %s", err)

        # Delete the stream
        print(f"Deleting stream: {stream_name}")
        try:
            kinesis_wrapper.kinesis_client.delete_stream(
                StreamName=stream_name, EnforceConsumerDeletion=True
            )
            print("Waiting for stream deletion to complete...")
            # Use the built-in waiter so the expected "not found" result
            # isn't logged as an error while polling.
            waiter = kinesis_wrapper.kinesis_client.get_waiter("stream_not_exists")
            waiter.wait(
                StreamName=stream_name,
                WaiterConfig={"Delay": 2, "MaxAttempts": 60},
            )
            print("Stream deleted successfully.")
        except WaiterError as err:
            logger.error("Timed out waiting for stream deletion: %s", err)
        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                print("Stream already deleted.")
            else:
                logger.error("Error deleting stream: %s", err)

        print(DASHES)
        print("Amazon Kinesis Data Streams scenario complete!")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    wrapper = KinesisWrapper.from_client()
    run_scenario(wrapper)
```
Define a wrapper class that is called by the scenario to manage Kinesis actions.  

```
class KinesisWrapper:
    """Encapsulates Amazon Kinesis Data Streams operations."""

    def __init__(self, kinesis_client):
        """
        Initializes the KinesisWrapper with a Kinesis client.

        :param kinesis_client: A Boto3 Kinesis client.
        """
        self.kinesis_client = kinesis_client

    @classmethod
    def from_client(cls):
        """
        Creates a KinesisWrapper instance with a default Kinesis client.

        :return: A KinesisWrapper instance.
        """
        kinesis_client = boto3.client("kinesis")
        return cls(kinesis_client)


    def list_streams(self, limit=100):
        """
        Lists Kinesis data streams in the account.

        :param limit: The maximum number of streams to list.
        :return: A list of stream summary dictionaries.
        """
        try:
            streams = list()
            response = self.kinesis_client.list_streams(Limit=limit)
            streams.extend(response.get("StreamSummaries", list()))
            while response.get("HasMoreStreams", False):
                summaries = response.get("StreamSummaries", list())
                if not summaries:
                    break
                next_name = summaries[-1]["StreamName"]
                response = self.kinesis_client.list_streams(
                    Limit=limit, ExclusiveStartStreamName=next_name
                )
                streams.extend(response.get("StreamSummaries", list()))
            logger.info("Listed %s stream(s).", len(streams))
            return streams
        except ClientError as err:
            if err.response["Error"]["Code"] == "LimitExceededException":
                logger.error(
                    "Request rate too high for ListStreams. Retry after a brief delay."
                )
            raise


    def describe_stream_summary(self, stream_name):
        """
        Provides a summarized description of a Kinesis data stream.

        :param stream_name: The name of the stream to describe.
        :return: A dictionary containing the stream description summary.
        """
        try:
            response = self.kinesis_client.describe_stream_summary(
                StreamName=stream_name
            )
            summary = response.get("StreamDescriptionSummary", dict())
            logger.info(
                "Described stream summary for '%s'. Status: %s.",
                stream_name,
                summary.get("StreamStatus", "UNKNOWN"),
            )
            return summary
        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                logger.error(
                    "Stream '%s' not found. Verify the stream name.", stream_name
                )
            raise


    def list_shards(self, stream_name, max_wait=30, poll_interval=2):
        """
        Lists the shards in a Kinesis data stream.

        A freshly created stream can report ACTIVE via DescribeStreamSummary
        before its shards are listable. Because ListShards is eventually
        consistent, it may briefly raise ResourceInUseException ("in state
        CREATING") or ResourceNotFoundException. This method retries on those
        errors until the shards become available or ``max_wait`` elapses.

        :param stream_name: The name of the stream whose shards to list.
        :param max_wait: Maximum seconds to retry while the stream is still
                         settling after creation.
        :param poll_interval: Seconds between retries.
        :return: A list of shard dictionaries.
        """
        elapsed = 0
        while True:
            try:
                shards = list()
                response = self.kinesis_client.list_shards(StreamName=stream_name)
                shards.extend(response.get("Shards", list()))
                while "NextToken" in response:
                    response = self.kinesis_client.list_shards(
                        NextToken=response["NextToken"]
                    )
                    shards.extend(response.get("Shards", list()))
                logger.info(
                    "Listed %s shard(s) for stream '%s'.", len(shards), stream_name
                )
                return shards
            except ClientError as err:
                code = err.response["Error"]["Code"]
                retryable = ("ResourceInUseException", "ResourceNotFoundException")
                if code in retryable and elapsed < max_wait:
                    logger.info(
                        "Stream '%s' not ready for ListShards yet. Retrying...",
                        stream_name,
                    )
                    time.sleep(poll_interval)
                    elapsed += poll_interval
                    continue
                if code == "ResourceNotFoundException":
                    logger.error(
                        "Stream '%s' not found. Verify the stream is ACTIVE.",
                        stream_name,
                    )
                raise


    def put_records(self, stream_name, records):
        """
        Writes multiple data records into a Kinesis data stream in a single call.

        :param stream_name: The name of the stream to write records to.
        :param records: A list of dicts, each with 'Data' (bytes) and 'PartitionKey' (str).
        :return: The response from the PutRecords call.
        """
        try:
            response = self.kinesis_client.put_records(
                StreamName=stream_name, Records=records
            )
            failed_count = response.get("FailedRecordCount", 0)
            logger.info(
                "Put %s record(s) to stream '%s' with %s failure(s).",
                len(records),
                stream_name,
                failed_count,
            )
            return response
        except ClientError as err:
            if err.response["Error"]["Code"] == "InvalidArgumentException":
                logger.error(
                    "Invalid argument for PutRecords. Check record sizes and parameters."
                )
            raise


    def get_shard_iterator(self, stream_name, shard_id, iterator_type="TRIM_HORIZON"):
        """
        Gets a shard iterator for reading data records from a shard.

        :param stream_name: The name of the stream.
        :param shard_id: The ID of the shard.
        :param iterator_type: The shard iterator type (e.g., TRIM_HORIZON, LATEST).
        :return: A shard iterator string.
        """
        try:
            response = self.kinesis_client.get_shard_iterator(
                StreamName=stream_name,
                ShardId=shard_id,
                ShardIteratorType=iterator_type,
            )
            shard_iterator = response.get("ShardIterator", None)
            logger.info(
                "Got shard iterator for shard '%s' of type '%s'.",
                shard_id,
                iterator_type,
            )
            return shard_iterator
        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                logger.error(
                    "Stream '%s' or shard '%s' not found. Verify shard ID is correct.",
                    stream_name,
                    shard_id,
                )
            raise


    def add_tags_to_stream(self, stream_name, tags):
        """
        Adds or updates tags for a Kinesis data stream.

        :param stream_name: The name of the stream to tag.
        :param tags: A dictionary of tag key-value pairs.
        """
        try:
            self.kinesis_client.add_tags_to_stream(StreamName=stream_name, Tags=tags)
            logger.info("Added %s tag(s) to stream '%s'.", len(tags), stream_name)
        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                logger.error("Stream '%s' not found. Cannot add tags.", stream_name)
            raise


    def list_tags_for_stream(self, stream_name):
        """
        Lists the tags for a Kinesis data stream.

        :param stream_name: The name of the stream whose tags to list.
        :return: A tuple of (list of tag dictionaries with 'Key' and 'Value',
                 bool indicating whether more tags are available).
        """
        try:
            response = self.kinesis_client.list_tags_for_stream(StreamName=stream_name)
            tags = response.get("Tags", list())
            has_more = response.get("HasMoreTags", False)
            logger.info(
                "Listed %s tag(s) for stream '%s'. HasMoreTags: %s.",
                len(tags),
                stream_name,
                has_more,
            )
            return tags, has_more
        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                logger.error("Stream '%s' not found when listing tags.", stream_name)
            raise


    def remove_tags_from_stream(self, stream_name, tag_keys):
        """
        Removes tags from a Kinesis data stream.

        :param stream_name: The name of the stream to remove tags from.
        :param tag_keys: A list of tag keys to remove.
        """
        try:
            self.kinesis_client.remove_tags_from_stream(
                StreamName=stream_name, TagKeys=tag_keys
            )
            logger.info("Removed tag(s) %s from stream '%s'.", tag_keys, stream_name)
        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                logger.error("Stream '%s' not found for tag removal.", stream_name)
            raise


    def register_stream_consumer(self, stream_arn, consumer_name):
        """
        Registers an enhanced fan-out consumer with a Kinesis data stream.

        :param stream_arn: The ARN of the stream.
        :param consumer_name: The name for the consumer.
        :return: A dictionary containing consumer details.
        """
        try:
            response = self.kinesis_client.register_stream_consumer(
                StreamARN=stream_arn, ConsumerName=consumer_name
            )
            consumer = response.get("Consumer", dict())
            logger.info(
                "Registered consumer '%s' with status '%s'.",
                consumer_name,
                consumer.get("ConsumerStatus", "UNKNOWN"),
            )
            return consumer
        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceInUseException":
                logger.error(
                    "Consumer '%s' already exists or stream is not available.",
                    consumer_name,
                )
            raise


    def deregister_stream_consumer(self, consumer_arn):
        """
        Deregisters an enhanced fan-out consumer.

        :param consumer_arn: The ARN of the consumer to deregister.
        """
        try:
            self.kinesis_client.deregister_stream_consumer(ConsumerARN=consumer_arn)
            logger.info("Deregistered consumer with ARN '%s'.", consumer_arn)
        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                logger.error(
                    "Consumer not found. It may have already been deregistered."
                )
            raise
```
+ For API details, see the following topics in *AWS SDK for Python (Boto3) API Reference*.
  + [AddTagsToStream](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/AddTagsToStream)
  + [CreateStream](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/CreateStream)
  + [DeleteStream](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/DeleteStream)
  + [DeregisterStreamConsumer](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/DeregisterStreamConsumer)
  + [DescribeStreamSummary](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/DescribeStreamSummary)
  + [GetRecords](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/GetRecords)
  + [GetShardIterator](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/GetShardIterator)
  + [ListShards](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/ListShards)
  + [ListStreams](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/ListStreams)
  + [ListTagsForStream](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/ListTagsForStream)
  + [PutRecord](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/PutRecord)
  + [PutRecords](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/PutRecords)
  + [RegisterStreamConsumer](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/RegisterStreamConsumer)
  + [RemoveTagsFromStream](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/RemoveTagsFromStream)

------
#### [ SAP ABAP ]

**SDK for SAP ABAP**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/kns#code-examples). 

```
    DATA lo_stream_describe_result TYPE REF TO /aws1/cl_knsdescrstreamoutput.
    DATA lo_stream_description TYPE REF TO /aws1/cl_knsstreamdescription.
    DATA lo_sharditerator TYPE REF TO /aws1/cl_knsgetsharditerator01.
    DATA lo_record_result TYPE REF TO /aws1/cl_knsputrecordoutput.

    "Create stream."
    TRY.
        lo_kns->createstream(
            iv_streamname = iv_stream_name
            iv_shardcount = iv_shard_count ).
        MESSAGE 'Stream created.' TYPE 'I'.
      CATCH /aws1/cx_knsinvalidargumentex.
        MESSAGE 'The specified argument was not valid.' TYPE 'E'.
      CATCH /aws1/cx_knslimitexceededex.
        MESSAGE 'The request processing has failed because of a limit exceeded exception.' TYPE 'E'.
      CATCH /aws1/cx_knsresourceinuseex.
        MESSAGE 'The request processing has failed because the resource is in use.' TYPE 'E'.
    ENDTRY.

    "Wait for stream to becomes active."
    lo_stream_describe_result = lo_kns->describestream( iv_streamname = iv_stream_name ).
    lo_stream_description = lo_stream_describe_result->get_streamdescription( ).
    WHILE lo_stream_description->get_streamstatus( ) <> 'ACTIVE'.
      IF sy-index = 30.
        EXIT.               "maximum 5 minutes"
      ENDIF.
      WAIT UP TO 10 SECONDS.
      lo_stream_describe_result = lo_kns->describestream( iv_streamname = iv_stream_name ).
      lo_stream_description = lo_stream_describe_result->get_streamdescription( ).
    ENDWHILE.

    "Create record."
    TRY.
        lo_record_result = lo_kns->putrecord(
            iv_streamname = iv_stream_name
            iv_data       = iv_data
            iv_partitionkey = iv_partition_key ).
        MESSAGE 'Record created.' TYPE 'I'.
      CATCH /aws1/cx_knsinvalidargumentex.
        MESSAGE 'The specified argument was not valid.' TYPE 'E'.
      CATCH /aws1/cx_knskmsaccessdeniedex.
        MESSAGE 'You do not have permission to perform this AWS KMS action.' TYPE 'E'.
      CATCH /aws1/cx_knskmsdisabledex.
        MESSAGE 'KMS key used is disabled.' TYPE 'E'.
      CATCH /aws1/cx_knskmsinvalidstateex.
        MESSAGE 'KMS key used is in an invalid state. ' TYPE 'E'.
      CATCH /aws1/cx_knskmsnotfoundex.
        MESSAGE 'KMS key used is not found.' TYPE 'E'.
      CATCH /aws1/cx_knskmsoptinrequired.
        MESSAGE 'KMS key option is required.' TYPE 'E'.
      CATCH /aws1/cx_knskmsthrottlingex.
        MESSAGE 'The rate of requests to AWS KMS is exceeding the request quotas.' TYPE 'E'.
      CATCH /aws1/cx_knsprovthruputexcdex.
        MESSAGE 'The request rate for the stream is too high, or the requested data is too large for the available throughput.' TYPE 'E'.
      CATCH /aws1/cx_knsresourcenotfoundex.
        MESSAGE 'Resource being accessed is not found.' TYPE 'E'.
    ENDTRY.

    "Create a shard iterator in order to read the record."
    TRY.
        lo_sharditerator = lo_kns->getsharditerator(
          iv_shardid = lo_record_result->get_shardid( )
          iv_sharditeratortype = iv_sharditeratortype
          iv_streamname = iv_stream_name ).
        MESSAGE 'Shard iterator created.' TYPE 'I'.
      CATCH /aws1/cx_knsinvalidargumentex.
        MESSAGE 'The specified argument was not valid.' TYPE 'E'.
      CATCH /aws1/cx_knsprovthruputexcdex.
        MESSAGE 'The request rate for the stream is too high, or the requested data is too large for the available throughput.' TYPE 'E'.
      CATCH /aws1/cx_sgmresourcenotfound.
        MESSAGE 'Resource being accessed is not found.' TYPE 'E'.
    ENDTRY.

    "Read the record."
    TRY.
        oo_result = lo_kns->getrecords(                    " oo_result is returned for testing purposes. "
            iv_sharditerator   = lo_sharditerator->get_sharditerator( ) ).
        MESSAGE 'Shard iterator created.' TYPE 'I'.
      CATCH /aws1/cx_knsexpirediteratorex.
        MESSAGE 'Iterator expired.' TYPE 'E'.
      CATCH /aws1/cx_knsinvalidargumentex.
        MESSAGE 'The specified argument was not valid.' TYPE 'E'.
      CATCH /aws1/cx_knskmsaccessdeniedex.
        MESSAGE 'You do not have permission to perform this AWS KMS action.' TYPE 'E'.
      CATCH /aws1/cx_knskmsdisabledex.
        MESSAGE 'KMS key used is disabled.' TYPE 'E'.
      CATCH /aws1/cx_knskmsinvalidstateex.
        MESSAGE 'KMS key used is in an invalid state. ' TYPE 'E'.
      CATCH /aws1/cx_knskmsnotfoundex.
        MESSAGE 'KMS key used is not found.' TYPE 'E'.
      CATCH /aws1/cx_knskmsoptinrequired.
        MESSAGE 'KMS key option is required.' TYPE 'E'.
      CATCH /aws1/cx_knskmsthrottlingex.
        MESSAGE 'The rate of requests to AWS KMS is exceeding the request quotas.' TYPE 'E'.
      CATCH /aws1/cx_knsprovthruputexcdex.
        MESSAGE 'The request rate for the stream is too high, or the requested data is too large for the available throughput.' TYPE 'E'.
      CATCH /aws1/cx_knsresourcenotfoundex.
        MESSAGE 'Resource being accessed is not found.' TYPE 'E'.
    ENDTRY.

    "Delete stream."
    TRY.
        lo_kns->deletestream(
            iv_streamname = iv_stream_name ).
        MESSAGE 'Stream deleted.' TYPE 'I'.
      CATCH /aws1/cx_knslimitexceededex.
        MESSAGE 'The request processing has failed because of a limit exceeded exception.' TYPE 'E'.
      CATCH /aws1/cx_knsresourceinuseex.
        MESSAGE 'The request processing has failed because the resource is in use.' TYPE 'E'.
    ENDTRY.
```
+ For API details, see the following topics in *AWS SDK for SAP ABAP API reference*.
  + [AddTagsToStream](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html)
  + [CreateStream](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html)
  + [DeleteStream](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html)
  + [DeregisterStreamConsumer](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html)
  + [DescribeStreamSummary](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html)
  + [GetRecords](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html)
  + [GetShardIterator](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html)
  + [ListShards](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html)
  + [ListStreams](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html)
  + [ListTagsForStream](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html)
  + [PutRecord](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html)
  + [PutRecords](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html)
  + [RegisterStreamConsumer](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html)
  + [RemoveTagsFromStream](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html)

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.