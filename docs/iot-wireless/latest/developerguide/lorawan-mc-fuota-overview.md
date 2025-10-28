# Firmware update over-the-air (FUOTA) for

AWS IoT Core for LoRaWAN

Use Firmware Updates Over-The-Air (FUOTA) to deploy firmware updates to AWS IoT Core for LoRaWAN
devices.

Using FUOTA, you can send firmware updates to individual devices or to a group of
devices. You can also send firmware updates to multiple devices by creating a multicast
group. First add your devices to the multicast group, and then send your firmware update
image to all those devices. We recommend that you digitally sign the firmware images so
that devices receiving the images can verify that they're coming from the right
source.

With AWS IoT Core for LoRaWAN's FUOTA, you can:

- Deploy new firmware images or delta images to a single device or a group of
  devices.
- Verify the authenticity and integrity of new firmware after it's deployed to
  devices.
- Monitor the progress of a deployment and debug issues in case of a failed
  deployment.
  AWS IoT Core for LoRaWAN's support for FUOTA and multicast groups is based on the [LoRa Alliance's](https://lora-alliance.org/about-lorawan "https://lora-alliance.org/about-lorawan") following
  specifications:

- LoRaWAN Remote Multicast Setup Specification, TS005-1.0.0
- LoRaWAN Fragmented Data Block Transportation Specification, TS004-1.0.0
- LoRaWAN Application Layer Clock Synchronization Specification,
  TS003-1.0.0

###### Note

AWS IoT Core for LoRaWAN automatically performs the clock synchronization according to the
LoRa Alliance specification. It uses the function `AppTimeReq` to reply
the server-side time to the devices that request it using ClockSync
signaling.

The following video describes how AWS IoT Core for LoRaWAN FUOTA tasks can be created and walks
you through the process of adding devices to the task and schedule a FUOTA task.

###### The following topics show how to perform FUOTA.

- [FUOTA process overview](lorawan-fuota-mc-process.md "lorawan-fuota-mc-process.md")
- [Create FUOTA task and provide firmware
  image](lorawan-fuota-create-task.md "lorawan-fuota-create-task.md")
- [Add devices and multicast groups and
  schedule FUOTA session](lorawan-fuota-add-devices.md "lorawan-fuota-add-devices.md")
- [Monitor and troubleshoot your FUOTA task and
  devices](lorawan-fuota-status.md "lorawan-fuota-status.md")
