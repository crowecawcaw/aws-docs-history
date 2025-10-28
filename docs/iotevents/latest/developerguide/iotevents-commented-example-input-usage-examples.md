End of support notice: On May 20, 2026, AWS will end support for
AWS IoT Events. After May 20, 2026, you will no longer be able to access the AWS IoT Events console or AWS IoT Events
resources. For more information, see [AWS IoT Events end of
support](iotevents-end-of-support.md "iotevents-end-of-support.md").

# Use BatchPutMessage for

inputs in AWS IoT Events

###### Example 1

Use the `BatchPutMessage` operation to send a
`"seedTemperatureInput"` message that sets the operational parameters for a
given area under temperature control and monitoring. Any message received by AWS IoT Events that
has a new `"areaId"` causes a new detector instance to be created. But the new
detector instance won't change state to `"idle"` and begin monitoring the
temperature and controlling heating or cooling units until a
`"seedTemperatureInput"` message is received for the new area.

CLI command:

```

aws iotevents-data batch-put-message --cli-input-json file://seedExample.json --cli-binary-format raw-in-base64-out
```

File: `seedExample.json`

```
{
  "messages": [
    {
      "messageId": "00001",
      "inputName": "seedTemperatureInput",
      "payload": "{\"areaId\": \"Area51\", \"desiredTemperature\": 20.0, \"allowedError\": 0.7, \"rangeHigh\": 30.0, \"rangeLow\": 15.0, \"anomalousHigh\": 60.0, \"anomalousLow\": 0.0, \"sensorCount\": 10, \"noDelay\": false}"
    }
  ]
}
```

Response:

```
{
    "BatchPutMessageErrorEntries": []
}
```

2

Use the `BatchPutMessage` operation to send a
`"temperatureInput"` message to report temperature sensor data for a sensor
in a given control and monitoring area.

CLI command:

```

aws iotevents-data batch-put-message --cli-input-json file://temperatureExample.json --cli-binary-format raw-in-base64-out
```

File: `temperatureExample.json`

```
{
  "messages": [
    {
      "messageId": "00005",
      "inputName": "temperatureInput",
      "payload": "{\"sensorId\": \"05\", \"areaId\": \"Area51\", \"sensorData\": {\"temperature\": 23.12} }"
    }
  ]
}
```

Response:

```
{
    "BatchPutMessageErrorEntries": []
}
```

###### Example 3

Use the `BatchPutMessage` operation to send a
`"seedTemperatureInput"` message to change the value of the desired
temperature for a given area.

CLI command:

```

aws iotevents-data batch-put-message --cli-input-json file://seedSetDesiredTemp.json --cli-binary-format raw-in-base64-out
```

File: `seedSetDesiredTemp.json`

```
{
  "messages": [
    {
      "messageId": "00001",
      "inputName": "seedTemperatureInput",
      "payload": "{\"areaId\": \"Area51\", \"desiredTemperature\": 23.0}"
    }
  ]
}
```

Response:

```
{
    "BatchPutMessageErrorEntries": []
}
```
