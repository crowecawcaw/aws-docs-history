# Add devices and multicast groups and

schedule FUOTA session

After you've created a FUOTA task, you can add devices to your task for which you
want to update the firmware. After your devices have been added successfully to the
FUOTA task, you can schedule a FUOTA session to update the device firmware.

- If you have only a small number of devices, you can add those devices
  directly to your FUOTA task.
- If you have a large number of devices that you want to update firmware
  for, you can add these devices to your multicast groups, and then add the
  multicast groups to your FUOTA task. For information about creating and
  using multicast groups, see [Create multicast groups to send a downlink
  payload to multiple devices](lorawan-multicast-groups.md "lorawan-multicast-groups.md").

###### Note

You can add either individual devices or multicast groups to the FUOTA task.
You can't add both devices and multicast groups to the task.

After you've added your devices or multicast groups, you can start a firmware
update session. AWS IoT Core for LoRaWAN collects the firmware image, fragments the images, and
then stores the fragments in an encrypted format. Your end devices collect the
fragments and apply the new firmware image. The time that it takes for the firmware
update depends on the image size and how the images were fragmented. After the
firmware update is complete, the encrypted fragments of the firmware image stored by
AWS IoT Core for LoRaWAN is deleted. You can still find the firmware image in the S3
bucket.

###### Note

If you use the AWS CLI to start a FUOTA session, you can configure the downlink
frequency and the `PingSlotPeriod` for Class B devices. First, you
must run the [`StartMulticastGroupSession`](../../2020-11-22/apireference/API_StartMulticastGroupSession.md "../../2020-11-22/apireference/API_StartMulticastGroupSession.md") API command with the
desired values for these parameters. Then, when you run the
`StartFuotaTask` API, it will use the appropriate values once the
multicast session has started. For more information, see [(Optional)
Configure downlink frequency of multicast group before starting FUOTA
session](#lorawan-fuota-devices-api-downlinkfreq "#lorawan-fuota-devices-api-downlinkfreq").

## Prerequisites

Before you can add devices or multicast groups to your FUOTA task, do the
following.

- You must have already created the FUOTA task and provided your
  firmware image. For more information, see [Create FUOTA task and provide firmware
  image](lorawan-fuota-create-task.md "lorawan-fuota-create-task.md").
- Provision the wireless devices that you want to update the device
  firmware for. For more information about onboarding your device, see
  [Onboard your devices to
  AWS IoT Core for LoRaWAN](lorawan-onboard-end-devices.md "lorawan-onboard-end-devices.md").
- To update the firmware of multiple devices, you can add them to a
  multicast group. For more information, see [Create multicast groups to send a downlink
  payload to multiple devices](lorawan-multicast-groups.md "lorawan-multicast-groups.md").
- When you onboard the devices to AWS IoT Core for LoRaWAN, specify the FUOTA
  configuration parameter `FPorts`. If you're using a LoRaWAN
  v1.0.x device, you must also specify the `GenAppKey`. For
  more information about the FUOTA configuration parameters, see [Prepare devices for multicast and
  FUOTA configuration](lorawan-prepare-devices-multicast.md "lorawan-prepare-devices-multicast.md").

## Add devices to a FUOTA task and

schedule a FUOTA session by using the console

To add devices or multicast groups and schedule a FUOTA session by using the
console, go to the [FUOTA
tasks](https://console.aws.amazon.com/iot/home#/wireless/fuotaTasks "https://console.aws.amazon.com/iot/home#/wireless/fuotaTasks") tab of the console. Then, choose the FUOTA task that you want
to add devices to and perform the firmware update.

###### Add devices and multicast groups

1. You can add either individual devices or multicast groups to your
   FUOTA task. However, you can't add both individual devices and multicast
   groups to the same FUOTA task. To add devices using the by console, do
   the following.
   1. In the **FUOTA task details**, choose
      **Add device**.
   2. Choose the frequency band or **RFRegion** for
      the devices you add to the task. This value must match the
      **RFRegion** that you chose for the FUOTA
      task.
   3. Choose whether you want to add individual devices or multicast
      groups to the task.
      - To add individual devices, choose **Add
        individual devices** and enter the device
        ID of each device that you want to add to your FUOTA
        task.
      - To add multicast groups, choose **Add
        multicast groups** and add your multicast
        groups to the task. You can filter the multicast groups
        you want to add to the task by using the device profile
        or tags. When you filter by device profile, you can
        choose multicast groups that with devices that have a
        profile with **Supports Class B** or
        **Supports Class C**
        enabled.

2. ###### Schedule FUOTA session

After your devices or multicast groups have been added successfully,
you can schedule a FUOTA session. To schedule a session, do the
following.

    1. Choose the FUOTA task for which you want to update the device
     firmware and then choose **Schedule FUOTA
     session**.
    2. Specify a **Start date** and **Start
     time** for your FUOTA session. Make sure that the
     start time is 30 minutes or later from the current time.

## Add devices to a FUOTA task and

schedule a FUOTA session by using the API

You can use the AWS IoT Wireless API or the CLI to add your wireless devices
or multicast groups to your FUOTA task. You can then schedule a FUOTA
session.

###### Topics

- [(Optional)
  Configure downlink frequency of multicast group before starting FUOTA
  session](#lorawan-fuota-devices-api-downlinkfreq "#lorawan-fuota-devices-api-downlinkfreq")
- [Add devices and
  multicast groups to FUOTA task](#lorawan-fuota-devices-api-adddevices "#lorawan-fuota-devices-api-adddevices")
- [Schedule FUOTA
  session](#lorawan-fuota-devices-api-schedule "#lorawan-fuota-devices-api-schedule")

### (Optional)

Configure downlink frequency of multicast group before starting FUOTA
session

By default, when you start a FUOTA session, it will automatically start a
multicast session. If you haven't already started a multicast session, the
FUOTA session will use the default values for the downlink frequency and the
`PingSlotPeriod` parameter for class B devices.

To configure the downlink frequency and `PingSlotPeriod`
parameter, you can start a multicast session by specifying the values that
you want to use for these parameters. To start a multicast session, you can
use the [`StartMulticastGroupSession`](../../2020-11-22/apireference/API_StartMulticastGroupSession.md "../../2020-11-22/apireference/API_StartMulticastGroupSession.md") API operation or
the [`start-multicast-group-session`](../../../cli/latest/reference/iotwireless/start-multicast-group-session.md "../../../cli/latest/reference/iotwireless/start-multicast-group-session.md") CLI command. For
information about using this API, see [Schedule a downlink message by
using the API](lorawan-multicast-schedule-downlink.md#lorawan-multicast-downlink-api "lorawan-multicast-schedule-downlink.md#lorawan-multicast-downlink-api").

After you have started the multicast session, when you start a FUOTA task,
the task will automatically derive the downlink frequency and the
`PingSlotPeriod` parameter values that you specified when
using the API. In addition:

- The data rate for the FUOTA transfer is determined based on the
  fragment size by FUOTA.
- The session timeout for the multicast group is calculated when
  starting the FUOTA task. If a multicast session has already started,
  then the session is restarted with a new timeout. The session
  timeout for the FUOTA task is calculated based on the data rate and
  the number of fragments to be sent. You can start the multicast
  group session with any session time out. If this timeout is used for
  the FUOTA task, the session timeout will be automatically
  updated.

For information about starting a FUOTA task, see [Schedule FUOTA
session](#lorawan-fuota-devices-api-schedule "#lorawan-fuota-devices-api-schedule").

### Add devices and

multicast groups to FUOTA task

You can associate either wireless devices or multicast groups with your
FUOTA task.

- To associate individual devices to your FUOTA task, use the [`AssociateWirelessDeviceWithFuotaTask`](../../2020-11-22/apireference/API_AssociateWirelessDeviceWithFuotaTask.md "../../2020-11-22/apireference/API_AssociateWirelessDeviceWithFuotaTask.md")
  API operation or the [`associate-wireless-device-with-fuota-task`](../../../cli/latest/reference/iotwireless/associate-wireless-device-with-fuota-task.md "../../../cli/latest/reference/iotwireless/associate-wireless-device-with-fuota-task.md")
  CLI command, and provide the `WirelessDeviceID` as
  input.

```
aws iotwireless associate-wireless-device-with-fuota-task \
    --id `"01a23cde-5678-4a5b-ab1d-33456808ecb2"`
    --wireless-device-id `"ab0c23d3-b001-45ef-6a01-2bc3de4f5333"`
```

- To associate multicast groups to your FUOTA task, use the [`AssociateMulticastGroupWithFuotaTask`](../../2020-11-22/apireference/API_AssociateMulticastGroupWithFuotaTask.md "../../2020-11-22/apireference/API_AssociateMulticastGroupWithFuotaTask.md")
  API operation or the [`associate-multicast-group-with-fuota-task`](../../../cli/latest/reference/iotwireless/associate-multicast-group-with-fuota-task.md "../../../cli/latest/reference/iotwireless/associate-multicast-group-with-fuota-task.md")
  CLI command, and provide the `MulticastGroupID` as
  input.

```
aws iotwireless associate-multicast-group-with-FUOTA-task \
    --id `"01a23cde-5678-4a5b-ab1d-33456808ecb2"`
    --multicast-group-id `"ab0c23d3-b001-45ef-6a01-2bc3de4f5333"`
```

After you've associated your wireless devices or multicast group to your
FUOTA task, use the following API operations or CLI commands to list your
devices or multicast groups or to disassociate them from your task.

- [`DisassociateWirelessDeviceFromFuotaTask`](../../2020-11-22/apireference/API_DisassociateWirelessDeviceFromFuotaTask.md "../../2020-11-22/apireference/API_DisassociateWirelessDeviceFromFuotaTask.md")
  or [`disassociate-wireless-device-from-fuota-task`](../../../cli/latest/reference/iotwireless/disassociate-wireless-device-from-fuota-task.md "../../../cli/latest/reference/iotwireless/disassociate-wireless-device-from-fuota-task.md")
- [`DisassociateMulticastGroupFromFuotaTask`](../../2020-11-22/apireference/API_DisassociateMulticastGroupFromFuotaTask.md "../../2020-11-22/apireference/API_DisassociateMulticastGroupFromFuotaTask.md")
  or [`disassociate-multicast-group-from-fuota-task`](../../../cli/latest/reference/iotwireless/disassociate-multicast-group-from-fuota-task.md "../../../cli/latest/reference/iotwireless/disassociate-multicast-group-from-fuota-task.md")
- [`ListWirelessDevices`](../../2020-11-22/apireference/API_ListWirelessDevices.md "../../2020-11-22/apireference/API_ListWirelessDevices.md") or [`list-wireless-devices`](../../../cli/latest/reference/iotwireless/delete-multicast-group.md "../../../cli/latest/reference/iotwireless/delete-multicast-group.md")
- [`ListMulticastGroups`](../../2020-11-22/apireference/API_ListMulticastGroups.md "../../2020-11-22/apireference/API_ListMulticastGroups.md") or [`list-multicast-groups-by-fuota-task`](../../../cli/latest/reference/iotwireless/list-multicast-groups.md "../../../cli/latest/reference/iotwireless/list-multicast-groups.md")

###### Note

The API:

    + `ListWirelessDevices` can list wireless
     devices in general, and devices associated with a
     multicast group, when `MulticastGroupID` is
     used as the filter. The API lists wireless devices
     associated with a FUOTA task when
     `FuotaTaskID` is used as the
     filter.
    + `ListMulticastGroups` can list multicast
     groups in general and multicast groups associated with a
     FUOTA task when `FuotaTaskID` is used as the
     filter.

### Schedule FUOTA

session

After your devices or multicast groups have been successfully added to the
FUOTA task, you can start a FUOTA session to update the device firmware. The
start time must be 30 minutes or later from the current time. To schedule a
FUOTA session by using the API or CLI, use the [`StartFuotaTask`](../../2020-11-22/apireference/API_StartFuotaTask.md "../../2020-11-22/apireference/API_StartFuotaTask.md") API operation or the [`start-fuota-task`](../../../cli/latest/reference/iotwireless/start-fuota-task.md "../../../cli/latest/reference/iotwireless/start-fuota-task.md") CLI
command.

```
aws iotwireless start-fuota-task --id `"01a23cde-5678-4a5b-ab1d-33456808ecb2"`
```

After you've started a FUOTA session, You can no longer add devices or
multicast groups to the task. You can get information about the status of
your FUOTA session by using the [`GetFuotaTask`](../../2020-11-22/apireference/API_GettFuotaTask.md "../../2020-11-22/apireference/API_GettFuotaTask.md") API operation or the [`get-fuota-task`](../../../cli/latest/reference/iotwireless/get-fuota-task.md "../../../cli/latest/reference/iotwireless/get-fuota-task.md") CLI
command.
