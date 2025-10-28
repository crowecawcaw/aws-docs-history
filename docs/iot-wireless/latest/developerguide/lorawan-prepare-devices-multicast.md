# Prepare devices for multicast and

FUOTA configuration

When you add your wireless device to AWS IoT Core for LoRaWAN, you can prepare your wireless
device for multicast setup and FUOTA configuration by using the console or the CLI. If
you're performing this configuration for the first time, we recommend that you use the
console. To manage your multicast group and add or remove a number of devices from your
group, we recommend using the CLI to manage a large number of resources.

## GenAppKey and FPorts

When you add your wireless device, before you can add your devices to multicast
groups or perform FUOTA, configure the following parameters. Before you configure
these parameters, make sure that your devices support FUOTA and multicast and your
wireless device specification is either `OTAA v1.1` or
`OTAAv1.0.x`.

- `GenAppKey`: For devices that support the LoRaWAN version 1.0.x
  and to use multicast groups, the `GenAppKey` is the
  device-specific root key from which the session keys for your multicast
  group are derived.

###### Note

For LoRaWAN devices that use the wireless specification `OTAA
 v1.1`, the `AppKey` is used for the same purpose as
the `GenAppKey`.

To set up the parameters to initiate the data transfer, AWS IoT Core for LoRaWAN
distributes session keys with the end devices. For more information about
LoRaWAN versions, see [LoRaWAN version](lorawan-manage-end-devices.md#lorawan-lorawan-version "lorawan-manage-end-devices.md#lorawan-lorawan-version").

###### Note

AWS IoT Core for LoRaWAN stores the `GenAppKey` information that you
provide in an encrypted format.

- `FPorts`: According to the LoRaWAN specifications for FUOTA and
  multicast groups, AWS IoT Core for LoRaWAN assigns the default values for the following
  fields of the `FPorts` parameter. If you have already assigned
  any of the following `FPort` values, then you can choose a
  different value that is available, from 1 to 223.
  - `Multicast`: 200

  This `FPort` value is used for multicast groups.
  - `FUOTA`: 201

  This `FPort` value is used for FUOTA.
  - `ClockSync`: 202

  This `FPort` value is used for the clock
  synchronization.

## Device profiles for multicast and

FUOTA

At the start of a multicast session, a class B or class C distribution window is
used to send the downlink message to the devices in your group. The devices that you
add for multicast and FUOTA must support class B or class C modes of operation.
Depending on the device class that your device supports, choose a device profile for
your device that has either or both class B or class C modes enabled.

For information about device profiles, see [Add profiles to AWS IoT Core for LoRaWAN](lorawan-define-profiles.md "lorawan-define-profiles.md").

## Prepare devices for

multicast and FUOTA by using the console

To specify the FPorts and GenAppKey parameters for multicast setup and FUOTA by
using the console:

1. Navigate to the [Devices hub of the
   AWS IoT console](https://console.aws.amazon.com/iot/home#/wireless/devices "https://console.aws.amazon.com/iot/home#/wireless/devices") and choose **Add wireless
   device**.
2. Choose the **Wireless device specification**. Your device
   must use OTAA for device activation. When you choose OTAA v1.0.x or OTAA
   v1.1, a **FUOTA configuration-Optional** section
   appears.
3. Enter the EUI (Extended Unique Identifier) parameters for your wireless
   device.
4. Expand the **FUOTA configuration-Optional** section and
   then choose **This device supports firmware updates over the air
   (FUOTA)**. You can now enter the **FPort**
   values for multicast, FUOTA, and clock sync. If you chose `OTAA
v1.0.x` for the wireless device specification, enter the
   **GenAppKey**.
5. Add your device to AWS IoT Core for LoRaWAN by choosing your profiles and a
   destination for routing messages. For the device profile linked to the
   device, make sure you select one or both **Supports Class
   B** or **Supports Class C** modes.

###### Note

To specify the FUOTA configuration parameters, you must use the [Devices hub of the
AWS IoT console](https://console.aws.amazon.com/iot/home#/wireless/devices "https://console.aws.amazon.com/iot/home#/wireless/devices"). These parameters don't appear if you onboard your
devices by using the **Intro** page of the AWS IoT
console.

For more information about the wireless device specification and onboarding your
device, see [Add your wireless device to
AWS IoT Core for LoRaWAN](lorawan-end-devices-add.md "lorawan-end-devices-add.md").

###### Note

You can specify these parameters only when you create the wireless device. You
can't change or specify parameters when you update an existing device.

## Prepare devices for

multicast and FUOTA by using the API

To use multicast groups or to perform FUOTA, configure these parameters by using
the [`CreateWirelessDevice`](../../2020-11-22/apireference/API_CreateWirelessDevice.md "../../2020-11-22/apireference/API_CreateWirelessDevice.md") API operation or the [`create-wireless-device`](../../../cli/latest/reference/iotwireless/create-wireless-device.md "../../../cli/latest/reference/iotwireless/create-wireless-device.md") CLI command. In
addition to specifying the application key and FPorts parameters, make sure that the
device profile that's linked to the device supports one or both class B or class C
modes.

You can provide an `input.json` file as input to the
`create-wireless-device` command.

```
aws iotwireless create-wireless-device \
    --cli-input-json file://input.json
```

where:

**Contents of input.json**

```
{
    "Description": "My LoRaWAN wireless device"
    "DestinationName": "IoTWirelessDestination"
    "LoRaWAN": {
        "DeviceProfileId": "ab0c23d3-b001-45ef-6a01-2bc3de4f5333",
        "ServiceProfileId": "fe98dc76-cd12-001e-2d34-5550432da100",
        "FPorts": {
            "ClockSync": 202,
            "Fuota": 201,
            "Multicast": 200
      },
        "OtaaV1_0_x": {
            "AppKey": "3f4ca100e2fc675ea123f4eb12c4a012",
            "AppEui": "b4c231a359bc2e3d",
            "GenAppKey": "01c3f004a2d6efffe32c4eda14bcd2b4"
        },
        "DevEui": "ac12efc654d23fc2"
    },
    "Name": "SampleIoTWirelessThing"
    "Type": LoRaWAN
}
```

For information about the CLI commands that you can use, see [AWS CLI
reference](../../../cli/latest/reference/iotwireless/index.md "../../../cli/latest/reference/iotwireless/index.md").

###### Note

After you specify the values of these parameters, you can't update them by
using the `UpdateWirelessDevice` API operation. Instead, you can
create a new
device
with the values for the parameters `GenAppKey` and
`FPorts`.

To get information about the values specified for these parameters, you can use
the [`GetWirelessDevice`](../../2020-11-22/apireference/API_GetWirelessDevice.md "../../2020-11-22/apireference/API_GetWirelessDevice.md") API operation or the [`get-wireless-device`](../../../cli/latest/reference/iotwireless/get-wireless-device.md "../../../cli/latest/reference/iotwireless/get-wireless-device.md") CLI
command.

## Next steps

After you've configured the parameters, you can create multicast groups and FUOTA
tasks to send downlink payload or update the firmware of your LoRaWAN
devices.

- For information about creating multicast groups, see [Create multicast groups and add
  devices to the group](lorawan-create-multicast-groups.md "lorawan-create-multicast-groups.md").
- For information about creating FUOTA tasks, see [Create FUOTA task and provide firmware
  image](lorawan-fuota-create-task.md "lorawan-fuota-create-task.md").
