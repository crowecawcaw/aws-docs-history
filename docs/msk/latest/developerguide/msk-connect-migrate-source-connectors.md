

# Migrate source connectors to Amazon MSK Connect
<a name="msk-connect-migrate-source-connectors"></a>

Source connectors are Apache Kafka Connect applications that import records from external systems into Kafka. This section describes the process for migrating Apache Kafka Connect source connector applications that are running on-premises or self-managed Kafka Connect clusters that are running on AWS to Amazon MSK Connect.

The Kafka Connect source connector application stores offsets in a topic that’s named with the value that’s set for the config property `offset.storage.topic`. The following are the sample offset messages for a JDBC connector that’s running two tasks that import data from two different tables named `movies` and `shows`. The most recent row imported from the table movies has a primary ID of `18343`. The most recent row imported from the shows table has a primary ID of `732`.

```
["jdbcsource",{"protocol":"1","table":"sample.movies"}] {"incrementing":18343}
["jdbcsource",{"protocol":"1","table":"sample.shows"}] {"incrementing":732}
```

To migrate source connectors to Amazon MSK Connect, do the following:

1. Create an Amazon MSK Connect [custom plugin](https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect-plugins.html) by pulling connector libraries from your on-premises or self-managed Kafka Connect cluster.

1. Create Amazon MSK Connect [worker properties](https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect-config-provider.html#msk-connect-config-providers-create-custom-config) and set the properties `key.converter`, `value.converter`, and `offset.storage.topic` to the same values that are set for the Kafka connector that’s running in your existing Kafka Connect cluster.

1. Pause the connector application on the existing cluster by making a `PUT /connectors/{{connector-name}}/pause` request on the existing Kafka Connect cluster.

1. Make sure that all of the connector application’s tasks are completely stopped. You can stop the tasks either by making a `GET /connectors/{{connector-name}}/status` request on the existing Kafka Connect cluster or by consuming the messages from the topic name that’s set for the property `status.storage.topic`.

1. Get the connector configuration from the existing cluster. You can get the connector configuration either by making a `GET /connectors/{{connector-name}}/config/` request on the existing cluster or by consuming the messages from the topic name that’s set for the property `config.storage.topic`.

1. Create a new [Amazon MSK Connector](https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect-connectors.html) with the same name as an existing cluster. Create this connector by using the connector custom plugin that you created in step 1, the worker properties that you created in step 2, and the connector configuration that you extracted in step 5.

1. When the Amazon MSK Connector status is `active`, view the logs to verify that the connector has started importing data from the source system.

1. Delete the connector in the existing cluster by making a `DELETE /connectors/{{connector-name}}` request.