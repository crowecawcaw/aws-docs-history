# Add your device profile and

Sidewalk end device

This section shows how you can create a device profile. It also shows how you can
use the AWS IoT console and the AWS CLI to add your Sidewalk end device to
AWS IoT Core for Amazon Sidewalk.

## Add your Sidewalk

device (console)

To add your Sidewalk device using the AWS IoT console, go to the [Sidewalk
tab of the Devices hub](https://console.aws.amazon.com/iot/home#/wireless/devices?tab=sidewalk "https://console.aws.amazon.com/iot/home#/wireless/devices?tab=sidewalk"), choose **Provision
device**, and then perform the following steps.

![Workflow for adding, provisioning, and registering your Sidewalk device to connect to the cloud.](images/iot-sidewalk-provision-device.PNG)

1. ###### Specify device details

Specify the configuration information for your Sidewalk device.
You can also create a new device profile, or choose an existing profile
for your Sidewalk device.

    1. Specify a device name and optional description. The
     description can be up to 2,048 characters long. These fields can
     be edited after you create the device.
    2. Choose a device profile to associate with your Sidewalk
     device. If you have any existing device profiles, you can choose
     your profile. To create a new profile, choose **Create
     new profile**, and then enter a name for the
     profile.


    ###### Note

    To attach tags to your device profile, after you create
     your profile, go to the [Profiles hub](https://console.aws.amazon.com/iot/home#/wireless/profiles "https://console.aws.amazon.com/iot/home#/wireless/profiles")
     and then edit your profile to add this information.
    3. Specify the name of your destination that will route messages
     from your device to other AWS services. If you haven't already
     created a destination, go to the [Destinations
     hub](https://console.aws.amazon.com/iot/home#/wireless/destinations "https://console.aws.amazon.com/iot/home#/wireless/destinations") to create your destination. You can then choose
     that destination for your Sidewalk device. For more
     information, see [Add a destination for your
     Sidewalk end device](iot-sidewalk-qsg-destination.md "iot-sidewalk-qsg-destination.md").
    4. Choose **Next** to continue adding your
     Sidewalk device.

2. ###### Associate Sidewalk device with AWS IoT thing (Optional)

You can optionally associate your Sidewalk device to an AWS IoT
thing. IoT things are entries in the AWS IoT device registry. Things make
it easier to search and manage your devices. Associating a thing with
your device lets your device access other AWS IoT Core features.

To associate your device with a thing, choose **Automatic
thing registration**.

    1. Enter a unique name for the IoT thing that you want to
     associate your Sidewalk device. Thing names are case
     sensitive and must be unique in your AWS account and
     AWS Region.
    2. Provide any additional configurations for your IoT thing, such
     as using a thing type, or searchable attributes that can be used
     to filter from a list of things.
    3. Choose **Next** and verify the information
     about your Sidewalk device, and then choose
     **Create**.

## Add your Sidewalk device

(CLI)

To add your Sidewalk device and download the JSON files that will be
used to provision your Sidewalk device, perform the following API
operations.

###### Topics

- [Step 1: Create a device
  profile](#iot-sidewalk-profile-create "#iot-sidewalk-profile-create")
- [Step 2: Add your
  Sidewalk device](#iot-sidewalk-device-create "#iot-sidewalk-device-create")

### Step 1: Create a device

profile

To create a device profile in your AWS account, use the [`CreateDeviceProfile`](../apireference/API_CreateDeviceProfile.md "../apireference/API_CreateDeviceProfile.md") API operation or the
[`create-device-profile`](../../../cli/latest/reference/create-device-profile.md "../../../cli/latest/reference/create-device-profile.md") CLI command. When
creating your device profile, specify the name and provide any optional tags
as name-value pairs.

For example, the following command creates a device profile for your
Sidewalk devices:

```
aws iotwireless create-device-profile \
    --name `sidewalk_profile` --sidewalk {}
```

Running this command returns the Amazon Resource Name (ARN) and the ID of
the device profile as output.

```
{
    "DeviceProfileArn": "arn:aws:iotwireless:`us-east-1`:`123456789012`:DeviceProfile/`12345678-a1b2-3c45-67d8-e90fa1b2c34d`",
    "DeviceProfileId": "`12345678-a1b2-3c45-67d8-e90fa1b2c34d`"
}
```

### Step 2: Add your

Sidewalk device

To add your Sidewalk device to your account for AWS IoT Core for Amazon Sidewalk, use
the [`CreateWirelessDevice`](../apireference/API_CreateWirelessDevice.md "../apireference/API_CreateWirelessDevice.md") API operation or the
[`create-wireless-device`](../../../cli/latest/reference/create-wireless-device.md "../../../cli/latest/reference/create-wireless-device.md") CLI command. When
creating your device, specify the following parameters, in addition to an
optional name and description for your Sidewalk device.

###### Note

If you want to associate your Sidewalk device with an AWS IoT
thing, use the [`AssociateWirelessDeviceWithThing`](../apireference/API_AssociateWirelessDeviceWithThing.md "../apireference/API_AssociateWirelessDeviceWithThing.md") API
operation or the [`associate-wireless-device-with-thing`](../../../cli/latest/reference/associate-wireless-device-with-thing.md "../../../cli/latest/reference/associate-wireless-device-with-thing.md") CLI
command.

The following command shows an example of creating a Sidewalk
device:

```
aws iotwireless create-wireless-device \
     --cli-input-json "`file://device.json`"
```

The following shows the contents of the file
`device.json`.

**Contents of device.json**

```
{
  "Type": "Sidewalk",
  "Name": "`SidewalkDevice`",
  "DestinationName": "`SidewalkDestination`",
  "Sidewalk": {
    "DeviceProfileId": "`12345678-a1b2-3c45-67d8-e90fa1b2c34d`"
    }
}
```

Running this command returns the device ID and Amazon Resource Name (ARN)
as output.

```
{
    "Arn": "arn:aws:iotwireless:`us-east-1`:`123456789012`:WirelessDevice/`23456789-abcd-0123-bcde-fabc012345678`",
    "Id": `"23456789-abcd-0123-bcde-fabc012345678"`
}
```

#### (Optional) Create

your Sidewalk end device and get the Sidewalk device
location

If you want to enable location data when you create your
Sidewalk end device with AWS IoT Core for Amazon Sidewalk, enable positioning.
Replace `LocationDestination` with the
destination name to which you want to send the device location data
to.

###### Note

You must enable positioning to use the device location feature. If
you enable device location for the Sidewalk-enabled device,
your raw uplink payload won't be propagated to the destination.

```
// Add your Sidewalk device by using the device profile ID.
aws iotwireless create-wireless-device
  --type "Sidewalk"
  --name `"sidewalk_device"` \
  --description `"My Sidewalk Device Description"` \
  --destination-name `"UplinkDestination"` \
  --positioning `"Enabled"` \
  --sidewalk DeviceProfileId=`"12345678-234a-45bc-67de-e8901234f0a1"`,Positioning={DestinationName=`"LocationDestination"`}
```

###### Note

For Bluetooth Low Energy based location, AWS IoT returns location coordinates
based on the approximate location of nearby Sidewalk Gateways that are
connected to Amazon Sidewalk and have the Community Finding feature enabled.
Gateway Location Data is AWS Content and is provided to you solely for
the purpose of assisting you in locating your devices that are connected
to Amazon Sidewalk, and you must only use the data for that purpose. You must
only use and access location data via the interface and functionality
that we generally make available to you, and you must not attempt to
re-identify, reverse engineer, or re-map any Gateway location data provided
by us to you.
