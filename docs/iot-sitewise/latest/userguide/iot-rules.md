# Ingest data to AWS IoT SiteWise using AWS IoT Core rules

Send data to AWS IoT SiteWise from AWS IoT things and other AWS services by using rules in
AWS IoT Core. Rules transform MQTT messages and perform actions to interact with AWS services.
The AWS IoT SiteWise rule action forwards messages data to the [BatchPutAssetPropertyValue](../APIReference/API_BatchPutAssetPropertyValue.md "../APIReference/API_BatchPutAssetPropertyValue.md") operation from the
AWS IoT SiteWise API. For more information, see [Rules](../../../iot/latest/developerguide/iot-rules.md "../../../iot/latest/developerguide/iot-rules.md") and [AWS IoT SiteWise action](../../../iot/latest/developerguide/iot-rule-actions.md#iotsitewise-rule "../../../iot/latest/developerguide/iot-rule-actions.md#iotsitewise-rule") in the
_AWS IoT Developer Guide_.

To follow a tutorial that walks through the steps required to set up a rule that
ingests data through device shadows, see [Ingest data to AWS IoT SiteWise from AWS IoT things](ingest-data-from-iot-things.md "ingest-data-from-iot-things.md").

You can also send data from AWS IoT SiteWise to other AWS services. For more information, see
[Interact with other AWS services](interact-with-other-services.md "interact-with-other-services.md").

###### Topics

- [Grant AWS IoT the required access](grant-rule-access.md "grant-rule-access.md")
- [Configure the AWS IoT SiteWise rule action](configure-rule-action.md "configure-rule-action.md")
- [Reduce costs with Basic Ingest in AWS IoT SiteWise](basic-ingest-rules.md "basic-ingest-rules.md")
