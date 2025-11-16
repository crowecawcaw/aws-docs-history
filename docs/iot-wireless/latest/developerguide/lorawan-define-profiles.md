# Add profiles to AWS IoT Core for LoRaWAN

Device and service profiles can be defined to describe common device
configurations. These profiles describe configuration parameters that are shared by
devices to make it easier to add those devices. AWS IoT Core for LoRaWAN supports device
profiles and service profiles.

The configuration parameters and the values to enter into these profiles are
provided by the device's manufacturer.

## Add device profiles

Device profiles define the device capabilities and boot parameters that the
network server uses to set the LoRaWAN radio access service. It includes
selection of parameters such as LoRa frequency band, LoRa regional parameters
version, and MAC version of the device. To learn about the different frequency
bands, see [Consider selection of LoRa frequency
bands for your gateways and device connection](lorawan-rfregion-permissions.md#lorawan-frequency-bands "lorawan-rfregion-permissions.md#lorawan-frequency-bands").

### Add a device profile by

using the console

If you're adding a wireless device by using the console as described in
[Add your wireless device
specification to AWS IoT Core for LoRaWAN using the console](lorawan-end-devices-add.md#lorawan-end-device-spec-console "lorawan-end-devices-add.md#lorawan-end-device-spec-console"), after you've added
the wireless device specification, you can add your device profile.
Alternatively, you can also add wireless devices from the [Profiles](https://console.aws.amazon.com/iot/home#/wireless/profiles "https://console.aws.amazon.com/iot/home#/wireless/profiles") page of the AWS IoT console on the
**LoRaWAN** tab.

You can choose from default device profiles or create a new device
profile. We recommend that you use the default device profiles. If your
application requires you to create a device profile, provide a
**Device profile name**, select the **Frequency
band (RfRegion)** that you're using for the device and gateway,
and keep the other settings to the default values, unless specified
otherwise in the device documentation.

### Add a device profile by using

the API

If you're adding a wireless device by using the API, you must create your
device profile before creating the wireless device.

The following lists describe the API actions that perform the tasks
associated with adding, updating, or deleting a service profile.

###### AWS IoT Wireless API actions for service profiles

- [CreateDeviceProfile](../apireference/API_CreateDeviceProfile.md "../apireference/API_CreateDeviceProfile.md")
- [GetDeviceProfile](../apireference/API_GetDeviceProfile.md "../apireference/API_GetDeviceProfile.md")
- [ListDeviceProfiles](../apireference/API_ListDeviceProfiles.md "../apireference/API_ListDeviceProfiles.md")
- [DeleteDeviceProfile](../apireference/API_DeleteDeviceProfile.md "../apireference/API_DeleteDeviceProfile.md")

For the complete list of the actions and data types available to create
and manage AWS IoT Core for LoRaWAN resources, see the [AWS IoT Wireless API
reference](../apireference/welcome.md "../apireference/welcome.md").

###### How to use the AWS CLI to create a device profile

You can use the AWS CLI to create a device profile by using the [create-device-profile](../../../cli/latest/reference/iotwireless/create-device-profile.md "../../../cli/latest/reference/iotwireless/create-device-profile.md") command. The
following example creates a device profile.

```
aws iotwireless create-device-profile
```

Running this command automatically creates a device profile with an ID
that you can use when creating the wireless device. You can now create the
service profile using the following API and then create the wireless device
by using the device and service profiles.

```
{
    "Arn": "arn:aws:iotwireless:us-east-1:123456789012:DeviceProfile/12345678-a1b2-3c45-67d8-e90fa1b2c34d",
    "Id": "12345678-a1b2-3c45-67d8-e90fa1b2c34d"
}
```

For information about the CLIs that you can use, see [AWS CLI reference](../../../cli/latest/reference/iotwireless/index.md "../../../cli/latest/reference/iotwireless/index.md")

## Add service profiles

Service profiles describe the communication parameters the device needs to
communicate with the application server.

###### Note

When creating a service profile, you can specify that you want to use the
public network instead of your own private LoRaWAN gateway. For more
information, see [Managing LoRaWAN traffic from public networks
(Everynet)](iot-lorawan-roaming.md "iot-lorawan-roaming.md").

### Add a service profile

using the console

If you're adding a wireless device using the console as described in [Add your wireless device
specification to AWS IoT Core for LoRaWAN using the console](lorawan-end-devices-add.md#lorawan-end-device-spec-console "lorawan-end-devices-add.md#lorawan-end-device-spec-console"), after you've added
the device profile, you can add your service profile. Alternatively, you can
also add wireless devices from the [Profiles](https://console.aws.amazon.com/iot/home#/wireless/profiles "https://console.aws.amazon.com/iot/home#/wireless/profiles") page of the AWS IoT console on the
**LoRaWAN** tab.

We recommend that you leave the setting **AddGWMetaData**
enabled so that you'll receive additional gateway metadata for each payload,
such as RSSI and SNR for the data transmission.

### Add a service profile using

the API

If you're adding a wireless device using the API, you must first create
your service profile before creating the wireless device.

The following lists describe the API actions that perform the tasks
associated with adding, updating, or deleting a service profile.

###### AWS IoT Wireless API actions for service profiles

- [CreateServiceProfile](../apireference/API_CreateServiceProfile.md "../apireference/API_CreateServiceProfile.md")
- [GetServiceProfile](../apireference/API_GetServiceProfile.md "../apireference/API_GetServiceProfile.md")
- [ListServiceProfiles](../apireference/API_ListServiceProfiles.md "../apireference/API_ListServiceProfiles.md")
- [DeleteServiceProfile](../apireference/API_DeleteServiceProfile.md "../apireference/API_DeleteServiceProfile.md")

For the complete list of the actions and data types available to create
and manage AWS IoT Core for LoRaWAN resources, see the [AWS IoT Wireless API
reference](../apireference/welcome.md "../apireference/welcome.md").

###### How to use the AWS CLI to create a service profile

You can use the AWS CLI to create a service by using the [create-service-profile](../../../cli/latest/reference/iotwireless/create-service-profile.md "../../../cli/latest/reference/iotwireless/create-service-profile.md") command. The
following example creates a service profile.

```
aws iotwireless create-service-profile
```

Running this command automatically creates a service profile with an ID
that you can use when creating the wireless device. You can now create the
wireless device by using the device and service profiles.

```
{
    "Arn": "arn:aws:iotwireless:us-east-1:123456789012:ServiceProfile/12345678-a1b2-3c45-67d8-e90fa1b2c34d",
    "Id": "12345678-a1b2-3c45-67d8-e90fa1b2c34d"
}
```
