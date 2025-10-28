# Perform firmware update over-the-air (FUOTA) for

LoRaWAN devices and multicast groups

Efficient firmware updates are crucial for maintaining the performance and security of IoT
devices in the field. AWS IoT Core for LoRaWAN supports multicast firmware over-the-air (FUOTA) update
feature that streamlines the process of updating firmware on multiple LoRaWAN devices
simultaneously.

Multicast FUOTA uses the multicast capabilities of the LoRaWAN protocol, and distributes
firmware updates to groups of devices without the need for individual unicast transmissions.
Using multicast FUOTA, you can significantly reduce the time and bandwidth required for
firmware updates, ensuring your IoT deployments remain up-to-date and secure.

You can perform firmware update over-the-air to update the device firmware of a single
LoRaWAN device or a group of devices. To update the device firmware or to send a downlink
payload to multiple devices, create a multicast group. Using multicast, a source can send
data to a single multicast group, which is then distributed to a group of recipient
devices.

AWS IoT Core for LoRaWAN's support for FUOTA and multicast groups is based on the [LoRa Alliance's](https://lora-alliance.org/about-lorawan "https://lora-alliance.org/about-lorawan") following
specifications:

- LoRaWAN Remote Multicast Setup Specification v1.0.0
- LoRaWAN Fragmented Data Block Transportation Specification v1.0.0
- LoRaWAN Application Layer Clock Synchronization Specification v1.0.0

###### Note

AWS IoT Core for LoRaWAN automatically performs the clock synchronization according to the LoRa
Alliance specification. It uses the function `AppTimeReq` to reply the
server-side time to the devices that request it using ClockSync signaling.

The following topics show how to create multicast groups and perform FUOTA.

###### Topics

- [Prepare devices for multicast and
  FUOTA configuration](lorawan-prepare-devices-multicast.md "lorawan-prepare-devices-multicast.md")
- [Create multicast groups to send a downlink
  payload to multiple devices](lorawan-multicast-groups.md "lorawan-multicast-groups.md")
- [Firmware update over-the-air (FUOTA) for
  AWS IoT Core for LoRaWAN](lorawan-mc-fuota-overview.md "lorawan-mc-fuota-overview.md")
