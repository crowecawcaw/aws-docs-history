End of support notice: On May 20, 2026, AWS will end support for
AWS IoT Events. After May 20, 2026, you will no longer be able to access the AWS IoT Events console or AWS IoT Events
resources. For more information, see [AWS IoT Events end of
support](iotevents-end-of-support.md "iotevents-end-of-support.md").

# Input definitions for detector models

in AWS IoT Events

We want to create one detector model that we can use to monitor and control the
temperature in several different areas. Each area can have several sensors that report the
temperature. We assume each area is served by one heating unit and one cooling unit that can
be turned on or off to control the temperature in the area. Each area is controlled by one
detector instance.

Because the different areas we monitor and control might have different characteristics
that demand different control parameters, we define the `'seedTemperatureInput'`
to provide those parameters for each area. When we send one of these input messages to
AWS IoT Events, a new detector model instance is created that has the parameters we want to use in
that area. Here's the definition of that input.

CLI command:

```

aws iotevents create-input --cli-input-json file://seedInput.json
```

File: `seedInput.json`

```
{
  "inputName": "seedTemperatureInput",
  "inputDescription": "Temperature seed values.",
  "inputDefinition": {
    "attributes": [
      { "jsonPath": "areaId" },
      { "jsonPath": "desiredTemperature" },
      { "jsonPath": "allowedError" },
      { "jsonPath": "rangeHigh" },
      { "jsonPath": "rangeLow" },
      { "jsonPath": "anomalousHigh" },
      { "jsonPath": "anomalousLow" },
      { "jsonPath": "sensorCount" },
      { "jsonPath": "noDelay" }
    ]
  }
}
```

Response:

```
{
    "inputConfiguration": {
        "status": "ACTIVE",
        "inputArn": "arn:aws:iotevents:us-west-2:123456789012:input/seedTemperatureInput",
        "lastUpdateTime": 1557519620.736,
        "creationTime": 1557519620.736,
        "inputName": "seedTemperatureInput",
        "inputDescription": "Temperature seed values."
    }
}
```

###### Notes

- A new detector instance is created for each unique `'areaId'` received in
  any message. See the `'key'` field in the `'areaDetectorModel'`
  definition.
- The average temperature can vary from the `'desiredTemperature'` by the
  `'allowedError'` before the heating or cooling units are activated for the
  area.
- If any sensor reports a temperature above the `'rangeHigh'`, the detector
  reports a spike and immediately starts the cooling unit.
- If any sensor reports a temperature below the `'rangeLow'`, the detector
  reports a spike and immediately starts the heating unit.
- If any sensor reports a temperature above the `'anomalousHigh'` or below
  the `'anomalousLow'`, the detector reports an anomalous sensor reading, but
  ignores the reported temperature reading.
- The `'sensorCount'` tells the detector how many sensors are reporting for
  the area. The detector calculates the average temperature in the area by giving the
  appropriate weight factor to each temperature reading it receives. Because of this, the
  detector won't have to keep track of what each sensor reports, and the number of sensors
  can be changed dynamically, as needed. However, if an individual sensor goes offline,
  the detector won't know this or make allowances for it. We recommend that you create
  another detector model specifically for monitoring the connection status of each sensor.
  Having two complementary detector models simplifies the design of both.
- The `'noDelay'` value can be `true` or `false`.
  After a heating or cooling unit is turned on, it should remain on for a certain minimum
  time to protect the integrity of the unit and lengthen its operating life. If
  `'noDelay'` is set to `false`, the detector instance enforces a
  delay before it turns off the cooling and heating units, to ensure that they are run for
  the minimum time. The number of seconds of delay has been hardcoded in the detector
  model definition because we are unable to use a variable value to set a timer.
  The `'temperatureInput'` is used to transmit sensor data to a detector
  instance.

CLI command:

```

aws iotevents create-input --cli-input-json file://temperatureInput.json
```

File: `temperatureInput.json`

```
{
  "inputName": "temperatureInput",
  "inputDescription": "Temperature sensor unit data.",
  "inputDefinition": {
    "attributes": [
      { "jsonPath": "sensorId" },
      { "jsonPath": "areaId" },
      { "jsonPath": "sensorData.temperature" }
    ]
  }
}
```

Response:

```
{
    "inputConfiguration": {
        "status": "ACTIVE",
        "inputArn": "arn:aws:iotevents:us-west-2:123456789012:input/temperatureInput",
        "lastUpdateTime": 1557519707.399,
        "creationTime": 1557519707.399,
        "inputName": "temperatureInput",
        "inputDescription": "Temperature sensor unit data."
    }
}
```

###### Notes

- The `'sensorId'` isn't used by an example detector instance to control or
  monitor a sensor directly. It's automatically passed into notifications sent by the
  detector instance. From there, it can be used to identify the sensors that are failing
  (for example, a sensor that regularly sends anomalous readings might be about to fail),
  or that have gone offline (when it's used as an input to an additional detector model
  that monitors the device's heartbeat). The `'sensorId'` can also help
  identify warm or cold zones in an area if its readings regularly differ from the
  average.
- The `'areaId'` is used to route the sensor's data to the appropriate
  detector instance. A detector instance is created for each unique `'areaId'`
  received in any message. See the `'key'` field in the
  `'areaDetectorModel'` definition.
