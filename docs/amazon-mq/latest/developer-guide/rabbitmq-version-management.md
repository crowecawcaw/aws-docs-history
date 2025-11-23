# Managing Amazon MQ for RabbitMQ engine versions

RabbitMQ organizes version numbers according to semantic versioning specification as
`X.Y.Z`. In Amazon MQ for RabbitMQ implementations, `X` denotes the
major version, `Y` represents the minor version, and `Z` denotes the patch version number.
Amazon MQ considers a version change to be major if the major version numbers change. For example, upgrading from
version **3**.13 to **4**.0 is
considered a major version upgrade. A version change is considered minor
if only the minor or patch version number changes. For example, upgrading from version 3.**11**.28 to 3.**12**.13 is
considered a minor version upgrade.

Amazon MQ for RabbitMQ recommends all brokers use the latest supported version RabbitMQ 4.2. For instructions on how to upgrade your broker engine version,
see [Upgrading an Amazon MQ broker engine version](upgrading-brokers.md "upgrading-brokers.md").

When you create a new Amazon MQ for RabbitMQ broker, you only need to specify the major and minor
version numbers. For example, RabbitMQ 4.2. If you do not specify the engine version when creating a broker,
Amazon MQ automatically defaults to the latest engine version.

###### Important

Amazon MQ does not support
[streams](https://www.rabbitmq.com/streams.html "https://www.rabbitmq.com/streams.html").
Creating a stream will result in data loss.

Amazon MQ does not support using structured logging in JSON.

Amazon MQ supports two major version releases of RabbitMQ:

- [RabbitMQ 4](rabbitmq-4.md "rabbitmq-4.md")

Amazon MQ supports RabbitMQ 4.2 in the RabbitMQ 4 release series only on the mq.m7g instance type
across all supported instance sizes.

- **RabbitMQ 3**

Amazon MQ supports RabbitMQ 3.13 in the RabbitMQ 3 release series on mq.t3, mq.m5, and mq.m7g
instance types across all supported instance sizes.

## Listing supported engine versions

You can list all supported minor and major engine versions by using the [`describe-broker-instance-options`](../../../cli/latest/reference/mq/describe-broker-instance-options.md "../../../cli/latest/reference/mq/describe-broker-instance-options.md")
AWS CLI command.

```
aws mq describe-broker-instance-options
```

To filter the results by engine and instance type use the
`--engine-type` and `--host-instance-type` options as shown in the following.

```
aws mq describe-broker-instance-options --engine-type `engine-type` --host-instance-type `instance-type`
```

For example, to filter the results for RabbitMQ, and `mq.m7g.large` instance type, replace
`engine-type` with `RABBITMQ` and `instance-type` with `mq.m7g.large`.
