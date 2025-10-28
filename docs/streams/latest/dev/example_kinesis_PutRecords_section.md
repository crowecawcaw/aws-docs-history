# Use `PutRecords` with an AWS SDK or CLI

The following code examples show how to use `PutRecords`.

CLI

**AWS CLI**

**To write multiple records into a data stream**

The following `put-records` example writes a data record using the specified partition key and another data record using a different partition key in a single call.

```
`aws kinesis put-records \
 --stream-name `samplestream` \
 --records `Data=blob1,PartitionKey=partitionkey1` `Data=blob2,PartitionKey=partitionkey2``

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

For more information, see [Developing Producers Using the Amazon Kinesis Data Streams API with the AWS SDK for Java](developing-producers-with-sdk.md "developing-producers-with-sdk.md") in the _Amazon Kinesis Data Streams Developer Guide_.

- For API details, see
  [PutRecords](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/put-records.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/put-records.html")
  in _AWS CLI Command Reference_.

JavaScript

**SDK for JavaScript (v3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/kinesis#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/kinesis#code-examples").

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

- For API details, see
  [PutRecords](../../../AWSJavaScriptSDK/v3/latest/client/kinesis/command/PutRecordsCommand.md "../../../AWSJavaScriptSDK/v3/latest/client/kinesis/command/PutRecordsCommand.md")
  in _AWS SDK for JavaScript API Reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
