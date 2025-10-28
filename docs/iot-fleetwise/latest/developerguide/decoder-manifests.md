# Manage AWS IoT FleetWise decoder manifests

###### Important

Access to certain AWS IoT FleetWise features is currently gated. For more information, see [AWS Region and feature availability in AWS IoT FleetWise](fleetwise-regions.md "fleetwise-regions.md").

Decoder manifests contain decoding information that AWS IoT FleetWise uses to transform
vehicle data (binary data) into human-readable values and to prepare your data for data
analyses. Network interface and signal decoders are the core components that you work
with to configure decoder manifests.

**Network interface**

Contains information about the protocol that the in-vehicle network uses.
AWS IoT FleetWise supports the following protocols.

**Controller Area Network (CAN bus)**

A protocol that defines how data is communicated between
electronic control units (ECUs). ECUs can be the engine control
unit, airbags, or the audio system.

**On-board diagnostic (OBD) II**

A further developed protocol that defines how self-diagnostic data
is communicated between ECUs. It provides a number of standard
diagnostic trouble codes (DTCs) that help identify what is wrong
with your vehicle.

**Vehicle middleware**

The vehicle middleware defined as a type of network interface. Examples
of vehicle middleware include Robot Operating System (ROS 2) and Scalable
service-Oriented MiddlewarE over IP (SOME/IP).

###### Note

AWS IoT FleetWise supports ROS 2 middleware for vision system data.

**Custom interfaces**

You can also use your own interface to decode signals at the Edge. This
can save you time since you don't need to create decoding rules in the
cloud.

**Signal decoder**

Provides detailed decoding information for a specific signal. Every signal
specified in the vehicle model must be paired with a signal decoder. If the
decoder manifest contains CAN network interfaces, it must contain CAN decoder
signals. If the decoder manifest contains OBD network interfaces, it must
contain OBD signal decoders.

The decoder manifest must contain message signal decoders if it also contains
vehicle middleware interfaces. Or, if the decoder manifest contains custom decoding
interfaces, it must also contain custom decoding signals.

Each decoder manifest must be associated with a vehicle model. AWS IoT FleetWise uses the
associated decoder manifest to decode data from vehicles created based on the vehicle
model.

Each decoder manifest has a status field that contains the state of the decoder
manifest. The state can be one of the following values:

- `ACTIVE` – The decoder manifest is active.
- `DRAFT` – The configuration of the decoder manifest isn't
  saved.
- `VALIDATING` – The decoder manifest is under validation for
  its eligibility. This only applies to decoder manifests that contain at least
  one vision system data signal.
- `INVALID` – The decoder manifest failed validation and can't
  be activated yet. This only applies to decoder manifests that contain at least
  one vision system data signal. You can use the ListDecoderManifests and GetDecoderManifest
  APIs to check the reason for a failed validation.

###### Important

- If you use the AWS IoT FleetWise console to create a decoder manifest, AWS IoT FleetWise
  automatically activates the decoder manifest for you.
- If you use the `CreateDecoderManifest` API operation to create
  a decoder manifest, the decoder manifest stays in the `DRAFT`
  state.
- You can't create vehicles from vehicle models that are associated with a
  `DRAFT` decoder manifest. Use the
  `UpdateDecoderManifest` API operation to change the decoder
  manifest to the `ACTIVE` state.
- You can't edit decoder manifests that are in the `ACTIVE`
  state.

###### Topics

- [Configure AWS IoT FleetWise
  network interfaces and decoder signals](configure-network-interfaces-decoder-signals.md "configure-network-interfaces-decoder-signals.md")
- [Create an AWS IoT FleetWise decoder manifest](create-decoder-manifest.md "create-decoder-manifest.md")
- [Update an AWS IoT FleetWise decoder manifest](update-decoder-manifest.md "update-decoder-manifest.md")
- [Delete an AWS IoT FleetWise decoder manifest](delete-decoder-manifest.md "delete-decoder-manifest.md")
- [Get AWS IoT FleetWise decoder manifest
  information](get-decoder-manifest-information.md "get-decoder-manifest-information.md")
