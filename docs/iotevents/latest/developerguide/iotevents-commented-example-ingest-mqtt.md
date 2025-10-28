End of support notice: On May 20, 2026, AWS will end support for
AWS IoT Events. After May 20, 2026, you will no longer be able to access the AWS IoT Events console or AWS IoT Events
resources. For more information, see [AWS IoT Events end of
support](iotevents-end-of-support.md "iotevents-end-of-support.md").

# Ingest MQTT messages in

AWS IoT Events

If your sensor computing resources can't use the `"BatchPutMessage"` API, but
can send their data to the AWS IoT Core message broker using a lightweight MQTT client, you can
create an AWS IoT Core topic rule to redirect message data to an AWS IoT Events input. The following
is a definition of an AWS IoT Events topic rule that takes the `"areaId"` and
`"sensorId"` input fields from the MQTT topic, and the
`"sensorData.temperature"` field from the message payload `"temp"`
field, and ingests this data into our AWS IoT Events `"temperatureInput"`.

CLI command:

```

aws iot create-topic-rule --cli-input-json file://temperatureTopicRule.json
```

File: `seedSetDesiredTemp.json`

```
{
  "ruleName": "temperatureTopicRule",
  "topicRulePayload": {
    "sql": "SELECT topic(3) as areaId, topic(4) as sensorId, temp as sensorData.temperature FROM 'update/temperature/#'",
    "description": "Ingest temperature sensor messages into IoT Events",
    "actions": [
      {
        "iotEvents": {
          "inputName": "temperatureInput",
          "roleArn": "arn:aws:iam::123456789012:role/service-role/anotheRole"
        }
      }
    ],
    "ruleDisabled": false,
    "awsIotSqlVersion": "2016-03-23"
  }
}
```

Response: [none]

If the sensor sends a message on the topic `"update/temperature/Area51/03"`
with the following payload.

```
{ "temp": 24.5 }
```

This results in data being ingested into AWS IoT Events as if the following
`"BatchPutMessage"` API call had been made.

```

aws iotevents-data batch-put-message --cli-input-json file://spoofExample.json --cli-binary-format raw-in-base64-out
```

File: `spoofExample.json`

```
{
  "messages": [
    {
      "messageId": "54321",
      "inputName": "temperatureInput",
      "payload": "{\"sensorId\": \"03\", \"areaId\": \"Area51\", \"sensorData\": {\"temperature\": 24.5} }"
    }
  ]
}
```
