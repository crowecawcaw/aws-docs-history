

# State management of Amazon MSK Connect applications
<a name="msk-connect-state-management"></a>

By default, Amazon MSK Connect creates three separate topics in the Kafka cluster for each Amazon MSK Connector to store the connector’s configuration, offset, and status. The default topic names are structured as follows:
+ \_\_msk\_connect\_configs\_{{connector-name}}\_{{connector-id}}
+ \_\_msk\_connect\_status\_{{connector-name}}\_{{connector-id}}
+ \_\_msk\_connect\_offsets\_{{connector-name}}\_{{connector-id}}

**Note**  
To provide the offset continuity between source connectors, you can use an offset storage topic of your choice, instead of the default topic. Specifying an offset storage topic helps you accomplish tasks like creating a source connector that resumes reading from the last offset of a previous connector. To specify an offset storage topic, supply a value for the [offset.storage.topic](https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect-workers.html#msk-connect-manage-connector-offsets) property in the Amazon MSK Connect worker configuration before creating the connector.