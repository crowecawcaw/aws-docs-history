# MQTT message payload

The message payload that is sent in your MQTT messages isn't specified by AWS IoT,
unless it's for one of the [Reserved topics](reserved-topics.md "reserved-topics.md"). To accommodate your
application's needs, we recommend you define the message payload for your topics within
the constraints of the [AWS IoT Core Service Quotas for Protocols](../../../general/latest/gr/iot-core.md#iot-protocol-limits "../../../general/latest/gr/iot-core.md#iot-protocol-limits").

Using a JSON format for your message payload enables the AWS IoT rules engine to parse
your messages and apply SQL queries to it. If your application doesn't require the rules
engine to apply SQL queries to your message payloads, you can use any data format that
your application requires. For information about limitations and reserved characters in
a JSON document used in SQL queries, see [JSON extensions](iot-sql-json.md "iot-sql-json.md").

For more information about designing your MQTT topics and their corresponding message
payloads, see [Designing MQTT Topics for AWS IoT Core](../../../whitepapers/latest/designing-mqtt-topics-aws-iot-core/designing-mqtt-topics-aws-iot-core.md "../../../whitepapers/latest/designing-mqtt-topics-aws-iot-core/designing-mqtt-topics-aws-iot-core.md").

If a message size limit exceeds the service quotas, it will result in a
`CLIENT_ERROR` with reason `PAYLOAD_LIMIT_EXCEEDED` and
"Message payload exceeds size limit for message type." For more information about
message size limit, see [AWS IoT Core message
broker limits and quotas](../../../general/latest/gr/iot-core.md#message-broker-limits.html "../../../general/latest/gr/iot-core.md#message-broker-limits.html").
