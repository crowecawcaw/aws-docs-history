# Reducing messaging costs with Basic Ingest

You can use Basic Ingest, to securely send device data to the AWS services supported by
[AWS IoT rule actions](iot-rule-actions.md "iot-rule-actions.md"), without incurring [messaging costs](https://aws.amazon.com/iot-core/pricing/ "https://aws.amazon.com/iot-core/pricing/"). Basic Ingest optimizes
data flow by removing the publish/subscribe message broker from the ingestion path.

Basic Ingest can send messages from your devices or applications. The messages have topic
names that start with `$aws/rules/`rule_name`for their
 first three levels, where`rule_name`` is the name of the
AWS IoT rule that you want to invoke.

You can use an existing rule with Basic Ingest by adding the Basic Ingest prefix
(`$aws/rules/`rule_name``) to the message topic that
 you'd use to invoke the rule. For example, if you have a rule named `BuildingManager`  that's invoked by messages with topics like
 `Buildings/Building5/Floor2/Room201/Lights` (`"sql": "SELECT \* FROM
'Buildings/#'"`), you can invoke the same rule with Basic Ingest by sending a message
 with topic
 `$aws/rules/BuildingManager/Buildings/Building5/Floor2/Room201/Lights`.

###### Note

- Your devices and rules can't subscribe to Basic Ingest reserved topics. For
  example, the AWS IoT Device Defender metric `num-messages-received` metrics is not
  emitted as it doesn't support subscribing to topics. For more
  information, see [Reserved topics](reserved-topics.md "reserved-topics.md").
- If you need a publish/subscribe broker to distribute messages to multiple subscribers
  (for example, to deliver messages to other devices and the rules engine), you should
  continue to use the AWS IoT message broker to handle the message distribution. However, make
  sure that you publish your messages on topics other than Basic Ingest topics.

## Using Basic Ingest

Before you use Basic Ingest, verify that your device or application is using a [policy](iot-policies.md "iot-policies.md") that has publish permissions on
`$aws/rules/*`. Or, you can specify permission for individual rules
with `$aws/rules/`rule_name`/*` in the policy. Otherwise,
your devices and applications can continue to use their existing connections with
AWS IoT Core.

When the message reaches the rules engine, there's no difference in implementation or
error handling between rules invoked from Basic Ingest and those invoked through message
broker subscriptions.

You can create rules for use with Basic Ingest. Keep in mind the following:

- The initial prefix of a Basic Ingest topic
  (`$aws/rules/`rule_name``) isn't available to the
  [topic(Decimal)](iot-sql-functions.md#iot-function-topic "iot-sql-functions.md#iot-function-topic") function.
- If you define a rule that's invoked only with Basic Ingest, the `FROM`
  clause is optional in the `sql` field of the `rule` definition. It's
  still required if the rule is also invoked by other messages that must be sent through the
  message broker (for example, because those other messages must be distributed to multiple
  subscribers). For more information, see [AWS IoT SQL reference](iot-sql-reference.md "iot-sql-reference.md").
- The first three levels of the Basic Ingest topic
  (`$aws/rules/`rule_name``) aren't counted toward
  the 8-segment length limit or toward the 256-total character limit for a topic. Otherwise,
  the same restrictions apply as documented in [AWS IoT
  Limits](../../../general/latest/gr/iot-core.md#limits_iot "../../../general/latest/gr/iot-core.md#limits_iot").
- If a message is received with a Basic Ingest topic that specifies an inactive rule or
  a rule that doesn't exist, an error log is created in an Amazon CloudWatch log to help you with
  debugging. For more information, see [Rules engine log entries](cwl-format.md#rule-engine-logs "cwl-format.md#rule-engine-logs"). A `RuleNotFound` metric is indicated and
  you can create alarms on this metric. For more information, see Rule Metrics in [Rule metrics](metrics_dimensions.md#rulemetrics "metrics_dimensions.md#rulemetrics").
- You can still publish with QoS 1 on Basic Ingest topics. You receive a PUBACK after
  the message is successfully delivered to the rules engine. Receiving a PUBACK doesn't mean
  that your rule actions were completed successfully. You can configure an error action to
  handle errors when an action is run. For more information, see [Error handling (error action)](rule-error-handling.md "rule-error-handling.md").
