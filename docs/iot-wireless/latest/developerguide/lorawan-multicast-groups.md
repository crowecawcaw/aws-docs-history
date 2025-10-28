# Create multicast groups to send a downlink

payload to multiple devices

To send a downlink payload to multiple devices, create a multicast group. Using
multicast, a source can send data to a single multicast address, which is then
distributed to an entire group of recipient devices.

Devices in a multicast group share the same multicast address, session keys, and frame
counter. By using the same session keys, devices in a multicast group can decrypt the
message when a downlink transmission is initiated. A multicast group only supports
downlink. It doesn't confirm whether the downlink payload has been received by the
devices.

With AWS IoT Core for LoRaWAN's multicast groups, you can:

- Filter your list of devices by using the device profile, RFRegion, or device
  class, and then add these devices to a multicast group.
- Schedule and send one or more downlink payload messages to devices in a
  multicast group, within a 48-hour distribution window.
- Have devices temporarily switch to Class B or class C mode at the start of
  your multicast session for receiving the downlink message.
- Monitor your multicast group setup and the state of its devices, and also
  troubleshoot any issues.
- Use Firmware Updates-Over-The-Air (FUOTA) to securely deploy firmware updates
  to devices in a multicast group.
  The following video describes how AWS IoT Core for LoRaWAN multicast groups can be created and
  walks you through the process of adding a device to the group and schedule a downlink
  message to the group.

The following shows how to create your multicast group and schedule a downlink
message.

###### Topics

- [Create multicast groups and add
  devices to the group](lorawan-create-multicast-groups.md "lorawan-create-multicast-groups.md")
- [Choose participating gateways to
  receive multicast downlink messages](lorawan-multicast-choose-gateways.md "lorawan-multicast-choose-gateways.md")
- [Monitor and troubleshoot your multicast
  groups](lorawan-multicast-status.md "lorawan-multicast-status.md")
- [Schedule a downlink message
  for your multicast group](lorawan-multicast-schedule-downlink.md "lorawan-multicast-schedule-downlink.md")
