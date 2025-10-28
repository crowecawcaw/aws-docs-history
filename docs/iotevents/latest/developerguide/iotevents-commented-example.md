End of support notice: On May 20, 2026, AWS will end support for
AWS IoT Events. After May 20, 2026, you will no longer be able to access the AWS IoT Events console or AWS IoT Events
resources. For more information, see [AWS IoT Events end of
support](iotevents-end-of-support.md "iotevents-end-of-support.md").

# A commented example: HVAC temperature control

with AWS IoT Events

Some of the following example JSON files have comments inline, which makes them invalid
JSON. Complete versions of these examples, without comments, are available at [Example: Using HVAC temperature control with AWS IoT Events](iotevents-examples-hvac.md "iotevents-examples-hvac.md").

This example implements a thermostat control model that gives you the ability to do the
following.

- Define just one detector model that can be used to monitor and control multiple areas.
  A detector instance is created for each area.
- Ingest temperature data from multiple sensors in each control area.
- Change the temperature set point for an area.
- Set operational parameters for each area and reset these parameters while the instance
  is in use.
- Dynamically add or delete sensors from an area.
- Specify a minimum runtime to protect heating and cooling units.
- Reject anomalous sensor readings.
- Define emergency set points that immediately engage heating or cooling if any one
  sensor reports a temperature above or below a given threshold.
- Report anomalous readings and temperature spikes.

###### Topics

- [Input definitions for detector models
  in AWS IoT Events](iotevents-commented-example-inputs.md "iotevents-commented-example-inputs.md")
- [Create an AWS IoT Events detector model
  definition](iotevents-commented-example-detector-model.md "iotevents-commented-example-detector-model.md")
- [Use BatchUpdateDetector
  to update an AWS IoT Events detector model](iotevents-commented-example-batch-update-detector.md "iotevents-commented-example-batch-update-detector.md")
- [Use BatchPutMessage for
  inputs in AWS IoT Events](iotevents-commented-example-input-usage-examples.md "iotevents-commented-example-input-usage-examples.md")
- [Ingest MQTT messages in
  AWS IoT Events](iotevents-commented-example-ingest-mqtt.md "iotevents-commented-example-ingest-mqtt.md")
- [Generate Amazon SNS messages in
  AWS IoT Events](iotevents-commented-example-generated-sns.md "iotevents-commented-example-generated-sns.md")
- [Configure the
  DescribeDetector API in AWS IoT Events](iotevents-commented-example-describe-detector.md "iotevents-commented-example-describe-detector.md")
- [Use the AWS IoT Core rules
  engine for AWS IoT Events](iotevents-commented-examples-iot-rules-examples.md "iotevents-commented-examples-iot-rules-examples.md")
