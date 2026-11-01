

# Use `PutRecords` with an AWS SDK or CLI
<a name="example_kinesis_PutRecords_section"></a>

The following code examples show how to use `PutRecords`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example: 
+  [Learn the basics](example_kinesis_Scenario_GettingStarted_section.md) 

------
#### [ CLI ]

**AWS CLI**  
**To write multiple records into a data stream**  
The following `put-records` example writes a data record using the specified partition key and another data record using a different partition key in a single call.  

```
aws kinesis put-records \
    --stream-name {{samplestream}} \
    --records {{Data=blob1,PartitionKey=partitionkey1}} {{Data=blob2,PartitionKey=partitionkey2}}
```
Output:  

```
{
    "FailedRecordCount": 0,
    "Records": [
        {
            "SequenceNumber": "49600883331171471519674795588238531498465399900093808706",
            "ShardId": "shardId-000000000004"
        },
        {
            "SequenceNumber": "49600902273357540915989931256902715169698037101720764562",
            "ShardId": "shardId-000000000009"
        }
    ],
    "EncryptionType": "KMS"
}
```
For more information, see [Developing Producers Using the Amazon Kinesis Data Streams API with the AWS SDK for Java](https://docs.aws.amazon.com/streams/latest/dev/developing-producers-with-sdk.html) in the *Amazon Kinesis Data Streams Developer Guide*.  
+  For API details, see [PutRecords](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/put-records.html) in *AWS CLI Command Reference*. 

------
#### [ JavaScript ]

**SDK for JavaScript (v3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/kinesis#code-examples). 

```
import { PutRecordsCommand, KinesisClient } from "@aws-sdk/client-kinesis";

/**
 * Put multiple records into a Kinesis stream.
 * @param {{ streamArn: string }} config
 */
export const main = async ({ streamArn }) => {
  const client = new KinesisClient({});
  try {
    await client.send(
      new PutRecordsCommand({
        StreamARN: streamArn,
        Records: [
          {
            Data: new Uint8Array(),
            /**
             * Determines which shard in the stream the data record is assigned to.
             * Partition keys are Unicode strings with a maximum length limit of 256
             * characters for each key. Amazon Kinesis Data Streams uses the partition
             * key as input to a hash function that maps the partition key and
             * associated data to a specific shard.
             */
            PartitionKey: "TEST_KEY",
          },
          {
            Data: new Uint8Array(),
            PartitionKey: "TEST_KEY",
          },
        ],
      }),
    );
  } catch (caught) {
    if (caught instanceof Error) {
      //
    } else {
      throw caught;
    }
  }
};

// Call function if run directly.
import { fileURLToPath } from "node:url";
import { parseArgs } from "node:util";

if (process.argv[1] === fileURLToPath(import.meta.url)) {
  const options = {
    streamArn: {
      type: "string",
      description: "The ARN of the stream.",
    },
  };

  const { values } = parseArgs({ options });
  main(values);
}
```
+  For API details, see [PutRecords](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/kinesis/command/PutRecordsCommand) in *AWS SDK for JavaScript API Reference*. 

------
#### [ Python ]

**SDK for Python (Boto3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/kinesis#code-examples). 

```
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
```
+  For API details, see [PutRecords](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/PutRecords) in *AWS SDK for Python (Boto3) API Reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.