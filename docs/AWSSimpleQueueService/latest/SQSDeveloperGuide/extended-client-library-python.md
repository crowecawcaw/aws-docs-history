# Managing large Amazon SQS messages using Python

and Amazon S3

Use the Amazon SQS [Amazon SQS Extended
Client Library for Python](https://github.com/awslabs/amazon-sqs-python-extended-client-lib/ "https://github.com/awslabs/amazon-sqs-python-extended-client-lib/") with Amazon S3 to manage large Amazon SQS messages, especially
for payloads between 256 KB and 2 GB. The library stores the message payload in an Amazon S3
bucket and sends a message containing a reference to the stored object in the Amazon SQS
queue.

With the Amazon SQS Extended Client Library for Python, you can:

- Specify whether payloads are always stored in Amazon S3, or only stored in Amazon S3 when a
  payload size exceeds 256 KB
- Send a message that references a single message object stored in an Amazon S3 bucket
- Retrieve the corresponding payload object from an Amazon S3 bucket
- Delete the corresponding payload object from an Amazon S3 bucket

## Prerequisites

The following are the prerequisites for using the Amazon SQS Extended Client Library for
Python:

- An AWS account with the necessary credentials. To create an AWS account,
  navigate to the [AWS home page](https://aws.amazon.com/ "https://aws.amazon.com/") ,
  and then choose **Create an AWS Account** .
  Follow the instructions. For information about credentials, see [Credentials](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html "https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html").
- An AWS SDK: The example on this page uses AWS Python SDK Boto3. To install
  and set up the SDK, see the [_AWS SDK for Python_](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html "https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html")
  documentation in the _AWS SDK for Python Developer
  Guide_
- Python 3.x (or later) and `pip`.
- The Amazon SQS Extended Client Library for Python, available from [PyPI](https://pypi.org/project/amazon-sqs-extended-client/ "https://pypi.org/project/amazon-sqs-extended-client/")

###### Note

You can use the Amazon SQS Extended Client Library for Python to manage Amazon SQS messages
using Amazon S3 only with the AWS SDK for Python. You can't do this with the AWS CLI,
the Amazon SQS console, the Amazon SQS HTTP API, or any of the other AWS SDKs.

## Configuring message storage

The Amazon SQS Extended Client makes uses the following message attributes to configure
the Amazon S3 message storage options:

- `large_payload_support`: The Amazon S3 bucket name to store large
  messages.
- `always_through_s3`: If `True`, then all messages are
  stored in Amazon S3. If `False`, messages smaller than 256 KB will not be
  serialized to the s3 bucket. The default is `False`.
- `use_legacy_attribute`: If `True`, all published messages
  use the Legacy reserved message attribute (`SQSLargePayloadSize`)
  instead of the current reserved message attribute
  (`ExtendedPayloadSize`).

## Managing large Amazon SQS

messages with Extended Client Library for Python

The following example creates an Amazon S3 bucket with a random name. It then creates
an Amazon SQS queue named `MyQueue` and sends a message that is stored in an S3
bucket and is more than 256 KB to the queue. Finally, the code retrieves the message,
returns information about it, and then deletes the message, the queue, and the bucket.

```

import boto3
import sqs_extended_client

#Set the Amazon SQS extended client configuration with large payload.
sqs_extended_client = boto3.client("sqs", region_name="us-east-1")
sqs_extended_client.large_payload_support = "amzn-s3-demo-bucket"
sqs_extended_client.use_legacy_attribute = False


# Create an SQS message queue for this example. Then, extract the queue URL.
queue = sqs_extended_client.create_queue(
    QueueName = "MyQueue"
)
queue_url = sqs_extended_client.get_queue_url(
    QueueName = "MyQueue"
)['QueueUrl']


# Create the S3 bucket and allow message objects to be stored in the bucket.
sqs_extended_client.s3_client.create_bucket(Bucket=sqs_extended_client.large_payload_support)

# Sending a large message
small_message = "s"
large_message = small_message * 300000 # Shall cross the limit of 256 KB

send_message_response = sqs_extended_client.send_message(
    QueueUrl=queue_url,
    MessageBody=large_message
)
assert send_message_response['ResponseMetadata']['HTTPStatusCode'] == 200

# Receiving the large message
receive_message_response = sqs_extended_client.receive_message(
    QueueUrl=queue_url,
    MessageAttributeNames=['All']
)
assert receive_message_response['Messages'][0]['Body'] == large_message
receipt_handle = receive_message_response['Messages'][0]['ReceiptHandle']

# Deleting the large message
# Set to True for deleting the payload from S3
sqs_extended_client.delete_payload_from_s3 = True
delete_message_response = sqs_extended_client.delete_message(
    QueueUrl=queue_url,
    ReceiptHandle=receipt_handle
)

assert delete_message_response['ResponseMetadata']['HTTPStatusCode'] == 200

# Deleting the queue
delete_queue_response = sqs_extended_client.delete_queue(
    QueueUrl=queue_url
)

assert delete_queue_response['ResponseMetadata']['HTTPStatusCode'] == 200

```
