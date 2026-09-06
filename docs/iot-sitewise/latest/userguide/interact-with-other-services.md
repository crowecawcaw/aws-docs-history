

# Interact with other AWS services
<a name="interact-with-other-services"></a>

AWS IoT SiteWise can publish asset data to the AWS IoT MQTT publish-subscribe message broker, so that you can interact with your asset data from other AWS services. AWS IoT SiteWise assigns each asset property a unique MQTT topic that you can use to route your asset data to other AWS services using AWS IoT Core rules. For example, you can configure AWS IoT Core rules to do the following tasks:
+ Identify equipment failure and notify appropriate personnel by sending data to [AWS IoT Events](https://docs.aws.amazon.com/iotevents/latest/developerguide/).
+ Historize select asset data for use in external software solutions by sending data to [Amazon DynamoDB](https://docs.aws.amazon.com/dynamodb/).
+ Generate weekly reports by triggering an [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) function.

You can follow a tutorial that walks through the steps required to set up a rule that stores property values in DynamoDB. For more information, see [Publish property value updates to Amazon DynamoDB](publish-to-amazon-dynamodb.md).

For more information about how to configure a rule, see [Rules](https://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html) in the *AWS IoT Developer Guide*.

You can also consume data from other AWS services back into AWS IoT SiteWise. To ingest data through the AWS IoT SiteWise rule action, see [Ingest data to AWS IoT SiteWise using AWS IoT Core rules](iot-rules.md).

**Topics**
+ [Understand asset properties in MQTT topics](mqtt-topics.md)
+ [Turn on asset property notifications in AWS IoT SiteWise](property-notifications.md)
+ [Query asset property notifications in AWS IoT SiteWise](query-notification-messages.md)
+ [Export data to Amazon S3 with asset property notifications](export-to-s3.md)
+ [Integrate AWS IoT SiteWise with Grafana](grafana-integration.md)
+ [Integrate AWS IoT SiteWise and AWS IoT TwinMaker](integrate-tm.md)
+ [Detect anomalies with Lookout for Equipment](anomaly-detection.md)