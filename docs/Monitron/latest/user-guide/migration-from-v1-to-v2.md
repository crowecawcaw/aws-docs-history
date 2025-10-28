Amazon Monitron is no longer open to new customers. Existing customers can
continue to use the service as normal. For capabilities similar to Amazon
Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron "https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron").

# Migration from Kinesis v1 to v2

If you are currently using the v1 data schema, you may already be sending data to
Amazon S3, or further processing the data stream payload with Lambda.

###### Topics

- [Updating the data schema to v2](#updating-to-v2 "#updating-to-v2")
- [Updating data processing with Lambda](#updating-with-lam "#updating-with-lam")

## Updating the data schema to v2

If you have already configured a data stream with the v1 schema, you can
update your data export process by doing the following:

1. Open your Amazon Monitron console.
2. Navigate to your project.
3. Stop the [current live data
   export](monitron-kinesis-export-v2.md#stop-kinesis-export-v2 "monitron-kinesis-export-v2.md#stop-kinesis-export-v2").
4. Start the live data export to create a new data stream.
5. Select the newly created data stream.
6. Choose **start live data export**. At this point, the
   new schema will send your payload through the data stream.
7. (Optional) Go to the Kinesis console and delete your old data
   stream.
8. Configure a new delivery method for your newly created data stream
   with the v2 schema.

Your new stream now delivers payloads conforming to the v2 schema to your new
bucket. We recommend using two distinct buckets to have a consistent format in
case you want to process all the data in these buckets. For example, using other
services such as Athena and AWS Glue.

###### Note

If you were delivering your data to Amazon S3, learn how to [store exported data in Amazon S3](kinesis-store-S3-v2.md#kinesis-store-S3-title-v2 "kinesis-store-S3-v2.md#kinesis-store-S3-title-v2")
for details on how to deliver your data to Amazon S3 with the v2 schema.

###### Note

If you were using a Lambda function to process your payloads, learn how to
[process data with Lambda](data-export-lambda.md "data-export-lambda.md"). You can also refer to the [updating with Lambda](#updating-with-lam "#updating-with-lam") section for more
information.

## Updating data processing with Lambda

Updating the data processing with Lambda requires you to consider that the v2
data stream is now event-based. Your initial v1 Lambda code may have been similar
to the following:

```
import base64

def main_handler(event):
    # Kinesis "data" blob is base64 encoded so decode here:
    for record in event['Records']:
        payload = base64.b64decode(record["kinesis"]["data"])

        measurement = payload["measurement"]
        projectDisplayName = payload["projectDisplayName"]

        # Process the content of the measurement
        # ...
```

Since the v1 data schema is on a deprecation path, the previous Lambda code
won't work with all the new data streams.

The following Python sample code will process events from Kinesis stream with
the data schema v2. This code uses the new `eventType` parameter to
orient the processing to the appropriate handler:

```
import base64

handlers = {
    "measurement": measurementEventHandler,
    "gatewayConnected": gatewayConnectedEventHandler,
    "gatewayDisconnected": gatewayDisconnectedEventHandler,
    "sensorConnected": sensorConnectedEventHandler,
    "sensorDisconnected": sensorDisconnectedEventHandler,
}

def main_handler(event):
    # Kinesis "data" blob is base64 encoded so decode here:
    for record in event['Records']:
        payload = base64.b64decode(record["kinesis"]["data"])

        eventType = payload["eventType"]
        if eventType not in handler.keys():
            log.info("No event handler found for the event type: {event['eventType']}")
            return

        # Invoke the appropriate handler based on the event type.
        eventPayload = payload["eventPayload"]
        eventHandler = handlers[eventType]
        eventHandler(eventPayload)

def measurementEventHandler(measurementEventPayload):
    # Handle measurement event
    projectName = measurementEventPayload["projectName"]

    # ...

def gatewayConnectedEventHandler(gatewayConnectedEventPayload):
    # Handle gateway connected event

# Other event handler functions
```
