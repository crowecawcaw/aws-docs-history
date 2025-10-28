End of support notice: On May 20, 2026, AWS will end support for
AWS IoT Events. After May 20, 2026, you will no longer be able to access the AWS IoT Events console or AWS IoT Events
resources. For more information, see [AWS IoT Events end of
support](iotevents-end-of-support.md "iotevents-end-of-support.md").

# Example: Using HVAC temperature control with AWS IoT Events

## Background story

This example implements a temperature control model (a thermostat) with these
features:

- One detector model you define that can monitor and control multiple areas. (A
  detector instance will be created for each area.)
- Each detector instance receives temperature data from multiple sensors placed in
  each control area.
- You can change the desired temperature (the set point) for each area at any
  time.
- You can define the operational parameters for each area and change these parameters
  at any time.
- You can add sensors to or delete sensors from an area at any time.
- You can enable a minimum run for time heating and cooling units to protect them from
  damage.
- The detectors will reject, and report, anomalous sensor readings.
- You can define emergency temperature set points. If any one sensor reports a
  temperature above or below the set points you have defined, heating or cooling units
  will be engaged immediately, and the detector will report that temperature spike.

This example demonstrates the following functional capabilities:

- Create event detector models.
- Create inputs.
- Ingest inputs into a detector model.
- Evaluate trigger conditions.
- Refer to state variables in conditions and set the values of variables depending on
  conditions.
- Refer to timers in conditions and set timers depending on conditions.
- Take actions that send Amazon SNS and MQTT messages.
