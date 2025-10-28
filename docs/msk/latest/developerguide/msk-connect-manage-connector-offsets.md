# Manage source connector offsets using `offset.storage.topic`

This section provides information to help you manage source connector offsets using
the _offset storage topic_. The offset storage topic is
an internal topic that Kafka Connect uses to store connector and task configuration
offsets.

## Considerations

Consider the following when you manage source connector offsets.

- To specify an offset storage topic, provide the name of the Kafka topic
  where connector offsets are stored as the value for
  `offset.storage.topic` in your worker configuration.
- Use caution when you make changes to a connector configuration. Changing
  configuration values may result in unintended connector behavior if a source
  connector uses values from the configuration to key offset records. We
  recommend that you refer to your plugin's documentation for guidance.
- Customize default number of partitions
  – In addition to customizing the worker configuration by adding
  `offset.storage.topic`, you can customize the number of
  partitions for the offset and status storage topics. Default partitions for
  internal topics are as follows.
  - `config.storage.topic`: 1, not configurable, must be
    single partition topic
  - `offset.storage.topic`: 25, configurable by providing
    `offset.storage.partitions`
  - `status.storage.topic`: 5, configurable by providing
    `status.storage.partitions`

- Manually deleting topics – Amazon MSK
  Connect creates new Kafka connect internal topics (topic name starts with
  `__amazon_msk_connect`) on every deployment of connectors.
  Old topics that are attached to deleted connectors are not automatically
  removed because internal topics, such as `offset.storage.topic`,
  can be reused among connectors. However, you can manually delete unused
  internal topics created by MSK Connect. The internal topics are named
  following the format
  `__amazon_msk_connect_<offsets|status|configs>_`connector*name`*`connector_id``.

The regular expression
`__amazon_msk_connect_<offsets|status|configs>_`connector*name`*`connector_id``
can be used to delete the internal topics. You should not delete an internal topic that is currently in use by a running connector.

- Using the same name for the internal topics created
  by MSK Connect – If you want to reuse the offset storage
  topic to consume offsets from a previously created connector, you must give
  the new connector the same name as the old connector. The
  `offset.storage.topic` property can be set using the worker
  configuration to assign the same name to the
  `offset.storage.topic` and reused between different
  connectors. This configuration is described in [Managing connector offsets](msk-connect-workers.md#msk-connect-create-custom-worker-config "msk-connect-workers.md#msk-connect-create-custom-worker-config"). MSK Connect does not allow
  different connectors to share `config.storage.topic` and
  `status.storage.topic`. Those topics are created each time
  you create a new connector in MSKC. They are automatically named following
  the format
  `__amazon_msk_connect_<status|configs>_`connector*name`*`connector_id``,
  and so are different across the different connectors that you create.
