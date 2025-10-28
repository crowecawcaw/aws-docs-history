End of support notice: On May 20, 2026, AWS will end support for
AWS IoT Events. After May 20, 2026, you will no longer be able to access the AWS IoT Events console or AWS IoT Events
resources. For more information, see [AWS IoT Events end of
support](iotevents-end-of-support.md "iotevents-end-of-support.md").

# Create an AWS IoT Events input to capture device data

When setting up inputs for AWS IoT Events, you can leverage the AWS CLI to define how your devices
communicate sensor data. For example, if your devices send JSON-formatted messages with
motor identifiers and sensor readings, you can capture this data by creating an input that
maps specific attributes from the messages, such as the pressure and the motor ID. The
process starts by defining an input in a JSON file, specifying the relevant data points, and
using the AWS CLI to register the input for AWS IoT Events. This enables AWS IoT to monitor and respond
to critical conditions based on real-time sensor data.

As an example, suppose your devices send messages with the following format.

```
{
  "motorid": "Fulton-A32",
  "sensorData": {
    "pressure": 23,
    "temperature": 47
  }
}
```

You can create an input to capture the `pressure` data and the
`motorid` (that identifies the specific device that sent the message) using the
following AWS CLI command.

```

aws iotevents create-input  --cli-input-json file://pressureInput.json
```

The file `pressureInput.json` contains the following.

```
{
  "inputName": "PressureInput",
  "inputDescription": "Pressure readings from a motor",
  "inputDefinition": {
    "attributes": [
      { "jsonPath": "sensorData.pressure" },
      { "jsonPath": "motorid" }
    ]
  }
}
```

When you create your own inputs, remember to first collect example messages as JSON
files from your devices or processes. You can use them to create an input from the console
or the CLI.
