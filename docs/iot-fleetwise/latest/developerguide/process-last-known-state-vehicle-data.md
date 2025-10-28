# Process last known state vehicle

data using MQTT messaging

###### Important

Access to certain AWS IoT FleetWise features is currently gated. For more information, see [AWS Region and feature availability in AWS IoT FleetWise](fleetwise-regions.md "fleetwise-regions.md").

To receive updates from your vehicle and process its data, subscribe to the following
MQTT topic. For more information, see [MQTT
topics](../../../iot/latest/developerguide/iot-connect-devices.md "../../../iot/latest/developerguide/iot-connect-devices.md") in the _AWS IoT Core Developer Guide._

```
$aws/iotfleetwise/vehicles/`$vehicle_name`/last_known_state/`$state_template_name`/data
```

Last known state signal update messages might be received out of order, as MQTT doesn't
guarantee ordering. Any clients which use MQTT to receive and process vehicle data must
handle this. Last known state signal update messages follow the MQTT 5 messaging protocol.

The message header for each MQTT message has the following user properties:

- **vehicleName** – A unique identifier of the
  [vehicles](vehicles.md "vehicles.md").
- **stateTemplateName** – A unique identifier of the last
  known state [state template](state-templates.md "state-templates.md").
  In addition, you can specify [vehicle attributes](signal-catalogs.md "signal-catalogs.md")
  to be included in the MQTT message header by specifying the `metadataExtraDimensions`
  request parameter while updating or creating a state template. (See [State Templates](state-templates.md "state-templates.md").)

The user properties in the MQTT message header are useful for routing messages to different
destinations without inspecting the payload.

The MQTT message payload contains data collected from the vehicles. You can specify
vehicle attributes to be included in the MQTT message payload by specifying the
`extraDimensions` request parameter while creating or updating a state template
(see [Create an AWS IoT FleetWise state template](state-templates.md "state-templates.md")). The extra dimensions
enrich the data collected from the vehicles by associating extra dimensions to them.

The MQTT message payload is protocol buffers (Protobuf) encoded, and the MQTT message header contains a content
type indicator defined as application/octet-stream. The Protobuf encoding schema is as
follows:

```
// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

syntax = "proto3";

option java_package = "com.amazonaws.iot.autobahn.schemas.lastknownstate";
package Aws.IoTFleetWise.Schemas.CustomerMessage;

message LastKnownState {

  /*
   * The absolute timestamp in milliseconds since Unix Epoch of when the event was triggered in vehicle.
   */
  uint64 time_ms = 1;

  /*
   * This field is deprecated, use signals instead
   */
  repeated Signal signal = 2 [ deprecated = true ];

  repeated Signal signals = 3;

  repeated ExtraDimension extra_dimensions = 4;
}

message Signal {

  /*
   * The Fully Qualified Name of the signal is the path to the signal plus the signal's name.
   * For example, Vehicle.Chassis.SteeringWheel.HandsOff.HandsOffSteeringState
   * The fully qualified name can have up to 150 characters. Valid characters: a-z, A-Z, 0-9, : (colon), and _ (underscore).
   */
  string name = 1;

  /*
   * The FWE reported signal value can be one of the following data types.
   */
  oneof SignalValue {
    double double_value = 2;

    bool boolean_value = 3;

    sint32 int8_value = 4;

    uint32 uint8_value = 5;

    sint32 int16_value = 6;

    uint32 uint16_value = 7;

    sint32 int32_value = 8;

    uint32 uint32_value = 9;

    sint64 int64_value = 10;

    uint64 uint64_value = 11;

    float float_value = 12;
    /*
     * An UTF-8 encoded or 7-bit ASCII string
     */
    string string_value = 13;
  }
}

message ExtraDimension {
  /*
   * The Fully Qualified Name of the attribute is the path to the attribute plus the attribute's name.
   * For example, Vehicle.Model.Color
   * The fully qualified name can have up to 150 characters. Valid characters: a-z, A-Z, 0-9, : (colon), and _ (underscore).
   */
  string name = 1;

  oneof ExtraDimensionValue {
    /*
     * An UTF-8 encoded or 7-bit ASCII string
     */
    string string_value = 2;
  }
}
```

Where:

- `time_ms`:

The absolute timestamp (in milliseconds since the Unix Epoch)
of when the event was triggered in the vehicle. The Edge Agent software
uses on the vehicle's clock for this timestamp.

- `signal`:

An array of `Signal`s that contain the signal information: `name`
(string) and `signalValue` which supports the following data types -
`double`, `bool`, `int8`, `uint8`, `int16`,
`uint16`, `int32`, `uint32`, `int64`, `uint64`,
`float`, `string`.

- `extra_dimensions`:

An array of `ExtraDimensions` that contain vehicle attribute information:
`name` (string) and `extraDimensionValue` which currently only
supports the `string` data type.
