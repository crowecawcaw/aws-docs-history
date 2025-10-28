# Set up EventBridge Kafka sink connector for MSK Connect

This topic shows you how to set up the [EventBridge Kafka sink connector](https://github.com/awslabs/eventbridge-kafka-connector "https://github.com/awslabs/eventbridge-kafka-connector") for MSK Connect. This connector lets you send events from your MSK cluster to EventBridge [event buses](../../../eventbridge/latest/userguide/eb-event-bus.md "../../../eventbridge/latest/userguide/eb-event-bus.md"). This topic describes the process for creating the required resources and configuring the connector to enable seamless data flow between Kafka and EventBridge.

###### Topics

- [Prerequisites](#mkc-eb-kafka-prerequisites "#mkc-eb-kafka-prerequisites")
- [Set up the resources required for MSK Connect](#mkc-eb-kafka-set-up-resources "#mkc-eb-kafka-set-up-resources")
- [Create the connector](#mkc-eb-kafka-create-connector "#mkc-eb-kafka-create-connector")
- [Send messages to Kafka](#mkc-eb-kafka-send-json-encoded-messages "#mkc-eb-kafka-send-json-encoded-messages")

## Prerequisites

Before deploying the connector, make sure that you have the following resources:

- **Amazon MSK cluster**: An active MSK cluster to produce and consume Kafka messages.
- **Amazon EventBridge event bus**: An EventBridge event bus to receive events from the Kafka topics.
- **IAM roles**: Create IAM roles with the necessary permissions for MSK Connect and the EventBridge connector.
- [Access to the public internet](msk-connect-internet-access.md "msk-connect-internet-access.md") from MSK Connect or a [VPC interface endpoint](../../../eventbridge/latest/userguide/eb-related-service-vpc.md "../../../eventbridge/latest/userguide/eb-related-service-vpc.md") for EventBridge created in the VPC and subnet of your MSK cluster. This helps you avoid traversing the public internet and without requiring NAT gateways.
- A [client machine](create-serverless-cluster-client.md "create-serverless-cluster-client.md"), such as an Amazon EC2 instance or [AWS CloudShell](https://aws.amazon.com/cloudshell/ "https://aws.amazon.com/cloudshell/"), to create topics and send records to Kafka.

## Set up the resources required for MSK Connect

You create an IAM role for the connector, and then you create the connector. You also create an EventBridge rule to filter Kafka events sent to the EventBridge event bus.

###### Topics

- [IAM role for the connector](#mkc-eb-kafka-iam-role-connector "#mkc-eb-kafka-iam-role-connector")
- [An EventBridge rule for incoming events](#mkc-eb-kafka-create-rule "#mkc-eb-kafka-create-rule")

### IAM role for the connector

The IAM role that you associate with the connector must have the [PutEvents](../../../eventbridge/latest/userguide/eb-permissions-reference.md "../../../eventbridge/latest/userguide/eb-permissions-reference.md") permission to allow sending events to EventBridge. The following IAM policy example grants you the permissin to send events to an event bus named `example-event-bus`. Make sure that you replace the resource ARN in the following example with the ARN of your event bus.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "events:PutEvents"
 ],
 "Resource": "arn:aws:events:`us-east-1`:`123456789012`:event-bus/`example-event-bus`"
 }
 ]
}`

```

In addition, you must make sure that your IAM role for the connector contains the following trust policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "kafkaconnect.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

### An EventBridge rule for incoming events

You create [rules](../../../eventbridge/latest/userguide/eb-rules.md "../../../eventbridge/latest/userguide/eb-rules.md") that match incoming events with event data criteria, known as [_event pattern_](../../../eventbridge/latest/userguide/eb-event-patterns.md "../../../eventbridge/latest/userguide/eb-event-patterns.md"). With an event pattern, you can define the criteria to filter incoming events, and determine which events should trigger a particular rule and subsequently be routed to a designated [target](../../../eventbridge/latest/userguide/eb-targets.md "../../../eventbridge/latest/userguide/eb-targets.md"). The following example of an event pattern matches Kafka events sent to the EventBridge event bus.

```
{
  "detail": {
    "topic": ["msk-eventbridge-tutorial"]
  }
}
```

The following is an example of an event sent from Kafka to EventBridge using the Kafka sink connector.

```
{
  "version": "0",
  "id": "dbc1c73a-c51d-0c0e-ca61-ab9278974c57",
  "account": "123456789012",
  "time": "2025-03-26T10:15:00Z",
  "region": "us-east-1",
  "detail-type": "msk-eventbridge-tutorial",
  "source": "kafka-connect.msk-eventbridge-tutorial",
  "resources": [],
  "detail": {
    "topic": "msk-eventbridge-tutorial",
    "partition": 0,
    "offset": 0,
    "timestamp": 1742984100000,
    "timestampType": "CreateTime",
    "headers": [],
    "key": "order-1",
    "value": {
      "orderItems": [
        "item-1",
        "item-2"
      ],
      "orderCreatedTime": "Wed Mar 26 10:15:00 UTC 2025"
    }
  }
}
```

In the EventBridge console, [create a rule](../../../eventbridge/latest/userguide/eb-create-rule.md "../../../eventbridge/latest/userguide/eb-create-rule.md") on the event bus using this example pattern and specify a target, such as a CloudWatch Logs group. The EventBridge console will automatically configure the necessary access policy for the CloudWatch Logs group.

## Create the connector

In the following section, you create and deploy the [EventBridge Kafka sink connector](https://github.com/awslabs/eventbridge-kafka-connector "https://github.com/awslabs/eventbridge-kafka-connector") using the AWS Management Console.

###### Topics

- [Step 1: Download the connector](#mkc-eb-kafka-download-connector "#mkc-eb-kafka-download-connector")
- [Step 2: Create an Amazon S3 bucket](#mkc-eb-kafka-s3-bucket-create "#mkc-eb-kafka-s3-bucket-create")
- [Step 3: Create a plugin in MSK Connect](#mkc-eb-kafka-create-plugin "#mkc-eb-kafka-create-plugin")
- [Step 4: Create the connector](#mkc-eb-kafka-create-connector "#mkc-eb-kafka-create-connector")

### Step 1: Download the connector

Download the latest EventBridge connector sink JAR from the [GitHub releases page](https://github.com/awslabs/eventbridge-kafka-connector/releases "https://github.com/awslabs/eventbridge-kafka-connector/releases") for the EventBridge Kafka connector. For example, to download the version v1.4.1, choose the JAR file link, `kafka-eventbridge-sink-with-dependencies.jar`, to download the connector. Then, save the file to a preferred location on your machine.

### Step 2: Create an Amazon S3 bucket

1. To store the JAR file in Amazon S3 for use with MSK Connect, open the AWS Management Console, and then choose Amazon S3.
2. In the Amazon S3 console, choose **Create bucket**, and enter a unique bucket name. For example, `amzn-s3-demo-bucket1-eb-connector`.
3. Choose an appropriate Region for your Amazon S3 bucket. Make sure that it matches the Region where your MSK cluster is deployed.
4. For **Bucket settings**, keep the default selections or adjust as needed.
5. Choose **Create bucket**
6. Upload the JAR file to the Amazon S3 bucket.

### Step 3: Create a plugin in MSK Connect

1. Open the AWS Management Console, and then navigate to **MSK Connect**.
2. In the left navigation pane, choose **Custom plugins**.
3. Choose **Create plugin**, and then enter a **Plugin name**. For example, `eventbridge-sink-plugin`.
4. For **Custom plugin location**, paste the **S3 object URL**.
5. Add an optional description for the plugin.
6. Choose **Create plugin**.

After the plugin is created, you can use it to configure and deploy the EventBridge Kafka connector in MSK Connect.

### Step 4: Create the connector

Before creating the connector, we recommend to create the required Kafka topic to avoid connector errors. To create the topic, use your client machine.

1. In the left pane of the MSK console, choose **Connectors**, and then choose **Create connector**.
2. In the list of plugins, choose **eventbridge-sink-plugin**, then choose **Next**.
3. For the connector name, enter `EventBridgeSink`.
4. In the list of clusters, choose your MSK cluster.
5. Copy the following configuration for the connector and paste it into the **Connector configuration** field

Replace the placeholders in the following configuration, as required.

    * Remove `aws.eventbridge.endpoint.uri` if your MSK cluster has public internet accesss.
    * If you use PrivateLink to securely connect from MSK to EventBridge, replace the DNS part after `https://` with the correct private DNS name of the (optional) VPC interface endpoint for EventBridge that you created earlier.
    * Replace the EventBridge event bus ARN in the following configuration with the ARN of your event bus.
    * Update any Region-specific values.

```
{
  "connector.class": "software.amazon.event.kafkaconnector.EventBridgeSinkConnector",
  "aws.eventbridge.connector.id": "msk-eventbridge-tutorial",
  "topics": "msk-eventbridge-tutorial",
  "tasks.max": "1",
  "aws.eventbridge.endpoint.uri": "https://events.us-east-1.amazonaws.com",
  "aws.eventbridge.eventbus.arn": "arn:aws:events:us-east-1:123456789012:event-bus/example-event-bus",
  "value.converter.schemas.enable": "false",
  "value.converter": "org.apache.kafka.connect.json.JsonConverter",
  "aws.eventbridge.region": "us-east-1",
  "auto.offset.reset": "earliest",
  "key.converter": "org.apache.kafka.connect.storage.StringConverter"
}
```

For more information about connector configuration, see [eventbridge-kafka-connector](https://github.com/awslabs/eventbridge-kafka-connector "https://github.com/awslabs/eventbridge-kafka-connector").

If needed, change the settings for workers and autoscaling. We also recommend to use the latest available (recommended) Apache Kafka Connect version from the dropdown. Under **Access permissions**, use the role created earlier. We also recommend to enable logging to CloudWatch for observability and troubleshooting. Adjust the other optional settings, such as tags, based on your needs. Then, deploy the connector and wait for the status to enter Running state.

## Send messages to Kafka

You can configure message encodings, such as Apache Avro and JSON, by specifying different converters using the `value.converter` and, optionally, `key.converter` settings available in Kafka Connect.

The [connector example](#connector-ex "#connector-ex") in this topic is configured to work with JSON-encoded messages, as indicated by the use of `org.apache.kafka.connect.json.JsonConverter` for `value converter`. When the connector is in Running state, send records to the `msk-eventbridge-tutorial` Kafka topic from your client machine.
