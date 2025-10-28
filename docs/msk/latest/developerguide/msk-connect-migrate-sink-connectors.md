# Migrate sink connectors to Amazon MSK

Connect

Sink connectors are Apache Kafka Connect applications that export data from Kafka to external systems. This section describes the process for migrating Apache Kafka Connect sink connector applications that are running on-premises or self-managed Kafka Connect clusters that are running on AWS to Amazon MSK Connect.

Kafka Connect sink connectors use the Kafka group membership API and store offsets in the same `__consumer_offset` topics as a typical consumer application. This behavior simplifies migration of the sink connector from a self-managed cluster to Amazon MSK Connect.

To migrate sink connectors to Amazon MSK Connect, do the following:

1. Create an Amazon MSK Connect [custom plugin](msk-connect-plugins.md "msk-connect-plugins.md") by pulling connector libraries from your on-premises or self-managed Kafka Connect cluster.
2. Create Amazon MSK Connect [worker properties](msk-connect-config-provider.md#msk-connect-config-providers-create-custom-config "msk-connect-config-provider.md#msk-connect-config-providers-create-custom-config") and set the properties `key.converter` and `value.converter` to the same values that are set for the Kafka connector that’s running in your existing Kafka Connect cluster.
3. Pause the connector application on your existing cluster by making a `PUT /connectors/`connector-name`/pause` request on the existing Kafka Connect cluster.
4. Make sure that all of the connector application’s tasks are completely stopped. You can stop the tasks either by making a `GET /connectors/`connector-name`/status` request on the existing Kafka Connect cluster, or by consuming the messages from the topic name that’s set for the property `status.storage.topic`.
5. Get the connector configuration from the existing cluster. You can get the connector configuration either by making a `GET /connectors/`connector-name`/config` request on the existing cluster, or by consuming the messages from the topic name that’s set for the property `config.storage.topic`.
6. Create a new [Amazon MSK Connector](msk-connect-connectors.md "msk-connect-connectors.md") with same name as the existing cluster. Create this connector by using the connector custom plugin that you created in step 1, the worker properties that you created in step 2, and the connector configuration that you extracted in step 5.
7. When the Amazon MSK Connector status is `active`, view the logs to verify that the connector has started importing data from the source system.
8. Delete the connector in the existing cluster by making a `DELETE /connectors/`connector-name`` request.
