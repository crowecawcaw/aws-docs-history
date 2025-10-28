# Amazon SNS Extended Client Library for

Python

## Prerequisites

The following are the prerequisites for using the [Amazon SNS
Extended Client Library for Python](https://github.com/awslabs/amazon-sns-python-extended-client-lib "https://github.com/awslabs/amazon-sns-python-extended-client-lib"):

- An AWS SDK. The example on this page uses AWS Python SDK Boto3. To
  install and set up the SDK, see the [_AWS SDK for Python_](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html "https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html")
  documentation.
- An AWS account with the proper credentials. To create an AWS account,
  navigate to the [AWS home page](https://aws.amazon.com/ "https://aws.amazon.com/"), and
  then choose **Create an AWS Account**. Follow the
  instructions.

For information about credentials, see [Credentials](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html "https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html") in the _AWS SDK for Python
Developer Guide_.

- Python 3.x (or later) and pip.
- The Amazon SNS Extended Client Library for Python (also available from [PyPI](https://pypi.org/project/amazon-sns-extended-client/ "https://pypi.org/project/amazon-sns-extended-client/")).

## Configuring message

storage

The below attributes are available on Boto3 Amazon SNS [Client](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#client "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#client"), [Topic](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/topic/index.html "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/topic/index.html"), and [PlatformEndpoint](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/platformendpoint/index.html "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/platformendpoint/index.html") objects to configure the Amazon S3 message storage
options.

- **`large_payload_support`**
  – The Amazon S3 bucket name that will store large messages.
- **`use_legacy_attribute`**
  – If `True`, then all published messages use the Legacy
  reserved message attribute (`SQSLargePayloadSize`) instead of the
  current reserved message attribute
  (`ExtendedPayloadSize`).
- **`message_size_threshold`**
  – The threshold for storing the message in the large messages bucket.
  Cannot be less than `0`, or greater than `262144`. The
  default is `262144`.
- **`always_through_s3`** –
  If `True`, then all messages are stored in Amazon S3. The default is
  `False`.
- **`s3_client`**
  – The Boto3 Amazon S3 `client` object to use to store objects
  to Amazon S3. Use this if you want to control the Amazon S3 client (for example,
  custom Amazon S3 config or credentials). Defaults to
  `boto3.client("s3")` on first use if not previously
  set.

## Example: Publishing messages to

Amazon SNS with the payload stored in Amazon S3

The following code example shows how to:

- Create a sample Amazon SNS topic and Amazon SQS queue.
- Attach the policy to the Amazon SQS queue to receive the message from Amazon SNS
  topic.
- Subscribe the queue to receive messages from the topic.
- Publish a test message using the Amazon SNS extended client, Topic resource,
  and PlatformEndpoint resource.
- The message payload is stored in Amazon S3, and the reference to it is
  published.
- Print the published message from the queue along with the original message
  retrieved from Amazon S3.

To publish a large message, use the Amazon SNS Extended Client Library for Python. The
message you send references an Amazon S3 object containing the actual message
content.

```
import boto3
from sns_extended_client import SNSExtendedClientSession
from json import loads

s3_extended_payload_bucket = "extended-client-bucket-store"  # S3 bucket with the given bucket name is a resource which is created and accessible with the given AWS credentials
TOPIC_NAME = "---TOPIC-NAME---"
QUEUE_NAME = "---QUEUE-NAME---"

def allow_sns_to_write_to_sqs(topicarn, queuearn):
    policy_document = """{{
        "Version": "2012-10-17",
        "Statement":[
            {{
            "Sid":"MyPolicy",
            "Effect":"Allow",
            "Principal" : {{"AWS" : "*"}},
            "Action":"SQS:SendMessage",
            "Resource": "{}",
            "Condition":{{
                "ArnEquals":{{
                "aws:SourceArn": "{}"
                }}
            }}
            }}
        ]
        }}""".format(queuearn, topicarn)

    return policy_document

def get_msg_from_s3(body,sns_extended_client):
    """Handy Helper to fetch message from S3"""
    json_msg = loads(body)
    s3_object = sns_extended_client.s3_client.get_object(
        Bucket=json_msg[1].get("s3BucketName"), Key=json_msg[1].get("s3Key")
    )
    msg = s3_object.get("Body").read().decode()
    return msg


def fetch_and_print_from_sqs(sqs, queue_url,sns_extended_client):
    sqs_msg = sqs.receive_message(
        QueueUrl=queue_url,
        AttributeNames=['All'],
        MessageAttributeNames=['All'],
        VisibilityTimeout=0,
        WaitTimeSeconds=0,
        MaxNumberOfMessages=1
    ).get("Messages")[0]

    message_body = sqs_msg.get("Body")
    print("Published Message: {}".format(message_body))
    print("Message Stored in S3 Bucket is: {}\n".format(get_msg_from_s3(message_body,sns_extended_client)))

    # Delete the Processed Message
    sqs.delete_message(
        QueueUrl=queue_url,
        ReceiptHandle=sqs_msg['ReceiptHandle']
    )


sns_extended_client = boto3.client("sns", region_name="us-east-1")
create_topic_response = sns_extended_client.create_topic(Name=TOPIC_NAME)
sns_topic_arn = create_topic_response.get("TopicArn")

# create and subscribe an sqs queue to the sns client
sqs = boto3.client("sqs",region_name="us-east-1")
demo_queue_url = sqs.create_queue(QueueName=QUEUE_NAME).get("QueueUrl")
sqs_queue_arn = sqs.get_queue_attributes(
    QueueUrl=demo_queue_url, AttributeNames=["QueueArn"]
)["Attributes"].get("QueueArn")

# Adding policy to SQS queue such that SNS topic can send msg to SQS queue
policy_json = allow_sns_to_write_to_sqs(sns_topic_arn, sqs_queue_arn)
response = sqs.set_queue_attributes(
    QueueUrl = demo_queue_url,
    Attributes = {
        'Policy' : policy_json
    }
)

# Set the RawMessageDelivery subscription attribute to TRUE if you want to use
# SQSExtendedClient to help with retrieving msg from S3
sns_extended_client.subscribe(TopicArn=sns_topic_arn, Protocol="sqs",
Endpoint=sqs_queue_arn
, Attributes={"RawMessageDelivery":"true"}
)

sns_extended_client.large_payload_support = s3_extended_payload_bucket

# Change default s3_client attribute of sns_extended_client to use 'us-east-1' region
sns_extended_client.s3_client = boto3.client("s3", region_name="us-east-1")


# Below is the example that all the messages will be sent to the S3 bucket
sns_extended_client.always_through_s3 = True
sns_extended_client.publish(
    TopicArn=sns_topic_arn, Message="This message should be published to S3"
)
print("\n\nPublished using SNS extended client:")
fetch_and_print_from_sqs(sqs, demo_queue_url,sns_extended_client)  # Prints message stored in s3

# Below is the example that all the messages larger than 32 bytes will be sent to the S3 bucket
print("\nUsing decreased message size threshold:")

sns_extended_client.always_through_s3 = False
sns_extended_client.message_size_threshold = 32
sns_extended_client.publish(
    TopicArn=sns_topic_arn,
    Message="This message should be published to S3 as it exceeds the limit of the 32 bytes",
)

fetch_and_print_from_sqs(sqs, demo_queue_url,sns_extended_client)  # Prints message stored in s3


# Below is the example to publish message using the SNS.Topic resource
sns_extended_client_resource = SNSExtendedClientSession().resource(
    "sns", region_name="us-east-1"
)

topic = sns_extended_client_resource.Topic(sns_topic_arn)
topic.large_payload_support = s3_extended_payload_bucket

# Change default s3_client attribute of topic to use 'us-east-1' region
topic.s3_client = boto3.client("s3", region_name="us-east-1")

topic.always_through_s3 = True
# Can Set custom S3 Keys to be used to store objects in S3
topic.publish(
    Message="This message should be published to S3 using the topic resource",
    MessageAttributes={
        "S3Key": {
            "DataType": "String",
            "StringValue": "347c11c4-a22c-42e4-a6a2-9b5af5b76587",
        }
    },
)
print("\nPublished using Topic Resource:")
fetch_and_print_from_sqs(sqs, demo_queue_url,topic)

# Below is the example to publish message using the SNS.PlatformEndpoint resource
sns_extended_client_resource = SNSExtendedClientSession().resource(
    "sns", region_name="us-east-1"
)

platform_endpoint = sns_extended_client_resource.PlatformEndpoint(sns_topic_arn)
platform_endpoint.large_payload_support = s3_extended_payload_bucket

# Change default s3_client attribute of platform_endpoint to use 'us-east-1' region
platform_endpoint.s3_client = boto3.client("s3", region_name="us-east-1")

platform_endpoint.always_through_s3 = True
# Can Set custom S3 Keys to be used to store objects in S3
platform_endpoint.publish(
    Message="This message should be published to S3 using the PlatformEndpoint resource",
    MessageAttributes={
        "S3Key": {
            "DataType": "String",
            "StringValue": "247c11c4-a22c-42e4-a6a2-9b5af5b76587",
        }
    },
)
print("\nPublished using PlatformEndpoint Resource:")
fetch_and_print_from_sqs(sqs, demo_queue_url,platform_endpoint)
```

**Output**

```
Published using SNS extended client:
Published Message: ["software.amazon.payloadoffloading.PayloadS3Pointer", {"s3BucketName": "extended-client-bucket-store", "s3Key": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"}]
Message Stored in S3 Bucket is: This message should be published to S3

Using decreased message size threshold:
Published Message: ["software.amazon.payloadoffloading.PayloadS3Pointer", {"s3BucketName": "extended-client-bucket-store", "s3Key": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"}]
Message Stored in S3 Bucket is: This message should be published to S3 as it exceeds the limit of the 32 bytes

Published using Topic Resource:
Published Message: ["software.amazon.payloadoffloading.PayloadS3Pointer", {"s3BucketName": "extended-client-bucket-store", "s3Key": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"}]
Message Stored in S3 Bucket is: This message should be published to S3 using the topic resource

Published using PlatformEndpoint Resource:
Published Message: ["software.amazon.payloadoffloading.PayloadS3Pointer", {"s3BucketName": "extended-client-bucket-store", "s3Key": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"}]
Message Stored in S3 Bucket is: This message should be published to S3 using the PlatformEndpoint resource
```
