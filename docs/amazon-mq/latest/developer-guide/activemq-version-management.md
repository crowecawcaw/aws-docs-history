# Managing Amazon MQ for ActiveMQ engine versions

Apache ActiveMQ organizes version numbers according to semantic versioning specification
as `X.Y.Z`. In Amazon MQ for ActiveMQ implementations, `X` denotes the
major version, `Y` represents the minor version, and `Z` denotes the
patch version number. Amazon MQ considers a version change to be major if the major version
numbers change. For example, upgrading from version **5**.17 to
**6**.0 is considered a _major version
upgrade_. A version change is considered minor if only the minor or patch
version number changes. For example, upgrading from version 5.**18** to 5.**19** is considered a _minor
version upgrade_. When `autoMinorVersionUpgrade` is turned on,
Amazon MQ upgrades your broker to the newest available patch version.

Amazon MQ for ActiveMQ recommends all brokers use the latest supported minor version. For instructions on how to upgrade your broker engine version,
see [Upgrading an Amazon MQ broker engine version](upgrading-brokers.md "upgrading-brokers.md").

## Supported engine versions on Amazon MQ for ActiveMQ

The Amazon MQ version support calendar indicates when a broker engine version
will reach end of support. When a version reaches end of support, Amazon MQ
upgrades all brokers on this version to the next supported version automatically.
This upgrade takes place during your broker's scheduled maintenance windows,
within the 45 days following the end-of-support date.

Amazon MQ provides at least a 90 day notice before a version reaches end of support.
We recommend upgrading your broker before the end-of-support date to prevent any disruptions.
Additionally, you cannot create new brokers on versions scheduled for end of support within 30
days of the end of support date.

| Apache ActiveMQ version     | End of support on Amazon MQ |
| --------------------------- | --------------------------- |
| ActiveMQ 5.18 (recommended) |                             |
| ActiveMQ 5.17               | June 16, 2025               |
| ActiveMQ 5.16               | November 15, 2024           |
| ActiveMQ 5.15               | September 16, 2024          |

When you create a new Amazon MQ for ActiveMQ broker, you can specify any supported ActiveMQ engine version.
If you do not specify the engine version number
when creating a broker, Amazon MQ automatically defaults
to the latest engine version number.

## Engine version upgrades

You can manually upgrade your broker at any time to the next supported major or minor version. When you turn on
[automatic minor version upgrades](../api-reference/brokers-broker-id.md#brokers-broker-id-prop-updatebrokerinput-autominorversionupgrade "../api-reference/brokers-broker-id.md#brokers-broker-id-prop-updatebrokerinput-autominorversionupgrade"),
Amazon MQ will upgrade your broker to the latest supported patch version during the [maintenance window](maintaining-brokers.md "maintaining-brokers.md").

For more information about manually upgrading your broker, see [Upgrading an Amazon MQ broker engine version](upgrading-brokers.md "upgrading-brokers.md").

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

For example, to filter the results for ActiveMQ, and `mq.m5.large` instance type, replace
`engine-type` with `ACTIVEMQ` and `instance-type` with `mq.m5.large`.
