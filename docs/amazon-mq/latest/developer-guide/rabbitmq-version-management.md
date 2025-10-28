# Managing Amazon MQ for RabbitMQ engine versions

RabbitMQ organizes version numbers according to semantic versioning specification as
`X.Y.Z`. In Amazon MQ for RabbitMQ implementations, `X` denotes the
major version, `Y` represents the minor version, and `Z` denotes the patch version number.
Amazon MQ considers a version change to be major if the major version numbers change. For example, upgrading from
version **3**.13 to **4**.0 is
considered a _major version upgrade_. A version change is considered
minor if only the minor or patch version number changes. For example, upgrading from version 3.**11**.28 to 3.**12**.13 is
considered a _minor version upgrade_.

Amazon MQ for RabbitMQ recommends all brokers use the latest supported minor version. For instructions on how to upgrade your broker engine version,
see [Upgrading an Amazon MQ broker engine version](upgrading-brokers.md "upgrading-brokers.md").

###### Important

Amazon MQ does not support
[streams](https://www.rabbitmq.com/streams.html "https://www.rabbitmq.com/streams.html").
Creating a stream will result in data loss.

Amazon MQ does not support using structured logging in JSON, introduced in RabbitMQ 3.9

## Supported engine versions on Amazon MQ for RabbitMQ

The Amazon MQ version support calendar indicates when a broker engine version
will reach end of support. When a version reaches end of support, Amazon MQ
upgrades all brokers on this version to the next supported version automatically.
This upgrade takes place during your broker's scheduled maintenance windows,
within the 45 days following the end-of-support date.

Amazon MQ provides at least a 90 day notice before a version reaches end of support.
We recommend upgrading your broker before the end-of-support date to prevent any disruptions.
Additionally, you cannot create new brokers on versions scheduled for end of support within 30
days of the end of support date.

| RabbitMQ version   | End of support on Amazon MQ |
| ------------------ | --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 3.13 (recommended) |                             |
| 3.12               | March 17, 2025              |
| 3.11               | February 17, 2025           |
| 3.10               | October 15, 2024            |
| 3.9                | September 16, 2024          | When you create a new Amazon MQ for RabbitMQ broker, you can specify any supported RabbitMQ engine version. If you do not specify the engine version number when creating a broker, Amazon MQ automatically defaults to the latest engine version number. ## Engine version upgrades You can manually upgrade your broker at any time to the next supported major or minor version. When you turn on [automatic minor version upgrades](../api-reference/brokers-broker-id.md#brokers-broker-id-prop-updatebrokerinput-autominorversionupgrade "../api-reference/brokers-broker-id.md#brokers-broker-id-prop-updatebrokerinput-autominorversionupgrade"), Amazon MQ will upgrade your broker to the latest supported patch version during the [maintenance window](maintaining-brokers.md "maintaining-brokers.md"). For more information about manually upgrading your broker, see [Upgrading an Amazon MQ broker engine version](upgrading-brokers.md "upgrading-brokers.md"). For all brokers using engine version 3.13 and above, Amazon MQ manages upgrades to the latest supported patch version during the maintenance window. ###### Important RabbitMQ only allows incremental version updates (ex: 3.9.x to 3.10.x). You cannot skip minor versions when updating (ex: 3.8.x to 3.11.x). Single instance brokers will be offline while being rebooted. For cluster brokers, the mirrored queues must be synced during reboot. With longer queues, the queue-sync process can take longer. During the queue-sync process, the queue is unavailable to consumers and producer. When the queue-sync process is complete, the broker becomes available again. To minimize the impact, we recommend upgrading during a low traffic time. For more information on best practices for version upgrades, see [Amazon MQ for RabbitMQ best practices](best-practices-rabbitmq.md "best-practices-rabbitmq.md"). ## Listing supported engine versions You can list all supported minor and major engine versions by using the [`describe-broker-instance-options`](../../../cli/latest/reference/mq/describe-broker-instance-options.md "../../../cli/latest/reference/mq/describe-broker-instance-options.md") AWS CLI command. `aws mq describe-broker-instance-options` To filter the results by engine and instance type use the `--engine-type` and `--host-instance-type` options as shown in the following. `` aws mq describe-broker-instance-options --engine-type `engine-type` --host-instance-type `instance-type` `` For example, to filter the results for RabbitMQ, and `mq.m7g.large` instance type, replace `engine-type` with `RABBITMQ` and `instance-type` with `mq.m7g.large`. |
