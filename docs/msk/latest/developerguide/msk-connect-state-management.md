# State management of Amazon MSK Connect applications

By default, Amazon MSK Connect creates three separate topics in the Kafka cluster for each Amazon MSK Connector to store the connector’s configuration, offset, and status. The default topic names are structured as follows:

- \_\_msk_connect_configs\_`connector-name`\_`connector-id`
- \_\_msk_connect_status\_`connector-name`\_`connector-id`
- \_\_msk_connect_offsets\_`connector-name`\_`connector-id`

###### Note

To provide the offset continuity between source connectors, you can use an offset storage topic of your choice, instead of the default topic. Specifying an offset storage topic helps you accomplish tasks like creating a source connector that resumes reading from the last offset of a previous connector. To specify an offset storage topic, supply a value for the [offset.storage.topic](msk-connect-workers.md#msk-connect-manage-connector-offsets "msk-connect-workers.md#msk-connect-manage-connector-offsets") property in the Amazon MSK Connect worker configuration before creating the connector.
