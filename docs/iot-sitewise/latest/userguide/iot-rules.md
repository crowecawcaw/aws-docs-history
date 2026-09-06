

# Ingest data to AWS IoT SiteWise using AWS IoT Core rules
<a name="iot-rules"></a>

Send data to AWS IoT SiteWise from AWS IoT things and other AWS services by using rules in AWS IoT Core. Rules transform MQTT messages and perform actions to interact with AWS services. The AWS IoT SiteWise rule action forwards messages data to the [BatchPutAssetPropertyValue](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_BatchPutAssetPropertyValue.html) operation from the AWS IoT SiteWise API. For more information, see [Rules](https://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html) and [AWS IoT SiteWise action](https://docs.aws.amazon.com/iot/latest/developerguide/iot-rule-actions.html#iotsitewise-rule) in the *AWS IoT Developer Guide*.

To follow a tutorial that walks through the steps required to set up a rule that ingests data through device shadows, see [Ingest data to AWS IoT SiteWise from AWS IoT things](ingest-data-from-iot-things.md).

You can also send data from AWS IoT SiteWise to other AWS services. For more information, see [Interact with other AWS services](interact-with-other-services.md).

**Topics**
+ [Grant AWS IoT the required access](grant-rule-access.md)
+ [Configure the AWS IoT SiteWise rule action](configure-rule-action.md)
+ [Reduce costs with Basic Ingest in AWS IoT SiteWise](basic-ingest-rules.md)