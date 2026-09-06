

# Add your device to AWS IoT Core for Amazon Sidewalk
<a name="iot-sidewalk-create-device"></a>

Before creating a wireless device, first create a device profile. Device profiles define the device capabilities and other parameters for your Sidewalk devices. A single device profile can be associated with multiple devices.

After you create a device profile, when you retrieve information about the profile, it returns a `DeviceTypeId`. When you provision your end device, you'll use this ID, the device certificates, application server public key, and the SMSN.

## How to create and add your device
<a name="iot-sidewalk-device-how"></a>

1. Create a device profile for your Sidewalk end devices. Specify a profile name to use for your Sidewalk devices as an alphanumeric string. The profile will help identify the devices to associate it with.
   + (Console) When adding your Sidewalk device, you can also create a new profile. This helps you quickly add your device to AWS IoT Core for Amazon Sidewalk and associate it with a profile.
   + (API) Use the `CreateDeviceProfile` API operation by specifying a profile name and the Sidewalk object, `sidewalk {}`. The API response will contain a profile ID and ARN (Amazon Resource Name).

1. Add your wireless device to AWS IoT Core for Amazon Sidewalk. Specify a destination name and choose the device profile that you created in the previous step. 
   + (Console) When adding your Sidewalk device, enter a destination name, and choose the profile that you created.
   + (API) Use the `CreateWirelessDevice` API operation. Specify a destination name and the ID of the device profile obtained previously.  
**Wireless device parameters**    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/iot-wireless/latest/developerguide/iot-sidewalk-create-device.html)

1. Obtain the JSON file that contains the required information for provisioning your end device.
   + (Console) Download this file from the details page of the Sidewalk device that you created.
   + (API) Use the `GetDeviceProfile` and `GetWirelessDevice` API operations to retrieve information about your device profile and wireless device. Store the API response information as JSON files, such as {{`device_profile.json`}} and {{`wireless_device.json`}}.