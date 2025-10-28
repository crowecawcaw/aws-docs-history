After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# Step 1: Prepare

Before you create an Amazon Kinesis Data Analytics application for this exercise, you must create two
Kinesis data streams. Configure one of the streams as the streaming source for your
application, and the other stream as the destination where Kinesis Data Analytics persists your
application output.

###### Topics

- [Step 1.1: Create the Input and
  Output Data Streams](#app-anomaly-create-two-streams "#app-anomaly-create-two-streams")
- [Step 1.2: Write
  Sample Records to the Input Stream](#app-anomaly-write-sample-records-inputstream "#app-anomaly-write-sample-records-inputstream")

## Step 1.1: Create the Input and

Output Data Streams

In this section, you create two Kinesis streams: `ExampleInputStream`
and `ExampleOutputStream`. You can create these streams using the
AWS Management Console or the AWS CLI.

- ###### To use the console
  1.  Sign in to the AWS Management Console and open the Kinesis console at
      [https://console.aws.amazon.com/kinesis](https://console.aws.amazon.com/kinesis "https://console.aws.amazon.com/kinesis").
  2.  Choose **Create data stream**. Create a
      stream with one shard named `ExampleInputStream`. For
      more information, see [Create a Stream](../../../streams/latest/dev/learning-kinesis-module-one-create-stream.md "../../../streams/latest/dev/learning-kinesis-module-one-create-stream.md") in the _Amazon Kinesis Data Streams
      Developer Guide_.
  3.  Repeat the previous step, creating a stream with one shard
      named `ExampleOutputStream`.

- ###### To use the AWS CLI
  1.  Use the following Kinesis `create-stream` AWS CLI
      command to create the first stream
      (`ExampleInputStream`).

  ```
  $ aws kinesis create-stream \
  --stream-name `ExampleInputStream` \
  --shard-count *1* \
  --region *us-east-1* \
  --profile *adminuser*
  ```

  2.  Run the same command, changing the stream name to
      `ExampleOutputStream`. This command creates the
      second stream that the application uses to write output.

## Step 1.2: Write

Sample Records to the Input Stream

In this step, you run Python code to continuously generate sample records and
write these records to the `ExampleInputStream` stream.

```
{"heartRate": 60, "rateType":"NORMAL"}
...
{"heartRate": 180, "rateType":"HIGH"}
```

1. Install Python and `pip`.

For information about installing Python, see the [Python](https://www.python.org/ "https://www.python.org/") website.

You can install dependencies using pip. For information about
installing pip, see [Installation](https://pip.pypa.io/en/stable/installing/ "https://pip.pypa.io/en/stable/installing/")
on the pip website. 2. Run the following Python code. The `put-record` command in
the code writes the JSON records to the stream.

```

from enum import Enum
import json
import random
import boto3

STREAM_NAME = "ExampleInputStream"


class RateType(Enum):
    normal = "NORMAL"
    high = "HIGH"


def get_heart_rate(rate_type):
    if rate_type == RateType.normal:
        rate = random.randint(60, 100)
    elif rate_type == RateType.high:
        rate = random.randint(150, 200)
    else:
        raise TypeError
    return {"heartRate": rate, "rateType": rate_type.value}


def generate(stream_name, kinesis_client, output=True):
    while True:
        rnd = random.random()
        rate_type = RateType.high if rnd < 0.01 else RateType.normal
        heart_rate = get_heart_rate(rate_type)
        if output:
            print(heart_rate)
        kinesis_client.put_record(
            StreamName=stream_name,
            Data=json.dumps(heart_rate),
            PartitionKey="partitionkey",
        )


if __name__ == "__main__":
    generate(STREAM_NAME, boto3.client("kinesis"))

```

###### Next Step

[Step 2: Create an Application](app-anom-score-create-app.md "app-anom-score-create-app.md")
