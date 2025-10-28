# Configure AWS IoT FleetWise

network interfaces and decoder signals

###### Important

Access to certain AWS IoT FleetWise features is currently gated. For more information, see [AWS Region and feature availability in AWS IoT FleetWise](fleetwise-regions.md "fleetwise-regions.md").

Every decoder manifest has at least a network interface and signal decoders paired
with signals specified in the associated vehicle model.

If the decoder manifest contains CAN network interfaces, it must contain CAN
signal decoders. If the decoder manifest contains OBD network interfaces, it must
contain OBD signal decoders.

###### Topics

- [Configure network
  interfaces](#configure-network-interfaces "#configure-network-interfaces")
- [Configure signal decoders](#configure-decoder-signals "#configure-decoder-signals")

## Configure network

interfaces

To configure a CAN network interface, specify the following
information.

- `name` – The CAN interface's name.

The interface name must be unique and can have 1–100
characters.

- (Optional) `protocolName` – The protocol's
  name.

Valid values: `CAN-FD` and `CAN`

- (Optional) `protocolVersion` – AWS IoT FleetWise currently
  supports CAN-FD and CAN 2.0b.

Valid values: `1.0` and `2.0b`

To configure an OBD network interface, specify the following
information.

- `name` – The OBD interface's name.

The interface name must be unique and can have 1–100
characters.

- `requestMessageId` – The ID of the message that is
  requesting data.
- (Optional) `dtcRequestIntervalSeconds` – How often
  to request diagnostic trouble codes (DTCs) from the vehicle in seconds.
  For example, if the specified value is 120, the Edge Agent software collects
  stored DTCs once every 2 minutes.
- (Optional) `hasTransmissionEcu` – Whether the
  vehicle has a transmission control module (TCM).

Valid values: `true` and `false`

- (Optional) `obdStandard` – The OBD standard that
  AWS IoT FleetWise supports. AWS IoT FleetWise currently supports the World Wide
  Harmonization On-Board Diagnostics (WWH-OBD) ISO15765-4 standard.
- (Optional) `pidRequestIntervalSeconds` – How often
  to request OBD II PIDs from the vehicle. For example, if the specified
  value is 120, the Edge Agent software collects OBD II PIDs once every 2
  minutes.
- (Optional) `useExtendedIds` – Whether to use
  extended IDs in the message.

Valid values: `true` and `false`

To configure a vehicle middleware network interface, specify the following
information.

- `name` – The vehicle middleware interface's name.

The interface name must be unique and can have 1–100
characters.

- `protocolName` – The protocol's name.

Valid values: `ROS_2`

To configure a custom decoding interface, specify the following
information.

- `name` – The name of your decoder that you use to decode signals at the Edge.

The decoder interface name can have 1–100 characters.

## Configure signal decoders

To configure a CAN signal decoder, specify the following information.

- `factor` – The multiplier used to decode the
  message.
- `isBigEndian` – Whether the byte ordering of the
  message is big-endian. If it's big-endian, the most significant value in
  the sequence is stored first, at the lowest storage address.
- `isSigned` – Whether the message is signed. If it's
  signed, the message can represent both positive and negative
  numbers.
- `length` – The length of the message in
  bits.
- `messageId` – The ID of the message.
- `offset` – The offset used to calculate the signal
  value. Combined with factor, the calculation is `value = raw_value
- factor + offset`.
- `startBit` – Indicates the location of the first bit
  of the message.
- (Optional) `name` – The name of the signal.
- (Optional) `signalValueType` – The value type of the signal. Integer is the default value type.

To configure an OBD signal decoder, specify the following information.

- `byteLength` – The length of the message in
  bytes.
- `offset` – The offset used to calculate the signal
  value. Combined with scaling, the calculation is `value = raw_value
- scaling + offset`.
- `pid` – The diagnostic code used to request a
  message from a vehicle for this signal.
- `pidResponseLength` – The length of the requested
  message.
- `scaling` – The multiplier used to decode the
  message.
- `serviceMode` – The mode of operation (diagnostic
  service) in a message.
- `startByte` – Indicates the beginning of the
  message.
- (Optional) `bitMaskLength` – The number of bits that
  are masked in a message.
- (Optional) `bitRightShift` – The number of positions
  shifted to the right.
- (Optional) `isSigned` – Whether the message is signed. If it's signed, the message can represent both positive and negative numbers. The message is not signed by default (`false`).
- (Optional) `signalValueType` – The value type of the signal. Integer is the default value type.

To configure a message signal decoder, specify the following
information.

- `topicName` – The topic name for the message signal.
  It corresponds to topics in ROS 2. For more information about the
  structured message object, see [StructuredMessage](../APIReference/API_StructuredMessage.md "../APIReference/API_StructuredMessage.md").
- `structuredMessage` – The structured message for the
  message signal. It can be defined with either a
  primitiveMessageDefinition, structuredMessageListDefinition, or
  structuredMessageDefinition recursively.

To configure a custom decoding signal, specify the following information.

- (Optional) `id` – The ID of the signal that you decode
  yourself using your decoder interface. The signal ID can have 1–150
  characters. If not specified, the `id` defaults to the
  `fullyQualifiedName` of the signal.
